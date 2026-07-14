<!-- source: https://cloud.tencent.com/document/product/436/63671 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:12:50+08:00 -->

# 删除文件 - rm

最近更新时间：2026-04-16 16:32:52


## 命令格式

./coscli rm cos://<bucket-name>[/prefix/] [flag]

rm 命令包含以下参数：

参数格式 参数用途 示例
cos://<bucket-name>指定需要访问的存储桶。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag。使用桶别名访问：cos://example-alias

使用桶名称访问：cos://examplebucket-1250000000
/prefix/可选参数。指定某一文件夹。/picture/

rm 命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法。
无--include 包含特定模式的文件。
无--exclude 排除特定模式的文件。
-r--recursive 是否递归地遍历文件夹下所有文件。
-f--force 强制删除（删除文件前不弹出确认信息）。
无--fail-output 此选项决定是否启用删除文件时的错误输出（默认为`true`，开启）。如果启用，文件删除失败将被记录在指定目录内（如果没有指定，默认为`./coscli_output`）。如果禁用，只会将删除错误文件的数量输出到控制台。
无--fail-output-path 此选项用于指定记录删除文件时的错误输出文件夹。通过提供自定义文件夹路径，您可以控制错误输出文件夹的位置和名称。如果未设置此选项，将使用默认的错误日志文件夹`./coscli_output`。
无--all-versions 仅支持在已开启版本控制的 Bucket 内且传入 --recursive（-r） 参数时可用，遍历删除指定路径下所有版本
无--version-id 仅支持在已开启版本控制的 Bucket 内且未传入--recursive（-r） 参数时可用，删除指定 object 的指定版本

**说明：**

`--include` 和`--exclude` 支持标准正则表达式的语法，您可以使用它来过滤出符合特定条件的文件。

使用 zsh 时，您可能需要在 pattern 字符串的两端加上双引号。

./coscli rm cos://bucket1/example/ -r --include ".*\\.mp4$"

关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。

## 操作示例

### 删除 fig1.png 文件

./coscli rm cos://bucket1/fig1.png

### 删除 picture 文件夹及包含的所有内容

./coscli rm cos://bucket1/picture/ -r

### 删除 fig1.png 文件的指定版本

./coscli rm cos://bucket1/fig1.png --version-id xxx

### 删除 test 前缀的所有版本

./coscli rm cos://bucket1/test -r --all-versions
