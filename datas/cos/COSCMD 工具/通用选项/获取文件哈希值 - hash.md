<!-- source: https://cloud.tencent.com/document/product/436/63672 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:12:54+08:00 -->

# 获取文件哈希值 - hash

最近更新时间：2025-04-02 19:21:32


## 命令格式

./coscli hash <object-name> [flag]

hash 命令包含以下参数：

参数格式 参数用途 示例
<object-name>用于指定访问的文件。可以为本地路径或 COS 文件路径。COS 路径支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0 "https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0") 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag 本地路径：~/example.txt

使用桶别名指定 COS 文件路径：cos://bucketalias/example.txt

使用桶名称指定 COS 文件路径：cos://examplebucket-1250000000/example.txt

hash 命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法
无--type 哈希类型（md5或 crc64，默认为 crc64）

注意：md5仅能获取 etag，如需获取文件 md5，可以下载完整文件后计算

**说明：**

关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763 "https://cloud.tencent.com/document/product/436/71763") 文档。

## 操作示例

### 计算本地文件的 crc64

./coscli hash ~/test.txt

### 获取 COS 文件的 md5

./coscli hash cos://bucket1/example.txt --type=md5
