<!-- source: https://cloud.tencent.com/document/product/436/80454 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:18:25+08:00 -->

# COS 音视频播放器概述

最近更新时间：2026-03-20 11:23:21


## 协议支持

音视频协议 URL 地址格式 PC 浏览器 移动端浏览器
MP3 https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp3 支持 支持
MP4 https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp4 支持 支持
HLS

(M3U8)https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.m3u8 支持 支持
FLV https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.flv 支持 支持
DASH https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mpd 支持 支持

**注意：**

HLS、FLV、DASH 视频在部分浏览器环境中播放需要依赖 [Media Source Extensions](https://caniuse.com/?search=Media+Source+Extensions)。

## 功能支持

功能 TCPlayer 播放器 DPlayer 播放器 Videojs 播放器
播放 MP4 格式视频[查看详情](https://cloud.tencent.com/document/product/460/65863#1)[查看详情](https://cloud.tencent.com/document/product/460/80408#1)[查看详情](https://cloud.tencent.com/document/product/460/80409#1)
播放 HLS 格式视频[查看详情](https://cloud.tencent.com/document/product/460/65863#1)[查看详情](https://cloud.tencent.com/document/product/460/80408#1)[查看详情](https://cloud.tencent.com/document/product/460/80409#1)
播放 FLV 格式视频[查看详情](https://cloud.tencent.com/document/product/460/65863#1)[查看详情](https://cloud.tencent.com/document/product/460/80408#1)[查看详情](https://cloud.tencent.com/document/product/460/80409#1)
播放 DASH 格式视频[查看详情](https://cloud.tencent.com/document/product/460/65863#1)[查看详情](https://cloud.tencent.com/document/product/460/80408#1)[查看详情](https://cloud.tencent.com/document/product/460/80409#1)
播放 PM3U8（私有 M3U8）视频[查看详情](https://cloud.tencent.com/document/product/460/65863#2)[查看详情](https://cloud.tencent.com/document/product/460/80408#.E6.92.AD.E6.94.BE-pm3u8-.E8.A7.86.E9.A2.91)[查看详情](https://cloud.tencent.com/document/product/460/80409#2)
设置封面图[查看详情](https://cloud.tencent.com/document/product/460/65863#3)[查看详情](https://cloud.tencent.com/document/product/460/80408#3)[查看详情](https://cloud.tencent.com/document/product/460/80409#3)
设置 HLS 标准加密[查看详情](https://cloud.tencent.com/document/product/460/65863#4)[查看详情](https://cloud.tencent.com/document/product/460/80408#4)[查看详情](https://cloud.tencent.com/document/product/460/80409#4)
切换清晰度[查看详情](https://cloud.tencent.com/document/product/460/65863#5)[查看详情](https://cloud.tencent.com/document/product/460/80408#.E5.88.87.E6.8D.A2.E5.A4.9A.E6.B8.85.E6.99.B0.E5.BA.A6)-
设置动态水印[查看详情](https://cloud.tencent.com/document/product/460/65863#6)--
设置左上角 LOGO-[查看详情](https://cloud.tencent.com/document/product/460/80408#6)-
设置进度预览图[查看详情](https://cloud.tencent.com/document/product/460/65863#8)--
设置字幕[查看详情](https://cloud.tencent.com/document/product/460/65863#9)--
设置多语言[查看详情](https://cloud.tencent.com/document/product/460/65863#10)--
设置贴片广告[查看详情](https://cloud.tencent.com/document/product/460/65863#7)--

**说明：**

播放器兼容常见的浏览器，播放器内部会自动区分平台，并使用最优的播放方案。例如在 Chrome 等现代浏览器中优先使用 HTML5 技术实现视频播放，而手机浏览器上会使用 HTML5 技术或者浏览器内核能力实现视频播放。

## 使用指引

[使用 TCPlayer 播放 COS 视频文件](https://cloud.tencent.com/document/product/460/65863)

[使用 DPlayer 播放 COS 视频文件](https://cloud.tencent.com/document/product/460/80408)

[使用 VideojsPlayer 播放 COS 视频文件](https://cloud.tencent.com/document/product/460/80409)

## Demo 体验

### Web 端体验

您可直接在电脑端浏览器访问 [COS 音视频体验馆](https://cloud.tencent.com/act/pro/cos-video)，体验 COS 的音视频处理功能。

### 移动端体验

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/d89b00e8188f050e7cb9df3ec950bdfb.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/d89b00e8188f050e7cb9df3ec950bdfb.png)

### 示例代码

前往 GitHub [获取示例代码](https://github.com/tencentyun/cos-demo/tree/main/cos-video)。
