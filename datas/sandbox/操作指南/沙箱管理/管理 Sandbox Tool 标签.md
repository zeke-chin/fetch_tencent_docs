<!-- source: https://cloud.tencent.com/document/product/1814/132212 -->
<!-- fetcher: jina -->

# 管理 Sandbox Tool 标签

最近更新时间：2026-05-27 20:38:30


## 开始之前

已安装 `agr` CLI。

已配置可调用 AGS 的云 API 凭证。

已确认本次操作使用的地域，以及目标 Tool 所在账号上下文。

如果要更新或清空标签，需准备目标 `ToolId`。

如需切换地域，可在命令中追加 `--region <region>`。

## CLI 操作总览

任务 命令 说明
创建 Tool 时设置标签`agr tool create --tags '[{"Key":"env","Value":"prod"}]'``--tags` 接收 JSON 数组，可一次传入多个标签
按标签筛选 Tool`agr tool list --filters '[{"Name":"Tag","Values":["env=prod"]}]'`按 `key=value` 精确匹配标签
更新标签`agr tool update <tool-id> --tags '[{"Key":"env","Value":"prod"}]'`传入更新后的目标标签数组
清空全部标签`agr tool update <tool-id> --tags '[]'`将标签数组设为空

**注意：**

`agr tool update --tags` 表示更新后的目标状态，不是增量追加。旧标签如果没有出现在新请求中，更新后会被删除。

## 创建 Tool 时设置标签

创建 Tool 时，在 `--tags` 中传入标签数组：

agr tool create \

 --tool-name code-prod \

 --tool-type code-interpreter \

 --network-configuration '{"NetworkMode":"SANDBOX"}' \

 --tags '[{"Key":"env","Value":"prod"},{"Key":"team","Value":"search"}]' \

 -o json \

 --non-interactive

创建成功后，记录返回的 `ToolId`，用于后续查询、更新和回滚。

### 验证

agr tool list --tool-ids <tool-id> --limit 1 -o json --non-interactive

确认返回结果中的 `Tags` 字段包含刚写入的标签。如果同一个账号下存在多个同名 Tool，优先按 `ToolId` 核对结果。

## 按标签筛选 Tool

按 `key=value` 精确匹配标签时，使用 `--filters` 传入过滤条件：

agr tool list \

 --filters '[{"Name":"Tag","Values":["env=prod"]}]' \

 --limit 20 \

 -o json \

 --non-interactive

### 验证

确认目标 Tool 出现在返回结果中，并检查其 `Tags` 字段是否包含 `env=prod`。如果结果较多，可结合 `--tool-ids` 或分页参数缩小范围。

### 对系统影响

该操作为只读查询，不会创建、修改或删除任何资源，也不改变 Tool 的标签、状态或配置。

## 更新 Sandbox Tool 标签

修改已有标签时，在 `--tags` 中传入更新后的目标标签数组：

agr tool update <tool-id> \

 --tags '[{"Key":"env","Value":"prod"},{"Key":"team","Value":"agent-platform"},{"Key":"owner","Value":"search"}]' \

 -o json \

 --non-interactive

### 验证

agr tool list --tool-ids <tool-id> --limit 1 -o json --non-interactive

确认返回结果中的 `Tags` 字段已经反映更新后的标签集合。

## 清空全部标签

如需移除当前 Tool 的全部标签，可将 `--tags` 设为空数组：

agr tool update <tool-id> --tags '[]' -o json --non-interactive

### 验证

agr tool list --tool-ids <tool-id> --limit 1 -o json --non-interactive

确认返回结果中的 `Tags` 字段为空数组。

## 程序化调用

本文以 `agr` CLI 为主。如果需要在应用或流水线中直接更新标签，请参见 更新沙箱工具 API。该页面提供 `UpdateSandboxTool` 的请求字段、返回结构，以及 SDK 和 API Explorer 入口。

## 回滚

如果更新后的标签不符合预期，可再次执行 `agr tool update`，传入修正后的目标标签数组：

agr tool update <tool-id> \

 --tags '[{"Key":"env","Value":"prod"},{"Key":"team","Value":"search"}]' \

 -o json \

 --non-interactive

如需恢复到无标签状态：

agr tool update <tool-id> --tags '[]' -o json --non-interactive

## 相关文档

[创建沙箱工具](https://cloud.tencent.com/document/product/1814/132210)

[查询沙箱工具](https://cloud.tencent.com/document/product/1814/132214)

[更新与删除](https://cloud.tencent.com/document/product/1814/132213)
