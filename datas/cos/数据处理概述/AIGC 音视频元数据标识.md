<!-- source: https://cloud.tencent.com/document/product/436/124898 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:36:37+08:00 -->

# AIGC 音视频元数据标识

最近更新时间：2025-11-11 18:11:12


## 功能简介

《人工智能生成合成内容标识办法》中规定，自2025年9月1日起，AI 生成的视频、音频需要附加元数据标识。为协助 AI 业务执行《标识办法》，数据万象推出了完全符合《标识办法》的 AIGC 元数据标识功能，让存储在 COS 中的 AIGC 视频、音频可以便捷的添加元数据标识。

**说明：**

音视频元数据标识是付费服务，将产生**转封装或转码费用**，具体的费用明细请参见 [媒体处理费用](https://cloud.tencent.com/document/product/460/58120)。

## 使用限制

视频格式限制：支持添加、查询 MP4、AVI、MKV、FLV、WebM、MOV 格式视频的 AIGC 元数据标识。

音频格式限制：支持添加、查询 MP3、FLAC、WAV、M4A 格式音频的 AIGC 元数据标识。

其他限制，请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620#Media-processing)。

## 适用场景

### AI 生成视频、音频业务

使用 AI 大模型生成视频或音频的业务，对生成的音视频需添加元数据标识。

### 内容传播场景

在传播音视频时，如果视频或音频是由 AI 生成的，需对其添加元数据标识。

## 前提条件

已开通 COS 服务、创建存储桶并上传文件到存储桶。具体操作请参见 [存储桶文件](https://cloud.tencent.com/document/product/460/46485)。

已开通数据万象服务并绑定存储桶。具体操作请参见 [存储桶绑定](https://cloud.tencent.com/document/product/460/46483)。

## 使用方式

数据万象提供如下方式添加 AIGC 音视频元数据标识：

云上数据处理：通过异步任务接口，对已存储在 COS 中的音视频，添加 AIGC 元数据标识，请参见 [音视频转封装接口](https://cloud.tencent.com/document/product/460/84789) 或 [音视频转码接口](https://cloud.tencent.com/document/product/460/84790)。

工作流自动处理：您可以通过控制台配置音视频处理工作流，0代码开发实现音视频上传时，自动添加 AIGC 元数据标识，请参见 [数据工作流](https://cloud.tencent.com/document/product/460/46488)。
