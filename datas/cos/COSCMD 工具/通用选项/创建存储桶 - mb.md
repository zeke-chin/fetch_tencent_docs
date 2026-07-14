<!-- source: https://cloud.tencent.com/document/product/436/63145 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:12:30+08:00 -->

# 创建存储桶 - mb

最近更新时间：2025-09-15 16:11:22


## 命令格式

./coscli mb cos://<BucketName-APPID> -e <endpoint> [flag]

**注意：**

使用 mb 命令创建存储桶，需要携带全局 flag `-e` 或 `--endpoint` 指定存储桶所在地域。

mb 命令包含以下参数：

参数格式 参数用途 示例
cos://<BucketName-APPID>用于自定义存储桶名称 cos://examplebucket-1250000000

mb 命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法
-r--region 存储桶地域
-m--maz 创建多 az 的存储桶
-o--ofs 创建 ofs 的存储桶
无--acl 设置存储桶的 ACL，例如 private，public-read，public-read-write
无--grant-read 赋予被授权者读取存储桶的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 id="100000000001",id="100000000002"。
无--grant-read-acp 赋予被授权者读取存储桶的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 id="100000000001",id="100000000002"。
无--grant-write-acp 赋予被授权者写入存储桶的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 id="100000000001",id="100000000002"。
无--grant-full-control 赋予被授权者操作存储桶的所有权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 id="100000000001",id="100000000002"。
无--tags 存储桶标签集合，最多可设置50个标签（例如，--tags="Key1=Value1&Key2=Value2"）

**说明：**

使用 mb 命令成功创建存储桶后，推荐您在配置文件中新增该桶的信息，方便后续使用桶别名快速操作。具体命令用法，可参见下方操作示例。

关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。

## 操作示例：创建存储桶 bucket3-1250000000

./coscli mb cos://bucket3-1250000000 -e cos.ap-chengdu.myqcloud.com

如果您希望为刚创建的存储桶配置别名，需要使用以下命令更新配置文件：

./coscli config add -b bucket3-1250000000 -e cos.ap-chengdu.myqcloud.com -a bucket3

更新后可用 cos://bucket3 访问此存储桶。
