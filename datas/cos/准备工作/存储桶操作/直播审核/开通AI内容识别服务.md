<!-- source: https://cloud.tencent.com/document/product/436/110392 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:06:31+08:00 -->

# 开通AI内容识别服务

最近更新时间：2024-08-28 10:13:01


## 简介

本文档提供关于开通AI内容识别服务的相关 API 概览以及 SDK 示例代码。

API 操作描述
[开通AI内容识别服务](https://cloud.tencent.com/document/product/460/79593)开通AI内容识别服务

## 开通AI内容识别服务

#### 功能说明

本接口用于开通AI 内容识别（异步）服务并生成队列。

#### 示例代码

def ci_open_ai_bucket():

 # 开通AI内容识别服务

 response, data = client.ci_open_ai_bucket(

 Bucket=bucket_name

 )

 print(response)

 print(data)

 return response, data

#### 参数说明

调用 ci_open_ai_bucket 函数，具体请求参数如下：

参数名称 参数描述 类型 是否必填
Bucket 存储桶名称 String 是

#### 返回结果说明

response 为响应头，data 为开通AI内容识别服务结果，数据类型都为 dict。

##### response内容

返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

##### 响应体data

响应体具体数据内容如下：

参数名称 参数描述 类型
RequestId 请求的唯一 ID String
AiBucket 存储桶信息 Container

AiBucket 节点内容：

参数名称 参数描述 类型
BucketId 存储桶 ID String
AliasBucketId 存储桶别名
Name 存储桶名称，同 BucketId String
Region 所在的地域 String
CreateTime 创建时间 String
