<!-- source: https://cloud.tencent.com/document/product/436/116403 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:12:04+08:00 -->

# COS 终端网络诊断工具使用指南

最近更新时间：2025-02-26 16:24:02


## 工具简介

COS 终端网络诊断工具是集成在 [COSBrowser](https://cloud.tencent.com/document/product/436/11366) 中，对终端到 COS 的网络链路进行排障的工具，它可以通过网络探测和传输测速进行真实的网络链路检测，并给出检测的结论和日志。本文将指导您如何使用这款工具进行网络诊断。

## 使用场景

当您的 APP 在移动端使用 COS 服务时遇到错误或者上传、下载慢的问题时，可以用该工具进行网络诊断。

移动端的网络情况往往比较复杂，例如手机本身的网络配置以及信号强度、DNS 劫持、运营商链路等等，这些都可能是使用 COS 服务遇到问题的原因，可以用该工具进行问题的确认和原因分析。

## 下载和安装

支持平台 系统要求 下载地址
Android Android 5.0及以上[Android](https://cosbrowser.cloud.tencent.com/cosbrowser-latest.apk)
iOS 移动端 iOS 12及以上[iOS](https://apps.apple.com/cn/app/id1469323992)

**说明：**

COSBrowser 移动端目前已覆盖绝大多数应用平台，例如应用宝、App Store 等，可通过单击上述下载地址或自行前往应用平台下载。

iOS 2.8.7及以上开始支持网络功能，安卓 2.8.6及以上开始支持网络功能。

下面以 iOS 移动端为例来介绍工具的具体使用流程。

## 诊断入口

登录页面。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/5b3430f14effb27b191a63eb8a3fcaf1.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/5b3430f14effb27b191a63eb8a3fcaf1.png)

个人页面。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/af90d7a975f2c06db6888f433da408fb.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/af90d7a975f2c06db6888f433da408fb.png)

桶列表菜单选项。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/4d58f6107f437f2c5d2d03cd1f5d3406.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/4d58f6107f437f2c5d2d03cd1f5d3406.png)

## 网络探测

网络探测可以帮助您检查本地网络开关和信号强度，检测本地代理和 VPN，以及进行网络探测（包括 DNS、Ping、Traceroute、Https），并给出探测结论以及一些解决方法。

### 功能

#### 本地网络检测

将检测当前设备的网络是否打开以及信号强度、是否配置了代理或使用 VPN，并给出结论和建议。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/0735c86ed1b13e52a7e29d6f0f5fef03.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/0735c86ed1b13e52a7e29d6f0f5fef03.png)

#### 网络探测

提供了多种网络探测方法，包括 DNS、Ping、Traceroute 和 Https。

DNS：将显示 DNS 解析的结果，包括**域名****IP**和 **A 记录**。

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/59b1dd631d63d25d8603fc31d7e566ba.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/59b1dd631d63d25d8603fc31d7e566ba.png)

Ping：将显示 ping 的结果，包括**平均耗时**和**丢包率**。

![Image 12](https://qcloudimg.tencent-cloud.cn/image/document/9957111967244adb6624e89afbab64cd.png)

![Image 13](https://qcloudimg.tencent-cloud.cn/image/document/9957111967244adb6624e89afbab64cd.png)

Traceroute：将显示路由跟踪的结果，包括最终是否**路由成功**、**平均耗时**和**平均丢包率**。

![Image 14](https://qcloudimg.tencent-cloud.cn/image/document/3ee5587d619cf221bd63ed98dfecb85b.png)

![Image 15](https://qcloudimg.tencent-cloud.cn/image/document/3ee5587d619cf221bd63ed98dfecb85b.png)

Https：将尝试建立 https 连接，并显示结果，包括**总耗时**。

![Image 16](https://qcloudimg.tencent-cloud.cn/image/document/9ead81a4307111ef028763333c59add1.png)

![Image 17](https://qcloudimg.tencent-cloud.cn/image/document/9ead81a4307111ef028763333c59add1.png)

#### 诊断结果和诊断日志

将给出诊断结果，包括可能的问题和建议的解决方案。您也可以查看详细的诊断日志，以获取更多信息或者将日志发送给相关的技术人员进行分析。

**注意：**

网络诊断工具只能提供网络问题的诊断，不能自动修复问题。如果您在使用工具时遇到任何问题，或者需要进一步的帮助，建议您联系网络服务提供商或专业的网络技术人员。

![Image 18](https://qcloudimg.tencent-cloud.cn/image/document/53c193f980b23db13e0306878450c916.png)

![Image 19](https://qcloudimg.tencent-cloud.cn/image/document/53c193f980b23db13e0306878450c916.png)

### 使用步骤

1. 进入网络诊断页面后，选择**网络探测**页签，进行探测。

测试账号内存储桶，此种方式要求登录后使用。

选择要测试的地域，若测试的地域不在列表中，则可选择**输入地域**，但是要确保该地域有已经创建的存储桶。然后选择需要诊断的存储桶，单击**开始诊断**。

![Image 20](https://qcloudimg.tencent-cloud.cn/image/document/214e92c3480f34a6be889ed02dac3b23.png)

![Image 21](https://qcloudimg.tencent-cloud.cn/image/document/214e92c3480f34a6be889ed02dac3b23.png)

输入域名进行探测，此种方式不要求登录。

进入网络诊断工具后，勾选**输入域名进行探测**，在输入框内直接输入需要探测的域名，单击**开始诊断**即可。也可以在右侧选择 COS 域名模板，然后填写对应的<桶名>和<地域>。

![Image 22](https://qcloudimg.tencent-cloud.cn/image/document/ffc53e684b13ef7a0733eb272b3efc86.png)

![Image 23](https://qcloudimg.tencent-cloud.cn/image/document/ffc53e684b13ef7a0733eb272b3efc86.png)

从桶列表菜单进入，会直接进入探测页面进行默认桶域名的探测。

![Image 24](https://qcloudimg.tencent-cloud.cn/image/document/e024d0d6fc7fc68d59f22417bbae6b02.png)

![Image 25](https://qcloudimg.tencent-cloud.cn/image/document/e024d0d6fc7fc68d59f22417bbae6b02.png)

2. 根据探测结果调整网络配置或将结果及日志发给相关的技术人员进行排查。

## 传输测速

传输测速可以对多种类型的 COS 域名进行真实的上传、下载操作，检测上传、下载过程中可能遇到的问题，并记录上传、下载的速度。

### 功能

#### 测试传输速度

针对偏远地区弱网问题，可以快速检测源站域名、全球加速域名、自定义加速域名的传输速度，并根据结果选择最优方案解决。

#### 排查现网问题，获取本地日志

针对现网客户问题，进行点对点排查。生成一个测速链接，让用户尝试复现，并将相关日志抛出，帮助定位问题，缩小排查范围。

### 使用步骤

该工具提供以下两种使用方式，下面详细介绍具体使用步骤。

#### 方式一：账号内存储桶测速

1. 安装成功后登录 APP，单击底部 Tab 栏**个人**，选择**网络诊断**>**传输测速**。

![Image 26](https://qcloudimg.tencent-cloud.cn/image/document/2ae1c73e1f5d9820d1251755ea6c3ece.png)

![Image 27](https://qcloudimg.tencent-cloud.cn/image/document/2ae1c73e1f5d9820d1251755ea6c3ece.png)

2. 选择要测试的地域，若测试的地域不在列表中，则可选择**输入地域**，但是要确保该地域有已经创建的存储桶，输入地域后，单击右侧**选择存储桶**按钮，选择要测试的存储桶。

![Image 28](https://qcloudimg.tencent-cloud.cn/image/document/737a83895fbdfb49b3a4010686f7e058.png)

![Image 29](https://qcloudimg.tencent-cloud.cn/image/document/737a83895fbdfb49b3a4010686f7e058.png)

3. 选择存储桶后，开始配置传输所用的域名。默认为源站域名，可以选择**全球加速**域名（选择的存储桶需 [开启全球加速功能](https://cloud.tencent.com/document/product/436/38864)）、**自定义域名**（确保域名有效可用，支持手动输入）等。

**说明：**

选择**全球加速**域名时，选择的存储桶需开全球加速功能。

选择**自定义域名**时，需确认域名有效可用。自定义域名支持手动输入。

4. 开始测速，结果如下图所示。

![Image 30](https://qcloudimg.tencent-cloud.cn/image/document/e7b9a4a086aa35b0d40b84952a796d09.png)

![Image 31](https://qcloudimg.tencent-cloud.cn/image/document/e7b9a4a086aa35b0d40b84952a796d09.png)

**说明：**

测试过程中会给存储桶内上传一个临时文件，并在测试完成后自动删除。

#### 方式二：测速链接测速

方式一只能测试自己的存储桶，但当需要其他人来帮我们测试他所在的网络环境到我们存储桶的传输速度同时又不方便让对方直接登录我们的账号。基于这种场景，我们提供了使用测速链接来测速，操作步骤如下：

**注意：**

COSBrowser PC 版本需使用2.11.25及以上。

1. 下载安装 COSBrowser PC 端并登录，单击右上角**工具箱，**选择**生成测速链接**。

![Image 32](https://qcloudimg.tencent-cloud.cn/image/document/431855346ebda377ee8587cb680395a5.png)

![Image 33](https://qcloudimg.tencent-cloud.cn/image/document/431855346ebda377ee8587cb680395a5.png)

2. 选择**存储桶**并单击**确定**，生成测速链接。

![Image 34](https://qcloudimg.tencent-cloud.cn/image/document/e0221706407a6f87b32fe48580cf493c.png)

![Image 35](https://qcloudimg.tencent-cloud.cn/image/document/e0221706407a6f87b32fe48580cf493c.png)

3. 将生成的测速链接复制发给对方来帮我们测速。当对方拿到测速链接时，可以通过以下方式来进行测速。

下载安装 COSBrowser APP 测速，无需登录，安装打开即可。在登录页面右上角单击诊断按钮，进入**传输测速**页面，粘贴**测速链接**并单击**开始测速**。

![Image 36](https://qcloudimg.tencent-cloud.cn/image/document/51b1fbba5b56a11cc6b4e8b4f4278128.png)

![Image 37](https://qcloudimg.tencent-cloud.cn/image/document/51b1fbba5b56a11cc6b4e8b4f4278128.png)

对方在浏览器中（手机、PC 端均可）打开生成的测速链接，单击**开始测速**。

![Image 38](https://qcloudimg.tencent-cloud.cn/image/document/e77a9d9ed3274d28e53853b03ee8bc40.png)

![Image 39](https://qcloudimg.tencent-cloud.cn/image/document/e77a9d9ed3274d28e53853b03ee8bc40.png)

## 结语

希望网络诊断工具以及测速工具能为 COS 的用户排查定位问题带来帮助。如果有更好的想法或者需要工具提供更多的功能，请 [联系我们](https://cloud.tencent.com/document/product/436/37708)。
