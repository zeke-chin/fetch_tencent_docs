<!-- source: https://cloud.tencent.com/document/product/436/127715 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:25:31+08:00 -->

# CreateIndex

最近更新时间：2026-01-22 17:15:02


## 功能描述

CreateIndex 接口请求可以在指定向量桶下创建一个索引。该 API 接口不支持匿名请求，您需要使用带 Authorization 签名认证的请求才能创建新的索引。

**说明：**

每个桶最多创建100个索引。

## 授权说明

将 [授权策略](https://cloud.tencent.com/document/product/598/80789) 中 action 设置为`cos:PutVectorIndex`。查看所有 [action](https://cloud.tencent.com/document/product/436/127699)。

## 请求

#### 请求示例

POST /CreateIndex HTTP/1.1

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

创建向量桶索引时提交 **application/json** 请求数据，需指定向量桶名称或向量桶资源名称和索引名称。

{

 "vectorBucketQcs": "string",

 "vectorBucketName": "string",

 "indexName": "string",

 "dataType": "string",

 "dimension": integer,

 "distanceMetric": "string",

 "metadataConfiguration": {

 "nonFilterableMetadataKeys": [ "string" ]

 }

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
vectorBucketName 无 向量桶名称，<BucketName-APPID>格式，例如 examplebucket-1250000000，支持小写字母、数字和 - ，长度限制3-63字符 string 否，vectorBucketName、vectorBucketQcs 必选其一
vectorBucketQcs 无 向量桶资源名称（QCS），例如 qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000，具体资源格式说明参考 [向量存储桶的资源](https://cloud.tencent.com/document/product/436/127699)string 否，vectorBucketName、vectorBucketQcs 必选其一
indexName 无 索引名称，由小写字母、数字、短横线(-)、点(.)组成，首尾必须是小写字母或数字，长度限制3-63字符 string 是
dataType 无 向量数据类型，默认值为 float32 string 是
dimension 无 向量维度。最小值为1，最大值为4096 integer 是
distanceMetric 无 相似性搜索的距离度量。可选值 euclidean（欧氏距离） 或者 cosine（余弦距离）string 是
metadataConfiguration 无 元数据配置 Container 否

Container 节点 metadataConfiguration 的内容：

节点名称（关键字）父节点 描述 类型 是否必选
nonFilterableMetadataKeys metadataConfiguration 不可用于过滤的元数据键。

数组元素：最少1个元素，最多10个元素。

key 的长度限制：最小长度为1字符，最大长度为63字符。string 数组 否，metadataConfiguration 有值时必选

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/127702) 文档。

#### 响应体

创建成功，返回 **application/json** 数据，包含向量索引资源信息。

{

 "indexQcs":"string"

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型
indexQcs 无 向量索引资源名称（QCS），例如 qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000/index/exampleindex，具体资源格式说明参见 [向量索引资源](https://cloud.tencent.com/document/product/436/127699)string

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/127703) 文档。

## 实际案例：创建索引

### 请求

POST /CreateIndex HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Sun, 26 May 2019 14:51:38 GMT

Content-Type: application/json

Content-Length: 39

Content-MD5: 1B2M2Y8AsgTpgAmY7PhCfg==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature=****************************************

Connection: close

{

 "vectorBucketName": "examplebucket-1250000000",

 "vectorBucketQcs": "qcs::cosvector:ap-beijing:uid/1250000000:bucket/examplebucket-1250000000",

 "indexName": "exampleindex",

 "dataType": "float32",

 "dimension": 768,

 "distanceMetric": "euclidean",

 "metadataConfiguration": {

 "nonFilterableMetadataKeys": [ "examplekey1", "examplekey2" ]

 }

}

### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Sun, 26 May 2019 14:51:37 GMT

x-cos-request-id: NWNlYWE3ZjlfZDQyNzVkNjRfMzg1N18yNzFh****

{

 "indexQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000/index/exampleindex"

}
