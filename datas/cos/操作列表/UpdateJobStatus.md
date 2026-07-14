<!-- source: https://cloud.tencent.com/document/product/436/38613 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:43:24+08:00 -->

# UpdateJobStatus

最近更新时间：2025-10-09 16:27:52


## 功能描述

UpdateJobStatus 用于更新任务状态。您可以使用这一接口实现启动一项任务或者取消一项正在进行的任务。有关批量处理任务的详细介绍，可参见 [批量处理概述](https://cloud.tencent.com/document/product/436/38601)。

## 授权说明

授权策略中 action 设置为 `cos:UpdateJobStatus`。查看所有 [action](https://cloud.tencent.com/document/product/598/69901)。

## 请求

#### **请求示例**

POST /jobs/<JobId>/status?requestedJobStatus=<RequestedJobStatus>&statusUpdateReason=<StatusUpdateReason> HTTP/1.1

Host: <UIN>.cos-control.<Region>.myqcloud.com

x-cos-appid: <appid>

Authorization: Auth String

**说明：**

Host: <UIN>.cos-control.<Region>.myqcloud.com，其中 <UIN> 为主账号 UIN 或已被授权的账号 UIN，例如100000000001，可参见 [账号信息](https://console.cloud.tencent.com/developer)；<Region> 为 COS 的可用地域，可参见 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求参数

#### **请求参数**

调用 UpdateJobStatus 需要使用清单任务名称的参数。该参数格式如下：

参数 描述 类型 是否必选
JobId 您想要更新的批量处理任务的 JobId。可调用 [ListJobs](https://cloud.tencent.com/document/product/436/38611) 接口查看已有的 JobId。长度限制为1 - 64字节。String 是
requestedJobStatus 您期望的批量处理任务的状态。当您将任务转移至`Ready`状态时，COS 将认为您已确认此项任务，并将执行此项任务。当您将任务转移至`Cancelled`状态时，COS 将取消此项任务。可选参数包括：Ready、Cancelled。String 是
statusUpdateReason 更新任务状态的原因。此项参数长度限制为0 - 256字节。String 否
x-cos-appid 用户的 APPID，长度为1 - 64字节。String 是

#### **请求头**

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### **请求体**

该请求无请求体。

## 响应

#### **响应头**

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### **响应体**

<UpdateJobStatusResult>

 <JobId>string</JobId>

 <Status>string</Status>

 <StatusUpdateReason>string</StatusUpdateReason>

</UpdateJobStatusResult>

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型
UpdateJobStatusResult 无 保存 UpdateJobStatus 结果的所有信息 Container

**Container 节点 UpdateJobStatusResult 的内容：**

节点名 父节点 描述 类型
JobId UpdateJobStatusResult 任务 ID。您所更新的任务的 ID，长度限制为5 - 36字节。String
Status UpdateJobStatusResult 任务的当前状态。合法参数项包括：Active、Cancelled、Cancelling、 Complete、Completing、Failed、Failing、New、Paused、Pausing、Preparing、Ready、 Suspended。String
StatusUpdateReason UpdateJobStatusResult 任务更新原因。长度限制为0 - 256字节。String

#### 错误码

该请求可能会发生的一些常见的特殊错误如下,其他错误请参见 [批量处理功能错误响应](https://cloud.tencent.com/document/product/436/38610)。

错误码 描述 状态码 API
InvalidArgument requestedJobStatus 参数必须为 Cancelled 或 Ready 400 UpdateJobStatus
InvalidRequest 指定任务已完成 400 UpdateJobStatus
InvalidRequest 任务状态变更错误 400 UpdateJobStatus
NoSuchJob 指定任务不存在或已完成 404 UpdateJobStatus，UpdateJobPriority

## 实际案例

#### 请求

POST /jobs/53dc6228-c50b-46f7-8ad7-65e7159f1aae/status?requestedJobStatus=Cancelled&statusUpdateReason=Reason HTTP/1.1

Host: 100000000001.cos-control.ap-chengdu.myqcloud.com

Date: Thu, 19 Dec 2024 18:00:29 GMT

x-cos-appid: 1250000000

Content-Type: application/xml

Content-Length: 1056

Content-MD5: hHcgq5mu8s0Ywe4WTGiQ+uA==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1576778429;1576785629&q-key-time=1576778429;1576785629&q-header-list=content-length;content-md5;content-type;date;host;x-cos-appid&q-url-param-list=&q-signature=****************************************

Connection: close

#### **响应**

HTTP/1.1 200 OK

<UpdateJobStatusResult>

 <JobId>53dc6228-c50b-46f7-8ad7-65e7159f1aae</JobId>

 <Status>Cancelled</Status>

 <StatusUpdateReason>Reason</StatusUpdateReason>

</UpdateJobStatusResult>
