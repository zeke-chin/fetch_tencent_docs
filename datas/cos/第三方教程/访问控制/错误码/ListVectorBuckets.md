<!-- source: https://cloud.tencent.com/document/product/436/127727 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:25:09+08:00 -->

# ListVectorBuckets

最近更新时间：2026-01-21 18:08:51


## 功能描述

ListVectorBuckets 接口是用来查询请求者名下全地域的向量存储桶列表。

## 授权说明

将 [授权策略](https://cloud.tencent.com/document/product/598/80789) 中 action 设置为`cos:ListVectorBuckets` 。查看所有 [action](https://cloud.tencent.com/document/product/436/127699)。

## 请求

#### 请求示例

**示例一：不携带请求体**

POST /ListVectorBuckets HTTP/1.1

Host: vectors.<Region>.coslake.com

Date: GMT Date

Content-Type: application/json

Content-Length: 0

Authorization: Auth String

**示例二：携带请求体**

POST /ListVectorBuckets HTTP/1.1

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

ListVectorBuckets 可以请求任意地域。获取结果为所有地域的存储向量桶排序结果。

#### 请求参数

此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/127701) 文档。

#### 请求体

遍历向量桶时提交 **application/json** 请求数据，本接口支持可选请求体。若不携带请求体，则采用默认参数从头开始遍历向量存储桶列表。若需指定分页或前缀过滤，可携带如下格式的 json 请求体。

{

 "maxResults": integer,

 "nextToken": "string",

 "prefix": "string"

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
maxResults 无 响应中要返回的向量桶的最大数量。最小值1，最大值500。默认值100。integer 否
nextToken 无 上一个分页标记。最小长度为1，最大长度为512。默认不填时认为从头开始遍历。string 否
prefix 无 将响应限制为以指定向量桶名称前缀开头的向量桶。最小长度为1，最大长度为63。string 否

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/127702) 文档。

#### 响应体

查询成功，返回 **application/json** 数据，包含所有地域下的向量桶列表。

{

 "nextToken": "string",

 "vectorBuckets": [

 {

 "creationTime": integer,

 "vectorBucketQcs": "string",

 "vectorBucketName": "string"

 }

 ]

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型
nextToken 无 上一个分页标记。最小长度为1，最大长度为512 string
vectorBuckets 无 返回具体向量内容 Container

Container 节点 vectorBuckets 的内容：

节点名称（关键字）父节点 描述 类型
creationTime vectorBucket 向量桶创建日期和时间，时间戳。integer
vectorBucketQcs vectorBucket 向量桶资源名称（QCS），例如qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000，具体资源格式说明参考 [向量存储桶的资源](https://cloud.tencent.com/document/product/436/127699) 。string
vectorBucketName vectorBucket 向量桶名称，<BucketName-APPID>格式，例如 examplebucket-1250000000。string

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/127703) 文档。

## 实际案例

#### 案例一：查询所有向量桶列表

#### 请求

POST /ListVectorBuckets HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Fri, 24 May 2019 11:59:50 GMT

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1558699190;1558706390&q-key-time=1558699190;1558706390&q-header-list=date;host&q-url-param-list=&q-signature=****************************************

Connection: close

#### 响应

HTTP/1.1 200 OK

Content-Type: application/json

Content-Length: 805

Connection: close

Date: Fri, 24 May 2019 11:59:51 GMT

Server: tencent-cos

x-cos-request-id: NWNlN2RjYjdfOGFiMjM1MGFfNTVjMl8zMmI1****

{

 "nextToken": "MjAwfDEwfDkudHh0fDF8MXx8MTY4NTUzOTIwMA==",

 "vectorBuckets": [

 {

 "creationTime": 1735449000,

 "vectorBucketName": "examplebucket1-1250000000",

 "vectorBucketQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket1-1250000000"

 },

 {

 "creationTime": 1732924800,

 "vectorBucketName": "examplebucket2-1250000000",

 "vectorBucketQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket2-1250000000"

 },

 {

 "creationTime": 1727740800,

 "vectorBucketName": "examplebucket3-1250000000",

 "vectorBucketQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket3-1250000000"

 }

 ]

}

#### 案例二：指定参数翻页查询

#### 请求

POST /ListVectorBuckets HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Sun, 26 May 2019 14:51:38 GMT

Content-Type: application/json

Content-Length: 45

Content-MD5: 1B2M2Y8AsgTpgAmY7PhCfg==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature=****************************************

Connection: close

{

 "maxResults": 2,

 "nextToken": "eyJpZCI6MTIzNDU2Nzg5MCwibGFzdFVwZGF0ZWAwOjAwWiJ9",

 "prefix": "examplebucket"

}

#### 响应

HTTP/1.1 200 OK

Content-Type: application/json

Content-Length: 805

Connection: close

Date: Fri, 24 May 2019 11:59:51 GMT

Server: tencent-cos

x-cos-request-id: NWNlN2RjYjdfOGFiMjM1MGFfNTVjMl8zMmI1****

{

 "nextToken": "MjAwfDEwfDkudHh0fDF8MXx8MTY4NTUzOTIwMA",

 "vectorBuckets": [

 {

 "creationTime": 1735449000,

 "vectorBucketName": "examplebucket1-1250000000",

 "vectorBucketQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket1-1250000000"

 },

 {

 "creationTime": 1732924800,

 "vectorBucketName": "examplebucket2-1250000000",

 "vectorBucketQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket2-1250000000"

 }

 ]

}
