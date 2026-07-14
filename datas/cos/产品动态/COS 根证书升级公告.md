<!-- source: https://cloud.tencent.com/document/product/436/117846 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T16:54:52+08:00 -->

# COS 根证书升级公告

最近更新时间：2025-12-29 17:57:15


## 背景

由于 Mozilla 信任库更新了其根证书信任策略，全球所有 CA 的可信根证书生成后最少15年更换一次，超过时间的可信根证书将会逐步被 Mozilla 停止信任。**2025年4月15日之后，GlobalSign R1旧根证书将不再被 Mozilla 浏览器信任。**

受此影响，GlobalSign 证书厂商将逐步停用旧根体系（R1）颁发 TLS/SSL 证书，并开始使用新根体系（R3）颁发 TLS/SSL 证书，以确保 TLS/SSL 证书在 Firefox 浏览器中继续受到信任。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/c22c3c3e3a677f876ff276d68ab56af0.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/c22c3c3e3a677f876ff276d68ab56af0.png)

## 通知

腾讯云对象存储（Cloud Object Storage，COS）的域名使用了 GlobalSign 签发的证书，为保障用户请求不受影响，COS 计划对域名证书进行逐步更新。变更计划如下：

2025年4月15日前，COS 证书会替换为交叉证书。交叉证书同时兼容 R1旧根证书和 R3新根证书，尽可能保障用户请求不受影响。

但是，由于交叉证书会逐步到期，R1旧根证书最终将被淘汰。届时，客户端使用 R3新根证书方可正常请求，使用 R1旧根证书的客户端会请求失败。因此，建议您尽快将新根证书添加至您的可信根证书库中。

长远来看，GlobalSign R3新根证书也将于2027年4月15日不再被 Mozilla 信任 ，同时在2029年3月18日最终到期。考虑到长期的安全性和兼容性，推荐客户端及时升级根证书，同时确保根证书列表中同时包含 GlobalSign R1、R3、R6、R46等所有已知且受信任的权威根证书（根证书列表可参见 [GlobalSign 根证书](https://support.globalsign.com/ca-certificates/root-certificates/globalsign-root-certificates)）。

## 用户适配

1. 验证根证书列表中是否已存在 GlobalSign R3新根证书。

如果该根证书缺失，请尽快将新根证书添加至您的可信根证书库中。

2. 确保权威根证书均已集成至可信根证书库内。

考虑到长期的安全性和兼容性，建议将所有已知且受信任的权威根证书预先集成到客户端的可信根证书库内，避免未来因证书信任链问题导致的连接失败或安全警告。

3. 关注服务监控。

交叉证书同时兼容 R1旧根证书和 R3新根证书，理论上来说不会影响用户请求。但因为每个客户调用环境的差异，可能存在某些不可预见的情况，我们建议您关注服务监控告警，如与您的业务无关可忽略。
