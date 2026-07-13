<!-- source: https://cloud.tencent.com/document/product/1814/132412 -->
<!-- fetcher: jina -->

# Mobile 沙箱（ADB）

最近更新时间：2026-06-03 09:09:00


## 操作场景

当您需要在 Mobile 沙箱中执行安装应用、采集日志、执行 Shell 命令、推送文件或拉取文件等调试任务时，可以通过 AGS CLI 建立本地 ADB 隧道，再使用 `agr instance mobile adb` 将 ADB 参数透传到目标实例。

适用场景包括：

安装或卸载测试 APK。

采集 `logcat` 日志定位应用问题。

执行 `adb shell` 检查系统属性、目录和进程状态。

在本地与实例之间传输测试文件。

## 前提条件

已创建并启动 Mobile 沙箱实例。

当前地域支持 Mobile 沙箱。

本地已安装 AGS CLI `agr`。执行 `agr version -o json` 验证命令可用；若正常返回版本信息，则表示已正确安装并加入 `PATH`。如命令不可用，请先参考 [安装与配置](https://cloud.tencent.com/document/product/1814/132205) 完成安装。

本地已安装 Android SDK Platform-Tools，且 `adb` 已加入 `PATH`；如果未加入 `PATH`，请先设置 `ADB_PATH` 环境变量指向 `adb` 可执行文件。

已完成 `agr` 身份凭证配置，并具备访问目标实例的权限。执行 `agr status -o json`，确认 `Data.ConfigFound`、`Data.ConfigLoaded`、`Data.Auth.SecretId.Present` 和 `Data.Auth.SecretKey.Present` 均为 `true`。

本地网络可以访问 AGS 服务域名的 443 端口。

## 操作步骤

### 建立 ADB 连接

1. 执行以下命令，建立到目标实例的本地 ADB 隧道：

agr -o json instance mobile connect ins-mobile-7f3c9b2d

预期输出为 JSON，重点关注 `Data.InstanceId`、`Data.AdbAddress`、`Data.Port` 和 `Data.LogPath` 字段。例如：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.mobile.connect",

 "Status": "succeeded",

 "Data": {

 "InstanceId": "ins-mobile-7f3c9b2d",

 "AdbAddress": "127.0.0.1:50379",

 "Port": 50379,

 "Pid": 48211,

 "LogPath": "/home/you/.agr/tunnel-ins-mobile-7f3c9b2d.log"

 },

 "Failure": null,

 "Warnings": [],

 "Meta": {

 "Backend": "remote",

 "DurationMs": 842

 }

}

该命令会为实例分配本地回环地址，并自动执行一次 `adb connect`。

2. 查看当前已建立的连接：

agr -o json instance mobile list

预期输出为 JSON，`Data.Items` 中会列出当前实例、本地映射地址和连接状态。例如：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.mobile.list",

 "Status": "succeeded",

 "Data": {

 "Items": [

 {

 "InstanceId": "ins-mobile-7f3c9b2d",

 "AdbAddress": "127.0.0.1:50379",

 "Port": 50379,

 "Pid": 48211,

 "CreatedAt": "2026-05-17T10:21:35+08:00",

 "Status": "connected"

 }

 ],

 "Total": 1

 },

 "Failure": null,

 "Warnings": [],

 "Meta": {

 "Backend": "remote",

 "DurationMs": 117

 }

}

如果 `Data.Total` 为 `1` 且 `Data.Items[0].Status` 为 `connected`，表示本地 ADB 隧道已建立。

### 执行常见 ADB 操作

建立连接后，您可以使用 `agr instance mobile adb` 将 ADB 参数透传到指定实例。

#### 执行 Shell 命令

agr -o json instance mobile adb ins-mobile-7f3c9b2d -- shell getprop ro.build.version.release

预期输出为 JSON，命令执行结果位于 `Data.Stdout`、`Data.Stderr` 和 `Data.ExitCode` 字段。例如：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.mobile.adb",

 "Status": "succeeded",

 "Data": {

 "Stdout": "14\n",

 "Stderr": "",

 "ExitCode": 0

 },

 "Failure": null,

 "Warnings": [],

 "Meta": {

 "Backend": "remote",

 "DurationMs": 221

 }

}

#### 安装应用

agr -o json instance mobile adb ins-mobile-7f3c9b2d -- install /path/to/demo.apk

#### 采集日志

agr -o json instance mobile adb ins-mobile-7f3c9b2d -- logcat

#### 推送文件

agr -o json instance mobile adb ins-mobile-7f3c9b2d -- push ./demo.apk /sdcard/Download/demo.apk

#### 拉取文件

agr -o json instance mobile adb ins-mobile-7f3c9b2d -- pull /sdcard/Download/result.json ./result.json

**注意：**

执行 `agr instance mobile adb` 时，必须在实例 ID 后添加 `--`，用于分隔 ADB 参数。

### 断开连接

完成操作后，执行以下命令断开单个实例连接：

agr -o json instance mobile disconnect ins-mobile-7f3c9b2d

如果需要一次性断开所有已建立的 Mobile ADB 连接，请执行：

agr -o json instance mobile disconnect --all

预期输出为 JSON，`Data.Disconnected` 返回已断开的实例 ID 列表，`Data.Count` 返回断开数量。例如：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.mobile.disconnect",

 "Status": "succeeded",

 "Data": {

 "Disconnected": [

 "ins-mobile-7f3c9b2d"

 ],

 "Count": 1

 },

 "Failure": null,

 "Warnings": [],

 "Meta": {

 "Backend": "remote",

 "DurationMs": 96

 }

}

## 使用说明

`agr instance mobile connect` 会在后台维护本地隧道，并把实例映射到 `127.0.0.1:<port>`。

`agr instance mobile list` 可用于查看当前实例、本地地址和连接状态。

`agr instance mobile adb` 适合直接执行单条 ADB 命令。

当您需要使用本地 `adb` 工具排查问题时，可以使用 `connect` 命令返回的 `Data.AdbAddress` 作为目标地址。

## 使用限制

同一实例同一时刻只保留一个活跃的 ADB 连接。新的连接建立后，旧连接会被断开。

当网络抖动导致隧道短暂中断时，CLI 会尝试自动重连；重连期间本地监听端口保持不变。

如果当前连接被另一个新的客户端抢占，原连接不会自动恢复，需要重新执行连接命令。

目标实例必须处于可访问状态；如果实例已停止、已销毁或当前账号无权限访问，连接命令会失败。

ADB 连接依赖本地 `adb` 可执行文件。未安装 `adb` 或配置错误时，`connect` 和 `adb` 子命令都无法执行。

## 相关操作

使用 `agr -o json instance mobile list` 查看当前已建立的连接。

使用 `agr -o json instance mobile disconnect --all` 清理本地全部 Mobile ADB 隧道。
