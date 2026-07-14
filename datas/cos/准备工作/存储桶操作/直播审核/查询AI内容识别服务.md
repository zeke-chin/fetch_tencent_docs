<!-- source: https://cloud.tencent.com/document/product/436/110393 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:06:41+08:00 -->

# 查询AI内容识别服务

最近更新时间：2024-08-28 10:13:01


## 简介

本文档提供关于查询AI内容识别服务的相关 API 概览以及 SDK 示例代码。

API 操作描述
[查询AI内容识别服务](https://cloud.tencent.com/document/product/460/79594)查询AI内容识别服务

## 查询AI内容识别服务

#### 功能说明

本接口用于查询已经开通AI 内容识别（异步）服务的存储桶。

#### 示例代码

def ci_get_ai_bucket():

 # 查询AI内容识别服务

 data = client.ci_get_ai_bucket(

 Regions = "ap-chongqing",

 BucketNames = "test-12500000",

 BucketName = "test",

 PageNumber = "1",

 PageSize = "1"

 )

 print(data)

 return data

#### 参数说明

调用 ci_get_ai_bucket 函数，具体请求参数如下：

参数名称 参数描述 类型 是否必填
Regions 地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，详情请参见 [地域与域名](https://cloud.tencent.com/document/product/460/31066)String 否
BucketNames 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索 String 否
BucketName 存储桶名称前缀，前缀搜索 String 否
PageNumber 第几页 String 否
PageSize 每页个数，大于0且小于等于100的整数 String 否

#### 返回结果说明

data 为查询AI内容识别服务结果，数据类型为 dict。

##### response内容

返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

##### 响应体data

响应体具体数据内容如下：

参数名称 参数描述 类型
RequestId 请求的唯一 ID String
TotalCount 开通AI 内容识别（异步）的 Bucket 总数 Integer
PageNumber 当前页数，同请求中的 pageNumber Integer
PageSize 每页个数，同请求中的 pageSize Integer
AiBucketList AI 内容识别（异步） Bucket 详情 Container Array

AiBucketList 节点内容：

参数名称 参数描述 类型
BucketId 存储桶 ID String
Name 存储桶名称，同 BucketId String
Region 所在的地域 String
CreateTime 创建时间 String
