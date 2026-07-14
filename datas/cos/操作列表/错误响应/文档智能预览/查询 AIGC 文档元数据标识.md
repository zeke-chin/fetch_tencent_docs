<!-- source: https://cloud.tencent.com/document/product/436/124905 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:55:13+08:00 -->

# 查询 AIGC 文档元数据标识

最近更新时间：2025-11-11 18:11:12


## 功能描述

AIGC 文档元数据中包含了内容生产平台标识、内容传播平台标识等信息，您可以通过本接口获取文档中的 AIGC 元数据标识信息。

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加 `cos:GetObject` 权限，具体请参见 [COS action](https://cloud.tencent.com/document/product/598/69901)，数据万象其他权限请参见 [数据万象 action](https://cloud.tencent.com/document/product/598/98114)。

## 服务开通

使用该功能需将 [存储桶绑定数据万象](https://cloud.tencent.com/document/product/460/97479)。

使用该功能需提前通过 [控制台](https://cloud.tencent.com/document/product/460/46499) 或 [接口](https://cloud.tencent.com/document/product/460/103608) 开通文档处理服务。

## 使用限制

支持获取 pdf、xmind、md、docx、pptx、xlsx、dotx、potx、xltx 格式的 AIGC 元数据标识信息。

文档大小限制：不超过50MB。

接口请求默认并发数：10

地域限制：支持中国大陆公有云地域。

## 费用说明

该功能为付费服务，产生的费用将由数据万象收取，详细计费说明请参见 [文档处理费用](https://cloud.tencent.com/document/product/460/58121)。

## 接口示例

### 请求示例

GET /<ObjectKey>?ci-process=DocAIGCMetadata HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

Content-Length: <length>

**注意：**

Authorization: 携带鉴权信息，用于验证请求的合法性的请求头，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求参数说明

参数 描述 类型 是否必选
ObjectKey 对象文件名，例如 folder/test.pdf String 是
ci-process 代表数据万象处理操作的参数，查询 AIGC 文档元数据的操作，值固定为 DocAIGCMetadata String 是

#### 请求体

该请求无请求体。

### 响应示例

返回的内容为文档 AIGC 元数据标识信息。

{

 "AIGC": {

 "Label": "1",

 "ContentProducer": "000123",

 "ProduceID": "testProduceId",

 "ReservedCode1": "ewogICAgIm****UiLAp9",

 "ContentPropagator": "000123",

 "PropagateID": "testPropagatorId",

 "ReservedCode2": "ewogICAg*****UyIiwKfQ"

 }

}

#### 响应参数说明

参数 描述 类型
Label 用来标识内容是否属于 AI 生成的 String
ContentProducer AI 生产方业务标识，每个业务唯一 String
ProduceID AI 生产方提供的，文件标识，每个文件唯一 String
ReservedCode1 生产方提供的，用于防止数据篡改的标识，每个文件唯一 String
ContentPropagator 内容传播方业务标识，每个业务唯一 String
PropagateID 内容传播方提供的，文件标识，每个文件唯一 String
ReservedCode2 内容传播方提供的，用于防止数据篡改的标识，每个文件唯一 String

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/53983) 文档。

## 实际案例

#### 请求

GET /for-test.pdf?ci-process=DocAIGCMetadata HTTP/1.1

Host: examplebucket-1250000000.cos.ap-chongqing.myqcloud.com

Date: Fri, 10 Mar 2025 09:45:46 GMT

Authorization: q-sign-algorithm=sha1&q-ak=******&q-key-time=1484213027;32557109027&q-header-list=host&q-url-param-list=acl&q-signature=********

Content-Length: 0

#### 响应

HTTP/1.1 200 OK

Content-Type: application/json

Content-Length: 666

Connection: keep-alive

Date: Fri, 10 Mar 2025 09:45:46 GMT

Server: tencent-ci

x-cos-request-id: NTg3NzRiMjV******mNw==

{

 "AIGC": {

 "Label": "1",

 "ContentProducer": "000123",

 "ProduceID": "testProduceId",

 "ReservedCode1": "ewogICAgIm****UiLAp9",

 "ContentPropagator": "000123",

 "PropagateID": "testPropagatorId",

 "ReservedCode2": "ewogICAg*****UyIiwKfQ"

 }

}
