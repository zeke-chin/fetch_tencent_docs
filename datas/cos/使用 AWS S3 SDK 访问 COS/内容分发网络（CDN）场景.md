<!-- source: https://cloud.tencent.com/document/product/436/71471 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:18:57+08:00 -->

# 内容分发网络（CDN）场景

最近更新时间：2025-09-02 15:52:52


## 简介

内容审核功能提供了自动冻结能力，可以将违规文件自动进行冻结处理，对于使用了 CDN 场景的用户，内容审核的自动冻结能力也支持处理 CDN上的缓存数据。

## 操作步骤

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos)，在**存储桶列表**页面选择需操作的存储桶，进入存储桶管理页面。

2. 在左侧导航栏中，选择**内容审核**>**自动审核配置**，单击**图片审核**。

3. 单击**添加图片自动审核配置**，进入图片审核配置页面。

4. 开启**冻结设置**，找到**冻结后刷新 CDN**开关并开启。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/7b74bbb55ac4c00b3464021561a841c6.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/7b74bbb55ac4c00b3464021561a841c6.png)

5. 开启冻结后刷新 CDN 需要授权 CDN 服务，单击**前往 CAM 授权**进行授权。

![Image 4: img](https://qcloudimg.tencent-cloud.cn/image/document/86bac3494a24064a85b7d6364ef6b520.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/86bac3494a24064a85b7d6364ef6b520.png)

6. 授权完成后，返回当前页面刷新授权状态，选择您需要刷新的 CDN 域名，可多选。

7. 其余审核配置可参考 [设置图片审核](https://cloud.tencent.com/document/product/436/45433)。
