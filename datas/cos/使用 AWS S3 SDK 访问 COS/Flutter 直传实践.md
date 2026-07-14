<!-- source: https://cloud.tencent.com/document/product/436/95265 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:19:50+08:00 -->

# Flutter 直传实践

最近更新时间：2025-09-30 14:53:42


## 简介

本文档介绍如何不依赖 SDK，用简单的代码，在 Flutter 端直传文件到对象存储（Cloud Object Storage，COS）的存储桶。

**注意：**

本文档内容基于 XML 版本的 [API](https://cloud.tencent.com/document/product/436/7751)。

## 前提条件

1. 登录 [COS 控制台](https://console.cloud.tencent.com/cos5) 并创建存储桶，得到 Bucket（存储桶名称） 和 Region（地域名称），详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。

2. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/capi)， 获取您的项目 SecretId 和 SecretKey。

## 实践步骤

整体步骤逻辑为：

1. 客户端调用服务端接口传入文件后缀，服务端根据后缀和时间戳等生成 cos key 以及直传的 url。

2. 服务端通过 STS SDK 获取临时密钥。

3. 服务端用获取到的临时密钥对直传 url 进行签名并返回 url、签名、token 等信息。

4. 客户端获取到步骤 3 中的信息后，直接发起 put 请求并携带签名、token 等 header 进行上传。

具体代码可参见 Flutter 示例（[dio](https://github.com/TencentCloud/cos-sdk-flutter-plugin/blob/main/example_direct/lib/upload_dio.dart)、[httpclient](https://github.com/TencentCloud/cos-sdk-flutter-plugin/blob/main/example_direct/lib/upload_httpclient.dart)）。

## 服务端

**注意：**

正式部署时服务端请加一层您的网站本身的权限检验。

出于安全考虑，后端获取临时密钥后生成直传 url 并直接对其进行签名，可参见 [服务端签名实践](https://cloud.tencent.com/document/product/436/118723)。

具体步骤为：

1. 通过 STS SDK 获取临时密钥。

2. 根据后缀名生成 cos key 以及直传 url相关。

3. 使用临时密钥对直传 url 进行签名并返回直传 url、签名、token 等信息。

服务端配置步骤：

1. 配置好密钥、bucket 以及 region。

var config = {

 // 获取腾讯云密钥，建议使用限定权限的子用户的密钥 https://console.cloud.tencent.com/cam/capi

 secretId: process.env.COS_SECRET_ID,

 secretKey: process.env.COS_SECRET_KEY,

 // 密钥有效期

 durationSeconds: 1800,

 // 这里填写存储桶、地域，例如：test-1250000000、ap-guangzhou

 bucket: process.env.PERSIST_BUCKET,

 region: process.env.PERSIST_BUCKET_REGION,

 // 限制的上传后缀

 extWhiteList: ['jpg', 'jpeg', 'png', 'gif', 'bmp'],

};

2. 终端执行

npm install

3. 启动服务

node app.js

到这里服务端就启动成功了，可以开始客户端的流程。

如有其他语言或自行实现可以参考以下流程：

1. 向服务端获取临时密钥，服务端首先使用固定密钥 SecretId、SecretKey 向 STS 服务获取临时密钥，得到临时密钥 tmpSecretId、tmpSecretKey、sessionToken，详情请参见 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048) 或 [cos-sts-sdk](https://github.com/tencentyun/qcloud-cos-sts-sdk) 文档。

2. 对直传 url 进行签名，生成 authorization。

3. 返回直传 url、authorization、sessionToken 等信息，客户端上传文件时将得到的签名和 sessionToken，分别放到发请求时 header 的 authorization 和 x-cos-security-token 字段里。

## 客户端（Flutter）

具体代码可参见 Flutter 示例（[dio](https://github.com/TencentCloud/cos-sdk-flutter-plugin/blob/main/example_direct/lib/upload_dio.dart)、[httpclient](https://github.com/TencentCloud/cos-sdk-flutter-plugin/blob/main/example_direct/lib/upload_httpclient.dart)）。

#### 使用 dio 网络库

1. 从服务端请求直传和签名信息。

/// 获取直传的url和签名等

/// @param ext 文件后缀 直传后端会根据后缀生成cos key

/// @return 直传url和签名等

static Future<Map<String, dynamic>> getStsDirectSign(String ext) async {

 Dio dio = Dio();

 //直传签名业务服务端url（正式环境 请替换成正式的直传签名业务url）

 //直传签名业务服务端代码示例可以参考：https://github.com/tencentyun/cos-demo/blob/main/server/direct-sign/nodejs/app.js

 //10.91.22.16为直传签名业务服务器的地址 例如上述node服务，总之就是访问到直传签名业务服务器的url

 Response response = await dio.get('http://10.91.22.16:3000/sts-direct-sign',

 queryParameters: {'ext': ext});

 if (response.statusCode == 200) {

 if (kDebugMode) {

 print(response.data);

 }

 if (response.data['code'] == 0) {

 return response.data['data'];

 } else {

 throw Exception(

 'getStsDirectSign error code: ${response.data['code']}, error message: ${response.data['message']}');

 }

 } else {

 throw Exception(

 'getStsDirectSign HTTP error code: ${response.statusCode}');

 }

}

2. 使用获取到的直传和签名信息开始上传文件

/// 上传文件

/// @param filePath 文件路径

/// @param progressCallback 进度回调

static Future<void> upload(String filePath, ProgressCallback progressCallback) async {

 String ext = path.extension(filePath).substring(1);

 Map<String, dynamic> directTransferData;

 try {

 directTransferData = await getStsDirectSign(ext);

 } catch (err) {

 if (kDebugMode) {

 print(err);

 }

 throw Exception("getStsDirectSign fail");

 }

 String cosHost = directTransferData['cosHost'];

 String cosKey = directTransferData['cosKey'];

 String authorization = directTransferData['authorization'];

 String securityToken = directTransferData['securityToken'];

 String url = 'https://$cosHost/$cosKey';

 File file = File(filePath);

 Options options = Options(

 method: 'PUT',

 headers: {

 'Content-Length': await file.length(),

 'Content-Type': 'application/octet-stream',

 'Authorization': authorization,

 'x-cos-security-token': securityToken,

 'Host': cosHost,

 },

 );

 try {

 Dio dio = Dio();

 Response response = await dio.put(url,

 data: file.openRead(),

 options: options, onSendProgress: (int sent, int total) {

 double progress = sent / total;

 if (kDebugMode) {

 print('Progress: ${progress.toStringAsFixed(2)}');

 }

 progressCallback(sent, total);

 });

 if (response.statusCode == 200) {

 if (kDebugMode) {

 print('上传成功');

 }

 } else {

 throw Exception("上传失败 ${response.statusMessage}");

 }

 } catch (error) {

 if (kDebugMode) {

 print('Error: $error');

 }

 throw Exception("上传失败 ${error.toString()}");

 }

}

#### 使用原生 Http Client 网络库

1. 从服务端请求直传和签名信息。

/// 获取直传的url和签名等

/// @param ext 文件后缀 直传后端会根据后缀生成cos key

/// @return 直传url和签名等

static Future<Map<String, dynamic>> _getStsDirectSign(String ext) async {

 HttpClient httpClient = HttpClient();

 //直传签名业务服务端url（正式环境 请替换成正式的直传签名业务url）

 //直传签名业务服务端代码示例可以参考：https://github.com/tencentyun/cos-demo/blob/main/server/direct-sign/nodejs/app.js

 //10.91.22.16为直传签名业务服务器的地址 例如上述node服务，总之就是访问到直传签名业务服务器的url

 HttpClientRequest request = await httpClient

 .getUrl(Uri.parse("http://10.91.22.16:3000/sts-direct-sign?ext=$ext"));

 HttpClientResponse response = await request.close();

 String responseBody = await response.transform(utf8.decoder).join();

 if (response.statusCode == 200) {

 Map<String, dynamic> json = jsonDecode(responseBody);

 if (kDebugMode) {

 print(json);

 }

 httpClient.close();

 if (json['code'] == 0) {

 return json['data'];

 } else {

 throw Exception(

 'getStsDirectSign error code: ${json['code']}, error message: ${json['message']}');

 }

 } else {

 httpClient.close();

 throw Exception(

 'getStsDirectSign HTTP error code: ${response.statusCode}');

 }

}

2. 使用获取到的直传和签名信息开始上传文件

/// 上传文件

/// @param filePath 文件路径

/// @param progressCallback 进度回调

static Future<void> upload(String filePath, ProgressCallback progressCallback) async {

 // 获取直传签名等信息

 String ext = path.extension(filePath).substring(1);

 Map<String, dynamic> directTransferData;

 try {

 directTransferData = await _getStsDirectSign(ext);

 } catch (err) {

 if (kDebugMode) {

 print(err);

 }

 throw Exception("getStsDirectSign fail");

 }

 String cosHost = directTransferData['cosHost'];

 String cosKey = directTransferData['cosKey'];

 String authorization = directTransferData['authorization'];

 String securityToken = directTransferData['securityToken'];

 String url = 'https://$cosHost/$cosKey';

 File file = File(filePath);

 int fileSize = await file.length();

 HttpClient httpClient = HttpClient();

 HttpClientRequest request = await httpClient.putUrl(Uri.parse(url));

 request.headers.set('Content-Type', 'application/octet-stream');

 request.headers.set('Content-Length', fileSize.toString());

 request.headers.set('Authorization', authorization);

 request.headers.set('x-cos-security-token', securityToken);

 request.headers.set('Host', cosHost);

 request.contentLength = fileSize;

 Stream<List<int>> stream = file.openRead();

 int bytesSent = 0;

 stream.listen(

 (List<int> chunk) {

 bytesSent += chunk.length;

 double progress = bytesSent / fileSize;

 if (kDebugMode) {

 print('Progress: ${progress.toStringAsFixed(2)}');

 }

 progressCallback(bytesSent, fileSize);

 request.add(chunk);

 },

 onDone: () async {

 HttpClientResponse response = await request.close();

 if (response.statusCode == 200) {

 if (kDebugMode) {

 print('上传成功');

 }

 } else {

 throw Exception("上传失败 $response");

 }

 },

 onError: (error) {

 if (kDebugMode) {

 print('Error: $error');

 }

 throw Exception("上传失败 ${error.toString()}");

 },

 cancelOnError: true,

 );

}

## 相关文档

如果您有更丰富的接口调用需求，请参见 [Flutter SDK](https://cloud.tencent.com/document/product/436/86294) 。
