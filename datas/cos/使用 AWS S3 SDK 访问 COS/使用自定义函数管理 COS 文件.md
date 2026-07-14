<!-- source: https://cloud.tencent.com/document/product/436/71356 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:19:20+08:00 -->

# 使用自定义函数管理 COS 文件

最近更新时间：2025-08-29 15:03:52


## 概述

对象存储（Cloud Object Storage，COS）工作流提供了一系列针对音视频、图片等媒体文件的处理能力，用户可以按照自身需求，灵活快速地搭建媒体处理流水线。随着越来越多用户接入 COS 工作流，一些定制化需求也被提上议程。为了保障灵活性，COS 工作流推出了自定义云函数功能，支持用户在工作流中配置云函数节点，在云函数中实现定制化逻辑。 为了进一步降低用户的使用门槛，COS 工作流整理了常用的云函数功能模板，并将其创建流程集成至节点的配置步骤中，方便用户对处理前的源文件、处理后的产物文件进行后续加工。现已支持修改对象属性、移动对象，删除对象等基本操作。

## 应用场景

在媒体处理后，对源文件进行移动、沉降等处理，降低存储成本。

在媒体处理后，对产物文件进行标签设置，修改头部等处理，方便业务使用。

## 方案优势

开箱即用：无需开发函数逻辑，无需关注复杂的部署流程，简易配置即可使用。

配置灵活：可以按需配置常用功能节点，分别针对源文件和产物文件进行不同的业务操作。

拓展方便：支持用户修改云函数逻辑，以满足更多定制化需求。

## 操作步骤

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。

2. 在左侧导航栏中，单击**存储桶列表**，进入存储桶列表页面。

3. 单击待操作的存储桶，进入存储桶详情页面。

4. 在左侧导航栏中，选择**任务与工作流**>**工作流管理**，单击**创建工作流**。

5. 在创建工作流页面，单击 **“＋”** 号，配置业务需要的媒体处理节点，例如“音视频转码”节点，详情可参见 [数据工作流](https://cloud.tencent.com/document/product/460/46488)。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/e97c90b271584183cb63c1375519eda1.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/e97c90b271584183cb63c1375519eda1.png)

6. 在创建工作流页面，添加**自定义函数**节点，选择您需要的常用功能函数。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/64645b26fa6567f0b57878489660683b.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/64645b26fa6567f0b57878489660683b.png)

7. 如果您尚未创建此类函数，则单击**创建函数**。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/21fe300d235c6f2cfabd91c74d4f21e4.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/21fe300d235c6f2cfabd91c74d4f21e4.png)

8. 创建常用功能函数的步骤如下：

8.1 填写**函数基础配置**。输入函数名称前缀，勾选**授权 SCF 服务**，单击**下一步**。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/16c3eb511728270e92e73b191461f4af.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/16c3eb511728270e92e73b191461f4af.png)

8.2 填写**属性配置**。按业务需求设**置存储类型**，自定义头部等，单击**下一步**。

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/c047a425fbe9092ee3f50f2b113fef1b.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/c047a425fbe9092ee3f50f2b113fef1b.png)

8.3 勾选处理对象，可以只针对工作流源文件执行该操作。

![Image 12](https://qcloudimg.tencent-cloud.cn/image/document/20ac9ed7fad49c1984d9d6652a9e0955.png)

![Image 13](https://qcloudimg.tencent-cloud.cn/image/document/20ac9ed7fad49c1984d9d6652a9e0955.png)

8.4 单击**确认**。

8.5 COS 工作流封装了函数创建，版本发布，别名切流等过程，请等待其创建完成。

![Image 14](https://qcloudimg.tencent-cloud.cn/image/document/39d4cc84bd6722433bb6c0f9f8e81ccf.png)

![Image 15](https://qcloudimg.tencent-cloud.cn/image/document/39d4cc84bd6722433bb6c0f9f8e81ccf.png)

9. 创建完成后，选中刚刚创建的函数实例，单击**确定**。

![Image 16](https://qcloudimg.tencent-cloud.cn/image/document/2978b5019d96b31e49018fb14be76f9b.png)

![Image 17](https://qcloudimg.tencent-cloud.cn/image/document/2978b5019d96b31e49018fb14be76f9b.png)

10. 单击**保存**当前工作流即可。

## 操作验证

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。

2. 在左侧导航栏中，单击**存储桶列表**，进入存储桶列表页面。

3. 单击待操作的存储桶，进入存储桶详情页面。

4. 在左侧导航栏中，选择**任务与工作流**>**工作流管理**，进入工作流管理页面。

5. 找到刚创建的工作流，启动**上传触发执行**，并前往指定存储桶路径上传媒体文件，等待工作流执行。

6. 待工作流运行结束后，即： 可以看到媒体处理成功，产物已生成。

![Image 18](https://qcloudimg.tencent-cloud.cn/image/document/b9c4374b997176a685c00948e833d424.png)

![Image 19](https://qcloudimg.tencent-cloud.cn/image/document/b9c4374b997176a685c00948e833d424.png)

源文件已成功设置存储类型和自定义头部。

![Image 20](https://qcloudimg.tencent-cloud.cn/image/document/02c59639a9a1859daeeb3347fe1aee82.png)

![Image 21](https://qcloudimg.tencent-cloud.cn/image/document/02c59639a9a1859daeeb3347fe1aee82.png)
