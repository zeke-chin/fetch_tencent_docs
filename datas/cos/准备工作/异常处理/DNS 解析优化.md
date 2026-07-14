<!-- source: https://cloud.tencent.com/document/product/436/116371 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T22:16:36+08:00 -->

# DNS 解析优化

最近更新时间：2025-03-26 10:55:42


## 简介

本文介绍如何通过 COS SDK 使用 HTTPDNS 服务访问 COS。

## 功能说明

移动端 COS SDK 默认使用的是 LocalDNS，DNS 解析过程中可能会遇到解析异常、域名劫持、跨网访问等问题，通过接入 HTTPDNS 可以避免上述问题，解决移动互联网服务中域名解析异常带来的困扰。

因此，如果您对上传、下载等 COS 操作的成功率、延迟较为敏感，您可以使用 HTTPDNS 服务访问 COS。

## 前提条件

在开始执行操作前，您需要开通 HTTPDNS 服务，并添加对应的 COS 域名。详细操作步骤如下：

1. 前往 [移动解析 HTTPDNS 控制台](https://console.cloud.tencent.com/httpdns) 开通，具体操作请参见 [开通移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/54577)。

2. 在移动解析 HTTPDNS 控制台添加 COS 主域名 myqcloud.com，具体操作请参见 [添加域名](https://cloud.tencent.com/document/product/379/54588)。

3. 获取 HTTPDNS 配置信息，具体说明请参见 [配置信息说明](https://cloud.tencent.com/document/product/379/61203)。

**注意：**

HTTPDNS 虽然有一定免费额度，但是超过后会产生一定的费用，详情请参见 HTTPDNS [计费说明](https://cloud.tencent.com/document/product/379/9216)。

## 操作步骤

### 步骤1：HTTPDNS 配置

请您参考 HTTPDNS SDK 配置（[Android](https://cloud.tencent.com/document/product/379/78132)、[iOS](https://cloud.tencent.com/document/product/379/77755)） 进行 HTTPDNS SDK 的集成和配置。COS SDK 默认自动配置了 SDK 接入业务方式，您在配置 HTTPDNS SDK 过程中无需关注 SDK 接入业务方式（[Android](https://cloud.tencent.com/document/product/379/78132#sdk-.E6.8E.A5.E5.85.A5.E4.B8.9A.E5.8A.A1.E6.96.B9.E5.BC.8F)、[iOS](https://cloud.tencent.com/document/product/379/77755#.E6.B3.A8.E6.84.8F.E4.BA.8B.E9.A1.B9)）。

### 步骤2：COS SDK 中集成

Android

iOS

1. 通过 [初始化 COS 服务](https://cloud.tencent.com/document/product/436/12159#2.-.E6.B3.A8.E5.86.8C-cos-.E6.9C.8D.E5.8A.A1) 获取 CosXmlService。

2. 通过 CosXmlService 的 addCustomerDNSFetch 方法接入 HTTPDNS。

// 获取到CosXmlService

cosXmlService.addCustomerDNSFetch(hostname -> {

 String ips = MSDKDnsResolver.getInstance().getAddrByName(hostname);

 String[] ipArr = ips.split(";");

 if (0 == ipArr.length) {

 return Collections.emptyList();

 }

 List<InetAddress> inetAddressList = new ArrayList<>(ipArr.length);

 for (String ip : ipArr) {

 if ("0".equals(ip)) {

 continue;

 }

 try {

 InetAddress inetAddress = InetAddress.getByName(ip);

 inetAddressList.add(inetAddress);

 } catch (UnknownHostException ignored) {

 }

 }

 return inetAddressList;

});

1. 接入 HTTPDNS，首先需要在 Podfile 文件中添加 HTTPDNS 库依赖。

 pod 'QCloudCore/DNSLoader' // DNSLoader 模块，内部已封装腾讯 HTTPDNS

2. 导入头文件，并定义成员变量 dnsloader。

#import "QCloudHTTPDNSLoader.h"

@property (nonatomic,strong)QCloudHTTPDNSLoader * dnsloader;

3. 设置 HTTPDNS 参数，将步骤一生成的配置参数依次设置给对应字段。

QCloudDnsConfig config;

config.appId = @"******"; // 可选，应用 ID，腾讯云控制台申请获得，用于灯塔数据上报（未集成灯塔时该参数无效）

config.dnsIp = @"0.0.0.0"; // HTTPDNS 服务器 IP

config.dnsId = 1; // 授权 ID，腾讯云控制台申请后，通过邮件发送，用于域名解析鉴权

config.dnsKey = @"*******";// des 的密钥

config.encryptType = QCloudHttpDnsEncryptTypeDES; // 控制加密方式

config.debug = YES; // 是否开启 Debug 日志，YES：开启，NO：关闭。建议联调阶段开启，正式上线前关闭

config.timeout = 5000; // 可选，超时时间，单位ms，如设置0，则设置为默认值2000ms

self.dnsloader = [[QCloudHTTPDNSLoader alloc] initWithConfig:config];

[QCloudHttpDNS shareDNS].delegate = self.dnsloader;

## 示例工程

Android 示例 Demo 请参见 [COS SDK 网络优化 Demo](https://github.com/tencentyun/qcloud-sdk-android-samples/tree/master/COSTransferPractice) 下的 [CosServiceFactory](https://github.com/tencentyun/qcloud-sdk-android-samples/blob/master/COSTransferPractice/app/src/main/java/com/tencent/qcloud/costransferpractice/CosServiceFactory.java)。

iOS 示例 Demo 请参见 [COS SDK 网络优化 Demo](https://github.com/tencentyun/qcloud-sdk-ios-samples/tree/master/QCloudCOSXMLDemo) 下的 [AppDelegate](https://github.com/tencentyun/qcloud-sdk-ios-samples/blob/master/QCloudCOSXMLDemo/QCloudCOSXMLDemo/AppDelegate.m)。
