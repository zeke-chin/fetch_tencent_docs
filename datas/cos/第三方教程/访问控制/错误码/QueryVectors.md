<!-- source: https://cloud.tencent.com/document/product/436/127723 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:26:02+08:00 -->

# QueryVectors

最近更新时间：2026-01-21 18:08:52


## 功能描述

QueryVectors 接口请求可以根据指定查询向量在向量索引中执行近似最近邻搜索（Approximate Nearest Neighbor，ANN）查询，依据向量索引所指定的距离度量方式检索并返回结果。

## 授权说明

在您进行 [策略授权](https://cloud.tencent.com/document/product/436/127699) 时，action 需要设置为`cos:QueryVectors`，示例如下。

{

 "version": "2.0",

 "statement": [

 {

 "action": [

 "name/cos:QueryVectors"

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

POST /QueryVectors HTTP/1.1

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

{

 "indexQcs": "string",

 "indexName": "string",

 "vectorBucketName": "string"，

 "queryVector": { ... },

 "topK": int,

 "filter": JSON value

 "returnData": boolean,

 "returnMetadata": boolean

}

查询向量时提交 **application/json** 请求数据。您可以使用向量存储桶名称（vectorBucketName）和向量索引名称（indexName）的组合，也可以使用向量索引的资源六段式（indexQcs，详见[向量存储桶的资源](https://cloud.tencent.com/document/product/436/127699#e344f3d8-f60a-41b6-b584-2568376934f5)），任一方式指定目标向量索引。若同时指定，则需要二者指向同一目标向量索引。

节点名称（关键字）父节点 描述 类型 是否必选
indexQcs 无 向量索引资源六段式，例如 qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000/index/exampleindex，具体资源格式说明参见 [向量存储桶的资源](https://cloud.tencent.com/document/product/436/127699)String 否
indexName 无 向量索引名称，由小写字母、数字、短横线(-)、点(.)组成，首尾必须是小写字母或数字，长度限制3-63字符 String 否，indexQcs 没有值时必选
vectorBucketName 无 向量存储桶名称，<BucketName-APPID>格式，例如 examplebucket-1250000000，支持小写字母、数字和 - ，长度限制3-63字符 String 否，indexQcs 没有值时必选
queryVector 无 查询向量，输入向量的维度和数据类型必须与创建向量索引时所指定的相匹配 VectorData 是
topK 无 查询返回的近似最近邻搜索结果向量数目

参数限制：取值范围为1～30 Int 是
filter 无 查询向量时的预过滤器 Json Value 否
returnData 无 是否返回向量数据（默认值：false）Boolean 否
returnMetadata 无 是否返回向量元数据（默认值：false）Boolean 否
returnDistance 无 是否返回结果向量和查询向量的相似度距离（默认值：false）Boolean 否

VectorData 结构 queryVector 的内容：

节点名称（关键字）父节点 描述 类型 是否必选
float32 queryVector float32 类型的向量数据 float32 数组 是

### 元数据过滤

在写入向量时附带的可过滤的元数据支持您通过设定过滤条件对向量搜索结果进行过滤。通过传入filter，QueryVectors 接口请求可以在执行向量搜索前首先进行预过滤，仅对符合过滤条件的向量执行搜索。

元数据过滤支持以下操作符。

操作符 支持输入类型 描述
$eq Int、Float、String、Boolean 单个基本类型值的精确匹配

与数组类型元数据值进行比较时，若输入值与数组中的任一元素匹配，则视为符合条件
$ne Int、Float、String、Boolean 不等于
$gt Int、Float 大于
$gte Int、Float 大于或等于
$lt Int、Float 小于
$lte Int、Float 小于或等于
$in 基本类型（Int、Float、String、Boolean）的非空数组 匹配数组中的任何值
$nin 基本类型（Int、Float、String、Boolean）的非空数组 不匹配数组中的任何值
$exists Boolean true：检查字段是否存在

false：检查字段是否不存在
$and 过滤条件的非空数组 多个条件的逻辑 AND
$or 过滤条件的非空数组 多个条件的逻辑 OR

#### 示例

**示例一：精确匹配**

// 精确匹配元数据字段“color”等于“red”的向量

**{********"color"****:********{********"**$eq**"****:********"red"********}********}**

当未指定操作符时，默认使用`$eq`操作符。因此，以上精确匹配条件语句等效于以下简化语句：

// 等效于使用$eq操作符，简化写法

**{********"color"****:********"red"********}**

**示例二：数值比较**

// 匹配元数据字段“score”大于90.0的向量

**{********"score"****:********{********"**$gt**"****:********90.0********}********}**

// 匹配元数据字段“count”小于或等于10的向量

**{********"count"****:********{********"**$lte**"****:********10********}********}**

**示例三：数组元素匹配**

// 匹配元数据字段“color”值为“red”或“blue”的向量

**{********"color"****:********{********"**$in**"****:********[********"red"****,********"blue"********]********}********}**

// 匹配元数据字段“count”值不为10且不为20的向量

**{********"count"****:********{********"**$nin**"****:********[********10****,********20********]********}********}**

**示例四：存在性检查**

// 匹配存在“color”元数据字段的向量

**{********"color"****:********{********"**$exists**"****:********true********}********}**

// 匹配不存在“color”元数据字段的向量

**{********"color"****:********{********"**$exists**"****:********false********}********}**

**示例五：逻辑组合**

// 匹配同时满足“color”为“red”且“score”大于90.0的向量

**{********"**$and**"****:********[******{ "color": { "$eq": "red" } }, { "score": { "$gt": 90.0 } }******]********}**

## 响应

### 响应语法

HTTP/1.1 200 OK

Date: Tue, 30 Dec 2025 08:46:33 GMT

X-Cos-Request-Id: MTg4NWYxZTQ2YTNmOTMyOF*************

{

 "vectors": [

 {

 "key": "string",

 "data": { ... },

 "metadata": JSON value,

 "distance": float

 }

 ]

}

### 响应头

该接口请求仅返回公共响应头，参见 [公共响应头部](https://cloud.tencent.com/document/product/436/127701)。

### 响应体

请求成功，该接口请求返回HTTP 200状态码，并以JSON格式返回响应数据。

节点名称（关键字）父节点 描述 类型
vectors 无 根据传入key获取到的向量 QueryOutputVector 数组

QueryOutputVector 结构 vectors 的内容：

节点名称（关键字）父节点 描述 类型
key vectors 向量主键 String
data vectors 向量数据，根据向量索引数据类型由对应的字段承载数据 VectorData
metadata vectors 向量元数据 Json Value
distance vectors 结果向量与查询向量之间的相似度距离 Float

VectorData 结构 data 的内容：

节点名称（关键字）父节点 描述 类型
float32 vectors.data float32 类型的向量数据 float32 数组

## 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/127703) 文档。

## 实际案例

### 案例一：搜索向量数据

#### **请求**

POST /QueryVectors HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Tue, 30 Dec 2025 08:46:33 GMT

Content-type: application/json

Content-Length: 45

Content-MD5: 1B2M2Y8AsgTpgAmY7PhCfg==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature=****************************************

{

 "indexName": "example-index",

 "vectorBucketName": "example-bucket-125000000",

 "queryVector": {

 "float32": [1.0, 2.0]

 },

 "topK": 2,

 "returnData": true,

 "returnMetadata": true,

 "returnDistance": true

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

 },

 "distance": 0.0

 },

 {

 "key": "key-2",

 "data": {

 "float32": [3.0, 4.0]

 },

 "metadata": {

 "color": "blue",

 "count": 20

 },

 "distance": 8.0

 }

 ]

}

### 案例二：过滤并搜索向量数据

#### **请求**

POST /QueryVectors HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Tue, 30 Dec 2025 08:46:33 GMT

Content-type: application/json

Content-Length: 45

Content-MD5: 1B2M2Y8AsgTpgAmY7PhCfg==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature=****************************************

{

 "indexName": "example-index",

 "vectorBucketName": "example-bucket-125000000",

 "queryVector": {

 "float32": [1.0, 2.0]

 },

 "topK": 2,

 "filter": { "color": { "$eq": "red" } },

 "returnData": true,

 "returnMetadata": true,

 "returnDistance": true

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

 },

 "distance": 0.0

 },

 ]

}
