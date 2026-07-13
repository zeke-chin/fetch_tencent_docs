<!-- source: https://cloud.tencent.com/document/product/1814/132206 -->
<!-- fetcher: jina -->

# agr CLI 常用操作示例

最近更新时间：2026-05-27 20:38:30


## 使用前检查

### 查看 CLI 版本

agr version -o json

返回结果中包含版本号和构建信息：

{

 "SchemaVersion": "agr.v1",

 "Command": "version",

 "Status": "succeeded",

 "Data": {

 "Version": "51d952b",

 "Commit": "51d952b",

 "BuildTime": "2026-05-24_11:23:07"

 }

}

### 检查当前配置与凭证状态

agr status -o json

重点确认以下字段：

`Data.Auth.SecretId.Present`

`Data.Auth.SecretKey.Present`

`Data.Region`

`Data.Domain`

`Data.EffectiveOutput`

凭证已生效时，返回结果类似：

{

 "SchemaVersion": "agr.v1",

 "Command": "status",

 "Status": "succeeded",

 "Data": {

 "Auth": {

 "SecretId": {

 "Present": true,

 "Source": "TENCENTCLOUD_SECRET_ID"

 },

 "SecretKey": {

 "Present": true,

 "Source": "TENCENTCLOUD_SECRET_KEY"

 }

 },

 "ConfigFound": false,

 "ConfigLoaded": false,

 "Region": "ap-guangzhou",

 "Domain": "tencentags.com",

 "EffectiveOutput": "json"

 }

}

### 诊断本地配置与连通性

agr doctor -o json

重点确认 `Data.Checks[]` 中的 `SecretId`、`SecretKey` 和 `Connectivity` 检查项。连通性正常时输出类似：

{

 "SchemaVersion": "agr.v1",

 "Command": "doctor",

 "Status": "succeeded",

 "Data": {

 "Checks": [

 {

 "Name": "Connectivity",

 "Status": "ok",

 "Message": "API reachable, credentials valid"

 }

 ]

 }

}

## 查询 Tool 和 Instance

### 查看 Tool 列表

agr tool list --limit 20 -o json --non-interactive

返回结果包含 `Data.Items[]` 和分页信息：

{

 "SchemaVersion": "agr.v1",

 "Command": "tool.list",

 "Status": "succeeded",

 "Data": {

 "Items": [

 {

 "ToolId": "sdt-xxxxxxxx",

 "ToolName": "example-tool",

 "ToolType": "android-world",

 "Status": "ACTIVE",

 "NetworkConfiguration": {

 "NetworkMode": "PUBLIC"

 }

 }

 ],

 "Pagination": {

 "Limit": 20,

 "Offset": 0,

 "Total": 487

 }

 }

}

### 查看 Tool 详情

agr tool get <tool-id> -o json --non-interactive

输出中包含目标 Tool 的 `ToolId`、`ToolName`、`ToolType`、`Status` 和 `NetworkConfiguration`。如果只需确认 Tool 是否可用，优先检查 `Data.Status` 是否为 `ACTIVE`。

### 查看实例列表

agr instance list --limit 20 -o json --non-interactive

返回结果包含 `Data.Items[]` 和分页信息：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.list",

 "Status": "succeeded",

 "Data": {

 "Items": [

 {

 "InstanceId": "f8e694...",

 "ToolId": "sdt-xxxxxxxx",

 "ToolName": "example-tool",

 "Status": "STOPPED",

 "AuthMode": "DEFAULT",

 "NetworkMode": "PUBLIC"

 }

 ],

 "Pagination": {

 "Limit": 20,

 "Offset": 0,

 "Total": 42370

 }

 }

}

如果只关心运行中的实例，可追加 `--filters '[{"Name":"Status","Values":["RUNNING"]}]'`。

### 查看实例详情

agr instance get <instance-id> -o json --non-interactive

输出包含 `InstanceId`、`ToolId`、`ToolName`、`Status`、`TimeoutSeconds` 和 `UpdateTime`：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.get",

 "Status": "succeeded",

 "Data": {

 "InstanceId": "f8e694...",

 "ToolId": "sdt-xxxxxxxx",

 "ToolName": "example-tool",

 "Status": "STOPPED",

 "AuthMode": "DEFAULT",

 "NetworkMode": "PUBLIC",

 "TimeoutSeconds": 0

 }

}

## 创建和管理 Instance

### 创建实例并提取 `InstanceId`

如需先查看完整响应，可直接执行：

agr instance create --tool-id <tool-id> --timeout 5m -o json

自动化脚本通常再配合 `--jq` 提取 `InstanceId`：

INSTANCE_ID=$(agr instance create --tool-id <tool-id> --timeout 5m -o json --jq '.Data.InstanceId')

成功信号：

命令返回统一 JSON 信封，`Command` 为 `instance.create`。

`Data.InstanceId` 为非空字符串。

后续执行 `agr instance get "$INSTANCE_ID" -o json --non-interactive` 时，可以查询到该实例。

如果更习惯按 Tool 名称创建，也可以使用：

agr instance create --tool-name <tool-name> --timeout 5m -o json

### 查询实例状态

agr instance get "$INSTANCE_ID" -o json --non-interactive

重点检查 `Data.Status`。当前常见状态包括：

`STARTING`

`RUNNING`

`FAILED`

`STOPPING`

`STOPPED`

如果实例刚创建完成但仍为 `STARTING`，请等待片刻后重新查询，直到状态进入 `RUNNING` 再继续执行实例内操作。

### 暂停和恢复实例

agr instance pause "$INSTANCE_ID" -o json

agr instance get "$INSTANCE_ID" -o json --non-interactive

agr instance resume "$INSTANCE_ID" -o json

agr instance get "$INSTANCE_ID" -o json --non-interactive

执行后再用 `agr instance get "$INSTANCE_ID" -o json --non-interactive` 观察 `Data.Status` 是否切换为期望状态。如果状态未变化，请稍后重试，并确认实例当前生命周期是否允许暂停或恢复。

### 删除实例

agr instance delete "$INSTANCE_ID" --ignore-not-found -o json

成功信号：

命令返回统一 JSON 信封，`Status` 为 `succeeded`。

`Data.Deleted` 为 `1`，`Data.Failed` 为 `0`。

如需补充验证，可重新执行 `agr instance list --limit 20 -o json --non-interactive`，确认该实例不再出现在当前列表结果中。

## 在实例内执行代码和命令

### 在已有实例中执行代码

agr instance code run "$INSTANCE_ID" -l python -c 'print("hello from agr")' -o json

执行结果默认以 JSON 返回；如果需要实时查看 stdout/stderr，请改用 `--stream -o ndjson`。

从文件读取代码：

agr instance code run "$INSTANCE_ID" -l python -f ./hello.py -o json

如果需要实时输出，请改用：

agr instance code run "$INSTANCE_ID" -l python -c 'print("hello from agr")' --stream -o ndjson

`--stream` 不能与 `-o json` 同时使用。

### 使用临时实例执行一次性代码

agr instance code run --create-temp-instance -t <tool-name> -l python -c 'print("hello from temp instance")' -o json

适用场景：

只想验证 Tool 是否可运行。

不希望手动管理实例生命周期。

如果要保留临时实例便于继续排查，可追加 `--cleanup never`，然后手动执行 `agr instance delete`。

### 执行 Shell 命令

agr instance exec "$INSTANCE_ID" -o json -- pwd

指定工作目录和环境变量：

agr instance exec "$INSTANCE_ID" -o json --cwd /workspace --env APP_ENV=dev -- bash -lc 'echo $APP_ENV && pwd'

远端命令必须放在 `--` 之后，否则 CLI 会把后续参数继续解析为本地 flag。

如果命令返回 `INTERNAL_ERROR`，请先确认实例处于 `RUNNING`，再结合 `agr doctor -o json` 和 `agr instance get "$INSTANCE_ID" -o json --non-interactive` 排查实例健康状态。

## 文件传输和端口代理

### 上传文件到实例

agr instance file upload "$INSTANCE_ID" ./notes.txt /home/user/notes.txt -o json --non-interactive

上传后可通过后续业务命令读取目标路径，或在应用内直接验证该文件是否已经可用。如果命令返回 `INTERNAL_ERROR`，请先确认实例处于 `RUNNING`，并检查目标路径、实例内用户权限和当前实例类型是否支持该文件操作。

### 从实例下载文件

agr instance file download "$INSTANCE_ID" /home/user/notes.txt ./notes.txt -o json --non-interactive

下载后先在本地检查目标文件是否已经生成；如需进一步确认，可将本地文件内容与远端源文件再次比对。如果命令返回 `INTERNAL_ERROR`，请先确认实例状态、源路径和当前实例类型是否支持该文件操作。

### 建立端口代理

agr instance proxy "$INSTANCE_ID" 3000:8080

绑定所有本地网卡：

agr instance proxy "$INSTANCE_ID" 8080 --address 0.0.0.0

`agr instance proxy` 以前台方式运行，建立本地端口与实例端口的映射。执行后直接访问本地映射端口验证实例内服务是否可达；停止代理时终止当前进程即可。

### 获取 Browser 实例的 VNC 地址

agr instance browser vnc <instance-id> -o json

如需指定 VNC 端口：

agr instance browser vnc <instance-id> --port 9000 -o json

返回结果中包含 `Data.InstanceId`、`Data.VncUrl` 和 `Data.CdpUrl`。这些 URL 会附带临时访问参数，请勿直接写入脚本仓库或长期日志。

## 故障排查

### 云端凭证未配置

症状：

`agr status -o json` 中 `Data.Auth.SecretId.Present` 或 `Data.Auth.SecretKey.Present` 为 `false`。

`agr doctor -o json` 中 `SecretId`、`SecretKey` 检查项为 `warning`。

查询或管理命令返回认证相关错误，例如 `MISSING_CLOUD_CREDENTIALS`。

处理方式：

agr init --secret-id <your-secret-id> --secret-key <your-secret-key> --non-interactive

agr status -o json

agr doctor -o json

### 网络不通或 Endpoint 配置错误

症状：

已配置凭证后，`agr doctor -o json` 中 `Connectivity` 检查项不是 `ok`。

业务命令返回网络连接、TLS 或超时类错误。

处理方式：

先运行 `agr doctor -o json`，确认问题是否出在连通性。

如果仍处于未配置凭证状态，先完成初始化，再重新执行连通性检查。

检查 `--cloud-endpoint`、`--region`、代理设置和本地网络出口。

如果只想恢复默认设置，可先移除自定义的 `--cloud-endpoint` 参数后重试。

### 命令或参数与当前版本不匹配

症状：

CLI 返回 `unknown command`、`INVALID_USAGE` 或参数解析错误。

命令以退出码 `2` 结束，表示用法错误。

处理方式：

agr --help

agr <command> --help

agr schema -o json

agr version -o json

agr explain exit-codes -o json

`agr explain exit-codes -o json` 可用于查看当前 CLI 的退出码含义：

{

 "0": "success",

 "1": "error",

 "2": "usage",

 "4": "auth",

 "255": "remote_execution_failed"

}

如果旧脚本仍然使用已经不存在的命令组，请以当前版本的 `agr --help` 和 `agr schema -o json` 为准进行调整。

### 本地缓存目录不可写

症状：

`agr doctor -o json` 的 `Data.Checks[]` 中出现 `TokenCache` 警告。

处理方式：

为 `~/.agr` 准备可写目录，或在命令中使用 `--config` 指向可写配置文件路径。

## 相关文档

安装与配置

agr CLI 命令参考

启动 Sandbox Instance

查询 Sandbox Instance

停止与超时

常见错误码
