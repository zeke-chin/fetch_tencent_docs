<!-- source: https://cloud.tencent.com/document/product/436/11142 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:16:46+08:00 -->

# 配置自定义域名支持 HTTPS 访问

最近更新时间：2026-07-03 11:28:02


## 简介

本文主要介绍如何配置用户自有域名（自定义域名，例如`example.com`）实现通过 HTTPS 方式访问对象存储（Cloud Object Storage，COS）资源。具体操作指引如下：

[开启 CDN 加速时配置 HTTPS 访问](https://cloud.tencent.com/document/product/436/11142#.E5.BC.80.E5.90.AF-cdn-.E5.8A.A0.E9.80.9F)

[关闭 CDN 加速时配置 HTTPS 访问](https://cloud.tencent.com/document/product/436/11142#.E5.85.B3.E9.97.AD-cdn-.E5.8A.A0.E9.80.9F)

## 操作步骤

### 开启 CDN 加速时配置 HTTPS 访问

#### 步骤1：绑定自定义域名

将您的自有域名绑定到存储桶，并开启 CDN 加速，然后通过自有域名实现 HTTPS 方式访问 COS 资源，详细操作指引请参见[开启自定义 CDN 加速域名](https://cloud.tencent.com/document/product/436/36637) 文档。

#### 步骤2：配置 HTTPS 访问

在 [CDN 控制台](https://console.cloud.tencent.com/cdn) 进行 HTTPS 配置，详细操作指引请参见 [HTTPS 加速配置指南](https://cloud.tencent.com/document/product/228/41687)。

### 关闭 CDN 加速时配置 HTTPS 访问

本章节主要以示例的形式介绍在不开启 CDN 加速的情况下，直接通过自有域名 `https://example.com` 访问所属地域为广州、名称为 testhttps-1250000000 的存储桶，具体操作步骤如下：

#### 步骤1：绑定自定义域名

您可以通过 COS 控制台将您的自有域名绑定到存储桶，然后为自有域名绑定证书，实现 HTTPS 方式访问 COS 资源，详见 [方式一](https://cloud.tencent.com/document/product/436/11142#1)。

您也可通过**反向代理配置自定义域名**（关闭 CDN 加速）的方式实现 HTTPS 访问。可参考 [方式二](https://cloud.tencent.com/document/product/436/11142#2)。

方式一：通过 COS 控制台绑定自定义源站域名

将域名 `https://example.com`绑定到存储桶 testhttps-1250000000，并绑定证书，详细操作指引请参见 [开启自定义源站域名](https://cloud.tencent.com/document/product/436/36638) 文档。

**说明：**

如果您的域名还没有 HTTPS 证书，可点击 [申请腾讯云证书](https://console.cloud.tencent.com/ssl)。

方式二：为域名配置反向代理

在服务器上为域名 `https://example.com` 配置反向代理。具体配置参考如下（以下 Nginx 配置仅供参考）：

server {

 listen 443;

 server_name example.com;

 ssl on;

 ssl_certificate /usr/local/nginx/conf/server.crt;

 ssl_certificate_key /usr/local/nginx/conf/server.key;

 error_log logs/example.com.error_log;

 access_log logs/example.com.access_log;

 location / {

 root /data/www/;

 proxy_pass http://testhttps-1250000000.cos.ap-guangzhou.myqcloud.com; #配置存储桶（Bucket）的默认下载域名

 }

}

其中 `server.crt;`、`server.key` 是您的自有（自定义）域名的 HTTPS 证书。若您的域名还没有 HTTPS 证书 ，请前往 [腾讯云 SSL 证书](https://cloud.tencent.com/product/ssl) 页面进行申请。 若暂时没有证书，可以删除以下配置信息，但访问时会出现告警，单击继续即可访问：

ssl on;

ssl_certificate /usr/local/nginx/conf/server.crt;

ssl_certificate_key /usr/local/nginx/conf/server.key;

#### 步骤2：解析域名到服务器

在您域名的 DNS 解析服务商处解析您的域名。若您使用的是腾讯云 DNS 解析，请前往 [DNS 解析控制台](https://console.cloud.tencent.com/cns)，将域名`example.com`解析到步骤1中的服务器的 IP 上，详细指引请参见 [快速添加域名解析](https://cloud.tencent.com/document/product/302/3446)。

#### 步骤3：进阶配置

**通过浏览器直接打开网页** 在配置自定义域名支持 HTTPS 访问后，就可以通过您的域名下载存储桶（Bucket）中的对象（Object）了。若根据业务需要，需要直接在浏览器中访问网页、图片等，可通过静态网站功能实现。详细操作指引请参见 [设置静态网站](https://cloud.tencent.com/document/product/436/14984)。 配置完成后，在 Nginx 配置中增加一行信息，重启 Nginx，刷新浏览器缓存即可。

proxy_set_header Host $http_host;

其中`$http_host`替换为您的存储桶默认访问域名，例如 `proxy_set_header Host testhttps-1250000000.cos.ap-guangzhou.myqcloud.com`。

**配置防盗链** 若存储桶（Bucket）是公有的，会有被盗链的风险。用户可以通过设置防盗链，开启 Referer 白名单，防止被恶意盗链。具体操作步骤如下：

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)， 开启防盗链设置功能，选择白名单。详细操作指引请参见 [设置防盗链](https://cloud.tencent.com/document/product/436/13319)。

2. 在 Nginx 配置文件中，增加一行信息并重启 Nginx，刷新浏览器缓存。

proxy_set_header Referer www.test.com;

3. 设置完成后，直接打开文件将提示报错 `errorcode：-46616`。错误提示：未命中 referer 白名单，但是通过代理访问自定义域名，可以正常打开网页。

{

errorcode: -46616,

errormsg: "not hit white referer, retcode:-46616"

}
