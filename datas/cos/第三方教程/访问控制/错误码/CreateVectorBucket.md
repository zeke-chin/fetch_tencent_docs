<!-- source: https://cloud.tencent.com/document/product/436/127725 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:24:59+08:00 -->

# CreateVectorBucket

最近更新时间：2026-01-21 18:08:51


## 功能描述

CreateVectorBucket 接口请求可以在指定账号下创建一个地域的向量存储桶。该 API 接口不支持匿名请求，您需要使用带 Authorization 签名认证的请求才能创建新的向量桶 。创建向量桶的用户默认成为向量桶的持有者。

**说明：**

单个主账号在单个地域最多创建100个向量桶。

## 授权说明

将 [授权策略](https://cloud.tencent.com/document/product/598/80789) 中 action 设置为 `cos:PutVectorBucket`。查看所有 [action](https://cloud.tencent.com/document/product/436/127699)。

## 请求

#### 请求示例

POST /CreateVectorBucket HTTP/1.1

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

创建向量桶时提交 **application/json** 请求数据，需指定向量桶名字。默认不加密，加密需要显式设置 encryptionConfiguration 并指定 sseType。

{

 "vectorBucketName": "string",

 "encryptionConfiguration": {

 "sseType": "string"

 }

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
vectorBucketName 无 向量桶名称，<BucketName-APPID>格式，例如 examplebucket-1250000000，支持小写字母、数字和 - ，长度限制为3-63个字符 string 是
encryptionConfiguration 无 向量桶服务端加密方式，仅支持 SSE-COS Container 否

**Container 节点**encryptionConfiguration**的内容：**

节点名称（关键字）父节点 描述 类型 是否必选
sseType encryptionConfiguration 向量桶服务端加密类型，仅支持 AES256 string 是（当且仅当 encryptionConfiguration 存在时）

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/127702) 文档。

#### 响应体

创建成功，返回 **application/json** 数据，包含向量桶信息。

{

 "vectorBucketQcs": "string"

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型
vectorBucketQcs 无 向量桶资源名称（QCS），例如 qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000，具体资源格式说明参见 [向量存储桶的资源](https://cloud.tencent.com/document/product/436/127699)string

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/127703) 文档。

## 实际案例

### 案例一：创建向量桶

#### 请求

POST /CreateVectorBucket HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Sun, 26 May 2019 14:51:38 GMT

Content-Type: application/json

Content-Length: 39

Content-MD5: 1B2M2Y8AsgTpgAmY7PhCfg==

Authorization: q-sign-algorithm=sha1&q-ak= ************************************ &q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature= ****************************************

Connection: close

{

 "vectorBucketName": "examplebucket-1250000000"

}

#### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Sun, 26 May 2019 14:51:37 GMT

Server: tencent-cos

x-cos-request-id: NWNlYWE3ZjlfZDQyNzVkNjRfMzg1N18yNzFh****

{

 "vectorBucketQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000"

}

### 案例二：创建 SSE-COS 加密向量桶

#### 请求

POST /CreateVectorBucket HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Fri, 14 Jun 2019 13:48:59 GMT

Content-Type: application/json

Content-Length: 104

Content-MD5: 7TvS8AsgTpgAmY7PhCfg==

Authorization: q-sign-algorithm=sha1&q-ak= ************************************ &q-sign-time=1560520139;1560527339&q-key-time=1560520139;1560527339&q-header-list=content-length;date;host;x-cos-acl;x-cos-grant-read-acp;x-cos-grant-write&q-url-param-list=&q-signature= ****************************************

Connection: close

{

 "vectorBucketName": "examplebucket-1250000000",

 "encryptionConfiguration": {

 "sseType": "AES256"

 }

}

#### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Fri, 14 Jun 2019 13:49:00 GMT

Server: tencent-cos

x-cos-request-id: NWQwM2E1Y2NfZjBhODBiMDlfOTM1YV83NDRi****

{

 "vectorBucketQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000"

}
