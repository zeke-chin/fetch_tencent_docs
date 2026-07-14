<!-- source: https://cloud.tencent.com/document/product/436/105009 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:18:14+08:00 -->

# 小程序端播放 HLS 加密视频

最近更新时间：2025-08-11 17:23:12


## 前置步骤

先**创建加密视频**，**搭建 token 服务**，详情请参见 [HLS 视频加密播实践](https://cloud.tencent.com/document/product/460/59291)。

## 小程序端播放指引

由于小程序端的 video 标签是原生支持 HLS 格式，所以以下步骤主要是计算和拼接一个可以正常被 video 标签播放的地址。步骤如下：

1. 新建小程序工程代码，在 pages/index/index.wxml 里加 video 标签。

<video src="{{src}}"></video>

2. 在 pages/index/index.js 里填入以下代码示例。

Page({

 data: {

 // 将要播放的转码后的 m3u8 视频链接

 objectKey: 'hls/video.m3u8',

 // 最终播放的 URL

 playUrl: '',

 },

 onReady: async function () {

 wx.request({

 method: 'POST',

 // 替换成自己实现的 hls token server

 // token server 参考文档：https://cloud.tencent.com/document/product/460/104024#5ea2a185-f626-4f4c-9011-cc7684c39baf

 // token server 代码示例：https://github.com/tencentyun/cos-demo/tree/main/server/hls-decrypt-token/

 url: 'https://example.com/samples/hls/getPlayUrl',

 data: JSON.stringify({

 objectKey: opt.objectKey,

 protectContentKey: 0, // 小程序不支持私有加密，需要传入 0，服务端根据 UserAgent 允许小程序来源的请求传入 0。

 }),

 header: {

 'Content-Type': 'application/json',

 },

 dataType: 'json',

 success: (res) => {

 // 由服务端决定 url 的参数、域名，拼接成播放地址给前端播放。

 const { playUrl } = res.data;

 this.setData({ playUrl: playUrl});

 },

 fail(res) {

 console.log(res);

 },

 });

 }

})

3. 在小程序开发工具上打开项目编译，即可正常播放 HLS 加密视频。

## 相关文档

[HLS 视频加密](https://cloud.tencent.com/document/product/460/104295)
