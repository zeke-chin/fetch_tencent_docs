<!-- source: https://cloud.tencent.com/document/product/436/41153 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:21:20+08:00 -->

# 将 WordPress 远程附件存储到 COS

最近更新时间：2025-08-01 18:08:22


## 简介

[WordPress](https://cn.wordpress.org/) 是使用 PHP 语言开发的博客平台，用户可以在支持 PHP 和 MySQL 数据库的服务器上架设属于自己的网站，也可以把 WordPress 当作一个内容管理系统（CMS）来使用。

WordPress 功能强大、扩展性强，这主要得益于其插件众多，易于扩充功能，基本上一个完整网站该有的功能，通过其第三方插件都能实现所有功能。

这篇文章我们来介绍一下如何使用插件实现远程附件功能，将 WordPress 的媒体库附件存储在腾讯云 [对象存储（Cloud Object Storage，COS）](https://cloud.tencent.com/product/cos) 上。

COS 具有高扩展性、低成本、可靠和安全等特点，将媒体库附件保存在 COS 上有以下好处：

附件将拥有更高的可靠性。

您的服务器无需为附件准备额外的存储空间。

用户查看图片附件时将直连 COS 服务器，不占用您服务器的下行带宽/流量，用户访问速度更快。

可配合腾讯云 [内容分发网络（Content Delivery Network，CDN）](https://cloud.tencent.com/product/cdn) 进一步提升用户查看图片附件的速度，优化网站访问速度。

## 前提条件

1. 已有 COS 存储桶。如无，可参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 操作指引。

2. 已创建服务器。例如云服务器（Cloud Virtual Machine，CVM）。相关指引可参见 [CVM 产品文档](https://cloud.tencent.com/document/product/213)。

## 实践步骤

### WordPress 部署

基于腾讯云服务器来快速搭建 WordPress，有两种方式：通过镜像部署和手动部署。如果您对业务网站有较高的扩展性需求，可手动搭建，详情请参见以下指引：

[手动搭建 WordPress 个人站点（Linux）](https://cloud.tencent.com/document/product/213/8044)

[手动搭建 WordPress 个人站点（Windows）](https://cloud.tencent.com/document/product/213/39540)

这里介绍通过镜像部署 WordPress，镜像部署简便快捷。操作步骤如下：

1. 通过镜像部署 WordPress。

1.1 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的**新建**。

1.2 根据页面提示选择机型，并在**实例配置 > 镜像 > 云镜像市场**中输入 **WordPress** 进行搜索，并选择所需的镜像。本文举例选择使用 docker 部署 WordPress 的镜像。

1.3 完成选购后，登录 CVM 控制台，为刚创建的实例关联安全组，需添加放通80端口的入站规则。

2. 在实例的管理页面，复制该云服务器实例的**公网 IP，**在本地浏览器中访问地址`http://公网 IP/wp-admin`，开始安装 WordPress 网站：

2.1 选择 WordPress 语言后，单击 **Continue**。

2.2 按需输入 WordPress 站点标题、管理员用户名、管理员密码及电子邮件。

2.3 单击**安装WordPress**。

2.4 单击**登录**。

**说明：**

如果您希望使用云服务器直接搭建个人站点（不使用容器服务），请参见 [手动搭建 WordPress 个人站点（Linux）](https://cloud.tencent.com/document/product/213/9740)。

### 创建 COS 存储桶

1. 创建一个**公有读私有写**的存储桶，存储桶的地域建议与运行 WordPress 博客平台的 CVM 的地域相同，创建详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。

2. 在**存储桶列表**中找到刚才创建的存储桶，并单击其存储桶名称，进入存储桶页面。

3. 在左侧导航栏中，单击**概览**，查看访问域名并记录。

### 安装并配置插件

#### 源码安装

由于使用 docker 部署 WordPress 的镜像，WordPress 部署在容器中，因此需要先执行 `docker ps` 查找 WordPress 所在的容器 ID，然后执行`docker exec` 进入容器。如下图所示：

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/99e110ad41b958878a923098042abdaf.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/99e110ad41b958878a923098042abdaf.png)

**注意：**

如果您遇到权限问题，可以尝试在命令前加上 `sudo`。

进入容器后，请自行安装 wget 和 unzip。接着下载插件源码，将插件源码上传到 WordPress 插件目录`wp-content/plugins`，最后在后台启用。

下面以 Ubuntu 为例安装插件：

1. 进入 wp-content 的父目录：

cd /var/www/html

2. 添加权限：

chmod -R 777 wp-content

3. 创建插件目录：

cd wp-content/plugins/

mkdir tencent-cloud-cos

cd tencent-cloud-cos

4. 下载插件到插件目录：

curl -O -L https://cosbrowser.cloud.tencent.com/code/tencent-cloud-cos.zip

unzip tencent-cloud-cos.zip

rm tencent-cloud-cos.zip -f

5. 单击“插件”左侧菜单，即可看到该插件，单击启用该插件。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/2618d668a5e9e24facb67689aa73162c.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/2618d668a5e9e24facb67689aa73162c.png)

#### **配置插件**

在插件 tencent-cloud-cos 配置 COS 存储桶信息：

1. 单击“设置”按钮来配置插件 tencent-cloud-cos。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/21eaaf7744d566645239c0362c40fe5f.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/21eaaf7744d566645239c0362c40fe5f.png)

2. 在页面中配置 COS 的相关信息，配置说明见下表：

配置项 配置值
SecretId、SecretKey 访问密钥信息，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中创建和获取
所属地域 创建存储桶时所选择的地域
空间名称 创建存储桶时自定义的存储桶名称，例如examplebucket-1250000000
访问域名 指 COS 的默认存储桶域名，用户在创建存储桶时，由系统根据存储桶名称和地域自动生成。不同地域的存储桶有不同的默认域名。您可以前往 [对象存储控制台](https://console.cloud.tencent.com/cos5) ，在存储桶的概览 > 域名信息中查看
自动重命名 文件上传到 COS 后自动重命名，避免与已有同名文件相冲突，可按照指定格式重命名
不在本地保存 开启后，不会在本地保留源文件
保留远程文件 开启后，当删除文件，将只删除本地文件副本，仍然保留远程 COS 桶中的文件副本，可方便找回
禁止缩略图 开启后不会上传对应的缩略图文件
数据万象 开启数据万象服务，可对图片进行编辑、压缩、转换格式、添加水印等操作，详情可参见 [数据万象产品介绍](https://cloud.tencent.com/product/ci)
文件审核 开启文件审核，可对图片、视频、音频、文本、文档、网页等多媒体内容进行安全智能审核服务，可帮助用户有效识别色情低俗、违法违规、恶心反感等违禁内容，规避运营风险，详情可参见 [内容审核概述](https://cloud.tencent.com/document/product/436/45435)
文档预览 开启文档预览，可将文件转码为图片、PDF 或 HTML5页面，解决文档内容的页面展示问题，详情可参见 [文档预览概述](https://cloud.tencent.com/document/product/436/45906)
调试 记录错误、异常和警告信息

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/9442b0e4d7a86e8859508e4726228b56.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/9442b0e4d7a86e8859508e4726228b56.png)

3. 配置完成后，单击**保存配置**即可。

## **验证 WordPress 附件存储到 COS**

在 WordPress 创建一篇带图片的文章，查看图片是否保存在 COS。

1. 创建一篇带图片的文章。在 WordPress 仪表盘，单击“文章”左侧菜单。

1.

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/7f6bc2770e3503221124af2e4466ecaa.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/7f6bc2770e3503221124af2e4466ecaa.png)

2. 对 WordPress 默认生成的“世界，您好！”文章进行编辑。

3.

![Image 12](https://qcloudimg.tencent-cloud.cn/image/document/786cb97419bd60499aa526a6e0924a61.png)

![Image 13](https://qcloudimg.tencent-cloud.cn/image/document/786cb97419bd60499aa526a6e0924a61.png)

4. 单击右边 “＋”按钮。

![Image 14: img](https://qcloudimg.tencent-cloud.cn/image/document/e0c1eb24efecd38cfc5702140991d792.png)

![Image 15](https://qcloudimg.tencent-cloud.cn/image/document/e0c1eb24efecd38cfc5702140991d792.png)

5. 然后选择上传一张图片。

![Image 16: img](https://qcloudimg.tencent-cloud.cn/image/document/8202cf7752e0b927af1e01dddbf5cdb7.jpg)

![Image 17](https://qcloudimg.tencent-cloud.cn/image/document/8202cf7752e0b927af1e01dddbf5cdb7.jpg)

6. 上传完成后，查看已上传图片的 URL，确认图片地址为 COS 的地址，例如`https://wd-125000000.cos.ap-nanjing.myqcloud.com/2022/10/立夏-1200x675.jpeg`，格式为：`https://<BucketName-APPID>.cos.<Region>.myqcloud.com/<ObjectKey>`，表示图片已上传到 COS 存储桶。

![Image 18: img](https://qcloudimg.tencent-cloud.cn/image/document/4c267ba6d3c458ab6c980d67ad96b63a.jpg)

![Image 19](https://qcloudimg.tencent-cloud.cn/image/document/4c267ba6d3c458ab6c980d67ad96b63a.jpg)

7. 登录 COS 控制台，在 COS 存储桶里能看到您刚才上传的图片。

![Image 20](https://qcloudimg.tencent-cloud.cn/image/document/6cec715685ba594837b0704c5443ea9b.png)

![Image 21](https://qcloudimg.tencent-cloud.cn/image/document/6cec715685ba594837b0704c5443ea9b.png)

**说明：**

以上测试成功后，接下来如果需要同步旧资源到 COS 存储桶中（可使用 [COSCMD 工具](https://cloud.tencent.com/document/product/436/10976) 或者 [COS Migration 工具](https://cloud.tencent.com/document/product/436/15392)），**否则后台无法正常预览旧资源**。同步完成以后，可以开启回源设置，可参考下文的 [设置回源](https://cloud.tencent.com/document/product/436/41153#1)。

## 扩展

1. 使用 CDN 加速访问 存储桶如果需要配置 CDN 加速，可参见 [CDN 加速配置](https://cloud.tencent.com/document/product/436/18670) 文档。在插件设置中将 URL 前缀修改为默认 CDN 加速域名或自定义加速域名即可。

2. 替换数据库中的资源地址 如果不是新创建的站点，数据库当中必定是旧的资源链接地址，我们需要将资源地址进行替换，插件提供了替换功能，请在首次替换前记得备份。

旧域名填写原资源域名，例如`https://example.com/`

新域名填写现在的资源域名，例如`https://img.example.com/`

3. 设置跨域访问 在文章中引用对应的资源链接，控制台会提示跨域的错误`No 'Access-Control-Allow-Origin' header is present on the requested resource`。原因是没有添加 header。您需要在跨域访问 CORS 设置中添加 HTTP Header 配置。下面提供两种途径进行配置：

在 COS 控制台上配置

![Image 22](https://qcloudimg.tencent-cloud.cn/image/document/5cba71711c7beaf898a8570a885f017b.png)

![Image 23](https://qcloudimg.tencent-cloud.cn/image/document/5cba71711c7beaf898a8570a885f017b.png)

**说明：**

关于跨域配置操作步骤，请参见 [设置跨域访问](https://cloud.tencent.com/document/product/436/13318) 文档。

在 CDN 控制台上配置

如允许所有域名，则配置如下：

Access-Control-Allow-Origin: *

只允许您个人的域名访问，则配置如下：

Access-Control-Allow-Origin: https://example.com

4.

设置回源

 如果您不在 WordPress 后台媒体库中上传资源，建议开启回源设置，详细步骤请参见 [设置回源](https://cloud.tencent.com/document/product/436/13310) 文档。 开启回源设置后，当客户端首次访问 COS 源文件时，COS 发现无法命中对象，对客户端返回 302 HTTP 状态码并跳转至回源地址所对应的地址，此时对象由源站提供给客户端，从而保证访问。同时 COS 从源站复制该文件并保存至存储桶对应的目录中；第二次访问时，COS 直接命中对象并返回给客户端。

## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击“[此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406)”一键启动，立即使用！
