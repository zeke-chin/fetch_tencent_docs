<!-- source: https://cloud.tencent.com/document/product/436/119464 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:50:01+08:00 -->

# 创建模板转码 pro（广电专业格式）

最近更新时间：2025-08-11 17:23:13


## 功能描述

创建音视频转码 pro 模板。

**说明：**

如需使用此功能，可 [提交工单](https://console.cloud.tencent.com/workorder/category) 开通白名单。

此功能为广电专业格式转码，可处理 Apple Prores、Sony XAVC 等格式。

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加 `ci:CreateMediaTemplate`权限。数据万象支持的所有操作接口请参见 [CI action](https://cloud.tencent.com/document/product/598/98114)。

## 服务开通

使用该功能需提前 [绑定存储桶](https://cloud.tencent.com/document/product/460/46483)，开通数据万象服务。

使用该功能需提前通过 [控制台](https://cloud.tencent.com/document/product/460/87745) 或 [接口](https://cloud.tencent.com/document/product/460/72823) 开通媒体处理服务。

**注意：**

数据万象绑定后，如果您手动对存储桶进行数据万象的解绑操作，将无法继续使用该功能。

## 使用限制

使用该接口时，请先确认相关限制条件。详情请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620#Media-processing)。

## 请求

#### 请求示例

POST /template HTTP/1.1

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

节点名称（关键字）父节点 描述 类型 是否必选
Request 无 保存请求的容器 Container 是

Container 类型

Request

 的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
Tag Request 模板类型：TranscodePro String 是
Name Request 模板名称 仅支持中文、英文、数字、_、-和* ，长度不超过64 String 是
Container Request 容器格式 Container 是
Video Request 视频信息 Container 是
TimeInterval Request 时间区间 Container 否
Audio Request 音频信息，不传 Audio，相当于删除音频信息 Container 否
TransConfig Request 转码配置 Container 否

Container 类型

Container

 的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
Format Request.Container 封装格式：有效值为 mxf、mov、mkv String 是

设定 Container，音频视频支持的编解码格式如下表：

Container Audio Codecs Video Codecs
mxf pcm_s24le xavc
mov、mkv aac、mp3 apple_prores

Container 类型

Video

 的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选 默认值
Codec Request.Video 编解码格式，支持 xavc、apple_prores String 是 无
Profile Request.Video 视频算法器预置，取值范围见下表 String 是 无
Width Request.Video 宽，取值范围见下表 String 是 无
Height Request.Video 高，取值范围见下表 String 是 无
Interlaced Request.Video 场模式，取值范围见下表 String 是 无
Fps Request.Video 帧率，取值范围见下表 String 是 无
Bitrate Request.Video 视频输出文件的码率，取值范围见下表 String 否 无
Rotate Request.Video 旋转角度

值范围：[0, 360)

单位：度 String 否 无

**注意：**

'-' 表示留空。

码率可选值与帧率可选值序号对应。

当 Video.Codec 为 xavc 时：

Profile Width Height Interlaced Fps Bitrate(单位:kbps)
XAVC-HD_intra_420_10bit_class50 1440 1080 true 1、25

2、30000/1001-
XAVC-HD_intra_420_10bit_class50 1440 1080 false 1、25

2、24000/1001

3、30000/1001-
XAVC-HD_intra_422_10bit_class100 1280 720 false 1、50

2、60000/1001-
XAVC-HD_intra_422_10bit_class100 1920 1080 true 1、25

2、30000/1001-
XAVC-HD_intra_422_10bit_class100 1920 1080 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001-
XAVC-HD_intra_422_10bit_class200 1920 1080 true 1、25

2、30000/1001-
XAVC-HD_intra_422_10bit_class200 1920 1080 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001-
XAVC-4K_intra_422_10bit_class100 2048 1080 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001-
XAVC-4K_intra_422_10bit_class300 3840 2160 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001-
XAVC-4K_intra_422_10bit_class300 4096 2160 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001-
XAVC-4K_intra_422_10bit_class480 3840 2160 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001-
XAVC-4K_intra_422_10bit_class480 4096 2160 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001-
XAVC-4K_intra_422_10bit 2048 1080 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001 1、93000

2、185000

3、89000

4、111000

5、222000
XAVC-4K_intra_422_10bit 3840 2160 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001 1、250000或400000

2、500000或800000

3、240000或384000

4、300000或480000

5、600000或960000
XAVC-4K_intra_422_10bit 4096 2160 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001 1、250000或400000

2、500000或800000

3、240000或384000

4、300000或480000

5、600000或960000
XAVC-HD_422_10bit 1280 720 false 1、50

2、60000/1001 1、50000

2、50000
XAVC-HD_422_10bit 1920 1080 true 1、25

2、30000/1001 1、25000或35000或50000

2、25000或35000或50000
XAVC-HD_422_10bit 1920 1080 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001 1、25000或35000或50000

2、35000或50000

3、25000或35000或50000

4、25000或35000或50000

5、35000或50000
XAVC-4K_422_10bit 3840 2160 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001 1、100000或140000或200000

2、140000或200000

3、100000或140000或200000

4、100000或140000或200000

5、140000或200000
XAVC-4K_420_8bit 3840 2160 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001 1、188000

2、300000

3、188000

4、188000

5、300000

当 Video.Codec 为 apple_prores 时：

Profile
1.ProRes_422_Proxy

2.ProRes_422_LT

3.ProRes_422

4.ProRes_422_HQ

5.ProRes_4444

6.ProRes_4444_XQ

7.ProRes_4444_alpha

8.ProRes_4444_XQ_alpha

Width Height Interlaced Fps Bitrate(单位:kbps)
720 486 false 1、24000/1001

2、30000/1001 取值范围:[2000,3000000]
720 486 true 1、60000/1001 取值范围:[2000,3000000]
720 576 false 1、25 取值范围:[2000,3000000]
720 576 true 1、50 取值范围:[2000,3000000]
960 720 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001 取值范围:[2000,3000000]
1280 720 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001 取值范围:[2000,3000000]
1280 1080 false 1、24000/1001

2、30000/1001 取值范围:[2000,3000000]
1280 1080 true 1、60000/1001 取值范围:[2000,3000000]
1440 1080 false 1、24000/1001

2、25

3、30000/1001 取值范围:[2000,3000000]
1440 1080 true 1、50

2、60000/1001 取值范围:[2000,3000000]
1920 1080 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001 取值范围:[2000,3000000]
1920 1080 true 1、50

2、60000/1001 取值范围:[2000,3000000]
2048 1080 false 1、25

2、50

3、24000/1001

4、30000/1001

5、60000/1001 取值范围:[2000,3000000]
2048 1556 false 1、25 2、50 3、24000/1001 4、30000/1001 5、60000/1001 取值范围:[2000,3000000]
3840 2160 false 1、25 2、50 3、24000/1001 4、30000/1001 5、60000/1001 取值范围:[2000,3000000]
4096 2160 false 1、25 2、50 3、24000/1001 4、30000/1001 5、60000/1001 取值范围:[2000,3000000]
5120 2700 false 1、25 2、50 3、24000/1001 4、30000/1001 5、60000/1001 取值范围:[2000,3000000]
6144 3240 false 1、25 2、50 3、24000/1001 4、30000/1001 5、60000/1001 取值范围:[2000,3000000]
8192 4320 false 1、25 2、50 3、24000/1001 4、30000/1001 5、60000/1001 取值范围:[2000,3000000]

 Container 类型

TimeInterval

 的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 默认值 是否必选
Start Request.TimeInterval 开始时间

[0， 视频时长]

单位为秒

支持 float 格式，执行精度精确到毫秒 String 0 否
Duration Request.TimeInterval 持续时间

[0， 视频时长]

单位为秒

支持 float 格式，执行精度精确到毫秒 String 视频原始时长 否

Container 类型

Audio

的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 默认值 是否必选
Codec Request.Audio 编解码格式，pcm_s24le、aac、mp3 String 无 是
Remove Request.Audio 是否删除源音频流，取值 true、false String false 否

Container 类型

TransConfig

 的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 默认值 是否必选
AdjDarMethod Request.TransConfig 分辨率调整方式

取值 scale、crop、pad、none

当输出视频的宽高比与原视频不等时，根据此参数做分辨率的相应调整 String none 否
IsCheckReso Request.TransConfig 是否检查分辨率，取值 true、false

当为 false 时，按照配置参数转码 String false 否
ResoAdjMethod Request.TransConfig 分辨率调整方式

当 IsCheckReso 为 true 时生效，取值0、1；

0 表示使用原视频分辨率；

1 表示返回转码失败 String 0 否
IsCheckVideoBitrate Request.TransConfig 是否检查视频码率，取值 true、false

当为 false 时，按照配置参数转码 String false 否
VideoBitrateAdjMethod Request.TransConfig 视频码率调整方式

IsCheckVideoBitrate 为 true 时生效，取值0、1；

当输出视频码率大于原视频码率时，0表示使用原视频码率；1表示返回转码失败 String 0 否
IsCheckAudioBitrate Request.TransConfig 是否检查音频码率，取值 true、false

当为 false 时，按照配置参数转码 String false 否
AudioBitrateAdjMethod Request.TransConfig 音频码率调整方式

IsCheckAudioBitrate 为 true 时生效，取值0、1；

当输出音频码率大于原音频码率时，0表示使用原音频码率；1表示返回转码失败 String 0 否
IsCheckVideoFps Request.TransConfig 是否检查视频帧率，取值 true、false

当为 false 时，按照配置参数转码 String false 否
VideoFpsAdjMethod Request.TransConfig 视频帧率调整方式

IsCheckVideoFps 为 true 时生效，取值0、1；

当输出视频帧率大于原视频帧率时，0表示使用原视频帧率；1表示返回转码失败 String 0 否
DeleteMetadata Request.TransConfig 是否删除文件中的 MetaData 信息，取值 true、false String false 否
IsHdr2Sdr Request.TransConfig 是否开启 HDR 转 SDR，取值 true、false String false 否

AdjDarMethod 参数图示：

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/00af4271caaaa2279f6b70c8a319a9cd.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/00af4271caaaa2279f6b70c8a319a9cd.png)

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

<Response>

 <Template>

 <Tag>TranscodePro</Tag>

 <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>

 <Name>TemplateName</Name>

 <BucketId>test-1234567890</BucketId>

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
Response 无 保存结果的容器 Container

Container 节点

Response

 的内容：

节点名称（关键字）父节点 描述 类型
TemplateId Response.Template 模板 ID String
Name Response.Template 模板名称 String
BucketId Response.Template 模板所属存储桶 String
Category Response.Template 模板属性，Custom 或者 Official String
Tag Response.Template 模板类型，TranscodePro String
UpdateTime Response.Template 更新时间 String
CreateTime Response.Template 创建时间 String
TransProTpl Response.Template 详细的模板参数 Container

Container 节点

TransProTpl

 的内容：

节点名称（关键字）父节点 描述 类型
TimeInterval Response.Template.TransProTpl 同请求体中的 [Request.TimeInterval](https://cloud.tencent.com/document/product/436/119464#TimeInterval)Container
Container Response.Template.TransProTpl 同请求体中的 [Request.Container](https://cloud.tencent.com/document/product/436/119464#Container)Container
Video Response.Template.TransProTpl 同请求体中的 [Request.Video](https://cloud.tencent.com/document/product/436/119464#Video)Container
Audio Response.Template.TransProTpl 同请求体中的 [Request.Audio](https://cloud.tencent.com/document/product/436/119464#Audio)Container
TransConfig Response.Template.TransProTpl 同请求体中的 [Request.TransConfig](https://cloud.tencent.com/document/product/436/119464#TransConfig)Container

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

POST /template HTTP/1.1

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signatrue=****************************************

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

 <Template>

 <Tag>TranscodePro</Tag>

 <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>

 <Name>TemplateName</Name>

 <BucketId>test-1234567890</BucketId>

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
