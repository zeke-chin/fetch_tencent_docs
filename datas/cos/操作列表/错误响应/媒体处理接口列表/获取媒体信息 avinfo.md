<!-- source: https://cloud.tencent.com/document/product/436/124611 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:48:45+08:00 -->

# 获取媒体信息 avinfo

最近更新时间：2025-10-30 15:48:22


## 功能描述

本接口用于获取媒体文件的信息，如音视频文件的元信息。

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加 `cos:GetObject`权限。对象存储支持的所有操作接口请参见 [COS action](https://cloud.tencent.com/document/product/598/69901)。

## 服务开通

使用该功能需提前 [绑定存储桶](https://cloud.tencent.com/document/product/460/46483)，开通数据万象服务。

使用该功能需提前通过 [控制台](https://cloud.tencent.com/document/product/460/87745) 或 [接口](https://cloud.tencent.com/document/product/460/72823) 开通媒体处理服务 。

**注意：**

数据万象绑定后，如果您手动对存储桶进行数据万象的解绑操作，将无法继续使用该功能。

## 使用限制

使用该接口时，请先确认相关限制条件。详情请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620#Media-processing)。

## 费用说明

该接口为付费服务，产生的费用将由数据万象收取，详细计费说明可参见 [媒体处理费用](https://cloud.tencent.com/document/product/460/58120)。

## 请求

#### 请求示例

GET /<ObjectKey>?ci-process=avinfo HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

Content-Length: <length>

**说明：**

Authorization: Auth String，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求参数

参数说明如下：

节点名称（关键字）描述 类型 是否必选
ObjectKey 对象文件名。例如 test.mp4 String 是
ci-process 操作类型。固定值：avinfo，代表使用获取媒体信息功能 String 是
magicvar 魔法变量参数，当设置为“1”时，音频/视频流信息会被分别解析，封装输出 String 否

#### 请求体

该请求无请求体。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该响应体返回为 **application/json** 数据，包含完整节点数据的内容展示如下：

{

 "streams": [

 {

 "index": 0,

 "codec_name": "h264",

 "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",

 "codec_type": "video",

 "codec_time_base": "1/30",

 "codec_tag_string": "avc1",

 "codec_tag": "0x31637661",

 "width": 1152,

 "height": 864,

 "has_b_frames": 0,

 "sample_aspect_ratio": "1:1",

 "display_aspect_ratio": "4:3",

 "pix_fmt": "yuv420p",

 "level": 40,

 "is_avc": "1",

 "nal_length_size": "4",

 "r_frame_rate": "15/1",

 "avg_frame_rate": "15/1",

 "time_base": "1/15000",

 "start_time": "0.000000",

 "duration": "6413.333333",

 "nb_frames": "96200",

 "tags": {

 "creation_time": "2013-01-07 12:58:08",

 "language": "eng",

 "handler_name": "Video Media Handler"

 }

 },

 {

 "index": 1,

 "codec_name": "aac",

 "codec_long_name": "Advanced Audio 编码器全名Coding",

 "codec_type": "audio",

 "codec_time_base": "1/44100",

 "codec_tag_string": "mp4a",

 "codec_tag": "0x6134706d",

 "sample_fmt": "s16",

 "sample_rate": "44100",

 "channels": 2,

 "bits_per_sample": 0,

 "r_frame_rate": "0/0",

 "avg_frame_rate": "0/0",

 "time_base": "1/44100",

 "start_time": "0.000000",

 "duration": "6413.374694",

 "nb_frames": "276201",

 "tags": {

 "creation_time": "2013-01-07 12:58:08",

 "language": "eng",

 "handler_name": "Sound Media Handler"

 }

 }

 ],

 "format": {

 "nb_streams": 2,

 "format_name": "mov,mp4,m4a,3gp,3g2,mj2",

 "format_long_name": "QuickTime/MPEG-4/Motion JPEG 2000 format",

 "start_time": "0.000000",

 "duration": "6413.359589",

 "size": "101416337",

 "bit_rate": "126506",

 }

}

具体的数据内容如下：

Container 节点 format 的内容（某字段未获取到有效值时不返回）：

节点名称（关键字）父节点 描述 类型
nb_streams format Stream（包含 video、audio、sub_info）的数量 Integer
nb_programs format 节目的数量 Integer
format_name format 容器格式名字 String
format_long_name format 容器格式的详细名字 String
start_time format 起始时间，单位为秒 String
duration format 时长，单位为秒 String
bit_rate format 比特率，单位为kbps String
size format 大小，单位为Byte String

当未设置 magicvar 参数时，返回内容如下：

节点名称（关键字）父节点 描述 类型
streams 无 音视频流信息 Array
format 无 格式信息 Container

Container 节点 streams 详细信息：

节点名称（关键字）父节点 描述 类型
index streams 该流的编号 Integer
codec_type streams 流类型 String
codec_name streams 编解码格式名字 String
codec_long_name streams 编解码格式的详细名字 String
codec_time_base streams 编码时基 String
codec_tag_string streams 编码标签名 String
codec_tag streams 编码标签 String
color_primaries streams 色原 String
color_range streams 色彩范围 String
color_transfer streams 色彩通道 String
profile streams 视频编码档位 String
height streams 视频高度，单位为px Integer
width streams 视频宽度，单位为px Integer
has_b_frames streams 是否有 B 帧。1表示有，0表示无 String
refs streams 视频编码的参考帧个数 Integer
sample_aspect_ratio streams 采样宽高比 String
display_aspect_ratio streams 显示宽高比 String
pix_fmt streams 像素格式 String
filed_order streams 场的顺序 String
level streams 视频编码等级 Integer
r_frame_rate streams 视频帧率 String
avg_frame_rate streams 平均帧率 String
timebase streams 时基 String
start_time streams 流开始时间，单位为秒 String
duration streams 流时长，单位为秒 String
bit_rate streams 比特率，单位为kbps String
nb_frames streams 总帧数 String
language streams 语言 String
rotation streams 旋转角度 String
creation_time streams 流创建时间 String
sample_fmt streams 采样格式 String
sample_rate streams 采样率 String
channels streams 通道数量 Integer
channel_layout streams 通道格式 String

当设置 magicvar 参数时，返回内容如下：

节点名称（关键字）父节点 描述 类型
format 无 格式信息 Container
video 无 视频信息 Container
audio 无 音频信息 Container

Container 节点 video 详细信息：

节点名称（关键字）父节点 描述 类型
index video 该流的编号 Integer
codec_type video 流类型, 固定为 video String
codec_name video 编解码格式名字 String
codec_long_name video 编解码格式的详细名字 String
codec_time_base video 编码时基 String
codec_tag_string video 编码标签名 String
codec_tag video 编码标签 String
color_primaries video 色原 String
color_range video 色彩范围 String
color_transfer video 色彩通道 String
profile video 视频编码档位 String
height video 视频高，单位为px Integer
width video 视频宽，单位为px Integer
has_b_frames video 是否有 B 帧。1表示有，0表示无 String
refs video 视频编码的参考帧个数 Integer
sample_aspect_ratio video 采样宽高比 String
display_aspect_ratio video 显示宽高比 String
pix_fmt video 像素格式 String
filed_order video 场的顺序 String
level video 视频编码等级 Integer
r_frame_rate video 视频帧率 String
avg_frame_rate video 平均帧率 String
timebase video 时基 String
start_time video 视频开始时间，单位为秒 String
duration video 视频时长，单位为秒 String
bit_rate video 比特率，单位为kbps String
nb_frames video 总帧数 String
language video 语言 String
rotation video 旋转角度 String
creation_time video 流创建时间 String

Container 节点 audio 详细信息：

节点名称（关键字）父节点 描述 类型
index audio 该流的编号 Integer
codec_type audio 流类型, 固定为 audio String
codec_name audio 编解码格式名字 String
codec_long_name audio 编解码格式的详细名字 String
codec_time_base audio 编码时基 String
codec_tag_string audio 编码标签名 String
codec_tag audio 编码标签 String
sample_fmt audio 采样格式 String
sample_rate audio 采样率 String
channels audio 通道数量 Integer
channel_layout audio 通道格式 String
timebase audio 时基 String
start_time audio 音频开始时间，单位为秒 String
duration audio 音频时长，单位为秒 String
bit_rate audio 比特率，单位为kbps String
language audio 语言 String
creation_time audio 流创建时间 String

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/53983) 文档。

## 实际案例

#### 请求1 ：未设置魔法变量

GET /for-test.mp4?ci-process=avinfo HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Fri, 10 Mar 2016 09:45:46 GMT

Authorization: q-sign-algorithm=sha1&q-ak=***************************************&q-key-time=1484213027;32557109027&q-header-list=host&q-url-param-list=acl&q-signature=****************************************

Content-Length: 0

#### 响应1

HTTP/1.1 200 OK

Content-Type: application/json

Content-Length: 666

Connection: keep-alive

Date: Fri, 10 Mar 2016 09:45:46 GMT

Server: tencent-ci

x-cos-request-id: NTg3NzRiMjVfYmRjMzVfMTViMl82ZGZmNw==

{

"format": {

"bit_rate": "1166.619000",

"duration": "27.000000",

"format_long_name": "QuickTime / MOV",

"format_name": "mov,mp4,m4a,3gp,3g2,mj2",

"nb_programs": 0,

"nb_streams": 2,

"size": "3937340",

"start_time": "0.000000"

},

"streams": [{

"avg_frame_rate": "30/1",

"bit_rate": "1028.621000",

"codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",

"codec_name": "h264",

"codec_tag": "0x31637661",

"codec_tag_string": "avc1",

"codec_time_base": "1/15360",

"codec_type": "video",

"color_primaries": "bt709",

"color_range": "tv",

"color_transfer": "bt709",

"duration": "27.000000",

"has_b_frames": "2",

"height": 1280,

"index": 0,

"language": "und",

"level": 31,

"nb_frames": "810",

"pix_fmt": "yuv420p",

"profile": "High",

"r_frame_rate": "30/1",

"refs": 1,

"rotation": "0.000000",

"start_time": "0.000000",

"timebase": "1/15360",

"width": 720

}, {

"bit_rate": "129.505000",

"channel_layout": "stereo",

"channels": 2,

"codec_long_name": "AAC (Advanced Audio Coding)",

"codec_name": "aac",

"codec_tag": "0x6134706d",

"codec_tag_string": "mp4a",

"codec_time_base": "1/44100",

"codec_type": "audio",

"duration": "26.915011",

"index": 1,

"language": "und",

"sample_fmt": "fltp",

"sample_rate": "44100",

"start_time": "0.000000",

"timebase": "1/44100"

}]

}

#### 请求2 ：设置魔法变量

GET /for-test.mp4?ci-process=avinfo&magicvar=1 HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Fri, 10 Mar 2016 09:45:46 GMT

Authorization: q-sign-algorithm=sha1&q-ak=***************************************&q-key-time=1484213027;32557109027&q-header-list=host&q-url-param-list=acl&q-signature=****************************************

Content-Length: 0

#### 响应2

{

"audio": {

"bit_rate": "129.505000",

"channel_layout": "stereo",

"channels": 2,

"codec_long_name": "AAC (Advanced Audio Coding)",

"codec_name": "aac",

"codec_tag": "0x6134706d",

"codec_tag_string": "mp4a",

"codec_time_base": "1/44100",

"codec_type": "audio",

"duration": "26.915011",

"index": 1,

"language": "und",

"sample_fmt": "fltp",

"sample_rate": "44100",

"start_time": "0.000000",

"timebase": "1/44100"

},

"format": {

"bit_rate": "1166.619000",

"duration": "27.000000",

"format_long_name": "QuickTime / MOV",

"format_name": "mov,mp4,m4a,3gp,3g2,mj2",

"nb_programs": 0,

"nb_streams": 2,

"size": "3937340",

"start_time": "0.000000"

},

"video": {

"avg_frame_rate": "30/1",

"bit_rate": "1028.621000",

"codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",

"codec_name": "h264",

"codec_tag": "0x31637661",

"codec_tag_string": "avc1",

"codec_time_base": "1/15360",

"codec_type": "video",

"color_primaries": "bt709",

"color_range": "tv",

"color_transfer": "bt709",

"duration": "27.000000",

"has_b_frames": "2",

"height": 1280,

"index": 0,

"language": "und",

"level": 31,

"nb_frames": "810",

"pix_fmt": "yuv420p",

"profile": "High",

"r_frame_rate": "30/1",

"refs": 1,

"rotation": "0.000000",

"start_time": "0.000000",

"timebase": "1/15360",

"width": 720

}

}
