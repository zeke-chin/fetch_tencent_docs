<!-- source: https://cloud.tencent.com/document/product/1814/123812 -->
<!-- fetcher: jina -->

# Agent 沙箱应用场景

最近更新时间：2026-03-24 11:46:29


## Vibe Coding

在 Vibe Coding 场景中，本地 IDE Copilot 模式虽然便捷，但存在严重安全风险：AI 生成的代码直接运行在本地环境，一旦包含 `rm -rf` 等危险指令，可能造成数据不可逆损失。

因此，逐步转向云端模式，如 AI 编程、前端页面生成、云端 IDE 等。AI 生成的代码在**云端沙箱环境**中运行，与本地隔离，既能避免入侵风险，又具备更强的资源弹性与可扩展性。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/6b3a8e3f56a256173068dc2f50cb8dc0.gif)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/6b3a8e3f56a256173068dc2f50cb8dc0.gif)

## 数据处理、PPT 制作等

通用 Agent 或企业办公 Agent 可以通过代码生成的方式完成数据清洗、数据分析、图表制作、甚至 PPT 制作。所有代码均在**云端沙箱**中运行，与本地彻底隔离，既安全可信，又具备弹性算力，真正成为企业数字员工的办公工具，让办公自动化更高效、更安心。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/6fc07adf7790d2c486416eae582fb7e8.gif)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/6fc07adf7790d2c486416eae582fb7e8.gif)

## GUI Agent

在 GUI Agent 场景中，智能体成为具备全栈交互能力的虚拟人类。依托云端沙箱的安全隔离与弹性算力，它能够在不同环境中模拟人机操作：

Browser Use Agent：在浏览器沙箱中执行网页打开、元素点击、数据采集与自动下单。

Computer Use Agent：在虚拟桌面处理 Excel、生成 PPT、管理文件，实现办公自动化。

Mobile Use Agent：在虚拟手机中操控 App，支持自动化测试与高并发业务操作。

GUI Agent 有效解决企业存量系统改造困难的问题，从“代码/API 驱动”演进为“操作驱动”，在云沙箱的助力下，覆盖 Web、桌面和移动端场景，成为真正的 虚拟数字员工。

## 强化学习场景

在 GUI-Agent 强化学习场景中，Agent 如学徒般，通过反复尝试、反馈和优化逐步掌握复杂界面操作。云端沙箱是核心执行环境，提供：

安全隔离：操作严格限制在沙箱内，避免影响真实系统与账号。

可观测性：完整记录操作轨迹、状态转移与奖励信号，支持精细化训练分析。

弹性扩展：支持大规模并发创建沙箱实例，支持模型训练，满足高强度算力需求。

依托沙箱，GUI-Agent 能在安全、可控、可扩展的环境中持续进化，最终具备自主完成复杂办公与操作任务的能力，真正成长为 “数字员工”。
