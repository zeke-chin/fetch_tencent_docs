<!-- source: https://cloud.tencent.com/document/product/1814/132406 -->
<!-- fetcher: jina -->

# 沙箱访问 Token

最近更新时间：2026-06-03 09:09:01


## 适用范围

沙箱访问 Token 只对单个 `InstanceId` 生效，适合以下场景：

为指定实例签发或复用实例级访问凭证。

校验指定 Token 是否有效，并确认其归属的实例。

校验基于实例 Token 生成的下载 URL 签名。

在实例销毁或不再需要访问凭证时，立即删除该实例对应的 Token。

如果您要管理账号级 AGS 资源，或为自动化脚本、CI/CD、长期运行服务配置统一凭证，请使用 API Key，而不是沙箱访问 Token。

## 与 API Key 的区别

维度 沙箱访问 Token API Key
作用域 单个 `InstanceId`账号级 AGS 调用
获取方式 访问 Token 接口 API Key 服务接口
典型用途 实例访问鉴权、实例级校验、下载签名校验 自动化脚本、CI/CD、长期运行服务
生命周期 由实例类型决定最大值 长期有效，直到删除或被置为 inactive

## 获取沙箱访问 Token

您可以通过 AcquireSandboxInstanceToken 接口获取沙箱访问 Token，详情请参见 [获取沙箱实例的访问 Token](https://cloud.tencent.com/document/product/1814/124818)。
