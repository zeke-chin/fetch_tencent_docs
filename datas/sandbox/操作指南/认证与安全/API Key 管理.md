<!-- source: https://cloud.tencent.com/document/product/1814/132405 -->
<!-- fetcher: jina -->

# API Key 管理

最近更新时间：2026-06-03 09:09:01


## 使用限制

限制项 说明
明文只返回一次 API Key 明文仅在创建成功时返回，后续只能查看脱敏后的 `MaskedKey`。
CLI 暂不支持独立验证`agr` CLI 没有独立的 `verify` 子命令，需通过实际业务请求验证有效性。
配额上限 配额按 `SubAccountUin` 维度生效，超限后创建会返回 `LimitExceeded.APIKeyQuota`。
CLI 能力范围`agr` CLI 支持创建、列表和删除操作；单 Key 详情查询和属性修改暂不提供 CLI 入口。

## 前提条件

1. 已安装并配置 `agr` CLI。

2. 已配置可用的云 API 凭证。

3. 执行以下命令确认凭证已就绪：

agr status -o json --non-interactive

输出中 `Data.Auth.SecretId.Present` 和 `Data.Auth.SecretKey.Present` 都应为 `true`。

## 查看 API Key 列表

agr apikey list -o json --non-interactive

示例输出：

{

 "SchemaVersion": "agr.v1",

 "Command": "apikey.list",

 "Status": "succeeded",

 "Data": {

 "Items": [

 {

 "CreatedAt": "2026-04-22T08:14:47.816Z",

 "KeyId": "ark-xxxxxxxx",

 "MaskedKey": "ark_xx****xxxx",

 "Name": "ci-bot",

 "Status": "API_KEY_STATUS_ACTIVE"

 }

 ]

 }

}

返回字段说明：

字段 说明
`KeyId`API Key 的公开标识，可用于删除操作。
`MaskedKey`脱敏后的 Key 值，用于辅助识别。
`Name`创建时指定的名称。
`Status`当前状态，例如 `API_KEY_STATUS_ACTIVE`。
`CreatedAt`创建时间（UTC）。

该操作为只读查询，不会创建、修改或删除任何资源。

## 创建 API Key

agr apikey create -n ci-bot -o json --non-interactive

成功后响应返回 `KeyId`、`APIKey` 和 `Name`。其中 `APIKey`**只在此时返回一次**，请立即保存到密钥管理系统。

创建后验证：

1. 记录响应中的 `KeyId`。

2. 执行 `agr apikey list -o json --non-interactive`，确认新 `KeyId` 出现在列表中。

3. 用该 Key 发起一次实际的 AGS 业务请求，确认有效性。

如果只是测试创建流程，验证完成后请立即删除测试 Key，避免残留凭证。

### 常见失败信号

错误码 含义
`LimitExceeded.APIKeyQuota`当前子账号配额已用尽。
`UnauthorizedOperation`当前身份没有创建 API Key 的权限。
`InvalidParameter`请求参数不合法。

## 验证 API Key 有效性

API Key 是否可用，应以实际业务请求结果为准。建议按以下顺序确认：

1. 执行 `agr apikey list -o json --non-interactive`，确认目标 `KeyId` 存在且状态为 `API_KEY_STATUS_ACTIVE`。

2. 使用该 Key 发起一次真实的 AGS 业务请求，以实际响应作为最终验证结果。

**说明：**

`agr` CLI 暂不支持独立的 `apikey verify` 子命令。上述两步是当前推荐的可用性确认方法。

在自动化流程中，建议直接以业务请求结果做健康检查，而不是仅依赖列表查询。

## 删除 API Key

如果某个 API Key 不再使用或怀疑已泄漏，立即删除：

agr apikey delete <key-id> -o json --non-interactive

删除后不可恢复。执行 `agr apikey list -o json --non-interactive` 确认目标 `KeyId` 已从列表中移除。

## 权限与配额

### 权限范围

API Key 归属于创建时的账号身份。

删除操作会校验 `AppId` 和 `SubAccountUin` 是否与目标 Key 一致；不属于当前身份的 Key 无法删除。

API Key 的可用范围跟随创建者当前的 AGS 账号权限。

### 配额

配额按 `SubAccountUin` 维度生效。

达到上限后创建会返回 `LimitExceeded.APIKeyQuota`。

## 安全建议

创建后立即将明文 `APIKey` 存入密钥管理系统，不要保存在聊天记录、文档或代码仓库中。

为不同环境（dev / staging / prod）创建独立 Key，避免跨环境复用。

定期执行 `agr apikey list` 清理不再使用的 Key。

怀疑泄漏时，优先删除旧 Key，再创建新 Key。

使用清晰的 `Name` 标识用途，便于后续识别和审计。

## 相关文档

[沙箱访问 Token](https://cloud.tencent.com/document/product/1814/132406)
