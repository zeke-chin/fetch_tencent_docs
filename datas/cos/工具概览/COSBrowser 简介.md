<!-- source: https://cloud.tencent.com/document/product/436/11366 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:11:36+08:00 -->

# COSBrowser 简介

最近更新时间：2024-11-05 18:49:31


## 下载地址

COSBrowser 分类 支持平台 系统要求 下载地址
桌面端 Windows Windows 7 32/64位以上、Windows Server 2008 R2 64位以上[Windows](https://cosbrowser.cloud.tencent.com/cosbrowser-setup-latest.exe)
macOS macOS 10.13以上[macOS Intel 芯片版](https://cosbrowser.cloud.tencent.com/cosbrowser-latest.dmg)

[macOS Apple 芯片版](https://cosbrowser.cloud.tencent.com/cosbrowser-latest-arm64.dmg)
Linux 需带有图形界面并支持 [AppImage](https://appimage.org/) 格式

**注意：**

CentOS 启动客户端需在终端执行`./cosbrowser.AppImage --no-sandbox`[Linux](https://cosbrowser.cloud.tencent.com/cosbrowser-latest-linux.zip)
移动端 Android Android 5.0 及以上[Android](https://cosbrowser.cloud.tencent.com/cosbrowser-latest.apk)
iOS iOS 12 及以上[iOS](https://apps.apple.com/cn/app/id1469323992)
网页版 Web Chrome/FireFox/Safari/IE10+等浏览器[Web](https://cosbrowser.cloud.tencent.com/web)

## 桌面端功能列表

COSBrowser 桌面端注重对资源的管理，用户可以通过 COSBrowser 批量的上传，下载数据。

**注意：**

COSBrowser 桌面端会使用系统配置的代理来尝试网络连接，请确保您的代理配置正常或请停用无法连接互联网的代理配置。

Windows 用户可在操作系统的 “Internet 选项”中查询。

macOS 用户可在“网络偏好设置”中查询。

Linux 用户可在系统设置 > 网络 > 网络代理中查询。

COSBrowser 桌面端支持以下功能：

### 存储桶管理

功能 功能说明
[创建/删除存储桶](https://cloud.tencent.com/document/product/436/38103#createordelete "https://cloud.tencent.com/document/product/436/38103#createordelete")支持创建、删除存储桶
[查看/配置存储桶](https://cloud.tencent.com/document/product/436/38103#head "https://cloud.tencent.com/document/product/436/38103#head")支持查看存储桶基本信息
[搜索存储桶](https://cloud.tencent.com/document/product/436/38103#search "https://cloud.tencent.com/document/product/436/38103#search")支持按照存储桶名称或者存储桶标签快速搜索存储桶
[查看统计数据](https://cloud.tencent.com/document/product/436/38103#data "https://cloud.tencent.com/document/product/436/38103#data")支持查看存储桶的当前存储量及对象总数
[设置存储桶访问权限](https://cloud.tencent.com/document/product/436/38103#acl "https://cloud.tencent.com/document/product/436/38103#acl")支持修改存储桶访问权限
[设置存储桶标签](https://cloud.tencent.com/document/product/436/38103#tag "https://cloud.tencent.com/document/product/436/38103#tag")支持查看、编辑或删除存储桶标签
[设置存储桶的上传/下载域名](https://cloud.tencent.com/document/product/436/38103#domain "https://cloud.tencent.com/document/product/436/38103#domain")支持设置上传、下载域名
[查看域名](https://cloud.tencent.com/document/product/436/38103#domain1 "https://cloud.tencent.com/document/product/436/38103#domain1")支持查看存储桶的域名配置情况
[设置版本控制](https://cloud.tencent.com/document/product/436/38103#version "https://cloud.tencent.com/document/product/436/38103#version")支持开启、暂停存储桶版本控制
[设置全球加速](https://cloud.tencent.com/document/product/436/38103#accelerate "https://cloud.tencent.com/document/product/436/38103#accelerate")支持开启、暂停存储桶全球加速
[添加收藏路径](https://cloud.tencent.com/document/product/436/38103#path "https://cloud.tencent.com/document/product/436/38103#path")支持添加收藏路径
[生成授权码](https://cloud.tencent.com/document/product/436/38103#code "https://cloud.tencent.com/document/product/436/38103#code")通过授权码可实现临时登录 COSBrowser 客户端

### 对象管理

功能 功能说明
[上传文件/文件夹](https://cloud.tencent.com/document/product/436/38103#upload "https://cloud.tencent.com/document/product/436/38103#upload")支持单个上传、批量上传、增量上传文件或文件夹至存储桶
[下载文件/文件夹](https://cloud.tencent.com/document/product/436/38103#download "https://cloud.tencent.com/document/product/436/38103#download")支持单个下载、批量下载、增量下载文件或文件夹至本地
[删除文件/文件夹](https://cloud.tencent.com/document/product/436/38103#delete "https://cloud.tencent.com/document/product/436/38103#delete")支持单个删除、批量删除存储桶中的文件或文件夹
[文件同步](https://cloud.tencent.com/document/product/436/38103#sync "https://cloud.tencent.com/document/product/436/38103#sync")支持将本地文件实时同步至存储桶中
[复制粘贴文件](https://cloud.tencent.com/document/product/436/38103#copy "https://cloud.tencent.com/document/product/436/38103#copy")支持单个复制、批量复制一个目录下的文件或文件夹至另一个目录
[文件重命名](https://cloud.tencent.com/document/product/436/38103#rename "https://cloud.tencent.com/document/product/436/38103#rename")支持重命名存储桶中的文件
[新建文件夹](https://cloud.tencent.com/document/product/436/38103#newfolder "https://cloud.tencent.com/document/product/436/38103#newfolder")支持在存储桶中新建文件夹
[查看文件详情](https://cloud.tencent.com/document/product/436/38103#details "https://cloud.tencent.com/document/product/436/38103#details")支持查看存储桶中的文件基本信息
[生成文件链接](https://cloud.tencent.com/document/product/436/38103#url "https://cloud.tencent.com/document/product/436/38103#url")支持通过请求临时签名的方式生成带有时效的文件访问链接
[分享文件/文件夹](https://cloud.tencent.com/document/product/436/38103#share "https://cloud.tencent.com/document/product/436/38103#share")支持分享文件和文件夹，支持设置分享的有效时间
[导出文件链接](https://cloud.tencent.com/document/product/436/38103#export "https://cloud.tencent.com/document/product/436/38103#export")支持批量导出文件链接
[文件预览](https://cloud.tencent.com/document/product/436/38103#preview "https://cloud.tencent.com/document/product/436/38103#preview")支持预览存储桶中的媒体文件（图片、视频、音频）
[搜索文件](https://cloud.tencent.com/document/product/436/38103#search1 "https://cloud.tencent.com/document/product/436/38103#search1")支持以前缀搜索的方式对存储桶中的文件进行搜索
[查看历史版本或文件碎片](https://cloud.tencent.com/document/product/436/38103#versionid "https://cloud.tencent.com/document/product/436/38103#versionid")支持在已开启版本控制的存储桶中，查看文件的历史版本支持查看存储桶内的文件碎片详情
[文件对比](https://cloud.tencent.com/document/product/436/38103#compare "https://cloud.tencent.com/document/product/436/38103#compare")支持将本地文件夹与存储桶里的文件进行对比
[文件列表管理](https://cloud.tencent.com/document/product/436/38103#file "https://cloud.tencent.com/document/product/436/38103#file")文件列表支持列表布局、网格布局

### 数据处理

功能 功能说明
[视频转码](https://cloud.tencent.com/document/product/436/38103#video "https://cloud.tencent.com/document/product/436/38103#video")支持对已开启媒体处理功能的存储桶中的文件进行转码
[图片处理](https://cloud.tencent.com/document/product/436/38103#picture "https://cloud.tencent.com/document/product/436/38103#picture")支持缩放、裁剪、旋转等基本图片处理和文字水印、图片水印，并支持生成处理后的图片链接

### 软件设置

功能 功能说明
[通用配置](https://cloud.tencent.com/document/product/436/38103#sets "https://cloud.tencent.com/document/product/436/38103#sets")支持设置 EndPoint/Service 域名、Bucket域名模板、自动切换备份域名、HTTPS、HTTPS 证书校验等
[设置网络代理](https://cloud.tencent.com/document/product/436/38103#sets "https://cloud.tencent.com/document/product/436/38103#sets")支持设置网络代理来访问 COS
[设置上传/下载的文件并发数](https://cloud.tencent.com/document/product/436/38103#sets "https://cloud.tencent.com/document/product/436/38103#sets")支持设置文件上传、下载的传输并发数
[设置上传/下载的分块并发数](https://cloud.tencent.com/document/product/436/38103#sets "https://cloud.tencent.com/document/product/436/38103#sets")支持设置文件分块上传、下载的分块数
[设置上传/下载失败重试数](https://cloud.tencent.com/document/product/436/38103#sets "https://cloud.tencent.com/document/product/436/38103#sets")支持设置文件上传、下载失败时的重试次数
[设置单线程上传/下载限速](https://cloud.tencent.com/document/product/436/38103#sets "https://cloud.tencent.com/document/product/436/38103#sets")支持设置单线程上传限速和下载限速
[设置上传二次校验](https://cloud.tencent.com/document/product/436/38103#sets "https://cloud.tencent.com/document/product/436/38103#sets")支持对上传至存储桶中的文件进行二次校验
[查看本地日志](https://cloud.tencent.com/document/product/436/38103#sets "https://cloud.tencent.com/document/product/436/38103#sets")支持将用户对 COSBrowser 的操作记录以本地日志的形式保存

## 移动端功能列表

COSBrowser 移动端注重对资源的查看及监控，用户可以随时随地监控 COS 的存储量、流量等数据。关于 COSBrowser 移动端所支持的功能，请参见 [移动端功能列表](https://cloud.tencent.com/document/product/436/38105)。

## 更新日志

桌面端更新日志：[changelog](https://github.com/tencentyun/cosbrowser/blob/master/changelog.md)

移动端更新日志：[changelog_mobile](https://github.com/tencentyun/cosbrowser/blob/master/changelog_mobile.md)

## 反馈和建议

如您在使用 COSBrowser 时有任何疑问或建议，欢迎反馈给我们：

桌面端反馈：[issues](https://github.com/tencentyun/cosbrowser/issues)

移动端反馈：[issues_mobile](https://support.qq.com/embed/phone/67467)

## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击 [此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406) 一键启动，立即使用！
