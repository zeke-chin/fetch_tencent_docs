<!-- source: https://cloud.tencent.com/document/product/1814/123811 -->
<!-- fetcher: jina -->

# Agent 沙箱概述

最近更新时间：2026-06-16 17:02:30


## Agentic 时代来临，为什么必须为“数字员工”配备沙箱

在过去两年里，Agent 从实验室的探索逐渐走向生产环境，不再只是模型能力的展示，而是真实承担起企业中的“数字员工”角色。随着任务日益复杂，既要写代码、调用工具，又要操作浏览器、处理数据，对工作环境的要求也越来越高：

既要足够自由，支持多种场景的多样化任务操作。

又要足够安全，避免误删数据或越权操作。

还要具备弹性和并发能力，支撑大规模落地。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/62067834093d0593edba111e55268efd.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/62067834093d0593edba111e55268efd.png)

随着 Agent 从工具调用逐渐演进到真正的 Agentic Agent ——能自主规划、动态调用工具并与环境交互，对运行环境提出了更高标准。为了让这些数字员工安全、稳定地完成复杂任务，我们迫切需要一个数字世界的沙箱，为 Agent 提供专属办公环境。

正是基于这样的需求，Agent 沙箱应运而生。它为数字员工提供了一个安全隔离、极速启动的“虚拟办公环境”，让每个 Agent 都能像真实员工一样高效开展工作，同时解决了场景灵活、安全性与规模化并发三大核心挑战，成为 Agent 从研发走向生产的关键基座。

## 腾讯云 Agent 沙箱服务产品介绍

Agent 沙箱服务，支持毫秒级启动与数万实例并发，提供了 Code、Browser、Computer 等多种沙箱类型的托管服务，为 AI Agent 提供安全、隔离、高性能的执行环境。产品依托腾讯云强大的底层算力与调度能力，提供超大规模的弹性资源供给，保障 Agent 在生产环境的稳定可用。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/e7112fd966343825229bedcd5b633e14.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/e7112fd966343825229bedcd5b633e14.png)

### 产品功能

Agent 沙箱服务在功能上涵盖两个维度：一是在沙箱类型上，支持代码沙箱、浏览器沙箱等多种形态；二是在沙箱使用上，提供完整的沙箱生命周期管理与内部操作能力。同时，产品还支持多样化的接入方式——不仅提供工程师 / Agent友好的 SDK、CLI、MCP、RESTful API，还兼容社区开源沙箱协议，方便用户灵活集成。

#### 多种沙箱类型支持

Agent 沙箱服务支持多种主流沙箱类型，并提供高度灵活的定制能力，满足智能体在不同场景下的运行需求。

代码执行沙箱：支持 Python、JavaScript 等多种编程语言，适用于数据处理、科学计算、图表生成、Vibe Coding 等安全代码运行场景。

浏览器沙箱：提供安全隔离的浏览器交互与测试环境，有效降低对本地系统的潜在风险，适用于 Deep Research、通用 Agent 等浏览器操作场景。

电脑沙箱（即将上线）：提供完整的远程虚拟机操控能力，支持对 Windows、Linux 系统进行鼠标控制、键盘输入、实时截屏等操作。

自定义沙箱：支持根据业务需求为智能体量身定制执行环境，包括：

环境定制 ：自由选择操作系统、预装软件、依赖库和工具链。

资源配置 ：按需灵活配置 CPU、内存、存储资源，提升资源利用率。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/a2712432b7c24ecc5b00f4ea6c36a28f.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/a2712432b7c24ecc5b00f4ea6c36a28f.png)

#### 完善的沙箱操作能力

Agent 沙箱服务提供完整的沙箱操作能力，涵盖生命周期管理、内部文件操作以及细粒度的权限控制。

在沙箱的基础生命周期管理上，Agent 沙箱服务支持启动、超时删除、自动空闲回收和暂停等能力，不仅覆盖多样化业务场景，还能有效降低资源消耗，帮助用户实现更高效的使用体验。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/6e6e96bb9d60b49173ab942610b54551.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/6e6e96bb9d60b49173ab942610b54551.png)

在文件操作方面，沙箱支持目录和文件的创建、读取、编辑与搜索，为 Agent 提供完整的内部文件管理能力；同时支持外挂存储，对接外部对象存储，方便文件的上传、下载与共享。借此，Agent 可以在沙箱中直接处理数据或中间结果，并安全地与外部系统交互，大幅提升了业务场景下的灵活性和效率。

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/fbfa5b7cdc9598be63f09df4921f84db.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/fbfa5b7cdc9598be63f09df4921f84db.png)

在权限管理方面，沙箱提供细粒度的角色控制能力，可灵活配置沙箱对腾讯云资源的访问范围，为 Agent 赋予安全且精细化的操作权限，从而在保障安全的同时释放更强大的云上操作能力。

备注：上述产品性能数据统计时间2025年8月，来自腾讯实验室测试结果。
