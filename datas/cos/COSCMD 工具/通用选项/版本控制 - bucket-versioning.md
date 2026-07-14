<!-- source: https://cloud.tencent.com/document/product/436/116525 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:13:35+08:00 -->

# 版本控制 - bucket-versioning

最近更新时间：2025-07-28 18:03:12


## 命令格式

以下 bucket-versioning 命令用于开启与暂停版本控制：

./coscli bucket-versioning --method [method] cos://<bucket-name> versioning

bucket-versioning 及其子命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法
-c--method 可选值 put/get

put 可选值 Enabled/Suspended

## 操作示例

### 开启存储桶版本控制

./coscli bucket-versioning --method put cos://examplebucket Enabled

### 暂停存储桶版本控制

./coscli bucket-versioning --method put cos://examplebucket Suspended

### 查看桶版本控制状态

./coscli bucket-versioning --method get cos://examplebucket
