<!-- source: https://cloud.tencent.com/document/product/436/63143 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:12:12+08:00 -->

# COSCLI 简介

最近更新时间：2025-09-22 11:45:52


COSCLI 是腾讯云对象存储（Cloud Object Storage，COS）提供的客户端命令行工具。通过 COSCLI 工具，您可以通过简单的命令行指令对您 COS 中的对象（Object）实现批量上传、下载、删除等操作。

COSCLI 使用 Go 编写，基于 Cobra 框架，支持配置多个存储桶和跨桶操作。您可以通过 `./coscli [command] --help` 来查看 COSCLI 的使用方法。

## 功能列表

[生成与修改配置文件 - config](https://cloud.tencent.com/document/product/436/63679)

[创建存储桶 - mb](https://cloud.tencent.com/document/product/436/63145)

[删除存储桶 - rb](https://cloud.tencent.com/document/product/436/63667)

[存储桶标签 - bucket-tagging](https://cloud.tencent.com/document/product/436/71764)

[查询存储桶或文件列表 - ls](https://cloud.tencent.com/document/product/436/63668)

[获取不同类型文件的统计信息 - du](https://cloud.tencent.com/document/product/436/63146)

[上传下载或拷贝文件 - cp](https://cloud.tencent.com/document/product/436/63669)

[同步上传下载或拷贝文件 - sync](https://cloud.tencent.com/document/product/436/63670)

[删除文件 - rm](https://cloud.tencent.com/document/product/436/63671)

[获取文件哈希值 - hash](https://cloud.tencent.com/document/product/436/63672)

[列出分块上传中产生的碎片 - lsparts](https://cloud.tencent.com/document/product/436/63673)

[清理碎片 - abort](https://cloud.tencent.com/document/product/436/63674)

[取回归档文件 - restore](https://cloud.tencent.com/document/product/436/63675)

[获取预签名 URL - signurl](https://cloud.tencent.com/document/product/436/63676)

[创建/获取软链接 - symlink](https://cloud.tencent.com/document/product/436/111863)

[查看对象内容 - cat](https://cloud.tencent.com/document/product/436/111864)

[列出目录下内容并统计 - lsdu](https://cloud.tencent.com/document/product/436/111865)

[版本控制 - bucket-versioning](https://cloud.tencent.com/document/product/436/116525)

[对象标签 - object-tagging](https://cloud.tencent.com/document/product/436/123441)

[管理对象 ACL - object-acl](https://cloud.tencent.com/document/product/436/123453)

[管理存储桶 ACL - bucket-acl](https://cloud.tencent.com/document/product/436/123442)

[存储桶策略 - bucket-policy](https://cloud.tencent.com/document/product/436/123503)

[存储桶加密策略 - bucket-encryption](https://cloud.tencent.com/document/product/436/123504)

[清单 - inventory](https://cloud.tencent.com/document/product/436/123505)

## 下载地址

COSCLI 工具支持 Windows、macOS、Linux 操作系统，详情请参见 [下载与安装配置](https://cloud.tencent.com/document/product/436/63144)。
