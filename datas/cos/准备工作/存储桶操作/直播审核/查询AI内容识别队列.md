<!-- source: https://cloud.tencent.com/document/product/436/110395 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:06:48+08:00 -->

# 查询AI内容识别队列

最近更新时间：2024-08-28 10:13:01


## 简介

本文档提供关于查询AI内容识别队列的相关 API 概览以及 SDK 示例代码。

API 操作描述
[查询AI内容识别队列](https://cloud.tencent.com/document/product/460/79394)查询AI内容识别队列

## 查询AI内容识别队列

#### 功能说明

本接口用于查询AI 内容识别（异步）队列。

#### 示例代码

def ci_get_ai_queue():

 # 查询AI内容识别队列

 # demo地址：https://github.com/tencentyun/cos-python-sdk-v5/blob/master/demo/ai_recognition_demo.py#L546

 response = client.ci_get_ai_queue(

 Bucket=bucket_name,

 QueueIds='',

 State='All',

 PageNumber='',

 PageSize=''

 )

 print(response)

 return response

#### 参数说明

调用 ci_get_ai_queue 函数，具体请求参数如下：

参数名称 参数描述 类型 是否必填
Bucket 存储桶名称 String 是
QueueIds 队列 ID（开通语音识别服务后自动生成，可通过 [万象控制台](https://cloud.tencent.com/document/product/460/46487) 在存储桶中查询），以“,”符号分割字符串 String 否
State Active 表示队列内的作业会被调度执行

Paused 表示队列暂停，作业不再会被调度执行，队列内的所有作业状态维持在暂停状态，已经执行中的任务不受影响 String 否
PageNumber 第几页，默认值1 String 否
PageSize 每页个数，默认值10 String 否

#### 返回结果说明

response 查询AI内容识别队列结果，数据类型都为 dict。

##### response内容

由于接口默认返回xml内容，解析结果都为string类型，以下描述为字段的真实类型。具体数据内容如下：

参数名称 参数描述 类型
RequestId 请求的唯一 ID String
TotalCount 队列总数 Integer
PageNumber 当前页数，同请求中的 pageNumber Integer
PageSize 每页个数，同请求中的 pageSize Integer
QueueList 队列数组 Container Array
NonExistPIDs 不存在的队列 ID 列表 String Array

QueueList 节点内容：

参数名称 参数描述 类型
QueueId 队列 ID String
Name 队列名字 String
State 当前状态，Active 或者 Paused String
NotifyConfig 回调配置 Container
MaxSize 队列最大长度 Integer
MaxConcurrent 当前队列最大并行执行的任务数 Integer
Category 队列类型 String
UpdateTime 更新时间 String
CreateTime 创建时间 String
BucketId 队列对应的存储桶名称 String

NotifyConfig 节点内容：

参数名称 参数描述 类型
Url 回调地址 String
State 开关状态 String
Type 回调类型 String
Event 回调事件 String
ResultFormat 回调类型 String
MqMode TDMQ 使用模式 String
MqRegion TDMQ 所属园区 String
MqName TDMQ 主题名称 String
