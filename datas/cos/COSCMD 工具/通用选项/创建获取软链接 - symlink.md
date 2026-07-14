<!-- source: https://cloud.tencent.com/document/product/436/111863 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:13:16+08:00 -->

# 创建获取软链接 - symlink

最近更新时间：2025-12-31 18:07:41


## 命令格式

./coscli symlink --method create cos://<bucket-name>/<key> --link linkKey [flag]

symlink 命令包含以下参数：

参数格式 参数用途 示例
cos://<bucket-name>需要指定存储桶。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag 使用桶别名访问：cos://example-alias

使用桶名称访问：cos://examplebucket-1250000000
/<key>创建软链接时需指定对象名/test

symlink 命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法
无--method 可选值 create/get
无--link 软链接 key 值

## 操作示例

### 为 bucket1桶内的 picture.jpg 创建软链接 symlink

./coscli symlink --method create cos://bucket1/picture.jpg --link symlink

### 通过软链接 symlink 获取指向的对象

./coscli symlink --method get cos://bucket2 --link symlink
