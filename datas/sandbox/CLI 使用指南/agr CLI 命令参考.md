<!-- source: https://cloud.tencent.com/document/product/1814/132207 -->
<!-- fetcher: jina -->

# agr CLI 命令参考

最近更新时间：2026-05-27 20:38:30


## 概述

`agr` 是 AGS 的命令行工具，用于管理 Tool、Instance、API Key、镜像预缓存任务，以及本地配置、诊断和原始 API 调用。

本文记录 `agr` 已公开的命令、参数形态和 JSON 输出约定。示例中的 `<tool-id>`、`<tool-name>`、`<instance-id>`、`<key-id>` 和镜像地址均为占位符。

## 使用前提

已安装 `agr`。

访问云端资源的命令需要可用的云端凭证。

自动化场景建议统一追加 `-o json --non-interactive`。

确认 CLI 可用：

agr version -o json

agr status -o json

agr doctor -o json

`agr version` 返回 `Data.Version`、`Data.Commit` 和 `Data.BuildTime`；`agr status` 返回 `Data.Auth`、`Data.Region`、`Data.Domain` 和 `Data.EffectiveOutput`；`agr doctor` 返回 `Data.Checks[]`，可直接查看凭证、连通性和本地配置状态。

如果需要初始化本地配置：

agr init --secret-id <your-secret-id> --secret-key <your-secret-key> --overwrite -o json

成功时返回统一 JSON 信封，`Status` 为 `succeeded`，`Failure` 为 `null`。重新执行 `agr status -o json` 时，`Data.Auth.SecretId.Present` 和 `Data.Auth.SecretKey.Present` 应为 `true`。

## 全局参数与输出

### 全局参数

参数 含义
`-o, --output`输出格式，支持 `text`、`json`、`ndjson`。
`--jq`对 JSON 输出执行 `jq` 表达式提取。
`--non-interactive`关闭交互行为。
`--config`指定配置文件路径。
`--region`指定访问地域，默认 `ap-guangzhou`。
`--cloud-endpoint`指定控制面 API Endpoint。
`--domain`指定数据面基础域名，默认 `tencentags.com`。
`--secret-id`显式传入 `SecretId`。
`--secret-key`显式传入 `SecretKey`。
`--debug`输出调试信息到标准错误。
`--generate-skeleton`为支持 request 的命令输出请求骨架。
`--no-browser`关闭自动打开浏览器。
`--no-color`关闭 ANSI 颜色输出。
`--internal`内部 Endpoint 快捷参数，已标记为 deprecated。

### JSON 输出信封

支持 JSON 输出的命令统一返回以下结构：

{

 "SchemaVersion": "agr.v1",

 "Command": "version",

 "Status": "succeeded",

 "Data": {},

 "Failure": null,

 "Warnings": [],

 "Meta": {

 "Backend": "cloud",

 "DurationMs": 0

 }

}

字段 含义
`SchemaVersion`返回结构版本。
`Command`实际执行的命令名。
`Status`执行状态，常见值为 `succeeded` 或 `failed`。
`Data`命令主体结果。
`Failure`失败详情；成功时为 `null`。
`Warnings`警告列表。
`Meta`元数据，常见字段为 `Backend` 和 `DurationMs`。

## 顶层命令

命令 别名 说明 JSON 输出 备注
`agr tool``t`管理 Tool 模板 支持 远端资源命令
`agr instance``i`管理 Instance 和实例内操作 支持`login`、`proxy` 为交互式
`agr apikey``ak`、`key`管理 API Key 支持 远端资源命令
`agr image`无 管理镜像相关任务 支持 公开子命令为 `precache`
`agr api`无 发送原始 Cloud API 请求 支持 低层 escape hatch
`agr init`无 初始化本地 CLI 配置 支持 本地配置命令
`agr explain`无 解释错误码和退出码 支持 只读
`agr status`无 查看当前 CLI 配置状态 支持 只读
`agr schema`无 输出机器可读命令 schema 支持 只读
`agr doctor`无 诊断本地配置和连通性 支持 只读
`agr version`无 查看 CLI 版本 支持 只读
`agr completion`无 生成 Shell 自动补全脚本 不支持 本地辅助命令

## Tool 命令

`agr tool` 用于管理沙箱 Tool 模板。

命令 别名 说明 JSON 输出
`agr tool create`无 创建 Tool 支持
`agr tool list`无 列出 Tool 支持
`agr tool get <tool-id>`无 查询 Tool 详情 支持
`agr tool update <tool-id>`无 更新 Tool 支持
`agr tool delete <tool-id>`无 删除 Tool 支持

### 创建 Tool

agr tool create -n <tool-name> -t <tool-type> --network SANDBOX -o json

常用参数：

参数 必填 含义
`-n, --name`是 Tool 名称
`-t, --type`是 Tool 类型
`--network`否 网络模式，支持 `PUBLIC`、`VPC`、`SANDBOX`
`-d, --description`否 Tool 描述
`--timeout`否 默认超时，例如 `5m`、`300s`、`1h`
`--persistent`否 是否创建持久化沙箱
`--mount`否 存储挂载 DSL
`--tag`否 标签，格式为 `key=value`
`--custom-configuration`否`CustomConfiguration` JSON、`@file` 或标准输入
`--log-configuration`否`LogConfiguration` JSON、`@file` 或标准输入
`--client-token`否 幂等令牌
`--request`否 完整请求体 JSON、`@file` 或标准输入

查看请求骨架：

agr tool create --generate-skeleton

输出的骨架包含 `NetworkConfiguration`、`StorageMounts`、`Tags` 等字段，可作为完整请求体的编辑起点。

### 查询、更新和删除 Tool

agr tool list --limit 20 -o json

agr tool get <tool-id> -o json

agr tool update <tool-id> --description "updated description" -o json

agr tool delete <tool-id> -o json

以上命令均支持 `-o json`，返回统一 JSON 信封。可通过 `agr tool <subcommand> --help` 查看各子命令的完整参数和过滤项。

## Instance 命令

`agr instance` 用于管理基于 Tool 创建的运行实例，以及在实例内执行代码、Shell、文件传输、Browser 和 Mobile 操作。

### 生命周期命令

命令 别名 说明 JSON 输出
`agr instance create``c`创建实例 支持
`agr instance list`无 列出实例 支持
`agr instance get <instance-id>`无 查询实例详情 支持
`agr instance update <instance-id>`无 更新实例 支持
`agr instance pause <instance-id>`无 暂停实例 支持
`agr instance resume <instance-id>`无 恢复实例 支持
`agr instance delete <instance-id>`无 删除实例 支持

### 创建实例

agr instance create --tool-name <tool-name> -o json

或通过 Tool ID：

agr instance create --tool-id <tool-id> -o json

常用参数：

参数 必填 含义
`-t, --tool-name`与 `--tool-id` 二选一 Tool 名称
`--tool-id`与 `--tool-name` 二选一 Tool ID
`--timeout`否 实例超时，例如 `5m`、`300s`、`1h`；裸数字按秒处理
`--auth-mode`否 认证模式，支持 `DEFAULT`、`TOKEN`、`NONE`、`PUBLIC`
`--mount-option`否 挂载覆盖项，可重复传入
`--metadata`否 JSON 数组形式的元数据
`--metadata-kv`否`KEY=VALUE` 形式的元数据
`--custom-configuration`否`CustomConfiguration` JSON、`@file` 或标准输入
`--client-token`否 幂等令牌
`--request`否 完整请求体 JSON、`@file` 或标准输入

查看请求骨架：

agr instance create --generate-skeleton

输出的骨架包含 `ToolId`、`ToolName`、`Timeout`、`MountOptions` 和 `Metadata` 等字段。

### 查询与状态过滤

agr instance list --limit 20 -o json

agr instance list --status RUNNING -o json

agr instance get <instance-id> -o json

`agr instance list` 支持的 `--status` 过滤值：

状态值 含义
`STARTING`正在启动
`RUNNING`运行中
`FAILED`启动失败
`STOPPING`正在停止
`STOPPED`已停止

### 更新、暂停、恢复和删除

agr instance update <instance-id> --timeout 10m -o json

agr instance pause <instance-id> -o json

agr instance resume <instance-id> -o json

agr instance delete <instance-id> --ignore-not-found -o json

删除场景建议保留 `--ignore-not-found`，便于脚本幂等清理。

### 实例内代码执行和 Shell 执行

命令 JSON 输出 NDJSON 输出 备注
`agr instance code run <instance-id>`支持 支持`--stream` 适合配合 `-o ndjson`
`agr instance exec <instance-id> -- <command>`支持 支持 远端命令必须放在 `--` 后

代码执行示例：

agr instance code run <instance-id> -l python -c "print('hello')" -o json

Shell 执行示例：

agr instance exec <instance-id> -o json --cwd /workspace --env APP_ENV=prod -- python app.py

需要实时输出时，使用 `--stream -o ndjson` 或默认文本输出。`--stream` 不适合与 `-o json` 同时使用。

临时实例：追加 `--create-temp-instance`（默认 `--cleanup always`），命令完成后自动删除临时实例。如果改为 `--cleanup never`，需手动执行 `agr instance delete`。

支持的 `code run` 语言：

`python`

`javascript`

`typescript`

`r`

`java`

`bash`

### 文件传输

agr instance file upload <instance-id> ./app.py /workspace/app.py -o json

agr instance file download <instance-id> /workspace/result.json ./result.json -o json

两条命令均支持 `-o json` 和 `--user` 参数。

### Browser、Mobile 和交互式入口

命令 JSON 输出 交互式 说明
`agr instance browser vnc <instance-id>`支持 否 返回 Browser 实例的 VNC URL
`agr instance mobile connect <instance-id>`支持 否 建立后台隧道并执行 `adb connect`
`agr instance mobile disconnect [instance-id]`支持 否 支持 `--all`
`agr instance mobile list`支持 否 列出当前活动连接
`agr instance mobile adb <instance-id> -- <adb-args...>`支持 否 执行 `adb` 命令
`agr instance proxy <instance-id> [local_port:]<remote_port>`不支持 是 本地端口转发
`agr instance login <instance-id>`不支持 是 当前终端内直接打开 PTY 会话

示例：

agr instance browser vnc <instance-id> -o json

agr instance mobile list -o json

agr instance mobile adb <instance-id> -o json -- shell ls /sdcard

agr instance proxy <instance-id> 3000:8080 --address 127.0.0.1

agr instance login <instance-id> --user root

`browser vnc`、`mobile list` 和 `mobile adb` 支持 JSON 输出；`proxy` 和 `login` 为交互式命令，不返回 JSON。

## API Key 命令

`agr apikey` 用于管理 API Key。

agr apikey create -n <name> -o json

agr apikey list -o json

agr apikey delete <key-id> -o json

`create`、`list` 和 `delete` 均支持 `-o json`，返回统一 JSON 信封。

## 镜像预缓存命令

`agr image` 公开的命令组为 `precache`。

agr image precache create --image <image-ref> --image-registry-type enterprise -o json

agr image precache get <image-digest> --image <image-ref> --image-registry-type enterprise -o json

查看请求骨架：

agr image precache create --generate-skeleton

输出包含 `Image` 和 `ImageRegistryType` 两个请求字段。`--image-registry-type` 支持 `enterprise` 和 `personal`。

## 原始 API 调用

`agr api` 只公开 `call` 子命令，用于发送原始 Cloud API 请求。常规资源管理优先使用 `tool`、`instance`、`apikey` 和 `image` 命令组。

agr api call --help

该命令组属于低层接口，适合 typed surface 尚未覆盖的场景。

## 常见报错与排查

### 凭证未配置

症状：远端资源命令返回 `Failure.Code: "MISSING_CLOUD_CREDENTIALS"`。

{

 "SchemaVersion": "agr.v1",

 "Command": "tool.list",

 "Status": "failed",

 "Data": null,

 "Failure": {

 "Code": "MISSING_CLOUD_CREDENTIALS",

 "Kind": "auth",

 "Message": "cloud API credentials are required",

 "Hint": "Run: agr init --secret-id <id> --secret-key <key>, or set TENCENTCLOUD_SECRET_ID and TENCENTCLOUD_SECRET_KEY.",

 "Retryable": false

 }

}

处理方式：

运行 `agr init --secret-id <your-secret-id> --secret-key <your-secret-key> --overwrite -o json`。

或在当前 shell 注入 `TENCENTCLOUD_SECRET_ID` 和 `TENCENTCLOUD_SECRET_KEY` 后重试。

用 `agr status -o json` 和 `agr doctor -o json` 复核状态。

### 网络不通或 Endpoint 配置错误

症状：命令返回 `Failure.Code: "ClientError.NetworkError"`。

{

 "SchemaVersion": "agr.v1",

 "Command": "tool.list",

 "Status": "failed",

 "Data": null,

 "Failure": {

 "Code": "ClientError.NetworkError",

 "Kind": "error",

 "Message": "Fail to get response because Post \"https://127.0.0.1:9/\": dial tcp 127.0.0.1:9: connect: connection refused",

 "Hint": "Run 'agr doctor' to diagnose configuration and connectivity.",

 "Retryable": false

 }

}

处理方式：

先运行 `agr doctor -o json`，确认 `Connectivity` 检查项是否为 `ok`。

检查 `--cloud-endpoint`、代理和网络连通性配置。

### 命令不存在或参数不匹配

症状：CLI 返回 `INVALID_USAGE`，或提示 `unknown command`。

Error: unknown command "sandbox" for "agr" (INVALID_USAGE)

Hint: Run 'agr --help' or 'agr schema -o json' to inspect valid commands and flags.

处理方式：

用 `agr --help`、`agr <command> --help` 或 `agr schema -o json` 复核当前版本支持的命令和参数。

用 `agr version -o json` 核对当前 CLI 版本。

### 本地缓存目录不可写

症状：`agr doctor -o json` 的 `Data.Checks[]` 中出现 `TokenCache` 警告。

处理方式：按提示创建本地目录并收紧权限，例如 `mkdir -p ~/.agr && chmod 700 ~/.agr`。

## 清理试用资源

如果试用过程中创建了远端资源，结束后请及时清理：

agr instance delete <instance-id> --ignore-not-found -o json

agr tool delete <tool-id> -o json

agr apikey delete <key-id> -o json

如果使用了 `--create-temp-instance`（默认 `--cleanup always`），临时实例会自动删除；如果改为 `--cleanup never`，请手动执行 `agr instance delete`。

## 已知限制

`agr completion` 只生成补全脚本，不返回 JSON。

`agr instance login` 和 `agr instance proxy` 为交互式命令，不支持 JSON 输出。

`agr instance code run --stream` 更适合与 `-o ndjson` 或默认文本输出搭配。

`agr --help` 未公开 `snapshot`、`sandbox` 或 `docs` 顶层命令；不要把这些命令写成已发布 CLI 能力。
