<!-- source: https://cloud.tencent.com/document/product/436/124901 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:47:11+08:00 -->

# 查询 AIGC 图片元数据标识

最近更新时间：2025-11-11 18:11:12


## 功能概述

AIGC 图片元数据中包含了内容生产平台标识、内容传播平台标识等信息，您可以通过本接口获取图片中的 AIGC 元数据标识信息。

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加 `cos:GetObject` 和 `ci:GetS3ImageAIGCDataJob` 权限，数据万象其他权限请参见 [数据万象 action](https://cloud.tencent.com/document/product/598/98114)。

## 服务开通

使用该功能将默认为您开通数据万象，并绑定存储桶，即可直接使用。

## 使用限制

使用该接口时，请先确认相关限制条件。详情请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620)。

支持获取 JPG/JPEG、PNG、AVIF 格式图片的 AIGC 元数据标识信息。

## 费用说明

该接口为付费服务，将产生**图片基础处理费用**，详细计费说明可参见 [图片处理费用](https://cloud.tencent.com/document/product/460/58117)。

## 接口示例

### 请求示例

GET /<ObjectKey>?ci-process=ImageAIGCMetadata HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

**注意：**

Authorization: 携带鉴权信息，用于验证请求的合法性的请求头，`ci-process=ImageAIGCMetadata` 请求参数需签入签名信息中，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

### 处理参数说明

#### **请求参数**

参数 含义 类型 是否必选
ObjectKey 对象文件名，例如 folder/sample.jpg。String 是
ci-process 代表数据万象处理操作的参数，查询 AIGC 图片元数据的操作，值固定为 ImageAIGCMetadata String 是

### 响应示例

返回的内容为图片 AIGC 元数据标识信息。

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
Label 用来标识内容是否属于 AI 生成 String
ContentProducer AI 生产方业务标识，每个业务唯一 String
ProduceID AI 生产方提供的，文件标识，每个文件唯一 String
ReservedCode1 生产方提供的，用于防止数据篡改的标识，每个文件唯一 String
ContentPropagator 内容传播方业务标识，每个业务唯一 String
PropagateID 内容传播方提供的，文件标识，每个文件唯一 String
ReservedCode2 内容传播方提供的，用于防止数据篡改的标识，每个文件唯一 String

**注意：**

若图片无 AIGC 元数据标识信息，将返回空内容`{}`。

## 实际案例

#### 请求

GET /example.jpg?ci-process=ImageAIGCMetadata HTTP/1.1

Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com

Date: Fri, 10 Mar 2025 09:45:46 GMT

Authorization: q-sign-algorithm=sha1&q-ak=*****&q-key-time=1484213027;32557109027&q-header-list=host&q-url-param-list=acl&q-signature=****************************************

Content-Length: 0

#### 响应

HTTP/1.1 200 OK

Content-Type: application/json

Content-Length: 666

Connection: keep-alive

Date: Fri, 10 Mar 2025 09:45:46 GMT

Server: tencent-ci

x-cos-request-id: NTg3NzRiMjV******l82ZGZmNw==

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
