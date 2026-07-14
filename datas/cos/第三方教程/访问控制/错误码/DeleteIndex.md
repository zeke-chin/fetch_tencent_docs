<!-- source: https://cloud.tencent.com/document/product/436/127716 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:25:38+08:00 -->

# DeleteIndex

最近更新时间：2026-01-21 18:08:51


## 功能描述

DeleteIndex 接口请求用于删除指定的索引。该 API 的请求者需要对向量桶和索引有写入权限。

**注意：**

删除索引后无法恢复，请谨慎操作。

## 授权说明

将 [授权策略](https://cloud.tencent.com/document/product/598/80789) 中 action 设置为`cos:DeleteVectorIndex`。查看所有 [action](https://cloud.tencent.com/document/product/436/127699)。

## 请求

#### 请求示例

POST /DeleteIndex HTTP/1.1

Host: vectors.<Region>.coslake.com

Date: GMT Date

Content-Type: application/json

Content-Length: Content Length

Content-MD5: MD5

Authorization: Auth String

[Request Body]

**说明：**

Host: vectors.<Region>.coslake.com，<Region> 为可用地域，更多信息请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/127701) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/127701) 文档。

#### 请求体

删除索引时提交 **application/json** 请求数据，需指定向量桶名字，索引名字或者使用索引资源名称。

{

 "indexQcs": "string",

 "indexName": "string",

 "vectorBucketName": "string"

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
vectorBucketName 无 向量桶名称，<BucketName-APPID>格式，例如 examplebucket-1250000000，支持小写字母、数字和 - ，长度限制3-63字符 string 否，vectorBucketName、indexQcs 必选其一
indexQcs 无 索引资源名称（QCS），例如 qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000/index/exampleindex，具体资源格式说明参见 [向量存储桶的资源](https://cloud.tencent.com/document/product/436/127699)string 否，vectorBucketName、indexQcs 必选其一
indexName 无 索引名称，由小写字母、数字、短横线(-)、点(.)组成，首尾必须是小写字母或数字，长度限制3-63字符 string 是

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/127702) 文档。

#### 响应体

此接口响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/127703) 文档。

## 实际案例

#### 请求

POST /DeleteIndex HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Sun, 26 May 2019 14:51:38 GMT

Content-Type: application/json

Content-Length: 129

Content-MD5: 1B2M2Y8AsgTpgAmY7PhCfg==

Authorization: q-sign-algorithm=sha1&q-ak= ************************************ &q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature= ****************************************

Connection: close

{

 "vectorBucketName": "examplebucket-1250000000",

 "indexName": "exampleindex"

}

#### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Tue, 28 May 2019 03:19:14 GMT

Server: tencent-cos

x-cos-request-id: NWNlY2E4YjFfNjljMDBiMDlfMmNiZTlfZGE0****
