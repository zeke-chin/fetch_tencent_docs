<!-- source: https://cloud.tencent.com/document/product/436/116676 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:51:30+08:00 -->

# 更新 AI 内容识别队列

最近更新时间：2026-03-27 16:09:10


## 功能描述

本接口用于更新 AI 内容识别（异步）的队列。

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加 `ci:UpdateAiProcessQueue` 权限。数据万象支持的所有操作接口请参见 [CI action](https://cloud.tencent.com/document/product/598/98114)。

## 服务开通

使用该功能需提前 [绑定存储桶](https://cloud.tencent.com/document/product/460/46483)，开通数据万象服务。

使用该功能需提前通过 [控制台](https://cloud.tencent.com/document/product/460/47193) 或 [接口](https://cloud.tencent.com/document/product/460/79593) 开通 AI 内容识别服务。

**注意：**

数据万象绑定后，如果您手动对存储桶进行数据万象的解绑操作，将无法继续使用该功能。

## 使用限制

使用该接口时，请先确认相关限制条件。详情请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620#content-recognition)。

## 请求

#### 请求示例

PUT /ai_queue/<queueId> HTTP/1.1

Host: <BucketName-APPID>.ci.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

Content-Length: <length>

Content-Type: application/xml

<body>

**说明：**

Authorization：Auth String，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

<queueId>：AI 内容识别队列 ID，可通过 [控制台](https://cloud.tencent.com/document/product/460/46487) 或 [接口](https://cloud.tencent.com/document/product/460/79394) 查询。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有以下请求体。

<Request>

 <Name>My-Queue-ai</Name>

 <State>Active</State>

 <NotifyConfig>

 <State>On</State>

 <Url>http://callback.demo.com</Url>

 <Type>Url</Type>

 <Event>TaskFinish,WorkflowFinish</Event>

 <ResultFormat>JSON</ResultFormat>

 </NotifyConfig>

</Request>

具体的数据内容如下：

节点名称（关键字）父节点 描述 类型 是否必选 默认值 限制
Request 无 保存结果的容器 Container 是 无 无

Container 节点 Request 的内容：

节点名称（关键字）父节点 描述 类型 默认值 是否必选
Name Request 队列名称，仅支持中文、英文、数字、_、-和*，长度不超过 128 String 无 是
State Request Active 表示队列内的作业会被调度执行

Paused 表示队列暂停，作业不再会被调度执行，队列内的所有作业状态维持在暂停状态，已经执行中的任务不受影响 String 无 是
NotifyConfig Request 回调配置 Container 无 是

Container 节点 NotifyConfig 的内容：

节点名称（关键字）父节点 描述 类型 默认值 是否必选
State Request.NotifyConfig 回调开关

Off

On String Off 否
Event Request.NotifyConfig 回调事件

TaskFinish：任务完成

WorkflowFinish：工作流完成 String 无 当 State = On 时，必选
ResultFormat Request.NotifyConfig 回调格式

XML

JSON String XML 否
Type Request.NotifyConfig 回调类型

Url

TDMQ String 无 当 State = On 时，必选
Url Request.NotifyConfig 回调地址，不能为内网地址。String 无 当 State = On，且 Type = Url 时，必选
MqMode Request.NotifyConfig TDMQ 使用模式

Topic：主题订阅

Queue: 队列服务 String 无 当 State = On，且 Type = TDMQ 时，必选
MqRegion Request.NotifyConfig TDMQ 所属园区，目前支持以下园区 sh（上海）、bj（北京）、gz（广州）、cd（成都）、cq（重庆）、nj（南京）、hk（中国香港）String 无 当 State = On，且 Type = TDMQ 时，必选
MqName Request.NotifyConfig TDMQ 主题名称 String 无 当 State = On，且 Type = TDMQ 时，必选

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

<Response>

 <RequestId>NjJmNDczY2RfOTBmYTUwNjRfNTA4ZV85</RequestId>

 <Queue>

 <QueueId>p4a17eeea29334bf499b7e20e2fbfd99d</QueueId>

 <Name>My-Queue-ai</Name>

 <State>Active</State>

 <NotifyConfig>

 <Url>http://callback.demo.com</Url>

 <Event>TaskFinish,WorkflowFinish</Event>

 <Type>Url</Type>

 <State>On</State>

 <ResultFormat>JSON</ResultFormat>

 <MqMode/>

      <MqName/>

      <MqRegion/>

 </NotifyConfig>

 <MaxSize>10000</MaxSize>

 <MaxConcurrent>10</MaxConcurrent>

 <Category>AIProcess</Category>

 <UpdateTime>2022-08-09T16:23:11+0800</UpdateTime>

 <CreateTime>2022-08-09T16:13:05+0800</CreateTime>

 <BucketId>example-12500000000</BucketId>

 </Queue>

</Response>

具体的数据内容如下：

节点名称（关键字）父节点 描述 类型
Response 无 保存结果的容器 Container

Container 节点 Response 的内容：

节点名称（关键字）父节点 描述 类型
RequestId Response 请求的唯一 ID String
Queue Response 队列信息 Container

Container 节点 Queue 的内容：

节点名称（关键字）父节点 描述 类型
QueueId Response.Queue 队列 ID String
Name Response.Queue 队列名字 String
State Response.Queue 当前状态，Active 或者 Paused String
NotifyConfig Response.Queue 回调配置，同 Request.NotifyConfig Container
MaxSize Response.Queue 队列最大长度 Int
MaxConcurrent Response.Queue 当前队列最大并行执行的任务数 Int
Category Response.Queue 队列类型 String
UpdateTime Response.Queue 更新时间 String
CreateTime Response.Queue 创建时间 String
BucketId Response.Queue 队列所属存储桶的 ID String

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

PUT /ai_queue/p4a17eeea29334bf499b7e20e2fbfd99d HTTP/1.1

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=****************************************

Host: test-1234567890.ci.ap-chongqing.myqcloud.com

Content-Length: 162

Content-Type: application/xml

<Request>

 <Name>My-Queue-ai</Name>

 <State>Active</State>

 <NotifyConfig>

 <State>On</State>

 <Url>http://callback.demo.com</Url>

 <Type>Url</Type>

 <Event>TaskFinish,WorkflowFinish</Event>

 <ResultFormat>JSON</ResultFormat>

 </NotifyConfig>

</Request>

#### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 100

Connection: keep-alive

Date: Thu, 09 Aug 2022 16:23:12 GMT

Server: tencent-ci

x-ci-request-id: NjJmNDczY2RfOTBmYTUwNjRfNTA4ZV85

<Response>

 <RequestId>NjJmNDczY2RfOTBmYTUwNjRfNTA4ZV85</RequestId>

 <Queue>

 <QueueId>p4a17eeea29334bf499b7e20e2fbfd99d</QueueId>

 <Name>My-Queue-ai</Name>

 <State>Active</State>

 <NotifyConfig>

 <Url>http://callback.demo.com</Url>

 <Event>TaskFinish,WorkflowFinish</Event>

 <Type>Url</Type>

 <State>On</State>

 <ResultFormat>JSON</ResultFormat>

 <MqMode/>

      <MqName/>

      <MqRegion/>

 </NotifyConfig>

 <MaxSize>10000</MaxSize>

 <MaxConcurrent>10</MaxConcurrent>

 <Category>AIProcess</Category>

 <UpdateTime>2022-08-09T16:23:11+0800</UpdateTime>

 <CreateTime>2022-08-09T16:13:05+0800</CreateTime>

 <BucketId>example-12500000000</BucketId>

 </Queue>

</Response>
