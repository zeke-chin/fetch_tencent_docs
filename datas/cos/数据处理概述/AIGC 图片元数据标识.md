<!-- source: https://cloud.tencent.com/document/product/436/124897 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:36:28+08:00 -->

# AIGC 图片元数据标识

最近更新时间：2025-11-11 18:11:12


## 功能简介

《人工智能生成合成内容标识办法》中规定，自2025年9月1日起，AI 生成的图片需要附加元数据标识。为协助 AI 业务执行《标识办法》，数据万象推出了完全符合《标识办法》的 AIGC 元数据标识功能，您可以对存储在 COS 中的 AIGC 图片便捷地**添加或查询元数据标识**。

**说明：**

图片元数据标识是付费服务，将产生**图片基础处理费用**，具体的费用明细及免费额度请参见 [图片处理费用](https://cloud.tencent.com/document/product/460/58117)。

## 使用限制

图片格式限制：JPG/JPEG、PNG、WebP、AVIF

图片体积限制：原图及添加元数据标识后的图片大小均不可超过32MB、宽高不可超过50000px且总像素不可超过2.5亿px。

## 适用场景

### 文生图、图生图业务

使用 AI 进行文字生成图片、图片生成图片的业务，对生成的图片需添加元数据标识。

### 内容传播场景

在传播图片时，需识别图片是否包含 AIGC 元数据，对于 AI 图片需要添加元数据标识。

## 前提条件

已开通 COS 服务、创建存储桶并上传文件到存储桶。具体操作请参见 [存储桶文件](https://cloud.tencent.com/document/product/460/46485)。

已开通数据万象服务并绑定存储桶。具体操作请参见 [存储桶绑定](https://cloud.tencent.com/document/product/460/46483)。

## 使用方式

数据万象提供如下方式添加和查询 AIGC 图片元数据标识：

上传图片时添加：通过 API 接口，在图片上传到 COS 时，同步添加 AIGC 元数据标识并存储，请参见 [添加 AIGC 图片元数据标识](https://cloud.tencent.com/document/product/460/122024)。

对 COS 中的图片进行添加：通过 API 接口，对已存储在 COS 中的图片，添加 AIGC 元数据标识，请参见 [添加 AIGC 图片元数据标识](https://cloud.tencent.com/document/product/460/122024)。

配置工作流自动添加：您可以通过控制台配置图片处理工作流，0代码开发实现图片上传时，自动添加 AIGC 元数据标识，请参见 [数据工作流](https://cloud.tencent.com/document/product/460/46488)。

查询 AIGC 元数据：通过 API 接口，对已存储在 COS 中的图片，查询 AIGC 元数据标识，请参见 [查询 AIGC 图片元数据标识](https://cloud.tencent.com/document/product/460/122025)。
