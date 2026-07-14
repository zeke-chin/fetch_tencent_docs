<!-- source: https://cloud.tencent.com/document/product/436/127712 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:25:22+08:00 -->

# GetVectorBucketPolicy

最近更新时间：2026-01-21 18:08:51


## 功能描述

GetVectorBucketPolicy 接口请求可以查询当前向量存储桶配置的访问控制策略。该 API 接口不支持匿名请求，您需要使用带 Authorization 签名认证的请求才能查询向量存储桶策略。

## 授权说明

将 [授权策略](https://cloud.tencent.com/document/product/598/80789) 中 action 设置为`cos:GetVectorBucketPolicy` 。查看所有 [action](https://cloud.tencent.com/document/product/436/127699)。

## 请求

#### 请求示例

POST /GetVectorBucketPolicy HTTP/1.1

Host: vectors.<Region>.coslake.com

Date: GMT Date

Content-Type: application/json

Content-Length: Content Length

Content-MD5: MD5

Authorization: Auth String

[Request Body]

**说明：**

Host: vectors.<Region>.coslake.com，更多信息可参见 [公共请求头部](https://cloud.tencent.com/document/product/436/127701) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

此接口无请求参数。

#### 请求体

需指定向量桶名字或者向量桶Qcs 。

{

 "vectorBucketQcs": "qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000",

 "vectorBucketName": "examplebucket-1250000000"

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
vectorBucketName 无 向量桶名称，<BucketName-APPID>格式，例如 examplebucket-1250000000，长度限制3-63个字符 string 否, vectorBucketName、vectorBucketQcs 必选其一
vectorBucketQcs 无 向量桶资源名称（QCS），例如qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000，具体资源格式说明参考 [向量存储桶的资源](https://cloud.tencent.com/document/product/436/127699)string 否, vectorBucketName、vectorBucketQcs 必选其一

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/127702) 文档。

#### 响应体

查询成功，返回 **application/json** 数据，包含向量桶策略信息。不同场景下的响应体请参见下方的实际案例。

{

 "policy": "string"

}

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型
policy 无 当前存储桶的策略字符串，一段 json 格式的策略信息序列化之后的字符串表示，按 json 格式再次解析一次可得到结构化的策略，示例可参考 [访问控制](https://cloud.tencent.com/document/product/436/127699)String

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/127703) 文档。

## 实际案例：查看策略

### 请求

POST /GetVectorBucketPolicy HTTP/1.1

Host: vectors.ap-guangzhou.coslake.com

Date: Sun, 26 May 2019 14:51:38 GMT

Content-Length: 47

Authorization: q-sign-algorithm=sha1&q-ak= ************************************ &q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature= ****************************************

Connection: close

{

 "vectorBucketName":"examplebucket-1250000000"

}

### 响应

HTTP/1.1 200 OK

Content-Length: 687

Connection: close

Date: Sun, 26 May 2019 14:51:37 GMT

X-Cos-Request-Id: NWNlYWE3ZjlfZDQyNzVkNjRfMzg1N18yNzFh****

{

 "policy": "{\"Statement\":[{\"Action\":[\"name/cos:DeleteVectorBucket\",\"name/cos:GetVectorBucket\",\"name/cos:PutVectorIndex\",\"name/cos:DeleteVectorIndex\",\"name/cos:GetVectorIndex\",\"name/cos:ListVectorIndexes\",\"name/cos:PutVectorBucketPolicy\",\"name/cos:GetVectorBucketPolicy\",\"name/cos:DeleteVectorBucketPolicy\",\"name/cos:PutVectors\",\"name/cos:GetVectors\",\"name/cos:DeleteVectors\",\"name/cos:ListVectors\",\"name/cos:QueryVectors\"],\"Effect\":\"Allow\",\"Principal\":{\"qcs\":[\"qcs::cam::uin/700000000000:uin/700001234567\"]},\"Resource\":[\"qcs::cosvector:ap-guangzhou:uid/1250000000:bucket/examplebucket-1250000000/*\"],\"Sid\":\"total\"}],\"Version\":\"2.0\"}"

}
