<!-- source: https://cloud.tencent.com/document/product/1814/132210 -->
<!-- fetcher: jina -->

# 创建沙箱工具（通过 CLI）

最近更新时间：2026-05-27 20:38:30


## 开始前检查

确认当前环境中的 `agr` CLI 可用：

agr version -o json --non-interactive

重点关注 `Data.Version` 和 `Data.Commit`。

**说明：**

如果 `agr tool create --help` 未显示本文参数，或 `agr version -o json` 未返回结构化结果，说明当前 CLI 版本过低，请先升级后再继续。

确认 Cloud API 凭证已注入当前 shell：

agr status -o json --non-interactive

当 `Data.Auth.SecretId.Present` 和 `Data.Auth.SecretKey.Present` 都为 `true` 时，当前 shell 已具备调用创建接口所需的认证信息。

如果准备使用 `VPC` 网络模式，还需要提前准备：

至少一个可用的 `SubnetIds`，用于指定 Tool 运行时可接入的子网。

至少一个可用的 `SecurityGroupIds`，用于指定该 Tool 关联的安全组。

按实际配置准备 `RoleArn`。如果配置了 COS 类型 `StorageMounts`、启用了 CLS 日志采集，或使用 `enterprise`/`personal` 镜像仓库，均需要提供对应角色授权。

## 选择 Tool 类型

创建请求中的 `ToolType` 使用短字符串值。下表列出当前公开支持的常见类型：

请求写法 典型场景 说明
`browser`浏览器访问、网页自动化 对应浏览器类预置 Tool。
`code-interpreter`代码执行、数据处理 适合最小可用 CLI 创建路径。
`mobile`移动端设备操作、移动端自动化 提供 Mobile 运行环境和 ADB 能力。
`osworld`桌面级交互、OS 环境操作 适合需要图形界面交互的任务。
`custom`自定义镜像、自定义启动命令、自定义端口 用于自定义容器 Tool。

`agr` CLI 的 `--type`、`--request` 以及后文 JSON 请求体都使用这些短值。完整类型列表与选型建议，请参见 [工具类型说明](https://cloud.tencent.com/document/product/1814/132209)。

## 选择网络模式

根据访问目标选择 `NetworkMode`：

模式 适用场景 额外前提
`SANDBOX`仅需隔离运行环境，不访问外部网络的场景 无额外网络参数。
`PUBLIC`需要访问公网或向外提供端口的场景 无额外网络参数。
`VPC`需要访问私网资源的场景 需要同时提供 `VpcConfig.SubnetIds` 和 `VpcConfig.SecurityGroupIds`。

当 `NetworkMode` 为 `VPC` 时：

必须同时提供 `VpcConfig.SubnetIds` 和 `VpcConfig.SecurityGroupIds`。

`SubnetIds` 为子网 ID（如 `subnet-xxx`），决定 Tool 可接入的子网。

`SecurityGroupIds` 为安全组 ID（如 `sg-xxx`），决定 Tool 关联的安全组。

**注意：**

在 `PUBLIC` 或 `SANDBOX` 模式下不要附带 `VpcConfig`。

## 使用 agr 创建预置 Tool

### 最小创建命令

以 `code-interpreter` 为例，演示最小 CLI 创建路径：

tool_name="code-interpreter-$(date +%s)"

agr tool create \

 --name "$tool_name" \

 --type code-interpreter \

 --network SANDBOX \

 --timeout 5m \

 -o json \

 --non-interactive

请求成功时返回：

{

 "SchemaVersion": "agr.v1",

 "Command": "tool.create",

 "Status": "succeeded",

 "Data": {

 "ToolId": "sdt-abc123xyz",

 "RequestId": "req-create-tool-20260522-001"

 }

}

返回 `ToolId` 仅表示创建请求已被接受，Tool 可能仍在异步创建中，建议进一步查询确认最终状态。

### 验证创建结果

使用 `ToolId` 查询 Tool 状态：

agr tool get <tool-id> -o json --non-interactive

建议核对以下字段：

字段 说明
`Data.ToolId`与创建返回一致。
`Data.ToolType`本文示例中回显 `code-interpreter`。
`Data.Status``ACTIVE` 表示可用于创建 Instance；`FAILED` 表示需要排查。
`Data.StatusReason`创建失败或状态异常时的直接排查入口。
`Data.NetworkConfiguration.NetworkMode`与请求中的网络模式一致。
`Data.DefaultTimeoutSeconds`超时配置换算后的秒数。

如需批量查看失败记录，建议先确认 `agr tool list` 已返回 `Data.Items`，再筛选 `FAILED` 状态：

agr tool list --limit 100 -o json --non-interactive

返回中包含 `Data.Items` 后，再执行：

agr tool list --limit 100 -o json --non-interactive \

 --jq '.Data.Items[] | select(.Status == "FAILED") | {ToolId, ToolName, StatusReason}'

## 创建自定义容器 Tool

当需要自定义镜像、启动命令、端口、资源规格或探针配置时，先准备完整 JSON 请求体，再通过 `agr tool create --request` 提交。

**说明：**

`agr tool create` 的 `--request` 接受完整 JSON 请求体（可包含网络、自定义配置、存储挂载等全部字段），支持 `@file` 或标准输入。`--mount` 和 `--tag` 支持多次传入。CLI 参数不使用 YAML 格式。

以下示例同时适用于：

CLI 的 `--request @tool-custom-python-web.json`

Cloud API `CreateSandboxTool` 的请求体

{

 "ToolName": "custom-python-web",

 "ToolType": "custom",

 "Description": "运行 Python Web 应用的自定义 Sandbox Tool",

 "DefaultTimeout": "30m",

 "ClientToken": "create-custom-python-web-20260522-001",

 "NetworkConfiguration": {

 "NetworkMode": "PUBLIC"

 },

 "Tags": [

 {

 "Key": "env",

 "Value": "test"

 },

 {

 "Key": "owner",

 "Value": "agent-platform"

 }

 ],

 "CustomConfiguration": {

 "Image": "crpi-xxxxxx.tencentcloudcr.com/agentrun/python-web:20260522",

 "ImageRegistryType": "enterprise",

 "Command": [

 "python"

 ],

 "Args": [

 "-m",

 "http.server",

 "8080"

 ],

 "Env": [

 {

 "Name": "APP_ENV",

 "Value": "test"

 }

 ],

 "Ports": [

 {

 "Name": "http",

 "Port": 8080,

 "Protocol": "TCP"

 }

 ],

 "Resources": {

 "CPU": "1000m",

 "Memory": "2Gi"

 },

 "Probe": {

 "HttpGet": {

 "Path": "/healthz",

 "Port": 8080,

 "Scheme": "HTTP"

 },

 "ReadyTimeoutMs": 10000,

 "ProbeTimeoutMs": 3000,

 "ProbePeriodMs": 1000,

 "SuccessThreshold": 1,

 "FailureThreshold": 5

 }

 }

}

将该请求体保存为 `tool-custom-python-web.json` 后，执行：

agr tool create \

 --request @tool-custom-python-web.json \

 -o json \

 --non-interactive

请求成功时返回：

{

 "SchemaVersion": "agr.v1",

 "Command": "tool.create",

 "Status": "succeeded",

 "Data": {

 "ToolId": "sdt-abc123xyz",

 "RequestId": "req-create-tool-20260522-001"

 }

}

创建后继续执行：

agr tool get <tool-id> -o json --non-interactive

确认 `Data.Status` 已进入 `ACTIVE`，再基于该 Tool 创建 Instance。

### custom 场景的关键字段

字段 使用说明
`DefaultTimeout`使用 duration 字符串，例如 `5m`、`300s`、`1h`。允许范围为 `300s` 到 `24h`；若低于 `300s`，接口将返回超时过小的错误。
`NetworkConfiguration.NetworkMode`使用 `PUBLIC`、`SANDBOX` 或 `VPC`。
`VpcConfig.SubnetIds` / `VpcConfig.SecurityGroupIds`仅在 `VPC` 模式下提供，至少各填写一个 ID。
`CustomConfiguration.Image`使用当前环境可访问的镜像地址。
`CustomConfiguration.ImageRegistryType`使用 `enterprise`、`personal` 或 `system`。
`CustomConfiguration.Command`必填，至少提供一个启动命令。
`CustomConfiguration.Ports`单个端口范围为 `1` 到 `65535`，协议使用 `TCP` 或 `UDP`。
`CustomConfiguration.Resources``CPU` 和 `Memory` 必填，使用 Kubernetes quantity 格式，例如 `1000m`、`2Gi`。服务端会结合配额和可用资源校验最终值。
`CustomConfiguration.Probe``ReadyTimeoutMs` 范围为 `1000` 到 `30000`；`ProbeTimeoutMs` 和 `ProbePeriodMs` 范围为 `100` 到 `30000`；`SuccessThreshold` 固定为 `1`；`FailureThreshold` 范围为 `1` 到 `100`。
`RoleArn`在以下场景需要提供：配置 COS 类型 `StorageMounts`、启用 CLS 日志采集，或使用 `enterprise`/`personal` 镜像仓库。

## 失败排查

如果创建后 Tool 长时间未进入 `ACTIVE`，按以下顺序排查：

1. 执行 `agr tool get <tool-id> -o json --non-interactive`。

2. 查看 `Data.Status` 是否为 `FAILED`。

3. 读取 `Data.StatusReason`，确认失败原因是否来自镜像、网络、探针、资源规格或授权配置。

4. 保留创建返回中的 `RequestId`，便于定位同一次创建请求。

5. 执行 `agr tool list --limit 100 -o json --non-interactive`，确认返回中已有 `Data.Items`。

6. 再执行 `agr tool list --limit 100 -o json --non-interactive --jq '.Data.Items[] | select(.Status == "FAILED") | {ToolId, ToolName, StatusReason}'`，筛选 `FAILED` 状态的 Tool。

**注意：**

如果当前 shell 未注入云凭证，`agr tool list` 会返回 `MISSING_CLOUD_CREDENTIALS`，此时 `Data` 为 `null`。在该响应上直接追加 `--jq` 表达式会返回 `INVALID_JQ_EXPRESSION`。遇到这种情况，请先补齐凭证再重试列表查询。

排查时重点回看以下输入：

`ToolType` 是否与目标场景一致

`NetworkMode` 是否与实际网络前提匹配

`VpcConfig` 是否仅在 `VPC` 模式下补齐

`RoleArn` 是否覆盖当前镜像、存储或日志需求

`CustomConfiguration.Image`、`Resources`、`Probe` 是否填写为服务端可接受的值

## 清理

验证完成后，如果不再需要该 Tool，执行以下命令清理：

agr tool delete <tool-id> -o json --non-interactive

删除前确认该 Tool 下没有运行中的 Instance，否则删除会被拒绝。删除后再次查询确认：

agr tool get <tool-id> -o json --non-interactive

查询返回资源不存在错误，说明该 Tool 已完成删除。

## 相关操作

[工具类型说明](https://cloud.tencent.com/document/product/1814/132209)

[查询沙箱工具](https://cloud.tencent.com/document/product/1814/132214)

[更新与删除](https://cloud.tencent.com/document/product/1814/132213)
