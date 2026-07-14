<!-- source: https://cloud.tencent.com/document/product/436/101601 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:17:02+08:00 -->

# 配置自定义 CDN 域名支持 Gzip 压缩

最近更新时间：2024-10-24 15:19:52


## 简介

本文仅介绍如何在对象存储（Cloud Object Storage，COS）控制台上配置 Gzip 压缩。若要在 CDN 控制台添加，请参见 CDN [智能压缩配置](https://cloud.tencent.com/document/product/228/41736) 文档。

## 操作步骤

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5) 。

2.  在左侧导航栏中，单击**存储桶列表**，进入存储桶列表页面。

3. 单击需要配置 Gzip 压缩的存储桶，进入存储桶配置页面。

4. 单击左侧的**域名与传输管理 > 自定义 CDN 加速域名**配置项。若无可用域名，请先添加域名。具体配置请参考 [开启自定义 CDN 加速域名](https://cloud.tencent.com/document/product/436/36637)。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/6121cbd28e6b55bf382b98612f52a8df.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/6121cbd28e6b55bf382b98612f52a8df.png)

5. 域名添加成功后，默认为该域名开启 CDN 智能压缩功能，并创建一条 Gzip 压缩规则。

该 Gzip 压缩规则详情如下：

**类型：**文件后缀

**内容：**js;html;css;xml;json;shtml;htm

**文件范围：**256Byte ~ 2MB

**压缩方式：**Gzip

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/8131631f5400b6fe1ed488af405bcc35.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/8131631f5400b6fe1ed488af405bcc35.png)

6. 在**个性化配置**列中的 **CDN 智能压缩**，可查看 Gzip 压缩的配置状态和已配置的压缩方式。

若显示“未配置”，指未开启 CDN 智能压缩配置状态。

为了减少传输文件大小，节省开销，推荐开启 CDN 智能压缩功能。可点击气泡，根据提示单击“CDN 控制台”，快捷跳转至 CDN 控制台进行配置。操作指引请参见 [智能压缩配置](https://cloud.tencent.com/document/product/228/41736)。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/981c450b40dcf239287da8db19c45fbf.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/981c450b40dcf239287da8db19c45fbf.png)

若显示“gzip”或其他字段，指当前配置的压缩方式。

如需新增，修改或查看 CDN 智能压缩规则（例如压缩方式、类型、内容、文件范围等），可点击气泡，根据提示单击“CDN 控制台”，快捷跳转至 CDN 控制台进行配置。操作指引请参见 [智能压缩配置](https://cloud.tencent.com/document/product/228/41736)。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/af1ae75659b9c5e0db29fc58309401f1.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/af1ae75659b9c5e0db29fc58309401f1.png)

**说明**

 有关智能压缩配置规则的更多信息，例如配置约束、规则生效优先级等，请参见内容分发网络 CDN 配置指南中的 [智能压缩配置](https://cloud.tencent.com/document/product/228/41736)。
