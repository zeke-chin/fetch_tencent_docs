<!-- source: https://cloud.tencent.com/document/product/436/40334 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:20:30+08:00 -->

# CRC64校验

最近更新时间：2026-03-24 16:49:22


## 简介

数据在客户端和服务器间传输时可能会出现错误，COS 除了可以通过 [MD5和自定义属性](https://cloud.tencent.com/document/product/436/36427) 验证数据完整性外，还可以通过 CRC64检验码来进行数据校验。

COS 会对新上传的对象进行 CRC64计算，并将结果作为对象的属性进行存储，随后在返回的响应头部中携带 x-cos-hash-crc64ecma，该头部表示上传对象的 CRC64值，根据 [ECMA-182标准](https://www.ecma-international.org/publications-and-standards/standards/ecma-182/) 计算得到。对于 CRC64特性上线前就已经存在于 COS 的对象，COS 不会对其计算 CRC64值，所以获取此类对象时不会返回其 CRC64值。

**说明：**

CRC64（循环冗余校验64位）是一种高效的数据完整性验证算法，通过多项式除法生成64位校验值。相比传统 MD5校验，CRC64具备以下优势：

抗碰撞性更强：64位校验码空间更大，重复概率低。

计算效率更高：流式处理特性适合大文件校验，内存占用仅为常数级别。

支持片段合并：适合异步边下载边计算，节省计算时间。

行业认可度高：被 ISO、ITU-T 等国际标准广泛采用，腾讯云 COS 选用 ECMA-182标准实现。

## COS API 支持 CRC64校验

目前支持 CRC64的 API 如下：

简单上传接口

[PUT Object](https://cloud.tencent.com/document/product/436/7749) 和 [POST Object](https://cloud.tencent.com/document/product/436/14690)：用户可在返回的响应头中获得文件 CRC64校验值。

分块上传接口

[Upload Part](https://cloud.tencent.com/document/product/436/7750)：用户可以根据 COS 返回的 CRC64值与本地计算的数值进行比较验证。

[Complete Multipart Upload](https://cloud.tencent.com/document/product/436/7742)：如果每个分块都有 CRC64属性，则会返回整个对象的 CRC64值，如果某些分块不具备 CRC64值，则不返回。

执行 [Upload Part - Copy](https://cloud.tencent.com/document/product/436/8287) 时，会返回对应的 CRC64值。

执行 [PUT Object - Copy](https://cloud.tencent.com/document/product/436/10881) 时，如果源对象存在 CRC64值，则返回 CRC64，否则不返回。

执行 [HEAD Object](https://cloud.tencent.com/document/product/436/7745) 和 [GET Object](https://cloud.tencent.com/document/product/436/7753) 时，如果对象存在 CRC64，则返回。用户可以根据 COS 返回的 CRC64值和本地计算的 CRC64进行比较验证。

## 查看 COS 对象 CRC64值

### 方式一：通过 COSBrowser PC/Web 查看

[安装](https://cloud.tencent.com/document/product/436/11366) 并登录 COSBrowser PC 客户端或访问 COSbrowser Web 版本，进入存储桶后，选择对象并右键单击**详情**。在对象详情中，Headers 对应的 x-cos-hash-crc64ecma 头部值就是 CRC64校验值。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/774d5abd7de8495084ab2444b6ef65af.webp)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/774d5abd7de8495084ab2444b6ef65af.webp)

### 方式二：通过浏览器查看

在浏览器打开 DevTools 开发者工具，访问对象临时签名地址，然后在 Network 里可以看到对象的 Response Headers，对应的 x-cos-hash-crc64ecma 头部值就是当前访问对象的 CRC64校验值。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/4c1439ccbf607594079e04fdb1dca6dc.webp)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/4c1439ccbf607594079e04fdb1dca6dc.webp)

## 计算本地文件 CRC64值

### 方式一：使用 COSCLI 工具计算 CRC64值

[COSCLI](https://cloud.tencent.com/document/product/436/63143) 是腾讯云对象存储提供的客户端命令行工具。通过 COSCLI 工具，您可以通过简单的命令行指令对您 COS 中的对象（Object）实现 CRC64计算以及批量上传、下载、删除等操作。

下载工具后，可以使用`./coscli hash ./filename` 命令计算得到本地文件 CRC64校验值。Window、Linux 示例如下：

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/2dd2a6acb016257fe46aecdb92c4fb66.webp)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/2dd2a6acb016257fe46aecdb92c4fb66.webp)

### 方式二：使用 Web 页面计算 CRC64值

浏览器访问 [在线计算 CRC64](https://cos.cloud.tencent.com/samples/cos/crc64.html) 页面，单击**选择文件**，完成上传后，当前页面会在计算完成后自动显示校验值。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/10f6999cb4ac265fa6a099f91b25902b.webp)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/10f6999cb4ac265fa6a099f91b25902b.webp)

## API 接口示例

#### 分块上传响应

下面为用户发出 Upload Part 请求后得到的响应示例。x-cos-hash-crc64ecma 头部表示分块的 CRC64值，用户可以通过该值与本地计算的 CRC64值进行比较，从而校验分块完整性。

HTTP/1.1 200 OK

content-length: 0

connection: close

date: Thu, 05 Dec 2019 01:58:03 GMT

etag: "358e8c8b1bfa35ee3bd44cb3d2cc416b"

server: tencent-cos

x-cos-hash-crc64ecma: 15060521397700495958

x-cos-request-id: NWRlODY0MmJfMjBiNDU4NjRfNjkyZl80ZjZi****

#### 完成分块上传响应

下面为用户发出 Complete Multipart Upload 请求后得到的响应示例。x-cos-hash-crc64ecma 头部表示整个对象的 CRC64值，用户可以通过该值与本地计算的 CRC64值进行比较，从而校验对象完整性。

HTTP/1.1 200 OK

content-type: application/xml

transfer-encoding: chunked

connection: close

date: Thu, 05 Dec 2019 02:01:17 GMT

server: tencent-cos

x-cos-hash-crc64ecma: 15060521397700495958

x-cos-request-id: NWRlODY0ZWRfMjNiMjU4NjRfOGQ4Ml81MDEw****

[Object Content]

## SDK 使用示例

### Python SDK

下面以 Python SDK 为例演示如何校验对象，完整的示例代码如下。

**说明：**

代码基于 Python 2.7，其中 Python SDK 详细使用方式，请参见 Python SDK 的 [对象操作](https://cloud.tencent.com/document/product/436/35151) 文档。

#### 1. 初始化配置

设置用户属性，包括 SecretId、SecretKey 和 Region，并创建客户端对象。

# -*- coding=utf-8

from qcloud_cos import CosConfig

from qcloud_cos import CosS3Client

from qcloud_cos import CosServiceError

from qcloud_cos import CosClientError

import sys

import os

import logging

import hashlib

import crcmod

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 设置用户属性, 包括 SecretId, SecretKey, Region

# APPID 已在配置中移除，请在参数 Bucket 中带上 APPID。Bucket 由 BucketName-APPID 组成

secret_id = os.environ['COS_SECRET_ID'] # 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140

secret_key = os.environ['COS_SECRET_KEY'] # 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140

region = 'ap-beijing' # 替换为您的 Region, 这里以北京为例

token = None # 使用临时密钥需要传入 Token，默认为空，可不填

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token) # 获取配置对象

client = CosS3Client(config)

#### 2. 计算对象的校验值

模拟对象分块，并计算整个对象的 CRC64校验值。

OBJECT_PART_SIZE = 1024 * 1024 #模拟每个分块的大小

OBJECT_TOTAL_SIZE = OBJECT_PART_SIZE * 1 + 123 #对象的总大小

object_body = '1' * OBJECT_TOTAL_SIZE #对象内容

#计算整个对象 CRC64校验值

c64 = crcmod.mkCrcFun(0x142F0E1EBA9EA3693, initCrc=0, xorOut=0xffffffffffffffff, rev=True)

local_crc64 =str(c64(object_body.encode()))

#### 3. 初始化分块上传

#初始化分块上传

response = client.create_multipart_upload(

 Bucket='examplebucket-1250000000', #替换为您的 Bucket 名称，examplebucket 是一个举例的存储桶，1250000000 为举例的 APPID

 Key='exampleobject', #替换为您上传的对象 Key 值

 StorageClass='STANDARD', #对象的存储类型

)

#获取分块上传的 UploadId

upload_id = response['UploadId']

#### 4. 分块上传对象

分块上传对象，通过将对象切分成多个块进行上传，最多支持10000分块，每个分块大小为1MB - 5GB，最后一个分块可以小于1MB。上传分块时，需要设置每个分块的 PartNumber（编号），并计算每个分块的 CRC64值，在分块上传成功后，可以通过返回的 CRC64值与本地计算的数值进行校验。

#分块上传对象，每个分块大小为 OBJECT_PART_SIZE ，最后一个分块可能不足 OBJECT_PART_SIZE

part_list = list()

position = 0

left_size = OBJECT_TOTAL_SIZE

part_number = 0

while left_size > 0:

 part_number += 1

 if left_size >= OBJECT_PART_SIZE:

 body = object_body[position:position+OBJECT_PART_SIZE]

 else:

 body = object_body[position:]

 position += OBJECT_PART_SIZE

 left_size -= OBJECT_PART_SIZE

 local_part_crc64 = str(c64(body))#本地计算 CRC64

 response = client.upload_part(

 Bucket='examplebucket-1250000000',

 Key='exampleobject',

 Body=body,

 PartNumber=part_number,

 UploadId=upload_id,

 )

 part_crc_64 = response['x-cos-hash-crc64ecma']# 服务器返回的 CRC64

 if local_part_crc64 != part_crc_64:# 数据检验

 print 'crc64 check FAIL'

 # print('crc64 check FAIL') # Python 3.x 版本的 print 语句

 exit(-1)

 etag = response['ETag']

 part_list.append({'ETag' : etag, 'PartNumber' : part_number})

#### 5. 完成分块上传

在所有分块上传完成后，需要进行完成分块上传操作。可以通过 COS 返回的 CRC64和本地对象的 CRC64进行比较验证。

#完成分块上传

response = client.complete_multipart_upload(

 Bucket='examplebucket-1250000000', #替换为您的 Bucket 名称，examplebucket 是一个举例的存储桶，1250000000 为举例的 APPID

 Key='exampleobject', #对象的 Key 值

 UploadId=upload_id,

 MultipartUpload={ #要求每个分块的 ETag 和 PartNumber 一一对应

 'Part' : part_list

 },

)

crc64ecma = response['x-cos-hash-crc64ecma']

if crc64ecma != local_crc64:# 数据检验

 print 'check crc64 Failed'

 # print('crc64 check FAIL') # Python 3.x 版本的 print 语句

 exit(-1)

### Java SDK

上传对象，推荐使用 Java SDK 的高级接口，参见 Java SDK [对象操作](https://cloud.tencent.com/document/product/436/65935)。

#### 如何在本地计算文件的 CRC64值

String calculateCrc64(File localFile) throws IOException {

 CRC64 crc64 = new CRC64();

 try (FileInputStream stream = new FileInputStream(localFile)) {

 byte[] b = new byte[1024 * 1024];

 while (true) {

 final int read = stream.read(b);

 if (read <= 0) {

 break;

 }

 crc64.update(b, read);

 }

 }

 return Long.toUnsignedString(crc64.getValue());

}

#### 如何获得 COS 对象的 CRC64值，并与本地文件做校验

// COSClient 的创建参考：[快速入门](https://cloud.tencent.com/document/product/436/10199);

ObjectMetadata cosMeta = COSClient().getObjectMetadata(bucketName, cosFilePath);

String cosCrc64 = cosMeta.getCrc64Ecma();

String localCrc64 = calculateCrc64(localFile);

if (cosCrc64.equals(localCrc64)) {

 System.out.println("ok");

} else {

 System.out.println("fail");

}

### iOS SDK

上传对象，推荐使用高级接口上传，参见 iOS SDK [高级上传](https://cloud.tencent.com/document/product/436/46381#.E4.B8.8A.E4.BC.A0.E5.AF.B9.E8.B1.A1)。

#### 如何计算本地文件的 CRC64值

##### Objective-C 示例：

uint64_t localCrc64 = [[[NSMutableData alloc] initWithContentsOfFile:@"本地文件路径"] qcloud_crc64];

NSString *localCrc64Str = [NSString stringWithFormat:@"%llu",localCrc64];

##### Swift 示例：

let localCrc64 = NSMutableData.init(contentsOfFile: "本地文件路径")?.qcloud_crc64();

let localCrc64Str = String(format: "%llu", localCrc64 ?? 0);

#### 如何获得 COS 对象的 CRC64值, 并与本地文件做校验

##### Objective-C 示例：

// 上传完成的回调中，进行获取上传文件的 CRC64值

[request setFinishBlock:^(QCloudUploadObjectResult *result, NSError *error) {

 NSDictionary * dic = [result __originHTTPURLResponse__].allHeaderFields;

 NSString * crc64 = dic[@"x-cos-hash-crc64ecma"];

}];

##### Swift 示例：

// 上传完成的回调中，进行获取上传文件的 CRC64值

uploadRequest.setFinish { (result, error) in

 let dic = result?. __originHTTPURLResponse__ .allHeaderFields;

 let crc64 = dic?["x-cos-hash-crc64ecma"];

}

#### 下载接口校验

腾讯云 COS iOS SDK 下载接口已经支持 CRC64校验，并默认开启，用户无需手动计算。

校验过程为异步分段校验，减少大文件 CRC64校验造成的耗时。

校验失败后会重试三次，重试后还是失败则会下载失败并在失败回调中给出 CRC64校验失败的异常。

续传时会先校验本地已下载的文件是否符合 CRC64校验结果，如果不一致则重新下载，以免全部下载完才发现不一致，造成用户时间、流量的浪费。

### Android SDK

您在上传或者下载成功后，可以在响应头部中获取 CRC64值。

**注意：**

 COS Android SDK 版本需要大于等于 v5.7.5。

#### 上传请求示例

// 1. 初始化 TransferService。在相同配置的情况下，您应该复用同一个 TransferService

TransferConfig transferConfig = new TransferConfig.Builder()

 .build();

TransferService transferService = new TransferService(cosXmlService, transferConfig);

// 2. 初始化 PutObjectRequest

// 存储桶名称，由 bucketname-appid 组成，appid 必须填入，可以在 COS 控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket

String bucket = "examplebucket-1250000000";

String cosPath = "exampleobject"; //对象在存储桶中的位置标识符，即称对象键

String srcPath = "examplefilepath"; //本地文件的绝对路径

PutObjectRequest putObjectRequest = new PutObjectRequest(bucket,

 cosPath, srcPath);

// 3. 调用 upload 方法上传文件

final COSUploadTask uploadTask = transferService.upload(putObjectRequest);

uploadTask.setCosXmlResultListener(new CosXmlResultListener() {

 @Override

 public void onSuccess(CosXmlRequest request, CosXmlResult result) {

 // 上传成功，可以在这里拿到文件的 CRC64

 String crc64 = result.getHeader("x-cos-hash-crc64ecma");

 }

 // 如果您使用 kotlin 语言来调用，请注意回调方法中的异常是可空的，否则不会回调 onFail 方法，即：

 // clientException 的类型为 CosXmlClientException?，serviceException 的类型为 CosXmlServiceException?

 @Override

 public void onFail(CosXmlRequest request,

 @Nullable CosXmlClientException clientException,

 @Nullable CosXmlServiceException serviceException) {

 if (clientException != null) {

 clientException.printStackTrace();

 } else {

 serviceException.printStackTrace();

 }

 }

});

**说明：**

更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/Android/app/src/androidTest/java/com/tencent/qcloud/cosxml/cssg/CRC64Verify.java) 查看。

#### 下载请求示例

腾讯云 COS Android SDK 下载接口已经支持 CRC64校验，并默认开启，用户无需手动计算。

校验过程为异步分段校验，减少大文件 CRC64校验造成的耗时。

校验失败后会重试三次，重试后还是失败则会下载失败并在失败回调中给出 CRC64校验失败的异常。

续传时会先校验本地已下载的文件是否符合 CRC64校验结果，如果不一致则重新下载，以免全部下载完才发现不一致，造成用户时间、流量的浪费。

// 1. 初始化 TransferService。在相同配置的情况下，您应该复用同一个 TransferService

TransferConfig transferConfig = new TransferConfig.Builder()

 .build();

TransferService transferService = new TransferService(cosXmlService, transferConfig);

// 2. 初始化 GetObjectRequest

// 存储桶名称，由bucketname-appid 组成，appid必须填入，可以在COS控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket

String bucket = "examplebucket-1250000000";

String cosPath = "exampleobject"; //对象在存储桶中的位置标识符，即称对象键

String savePathDir = context.getCacheDir().toString(); //本地目录路径

//本地保存的文件名，若不填（null），则与 COS 上的文件名一样

String savedFileName = "exampleobject";

GetObjectRequest getObjectRequest = new GetObjectRequest(bucket,

 cosPath, savePathDir, savedFileName);

// 3. 调用 download 方法下载文件

final COSDownloadTask downloadTask = transferService.download(getObjectRequest);

downloadTask.setCosXmlResultListener(new CosXmlResultListener() {

 @Override

 public void onSuccess(CosXmlRequest request, CosXmlResult result) {

 // 下载成功，可以在这里拿到 COS 上的文件 CRC64

 String cosCRC64 = result.getHeader("x-cos-hash-crc64ecma");

 }

 // 如果您使用 kotlin 语言来调用，请注意回调方法中的异常是可空的，否则不会回调 onFail 方法，即：

 // clientException 的类型为 CosXmlClientException?，serviceException 的类型为 CosXmlServiceException?

 @Override

 public void onFail(CosXmlRequest request,

 @Nullable CosXmlClientException clientException,

 @Nullable CosXmlServiceException serviceException) {

 if (clientException != null) {

 clientException.printStackTrace();

 } else {

 serviceException.printStackTrace();

 }

 }

});

**说明：**

更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/Android/app/src/androidTest/java/com/tencent/qcloud/cosxml/cssg/CRC64Verify.java) 查看。

#### CRC64校验

通过 `TransferService` 进行上传和下载时，SDK 默认进行了数据校验的工作，如果您仍然希望能够自己进行 CRC64校验，可以参考如下代码。

// 1. 参考以上上传或者下载请求示例代码获取 COS 对象的 CRC64值

String cosCRC64 = "examplecoscrc64";

// 2. 计算本地文件的 CRC64

File localFile = new File("examplefilepath");

String localCRC64 = DigestUtils.getCRC64String(localFile);

// 3. 比对 localCRC64 和 cos CRC64 是否一致

if (localCRC64.equals(cosCRC64)) {

 // CRC64 对比正确

}

**说明：**

更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/Android/app/src/androidTest/java/com/tencent/qcloud/cosxml/cssg/CRC64Verify.java) 查看。

## CRC64各语言示例代码

若需要自定义 CRC64校验，我们也提供了主流语言（Node.js、Java、Go、PHP、C++、C、.NET(C#)、Android、iOS 等）的 CRC64校验示例代码。

使用示例：

Node.Js

Java

Go

Php

C++

C

.NET(C#)

Android

iOS

// 1. CRC64计算 字符串、Buffer

// 结果：11051210869376104954

crc64('123456789')

// 2. 流式计算

// 结果：11051210869376104954

const hash21 = crc64Calculator().update('123').update('456').update('789').digest();

// 3. 追加计算

// 结果：11051210869376104954

const hash3 = crc64Concat(crc64('123456'), crc64('789'), 3);

// 4. 合并计算

// // 结果：11051210869376104954

const hash4 = crc64Combine([ {hash: crc64('12'), size: 2}, {hash: crc64('345'), size: 3}, {hash: crc64('6789'), size: 4},]);

// 5. 计算文件

crc64File('your_file_path', (err, hash5) => { console.log('5.', hash5);});

// 1、计算字符串

// 结果 11051210869376104954

testString("123456789");

private static void testString(String str) {

 CRC64Calculator crc = new CRC64Calculator();

 byte[] data = str.getBytes(StandardCharsets.UTF_8);

 crc.update(data);

 System.out.printf("%s: %s\n", str, Long.toUnsignedString(crc.getVlue(),10));

}

// 2、流式计算

// 结果 11051210869376104954

private static void testStream() {

 CRC64Calculator crc = new CRC64Calculator();

 crc.update("123456".getBytes(StandardCharsets.UTF_8));

 crc.update("789".getBytes(StandardCharsets.UTF_8));

 System.out.println("流式校验123456789: " + Long.toUnsignedString(crc.getVlue(),10));

}

// CRC64合并

// 结果 11051210869376104954

private static void testCombine() {

 CRC64Calculator part1 = new CRC64Calculator();

 part1.update("123456".getBytes(StandardCharsets.UTF_8));

 long crc1 = part1.getVlue();

 CRC64Calculator part2 = new CRC64Calculator();

 part2.update("789".getBytes(StandardCharsets.UTF_8));

 long crc2 = part2.getVlue();

 long combined = combine(crc1, crc2, 3);

 System.out.println("合并结果: " + Long.toUnsignedString(combined,10));

}

// 4、计算文件

fileCRC("your_file_path")

func main() {

 // 测试字符串计算

 testCRC64("123456789", 11051210869376104954)

 testCRC64("中文", 16371802884590399230) // 需要实际测试值

 // 流式处理测试

 testStreamCRC()

 // 文件校验测试

 if crc, err := FileCRC("your_file_path"); err == nil {

 fmt.Printf("文件校验结果: %d\n", crc)

 }

 // 合并测试

 testCombineCRC()

}

func testCRC64(data string, expected uint64) {

 crc := NewCRC64().(*CRC64)

 crc.Update([]byte(data))

 result := crc.Sum64()

 fmt.Printf("%s: %d (%v)\n", data, result, result == expected)

}

func testStreamCRC() {

 crc := NewCRC64().(*CRC64)

 crc.Update([]byte("123456"))

 crc.Update([]byte("789"))

 result := crc.Sum64()

 fmt.Printf("流式校验: %d\n", result)

}

func testCombineCRC() {

 crc1 := NewCRC64().(*CRC64)

 crc1.Update([]byte("123456"))

 sum1 := crc1.Sum64()

 crc2 := NewCRC64().(*CRC64)

 crc2.Update([]byte("789"))

 sum2 := crc2.Sum64()

 combined := CombineCRC64(sum1, sum2, 3)

 fmt.Printf("合并结果: %d\n", combined)

}

// 测试文件计算

$file_result = file_crc64("your_file_path");

echo "文件 CRC: " . $file_result[0] . PHP_EOL;

// 标准测试数据

$data_crc = data_crc64("123456789");

echo "数据 CRC: " . $data_crc . PHP_EOL;

// 合并测试

$crc1 = data_crc64("123456");

$crc2 = data_crc64("789");

$combined = combine_crc64($crc1, $crc2, 3);

echo "合并结果: " . $combined . PHP_EOL;

?>

// 计算字符串

const char* test_str1 = "123456789";

CRC64_ECMA crc1;

crc1.update(test_str1, strlen(test_str1));

std::cout << "123456789: "

 << std::dec << crc1.finalize() << std::endl;

const char* test_str = "中文";

CRC64_ECMA crc;

crc.update(test_str, strlen(test_str));

std::cout << "中文: "

 << std::dec << crc.finalize() << std::endl;

// 流式计算

CRC64_ECMA stream_crc;

stream_crc.update("123456", 6);

stream_crc.update("789", 3);

std::cout << "流式校验123456789: "

 << std::dec << stream_crc.finalize() << std::endl;

// 文件校验

try {

 std::cout << "文件校验: "

 << std::dec << file_crc("your_file_path") << std::endl;

} catch (const std::exception& e) {

 std::cerr << e.what() << std::endl;

}

// 合并测试

CRC64_ECMA part1, part2;

part1.update("123456", 6);

part2.update("789", 3);

uint64_t combined = CRC64_ECMA::combine(

 part1.finalize(),

 part2.finalize(),

 3 // 第二个数据块长度

);

std::cout << "合并结果: " << std::dec << combined << std::endl;

return 0;

CRC64_CTX ctx;

// 测试字符串 "123456789"

crc64_init(&ctx);

const char *test_str1 = "123456789";

crc64_update(&ctx, test_str1, strlen(test_str1));

printf("123456789: %llu\n", (unsigned long long)crc64_final(&ctx));

// 测试中文

crc64_init(&ctx);

const char *test_str = "中文";

crc64_update(&ctx, test_str, strlen(test_str));

printf("中文: %llu\n", (unsigned long long)crc64_final(&ctx));

// 流式处理测试

crc64_init(&ctx);

crc64_update(&ctx, "123456", 6);

crc64_update(&ctx, "789", 3);

printf("流式校验123456789: %llu\n", (unsigned long long)crc64_final(&ctx));

// 文件校验测试

const char *filename = "your_file_path";

printf("文件校验 %s: %llu\n", filename, (unsigned long long)file_crc(filename));

// 合并测试

CRC64_CTX part1, part2;

crc64_init(&part1);

crc64_update(&part1, "123456", 6);

uint64_t crc1 = crc64_final(&part1);

crc64_init(&part2);

crc64_update(&part2, "789", 3);

uint64_t crc2 = crc64_final(&part2);

uint64_t combined = crc64_combine(crc1, crc2, 3);

printf("合并结果: %llu\n", (unsigned long long)combined);

// 标准测试

TestString("123456789", 11051210869376104954);

TestString("中文", 16371802884590399230); // 需要实际测试值

// 流式处理测试

TestStream();

// 文件校验测试

TestFile("your_file_path");

// 合并测试

TestCombine();

static void TestString(string data, ulong expected)

{

 CRC64Calculator crc = new CRC64Calculator();

 byte[] bytes = Encoding.UTF8.GetBytes(data);

 crc.Update(bytes);

 ulong result = crc.Final();

 Console.WriteLine($"{data}: {result} ({(result == expected ? "通过" : "失败")})");

}

static void TestStream()

{

 CRC64Calculator crc = new CRC64Calculator();

 crc.Update(Encoding.ASCII.GetBytes("123456"));

 crc.Update(Encoding.ASCII.GetBytes("789"));

 ulong result = crc.Final();

 Console.WriteLine($"流式校验: {result}");

}

static void TestFile(string path)

{

 try

 {

 ulong crc = CRC64Calculator.ComputeFile(path);

 Console.WriteLine($"文件 {path} 的 CRC64: {crc}");

 }

 catch (Exception ex)

 {

 Console.WriteLine($"文件校验失败: {ex.Message}");

 }

}

static void TestCombine()

{

 CRC64Calculator crc1 = new CRC64Calculator();

 crc1.Update(Encoding.ASCII.GetBytes("123456"));

 ulong sum1 = crc1.Final();

 CRC64Calculator crc2 = new CRC64Calculator();

 crc2.Update(Encoding.ASCII.GetBytes("789"));

 ulong sum2 = crc2.Final();

 ulong combined = CRC64Calculator.Combine(sum1, sum2, 3);

 Console.WriteLine($"合并结果: {combined}");

}

// 整体计算文件的 crc64

InputStream inputStream1 = new FileInputStream("your_file_path");

// 计算整个文件的CRC64值

long wholeFileCRC = CRC64Calculator.getCRC64(inputStream1);

System.out.println("整个文件的CRC64值: " + wholeFileCRC);

inputStream1.close();

// 分段计算文件的crc64

InputStream inputStream2 = new FileInputStream("your_file_path");

// 定义分段大小(例如1MB)

long partSize = 1024 * 1024;

long totalCRC = 0;

long totalLength = 0;

long remaining = inputStream2.available();

// 分段计算

while (remaining > 0) {

 long currentPartSize = Math.min(partSize, remaining);

 // 计算当前分段的CRC

 long partCRC = CRC64Calculator.getCRC64(inputStream2, 0, currentPartSize);

 // 合并CRC值

 totalCRC = CRC64Calculator.combineCRC64(totalCRC, partCRC, currentPartSize);

 totalLength += currentPartSize;

 remaining = inputStream2.available();

}

System.out.println("分段计算合并后的CRC64值: " + totalCRC);

inputStream2.close();

#import "QCloudCRC64Tools.h"

// 执行文件计算

uint64_t result = [QCloudCRC64Tools crc64_filePath:@"your_file_path"];

NSLog(@"文件：%llu",result);

NSString *part1 = @"123456";

NSString *part2 = @"789";

// 计算分块 CRC

uint64_t crc1 = [QCloudCRC64Tools qcloud_crc64:[part1 dataUsingEncoding:NSUTF8StringEncoding]];

uint64_t crc2 = [QCloudCRC64Tools qcloud_crc64:[part2 dataUsingEncoding:NSUTF8StringEncoding]];

// 合并 CRC

uint64_t combined = [QCloudCRC64Tools qcloud_crc64ForCombineCRC1:crc1 CRC2:crc2 length:part2.length];

NSLog(@"合并：%llu",combined);

// 计算整体 CRC

uint64_t fullCRC = [QCloudCRC64Tools qcloud_crc64:[@"123456789" dataUsingEncoding:NSUTF8StringEncoding]];

NSLog(@"fullCRC：%llu",fullCRC);

uint64_t fullCRC1 = [QCloudCRC64Tools qcloud_crc64:[@"中文" dataUsingEncoding:NSUTF8StringEncoding]];

NSLog(@"fullCRC：%llu",fullCRC1);

**说明：**

完整代码下载地址如下：

Github 地址：[单击下载](https://github.com/tencentyun/cos-demo/tree/main/crc64)

快速下载地址：[单击下载](https://cosbrowser.cloud.tencent.com/code/crc64/crc64_example.zip)
