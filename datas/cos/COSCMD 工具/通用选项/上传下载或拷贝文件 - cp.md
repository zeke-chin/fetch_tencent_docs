<!-- source: https://cloud.tencent.com/document/product/436/63669 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:12:45+08:00 -->

# 上传下载或拷贝文件 - cp

最近更新时间：2026-05-27 17:52:34


## 命令格式

./coscli cp <source_path> <destination_path> [flags]

cp 命令包含以下参数：

参数格式 参数用途 示例
source_path 源文件路径。可以为本地路径或 COS 文件路径。COS 路径支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag 本地路径：~/example.txt

使用桶别名指定 COS 文件路径：cos://bucketalias/example.txt

使用桶名称指定 COS 文件路径：cos://examplebucket-1250000000/example.txt
destination_path 目的文件路径。可以为本地路径或 COS 文件路径。COS 路径支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag 本地路径：~/example.txt

使用桶别名指定 COS 文件路径：cos://bucketalias/example.txt

使用桶名称指定 COS 文件路径：cos://examplebucket-1250000000/example.txt

cp 命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
无--include 包含特定模式的文件（v1.0.4之前的版本在上传时仅筛选传入路径下的本地文件路径，v1.0.4以及之后版本会筛选传入的全路径）

例如：需要上传./test 下的所有文件到 COS，./test 下包含 aaa 文件夹，aaa 文件夹下包含1.txt 文件

1.0.4之前的版本会匹配 aaa/1.txt

1.0.4及之后版本会匹配 ./test/aaa/1.txt
无--exclude 排除特定模式的文件（v1.0.4之前的版本在上传时仅筛选传入路径下的本地文件路径，v1.0.4以及之后版本会筛选传入的全路径）

例如：需要上传./test 下的所有文件到 COS，./test 下包含 aaa 文件夹，aaa 文件夹下包含1.txt 文件

1.0.4之前的版本会匹配 aaa/1.txt

1.0.4及之后版本会匹配 ./test/aaa/1.txt
-r--recursive 是否递归遍历文件夹下所有文件
无--storage-class 指定上传文件的存储类型（默认 STANDARD），更多存储类型，请参见 [存储类型概述](https://cloud.tencent.com/document/product/436/33417)
无--part-size 文件的分块大小，单位为MB，默认值为32，最大支持5120。如果需要根据文件大小自适应分块大小，请设置为0
无--thread-num 文件分块并发线程数（默认并发5）
无--rate-limiting 单链接速率限制（0.1~100MB/s），单位MB/s
无--meta 上传文件的元信息。包括部分 HTTP 标准属性（HTTP Header）以及以 `x-cos-meta-` 开头的用户自定义元数据（User Meta）。文件元信息格式为 `header:value#header:value`，示例为 `Expires:2022-10-12T00:00:00.000Z#Cache-Control:no-cache#Content-Encoding:gzip#x-cos-meta-x:x`
无--routines 指定文件间并发上传或下载的线程数量，默认为`3`
无--fail-output 此选项决定是否启用上传或下载失败时文件的错误输出（默认为`true`，开启）。如果启用，文件传输失败将被记录在指定目录内（如果没有指定，默认为`./coscli_output`）。如果禁用，只会将错误文件的数量输出到控制台
无--fail-output-path 此选项用于指定记录上传或下载失败文件的错误输出文件夹。通过提供自定义文件夹路径，您可以控制错误输出文件夹的位置和名称。如果未设置此选项，将使用默认的错误日志文件夹`./coscli_output`
无--retry-num 限频重试次数（默认为`0`，不重试）。可选`1-10`次。当多台机器同时在同一个 COS 目录上执行下载操作时，可以通过指定此参数进行重试来规避限频错误
无--err-retry-num 错误重试次数（默认为`5`）。指定`1-10`次，或者设置为`0`表示不进行重试
无--err-retry-interval 重试间隔（仅在指定`--err-retry-num`为`1-10`时可用）。指定`1-10`秒的重试间隔，如果不指定或设置为`0`，每次重试间隔将在`1-10`秒内的随机值
无--only-current-dir 是否仅上传当前目录中的文件，忽略子目录及其内容（默认为 `false`，不忽略）
无--disable-all-symlink 是否上传时忽略所有软链接子文件和软链接子目录（默认为 `true`，不上传）。目前仅支持在 Linux 和 macOS 系统上使用
无--enable-symlink-dir 是否上传软链接的子目录（默认为 `false`，不上传）。目前仅支持在 Linux 和 macOS 系统上使用
无--disable-crc64 是否关闭 CRC64数据验证（默认为 `false`，启用验证）
无--disable-checksum 默认为 true ，仅校验分片 crc64。当设置为 false，将校验整个文件的 crc64。（coscli V1.0.6以及之前版本默认为 false）
无--move 会在文件成功拷贝到目标路径后，删除源文件（仅 cos 路径间可用）
无--version-id 下载指定版本的文件，仅支持在已开启版本控制的 Bucket 内使用（仅支持单文件）
无--process-log 是否开启进程日志，默认为 true，开启
无--process-log-path 此选项用于指定一个专用的输出文件夹来存储进程日志。日志将记录与文件上传或下载相关的信息，包括错误日志、正常执行日志、重试等详情。通过提供一个自定义的文件夹路径，您可以控制日志输出文件夹的位置和名称。如果未设置此选项，则将使用默认的日志文件夹（coscli_output）。
无--skip-dir 默认为 false，当设置为 true 时传输跳过文件夹。
无--acl 设置文件的 ACL，例如 private，public-read
无--grant-read 赋予被授权者读取对象的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 id="100000000001",id="100000000002"。
无--grant-read-acp 赋予被授权者读取对象的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 id="100000000001",id="100000000002"。
无--grant-write-acp 赋予被授权者写入对象的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 id="100000000001",id="100000000002"。
无--grant-full-control 赋予被授权者操作对象的所有权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 id="100000000001",id="100000000002"。
无--tags 对象的标签集合，最多可设置10个标签（例如，--tags="Key1=Value1&Key2=Value2"）
无--forbid-overwrite 针对未开启版本控制的存储桶，上传文件时，用于指定上传操作时是否禁止覆盖同名对象：

指定为 false 时，默认覆盖同名 Object。

指定为 true 时，表示禁止覆盖同名 Object。

当存储桶的版本控制是开启状态时，x-cos-forbid-overwrite 请求头部设置无效，即允许覆盖同名对象。
无--encryption-type 服务端加密方式（SSE-COS/SSE-C）。
无--server-side-encryption 服务端加密算法，支持 AES256、cos/kms。

使用 SSE-COS 或 SSE-KMS 时，此字段为必选项
无--sse-customer-algo 服务端加密算法，支持 AES256。

使用 SSE-C 时，此字段为必选项。
无--sse-customer-key 服务端加密密钥的 Base64编码。

例如 MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=。

使用 SSE-C 时，此字段为必选项。
无--sse-customer-key-md5 服务端加密密钥的 MD5哈希值，使用 Base64编码。

例如 U5L61r7jcwdNvT7frmUG8g==。

使用 SSE-C 时，此字段为必选项
无--check-point 是否开启断点续传，默认为 true，开启断点续传

**说明：**

使用命令时，请确保工具有访问本地路径的权限。

cp 命令在上传和下载大文件时会自动启用并发上传、下载。

当文件大于 `--part-size` 时，COSCLI 会先将文件按 `--part-size` 进行切块，之后用 `--thread-num` 个线程并发地执行上传、下载任务。

每个线程都会维护一个链接，对于每个链接，您可以使用 `--rate-limiting` 参数对单链接进行限速，当启用并发上传、下载时，总速率为 `--thread-num * --rate-limiting`。

当以分块形式上传/下载文件时，会默认开启断点续传。

`--include` 和 `--exclude` 支持标准正则表达式的语法，您可以使用它来过滤出符合特定条件的文件。

 默认不会上传软链接，如需上传软链接，设置 `--disable-all-symlink=false` 和`--enable-symlink-dir=true` 即可。**注意：如果软链接存在循环引用，可能导致工具进入死循环状态。**

使用 zsh 时，您可能需要在 pattern 串的两端加上双引号。

./coscli cp ~/test/ cos://bucket1/example/ -r --include ".*\.txt$" --meta=x-cos-meta-a:a#ContentType:text#Expires:2022-10-12T00:00:00.000Z

在 Windows cmd 中使用命令时，需注意“——”字符（中文破折号）粘贴进 cmd 会自动变为“--”，需手动输入一下。

关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。

## 操作示例

### 上传操作

#### 上传单文件

./coscli cp ~/example.txt cos://bucket1/example.txt

#### 将本地 test 文件夹下的所有文件及所有文件夹上传至 bucket1桶中的 example 文件夹下

./coscli cp ~/test/ cos://bucket1/example/ -r

#### 将本地 test 文件夹及其子文件夹下的所有 .mp4 类型文件上传至 bucket1桶中的 example 文件夹下

./coscli cp ~/test/ cos://bucket1/example/ -r --include ".*\.mp4$"

#### 将本地 test 文件夹及其子文件夹下的所有非 .md 类型文件上传至 bucket1桶中的 example 文件夹下

./coscli cp ~/test/ cos://bucket1/example/ -r --exclude ".*\.md$"

#### 将本地 test 文件夹及其子文件夹下的所有非 .md 和 非 .html 类型文件上传至 bucket1桶中的 example 文件夹下

./coscli cp ~/test/ cos://bucket1/example/ -r --exclude ".*\.html$|.*\.md$"

#### 本地 dir 文件夹下有 dirA、dirB、dirC、dirD 四个文件夹，将 dir 文件夹下除 dirD 文件夹之外的所有内容上传

./coscli cp dir/ cos://bucket1/example/ -r --exclude "dirD.*"

#### 将本地 test 文件夹下的所有文件及所有文件夹上传至 bucket1桶中的 example 文件夹下，并以归档类型文件存储

./coscli cp ~/test/ cos://bucket1/example/ -r --storage-class ARCHIVE

#### 将本地的 file.txt 文件上传至 bucket1桶并设置单链接速率限制为1.3MB/s

./coscli cp ~/file.txt cos://bucket1/file.txt --rate-limiting 1.3

### 下载操作

#### 下载单文件

./coscli cp cos://bucket1/example.txt ~/example.txt

#### 将 bucket1桶中的 example 文件夹下的所有文件及所有文件夹下载到本地 test 文件夹下

./coscli cp cos://bucket1/example/ ~/test/ -r

#### 将 bucket1桶中的 example 文件夹及其子文件夹下所有 .mp4类型文件下载至本地 test 文件夹下

./coscli cp cos://bucket1/example/ ~/test/ -r --include ".*\.mp4$"

#### 将 bucket1桶中的 example 文件夹及其子文件夹下所有非 .md 类型文件下载至本地 test 文件夹

./coscli cp cos://bucket1/example/ ~/test/ -r --exclude ".*\.md$"

#### 将 bucket1桶中的 example 文件夹及其子文件夹下所有非 .md 和 非 .html 类型文件下载至本地 test 文件夹

./coscli cp cos://bucket1/example/ ~/test/ -r --exclude ".*\.html$|.*\.md$"

#### 将 bucket1桶中的 example.txt 文件的 xxx 版本下载至本地 test 目录下

./coscli cp cos://bucket1/example.txt ~/test/ --version-id xxx

### 拷贝操作

#### 桶内拷贝单文件

./coscli cp cos://bucket1/example.txt cos://bucket1/example_copy.txt

#### 跨桶拷贝单文件

./coscli cp cos://bucket1/example.txt cos://bucket2/example_copy.txt

#### 将 bucket1桶中 example1文件夹下的所有文件及所有文件夹拷贝至 bucket2桶中 example2文件夹下

./coscli cp cos://bucket1/example1/ cos://bucket2/example2/ -r

#### 将 bucket1桶中 example1文件夹下及其子文件夹下的所有 .mp4类型文件拷贝至 bucket2桶中 example2文件夹下

./coscli cp cos://bucket1/example1/ cos://bucket2/example2/ -r --include ".*\.mp4$"

#### 将 bucket1桶中的 example1文件夹下及其子文件夹下所有非 .md 类型文件拷贝至 bucket2桶中 example2文件夹下

./coscli cp cos://bucket1/example1/ cos://bucket2/example2/ -r --exclude ".*\.md$"

#### 将 bucket1桶中的 example.txt 文件的 xxx 版本拷贝至 bucket2桶中

./coscli cp cos://bucket1/example.txt cos://bucket2/ --version-id xxx

#### 将 bucket1桶中的 test 文件夹移动至 bucket2桶中

./coscli cp cos://bucket1/test/ cos://bucket2/test/ --move -r
