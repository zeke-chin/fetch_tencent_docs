<!-- source: https://cloud.tencent.com/document/product/436/54986 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:37:37+08:00 -->

# 使用 CDN 域名访问 COS 返回 HTTP ERROR 403

最近更新时间：2024-08-01 17:10:01


## 现象描述

使用内容分发网络（Content Delivery Network，CDN）域名访问对象存储（Cloud Object Storage，COS）时，返回 HTTP ERROR 403 错误码。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/b5e2cbca7c7a368f9652914ad3dc2ae8.png)

## 可能原因

CDN 加速域名为关闭状态。

## 处理步骤

1.登录 [对象存储控制台](https://console.cloud.tencent.com/cos5 "https://console.cloud.tencent.com/cos5")。

2.在左侧导航栏中，选择**存储桶列表**，进入存储桶管理页面。

3.找到需要操作的存储桶，单击该存储桶名称，进入存储桶配置页面。

4.在左侧导航栏中，选择**域名与传输管理 > 默认 CDN 加速域名**，进入默认 CDN 加速域名页面。

**注意：**

自2022年5月9日起，对象存储（Cloud Object Storage，COS）服务将不再支持新增默认 CDN 加速域名。您已开启、或曾经开启的默认 CDN 加速域名不会受到影响，可以继续使用，但建议您使用自定义 CDN 加速域名代替默认 CDN 加速域名。关于自定义 CDN 加速域名的操作指引，请参见 [开启自定义 CDN 加速域名](https://cloud.tencent.com/document/product/436/36637 "https://cloud.tencent.com/document/product/436/36637") 文档。

5.在“默认 CDN 加速域名”栏中，检查当前状态是否为关闭状态。

是，请 [开启默认 CDN 加速域名](https://cloud.tencent.com/document/product/436/36636 "https://cloud.tencent.com/document/product/436/36636")。

否，请执行下一步。

6.在“自定义 CDN 加速域名”栏中，检查状态是否为已上线。

是，请 [联系我们](https://cloud.tencent.com/document/product/436/37708 "https://cloud.tencent.com/document/product/436/37708")。

否，请 [开启自定义 CDN 加速域名](https://cloud.tencent.com/document/product/436/36637 "https://cloud.tencent.com/document/product/436/36637")。
