<!-- source: https://cloud.tencent.com/document/product/1814/132375 -->
<!-- fetcher: jina -->

# 查询 Sandbox Instance

最近更新时间：2026-06-03 09:09:00


## 操作场景

确认实例是否正常运行。

按 Tool 筛选实例。

按状态筛选特定阶段的实例。

获取单个实例的详细信息。

在自动化流程中轮询实例状态，直到达到目标状态。

## 对系统影响

查询操作为只读，不会修改实例状态或配置。

## 前提条件

条件 说明
`agr` CLI 已安装并配置。执行 `agr doctor` 确认连通性
腾讯云凭证 环境变量 `TENCENTCLOUD_SECRET_ID` 和 `TENCENTCLOUD_SECRET_KEY` 已配置
权限 具备 Sandbox Instance 查询权限

验证环境就绪：

agr doctor -o json

## 查询实例列表

### 查询所有实例

agr instance list --limit 20 -o json

预期输出：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.list",

 "Status": "succeeded",

 "Data": {

 "Items": [

 {

 "InstanceId": "ins-abc12345",

 "ToolId": "tool-xyz78901",

 "ToolName": "my-dev-sandbox",

 "Status": "RUNNING",

 "TimeoutSeconds": 3600,

 "ExpiresAt": "2026-05-24T12:00:00Z",

 "CreateTime": "2026-05-24T10:00:00Z",

 "UpdateTime": "2026-05-24T10:00:05Z"

 },

 {

 "InstanceId": "ins-def67890",

 "ToolId": "tool-xyz78901",

 "ToolName": "my-dev-sandbox",

 "Status": "STOPPED",

 "StopReason": "TIMEOUT",

 "CreateTime": "2026-05-23T08:00:00Z",

 "UpdateTime": "2026-05-23T09:00:00Z"

 }

 ],

 "Pagination": {

 "Total": 2,

 "Offset": 0,

 "Limit": 20

 }

 },

 "Failure": null,

 "Warnings": [],

 "Meta": {}

}

### 按 Tool 筛选

查询某个 Tool 下的所有实例：

agr instance list --tool-id <tool-id> --limit 20 -o json

预期输出：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.list",

 "Status": "succeeded",

 "Data": {

 "Items": [

 {

 "InstanceId": "ins-abc12345",

 "ToolId": "tool-xyz78901",

 "ToolName": "my-dev-sandbox",

 "Status": "RUNNING",

 "TimeoutSeconds": 3600,

 "ExpiresAt": "2026-05-24T12:00:00Z",

 "CreateTime": "2026-05-24T10:00:00Z",

 "UpdateTime": "2026-05-24T10:00:05Z"

 }

 ],

 "Pagination": {

 "Total": 1,

 "Offset": 0,

 "Limit": 20

 }

 },

 "Failure": null,

 "Warnings": [],

 "Meta": {}

}

### 按状态筛选

查询处于特定状态的实例，使用 `--filters` 参数：

agr instance list --filters '[{"Name":"Status","Values":["RUNNING"]}]' --limit 20 -o json

预期输出：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.list",

 "Status": "succeeded",

 "Data": {

 "Items": [

 {

 "InstanceId": "ins-abc12345",

 "ToolId": "tool-xyz78901",

 "ToolName": "my-dev-sandbox",

 "Status": "RUNNING",

 "TimeoutSeconds": 3600,

 "ExpiresAt": "2026-05-24T12:00:00Z",

 "CreateTime": "2026-05-24T10:00:00Z",

 "UpdateTime": "2026-05-24T10:00:05Z"

 }

 ],

 "Pagination": {

 "Total": 1,

 "Offset": 0,

 "Limit": 20

 }

 },

 "Failure": null,

 "Warnings": [],

 "Meta": {}

}

筛选多个状态：

agr instance list --filters '[{"Name":"Status","Values":["RUNNING","STARTING"]}]' --limit 20 -o json

### 按实例 ID 批量查询

agr instance list --instance-ids ins-abc12345,ins-def67890 --limit 20 -o json

### 分页查询

当实例数量超过单页限制时，使用 `--offset` 和 `--limit` 进行分页：

agr instance list --offset 20 --limit 20 -o json

预期输出：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.list",

 "Status": "succeeded",

 "Data": {

 "Items": [

 {

 "InstanceId": "ins-page2001",

 "ToolId": "tool-batch001",

 "ToolName": "batch-runner",

 "Status": "STOPPED",

 "StopReason": "USER_STOPPED",

 "CreateTime": "2026-05-22T14:00:00Z",

 "UpdateTime": "2026-05-22T15:30:00Z"

 }

 ],

 "Pagination": {

 "Total": 35,

 "Offset": 20,

 "Limit": 20

 }

 },

 "Failure": null,

 "Warnings": [],

 "Meta": {}

}

### 组合筛选

`--tool-id`、`--filters` 和分页参数可以组合使用：

agr instance list --tool-id <tool-id> --filters '[{"Name":"Status","Values":["RUNNING"]}]' --offset 0 --limit 50 -o json

## 查询单个实例

获取指定实例的详细信息：

agr instance get <instance-id> -o json

预期输出：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.get",

 "Status": "succeeded",

 "Data": {

 "InstanceId": "ins-abc12345",

 "ToolId": "tool-xyz78901",

 "ToolName": "my-dev-sandbox",

 "Status": "RUNNING",

 "TimeoutSeconds": 3600,

 "ExpiresAt": "2026-05-24T12:00:00Z",

 "CreateTime": "2026-05-24T10:00:00Z",

 "UpdateTime": "2026-05-24T10:00:05Z"

 },

 "Failure": null,

 "Warnings": [],

 "Meta": {}

}

实例不存在时的错误输出：

{

 "SchemaVersion": "agr.v1",

 "Command": "instance.get",

 "Status": "failed",

 "Data": null,

 "Failure": {

 "Code": "INSTANCE_NOT_FOUND",

 "Kind": "not_found",

 "Message": "instance not found: ins-notexist",

 "Hint": "Run 'agr instance list' to find active instances.",

 "Retryable": false

 },

 "Warnings": [],

 "Meta": {}

}

## CLI 参数参考

### agr instance list

参数 类型 必填 说明
`--tool-id`string 否 按 Tool ID 筛选
`--instance-ids`stringArray 否 按实例 ID 列表筛选，逗号分隔
`--filters`string 否 JSON 数组格式的筛选条件，支持 `@file` 或 `-`（stdin）
`--limit`int 否 分页大小，最大 100
`--offset`int 否 分页偏移量
`--request`string 否 完整请求体 JSON，支持 `@file` 或 `-`（stdin）
`-o json`--输出 JSON 格式

#### Filters 支持的字段

Name Values 说明 示例
`Status`实例状态，大小写不敏感`[{"Name":"Status","Values":["RUNNING"]}]`
`created-since-time`RFC 3339 时间，返回此时间之后创建的实例`[{"Name":"created-since-time","Values":["2026-05-01T00:00:00Z"]}]`

当前 `--filters` 支持 `Status` 和 `created-since-time` 两个筛选字段。如需按标签等其他维度筛选，可在获取列表结果后于本地过滤。

### agr instance get

参数 类型 必填 说明
`<instance-id>`string（位置参数）是 目标实例 ID
`-o json`--输出 JSON 格式

## 返回结果字段说明

字段 类型 说明
`InstanceId`string 实例唯一标识
`ToolId`string 所属 Tool ID
`ToolName`string 所属 Tool 名称
`Status`string 实例当前状态
`TimeoutSeconds`int 实例超时时间（秒），运行中实例返回
`ExpiresAt`string 实例过期时间（RFC 3339），运行中实例返回
`StopReason`string 停止原因，已停止实例返回
`CreateTime`string 创建时间（RFC 3339）
`UpdateTime`string 最后更新时间（RFC 3339）

## 实例状态说明

状态 含义 是否终态
`STARTING`实例正在启动 否
`RUNNING`实例运行中，可执行操作 否
`STOPPING`实例正在停止 否
`STOPPED`实例已停止 是
`FAILED`实例启动失败 是
`STOP_FAILED`实例停止失败 是

自动化场景中，可轮询实例状态直到进入终态或目标状态 `RUNNING`。

## 常见错误

错误码 含义 处理方式
`INSTANCE_NOT_FOUND`实例不存在或已被清理 确认实例 ID 是否正确
`AUTH_FAILED`认证失败 检查腾讯云凭证配置
`MISSING_CLOUD_CREDENTIALS`未配置腾讯云凭证 配置 `TENCENTCLOUD_SECRET_ID` 和 `TENCENTCLOUD_SECRET_KEY`

## 相关文档

[启动 Sandbox Instance](https://cloud.tencent.com/document/product/1814/132322)：创建并启动实例，确认实例进入可用状态。

[实例生命周期](https://cloud.tencent.com/document/product/1814/132337)：实例从创建、运行到停止的状态流转全景。

[停止与超时](https://cloud.tencent.com/document/product/1814/132338)：主动停止实例，以及超时回收机制。

[修改运行中实例](https://cloud.tencent.com/document/product/1814/132324)：运行期间可调整的实例配置。

[沙箱启动失败排查](https://cloud.tencent.com/document/product/1814/132054)：查询结果为失败态时的排障路径。
