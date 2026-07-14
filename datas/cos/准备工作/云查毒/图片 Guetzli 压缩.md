<!-- source: https://cloud.tencent.com/document/product/436/106933 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:58:47+08:00 -->

# 图片 Guetzli 压缩

最近更新时间：2025-01-08 18:16:42


## 简介

本文档提供关于图片 Guetzli 压缩的相关 API 概览以及 SDK 示例代码。

**注意：**

COS 小程序 SDK 版本需要大于等于 v1.5.0。

API 操作描述
[开通 Guetzli 压缩](https://cloud.tencent.com/document/product/460/30112 "https://cloud.tencent.com/document/product/460/30112")对 Bucket 开通 Guetzli 压缩功能
[查询 Guetzli 状态](https://cloud.tencent.com/document/product/460/30111 "https://cloud.tencent.com/document/product/460/30111")用于查询 Guetzli 压缩功能是否开启
[关闭 Guetzli 压缩](https://cloud.tencent.com/document/product/460/30113 "https://cloud.tencent.com/document/product/460/30113")用于关闭 Guetzli 压缩功能

## 开通 Guetzli 压缩

#### 功能说明

对 Bucket 开通 Guetzli 压缩功能。

#### 使用示例

function openImageGuetzli() {

 // sdk引入以及初始化请参考：https://cloud.tencent.com/document/product/436/31953

 const config = {

 // 需要替换成您自己的存储桶信息

 Bucket: 'examplebucket-1250000000', // 存储桶，必须字段

 Region: 'COS_REGION', // 存储桶所在地域，必须字段 如 ap-beijing

 };

 const key = `` //

 const host = `${config.Bucket}.pic.${config.Region}.myqcloud.com`;

 const url = `https://${host}/${key}`;


 cos.request(

 {

 Method: 'PUT', // 固定值，必须

 Key: key, // 必须

 Url: url, // 请求的url，必须

 Action: 'guetzli'// 固定值

 },

 function (err, data) {

 if (err) {

 // 处理请求失败

 console.log(err);

 } else {

 // 处理请求成功

 console.log(data.Response);

 }

 },

 );

}

openImageGuetzli()

#### 参数说明

cos.request 方法参数说明：

参数名称 参数描述 类型 是否必填
Method 固定值：PUT String 是
Url 请求 url，固定值 String 是

#### 回调函数说明

function(err, data) { ... }

参数名称 参数描述 类型
err 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功则为空，更多详情请参见 [错误码](https://cloud.tencent.com/document/product/460/8523 "https://cloud.tencent.com/document/product/460/8523")Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
data 请求成功时返回的对象，如果请求发生错误，则为空 Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
- Response 响应结果，详情请参见 [开通 Guetzli 压缩](https://cloud.tencent.com/document/product/460/30112#.E5.93.8D.E5.BA.94 "https://cloud.tencent.com/document/product/460/30112#.E5.93.8D.E5.BA.94")Object

#### 相关链接

[API 文档](https://cloud.tencent.com/document/product/460/30112 "https://cloud.tencent.com/document/product/460/30112")

[功能指南](https://cloud.tencent.com/document/product/460/47500 "https://cloud.tencent.com/document/product/460/47500")

## 查询 Guetzli 状态

#### 功能说明

用于查询 Guetzli 压缩功能是否开启。

#### 使用示例

function describeImageGuetzli() {

 // sdk引入以及初始化请参考：https://cloud.tencent.com/document/product/436/31953

 const config = {

 // 需要替换成您自己的存储桶信息

 Bucket: 'examplebucket-1250000000', // 存储桶，必须字段

 Region: 'COS_REGION', // 存储桶所在地域，必须字段 如 ap-beijing

 };

 const key = `` //

 const host = `${config.Bucket}.pic.${config.Region}.myqcloud.com`;

 const url = `https://${host}/${key}`;


 cos.request(

 {

 Method: 'GET', // 固定值，必须

 Key: key, // 必须

 Url: url, // 请求的url，必须

 Action: 'guetzli'// 固定值

 },

 function (err, data) {

 if (err) {

 // 处理请求失败

 console.log(err);

 } else {

 // 处理请求成功

 console.log(data.Response);

 }

 },

 );

}

describeImageGuetzli()

#### 参数说明

cos.request 方法参数说明：

参数名称 参数描述 类型 是否必填
Method 固定值：GET String 是
Url 请求 url，固定值 String 是

#### 回调函数说明

function(err, data) { ... }

参数名称 参数描述 类型
err 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功则为空，更多详情请参见 [错误码](https://cloud.tencent.com/document/product/460/8523 "https://cloud.tencent.com/document/product/460/8523")Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
data 请求成功时返回的对象，如果请求发生错误，则为空 Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
- Response 响应结果，详情请参见 [查询 Guetzli 状态](https://cloud.tencent.com/document/product/460/30111#.E5.93.8D.E5.BA.94 "https://cloud.tencent.com/document/product/460/30111#.E5.93.8D.E5.BA.94")Object

#### 相关链接

[API 文档](https://cloud.tencent.com/document/product/460/30111 "https://cloud.tencent.com/document/product/460/30111")

[功能指南](https://cloud.tencent.com/document/product/460/47500 "https://cloud.tencent.com/document/product/460/47500")

## 关闭 Guetzli 压缩

#### 功能说明

用于关闭 Guetzli 压缩功能。

#### 使用示例

function closeImageGuetzli() {

 // sdk引入以及初始化请参考：https://cloud.tencent.com/document/product/436/31953

 const config = {

 // 需要替换成您自己的存储桶信息

 Bucket: 'examplebucket-1250000000', // 存储桶，必须字段

 Region: 'COS_REGION', // 存储桶所在地域，必须字段 如 ap-beijing

 };

 const key = `` //

 const host = `${config.Bucket}.pic.${config.Region}.myqcloud.com`;

 const url = `https://${host}/${key}`;


 cos.request(

 {

 Method: 'DELETE', // 固定值，必须

 Key: key, // 必须

 Url: url, // 请求的url，必须

 Action: 'guetzli'// 固定值

 },

 function (err, data) {

 if (err) {

 // 处理请求失败

 console.log(err);

 } else {

 // 处理请求成功

 console.log(data.Response);

 }

 },

 );

}

closeImageGuetzli()

#### 参数说明

cos.request 方法参数说明：

参数名称 参数描述 类型 是否必填
Method 固定值：DELETE String 是
Url 请求 url，固定值 String 是

#### 回调函数说明

function(err, data) { ... }

参数名称 参数描述 类型
err 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功则为空，更多详情请参见 [错误码](https://cloud.tencent.com/document/product/460/8523 "https://cloud.tencent.com/document/product/460/8523")Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
data 请求成功时返回的对象，如果请求发生错误，则为空 Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
- Response 响应结果，详情请参见 [关闭 Guetzli 压缩](https://cloud.tencent.com/document/product/460/30113#.E5.93.8D.E5.BA.94 "https://cloud.tencent.com/document/product/460/30113#.E5.93.8D.E5.BA.94")Object

#### 相关链接

[API 文档](https://cloud.tencent.com/document/product/460/30113 "https://cloud.tencent.com/document/product/460/30113")

[功能指南](https://cloud.tencent.com/document/product/460/47500 "https://cloud.tencent.com/document/product/460/47500")
