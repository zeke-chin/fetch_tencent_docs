<!-- source: https://cloud.tencent.com/document/product/436/127717 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:25:31+08:00 -->

# GetIndex

最近更新时间：2026-01-21 18:08:51


## 功能描述

GetIndex 请求可以确认该索引是否存在。有以下几种情况：

索引存在且有读取权限，返回 HTTP 状态码为200。

无索引读取权限，返回 HTTP 状态码为403。

索引不存在，返回 HTTP 状态码为404。

## 授权说明

将 [授权策略](https://cloud.tencent.com/document/product/598/80789) 中 action 设置为`cos:GetVectorIndex` 。查看所有 [action](https://cloud.tencent.com/document/product/436/127699)。

## 请求

#### 请求示例

POST /GetIndex HTTP/1.1

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

获取向量桶时提交 **application/json** 请求数据，需指定向量桶名字和索引名字或者使用索引资源名称。

{

 "indexQcs": "string",

 "indexName": "string",

 "vectorBucketName": "string"

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
vectorBucketName 无 向量桶名称，<BucketName-APPID>格式，例如 examplebucket-1250000000，支持小写字母、数字和 - ，长度限制3-63字符 string 否，vectorBucketName 和indexQcs 选其一
indexQcs 无 索引资源名称（QCS），例如qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000/index/exampleindex，具体资源格式说明参考 [向量索引资源](https://cloud.tencent.com/document/product/436/127699)string 否
indexName 无 索引名称，由小写字母、数字、短横线(-)、点(.)组成，首尾必须是小写字母或数字，长度限制3-63字符 string 是，仅当 indexQcs 有值时可选

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/127702) 文档。

#### 响应体

查询成功，返回 **application/json** 数据，包含索引基本信息。不同场景下的响应体请参见下方的实际案例。

{

 "index": {

 "creationTime": integer,

 "dataType": "string",

 "dimension": integer,

 "distanceMetric": "string",

 "indexQcs": "string",

 "indexName": "string",

 "metadataConfiguration": {

 "nonFilterableMetadataKeys": [ "string" ]

 },

 "vectorBucketName": "string"

 }

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型
index 无 保存 GET Index 结果的所有信息 Container
vectorBucketName 无 向量桶名称，<BucketName-APPID>格式，例如 examplebucket-1250000000，长度限制3-63字符 string

Container 节点 index 的内容：

节点名称（关键字）父节点 描述 类型
creationTime index 向量桶创建日期和时间，时间戳 integer
dataType index 向量数据类型，默认值为 float32 string
dimension index 向量维度。最小值为1，最大值为4096 integer
distanceMetric index 相似性搜索的距离度量。可选值 euclidean（欧氏距离） 或者 cosine（余弦距离）string
indexQcs index 向量索引资源名称（QCS），例如 qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000/index/exampleindex，具体资源格式说明参见 [向量索引资源](https://cloud.tencent.com/document/product/436/127699)string
indexName index 索引名称，长度限制3-63字符 string
metadataConfiguration index 元数据配置 Container

Container 节点 metadataConfiguration 的内容：

节点名称（关键字）父节点 描述 类型
nonFilterableMetadataKeys metadataConfiguration 不可用于过滤的元数据键。

数组元素：最少1个元素，最多10个元素。

key的长度限制：最小长度为1字符，最大长度为63字符。string 数组

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/127703) 文档。

## 实际案例：根据向量桶名称获取向量桶指定索引信息

### 请求

POST /GetIndex HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Sun, 26 May 2019 14:51:38 GMT

Content-Type: application/json

Content-Length: 45

Content-MD5: 1B2M2Y8AsgTpgAmY7PhCfg==

Authorization: q-sign-algorithm=sha1&q-ak= ************************************ &q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature= ****************************************

Connection: close

{

 "vectorBucketName": "examplebucket-1250000000",

 "indexName": "exampleindex"

}

### 响应

HTTP/1.1 200 OK

Content-Type: application/json

Content-Length: 228

Connection: close

Date: Tue, 28 May 2019 03:16:12 GMT

Server: tencent-cos

x-cos-request-id: NWNlY2E3ZmNfZjhjMDBiMDlfMTBjOWRfZDcz****

{

 "index": {

 "creationTime": 1735449900,

 "dataType": "float32",

 "dimension": 768,

 "distanceMetric": "cosine",

 "indexName": "exampleindex",

 "indexQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000:index/exampleindex",

 "metadataConfiguration": {

 "nonFilterableMetadataKeys": [ "examplekey1", "examplekey2" ]

 },

 "vectorBucketName": "examplebucket-1250000000"

 }

}
