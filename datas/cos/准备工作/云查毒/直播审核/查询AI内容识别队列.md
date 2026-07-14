<!-- source: https://cloud.tencent.com/document/product/436/106307 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:35:35+08:00 -->

# 查询AI内容识别队列

最近更新时间：2024-10-17 17:54:12


## 简介

查询AI内容识别队列功能是由 [数据万象](https://cloud.tencent.com/document/product/460 "https://cloud.tencent.com/document/product/460")（Cloud Infinite，CI）提供的，数据万象将处理能力与 COS SDK 完全结合，您可以直接按照本篇文档指引进行使用。 本文档提供关于查询AI内容识别队列的相关 API 概览以及 SDK 示例代码。

**注意：**

COS Javascript SDK 版本需要大于等于 v1.3.2。

API 操作描述
[查询AI内容识别队列](https://cloud.tencent.com/document/product/460/79394 "https://cloud.tencent.com/document/product/460/79394")本接口用于查询 AI 内容识别（异步）队列。

## 查询AI内容识别队列

#### 功能说明

本接口用于查询AI 内容识别（异步）队列。

#### 使用示例

function getAIQueue() {

 // sdk引入以及初始化请参考：https://cloud.tencent.com/document/product/436/11459

 const config = {

 // 需要替换成您自己的存储桶信息

 Bucket: 'examplebucket-1250000000', // 存储桶，必须字段

 Region: 'COS_REGION', // 存储桶所在地域，必须字段 如 ap-beijing

 };

 const key = 'ai_queue'; // 固定值

 const host = `${config.Bucket}.ci.${config.Region}.myqcloud.com`;

 const url = `https://${host}/${key}`;

 cos.request(

 {

 Method: 'GET', // 固定值，必须

 Key: key, // 必须

 Url: url, // 请求的url，必须

 Query: {

 // 队列 ID，以“,”符号分割字符串;是否必传：否

 // queueIds: "",

 // Active 表示队列内的作业会被调度执行Paused 表示队列暂停，作业不再会被调度执行，队列内的所有作业状态维持在暂停状态，已经执行中的任务不受影响;是否必传：否

 state: 'Active',

 // 第几页，默认值1;是否必传：否

 // pageNumber: 0,

 // 每页个数，默认值10;是否必传：否

 // pageSize: 0,

 },

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

getAIQueue();

#### 参数说明

cos.request 方法参数说明：

参数名称 参数描述 类型 是否必填
Method 固定值：GET String 是
Url 请求url，固定值 String 是
Key 固定值：ai_queue String 是
Query 其他请求参数 Container 是

Query 参数说明：

参数名称 参数描述 类型 是否必填
queueIds 队列 ID，以“,”符号分割字符串。String 否
state Active 表示队列内的作业会被调度执行Paused 表示队列暂停，作业不再会被调度执行，队列内的所有作业状态维持在暂停状态，已经执行中的任务不受影响。String 否
pageNumber 第几页，默认值1。Integer 否
pageSize 每页个数，默认值10。Integer 否

#### 回调函数说明

function(err, data) { ... }

参数名称 参数描述 类型
err 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功则为空，更多详情请参见 [错误码](https://cloud.tencent.com/document/product/460/8523 "https://cloud.tencent.com/document/product/460/8523")Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
data 请求成功时返回的对象，如果请求发生错误，则为空 Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
- Response 响应结果 详情请参见 [查询AI内容识别队列](https://cloud.tencent.com/document/product/460/79394#.E5.93.8D.E5.BA.94 "https://cloud.tencent.com/document/product/460/79394#.E5.93.8D.E5.BA.94")Object

#### 相关参考

[API 文档](https://cloud.tencent.com/document/product/460/79394 "https://cloud.tencent.com/document/product/460/79394")
