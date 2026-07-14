<!-- source: https://cloud.tencent.com/document/product/436/111864 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:13:25+08:00 -->

# 查看对象内容 - cat

最近更新时间：2025-04-17 18:19:12


## 命令格式

./coscli cat cos://<bucket-name>/<key> [flag]

cat 命令包含以下参数：

参数格式 参数用途 示例
cos://<bucket-name>/<key>指定需要存储桶中的对象。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 endpoint flag 使用桶别名访问：cos://example-alias/test.txt

使用桶名称访问：cos://examplebucket-1250000000/test.txt

cat 命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法

## 操作示例

### 查看 bucket1桶内 test.txt 的内容

./coscli cat cos://bucket1/test.txt
