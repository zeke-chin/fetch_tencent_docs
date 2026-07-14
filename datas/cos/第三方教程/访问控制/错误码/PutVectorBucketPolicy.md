<!-- source: https://cloud.tencent.com/document/product/436/127711 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:25:17+08:00 -->

# PutVectorBucketPolicy

最近更新时间：2026-01-21 18:08:51


## 功能描述

PutVectorBucketPolicy 接口请求可以为向量存储桶配置访问控制策略。该 API 接口不支持匿名请求，您需要使用带 Authorization 签名认证的请求才能创建向量存储桶策略。

**说明：**

PutVectorBucketPolicy 接口是覆盖模式，新的向量存储桶策略将会覆盖旧的存储桶策略。

## 授权说明

将 [授权策略](https://cloud.tencent.com/document/product/598/80789) 中 action 设置为`cos:PutVectorBucketPolicy` 。查看所有 [action](https://cloud.tencent.com/document/product/436/127699)。

## 请求

#### 请求示例

POST /PutVectorBucketPolicy HTTP/1.1

Host: vectors.<Region>.coslake.com

Date: GMT Date

Content-Type: application/json

Content-Length: Content Length

Content-MD5: MD5

Authorization: Auth String

[Request Body]

**说明：**

Host: vectors.<Region>.coslake.com，更多信息请可参见 [公共请求头部](https://cloud.tencent.com/document/product/436/127701) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

此接口无请求参数。

#### 请求体

需指定向量桶名字或者向量桶 Qcs，以及要配置的 policy 转义得到的字符串。

{

 "policy": "string",

 "vectorBucketQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000",

 "vectorBucketName": "examplebucket-1250000000"

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
policy 无 策略字符串，一段将 json 格式的策略信息序列化之后的字符串表示，示例可参考 [访问控制](https://cloud.tencent.com/document/product/436/127699)String 是
vectorBucketName 无 向量桶名称，<BucketName-APPID>格式，例如 examplebucket-1250000000，长度限制3-63个字符 string 否, vectorBucketName、vectorBucketQcs 必选其一
vectorBucketQcs 无 向量桶资源名称（QCS），例如 qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000，具体资源格式说明参考 [向量存储桶的资源](https://cloud.tencent.com/document/product/436/127699)string 否, vectorBucketName、vectorBucketQcs 必选其一

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/127702) 文档。

#### 响应体

此接口响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/127703) 文档。

## 实际案例：配置策略

##### policy 示例

{

 "Statement": [

 {

 "Action": [

 "name/cos:DeleteVectorBucket",

 "name/cos:GetVectorBucket",

 "name/cos:PutVectorIndex",

 "name/cos:DeleteVectorIndex",

 "name/cos:GetVectorIndex",

 "name/cos:ListVectorIndexes",

 "name/cos:PutVectorBucketPolicy",

 "name/cos:GetVectorBucketPolicy",

 "name/cos:DeleteVectorBucketPolicy",

 "name/cos:PutVectors",

 "name/cos:GetVectors",

 "name/cos:DeleteVectors",

 "name/cos:ListVectors",

 "name/cos:QueryVectors"

 ],

 "Effect": "Allow",

 "Principal": {

 "qcs": [

 "qcs::cam::uin/700000000000:uin/700001234567"

 ]

 },

 "Resource": [

 "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000/*"

 ],

 "Sid": "total"

 }

 ],

 "Version": "2.0"

}

##### 请求

POST /PutVectorBucketPolicy HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Sun, 26 May 2019 14:51:38 GMT

Content-Length: 0

Authorization: q-sign-algorithm=sha1&q-ak= ************************************ &q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature= ****************************************

Connection: close

{

 "policy": "{\"Statement\":[{\"Action\":[\"name/cos:DeleteVectorBucket\",\"name/cos:GetVectorBucket\",\"name/cos:PutVectorIndex\",\"name/cos:DeleteVectorIndex\",\"name/cos:GetVectorIndex\",\"name/cos:ListVectorIndexes\",\"name/cos:PutVectorBucketPolicy\",\"name/cos:GetVectorBucketPolicy\",\"name/cos:DeleteVectorBucketPolicy\",\"name/cos:PutVectors\",\"name/cos:GetVectors\",\"name/cos:DeleteVectors\",\"name/cos:ListVectors\",\"name/cos:QueryVectors\"],\"Effect\":\"Allow\",\"Principal\":{\"qcs\":[\"qcs::cam::uin/700000000000:uin/700001234567\"]},\"Resource\":[\"qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000/*\"],\"Sid\":\"total\"}],\"Version\":\"2.0\"}",

 "vectorBucketName":"examplebucket-1250000000"

}

##### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Sun, 26 May 2019 14:51:37 GMT

X-Cos-Request-Id: NWNlYWE3ZjlfZDQyNzVkNjRfMzg1N18yNzFh****
