<!-- source: https://cloud.tencent.com/document/product/436/124911 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:36:52+08:00 -->

# AIGC 文档元数据标识

最近更新时间：2025-11-11 18:11:12


## 功能简介

《人工智能生成合成内容标识办法》中规定，自2025年9月1日起，AI 生成的文本文档需要附加元数据标识。为协助 AI 业务执行《标识办法》，数据万象推出了完全符合《标识办法》的 AIGC 元数据标识功能，您可以对存储在 COS 中的 AIGC 文档便捷地**添加或查询元数据标识**。

**说明：**

该功能为付费功能，详细计费说明请参见 [文档处理费用](https://cloud.tencent.com/document/product/460/58121)。

## 使用限制

格式限制：支持添加、查询 docx\pptx\xlsx\dotx\xltx\potx\pdf\xmind\md 格式文档的 AIGC 元数据标识。

大小限制：不超过50MB。

默认处理并发：10。

地域限制：支持中国大陆公有云地域。

## 适用场景

### AI 生成文档业务

使用 AI 大模型生成文档的业务，对生成的文档需添加元数据标识。

### 内容传播场景

在传播文档时，如果文档是由 AI 生成的，需对其添加元数据标识。

## 前提条件

已开通 COS 服务、创建存储桶并上传文件到存储桶。具体操作请参见 [存储桶文件](https://cloud.tencent.com/document/product/460/46485)。

已开通数据万象服务并绑定存储桶。具体操作请参见 [存储桶绑定](https://cloud.tencent.com/document/product/460/46483)。

## 使用方式

数据万象提供如下方式添加及查询 AIGC 文档元数据标识：

对 COS 上的文档进行元数据添加：通过异步任务接口，对已存储在 COS 中的文档，添加 AIGC 元数据标识，请参见 [添加 AIGC 文档元数据标识接口](https://cloud.tencent.com/document/product/460/123076)。

工作流自动处理：您可以通过控制台配置文档处理工作流，0代码开发实现文档上传时，自动添加 AIGC 元数据标识，请参见 [数据工作流](https://cloud.tencent.com/document/product/460/46488)。

对 COS 上的文档进行元数据查询：您可以对已存储在 COS 中的文档，查询 AIGC 元数据标识，请参见 [查询 AIGC 文档元数据标识](https://cloud.tencent.com/document/product/460/123077)。
