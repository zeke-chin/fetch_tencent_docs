<!-- source: https://cloud.tencent.com/document/product/1814/130978 -->
<!-- fetcher: jina -->

# All-In-One 沙箱操作

最近更新时间：2026-04-24 17:32:52


## 前提条件

在执行后续所有代码前，请先完成 [配置环境变量](https://cloud.tencent.com/document/product/1814/123847)。

使用 All-In-One 沙箱实例前，您需要：

1. 在 [Agent 沙箱服务控制台](https://console.cloud.tencent.com/ags/sandbox?rid=1) 创建对应名称的 All-In-One 沙箱工具（使用自定义镜像）。

2. 将创建的沙箱工具名称填入下列代码的 `template` 参数中。

## 简介

All-In-One 沙箱（`sandbox-all-in-one`）是一个多功能合并镜像，在单个实例中同时提供以下能力：

能力 访问端口/路径 说明
代码执行`49999`兼容 E2B 协议，支持 Python / JS 等多语言
远程浏览器`9000/novnc/`基于 VNC 的浏览器可视化界面
VSCode 编辑器`9000/vscode/`code-server Web IDE
WebShell 终端`9000/ttyd/`基于 ttyd 的网页终端
终端 & 文件系统操作`49983`文件系统与命令执行接口

## 常用预装内容

### Python 包

包 用途
`playwright`浏览器自动化（使用系统 Chromium）
`selenium`浏览器自动化（WebDriver 方式）
`pyautogui`GUI 自动化（鼠标/键盘模拟）
`pillow`图像处理与截图
`anthropic`Anthropic Claude SDK
`openai`OpenAI SDK
`langchain`LLM 应用框架

### Node.js 包

包 用途
`playwright`浏览器自动化
`puppeteer`浏览器自动化（使用系统 Chromium）
`@anthropic-ai/sdk`Anthropic Claude SDK
`openai`OpenAI SDK
`@anthropic-ai/claude-code`Claude Code CLI
`@openai/codex`OpenAI Codex CLI
`@google/gemini-cli`Gemini CLI

## All-In-One 沙箱操作

### 创建沙箱实例

from e2b import Sandbox

# 创建一个 All-In-One 沙箱，template 替换为控制台新建的沙箱工具名称

sandbox = Sandbox.create(template="all-in-one-v1", timeout=3600)

### 获取各服务访问地址

All-In-One 沙箱通过 Nginx（端口`:9000`）统一对外暴露 UI 类服务，使用 `get_host()` 拼接访问 URL：

from e2b import Sandbox

sandbox = Sandbox.create(template="all-in-one-v1", timeout=3600)

token = sandbox._envd_access_token

host = sandbox.get_host(9000)

# 服务导航首页

index_url = f"https://{host}/?access_token={token}"

# NoVNC 远程桌面（可视化查看浏览器界面）

novnc_url = (

 f"https://{host}/novnc/vnc_lite.html?access_token={token}&path=websockify%3Faccess_token%3D{token}"

)

# VSCode Server Web IDE

vscode_url = f"https://{host}/vscode-sw-boot.html?access_token={token}"

# WebShell 终端

ttyd_url = f"https://{host}/ttyd/?access_token={token}"

print("首页:", index_url)

print("NoVNC:", novnc_url)

print("VSCode:", vscode_url)

print("终端:", ttyd_url)

### 从控制台获取访问链接

1. 登录 [Agent 沙箱服务控制台](https://console.cloud.tencent.com/ags/sandbox/tool?rid=1)，在左侧导航中选择**环境工具**。

2. 选择**All-In-One 沙箱**，点击沙箱工具名称，进入沙箱工具详情页。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/c0073fdf2e07fbafb9323465a7046b0c.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/c0073fdf2e07fbafb9323465a7046b0c.png)

3. 在实例列表中找到您要访问的沙箱，选择右侧的**操作 > 预览**，获得预览链接。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/ea9c3a43083a951f2f2e77cb58f71d1f.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/ea9c3a43083a951f2f2e77cb58f71d1f.png)

### 代码执行

All-In-One 沙箱内置代码执行能力，使用方式与代码解释器沙箱完全一致，详情请参见 [代码运行](https://cloud.tencent.com/document/product/1814/123851)。

### 浏览器操作（Playwright）

All-In-One 沙箱内置 Chromium，可通过 CDP URL 使用 Playwright 操控，详情请参见 [浏览器操作](https://cloud.tencent.com/document/product/1814/123852)。

**注意：**

`cdp_url` 拼接方式与浏览器沙箱相同，只需将 `template` 替换为 All-In-One 沙箱工具名称即可。

### 终端命令执行

All-In-One 沙箱支持在沙箱内执行 Shell 命令，详情请参见 [终端命令](https://cloud.tencent.com/document/product/1814/123850)。

### 文件系统操作

All-In-One 沙箱支持向沙箱上传和下载文件，详情请参见 [文件系统](https://cloud.tencent.com/document/product/1814/123849)。

### 效果演示

**首页**（默认 VSCode）

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/e306f655747888459f33e61eb751fa96.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/e306f655747888459f33e61eb751fa96.png)

WebShell

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/b2bd96824bb16c739d376da63ab48e3b.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/b2bd96824bb16c739d376da63ab48e3b.png)

浏览器可视化界面

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/c82d0759985e6821a2f9e5066afcd755.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/c82d0759985e6821a2f9e5066afcd755.png)
