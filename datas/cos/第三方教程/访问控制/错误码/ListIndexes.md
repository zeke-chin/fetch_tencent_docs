<!-- source: https://cloud.tencent.com/document/product/436/127729 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:25:43+08:00 -->

# ListIndexes

最近更新时间：2026-01-21 18:08:51


## 功能描述

ListIndexes 接口是用来查询请求者名下，对应向量桶的所有索引列表。

## 授权说明

将 [授权策略](https://cloud.tencent.com/document/product/598/80789) 中 action 设置为`cos:ListVectorIndexes` 。查看所有 [action](https://cloud.tencent.com/document/product/436/127699)。

## 请求

#### 请求示例

POST /ListIndexes HTTP/1.1

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

遍历索引时提交 **application/json** 请求数据，必须指定向量桶名称或者向量桶资源名称。

{

 "maxResults": integer,

 "nextToken": "string",

 "prefix": "string",

 "vectorBucketQcs": "string",

 "vectorBucketName": "string"

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
maxResults 无 响应中要返回的向量桶索引的最大数量。最小值1，最大值500。默认值100 integer 否
nextToken 无 上一个分页标记。最小长度为1，最大长度为512。默认不填则从头开始遍历 string 否
prefix 无 将响应限制为以指定索引名称前缀开头的向量桶索引。最小长度为1，最大长度为63 string 否
vectorBucketName 无 向量桶名称，<BucketName-APPID>格式，例如 examplebucket-1250000000，支持小写字母、数字和 - ，长度限制3-63字符 string 否，vectorBucketName 和vectorBucketQcs 选其一
vectorBucketQcs 无 向量桶资源名称（QCS），例如 qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000，具体资源格式说明参考 [向量存储桶的资源](https://cloud.tencent.com/document/product/436/127699)string 否

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/127702) 文档。

#### 响应体

查询成功，返回 **application/json** 数据，包含所有向量桶下的索引列表。

{

 "indexes": [

 {

 "creationTime": integer,

 "indexQcs": "string",

 "indexName": "string",

 "vectorBucketName": "string"

 }

 ],

 "nextToken": "string"

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型
nextToken 无 上一个分页标记。最小长度为1，最大长度为512 string
indexes 无 返回具体索引内容 Container

Container 节点 indexes 的内容：

节点名称（关键字）父节点 描述 类型
creationTime indexes 索引创建日期和时间，时间戳 integer
vectorBucketName indexes 向量桶名称，<BucketName-APPID>格式，例如 examplebucket-1250000000，长度限制3-63个字符 string
indexQcs indexes 索引资源名称（QCS），例如 qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000/index/exampleindex string
indexName indexes 索引名称，长度限制3-63个字符 string

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/127703) 文档。

## 实际案例

### 案例一：查询向量桶的所有索引列表

#### 请求

POST /ListIndexes HTTP/1.1

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

Content-Length: 805

Connection: close

Date: Fri, 24 May 2019 11:59:51 GMT

Server: tencent-cos

x-cos-request-id: NWNlN2djYjdfOGFiMjM1MGFfNTVjMl8zMmI1****

{

 "indexes": [

 {

 "creationTime": 1735449900,

 "indexName": "exampleindex1",

 "indexQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000:index/exampleindex1",

 "vectorBucketName": "examplebucket-1250000000"

 },

 {

 "creationTime": 1731657600,

 "indexName": "exampleindex2",

 "indexQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000:index/exampleindex2",

 "vectorBucketName": "examplebucket-1250000000"

 },

 {

 "creationTime": 1725955200,

 "indexName": "exampleindex3",

 "indexQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000:index/exampleindex3",

 "vectorBucketName": "examplebucket-1250000000"

 }

 ],

 "nextToken": "MjAyNS0xMi0zMFQwMTozNTowMFo7aW5kZXhfcHJvZHVjdF9yZWM="

}

### 案例二：指定参数翻页查询向量桶索引

#### 请求

POST /ListIndexes HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Sun, 26 May 2019 14:51:38 GMT

Content-Type: application/json

Content-Length: 45

Content-MD5: 1B2M2Y8AsgTpgAmY7PhCfg==

Authorization: q-sign-algorithm=sha1&q-ak= ************************************ &q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature= ****************************************

Connection: close

{

 "vectorBucketName": "examplebucket-1250000000",

 "maxResults": 2,

 "nextToken": "eyJpZCI6MTIzNDU2Nzg5MCwibGFzdFVwZGF0ZWAwOjAwWiJ9",

 "prefix": "exampleindex"

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

 "indexes": [

 {

 "creationTime": 1731657600,

 "indexName": "exampleindex2",

 "indexQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000:index/exampleindex2",

 "vectorBucketName": "examplebucket-1250000000"

 },

 {

 "creationTime": 1725955200,

 "indexName": "exampleindex3",

 "indexQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000:index/exampleindex3",

 "vectorBucketName": "examplebucket-1250000000"

 }

 ],

 "nextToken": "MjAyNS0xMi0zMFQwMTozNTowMFo7aW5kZXhfcHJvZHVjdF9yZWM="

}
