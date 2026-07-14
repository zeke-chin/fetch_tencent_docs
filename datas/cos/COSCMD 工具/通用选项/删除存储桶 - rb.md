<!-- source: https://cloud.tencent.com/document/product/436/63667 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:12:31+08:00 -->

# 删除存储桶 - rb

最近更新时间：2026-03-12 17:34:22


## 命令格式

./coscli rb cos://<bucket-name> [flag]

rb 命令包含以下参数：

参数格式 参数用途 示例
cos://<bucket-name>指定需要访问的存储桶。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag。使用桶别名访问：cos://example-alias

使用桶名称访问：cos://examplebucket-1250000000

rb 命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法
-r--region 存储桶地域

**说明：**

rb 命令仅可删除空存储桶，如果您的桶中还有文件请使用 [删除文件](https://cloud.tencent.com/document/product/436/63671) 命令和 [清理碎片](https://cloud.tencent.com/document/product/436/63674) 命令分别清空存储桶中的文件和文件碎片后再删除存储桶。

使用 rb 命令成功删除存储桶后，推荐您在配置文件中删除该桶的信息。具体命令用法，可参见下方操作示例。

关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。

## 操作示例

### 删除存储桶 bucket3（需要确认操作）

./coscli rb cos://bucket3-1250000000 -e cos.ap-chengdu.myqcloud.com

### 删除配置文件中的 bucket3 的存储桶配置

./coscli config delete -a bucket3
