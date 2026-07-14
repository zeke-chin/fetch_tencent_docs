<!-- source: https://cloud.tencent.com/document/product/436/17053 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:41:09+08:00 -->

# GET Bucket logging

最近更新时间：2025-07-24 18:30:42


## 功能描述

GET Bucket logging 用于获取源存储桶的日志配置信息。

**注意：**

只有源存储桶拥有者才可进行该请求操作。

## 请求

### 请求示例

GET /?logging HTTP 1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Authorization: Auth String

**说明：**

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，详情请参见 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；<Region> 为 COS 的可用地域，详情请参见 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

### 请求体

该请求的请求体为空。

## 响应

### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

<BucketLoggingStatus>

 <LoggingEnabled>

 <TargetBucket>examplebucket-1250000000</TargetBucket>

 <TargetPrefix>prefix</TargetPrefix>

 </LoggingEnabled>

</BucketLoggingStatus>

具体的数据内容如下：

节点名称（关键字）父节点 描述 类型
BucketLoggingStatus 无 存储桶日志状态信息 Container
LoggingEnabled BucketLoggingStatus 存储桶日志记录配置详细信息 Container
TargetBucket BucketLoggingStatus.LoggingEnabled 存放日志的目标存储桶，可以是同一个存储桶（但不推荐），或同一账户下、同一地域的存储桶 String
TargetPrefix BucketLoggingStatus.LoggingEnabled 日志存放在目标存储桶的指定路径 String

### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

### 请求

GET /?logging HTTP 1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Wed, 28 Oct 2017 21:32:00 GMT

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1484815944;32557711944&q-key-time=1484815944;32557711944&q-header-list=host&q-url-param-list=accelerate&q-signature=****************************************

### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 142

Connection: keep-alive

Date: Wed, 28 Oct 2017 21:32:00 GMT

Server: tencent-cos

x-cos-request-id: NTg4MDdlNGZfNDYyMDRlXzM0YWFf****

<BucketLoggingStatus>

 <LoggingEnabled>

 <TargetBucket>examplebucket-1250000000</TargetBucket>

 <TargetPrefix>prefix</TargetPrefix>

 </LoggingEnabled>

</BucketLoggingStatus>
