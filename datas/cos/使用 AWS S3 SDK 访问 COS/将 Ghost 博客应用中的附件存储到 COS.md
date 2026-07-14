<!-- source: https://cloud.tencent.com/document/product/436/81829 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:21:22+08:00 -->

# 将 Ghost 博客应用中的附件存储到 COS

最近更新时间：2024-11-15 21:48:52


## 简介

[Ghost](https://ghost.org/docs) 是一个基于 Node.js 快速搭建博客类网站的框架，开发者可通过 Ghost 官方 cli 工具一键生成自己的个人网站，并支持部署到云服务器和 Docker 上。

作为一个博客类网站，上传附件是必不可少的功能，Ghost 默认会将附件存储在本地，本文将介绍如何通过插件将附件保存在 [腾讯云对象存储（Cloud Object Storage，COS）](https://cloud.tencent.com/product/cos) 上，将论坛附件保存在 COS 上有以下好处：

附件将拥有更高的可靠性。

您的服务器无需为论坛附件准备额外的存储空间。

用户查看图片附件时将直连 COS 服务器，不占用您服务器的下行带宽/流量，用户访问速度更快。

可配合 [腾讯云内容分发网络（Content Delivery Network，CDN）](https://cloud.tencent.com/product/cdn) 进一步提升论坛用户查看图片附件的速度。

## 准备工作

**说明：**

本文提供的Ghost安装教程基于MacOS系统，如需在其他系统（如Windows、Linux）安装，请参考Ghost官网[安装文档](https://ghost.org/docs/install/)。

### 搭建 Ghost 网站

1. 安装 [Node.js](https://nodejs.org/en/download/) 环境。

2. 安装 ghost-cli。

npm install ghost-cli@latest -g

3. 创建一个项目，在该项目的根目录下执行命令：

ghost install local

创建成功后的项目结构如下图所示：

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/78836149a69faab33678f315230964d4.jpg)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/78836149a69faab33678f315230964d4.jpg)

4. 打开浏览器，进入 localhost:2368，出现注册页面，注册后进入管理后台。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/1d39baeefc7c911f378be9912cf84f8b.jpg)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/1d39baeefc7c911f378be9912cf84f8b.jpg)

### 创建 COS 存储桶

1. 在 [COS 控制台](https://console.cloud.tencent.com/cos/bucket) 创建一个访问权限为**公有读私有写**的存储桶，操作指引可参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。

2. 单击**安全管理 > 跨域访问 CORS 设置**，添加一行跨域设置，为方便调试可使用以下配置，操作指引可参见 [设置跨域访问](https://cloud.tencent.com/document/product/436/13318)。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/45d501384501a5170e7235a367983df5.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/45d501384501a5170e7235a367983df5.png)

## 将 Ghost 关联到 COS存储桶

**注意：**

建议使用子账号密钥，授权遵循 [最小权限指引](https://cloud.tencent.com/document/product/436/38618)，降低使用风险。子账号密钥获取可参考 [子账号访问密钥管理](https://cloud.tencent.com/document/product/598/37140)。

1. 修改 Ghost 项目根目录下的 config.development.json 配置文件，添加如下配置：

 "storage": {

 "active": "ghost-cos-store",

 "ghost-cos-store": {

 "BasePath": "ghost/", // 可修改为自己的目录名，不填写则默认根目录

 "SecretId": "************************************",

 "SecretKey": "***************",

 "Bucket": "xxx-125********",

 "Region": "**-*******",

 "QueryString": "?********"

 }

 }

参数说明如下：

配置项 配置值 类型 是否必选
BasePath 文件所存储的 COS 路径，可自行修改，不填写则默认根目录 string 否
SecretId 访问密钥信息，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中创建和获取 string 是
SecretKey 访问密钥信息，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中创建和获取。string 是
Bucket 创建存储桶时自定义的名称，例如 examplebucket-1250000000。string 是
Region 创建存储桶时所选择的地域，例如 ap-guangzhou。string 是
QueryString 查询参数，如万象图片处理参数 ?imageMogr2/format/<format>。string 否

2. 创建自定义存储目录，在ghost项目根目录下执行：

mkdir -p content/adapters/storage

3. 安装腾讯云官方提供的 [ghost-cos-store](https://github.com/tencentyun/ghost-cos-store) 插件。

3.1 通过 npm 安装。

cd content/adapters/storage // 需要在自定义存储目录下安装

npm install ghost-cos-store

3.2 在 storage 目录下创建 ghost-cos-store.js 文件，内容如下：

// content/adapters/storage/ghost-cos-store.js

module.exports = require('ghost-cos-store');

3.3 安装完成后，需要重启 Ghost。

ghost restart

## 发文并进行上传测试

1. 进入 Ghost 管理后台，单击发表一篇文章。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/aae08158738146ea518ca4985f2fc00e.jpg)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/aae08158738146ea518ca4985f2fc00e.jpg)

2. 单击上传图片，在浏览器抓包可以看到 upload 请求成功，并返回了图片对应的 COS 链接。

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/ffe48ae86dac61c626b3e38c2cb14b5c.jpg)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/ffe48ae86dac61c626b3e38c2cb14b5c.jpg)

## 使用数据万象处理上传的图片

ghost-cos-store插件支持配置QueryString参数，如果存储桶绑定了数据万象，可以通过加 url 参数，使用数据万象的图片压缩、转换格式、水印添加等操作。

### 准备工作

在使用图片处理功能之前，需要先在**存储桶详情页-数据处理-图片处理页面**开启对应的开关。

![Image 12](https://qcloudimg.tencent-cloud.cn/image/document/ea6af70d1d55cbd2abc2fac249a44622.png)

![Image 13](https://qcloudimg.tencent-cloud.cn/image/document/ea6af70d1d55cbd2abc2fac249a44622.png)

### 使用案例

开启了功能开关之后，可以在 config.development.json 配置文件里配置 QueryString 来使用，如：

1. 将上传后的图片转换格式后展示，具体参数可查看[图片高级压缩](https://cloud.tencent.com/document/product/436/60450)。

{

 "QueryString": "?imageMogr2/format/avif" // 将图片转换为avif格式后展示，支持tpg/avif/heif等格式

}

2. 使用[极智压缩](https://cloud.tencent.com/document/product/436/96675)压缩图片（目前仅支持北京，上海园区的存储桶）。

{

 "QueryString": "?imageSlim"

}

### 处理效果

配置后，在文章编辑页里上传图片，图片后面会自动带上处理参数。

1. 触发了格式转换：

![Image 14](https://qcloudimg.tencent-cloud.cn/image/document/c703b70d7d9cde1887c2b246f4af919a.png)

![Image 15](https://qcloudimg.tencent-cloud.cn/image/document/c703b70d7d9cde1887c2b246f4af919a.png)

2. 触发了极智压缩：

![Image 16](https://qcloudimg.tencent-cloud.cn/image/document/ef4aabb145e2d0ac13e29d477c4a69e2.png)

![Image 17](https://qcloudimg.tencent-cloud.cn/image/document/ef4aabb145e2d0ac13e29d477c4a69e2.png)

## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击“[此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406)”一键启动，立即使用！
