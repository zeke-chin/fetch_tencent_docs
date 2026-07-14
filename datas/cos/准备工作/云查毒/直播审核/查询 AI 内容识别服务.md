<!-- source: https://cloud.tencent.com/document/product/436/106984 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:35:22+08:00 -->

# 查询 AI 内容识别服务

最近更新时间：2024-11-29 18:48:52


## 简介

查询AI内容识别服务功能是由 [数据万象](https://cloud.tencent.com/document/product/460 "https://cloud.tencent.com/document/product/460")（Cloud Infinite，CI）提供的，数据万象将处理能力与 COS SDK 完全结合，您可以直接按照本篇文档指引进行使用。 本文档提供关于查询AI内容识别服务的相关 API 概览以及 SDK 示例代码。

**注意：**

COS 小程序 SDK 版本需要大于等于 v1.1.1。

API 操作描述
[查询AI内容识别服务](https://cloud.tencent.com/document/product/460/79594 "https://cloud.tencent.com/document/product/460/79594")本接口用于查询已经开通AI 内容识别（异步）服务的存储桶。

## 查询AI内容识别服务

#### 功能说明

本接口用于查询已经开通AI 内容识别（异步）服务的存储桶。

#### 使用示例

function getAIBucket() {

 // sdk引入以及初始化请参考：https://cloud.tencent.com/document/product/436/31953

 const config = {

 // 需要替换成您自己的存储桶信息

 Bucket: 'examplebucket-1250000000', // 存储桶，必须字段

 Region: 'COS_REGION', // 存储桶所在地域，必须字段 如 ap-beijing

 };

 const key = 'ai_bucket'; // 固定值

 const host = `ci.${config.Region}.myqcloud.com`;

 const url = `https://${host}/${key}`;

 cos.request(

 {

 Method: 'GET', // 固定值，必须

 Key: key, // 必须

 Url: url, // 请求的url，必须

 Query: {

 // 地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，详情请参见 地域与域名;是否必传：否

 // regions: '',

 // 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索;是否必传：否

 // bucketNames: '',

 // 存储桶名称前缀，前缀搜索;是否必传：否

 // bucketName: '',

 // 第几页;是否必传：否

 // pageNumber: 1,

 // 每页个数，大于0且小于等于100的整数;是否必传：否

 // pageSize: 10,

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

getAIBucket();

#### 参数说明

cos.request 方法参数说明：

参数名称 参数描述 类型 是否必填
Method 固定值：GET String 是
Url 请求url，固定值 String 是
Key 固定值：ai_bucket String 是
Query 其他请求参数 Container 是

Query 参数说明：

参数名称 参数描述 类型 是否必填
regions 地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，详情请参见 [地域与域名](https://cloud.tencent.com/document/product/460/31066)String 否
bucketNames 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索 String 否
bucketName 存储桶名称前缀，前缀搜索 String 否
pageNumber 第几页 Integer 否
pageSize 每页个数，大于0且小于等于100的整数 Integer 否

#### 回调函数说明

function(err, data) { ... }

参数名称 参数描述 类型
err 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功则为空，更多详情请参见 [错误码](https://cloud.tencent.com/document/product/460/8523 "https://cloud.tencent.com/document/product/460/8523")Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
data 请求成功时返回的对象，如果请求发生错误，则为空 Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
- Response 响应结果 详情请参见 [查询AI内容识别服务](https://cloud.tencent.com/document/product/460/79594#7c2ca189-dcf6-4dad-b1c3-4461fed0fdcc)Object

#### 相关链接

[API 文档](https://cloud.tencent.com/document/product/460/79594 "https://cloud.tencent.com/document/product/460/79594")
