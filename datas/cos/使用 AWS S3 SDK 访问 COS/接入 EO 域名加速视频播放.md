<!-- source: https://cloud.tencent.com/document/product/436/124372 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:18:18+08:00 -->

# 接入 EO 域名加速视频播放

最近更新时间：2026-06-12 11:10:32


## 使用加速域名播放的特点

**缓存逻辑**：加密的 ts 文件可正常缓存以提升访问速度；而 m3u8、getDecryptionKey 请求因需实时获取最新信息，要特殊配置为不缓存，每次请求均回源至 COS。

**EdgeOne 鉴权机制**：推荐开启 EdgeOne 鉴权功能，同时需通过边缘函数对 m3u8 请求进行改写，实现对返回内容中的 .ts url 自动添加 EdgeOne 签名，形成资源保护的第一道防线。

**回源鉴权保护**：为保障视频资源安全，推荐将 COS 存储桶的 ACL 访问权限设为私有读，并在 EdgeOne 域名配置中开启回源鉴权，进一步强化资源安全性。

## 前提条件

请先参考 [HLS 视频加密播放实践](https://cloud.tencent.com/document/product/460/59291)，完成 HLS Token 服务的搭建及 Web 播放示例的配置。

## 接入 EdgeOne 域名

### 添加域名并设置源站

登录 [EdgeOne 控制台](https://console.cloud.tencent.com/edgeone)，选择**基础服务**>**域名服务**>**域名管理**，添加域名并配置源站为**对象存储源站**，选择相应的存储桶并开启**私有访问授权**。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/e42696a0be50034b13b55b1c2bc9e312.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/e42696a0be50034b13b55b1c2bc9e312.png)

### 配置鉴权和缓存规则

在 [EdgeOne 控制台](https://console.cloud.tencent.com/edgeone)，进入**加速与安全**>**站点加速**>**规则引擎**，修改规则配置。

1. 对站点域名开启 EdgeOne 鉴权，保存好鉴权密钥。

2. 对带有请求参数 ci-process 的请求，特殊配置为**不缓存**。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/2f74586520d3b4a70deb9c2f8e3d9024.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/2f74586520d3b4a70deb9c2f8e3d9024.png)

### 配置边缘函数改写 m3u8请求

在 [EdgeOne 控制台](https://console.cloud.tencent.com/edgeone)，进入**边缘函数**>**函数管理**，根据 [edge-functions.zip](https://cosbrowser.cloud.tencent.com/code/hls/edge-functions.zip) 代码配置，按需修改最前面的代码里的鉴权密钥 PK、签名有效时间 TTL、签名参数名 KEY_NAME。保存并发布函数。并在函数触发配置里，指定触发条件为查询字符串带有 ci-process = pm3u8 的请求。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/32a74b0bc442102b199b8c0a29355684.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/32a74b0bc442102b199b8c0a29355684.png)

### 修改 HLS Token 服务生成 EO 域名链接

1. 改写 HLS Token 服务代码（示例：[Node.js 示例](https://github.com/tencentyun/cos-demo/tree/main/server/hls-decrypt-token/nodejs)、[Go 示例](https://github.com/tencentyun/cos-demo/tree/main/server/hls-decrypt-token/go)），对返回的 url 使用 EdgeOne 的域名，并使用 EdgeOne 的鉴权密钥实现 [EdgeOne 的 sign 签名计算](https://cloud.tencent.com/document/product/1552/71007) ，在 url 上带上签名。

2. 尝试在前端页面播放视频，会看到 pm3u8 请求返回的 .ts 链接已被替换为带有 EdgeOne 签名`?sign=xxx`的链接，并且能正常播放 COS HLS 私有加密视频。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/d7df51fcc50896bfbe0cd25027149149.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/d7df51fcc50896bfbe0cd25027149149.png)

通过以上步骤，可借助 EdgeOne 的加速能力，在保障 HLS 私有加密视频安全的前提下，实现高效、稳定的播放体验。
