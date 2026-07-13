<!-- source: https://cloud.tencent.com/document/product/1814/132323 -->
<!-- fetcher: jina -->

# 暂停与恢复 Sandbox Instance

最近更新时间：2026-06-03 09:09:00


## 操作场景

当您需要临时中断正在运行的 Sandbox Instance，但后续仍要继续使用时，可将实例暂停至 `PAUSED` 状态，并在需要时恢复到 `RUNNING` 状态。

## 对系统影响

暂停成功后，实例在恢复前不再提供原有访问能力。

暂停的实例会占用暂停实例配额；恢复成功后释放对应的暂停实例配额。

## 准备工作

已创建目标实例，并记录实例 ID。

暂停前确认实例状态为 `RUNNING`。

恢复前确认实例状态为 `PAUSED`。

如需使用 CLI，请执行 `agr status -o json`，确认 `Auth.SecretId.Present` 和 `Auth.SecretKey.Present` 都为 `true`。

如果您需要在恢复时同时更新实例超时时间，请准备 Cloud API 调用能力。

## 使用 CLI 暂停实例

1. 准备实例 ID。

INSTANCE_ID="uuid"

2. 暂停实例。

agr instance pause "$INSTANCE_ID" -o json

返回 `RequestId` 表示暂停请求已受理：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.pause",

 "Status": "succeeded",

 "Data": {

 "RequestId": "11111111-2222-3333-4444-555555555555"

 },

 "Failure": null

}

3. 查询实例状态，确认已暂停。

agr instance get "$INSTANCE_ID" -o json

查询结果可能短暂显示 `PAUSING`。当 `Status` 变为 `PAUSED` 时，暂停完成：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.get",

 "Status": "succeeded",

 "Data": {

 "InstanceId": "uuid",

 "ToolId": "sdt-3q9m7n2p",

 "ToolName": "code-interpreter-v1",

 "Status": "PAUSED",

 "TimeoutSeconds": 1800,

 "NetworkMode": "PUBLIC",

 "Persistent": false,

 "UpdateTime": "2026-05-19T10:12:30+08:00"

 },

 "Failure": null

}

## 使用 CLI 恢复实例

1. 恢复实例。

agr instance resume "$INSTANCE_ID" -o json

返回 `RequestId` 表示恢复请求已受理：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.resume",

 "Status": "succeeded",

 "Data": {

 "RequestId": "66666666-7777-8888-9999-000000000000"

 },

 "Failure": null

}

2. 查询实例状态，确认已恢复。

agr instance get "$INSTANCE_ID" -o json

查询结果可能短暂显示 `RESUMING`。当 `Status` 变为 `RUNNING` 时，恢复完成：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.get",

 "Status": "succeeded",

 "Data": {

 "InstanceId": "uuid",

 "ToolId": "sdt-3q9m7n2p",

 "ToolName": "code-interpreter-v1",

 "Status": "RUNNING",

 "TimeoutSeconds": 1800,

 "NetworkMode": "PUBLIC",

 "Persistent": false,

 "UpdateTime": "2026-05-19T10:18:10+08:00"

 },

 "Failure": null

}

## 清理资源

如果本次操作仅用于验证暂停与恢复功能，建议完成后删除该实例，避免保留不再使用的资源。

1. 删除实例。

agr instance delete "$INSTANCE_ID" -o json

返回示例：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.delete",

 "Status": "succeeded",

 "Data": {

 "Deleted": 1,

 "Failed": 0

 },

 "Failure": null

}

2. 验证清理结果。

agr instance get "$INSTANCE_ID" -o json

删除完成后，实例状态变为 `STOPPED`。如果状态仍为 `RUNNING` 或 `PAUSED`，请稍后重试删除操作。

## 状态流转

当前状态 可执行操作 中间状态 完成状态
`RUNNING`暂停`PAUSING``PAUSED`
`PAUSED`恢复`RESUMING``RUNNING`
`RESUME_FAILED`再次恢复`RESUMING``RUNNING`

## 相关操作

[启动 Sandbox Instance](https://cloud.tencent.com/document/product/1814/132322)

[查询 Sandbox Instance](https://cloud.tencent.com/document/product/1814/132375)

[停止与超时](https://cloud.tencent.com/document/product/1814/132338)
