<!-- source: https://cloud.tencent.com/document/product/436/115311 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:49:30+08:00 -->

# 提交视频 DNA 任务

最近更新时间：2026-05-13 17:28:04


## 功能描述

提交一个视频 DNA 任务，视频 DNA 任务可实现视频入库、视频查重、视频出库操作。

**注意：**

使用视频 DNA 需提前创建视频 DNA 库，点击 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=141&level2_id=635&source=0&data_title=T-Sec-%E4%B8%BB%E6%9C%BA%E5%AE%89%E5%85%A8&step=1) 创建 DNA 库。

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加 `ci:CreateMediaJobs`。数据万象支持的所有操作接口请参见 [CI action](https://cloud.tencent.com/document/product/598/98114)。

子账号使用异步处理接口时，需要授予 `cam:PassRole` 权限，异步处理接口会通过 CAM 的“角色”进行 COS 的资源读写操作，PassRole 权限用于传递角色， 具体请查看 [访问管理 > 写操作 > PassRole 接口](https://cloud.tencent.com/document/product/598/69872#.E5.86.99.E6.93.8D.E4.BD.9C)。

## 服务开通

使用该功能需提前 [绑定存储桶](https://cloud.tencent.com/document/product/460/46483)，开通数据万象服务。

使用该功能需提前通过 [控制台](https://cloud.tencent.com/document/product/460/87745) 或 [接口](https://cloud.tencent.com/document/product/460/72823) 开通媒体处理服务。

**注意：**

数据万象绑定后，如果您手动对存储桶进行数据万象的解绑操作，将无法继续使用该功能。

## 使用限制

使用该接口时，请先确认相关限制条件。详情请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620#Media-processing)。

## 费用说明

该接口为付费服务，产生的费用将由数据万象收取，详细计费说明可参见 [媒体处理费用](https://cloud.tencent.com/document/product/460/58120)。

视频 DNA 计费标准与视频标签一致，根据视频处理时长计费，例：入库时长为10分钟的视频，查重时长为5分钟的视频，费用为：10*0.05元/分钟+5*0.05元/分钟=0.75元。

## 请求

#### 请求示例

POST /jobs HTTP/1.1

Host: <BucketName-APPID>.ci.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

Content-Length: <length>

Content-Type: application/xml

<body>

**说明：**

Authorization: Auth String，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有如下请求体。

<Request>

 <Tag>DNA</Tag>

 <Input>

 <Object>input/demo.mp4</Object>

 </Input>

 <Operation>

 <DnaConfig>

 <RuleType>GetFingerPrint</RuleType>

 <DnaDbId>Db0fafe624fec211edbdc852540083a8ba</DnaDbId>

 </DnaConfig>

 <UserData>This is my data.</UserData>

 <JobLevel>0</JobLevel>

 </Operation>

 <CallBack>http://callback.demo.com</CallBack>

 <CallBackFormat>JSON</CallBackFormat>

</Request>

具体的数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
Request 无 保存请求的容器 Container 是

Container 类型 Request 的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
Tag Request 创建任务的 Tag：DNA String 是
Input Request 待操作的文件信息 Container 是
Operation Request 操作规则 Container 是
CallBackFormat Request 任务回调格式，JSON 或 XML，默认 XML，优先级高于队列的回调格式 String 否
CallBackType Request 任务回调类型，Url 或 TDMQ，默认 Url，优先级高于队列的回调类型 String 否
CallBack Request 任务回调地址，优先级高于队列的回调地址。设置为 no 时，表示队列的回调地址不产生回调 String 否
CallBackMqConfig Request 任务回调 TDMQ 配置，当 CallBackType 为 TDMQ 时必填。详情见 [CallBackMqConfig](https://cloud.tencent.com/document/product/460/78927#CallBackMqConfig)Container 否

Container 类型 Input 的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
Object Request.Input 输入文件路径。视频长度需小于1800s String 是

Container 类型

Operation

 的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
DnaConfig Request.Operation 视频 DNA 任务参数 Container 是
JobLevel Request.Operation 任务优先级，级别限制：0 、1 、2。级别越大任务优先级越高，默认为0 String 否
UserData Request.Operation 透传用户信息 String 否

Container 类型 DnaConfig 的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
RuleType Request.Operation.DnaConfig DNA 任务类型

GetFingerPrint：提取视频指纹并存入 DNA 库

FindSimilarVideo：从 DNA 库中进行视频查重

DeleteFingerPrint：从 DNA 库中删除视频 String 是
DnaDbId Request.Operation.DnaConfig DNA 库 ID String 是
VideoId Request.Operation.DnaConfig 视频唯一 ID，当 RuleType 为 DeleteFingerPrint 时生效且必选 String 否

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

<Response>

 <JobsDetail>

 <Code>Success</Code>

 <Message/>

 <Input>

 <BucketId>test-123456789</BucketId>

 <Object>input/demo.mp4</Object>

 <Region>ap-chongqing</Region>

 </Input>

 <JobId>j8d121820f5e411ec926ef19d53ba9c6f</JobId>

 <State>Submitted</State>

 <CreationTime>2022-06-27T15:23:10+0800</CreationTime>

 <StartTime>-</StartTime>

 <EndTime>-</EndTime>

 <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>

 <QueueType>Transcoding</QueueType>

 <Tag>DNA</Tag>

 <Operation>

 <DnaConfig>

 <DnaDbId>Db0fafe624fec211edbdc852540083a8ba</DnaDbId>

 <RuleType>FindSimilarVideo</RuleType>

 </DnaConfig>

 <JobLevel>0</JobLevel>

 </Operation>

 </JobsDetail>

</Response>

具体的数据内容如下：

节点名称（关键字）父节点 描述 类型
Response 无 保存结果的容器 Container

Container 节点 Response 的内容：

节点名称（关键字）父节点 描述 类型
JobsDetail Response 任务的详细信息 Container 数组

Container 节点

JobsDetail

 的内容：

节点名称（关键字）父节点 描述 类型
Code Response.JobsDetail 错误码，当 State 为 Failed 时生效 String
Message Response.JobsDetail 错误描述，当 State 为 Failed 时生效 String
JobId Response.JobsDetail 创建任务的 ID String
Tag Response.JobsDetail 创建任务的 Tag：DNA String
State Response.JobsDetail 任务状态

Submitted：已提交，待执行

Running：执行中

Success：执行成功

Failed：执行失败

Pause：任务暂停，当暂停队列时，待执行的任务会变为暂停状态

Cancel：任务被取消执行 String
CreationTime Response.JobsDetail 任务的创建时间 String
StartTime Response.JobsDetail 任务的开始时间 String
EndTime Response.JobsDetail 任务的结束时间 String
QueueId Response.JobsDetail 任务所属的 [队列 ID](https://cloud.tencent.com/document/product/460/46487)String
QueueType Response.JobsDetail 任务所属的队列类型 String
Input Response.JobsDetail 该任务的输入资源地址 Container
Operation Response.JobsDetail 该任务的规则 Container

Container 节点 Input 的内容：

节点名称（关键字）父节点 描述 类型
Region Response.JobsDetail.Input 存储桶的地域 String
BucketId Response.JobsDetail.Input 源文件所在存储桶 String
Object Response.JobsDetail.Input 源文件的文件名 String

Container 节点 Operation 的内容：

节点名称（关键字）父节点 描述 类型
DnaConfig Response.JobsDetail.Operation 同请求中的 Request.Operation.DnaConfig Container
DnaResult Response.JobsDetail.Operation DNA 任务结果，任务未完成时不返回 Container
UserData Response.JobsDetail.Operation 透传用户信息 String
JobLevel Response.JobsDetail.Operation 任务优先级 String

Container 节点 DnaResult 的内容：

节点名称（关键字）父节点 描述 类型
VideoId Response.JobsDetail.Operation.DnaResult 输入视频的唯一标识 ID String
Duration Response.JobsDetail.Operation.DnaResult 输入视频的时长，单位秒 Integer
Detection Response.JobsDetail.Operation.DnaResult 相似视频详情 Container 数组

Container 节点 Detection 的内容：

节点名称（关键字）父节点 描述 类型
VideoId Response.JobsDetail.Operation.DnaResult.Detection 匹配视频的 VideoId String
Similar Response.JobsDetail.Operation.DnaResult.Detection 相似度 Integer
SimilarDuration Response.JobsDetail.Operation.DnaResult.Detection 相似片段时长 Integer
Duration Response.JobsDetail.Operation.DnaResult.Detection 视频时长 Integer
MatchDetail Response.JobsDetail.Operation.DnaResult.Detection 匹配详情 Container 数组
Audio Response.JobsDetail.Operation.DnaResult.Detection 音频相似详情 Container

Container 节点 MatchDetail 的内容：

节点名称（关键字）父节点 描述 类型
MatchStartTime Response.JobsDetail.Operation.DnaResult.Detection.MatchDetail 相似视频匹配的开始时间，单位秒 Integer
MatchEndTime Response.JobsDetail.Operation.DnaResult.Detection.MatchDetail 相似视频匹配的结束时间，单位秒 Integer
SrcStartTime Response.JobsDetail.Operation.DnaResult.Detection.MatchDetail 源视频匹配的开始时间，单位秒 Integer
SrcEndTime Response.JobsDetail.Operation.DnaResult.Detection.MatchDetail 源视频匹配的结束时间，单位秒 Integer

Container 节点 Audio 的内容：

节点名称（关键字）父节点 描述 类型
Similar Response.JobsDetail.Operation.DnaResult.Detection.Audio 音频相似度 Integer

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

POST /jobs HTTP/1.1

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=****************************************

Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com

Content-Length: 166

Content-Type: application/xml

<Request>

 <Tag>DNA</Tag>

 <Input>

 <Object>input/demo.mp4</Object>

 </Input>

 <Operation>

 <DnaConfig>

 <RuleType>GetFingerPrint</RuleType>

 <DnaDbId>Db0fafe624fec211edbdc852540083a8ba</DnaDbId>

 </DnaConfig>

 <UserData>This is my data.</UserData>

 <JobLevel>0</JobLevel>

 </Operation>

 <CallBack>http://callback.demo.com</CallBack>

 <CallBackFormat>JSON</CallBackFormat>

</Request>

#### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 230

Connection: keep-alive

Date: Mon, 28 Jun 2022 15:23:12 GMT

Server: tencent-ci

x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>

 <JobsDetail>

 <Code>Success</Code>

 <Message/>

 <JobId>j8d121820f5e411ec926ef19d53ba9c6f</JobId>

 <State>Submitted</State>

 <CreationTime>2022-06-27T15:23:10+0800</CreationTime>

 <StartTime>-</StartTime>

 <EndTime>-</EndTime>

 <QueueId>p2242ab62c7c94486915508540933a2c6</QueueId>

 <QueueType>Transcoding</QueueType>

 <Tag>DNA</Tag>

 <Input>

 <BucketId>test-123456789</BucketId>

 <Object>input/demo.mp4</Object>

 <Region>ap-chongqing</Region>

 </Input>

 <Operation>

 <DnaConfig>

 <DnaDbId>Db0fafe624fec211edbdc852540083a8ba</DnaDbId>

 <RuleType>GetFingerPrint</RuleType>

 </DnaConfig>

 <JobLevel>0</JobLevel>

 </Operation>

 </JobsDetail>

</Response>
