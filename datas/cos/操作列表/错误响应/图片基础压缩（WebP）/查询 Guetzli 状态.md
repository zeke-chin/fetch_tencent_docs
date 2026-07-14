<!-- source: https://cloud.tencent.com/document/product/436/119421 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:46:18+08:00 -->

# 查询 Guetzli 状态

最近更新时间：2025-09-19 15:44:52


## 功能描述

用于查询 Guetzli 压缩功能是否开启。

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加 `ci:DescribeImageGuetzli` 权限。数据万象支持的所有操作接口请参见 [CI action](https://cloud.tencent.com/document/product/598/98114)。

## 服务开通

使用该功能需提前 [绑定存储桶](https://cloud.tencent.com/document/product/460/46483)，开通数据万象服务。

**注意：**

数据万象绑定后，如果您手动对存储桶进行数据万象的解绑操作，将无法继续使用该功能。

## 使用限制

使用该接口时，请先确认相关限制条件。详情请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620#Image-processing)。

## 请求

#### 请求语法

GET /?guetzli HTTP/1.1

Host: <BucketName-APPID>.pic.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

**说明：**

Authorization: Auth String，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778 "https://cloud.tencent.com/document/product/436/7778") 文档。

#### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865 "https://cloud.tencent.com/document/product/460/42865") 章节。

#### 非公共头部

该请求操作无特殊的请求头部信息。

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866 "https://cloud.tencent.com/document/product/460/42866") 章节。

#### 特有响应头

该响应无特殊的响应头。

#### 响应体

<?xml version="1.0" encoding="UTF-8" ?>

<GuetzliStatus>on</GuetzliStatus>

响应体参数说明如下：

参数名称 类型 描述
GuetzliStatus String Guetzli 压缩功能的开启状态
