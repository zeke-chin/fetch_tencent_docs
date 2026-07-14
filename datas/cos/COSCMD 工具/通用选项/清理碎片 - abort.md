<!-- source: https://cloud.tencent.com/document/product/436/63674 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:13:07+08:00 -->

# 清理碎片 - abort

最近更新时间：2026-04-16 16:32:52


## 命令格式

./coscli abort cos://<bucket-name>[/prefix/] [flag]

abort 命令包含以下参数：

参数格式 参数用途 示例
cos://<bucket-name>/<key>指定存储桶中的对象。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag 使用桶别名访问：cos://example-alias

使用桶名称访问：cos://examplebucket-1250000000
/prefix/可选参数。指定某一文件夹/picture/

abort 命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法
无--include 包含特定模式的文件
无--exclude 排除特定模式的文件
无--fail-output 此选项决定是否启用清理文件碎片时的错误输出（默认为`true`，开启）。如果启用，文件碎片清理失败将被记录在指定目录内（如果没有指定，默认为`./coscli_output`）。如果禁用，只会将清理失败的数量输出到控制台
无--fail-output-path 此选项用于指定记录清理文件碎片时的错误输出文件夹。通过提供自定义文件夹路径，您可以控制错误输出文件夹的位置和名称。如果未设置此选项，将使用默认的错误日志文件夹`./coscli_output`

**说明：**

关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。

## 操作示例

### 清除 bucket1桶内的所有文件碎片

./coscli abort cos://bucket1

### 清除 bucket1桶内 picture 文件夹下的所有碎片

./coscli abort cos://bucket1/picture/
