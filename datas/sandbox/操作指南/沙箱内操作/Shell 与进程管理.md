<!-- source: https://cloud.tencent.com/document/product/1814/132409 -->
<!-- fetcher: jina -->

# Shell 与进程管理

最近更新时间：2026-06-03 09:09:00


## 能力概览

Shell 与进程管理面向已经启动的 Sandbox Instance，适合以下场景：

执行一次性命令，例如查看进程、检查端口、读取日志。

打开交互式终端，直接在实例内排障或运行运维命令。

通过标准 Linux 命令启动后台进程，并在后续命令中查询状态或发送终止信号。

按需实时读取命令输出，而不是等待命令结束后一次性返回。

## 与代码执行的区别

维度 Shell 与进程管理 代码执行
主要入口`agr instance exec`、`agr instance login``agr instance code run`
主要输入 Shell command、参数、工作目录、环境变量 代码内容
典型返回 命令输出、退出状态，或交互式 PTY 会话 结构化执行结果、标准输出、标准错误
交互方式 可进入终端，也可流式读取命令输出 以一次执行请求为主
适合场景 运维命令、进程管理、交互式调试 运行代码片段、读取程序化结果

如果您的目标是“在实例里运行命令或管理进程”，请优先使用本文档中的 Shell 路径。如果您的目标是“提交一段代码并读取结构化执行结果”，请参见 [代码执行](https://cloud.tencent.com/document/product/1814/132408)。

## 入口选择

需求 推荐入口
执行一次性命令`agr instance exec`
实时读取命令输出`agr instance exec -s`
打开交互式终端`agr instance login`

## 前提条件

一个处于 RUNNING 状态的 Sandbox Instance（通过 `agr instance create` 创建，或使用已有实例）。

已安装 `agr` CLI，并已完成可访问目标实例的认证配置。

已获取目标实例的 Instance ID（通过 `agr instance list` 查看）。

建议先运行以下命令检查 CLI 与认证是否就绪：

agr version -o json

agr doctor -o json

可按以下信号判断环境是否已就绪：

`agr version -o json` 成功时，返回结果中的 `Status` 为 `succeeded`，并包含 `Data.Version`、`Data.Commit` 等版本信息。

`agr doctor -o json` 会返回 `Checks` 数组；继续执行本文步骤前，`SecretId`、`SecretKey` 和 `Connectivity` 三项应为 `ok`。如果任一项为 `warning`，请先按命令输出提示补齐认证配置。

示例中统一使用以下占位符：

export INSTANCE_ID="ins-xxxxxxxx"

## 执行一次性 Shell 命令

适用于检查实例当前状态，或执行会在短时间内结束的命令。

agr -o json instance exec "$INSTANCE_ID" -- ps -ef

命令成功后，返回结果中的 `Status` 为 `succeeded`，`Data.ExitCode` 为 `0`，`Data.Stdout` 中包含 `UID PID PPID` 等进程列表表头以及至少一行进程记录。例如：

{

 "Status": "succeeded",

 "Data": {

 "Stdout": "UID PID PPID C STIME TTY TIME CMD\nuser 1 0 0 10:00 ? 00:00:00 /usr/bin/python3 -m app",

 "Stderr": "",

 "ExitCode": 0

 }

}

如果远端命令执行失败，例如命令不存在、权限不足，或 Shell 本身返回非零退出码，CLI 会返回 `REMOTE_COMMAND_FAILED`，并以退出码 `255` 退出。建议优先检查 `Data.Error`、`Data.Stdout`、`Data.Stderr` 和 `Data.ExitCode` 四个字段定位问题。

您也可以为命令显式指定工作目录、环境变量或运行用户：

agr -o json instance exec "$INSTANCE_ID" \

 --cwd /workspace \

 --env APP_ENV=dev \

 --user user \

 -- sh -lc 'pwd && echo "$APP_ENV"'

## 流式读取命令输出

对于需要边执行边消费输出的命令，使用 `-s` 打开流式模式。输出按时间顺序逐行返回，而不是等命令全部结束后一次性输出。

agr -o ndjson instance exec "$INSTANCE_ID" -s -- \

 sh -lc 'for i in 1 2 3; do echo "tick-$i"; sleep 1; done'

流式模式下，CLI 以 NDJSON（每行一条 JSON 记录）格式持续输出命令执行过程中产生的内容，直到命令结束。

## 打开交互式 PTY 终端

当您需要持续输入命令、查看即时回显或手动排障时，使用交互式终端。

agr instance login "$INSTANCE_ID"

如果需要以其他用户进入终端，可显式指定 `--user`：

agr instance login "$INSTANCE_ID" --user root

命令会直接在当前控制台中建立 PTY 会话，进入会话后您可以看到 Shell 提示符并继续输入命令。在会话内执行 `exit` 即可正常退出终端。

**说明：**

`agr instance login` 直接接入 PTY 会话，不返回 JSON 结构化输出。

## 启动和检查后台进程

如果您需要在实例内保留一个后台任务，可以使用标准 Linux 方式在 Shell 中后台启动进程。

以下示例在实例内启动一个监听 `8080` 端口的简单 HTTP 服务，并回显后台进程 PID：

agr -o json instance exec "$INSTANCE_ID" -- \

 sh -lc 'nohup python3 -m http.server 8080 >/tmp/http-server.log 2>&1 & echo $!'

命令成功后，返回结果中包含 Shell 输出的 PID 值。启动后，使用新的命令检查进程是否仍在运行：

agr -o json instance exec "$INSTANCE_ID" -- \

 sh -lc 'ps -ef | grep "[h]ttp.server 8080"'

返回结果中包含对应进程的信息时，说明后台服务仍在运行。

## 发送终止信号

需要终止进程时，通过 `agr instance exec` 调用实例内的标准 Linux 命令。

优雅停止进程：

agr -o json instance exec "$INSTANCE_ID" -- kill -TERM 42

如果进程在等待期内仍未退出，再发送强制终止信号：

agr -o json instance exec "$INSTANCE_ID" -- kill -KILL 42

停止后检查进程状态：

agr -o json instance exec "$INSTANCE_ID" -- \

 sh -lc 'ps -p 42 -o pid='

当指定 PID 的进程已不存在时，`ps` 命令的退出码为非零且标准输出为空。`kill -TERM` 适合优雅停止可自行清理的进程；进程仍未退出时再使用 `kill -KILL` 强制终止。

## 支持的参数

参数 说明 适用命令
`--cwd`指定远端命令的工作目录`agr instance exec`
`--env`注入环境变量，格式为 `KEY=VALUE`，可重复指定`agr instance exec`
`--user`指定运行命令或终端的用户（默认 `user`）`agr instance exec`、`agr instance login`
`-s` / `--stream`启用流式输出模式`agr instance exec`
`-o json`以 JSON 格式返回结果`agr instance exec`
`-o ndjson`以 NDJSON 格式返回流式输出`agr instance exec`（配合 `-s`）

## 已知边界

`agr instance exec` 支持 `--cwd`、`--env`、`--user` 和 `-s`（流式）。

`agr instance login` 建立本地 PTY 会话，支持 `--user` 参数切换用户。

进程管理依赖标准 Linux 命令（`ps`、`kill`、`nohup` 等），无独立的进程生命周期子命令。

代码执行使用独立入口 `agr instance code run`，输入模型与 Shell 命令不同。

## 错误处理

CLI 常见失败类型：

命令 失败类型
`agr instance exec``MISSING_INSTANCE`、`REMOTE_COMMAND_FAILED`、`MISSING_CLOUD_CREDENTIALS`、`AUTH_FAILED`、`INVALID_JQ_EXPRESSION`
`agr instance login``MISSING_CLOUD_CREDENTIALS`、`AUTH_FAILED`

当命令执行失败时，优先检查：

`instance-id` 是否正确，实例是否仍处于 RUNNING 状态。

当前账号是否具备访问该实例的权限。实例在列表中可见不等于对该实例具备执行权限；如果遇到 `AUTH_FAILED`，请确认当前账号对目标实例的操作授权。

远端命令本身是否存在语法错误、权限不足或依赖缺失。
