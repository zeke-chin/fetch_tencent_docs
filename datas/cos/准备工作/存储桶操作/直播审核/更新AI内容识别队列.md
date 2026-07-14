<!-- source: https://cloud.tencent.com/document/product/436/110396 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:06:50+08:00 -->

# 更新AI内容识别队列

最近更新时间：2024-08-28 10:13:01


## 简介

本文档提供关于更新AI内容识别队列的相关 API 概览以及 SDK 示例代码。

API 操作描述
[更新AI内容识别队列](https://cloud.tencent.com/document/product/460/79397)更新AI内容识别队列

## 更新AI内容识别队列

#### 功能说明

本接口用于更新AI 内容识别（异步）的队列。

#### 示例代码

def ci_update_ai_queue():

 # 更新AI内容识别队列

 # demo地址：https://github.com/tencentyun/cos-python-sdk-v5/blob/master/demo/ai_recognition_demo.py#L559

 body = {

 # 队列名称，仅支持中文、英文、数字、_、-和*，长度不超过 128

 # 是否必传：是

 'Name': "test",

 # Active 表示队列内的作业会被调度执行；Paused 表示队列暂停，作业不再会被调度执行，队列内的所有作业状态维持在暂停状态，已经执行中的任务不受影响

 # 是否必传：是

 'State': "Active",

 # 回调配置

 # 是否必传：是

 'NotifyConfig': {

 # 回调开关OffOn

 # 是否必传：否

 'State': "On",

 # 回调事件，TaskFinish：任务完成；WorkflowFinish：工作流完成

 # 是否必传：否

 'Event': "TaskFinish",

 # 回调格式XMLJSON

 # 是否必传：否

 'ResultFormat': "XML",

 # 回调类型Url TDMQ

 # 是否必传：否

 'Type': "Url",

 # 回调地址，不能为内网地址。

 # 是否必传：否

 'Url': "http://www.test.cpm",

 # TDMQ 使用模式Topic：主题订阅Queue: 队列服务

 # 是否必传：否

 'MqMode': "Topic",

 # TDMQ 所属园区，目前支持园区 sh（上海）、bj（北京）、gz（广州）、cd（成都）、hk（中国香港）

 # 是否必传：否

 'MqRegion': "sh",

 # TDMQ 主题名称

 # 是否必传：否

 'MqName': "testTopic",

 },

 }

 response = client.ci_update_ai_queue(

 Bucket=bucket_name,

 QueueId="queueId",

 Request=body,

 ContentType="application/xml"

 )

 print(response)

 return response

#### 参数说明

调用 ci_update_ai_queue 函数，具体请求参数如下：

参数名称 参数描述 类型 是否必填
Bucket 存储桶名称 String 是
QueueId 队列 ID（开通内容识别服务后自动生成，可通过 [万象控制台](https://cloud.tencent.com/document/product/460/46487) 在存储桶中查询）String 是
Request 更新AI内容识别队列请求参数 Container 否

Request 节点内容：

参数名称 参数描述 类型 是否必填
Name 队列名称，仅支持中文、英文、数字、_、-和*，长度不超过 128 String 是
State Active 表示队列内的作业会被调度执行

Paused 表示队列暂停，作业不再会被调度执行，队列内的所有作业状态维持在暂停状态，已经执行中的任务不受影响 String 是
NotifyConfig 回调配置 Container 是

NotifyConfig 节点内容：

参数名称 参数描述 类型 是否必填
State 回调开关Off/On String 否
Event 回调事件

TaskFinish：任务完成

WorkflowFinish：工作流完成 String 否
ResultFormat 回调格式，XML/JSON String 否
Type 回调类型，Url/TDMQ String 否
Url 回调地址，不能为内网地址。String 否
MqMode TDMQ 使用模式

Topic：主题订阅

Queue: 队列服务 String 否
MqRegion TDMQ 所属园区，目前支持园区 sh（上海）、bj（北京）、gz（广州）、cd（成都）、hk（中国香港）String 否
MqName TDMQ 主题名称 String 否

#### 返回结果说明

response 为更新AI内容识别队列结果，数据类型为 dict。

##### response内容

由于接口默认返回xml内容，解析结果都为string类型，以下描述为字段的真实类型。具体数据内容如下：

参数名称 参数描述 类型
RequestId 请求的唯一 ID String
Queue 队列信息 Container

Queue 节点内容：

参数名称 参数描述 类型
QueueId 队列 ID String
Name 队列名字 String
State 当前状态，Active 或者 Paused String
NotifyConfig 回调配置，同 Request.NotifyConfig Container
MaxSize 队列最大长度 Integer
MaxConcurrent 当前队列最大并行执行的任务数 Integer
Category 队列类型 String
UpdateTime 更新时间 String
CreateTime 创建时间 String

NotifyConfig 节点内容：

参数名称 参数描述 类型
State 回调开关

Off

On String
Event 回调事件

TaskFinish：任务完成

WorkflowFinish：工作流完成 String
ResultFormat 回调格式

XML

JSON String
Type 回调类型

Url

TDMQ String
Url 回调地址，不能为内网地址。String
MqMode TDMQ 使用模式

Topic：主题订阅

Queue: 队列服务 String
MqRegion TDMQ 所属园区，目前支持园区 sh（上海）、bj（北京）、gz（广州）、cd（成都）、hk（中国香港）String
MqName TDMQ 主题名称 String
