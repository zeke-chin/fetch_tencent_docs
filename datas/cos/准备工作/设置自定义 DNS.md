<!-- source: https://cloud.tencent.com/document/product/436/98577 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:22:33+08:00 -->

# 设置自定义 DNS

最近更新时间：2023-09-15 17:33:33


## 简介

本文档提供关于如何使用自定义 DNS 请求 COS 服务。

## 设置动态自定义 DNS 回调

更推荐此方式，因为更灵活，更方便业务层控制。

#### 示例代码

// 一般在初始化密钥后进行设置

Cos.initCustomerDNSFetch(async (domain: string) => {

 const dnsMap: Map<string, string[]> = new Map([

 ['service.cos.myqcloud.com', ["106.119.174.56", "106.119.174.57", "106.119.174.55"]],

 ['cos.ap-guangzhou.myqcloud.com', ["27.155.119.179", "27.155.119.180", "27.155.119.166", "27.155.119.181"]],

 ]);

 let ips = null;

 dnsMap.forEach((value, key) => {

 // 通过endsWith进行筛选，可以适配更多子域名，例如 000000-1253960454.cos.ap-guangzhou.myqcloud.com也可以适配到cos.ap-guangzhou.myqcloud.com

 if (domain.endsWith(key)) {

 console.log(`HOST: ${key}, IPS: ${JSON.stringify(value)}`);

 ips = value;

 }

 });

 return ips;

});

## 设置静态自定义 DNS 配置

以下代码展示了如何设置静态自定义 DNS 配置。

#### 示例代码

const dnsArray = [

 {domain:'service.cos.myqcloud.com', ips: ["106.119.174.56", "106.119.174.57", "106.119.174.55"]},

 {domain:'000000-1253960454.cos.ap-guangzhou.myqcloud.com', ips: ["27.155.119.179", "27.155.119.180", "27.155.119.166", "27.155.119.181"]},

 {domain:'cos.ap-guangzhou.myqcloud.com', ips: ["27.155.119.179", "27.155.119.180", "27.155.119.166", "27.155.119.181"]},

];

// 一般在初始化密钥后进行设置

Cos.initCustomerDNS(dnsArray);
