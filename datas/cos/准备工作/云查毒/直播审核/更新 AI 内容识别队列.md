<!-- source: https://cloud.tencent.com/document/product/436/106987 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:42:00+08:00 -->

# 更新 AI 内容识别队列

最近更新时间：2024-06-06 16:01:03


## 简介

更新AI内容识别队列功能是由 [数据万象](https://cloud.tencent.com/document/product/460 "https://cloud.tencent.com/document/product/460")（Cloud Infinite，CI）提供的，数据万象将处理能力与 COS SDK 完全结合，您可以直接按照本篇文档指引进行使用。 本文档提供关于更新AI内容识别队列的相关 API 概览以及 SDK 示例代码。

**注意：**

COS 小程序 SDK 版本需要大于等于 v1.1.1。

API 操作描述
[更新AI内容识别队列](https://cloud.tencent.com/document/product/460/79397 "https://cloud.tencent.com/document/product/460/79397")本接口用于更新 AI 内容识别（异步）的队列。

## 更新AI内容识别队列

#### 功能说明

本接口用于更新 AI 内容识别（异步）的队列。

#### 使用示例

function updateAIQueue() {

 // sdk引入以及初始化请参考：https://cloud.tencent.com/document/product/436/31953

 const config = {

 // 需要替换成您自己的存储桶信息

 Bucket: 'examplebucket-1250000000', // 存储桶，必须字段

 Region: 'COS_REGION', // 存储桶所在地域，必须字段 如 ap-beijing

 };

 const queueId = 'xxxx'; // 队列id

 const key = `ai_queue/${queueId}`; // 固定格式

 const host = `${config.Bucket}.ci.${config.Region}.myqcloud.com`;

 const url = `https://${host}/${key}`;

 const body = COS.util.json2xml({

 Request: {

 // 队列名称，仅支持中文、英文、数字、_、-和*，长度不超过 128;是否必传：是

 Name: 'my_queue',

 // Active 表示队列内的作业会被调度执行Paused 表示队列暂停，作业不再会被调度执行，队列内的所有作业状态维持在暂停状态，已经执行中的任务不受影响;是否必传：是

 State: 'Active',

 // 回调配置;是否必传：是

 NotifyConfig: {

 // 回调开关OffOn;是否必传：否

 State: 'On',

 // 回调事件TaskFinish：任务完成WorkflowFinish：工作流完成;是否必传：否

 Event: 'TaskFinish',

 // 回调格式XMLJSON;是否必传：否

 // ResultFormat: '',

 // 回调类型UrlTDMQ;是否必传：否

 Type: 'Url',

 // 回调地址，不能为内网地址。;是否必传：否

 Url: 'http://example.com',

 // TDMQ 使用模式Topic：主题订阅Queue: 队列服务;是否必传：否

 // MqMode: '',

 // TDMQ 所属园区，目前支持园区 sh（上海）、bj（北京）、gz（广州）、cd（成都）、hk（中国香港）;是否必传：否

 // MqRegion: '',

 // TDMQ 主题名称;是否必传：否

 // MqName: '',

 },

 },

 });

 cos.request(

 {

 Method: 'PUT', // 固定值，必须

 Key: key, // 必须

 Url: url, // 请求的url，必须

 Body: body, // 请求体参数，必须

 ContentType: 'application/xml', // 固定值，必须

 },

 function (err, data) {

 if (err) {

 // 处理请求失败

 console.log(err);

 } else {

 // 处理请求成功

 console.log(data.Response);

 }

 }

 );

}

updateAIQueue();

#### 参数说明

cos.request 方法参数说明：

参数名称 参数描述 类型 是否必填
Method 固定值：PUT String 是
Url 请求 url，固定值 String 是
Key ai_queue/{queueId}String 是
ContentType 固定值 String 是
Body 请求体详情请参见 [更新AI内容识别队列](https://cloud.tencent.com/document/product/460/79397#.E8.AF.B7.E6.B1.82 "https://cloud.tencent.com/document/product/460/79397#.E8.AF.B7.E6.B1.82")Object 是

#### 回调函数说明

function(err, data) { ... }

参数名称 参数描述 类型
err 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功则为空，更多详情请参见 [错误码](https://cloud.tencent.com/document/product/460/8523 "https://cloud.tencent.com/document/product/460/8523")Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
data 请求成功时返回的对象，如果请求发生错误，则为空 Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
- Response 响应结果 详情请参见 [更新AI内容识别队列](https://cloud.tencent.com/document/product/460/79397#.E5.93.8D.E5.BA.94 "https://cloud.tencent.com/document/product/460/79397#.E5.93.8D.E5.BA.94")Object

#### 相关参考

[API 文档](https://cloud.tencent.com/document/product/460/79397 "https://cloud.tencent.com/document/product/460/79397")
