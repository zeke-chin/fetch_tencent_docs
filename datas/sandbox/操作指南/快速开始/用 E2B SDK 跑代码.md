<!-- source: https://cloud.tencent.com/document/product/1814/132253 -->
<!-- fetcher: jina -->

# 用 E2B SDK 跑代码

最近更新时间：2026-06-03 09:09:00


## 操作流程

操作步骤 说明
准备工作 准备 Python 环境、AGS API Key、endpoint 域名，以及可用的模板 ID 或模板别名。
步骤一：安装 SDK 并配置环境变量 安装 `e2b-code-interpreter`，配置 `E2B_API_KEY` 和 `E2B_DOMAIN`。
步骤二：创建 Sandbox 并执行代码 用最少 3 行 Python 创建 Sandbox、执行代码并打印结果。
步骤三：在 Sandbox 内安装依赖并再次执行 使用 `pip install` 安装依赖，再执行 Python 代码验证结果。
步骤四：关闭 Sandbox 调用 `kill()` 释放当前 Sandbox。

## 准备工作

已获取 AGS 提供的 API Key。

已获取 AGS 提供的 E2B 兼容 endpoint 域名，例如 `ap-guangzhou.tencentags.com`。

当前 API Key 已具备创建和使用 Code Interpreter Sandbox 的权限。

本地已安装 Python 3.10 或更高版本，以及 `pip`。

已确认当前环境中可用的模板 ID 或模板别名。本文示例使用 `code-interpreter-v1`。

**注意：**

`E2B_DOMAIN` 填写 AGS 提供的 E2B 兼容 endpoint 域名即可，不要添加 `https://` 前缀。您可以直接复用 [安装与配置](https://cloud.tencent.com/document/product/1814/132205) 中的域名配置说明；如果控制台快速开始示例展示了 `E2B_DOMAIN`，复制其中域名部分即可，例如 `ap-guangzhou.tencentags.com`。

## 步骤一：安装 SDK 并配置环境变量

### 安装 Python SDK

python3 -m pip install e2b-code-interpreter

### 配置 API Key、endpoint 和模板

export E2B_API_KEY="e2b_your_api_key"

export E2B_DOMAIN="ap-guangzhou.tencentags.com"

export AGS_TEMPLATE="code-interpreter-v1"

**说明：**

示例中的 `ap-guangzhou.tencentags.com` 为公开域名格式示例，请替换为 AGS 为当前接入地域提供的 E2B 兼容服务域名。

相关配置说明如下：

环境变量 是否必填 说明
`E2B_API_KEY`是 AGS 提供的 API Key。
`E2B_DOMAIN`是 AGS 提供的 E2B 兼容 endpoint 域名，只填写域名部分。
`AGS_TEMPLATE`建议 本文示例使用的模板 ID 或模板别名，便于直接复用示例代码。

如果您不希望通过环境变量传参，也可以在创建 Sandbox 时显式传入 `api_key` 和 `domain`：

from e2b_code_interpreter import Sandbox

sandbox = Sandbox.create(

 template="code-interpreter-v1",

 api_key="e2b_your_api_key",

 domain="ap-guangzhou.tencentags.com",

)

sandbox.kill()

环境变量方式创建 Sandbox 时，`template="code-interpreter-v1"` 也可以替换为 `template=os.environ["AGS_TEMPLATE"]`，便于在不同环境中复用同一份脚本。

## 步骤二：创建 Sandbox 并执行代码

执行以下示例，使用 3 行 Python 完成创建 Sandbox、执行代码和打印结果：

from e2b_code_interpreter import Sandbox

sandbox = Sandbox.create(template="code-interpreter-v1")

print(sandbox.run_code("print('hello from AGS via E2B SDK')").text)

sandbox.kill()

如果您希望从环境变量中读取模板，也可以改为：

import os

from e2b_code_interpreter import Sandbox

sandbox = Sandbox.create(template=os.environ["AGS_TEMPLATE"])

print(sandbox.run_code("print('hello from AGS via E2B SDK')").text)

sandbox.kill()

运行成功后，终端中会看到类似输出：

hello from AGS via E2B SDK

## 步骤三：在 Sandbox 内安装依赖并再次执行

如果您需要在当前 Sandbox 中安装 Python 依赖，可以先执行 `pip install`，再运行代码验证依赖是否可用。

from e2b_code_interpreter import Sandbox

sandbox = Sandbox.create(template="code-interpreter-v1")

sandbox.commands.run("python -m pip install requests")

execution = sandbox.run_code("import requests\nprint(requests.__version__)")

print(execution.text)

sandbox.kill()

执行完成后，根据输出确认依赖已安装成功。例如输出 `2.32.3`，表示 `requests` 已可在当前 Sandbox 中使用。

**说明：**

通过 `pip install` 安装的依赖只在当前 Sandbox 生命周期内生效。关闭 Sandbox 后，如需再次使用，请重新创建 Sandbox 并重新安装依赖，或改用已预装依赖的模板。

## 步骤四：关闭 Sandbox

如果您在前面的示例中没有立即调用 `kill()`，请在操作完成后显式关闭当前 Sandbox：

sandbox.kill()

关闭后，当前 Sandbox 会被释放。建议在脚本结束前始终执行一次清理，避免产生不必要的资源占用。

## 后续操作

如果您需要长期复用相同依赖，可以使用预装依赖的模板或自定义模板，避免每次启动后重新安装。

如果您需要在 Sandbox 中操作文件、执行 Shell 命令或保持运行上下文，可通过 `sandbox.files`、`sandbox.commands` 和 `sandbox.run_code(...)` 继续扩展脚本。

如果您需要同时运行多个 Sandbox 或管理 Sandbox 生命周期，请参阅 Instance 生命周期相关文档。
