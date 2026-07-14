<!-- source: https://cloud.tencent.com/document/product/436/127720 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:25:49+08:00 -->

# GetVectors

最近更新时间：2026-01-21 18:08:52


## 功能描述

GetVectors 接口请求可以根据 key 获取一条或多条向量数据。

**说明：**

单次 GetVectors 请求最多可获取100条向量数据。

## 授权说明

在您进行 [策略授权](https://cloud.tencent.com/document/product/436/127699) 时，action 需要设置为`cos:GetVectors`，示例如下。

{

 "version": "2.0",

 "statement": [

 {

 "action": [

 "name/cos:GetVectors",

 ],

 "effect": "allow",

 "principal": {

 "qcs": [

 "qcs::cam::uin/700000000000:uin/700001234567"

 ]

 },

 "resource": [

 "qcs::cosvector:ap-guangzhou:uid/125000000:bucket/example-bucket-125000000/index/example-index/*"

 ],

 "sid": "example_index_action"

 }

 ]

}

向量存储桶的更多 Action，请参见 [支持的 Action](https://cloud.tencent.com/document/product/436/127699#bfe166d0-4ff7-4eab-9df8-d4a366353f9f)。

## 请求

### 请求示例

POST /GetVectors HTTP/1.1

Host: vectors.<Region>.coslake.com

Date: GMT Date

Content-Type: application/json

Content-Length: Content Length

Content-MD5: MD5

Authorization: Auth String

[Request Body]

**说明：**

Host: vectors.<Region>.coslake.com，其中 <Region> 为可用地域，更多信息请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/127701) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求参数

此接口无请求参数。

### 请求体

获取向量数据时提交 **application/json** 请求数据，您可以使用向量存储桶名称（vectorBucketName）和向量索引名称（indexName）的组合，也可以使用向量索引的资源六段式（indexQcs，详见 [向量存储桶的资源](https://cloud.tencent.com/document/product/436/127699#e344f3d8-f60a-41b6-b584-2568376934f5)），任一方式指定目标向量索引。若同时指定，则需要二者指向同一目标向量索引。

{

 "indexQcs": "string",

 "indexName": "string",

 "vectorBucketName": "string",

 "keys": [ ... ],

 "returnData": boolean,

 "returnMetadata": boolean

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
indexQcs 无 向量索引资源六段式，例如 qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000/index/exampleindex，具体资源格式说明参见 [向量存储桶的资源](https://cloud.tencent.com/document/product/436/127699)String 否
indexName 无 向量索引名称，由小写字母、数字、短横线(-)、点(.)组成，首尾必须是小写字母或数字，长度限制3-63字符 String 否，indexQcs 没有值时必选
vectorBucketName 无 向量存储桶名称，<BucketName-APPID>格式，例如 examplebucket-1250000000，支持小写字母、数字和 - ，长度限制3-63字符 String 否，indexQcs 没有值时必选
keys 无 目标向量的主键 key

参数限制：

单个 key 长度为1～1024字符

数组长度为1～100 String 数组 是
returnData 无 是否返回向量数据（默认值：false）Boolean 否
returnMetadata 无 是否返回向量元数据（默认值：false）Boolean 否

## 响应

### 响应头

该接口请求仅返回公共响应头，参见 [公共响应头部](https://cloud.tencent.com/document/product/436/127701)。

### 响应体

{

 "vectors": [

 {

 "key": "string",

 "data": { ... },

 "metadata": JSON value

 }

 ]

}

请求成功，该接口请求返回 HTTP 200状态码，并以 JSON 格式返回响应数据。

节点名称（关键字）父节点 描述 类型
vectors 无 根据传入 key 获取到的向量 GetOutputVector 数组

GetOutputVector 结构 vectors 的内容：

节点名称（关键字）父节点 描述 类型
key vectors 向量主键 String
data vectors 向量数据，根据向量索引数据类型由对应的字段承载数据 VectorData
metadata vectors 向量元数据 Json Value

VectorData 结构 data 的内容：

节点名称（关键字）父节点 描述 类型
float32 vectors.data float32 类型的向量数据 float32 数组

## 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/127703) 文档。

## 实际案例

### 案例一：获取向量数据

#### **请求**

POST /GetVectors HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Tue, 30 Dec 2025 08:46:33 GMT

Content-type: application/json

Content-Length: 45

Content-MD5: 1B2M2Y8AsgTpgAmY7PhCfg==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature=****************************************

{

 "indexName": "example-index",

 "vectorBucketName": "example-bucket-125000000",

 "keys": [ "key-1", "key-2" ],

 "returnData": true

}

#### **响应**

HTTP/1.1 200 OK

Date: Tue, 30 Dec 2025 08:46:33 GMT

Content-Type: application/json

Content-Length: 100

Connection: close

X-Cos-Request-Id: MTg4NWYxZTQ2YTNmOTMyOF*************

{

 "vectors": [

 {

 "key": "key-1",

 "data": {

 "float32": [1.0, 2.0]

 }

 },

 {

 "key": "key-2",

 "data": {

 "float32": [3.0, 4.0]

 }

 }

 ]

}

### 案例二：获取向量数据和元数据

#### **请求**

POST /GetVectors HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Tue, 30 Dec 2025 08:46:33 GMT

Content-type: application/json

Content-Length: 45

Content-MD5: 1B2M2Y8AsgTpgAmY7PhCfg==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature=****************************************

{

 "indexName": "example-index",

 "vectorBucketName": "example-bucket-125000000",

 "keys": [ "key-1", "key-2" ],

 "returnData": true,

 "returnMetadata": true

}

#### **响应**

HTTP/1.1 200 OK

Date: Tue, 30 Dec 2025 08:46:33 GMT

Content-Type: application/json

Content-Length: 100

Connection: close

X-Cos-Request-Id: MTg4NWYxZTQ2YTNmOTMyOF*************

{

 "vectors": [

 {

 "key": "key-1",

 "data": {

 "float32": [1.0, 2.0]

 },

 "metadata": {

 "color": "red",

 "count": 10

 }

 },

 {

 "key": "key-2",

 "data": {

 "float32": [3.0, 4.0]

 },

 "metadata": {

 "color": "blue",

 "count": 20

 }

 }

 ]

}
