<!-- source: https://cloud.tencent.com/document/product/436/80977 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:22:03+08:00 -->

# 通过 Typecho + COS 搭建博客系统

最近更新时间：2024-11-04 20:24:12


## 简介

[Typecho](https://typecho.org/) 是一个基于 PHP 的开源博客平台。本文主要介绍如何使用插件实现远程附件功能，将 Typecho 的媒体库附件存储在腾讯云 [对象存储（Cloud Object Storage，COS）](https://cloud.tencent.com/product/cos) 上。

## 前提条件

1. 已有 COS 存储桶。如无，可参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 操作指引。

2. 已创建服务器。例如云服务器 CVM。相关指引可参见 [CVM 产品文档](https://cloud.tencent.com/document/product/213)。

## 实践步骤

### 安装 Typecho

您可以在 [Typecho 官方 Github 页面](https://github.com/typecho/typecho/releases/tag/v1.2.0) 下载 Typecho 1.2.0版本，并查看[官方安装指南](https://docs.typecho.org/install)进行安装。您也可以通过宝塔面板安装 Typecho。宝塔面板安装指引请参见 [宝塔官网](https://www.bt.cn/)。

**注意：**

COS 插件仅适用于特定的宝塔版本7.9.6、Typecho 1.2.0版本，下面以宝塔 7.9.6 版本安装 Typecho 1.2.0 为例进行说明。其他版本可能存在兼容问题，无法使用 COS 插件。

#### 安装宝塔

1. 首先准备一台 CVM 机器，然后安全组的入站规则和出站规则按照如下配置：

入站规则

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/016d3b8875cd2bbf91f8217cd2244884.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/016d3b8875cd2bbf91f8217cd2244884.png)

出站规则

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/6493caf6356b74e05e58513e8bd40889.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/6493caf6356b74e05e58513e8bd40889.png)

2. 执行宝塔官网提供的 Centos 安装脚本：

yum install -y wget && wget -O install.sh http://download.bt.cn/install/install_6.0.sh && sh install.sh ed8484bec

在 CVM 机器上直接执行如下图所示：

![Image 6: img](https://qcloudimg.tencent-cloud.cn/image/document/a67c80ef1179a6e94620ca170fabadae.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/a67c80ef1179a6e94620ca170fabadae.png)

3. 执行中会出现如下信息，直接输入 y 回车即可。

![Image 8: img](https://qcloudimg.tencent-cloud.cn/image/document/f163906f48875f65a80a37ba69ce3715.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/f163906f48875f65a80a37ba69ce3715.png)

 执行成功后，会生成网站账号（需记录保存），如下所示：

![Image 10: img](https://qcloudimg.tencent-cloud.cn/image/document/3b6f1d9663f92a8c3a1b3fef922cd6a3.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/3b6f1d9663f92a8c3a1b3fef922cd6a3.png)

#### 通过宝塔安装 Typecho

1. 宝塔安装后，打开桌面上的浏览器，输入在 CVM 生成的宝塔外网链接：`http://43.xxx.xxx.132:16859/c2601bbd`（使用时请替换为自己的 IP）。

2. 单击添加站点，并配置相关参数，输入 CVM 的 IP，其他配置（根目录、FTP 账号、数据库账号等）保持默认。

![Image 12](https://qcloudimg.tencent-cloud.cn/image/document/e578cc5d4653b0464ebb89fa32f44590.png)

![Image 13](https://qcloudimg.tencent-cloud.cn/image/document/e578cc5d4653b0464ebb89fa32f44590.png)

3. 站点创建完成后，进入站点。

4. 单击**文件**导航栏，在文件页面中单击**远程下载**，填入 Typecho 的 GitHub 源码地址：`https://github.com/typecho/typecho/releases/download/v1.2.0/typecho.zip`，然后单击**确认**。

![Image 14](https://qcloudimg.tencent-cloud.cn/image/document/675d1d1245ab996227f646f2fee9b6cb.png)

![Image 15](https://qcloudimg.tencent-cloud.cn/image/document/675d1d1245ab996227f646f2fee9b6cb.png)

5. Typecho 源码文件下载后，并完成解压，然后通过浏览器访问链接 `http://43.xxx.xxx.132/install.php`（使用时请替换为自己的站点 IP）。

6. 根据页面提示，填写如下信息：

![Image 16](https://qcloudimg.tencent-cloud.cn/image/document/3443ecaf526a80adc89ab8dd1e1e389c.png)

![Image 17](https://qcloudimg.tencent-cloud.cn/image/document/3443ecaf526a80adc89ab8dd1e1e389c.png)

**说明：** 可在宝塔界面中获取数据库用户名、密码、名字。

![Image 18](https://qcloudimg.tencent-cloud.cn/image/document/042880729f7489ab1bbfa89d01fc4cd6.png)

![Image 19](https://qcloudimg.tencent-cloud.cn/image/document/042880729f7489ab1bbfa89d01fc4cd6.png)

7. 配置完成后输入您设置的用户名和密码即可登录成功。

### 安装 COS 插件

1. 配置完成后，在宝塔 43.xxx.xxx.132 目录下单击**远程下载**，填入以下插件链接，然后得到该插件的压缩文件。

https://github.com/Tencent-Cloud-Plugins/tencentcloud-typecho-plugin-cos/archive/refs/heads/master.zip

2. 对压缩包进行解压后，复制 TypechoCosPlugin 文件夹到 Typecho 安装路径 /usr/plugins/ 内。复制 /var/Widget/Upload.php 到 Typecho 博客源码安装路径 /var/Widget/ 内，覆盖博客源码中的 /var/Widget/Upload.php 文件。

3. 刷新 Typecho 的后台，即可看到该插件并启用插件。

4. 启用插件后，设置插件相关参数以便关联到 COS，配置信息如下：

基础设置

配置项 配置值
SecretId 访问密钥信息，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中创建和获取
SecretKey 访问密钥信息，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中创建和获取。
所属地域 创建存储桶时所选择的地域。
存储桶名称 创建存储桶时自定义的名称，例如 examplebucket-1250000000。
对象存储路径 文件所存储的 COS 路径，插件默认路径为 usr/uploads，可自行修改。

![Image 20](https://qcloudimg.tencent-cloud.cn/image/document/403dd7a9abd4cc675e367b6ded31ff3d.jpg)

![Image 21](https://qcloudimg.tencent-cloud.cn/image/document/403dd7a9abd4cc675e367b6ded31ff3d.jpg)

高级设置

配置项 配置值
访问域名 不填则使用默认存储桶域名。详情请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。
使用签名链接 若您所创建的存储桶的访问权限为**私有读写**，则开启该项才可正常访问文件。详情可参见 [访问权限类型](https://cloud.tencent.com/document/product/436/13324#.E8.AE.BF.E9.97.AE.E6.9D.83.E9.99.90.E7.B1.BB.E5.9E.8B)。
本地删除同步删除 COS 文件 当您在**博客后台**删除文件时，是否同步删除 COS 上的对应文件。
在本地保存 开启后，上传到 COS 的同时，自动在本地相同路径保存一份副本。建议不开启，会占用本地服务器的存储空间。
删除时同步删除本地备份 当您在**博客后台**删除文件时，是否同步删除本地服务器备份的文件副本（前提是已开启在**本地保存**才会生效）。

![Image 22](https://qcloudimg.tencent-cloud.cn/image/document/3eda8bf0caa5cb58dd8fada9946da4bb.jpg)

![Image 23](https://qcloudimg.tencent-cloud.cn/image/document/3eda8bf0caa5cb58dd8fada9946da4bb.jpg)

5. 完成以上设置后，即可完成博客系统的搭建，上传图片即可显示该 COS 的存储桶域名。

![Image 24](https://qcloudimg.tencent-cloud.cn/image/document/64ec0bd0a23c9fbf0eebc92b05f5cc6b.png)

![Image 25](https://qcloudimg.tencent-cloud.cn/image/document/64ec0bd0a23c9fbf0eebc92b05f5cc6b.png)

## 常见问题

1. 若在安装页面中出现以下报错，则说明 PHP 版本可能不支持，建议是将 PHP 版本替换为7.2以上。

![Image 26: img](https://qcloudimg.tencent-cloud.cn/image/document/29f95a04f3c54d4f4dc626a7f6dc7b4c.png)

![Image 27](https://qcloudimg.tencent-cloud.cn/image/document/29f95a04f3c54d4f4dc626a7f6dc7b4c.png)

![Image 28: img](https://qcloudimg.tencent-cloud.cn/image/document/504a6188eef822f2bf77efa9ed1f1b8b.png)

![Image 29](https://qcloudimg.tencent-cloud.cn/image/document/504a6188eef822f2bf77efa9ed1f1b8b.png)

解决方法： 打开宝塔面板，单击软件商店，在 PHP 这里单击选择7.2以上版本即可。

![Image 30: img](https://qcloudimg.tencent-cloud.cn/image/document/3492950915eeffb490c984bc085896b4.png)

![Image 31](https://qcloudimg.tencent-cloud.cn/image/document/3492950915eeffb490c984bc085896b4.png)

2. 若提示**上传目录无法写入**等报错，则需要重新去 Typecho 官网下载最新安装包。

![Image 32: img](https://qcloudimg.tencent-cloud.cn/image/document/e6c8eaaabc9b017970ba5b60f3ed6fd4.png)

![Image 33](https://qcloudimg.tencent-cloud.cn/image/document/e6c8eaaabc9b017970ba5b60f3ed6fd4.png)

## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击 [此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406) 一键启动，立即使用！
