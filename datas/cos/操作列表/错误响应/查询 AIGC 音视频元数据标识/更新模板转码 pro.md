<!-- source: https://cloud.tencent.com/document/product/436/119466 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:50:04+08:00 -->

# 更新模板转码 pro

最近更新时间：2025-08-11 17:23:13


## 功能描述

更新音视频转码 pro 模板。

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加 `ci:UpdateMediaTemplate` 权限。数据万象支持的所有操作接口请参见 [CI action](https://cloud.tencent.com/document/product/598/98114)。

## 服务开通

使用该功能需提前 [绑定存储桶](https://cloud.tencent.com/document/product/460/46483)，开通数据万象服务。

使用该功能需提前通过 [控制台](https://cloud.tencent.com/document/product/460/87745) 或 [接口](https://cloud.tencent.com/document/product/460/72823) 开通媒体处理服务。

**注意：**

数据万象绑定后，如果您手动对存储桶进行数据万象的解绑操作，将无法继续使用该功能。

## 使用限制

使用该接口时，请先确认相关限制条件。详情请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620#Media-processing)。

## 请求

#### 请求示例

PUT /template/<TemplateId> HTTP/1.1

Host: <BucketName-APPID>.ci.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

Content-Length: <length>

Content-Type: application/xml

<body>

**说明：**

Authorization: Auth String，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

TemplateId：音视频转码 pro 模板的ID，可在 [创建音视频转码模板](https://cloud.tencent.com/document/product/460/84732) 的响应中获取。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有如下请求体。

<Request>

 <Tag>TranscodePro</Tag>

 <Name>TemplateName</Name>

 <Container>

 <Format>mxf</Format>

 </Container>

 <Video>

 <Codec>xavc</Codec>

 <Profile>XAVC-HD_422_10bit</Profile>

 <Width>1920</Width>

 <Height>1080</Height>

 <Interlaced>true</Interlaced>

 <Fps>30000/1001</Fps>

 <Bitrate>50000</Bitrate>

 </Video>

 <Audio>

 <Codec>pcm_s24le</Codec>

 </Audio>

 <TransConfig>

 <AdjDarMethod>scale</AdjDarMethod>

 <IsCheckReso>false</IsCheckReso>

 <ResoAdjMethod>1</ResoAdjMethod>

 </TransConfig>

 <TimeInterval>

 <Start>0</Start>

 <Duration>60</Duration>

 </TimeInterval>

</Request>

具体数据描述如下：

节点名称（关键字）父节点 描述 类型 必选
Request 无[同创建转码 Pro 模板接口的 Request](https://cloud.tencent.com/document/product/460/84732#Request)Container 是

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

<Response>

 <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>

 <Template>

 <Tag>TranscodePro</Tag>

 <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>

 <Name>TemplateName</Name>

 <BucketId>example-1250000000</BucketId>

 <Category>Custom</Category>

 <TransProTpl>

 <Container>

 <Format>mxf</Format>

 </Container>

 <Video>

 <Codec>xavc</Codec>

 <Profile>XAVC-HD_422_10bit</Profile>

 <Width>1920</Width>

 <Height>1080</Height>

 <Interlaced>true</Interlaced>

 <Fps>30000/1001</Fps>

 <Bitrate>50000</Bitrate>

 </Video>

 <Audio>

 <Codec>pcm_s24le</Codec>

 </Audio>

 <TransConfig>

 <AdjDarMethod>scale</AdjDarMethod>

 <IsCheckReso>false</IsCheckReso>

 <ResoAdjMethod>1</ResoAdjMethod>

 </TransConfig>

 <TimeInterval>

 <Start>0</Start>

 <Duration>60</Duration>

 </TimeInterval>

 </TransProTpl>

 <CreateTime>2020-08-05T11:35:24+0800</CreateTime>

 <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>

 </Template>

</Response>

具体的数据内容如下：

节点名称（关键字）父节点 描述 类型
Response 无[同创建转码 Pro 模板接口的 Response](https://cloud.tencent.com/document/product/460/84732#Response)Container

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

PUT /template/t1460606b9752148c4ab182f55163ba7cd HTTP/1.1

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=****************************************

Host: test-1234567890.ci.ap-beijing.myqcloud.com

Content-Length: 1666

Content-Type: application/xml

<Request>

 <Tag>TranscodePro</Tag>

 <Name>TemplateName</Name>

 <Container>

 <Format>mxf</Format>

 </Container>

 <Video>

 <Codec>xavc</Codec>

 <Profile>XAVC-HD_422_10bit</Profile>

 <Width>1920</Width>

 <Height>1080</Height>

 <Interlaced>true</Interlaced>

 <Fps>30000/1001</Fps>

 <Bitrate>50000</Bitrate>

 </Video>

 <Audio>

 <Codec>pcm_s24le</Codec>

 </Audio>

 <TransConfig>

 <AdjDarMethod>scale</AdjDarMethod>

 <IsCheckReso>false</IsCheckReso>

 <ResoAdjMethod>1</ResoAdjMethod>

 </TransConfig>

 <TimeInterval>

 <Start>0</Start>

 <Duration>60</Duration>

 </TimeInterval>

</Request>

#### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 100

Connection: keep-alive

Date: Thu, 14 Jul 2022 12:37:29 GMT

Server: tencent-ci

x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>

 <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>

 <Template>

 <Tag>TranscodePro</Tag>

 <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>

 <Name>TemplateName</Name>

 <BucketId>example-1250000000</BucketId>

 <Category>Custom</Category>

 <TransProTpl>

 <Container>

 <Format>mxf</Format>

 </Container>

 <Video>

 <Codec>xavc</Codec>

 <Profile>XAVC-HD_422_10bit</Profile>

 <Width>1920</Width>

 <Height>1080</Height>

 <Interlaced>true</Interlaced>

 <Fps>30000/1001</Fps>

 <Bitrate>50000</Bitrate>

 </Video>

 <Audio>

 <Codec>pcm_s24le</Codec>

 </Audio>

 <TransConfig>

 <AdjDarMethod>scale</AdjDarMethod>

 <IsCheckReso>false</IsCheckReso>

 <ResoAdjMethod>1</ResoAdjMethod>

 </TransConfig>

 <TimeInterval>

 <Start>0</Start>

 <Duration>60</Duration>

 </TimeInterval>

 </TransProTpl>

 <CreateTime>2020-08-05T11:35:24+0800</CreateTime>

 <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>

 </Template>

</Response>
