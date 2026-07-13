<!-- source: https://cloud.tencent.com/document/product/1814/132322 -->
<!-- fetcher: jina -->

# 启动 Sandbox Instance

最近更新时间：2026-06-03 09:09:00


## 适用场景

已有可用的 Sandbox Tool，需要启动一个临时实例来执行代码、调试 Browser 或验证自定义镜像。

需要在命令行中获取 `InstanceId`、`Status`、`TimeoutSeconds` 等字段，便于后续查询、调用和清理。

## 前提条件

已完成 [创建沙箱工具](https://cloud.tencent.com/document/product/1814/132210)，并拿到目标 `ToolId` 或 `ToolName`。

已按 [安装与配置](https://cloud.tencent.com/document/product/1814/132205) 完成 `agr` CLI 配置，或已具备 Cloud API 调用凭证。

已了解实例停止与自动过期规则。相关说明请参见 [停止与超时](https://cloud.tencent.com/document/product/1814/132338)。

确认 CLI 凭证已就绪：

agr version -o json

agr status -o json

确认 `agr status -o json` 返回中 `.Data.Auth.SecretId.Present` 和 `.Data.Auth.SecretKey.Present` 均为 `true`。

## 启动前说明

### ToolId 与 ToolName 的选择

**推荐使用**`ToolId`：适合生产环境、脚本自动化和长期维护场景，避免因重名或改名带来歧义。

`ToolName`**备选**：适合名称唯一、临时验证或本地调试场景。使用前建议先确认目标 Tool 的名称、唯一标识和当前可用状态。

### 超时字段单位对照

不同入口对超时参数的格式要求如下：

写入位置 示例 单位 说明
`agr instance create --timeout``30m`duration 字符串 与 Cloud API 请求体保持一致，支持 `s`、`m`、`h` 后缀，例如 `5m`、`300s`、`1h`。
`agr instance create --request` 中的 `Timeout``"30m"`duration 字符串 适合一次性传入完整请求体的场景。
Cloud API `StartSandboxInstance` 请求体 `Timeout``"30m"`duration 字符串 支持 `s`、`m`、`h` 后缀。
返回字段 `TimeoutSeconds``1800`秒 无论通过哪种入口启动，返回值统一以秒表示。

CLI 的 `--timeout` 与请求体中的 `Timeout` 使用相同的 duration 字符串格式。

### 确认最终生效的超时

`agr instance create` 的公开 help 与 schema 仅说明 `--timeout` 的格式与用途，未声明省略该参数时 CLI 会自动填入固定默认值。因此，建议按以下方式确认实际生效的超时：

1. **启动前查询 Tool 默认超时**（可选）：

agr tool get <tool-id> -o json

返回中的 `DefaultTimeoutSeconds` 表示该 Tool 当前配置的默认超时，单位为秒。该值仅反映 Tool 层面的配置，不是 CLI 的默认入参。

2. **创建时显式传入**`--timeout`：

如果任务对运行时长有明确要求，请在 `agr instance create` 中显式传入 `--timeout`，不要依赖 CLI 文档中未声明的省略行为。

3. **创建后复核返回结果**：

无论是否显式传入 `--timeout`，都应在实例创建成功后，以返回结果中的 `TimeoutSeconds` 和 `ExpiresAt` 复核最终生效值。

不同实例类型的停止与过期策略请参见 [停止与超时](https://cloud.tencent.com/document/product/1814/132338)。

## 通过 ToolId 启动

这是推荐的主路径。

1. 启动实例：

agr instance create \

 --tool-id <tool-id> \

 --timeout 30m \

 -o json

2. 记录返回中的关键字段：

`InstanceId` — 实例唯一标识，后续查询和清理都需要使用。

`Status` — 当前状态，`RUNNING` 表示已就绪。

`TimeoutSeconds` — 实例超时时间（秒）。

`ExpiresAt` — 实例到期时间。

示例输出：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.create",

 "Status": "succeeded",

 "Data": {

 "InstanceId": "ins-3x7g5m9q",

 "ToolId": "sdt-2ab4cd6e",

 "ToolName": "python-runner",

 "Status": "RUNNING",

 "TimeoutSeconds": 1800,

 "ExpiresAt": "2026-05-20T22:45:00+08:00",

 "RequestId": "req-9f6d7a2b"

 }

}

## 通过 ToolName 启动

当名称唯一且您明确知道目标 Tool 时，可以使用 `ToolName` 作为备选路径。

agr instance create \

 --tool-name <tool-name> \

 --timeout 30m \

 -o json

该命令同样返回 `ToolId`、`ToolName`、`InstanceId` 和 `Status`。如果同名 Tool 存在歧义，请改用 `ToolId`。

## 启动时覆盖自定义配置

`agr instance create` 支持通过 `--custom-configuration` 和 `--request` 两种方式传入自定义配置。

### 方式一：--custom-configuration

准备配置文件 `custom-configuration.json`：

{

 "Env": [

 {

 "Name": "LOG_LEVEL",

 "Value": "debug"

 },

 {

 "Name": "SESSION_MODE",

 "Value": "batch"

 }

 ]

}

启动时指定配置文件：

agr instance create \

 --tool-id <tool-id> \

 --custom-configuration @custom-configuration.json \

 -o json

### 方式二：--request

当您需要把 `ToolId`、`Timeout` 和 `CustomConfiguration` 放到同一个请求体中时，可使用 `--request`。

准备 `start-instance.json`：

{

 "ToolId": "<tool-id>",

 "Timeout": "30m",

 "CustomConfiguration": {

 "Env": [

 {

 "Name": "LOG_LEVEL",

 "Value": "debug"

 }

 ]

 }

}

启动命令：

agr instance create --request @start-instance.json -o json

**注意：**

`--request` 中的 `Timeout` 与 `--timeout` 一样使用 duration 字符串（如 `"30m"`）。

当 `CustomConfiguration.Env` 与 Tool 默认环境变量同名时，启动请求中的值会覆盖 Tool 默认值；未重复的默认变量继续保留，新增变量追加到实例配置中。

## 验证实例是否启动完成

实例创建命令返回成功后，建议再执行一次查询确认实际状态：

agr instance get <instance-id> -o json

只有 `.Data.Status` 为 `RUNNING` 时，实例才真正就绪可用。

`STARTING` 表示请求已受理或实例仍在启动中，不能作为可用的判断依据。

建议同时确认 `.Data.TimeoutSeconds`、`.Data.ToolId` 和 `.Data.ToolName` 是否符合预期。

## 清理实例

临时调试或验证完成后，建议立即清理实例，避免继续占用运行中的实例配额。

agr instance delete <instance-id> -o json

确认返回中 `.Data.Deleted` 为 `1` 即表示删除成功。

**说明：**

当前 CLI 未提供独立的 `stop` 子命令。如果您的目标是提前结束临时实例，可直接使用 `agr instance delete` 完成清理。

## Cloud API 启动示例

Cloud API 使用 `StartSandboxInstance` 操作启动实例。请求中 `ToolId` 或 `ToolName` 至少填写一个；`Timeout` 为可选字段，传入时使用 duration 字符串格式（如 `"30m"`）。

如果 Cloud API 请求中不传 `Timeout`，当前公开 API 文档仅保证返回结构中的 `TimeoutSeconds`、`ExpiresAt` 在未设置时可能为空，不承诺服务端一定会按某个固定默认值或 Tool 默认值补齐。若业务需要确定运行时长，建议在请求中显式传入 `Timeout`，并在返回结果中复核 `TimeoutSeconds` 与 `ExpiresAt`。

### 按 ToolId 启动

{

 "Action": "StartSandboxInstance",

 "Version": "2025-04-01",

 "Region": "ap-guangzhou",

 "ToolId": "tool-9x2k3m7q",

 "Timeout": "30m",

 "CustomConfiguration": {

 "Env": [

 {

 "Name": "LOG_LEVEL",

 "Value": "debug"

 }

 ]

 }

}

### 按 ToolName 启动

{

 "Action": "StartSandboxInstance",

 "Version": "2025-04-01",

 "Region": "ap-guangzhou",

 "ToolName": "python-runner",

 "Timeout": "45m"

}

### 返回示例

成功返回采用 Cloud API V3 统一包装结构，业务字段位于 `Response` 中：

{

 "Response": {

 "Instance": {

 "InstanceId": "ins-4q2p8m1k",

 "ToolId": "tool-9x2k3m7q",

 "ToolName": "python-runner",

 "Status": "Running",

 "TimeoutSeconds": 1800,

 "ExpiresAt": "2026-05-20T20:45:00+08:00",

 "Persistent": false,

 "CustomConfiguration": {

 "Env": [

 {

 "Name": "LOG_LEVEL",

 "Value": "debug"

 }

 ]

 },

 "CreateTime": "2026-05-20T20:15:00+08:00",

 "UpdateTime": "2026-05-20T20:15:00+08:00"

 },

 "RequestId": "req-7c8f0d2a"

 }

}

如果返回错误，HTTP 状态码仍为 `200`，具体错误信息位于 `Response.Error.Code` 和 `Response.Error.Message`。
