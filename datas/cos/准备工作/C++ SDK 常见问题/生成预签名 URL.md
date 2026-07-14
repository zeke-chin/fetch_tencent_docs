<!-- source: https://cloud.tencent.com/document/product/436/109478 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:15:55+08:00 -->

# 生成预签名 URL

最近更新时间：2025-08-08 17:42:02


## 简介

本文介绍对象存储 COS 通过 C++ SDK 实现生成对象预签名链接的示例代码和描述。

## 注意事项

2024年1月1日后创建的桶 [不支持使用默认域名在浏览器预览文件](https://cloud.tencent.com/document/product/436/96243)，建议您配置自定义域名，详情请参见 [存储桶切换自定义域名](https://cloud.tencent.com/document/product/436/102509)。

生成预签名 URL 支持使用永久密钥或临时密钥。

获取签名/预签名函数，默认签入 Header Host；您也可以选择不签入 Header Host，但可能导致请求失败或安全漏洞。

## 相关示例

功能名称 描述 示例代码
生成预签名 URL 对象存储（Cloud Object Storage，COS）支持使用预签名 URL 进行对象的上传、下载，原理是将签名嵌入 URL 生成签名链接。[GitHub完整示例](https://github.com/tencentyun/cos-cpp-sdk-v5/blob/master/demo/object_op_demo/get_object_url_demo.cpp)

## 前期准备

### 创建 CosAPI

调用 COS 的接口之前，必须先创建一个 CosAPI 的实例。这个实例用来后续调用请求。

qcloud_cos::CosAPI InitCosAPI() {

 uint64_t appid = 12500000000;

 std::string region = "ap-guangzhou";// bucket 的地域，请参见 https://cloud.tencent.com/document/product/436/62

 std::string secret_id = "************************************"; //用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140

 std::string secret_key = "************************************"; //用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140


 qcloud_cos::CosConfig config(appid, secret_id, secret_key, region);

 qcloud_cos::CosAPI cos_tmp(config);

 return cos_tmp;

}

### 使用临时密钥创建 CosAPI

如果要使用临时密钥请求 COS，则需要用临时密钥创建 CosAPI 实例。

qcloud_cos::CosAPI InitCosAPI() {

 // 需要已经获取到临时密钥的结果：tmp_secret_id、tmp_secret_key、

 // 临时密钥的生成参见 https://cloud.tencent.com/document/product/436/14048#cos-sts-sdk

 uint64_t appid = 12500000000;

 std::string region = "ap-guangzhou";

 std::string tmp_secret_id = "************************************";

 std::string tmp_secret_key = "************************************";

 std::string tmp_token = "token";


 qcloud_cos::CosConfig config(appid, tmp_secret_id, tmp_secret_key, region);

 config.SetTmpToken(tmp_token);

 qcloud_cos::CosAPI cos_tmp(config);

 return cos_tmp;

}

## **使用案例**

### 生成预签名 URL

#### 方法原型

std::string CosAPI::GeneratePresignedUrl(const GeneratePresignedUrlReq& req)

#### 请求示例

void GeneratePresignedUrlDemo(qcloud_cos::CosAPI& cos) {

 std::string object_name = "test.txt";

 qcloud_cos::GeneratePresignedUrlReq req(bucket_name, object_name, qcloud_cos::HTTP_GET); // 可设置请求方法

 // 下方代码块可选。默认签名生效的开始时间是本地当前时间，默认有效期 60s

 {

 req.SetHttps(); // 是否为 https

 uint64_t start_time_in_s = time(NULL);

 req.SetStartTimeInSec(start_time_in_s); // 设置签名生效的开始时间

 req.SetExpiredTimeInSec(60); // 设置签名的有效期

 }

 std::string presigned_url = cos.GeneratePresignedUrl(req);

 std::cout << "===================GeneratePresignedUrl=====================" << std::endl;

 std::cout << "Presigend Url=[" << presigned_url << "]" << std::endl;

 std::cout << "============================================================" << std::endl;

}

#### 参数说明

GeneratePresignedUrlReq 成员及函数说明：

参数名称 描述 参数类型
bucket_name 存储桶名称，存储桶的命名格式为 BucketName-APPID，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83)string
object_name 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/picture.jpg` 中，对象键为 doc/picture.jpg，详情请参见 [对象键](https://cloud.tencent.com/document/product/436/13324)string
method HTTP 方法，可选：HTTP_GET、HTTP_POST、HTTP_PUT、HTTP_DELETE、HTTP_HEAD string
SetHTTPS 设置开启 HTTPS，不设置则为 HTTP 无
SetStartTimeInSec 设置签名生效的开始时间 uint64_t
SetExpiredTimeInSec 设置签名的有效期 uint64_t
SetSignHeaderHost 是否签入 Host 头部（推荐），默认 true bool

#### 返回结果说明

返回对象预签名 URL。

### 生成预签名上传 URL 并使用该 URL 上传对象

**说明：**

本样例仅用 C++ SDK 使用的网络库进行演示。

#### 请求示例

//需额外加入以下头文件

#include "cos_defines.h"

#include "Poco/Net/Context.h"

#include "Poco/Net/HTTPClientSession.h"

#include "Poco/Net/HTTPRequest.h"

#include "Poco/Net/HTTPResponse.h"

#include "Poco/Net/HTTPSClientSession.h"

#include "Poco/Net/NetException.h"

#include "Poco/StreamCopier.h"

#include "Poco/URI.h"

void GeneratePresignedUrlAndPutObjectDemo(qcloud_cos::CosAPI& cos) {

 std::string object_name = "test.txt";

 qcloud_cos::GeneratePresignedUrlReq req(bucket_name, object_name, qcloud_cos::HTTP_PUT); // 可设置请求方法

 // 下方代码块可选则是否设置。默认签名生效的开始时间是本地当前时间，默认有效期 60s

 {

 req.SetUseHttps(false); // 是否为 https

 uint64_t start_time_in_s = time(NULL);

 req.SetStartTimeInSec(start_time_in_s); // 设置签名生效的开始时间

 req.SetExpiredTimeInSec(60); // 设置签名的有效期

 }

 std::string url_str = cos.GeneratePresignedUrl(req);

 std::cout << "===================GeneratePresignedUrl=====================" << std::endl;

 std::cout << "Presigend Url=[" << url_str << "]" << std::endl;

 std::cout << "============================================================" << std::endl;

 Poco::Net::HTTPResponse res;

 int retryIndex = 0;

 while (true) {

 try {

 std::cout << "send request to [" << url_str.c_str() << "]" << std::endl;

 Poco::URI url(url_str);

 std::string path = url.getPathAndQuery();

 std::unique_ptr<Poco::Net::HTTPClientSession> session;

 session.reset(new Poco::Net::HTTPClientSession(url.getHost(), url.getPort()));

 Poco::Net::HTTPRequest req(Poco::Net::HTTPRequest::HTTP_PUT, path, Poco::Net::HTTPMessage::HTTP_1_1);

 std::istringstream is("put object with PresignedUrl");

 std::streampos pos = is.tellg();

 is.seekg(0, std::ios::end);

 req.setContentLength(is.tellg());

 is.seekg(pos);

 std::ostringstream debug_os;

 req.write(debug_os);

 std::cout << "request=[" << debug_os.str().c_str() << "]" << std::endl;

 std::ostream& os = session->sendRequest(req);

 std::streamsize copy_size = HandleStreamCopier::handleCopyStream(nullptr, is, os);

 Poco::Net::StreamSocket& ss = session->socket();

 std::istream& recv_stream = session->receiveResponse(res);

 int response_code = res.getStatus();

 // 5xx 重试3次

 if (response_code / 100 != 5 || retryIndex >= 3) {

 std::cout << "Send request over, status=" << res.getStatus() << ", reason=" << res.getReason().c_str() << std::endl;

 break;

 }

 std::cout << "will retry, retryIndex: " << retryIndex << std::endl;

 retryIndex++;

 } catch (const std::exception& ex) {

 SDK_LOG_ERR("Exception:%s, errno=%d", std::string(ex.what()).c_str(), errno);

 break;

 }

 }

}
