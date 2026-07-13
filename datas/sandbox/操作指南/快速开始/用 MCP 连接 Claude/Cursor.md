<!-- source: https://cloud.tencent.com/document/product/1814/132251 -->
<!-- fetcher: jina -->

# 用 MCP 连接 Claude/Cursor

最近更新时间：2026-06-03 09:09:00


## 前提条件

开始配置前，请确认以下条件已就绪：

可用的 AGS API Key。

客户端支持通过远程 HTTP MCP server 注册自定义工具（Cursor 或 Claude Desktop）。

一个已创建的 Sandbox Tool 名称；如不指定，默认使用 `code-interpreter-v1`。

已选择公开可用地域。示例使用 `ap-guangzhou`，您可替换为其他已开放地域。

**说明：**

`mcp.{region}.tencentags.com` 是 AGS 对外公开的 MCP 接入域名格式，不是用户自建或源码部署地址。

建议优先通过 `X-API-KEY` Header 传递 API Key。只有客户端不支持 Header 时，再使用 URL 查询参数 `api_key` 作为兼容方式。

## 步骤 1：确认接入参数和模式

远程 HTTP MCP 服务接入需要以下参数：

配置项 是否必填 说明
`url`是 MCP 服务地址，推荐格式为 `https://mcp.{region}.tencentags.com/code`。
`X-API-KEY`推荐 通过 Header 传递 API Key。
`api_key`按需 Header 不可用时的兼容写法。
`toolname`否 Sandbox Tool 名称，默认值为 `code-interpreter-v1`。
`mode`否 沙箱管理模式，支持 `auto` 和 `manual`，默认值为 `auto`。

两种模式的差异如下：

模式 适用场景 生命周期行为 可用 Tool
`auto`单会话内连续执行代码、命令和文件读写。首次调用时自动创建 Sandbox，同一会话复用，会话结束后自动清理。`run_code`、`run_command`、`write_file`、`read_file`、`get_sandbox`、`set_sandbox_timeout`
`manual`需要显式控制 Sandbox 创建、复用和删除。不自动创建 Sandbox，由您显式创建、使用和删除。在 `auto` 的基础上额外增加 `create_sandbox` 和 `delete_sandbox`；执行类 Tool 要求传入 `sandbox_id`。

如果是首次接入，建议从 `auto` 模式开始；当任务需要显式复用同一 Instance 状态时，再切换到 `manual` 模式。

## 步骤 2：配置 Cursor

Cursor 通过 `mcp.json` 注册远程 HTTP MCP 服务。常见配置文件位置如下：

项目级：`.cursor/mcp.json`

用户级：`~/.cursor/mcp.json`

在配置文件中添加以下内容（以 `auto` 模式为例）：

{

 "mcpServers": {

 "ags-code-mcp": {

 "url": "https://mcp.ap-guangzhou.tencentags.com/code?toolname=code-interpreter-v1&mode=auto",

 "headers": {

 "X-API-KEY": "${AGS_API_KEY}"

 }

 }

 }

}

字段说明：

`url`：MCP 服务地址，包含 `toolname` 和 `mode` 参数。

`headers.X-API-KEY`：您的 AGS API Key。

如果需要切换地域，把 `ap-guangzhou` 替换为对应地域标识；如果需要显式控制生命周期，把 `mode=auto` 改为 `mode=manual`。如果客户端不支持自定义 Header，可将 API Key 追加为 URL 查询参数 `api_key=<your-api-key>`。

## 步骤 3：配置 Claude Desktop

Claude Desktop 同样可以接入该远程 HTTP MCP 服务。在 MCP 配置界面中填写以下信息：

**MCP 服务地址**：`https://mcp.ap-guangzhou.tencentags.com/code?toolname=code-interpreter-v1&mode=auto`

**鉴权 Header**：`X-API-KEY: <your-api-key>`

如果需要切换地域，把 `ap-guangzhou` 替换为对应地域标识；如果需要显式控制生命周期，把 `mode=auto` 改为 `mode=manual`。保存配置后，重新加载 MCP 设置，使客户端重新发现可用 Tool。

**说明：**

Claude Desktop 的界面字段名称可能随版本变化，但核心接入信息保持不变：同一个 MCP 服务地址、同一组鉴权 Header，以及相同的 `toolname` / `mode` 参数。

## 步骤 4：验证连接

完成配置后，先确认客户端已发现正确的 Tool 集合：

`auto` 模式应发现 6 个 Tool：`run_code`、`run_command`、`write_file`、`read_file`、`get_sandbox`、`set_sandbox_timeout`

`manual` 模式应发现 8 个 Tool：在 `auto` 的 6 个基础上增加 `create_sandbox` 和 `delete_sandbox`

建议按以下顺序验证功能：

1. **运行一段最小 Python 代码**：

运行 Python 代码 print("hello from ags")，并返回 stdout。

预期结果：客户端返回 `"hello from ags"`。

2. **执行一个简单命令**：

在 Sandbox 里执行命令 pwd，并返回 stdout。

预期结果：客户端返回当前工作目录路径。

3. **验证文件写入和读取**：

把 Hello, MCP 写入 /tmp/demo.txt，然后读回文件内容。

预期结果：客户端返回 `Hello, MCP`。

如果使用 `manual` 模式，请先调用 `create_sandbox` 获取 `sandbox_id`，再把同一个 `sandbox_id` 传给 `run_code`、`run_command`、`write_file`、`read_file` 和 `set_sandbox_timeout`。

**注意：**

如果客户端返回 `SESSION_NOT_FOUND`，说明当前会话已过期，或服务端已重建。请重新初始化 MCP 连接，然后再继续验证。

## 步骤 5：清理测试资源

验证完成后，建议及时清理测试资源：

`auto` 模式：结束当前测试会话，服务会按会话自动回收 Sandbox。

`manual` 模式：调用 `delete_sandbox` 删除当前 `sandbox_id` 对应的 Sandbox。

如果您为本次联调单独创建了测试 API Key，请按现有凭证管理流程停用或删除它。

## 结果验证

出现以下现象时，说明接入已成功：

Cursor 或 Claude Desktop 的 Tool 列表中，出现了与当前 `mode` 对应数量的 AGS Code MCP Tool。

`run_code`、`run_command` 和文件读写请求返回了实际执行结果，而不是"无法访问工具"之类的纯文本说明。

`manual` 模式下，客户端能先拿到 `sandbox_id`，再用同一个 `sandbox_id` 完成后续调用，且 `delete_sandbox` 能正常返回删除成功。

## 后续操作

需要延长会话空闲时间时，使用 `set_sandbox_timeout` 调整超时策略。

需要把 Sandbox 生命周期交给业务流程统一编排时，改用 `manual` 模式。
