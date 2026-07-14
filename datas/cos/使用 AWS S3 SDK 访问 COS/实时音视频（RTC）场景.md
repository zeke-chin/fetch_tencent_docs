<!-- source: https://cloud.tencent.com/document/product/436/81324 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:19:03+08:00 -->

# 实时音视频（RTC）场景

最近更新时间：2025-09-02 15:52:52


## 概述

随着低延时的实时音视频技术越来越成熟，也吸引了越来越多的用户使用实时音视频产品开发实现自己的音视频业务。在拓展音视频业务的同时，如何更好的管控音视频内容避免违规尤为重要。

为更好的支持用户在各种业务场景下的内容安全风险，对象存储与数据万象在原有静态音视频审核的基础上，进一步提供了流式音视频的审核，当用户直播内容属于违规内容时，可以及时发现并进行处理。

以腾讯云实时音视频产品（Tencent Real-Time Communication，TRTC）为例，整体审核流程如下图所示：

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/4e9e0eb4bf88bdc6f7ca20f32a4f13df.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/4e9e0eb4bf88bdc6f7ca20f32a4f13df.png)

流程如下：

1. TRTC 客户端发起直播请求。

2. TRTC 服务端收到请求后进行直播。

3. 通过 [发布音视频流到直播 CDN](https://cloud.tencent.com/document/product/647/84721) 可以拿到所需的直播流地址，有 rtmp、flv、hls 三种格式可用。

4. 使用万象直播流审核接口进行直播审核，SDK 封装此接口方便用户下载使用。

5. 客户拿到审核回调进行后续业务处理。

## 实践步骤

### 1. 创建存储桶

如果您已创建存储桶，可跳过该步骤。

如果您是首次使用 COS 控制台，可参考 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 进行操作。

### 2. 创建 TRTC 应用

如果您已创建 TRTC 应用，且能够使用 TRTC 相关功能时，可直接跳转到 [步骤4. 开启旁路推流](https://cloud.tencent.com/document/product/436/81324#4.-.E5.BC.80.E5.90.AF.E6.97.81.E8.B7.AF.E6.8E.A8.E6.B5.81)。

1. 登录 [TRTC 控制台](https://console.cloud.tencent.com/trtc)，单击**应用管理**，可以看到应用列表，单击**创建应用**，相关说明可参见 [创建应用](https://cloud.tencent.com/document/product/647/50493)。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/5c5b5a0101fdfa48677cb0aaf1100af6.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/5c5b5a0101fdfa48677cb0aaf1100af6.png)

2. 创建应用后，单击应用列表右侧的**详情**，可以看到应用概览，其中`SDKAppID`、`SDK密钥`需要在后续流程中用到，可以先记录下来。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/49a88b37e885c6e5bfb84d8c587f5c41.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/49a88b37e885c6e5bfb84d8c587f5c41.png)

3. 完成以上步骤，我们获取了 `SDKAppID`、`SDK密钥` 这两个重要数据，切记不要泄露这些数据。接下来可以开始对 TRTC DEMO 进行搭建。

### 3. TRTC DEMO 搭建流程

本 DEMO 目的是使客户快速了解直播流程，客户业务需求的具体实现可参见 [TRTC 官网使用文档](https://cloud.tencent.com/document/product/647)。流程如下：

1. 下载所需平台的 [SDK&Demo 源码](https://console.cloud.tencent.com/trtc/helpcenter)，直接下载 ZIP 包即可，本次示例使用的是 Android 平台。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/2222302fcfb07e7a707e0b8329a41f74.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/2222302fcfb07e7a707e0b8329a41f74.png)

2. 配置 TRTC-API-Example 工程文件。找到并打开 `LiteAVSDK_TRTC_Android_版本号/TRTC-API-Example/Debug/src/main/java/com/tencent/trtc/debug/GenerateTestUserSig.java` 文件。相关参数说明如下：

BIZID：默认为 PLACEHOLDER ，请设置为实际的 bizid，暂不使用 CDN 时请用0替换，以便编译通过。

APPID：默认为 PLACEHOLDER ，请设置为实际的 appid，暂不使用 CDN 时请用0替换，以便编译通过。

SDKAPPID：默认为 PLACEHOLDER ，请设置为实际的 SDKAppID（上面流程已获取，即`SDKAppID`）。

SECRETKEY：默认为 PLACEHOLDER ，请设置为实际的 SecretKey（上面流程已获取，即`SDKSecretKey`）。

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/f3964f0aa352c05489b714f10c25ebf2.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/f3964f0aa352c05489b714f10c25ebf2.png)

3. 编译运行。使用 Android Studio 打开源码工程 TRTC-API-Example，单击**运行**即可。运行成功后页面如下图所示，TRTC DEMO 提供视频通话、录屏直播等多种功能示例。

![Image 12](https://qcloudimg.tencent-cloud.cn/image/document/78f2d7de0c8baf18d3892ebef98ef585.png)

![Image 13](https://qcloudimg.tencent-cloud.cn/image/document/78f2d7de0c8baf18d3892ebef98ef585.png)

### 4. 开启旁路推流

1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/trtc)。

2. 在左侧导航栏选择**应用管理**，单击目标应用右侧的**配置**。

3. 在**旁路转推配置**中，单击**开启旁路转推**右侧的

![Image 14: img](https://qcloudimg.tencent-cloud.cn/image/document/ff6c0eb6278b579ef0055aed84d3a9bd.png)

![Image 15](https://qcloudimg.tencent-cloud.cn/image/document/ff6c0eb6278b579ef0055aed84d3a9bd.png)

，在弹出的**开启旁路转推功能**对话框中，单击**开启旁路转推功能**即可开通。

![Image 16](https://qcloudimg.tencent-cloud.cn/image/document/d6a21a413952e805ebdb5a16ef9fbad2.png)

![Image 17](https://qcloudimg.tencent-cloud.cn/image/document/d6a21a413952e805ebdb5a16ef9fbad2.png)

### 5. 云直播 CDN 拉流

可以通过 [发布音视频流到直播 CDN](https://cloud.tencent.com/document/product/647/84721) 获取到直播流数据，最后生成一条直播流地址，有 rtmp、flv、hls 三种协议可用。

 rtmp 协议的播放地址：rtmp://example.myhost.com/AppName_example/StreamName_example

 flv 协议的播放地址：http://example.myhost.com/AppName_example/StreamName_example.flv

 hls 协议的播放地址：http://example.myhost.com/AppName_example/StreamName_example.m3u8

我们推荐以 `http` 为前缀且以 `.flv` 为后缀的 **http - flv** 地址，该地址的播放具有时延低、秒开效果好且稳定可靠的特点。

### 6. 调用审核接口

获取到直播流后，使用万象的直播流审核接口进行直播审核。

直播流审核可使用对应语言的 [COS SDK](https://cloud.tencent.com/document/product/436/6474)。

直播审核参数说明，请参见 [提交直播审核任务](https://cloud.tencent.com/document/product/460/76261)。

直播审核回调内容，请参见 [直播审核回调内容](https://cloud.tencent.com/document/product/460/76266)。

提交审核时可以设置客户业务信息，审核回调时会原样返回，拿到审核回调后可以得到具体房间或具体用户的违规情况。相关参数说明，请参见 [UserInfo 节点说明](https://cloud.tencent.com/document/product/436/76260#.E8.AF.B7.E6.B1.82)。

### 7. 违规解散房间或踢用户

收到回调后判断是否违规，发现违规后发起解散房间或移出用户等处置操作，其他API接口可以参见 [客户端 API](https://cloud.tencent.com/document/product/647/94380)、[服务端 API](https://cloud.tencent.com/document/product/647/37077)。

[移出用户](https://cloud.tencent.com/document/product/647/40496)

[解散房间](https://cloud.tencent.com/document/product/647/50089)
