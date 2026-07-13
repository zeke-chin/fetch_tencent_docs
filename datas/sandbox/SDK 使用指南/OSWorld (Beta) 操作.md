<!-- source: https://cloud.tencent.com/document/product/1814/129382 -->
<!-- fetcher: jina -->

# OSWorld (Beta) 操作

最近更新时间：2026-05-18 16:14:11


## 简介

OSWorld 是一个面向多模态智能体（Multimodal Agents）的系统级评测基准数据集，旨在评估大模型在真实计算机环境中的开放式任务执行能力。

腾讯云 Agent Runtime 针对 OSWorld 评测场景特别推出了面向 OSWorld 评测场景的沙箱类型，为 OSWorld 评测提供以下优势特性：

1. 启动迅速：秒级创建评测环境，大幅缩短评测准备时间。

2. 高并发支持：可同时处理批量评测任务，提升评测效率。

3. 高度兼容性：完全兼容 OSWorld 任务定义，无需额外修改适配。

4. 资源隔离：确保每个评测任务独立运行，互不干扰。

5. 稳定可靠：提供持续稳定的评测环境，保障评测过程顺利进行。

该服务专为 OSWorld 评测场景优化设计，能够满足各类评测需求，帮助用户快速完成评测任务。

## **前提条件**

在开始操作前，请确保已完成以下准备工作：

1. 已开通腾讯云 Agent Runtime。

2. 已创建 OSWorld(Beta) 类型沙箱工具。

3. 已获取到以下信息，将填入到 .env 文件中。

4. 您的运行环境中有 uv、git 软件包。

# .env文件示例

# AGS (Agent Sandbox) Configuration

# 请从 Agent 沙箱服务获取APIKEY填写到此处

E2B_API_KEY=your_api_key_here

# 此处填写您创建 OSWorld 沙箱工具对应区域的地址

E2B_DOMAIN=ap-guangzhou.tencentags.com

# 此处填写您创建的 OSWorld 沙箱工具的名称

AGS_TEMPLATE=your_osworld_template_id

# 此处填写您想要 OSWorld 沙箱存活的时间

AGS_TIMEOUT=36000

# 如果您想真实运行评测，请填写以下内容

OPENAI_API_KEY=your_openai_api_key_here

OPENAI_BASE_URL=https://api.openai.com/v1

## 快速开始

# 克隆仓库

git clone https://github.com/TencentCloudAgentRuntime/ags-cookbook.git

cd ags-cookbook/examples/osworld-ags

# 克隆 OSWorld 原仓库

git clone https://github.com/xlang-ai/OSWorld.git osworld

cp -R overlay/OSWorld/. osworld/

# 复制并填写.env文件

cp .env.example osworld/.env

# 编辑 .env

# 安装依赖

make setup

# 快速启动

make run

## 详细使用

### 1. 获取示例代码

您需要先克隆腾讯云 [AGS Cookbook 仓库](https://github.com/TencentCloudAgentRuntime/ags-cookbook) 至本地。

git clone https://github.com/TencentCloudAgentRuntime/ags-cookbook.git

### 2. 进入示例目录

cd /path/to/ags-cookbook/examples/osworld-ags

### 3. 在示例目录中克隆 OSWorld 到 `./osworld`

# workdir:/path/to/ags-cookbook/examples/osworld-ags

git clone https://github.com/xlang-ai/OSWorld.git osworld

### 4. 应用 overlay

# workdir:/path/to/ags-cookbook/examples/osworld-ags

cp -R overlay/OSWorld/. osworld/

### 5. 配置环境变量

# workdir:/path/to/ags-cookbook/examples/osworld-ags

cp .env.example osworld/.env

填写 .env 文件。

# 请从腾讯云Agent沙箱服务产品控制台获取API KEY

E2B_API_KEY=your_ags_api_key_here

# 请根据您使用的region修改，如广州地域为ap-guangzhou.tencentags.com

E2B_DOMAIN=<region>.tencentags.com

# 请在腾讯云Agent沙箱服务产品控制台创建OSWorld类型沙箱工具，并将沙箱工具名称填写在这里

AGS_TEMPLATE=your_osworld_template_id

# 如果您想要真实运行OSWorld评测，请填写您的OpenAI密钥

OPENAI_API_KEY=your_openai_api_key_here

OPENAI_BASE_URL=https://api.openai.com/v1

### 6. 安装依赖

# workdir:/path/to/ags-cookbook/examples/osworld-ags

make setup

### 7. 快速运行

# workdir:/path/to/ags-cookbook/examples/osworld-ags

make run

### 8. 真实评测

# 注意，您需要在.env中填写 OpenAI 密钥来运行

cd osworld

uv run --python .venv/bin/python run_multienv.py --provider_name ags --model gpt-4 o --num_envs 2

## 更多信息

更多内容请参见 [TencentCloudAgentRuntime/ags-cookbook](https://github.com/TencentCloudAgentRuntime/ags-cookbook/blob/main/examples/osworld-ags/README_zh.md)。

## 沙箱运行 OSWorld 评测效果

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/29637b29f57f553976bf77f86c32fbcd.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/29637b29f57f553976bf77f86c32fbcd.png)

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/1c4517b0b1c1b46e208eaff528e26493.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/1c4517b0b1c1b46e208eaff528e26493.png)
