<!-- source: https://cloud.tencent.com/document/product/436/127726 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:25:05+08:00 -->

# GetVectorBucket

最近更新时间：2026-01-21 18:08:51


## 功能描述

GetVectorBucket 请求可以确认该向量桶是否存在，如果配置了加密配置也会返回对应服务端加密类型。有以下几种情况：

存储桶存在且有读取权限，返回 HTTP 状态码为200。

无存储桶读取权限，返回 HTTP 状态码为403。

存储桶不存在，返回 HTTP 状态码为404。

## 授权说明

将 [授权策略](https://cloud.tencent.com/document/product/598/80789) 中 action 设置为 `cos:GetVectorBucket` 。查看所有 [action](https://cloud.tencent.com/document/product/436/127699)。

## 请求

#### 请求示例

POST /GetVectorBucket HTTP/1.1

Host: vectors.<Region>.coslake.com

Date: GMT Date

Content-Type: application/json

Content-Length: Content Length

Content-MD5: MD5

Authorization: Auth String

[Request Body]

**说明：**

Host: vectors.<Region>.coslake.com，<Region> 为可用地域，可参见 [公共请求头部](https://cloud.tencent.com/document/product/436/127701) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/127701) 文档。

#### 请求体

获取向量桶时提交 **application/json** 请求数据，需指定向量桶名字，或者使用向量桶资源名称，两者必选其一。

{

 "vectorBucketQcs": "string",

 "vectorBucketName": "string"

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
vectorBucketName 无 向量桶名称，<BucketName-APPID>格式，例如 examplebucket-1250000000，长度限制3-63个字符 string 否, vectorBucketName、vectorBucketQcs 必选其一
vectorBucketQcs 无 向量桶资源名称（QCS），例如 qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000，具体资源格式说明参考 [向量存储桶的资源](https://cloud.tencent.com/document/product/436/127699)string 否, vectorBucketName、vectorBucketQcs 必选其一

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/127702) 文档。

#### 响应体

查询成功，返回 **application/json** 数据，包含向量桶基本信息。不同场景下的响应体请参见下方的实际案例。

{

 "vectorBucket": {

 "creationTime": integer,

 "encryptionConfiguration": {

 "sseType": "string"

 },

 "vectorBucketQcs": "string",

 "vectorBucketName": "string"

 }

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型
vectorBucket 无 包含 GET Vector Bucket 结果的所有信息 Container

Container 节点 vectorBucket 的内容**：**

节点名称（关键字）父节点 描述 类型
creationTime vectorBucket 向量桶创建日期和时间，时间戳 integer
encryptionConfiguration vectorBucket 向量桶服务端加密方式，仅支持 SSE-COS Container
vectorBucketQcs vectorBucket 向量桶资源名称（QCS），例如qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000，具体资源格式说明参考 [向量存储桶的资源](https://cloud.tencent.com/document/product/436/127699)string
vectorBucketName vectorBucket 向量桶名称，<BucketName-APPID>格式，例如 examplebucket-1250000000 string

Container 节点 encryptionConfiguration 的内容**：**

节点名称（关键字）父节点 描述 类型
sseType encryptionConfiguration 向量桶服务端加密类型，仅支持AES256 string

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/127703) 文档。

## 实际案例

#### 案例：根据向量桶名称获取向量桶

#### 请求

POST /GetVectorBucket HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Sun, 26 May 2019 14:51:38 GMT

Content-Type: application/json

Content-Length: 45

Content-MD5: 1B2M2Y8AsgTpgAmY7PhCfg==

Authorization: q-sign-algorithm=sha1&q-ak= ************************************ &q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature= ****************************************

Connection: close

{

 "vectorBucketName": "examplebucket-1250000000"

}

#### 响应

HTTP/1.1 200 OK

Content-Type: application/json

Content-Length: 228

Connection: close

Date: Tue, 28 May 2019 03:16:12 GMT

Server: tencent-cos

x-cos-request-id: NWNlY2E3ZmNfZjhjMDBiMDlfMTBjOWRfZDcz****

{

 "vectorBucket": {

 "creationTime": 1735445700,

 "encryptionConfiguration": {

 "sseType": "AES256"

 },

 "vectorBucketQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000",

 "vectorBucketName": "examplebucket-1250000000"

 }

}

#### 案例二：根据资源QCS获取向量桶

#### 请求

POST /GetVectorBucket HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Sun, 26 May 2019 14:51:38 GMT

Content-Type: application/json

Content-Length: 54

Content-MD5: 1B2M2Y8AsgTpgAmY7PhCfg==

Authorization: q-sign-algorithm=sha1&q-ak= ************************************ &q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature= ****************************************

Connection: close

{

 "vectorBucketQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000"

}

#### 响应

HTTP/1.1 200 OK

Content-Type: application/json

Content-Length: 228

Connection: close

Date: Tue, 28 May 2019 03:16:12 GMT

Server: tencent-cos

x-cos-request-id: NWNlY2E3ZmNfZjhjMDBiMDlfMTBjOWRfZDcz****

{

 "vectorBucket": {

 "creationTime": 1735445700,

 "encryptionConfiguration": {

 "sseType": "AES256"

 },

 "vectorBucketQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000",

 "vectorBucketName": "examplebucket-1250000000"

 }

}
