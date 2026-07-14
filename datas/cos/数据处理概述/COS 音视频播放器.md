<!-- source: https://cloud.tencent.com/document/product/436/104530 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:36:29+08:00 -->

# COS 音视频播放器

最近更新时间：2025-07-23 10:05:52


## 概述

腾讯云对象存储（COS）提供了丰富的音视频播放器代码示例，以满足不同场景下的音视频播放需求。以下介绍了代码示例中不同播放器支持的音视频协议、端侧适配性、播放功能，并基于 TCPlayer、DPlayer 和 Videojs 等第三方播放器提供了如何播放 COS 音视频文件的操作指引。

用户可以结合 [腾讯云数据万象（CI）](https://cloud.tencent.com/document/product/460/47503) 丰富的音视频处理能力，选择合适的播放器来实现更丰富、个性化的音视频体验。

**说明：**

播放存储在 COS 上的音视频文件，涉及音视频文件 [存储费用](https://cloud.tencent.com/document/product/436/53482) 和播放产生的 [流量费用](https://cloud.tencent.com/document/product/436/53863)。

## 音视频协议支持

音视频协议 URL 地址格式 PC 浏览器 移动端浏览器 iOS Android
MP3 https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp3 支持 支持 支持 支持
MP4 https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp4 支持 支持 支持 支持
HLS

(M3U8)https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.m3u8 支持 支持 支持 支持
FLV https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.flv 支持 支持 支持 支持
DASH https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mpd 支持 支持-支持

**注意：**

HLS、FLV、DASH 视频在部分浏览器环境中播放需要依赖 [Media Source Extensions](https://cloud.tencent.com/document/product/436/104530)。

## 功能支持

功能 Web iOS Android
TCPlayer 播放器 DPlayer 播放器 Videojs 播放器
播放 MP4格式视频[查看详情](https://cloud.tencent.com/document/product/460/65863#1)[查看详情](https://cloud.tencent.com/document/product/460/80408#1)[查看详情](https://cloud.tencent.com/document/product/460/80409#1)[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/ios)[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/android)
播放 HLS 格式视频[查看详情](https://cloud.tencent.com/document/product/460/65863#1)[查看详情](https://cloud.tencent.com/document/product/460/80408#1)[查看详情](https://cloud.tencent.com/document/product/460/80409#1)[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/ios)[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/android)
播放 FLV 格式视频[查看详情](https://cloud.tencent.com/document/product/460/65863#1)[查看详情](https://cloud.tencent.com/document/product/460/80408#1)[查看详情](https://cloud.tencent.com/document/product/460/80409#1)[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/ios)[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/android)
播放 DASH 格式视频[查看详情](https://cloud.tencent.com/document/product/460/65863#1)[查看详情](https://cloud.tencent.com/document/product/460/80408#1)[查看详情](https://cloud.tencent.com/document/product/460/80409#1)-[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/android)
播放 PM3U8 (私有M3U8) 视频[查看详情](https://cloud.tencent.com/document/product/460/65863#2)[查看详情](https://cloud.tencent.com/document/product/460/80408#.E6.92.AD.E6.94.BE-pm3u8-.E8.A7.86.E9.A2.91)[查看详情](https://cloud.tencent.com/document/product/460/80409#2)[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/ios)[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/android)
设置封面图[查看详情](https://cloud.tencent.com/document/product/460/65863#3)[查看详情](https://cloud.tencent.com/document/product/460/80408#3)[查看详情](https://cloud.tencent.com/document/product/460/80409#3)[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/ios)[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/android)
设置 HLS 标准加密[查看详情](https://cloud.tencent.com/document/product/460/104024)[查看详情](https://cloud.tencent.com/document/product/460/80408#4)[查看详情](https://cloud.tencent.com/document/product/460/104024)[查看详情](https://cloud.tencent.com/document/product/460/104147)[查看详情](https://cloud.tencent.com/document/product/460/104146)
切换清晰度[查看详情](https://cloud.tencent.com/document/product/460/65863#5)[查看详情](https://cloud.tencent.com/document/product/460/80408#.E5.88.87.E6.8D.A2.E5.A4.9A.E6.B8.85.E6.99.B0.E5.BA.A6)-[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/ios)[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/android)
设置动态水印[查看详情](https://cloud.tencent.com/document/product/460/65863#6)--[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/ios)[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/android)
设置左上角 LOGO-[查看详情](https://cloud.tencent.com/document/product/460/80408#6)-[查看详情](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/ios)-
设置进度预览图[查看详情](https://cloud.tencent.com/document/product/460/65863#8)----
设置字幕[查看详情](https://cloud.tencent.com/document/product/460/65863#9)----
设置多语言[查看详情](https://cloud.tencent.com/document/product/460/65863#10)----
设置贴片广告[查看详情](https://cloud.tencent.com/document/product/460/65863#7)----

## 如何播放 COS 音视频文件

[使用 TCPlayer 播放 COS 音视频文件](https://cloud.tencent.com/document/product/460/65863)

[使用 DPlayer 播放 COS 音视频文件](https://cloud.tencent.com/document/product/460/80408)

[使用 VideojsPlayer 播放 COS 音视频文件](https://cloud.tencent.com/document/product/460/80409)

[iOS 客户端播放 COS 音视频文件](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/ios)

[Android 客户端播放 COS音视频文件](https://github.com/tencentyun/cos-demo/tree/main/cos-video/examples/android)

## Demo 体验

COS 音视频体验馆提供完整的端侧（Web、Android、iOS）体验示例和代码示例，您可以通过以下方式快速体验并查看 Demo 代码。
