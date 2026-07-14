<!-- source: https://cloud.tencent.com/document/product/436/83859 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:37:17+08:00 -->

# 通过外网访问 COS 文件缓慢

最近更新时间：2026-06-23 17:00:03


## 现象描述

访问 COS 资源时，耗时比较久，甚至出现超时，无法访问的情况。

## 可能原因

涉及到跨境网络延迟比较慢，无法保证网络质量，例如，您在日本访问北京的存储桶这种跨境访问场景。

本地的机器负载满了，例如 CPU、内存以及外网带宽。

其他原因。

## 操作步骤

### 检查是否跨境访问

推荐方案：

1. 如果业务在境内，建议在境内部署存储桶，如果业务在境外，建议部署境外的存储桶。（推荐）

2. 可以使用 COS 的全球加速域名。（这个功能是主要优化跨境访问的问题，有额外费用。如果不涉及跨境访问，不建议使用这个域名）。

关于全球加速功能介绍和费用说明，请参见 [全球加速概述](https://cloud.tencent.com/document/product/436/38866)。建议使用前请先提交工单咨询腾讯云工程师，再确认是否使用。

### 检查本地机器配置

每个机器的配置可能不一样，建议检查电脑 CPU、内存以及外网带宽的负载。下面提供了腾讯云云服务器 Windows 的环境排查文档：（Windows 大体都类似，可以参考）

[检查 CPU 和内存](https://cloud.tencent.com/document/product/213/10233)

[检查带宽](https://cloud.tencent.com/document/product/213/10334)

### 根据使用场景进行检查

按照以下场景进行操作，如果在操作中有遇到问题，请先提交工单沟通。

#### 场景1：Windows、Mac 或者其他界面化系统的浏览器访问 COS 资源缓慢

1. 访问 `https://ping.huatuo.qq.com/` 这个网站，输入 COS 域名进行检测（不用携带协议以及具体的资源路径，可直接进行域名测试）。

这里可以直接确认下，本地的 IP 和 COS 给的 IP 是否是同一个运营商（可以直接把 IP 输入到百度搜索栏，然后按回车键，即可查看），例如都是电信或者联通运营商。 如果跨网络了（例如本地是电信，解析出来的是移动或者其他运营商的 IP），那就是解析问题，需要将本地的 DNS 修改为自己网络运营商提供的 DNS。

2. 执行 telnet 命令测试域名的80端口是否连通。

3. 操作命令：

telnet examplebucket-1250000000.cos.ap-beijing.myqcloud.com 80

**说明：**

关于 telnet 命令的安装方法，请自行查找相关资料。

4. 如果上述没有问题，再进行 MTR 网络测试，可参见 [网络排查工具 MTR 介绍文档](https://cloud.tencent.com/developer/article/1491610)。

4.1 安装 MTR

4.2 执行 `mtr COS 域名`，如下所示：

mtr examplebucket-1250000000.cos.ap-beijing.myqcloud.com

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/97836142a88910ff11b7b4dc6d345f51.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/97836142a88910ff11b7b4dc6d345f51.png)

 然后可以查看 Host 这一列，这些 IP 就是请求网络链路，对这些 IP 地址查看来源。 例如，在北京访问重庆的存储桶，那么这里的 IP 就不能去其他地方，例如您发现中间一个 IP 跑到了中国香港，这就是有问题的。

5. 执行 nslookup 命令，查看域名解析是否正常。

nslookup examplebucket-1250000000.cos.ap-beijing.myqcloud.com

根据解析到的 IP 和本地的 IP 对比，确认下解析到的 IP 和本地的 IP 是否为同一个地域和同一个运营商。

6. 抓包看下（在访问缓慢的环境下）

[Windows 抓包](https://cloud.tencent.com/developer/article/1865941)

[Mac 抓包](https://cloud.tencent.com/developer/article/2045860)（比较方便）

执行 tcpdump 命令，如下所示：

tcpdump host examplebucket-1250000000.cos.ap-beijing.myqcloud.com -w test.cap

打开另外的窗口请求访问缓慢的资源，完成后中断（Ctrl+C）抓包，test.cap 文件就是抓包文件。

然后提交工单，由腾讯云工程师协助排查。在提交工单时，请将上面您所做的网络测试信息以及截图一并提供，以便快速定位问题。

#### 场景2：移动端浏览器访问 COS 资源缓慢

1. 首先确认下访问慢的资源 URL，单独访问这个资源看看速度是否正常。

2. 同时，再访问一下其他网站是否正常（例如百度等）。

3. 换一个网络环境，例如连接其他 Wi-Fi 网络。

经过上述三步，如果确定只有 COS 资源访问缓慢，其他网站的资源访问正常。那么接下来可以在电脑端连接和手机一样的网络环境（例如连接同样的 Wi-Fi，或者电脑连接手机4G网络），再测试访问 COS 资源。

（1）如果电脑端测试复现，可以参考上述 [场景1](https://cloud.tencent.com/document/product/436/83859#case1) 进行排查。

（2）如果电脑端也访问正常，只有移动端有问题，可以对移动端进行网络测试操作，操作方法可参见 [场景1中的第1步](https://cloud.tencent.com/document/product/436/83859#case1)。

（3）测试网络路由，使用手机测试 IP 路由信息，可直接访问 `http://www.webkaka.com/Tracert.aspx`，输入 COS 域名进行测试。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/de0c8e6fccea1f234fb1b7caf2472a78.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/de0c8e6fccea1f234fb1b7caf2472a78.png)

在 IP 地址这一列，这些 IP 就是请求网络链路，对这些 IP 地址查看来源。例如，在北京访问重庆的存储桶，那么这里的 IP 不会出现中国香港 IP，否则是有问题的。

（4）如果上述没有问题，可进行抓包排查，可参见 [抓包教程](https://cloud.tencent.com/developer/article/1727282)。 然后提交工单，由腾讯云工程师协助排查。在提交工单时，请将上面您所做的网络测试信息以及截图一并提供，以便快速定位问题。

#### 场景3：黑窗口 Linux 机器访问 COS 资源缓慢

1. 测试下域名的80端口是否连通，操作命令如下：

telnet examplebucket-1250000000.cos.ap-beijing.myqcloud.com 80

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/3e37e6c50308575479738bae04186727.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/3e37e6c50308575479738bae04186727.png)

 若不连通，对百度网站进行测试，请将上述的 COS 域名换为 `www.baidu.com`。查看百度是否可以连通，确认下本地网络环境。

2. 执行 nslookup 命令，查看域名解析是否正常。

nslookup examplebucket-1250000000.cos.ap-hongkong.myqcloud.com

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/a1d5bad5af54cf050b057a617f3ca47f.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/a1d5bad5af54cf050b057a617f3ca47f.png)

 这里可以直接确认下，本地的 IP 和 COS 给的 IP 是否是同一个运营商（可以直接把 IP 输入到百度搜索栏，然后按回车键，即可查看），例如都是电信或者联通运营商。

3. 进行 MTR 网络测试，具体可参见 [场景1中的第3步](https://cloud.tencent.com/document/product/436/83859#case1)。

4. 使用 tcpdump 进行抓包，可参见 [抓包教程](https://cloud.tencent.com/developer/article/2045860)。 执行 tcpdump 命令，如下所示：

tcpdump host examplebucket-1250000000.cos.ap-hongkong.myqcloud.com -w test.cap

在另外的窗口请求访问缓慢的资源，完毕之后中断（Ctrl+C）抓包，test.cap 文件就是抓包文件。

然后提交工单，由腾讯云工程师协助排查。在提交工单时，请将上面您所做的网络测试信息以及截图一并提供，以便快速定位问题。
