<!-- source: https://cloud.tencent.com/document/product/436/96289 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:53:54+08:00 -->

# 转码Pro模板接口

最近更新时间：2025-12-30 10:10:53


## 简介

本文档提供关于音视频转码 pro 模板接口的 API 概览和 SDK 示例代码。

**注意**

 旧版本可能存在 bug，使用时建议升级到 [最新版本](https://github.com/tencentyun/cos-php-sdk-v5/releases/)。

API 操作描述
[创建模板 转码pro（广电专业格式）](https://cloud.tencent.com/document/product/460/84732)创建音视频转码 pro 模板
[更新模板 转码 pro](https://cloud.tencent.com/document/product/460/84753)更新音视频转码 pro 模板

## 创建转码 Pro 模板（广电专业格式）

#### 功能说明

创建音视频转码 pro 模板。

#### 方法原型

public Guzzle\Service\Resource\Model createMediaTranscodeProTemplate(array $args = array());

#### 请求示例

<?php

require dirname( __FILE__ , 2) . '/vendor/autoload.php';

$secretId = "SECRETID"; //替换为用户的 secretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi

$secretKey = "SECRETKEY"; //替换为用户的 secretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi

$region = "ap-beijing"; //替换为用户的 region，已创建桶归属的 region 可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket

$cosClient = new Qcloud\Cos\Client(

 array(

 'region' => $region,

 'scheme' => 'https', //协议头部，默认为http

 'credentials'=> array(

 'secretId' => $secretId ,

 'secretKey' => $secretKey)));

try {

 // 创建音视频转码 pro 模板 https://cloud.tencent.com/document/product/460/84732

 $result = $cosClient->createMediaTranscodeProTemplate(array(

 'Bucket' => 'examplebucket-125000000', //存储桶名称，由BucketName-Appid 组成，可以在COS控制台查看 https://console.cloud.tencent.com/cos5/bucket

 'Tag' => 'TranscodePro',

 'Name' => 'media-transcode-pro-name',

 'Container' => array(

 'Format' => 'mxf',

 ),

 'Video' => array(

 'Codec' => 'xavc',

 'Profile' => 'XAVC-HD_intra_420_10bit_class50',

 'Width' => '1440',

 'Height' => '1080',

 'Interlaced' => 'true',

 'Fps' => '30000/1001',

 'Bitrate' => '',

 'Rotate' => '',

 ),

 'TimeInterval' => array(

 'Start' => '',

 'Duration' => '',

 ),

 'Audio' => array(

 'Codec' => '',

 'Remove' => '',

 ),

 'TransConfig' => array(

 'AdjDarMethod' => '',

 'IsCheckReso' => '',

 'ResoAdjMethod' => '',

 'IsCheckVideoBitrate' => '',

 'VideoBitrateAdjMethod' => '',

 'IsCheckAudioBitrate' => '',

 'AudioBitrateAdjMethod' => '',

 'IsCheckVideoFps' => '',

 'VideoFpsAdjMethod' => '',

 'DeleteMetadata' => '',

 'IsHdr2Sdr' => '',

 ),

 ));

 // 请求成功

 print_r($result);

} catch (\Exception $e) {

 // 请求失败

 echo($e);

}

#### 参数说明

Request 中的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
Tag Request 模板类型：TranscodePro String 是
Name Request 模板名称 仅支持中文、英文、数字、_、-和* ，长度不超过 64 String 是
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

#### 返回结果示例

GuzzleHttp\Command\Result Object

(

 [RequestId] => NjRjMzYNjRjMjIxODBfMzUxNGSIOJOIDAJOIDg=

 [ContentType] => application/xml

 [ContentLength] => 1854

 [Template] => Array

 (

 [State] => Normal

 [TemplateId] => t1ca2f19asf798sd7f89s7f2e646

 [Name] => media-transcode-pro-name

 [BucketId] => examplebucket-1250000000

 [Category] => Custom

 [Tag] => TranscodePro

 [UpdateTime] => 2023-07-28 T15:02:44+0800

 [CreateTime] => 2023-07-28 T15:02:44+0800

 [TransProTpl] => Array

 (

 [Container] => Array

 (

 [Format] => mxf

 )

 [Video] => Array

 (

 [Codec] => xavc

 [Profile] => XAVC-HD_intra_420_10bit_class50

 [Width] => 1440

 [Height] => 1080

 [Interlaced] => true

 [Fps] => 30000/1001

 [Bitrate] =>

 [Rotate] =>

 )

 [TimeInterval] => Array

 (

 [Start] =>

 [Duration] =>

 )

 [Audio] => Array

 (

 [Codec] => pcm_s24le

 [Remove] => false

 )

 [TransConfig] => Array

 (

 [IsStreamCopy] => false

 [HlsEncrypt] => Array

 (

 [IsHlsEncrypt] => false

 [UriKey] =>

 [PlainText] =>

 [CiphertextBlob] =>

 [KmsRegion] =>

 )

 [DashEncrypt] => Array

 (

 [IsEncrypt] => false

 [UriKey] =>

 [PlainText] =>

 [CiphertextBlob] =>

 [KmsRegion] =>

 [KeyID] =>

 )

 [TranscodeIndex] =>

 [AdjDarMethod] => none

 [IsCheckReso] => false

 [ResoAdjMethod] => 0

 [IsCheckVideoBitrate] => false

 [VideoBitrateAdjMethod] => 0

 [IsCheckAudioBitrate] => false

 [AudioBitrateAdjMethod] => 0

 [IsCheckVideoFps] => false

 [VideoFpsAdjMethod] => 0

 [DeleteMetadata] => false

 [IsHdr2Sdr] => false

 )

 )

 )

 [Bucket] => examplebucket-1250000000

 [Location] => examplebucket-1250000000.ci.ap-guangzhou.myqcloud.com/template

)

## 更新转码Pro模板

#### 功能说明

更新音视频转码 pro 模板。

#### 方法原型

public Guzzle\Service\Resource\Model updateMediaTranscodeProTemplate(array $args = array());

#### 请求示例

<?php

require dirname( __FILE__ , 2) . '/vendor/autoload.php';

$secretId = "SECRETID"; //替换为用户的 secretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi

$secretKey = "SECRETKEY"; //替换为用户的 secretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi

$region = "ap-beijing"; //替换为用户的 region，已创建桶归属的 region 可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket

$cosClient = new Qcloud\Cos\Client(

 array(

 'region' => $region,

 'scheme' => 'https', //协议头部，默认为http

 'credentials'=> array(

 'secretId' => $secretId ,

 'secretKey' => $secretKey)));

try {

 // 更新音视频转码 pro 模板 https://cloud.tencent.com/document/product/460/84753

 $result = $cosClient->updateMediaTranscodeProTemplate(array(

 'Bucket' => 'examplebucket-125000000', //存储桶名称，由BucketName-Appid 组成，可以在COS控制台查看 https://console.cloud.tencent.com/cos5/bucket

 'Key' => '', // TemplateId

 'Tag' => 'TranscodePro',

 'Name' => 'media-transcode-pro-name',

 'Container' => array(

 'Format' => 'mxf',

 ),

 'Video' => array(

 'Codec' => 'xavc',

 'Profile' => 'XAVC-HD_intra_420_10bit_class50',

 'Width' => '1440',

 'Height' => '1080',

 'Interlaced' => 'true',

 'Fps' => '30000/1001',

 'Bitrate' => '',

 'Rotate' => '',

 ),

 'TimeInterval' => array(

 'Start' => '',

 'Duration' => '',

 ),

 'Audio' => array(

 'Codec' => '',

 'Remove' => '',

 ),

 'TransConfig' => array(

 'AdjDarMethod' => '',

 'IsCheckReso' => '',

 'ResoAdjMethod' => '',

 'IsCheckVideoBitrate' => '',

 'VideoBitrateAdjMethod' => '',

 'IsCheckAudioBitrate' => '',

 'AudioBitrateAdjMethod' => '',

 'IsCheckVideoFps' => '',

 'VideoFpsAdjMethod' => '',

 'DeleteMetadata' => '',

 'IsHdr2Sdr' => '',

 ),

 ));

 // 请求成功

 print_r($result);

} catch (\Exception $e) {

 // 请求失败

 echo($e);

}

#### 参数说明

Request 中的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 必选
Request 无 同创建转码 Pro 模板接口的 [Request](https://cloud.tencent.com/document/product/460/84732#Request)Container 是

#### 返回结果示例

GuzzleHttp\Command\Result Object

(

 [RequestId] => NjRjMzZNjRjMjIxODBfMzUxNGSIOJOIDAJOIDg=

 [ContentType] => application/xml

 [ContentLength] => 1854

 [Template] => Array

 (

 [State] => Normal

 [TemplateId] => t1ca2104pc7a00f19asf798sd7f89s7f2e646

 [Name] => media-transcode-pro-name

 [BucketId] => examplebucket-1250000000

 [Category] => Custom

 [Tag] => TranscodePro

 [UpdateTime] => 2023-07-28 T15:22:33+0800

 [CreateTime] => 2023-07-28 T15:02:44+0800

 [TransProTpl] => Array

 (

 [Container] => Array

 (

 [Format] => mxf

 )

 [Video] => Array

 (

 [Codec] => xavc

 [Profile] => XAVC-HD_intra_420_10bit_class50

 [Width] => 1440

 [Height] => 1080

 [Interlaced] => true

 [Fps] => 30000/1001

 [Bitrate] =>

 [Rotate] =>

 )

 [TimeInterval] => Array

 (

 [Start] =>

 [Duration] =>

 )

 [Audio] => Array

 (

 [Codec] => pcm_s24le

 [Remove] => false

 )

 [TransConfig] => Array

 (

 [IsStreamCopy] => false

 [HlsEncrypt] => Array

 (

 [IsHlsEncrypt] => false

 [UriKey] =>

 [PlainText] =>

 [CiphertextBlob] =>

 [KmsRegion] =>

 )

 [DashEncrypt] => Array

 (

 [IsEncrypt] => false

 [UriKey] =>

 [PlainText] =>

 [CiphertextBlob] =>

 [KmsRegion] =>

 [KeyID] =>

 )

 [TranscodeIndex] =>

 [AdjDarMethod] => none

 [IsCheckReso] => false

 [ResoAdjMethod] => 0

 [IsCheckVideoBitrate] => false

 [VideoBitrateAdjMethod] => 0

 [IsCheckAudioBitrate] => false

 [AudioBitrateAdjMethod] => 0

 [IsCheckVideoFps] => false

 [VideoFpsAdjMethod] => 0

 [DeleteMetadata] => false

 [IsHdr2Sdr] => false

 )

 )

 )

 [Key] => t1ca2104pc7a00f19asf798sd7f89s7f2e646

 [Bucket] => examplebucket-1250000000

 [Location] => examplebucket-1250000000.ci.ap-guangzhou.myqcloud.com/template/t1ca2104pc7a00f19asf798sd7f89s7f2e646

)
