<!-- source: https://cloud.tencent.com/document/product/436/63673 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:12:59+08:00 -->

# 列出分块上传中产生的碎片 - lsparts

最近更新时间：2025-02-28 18:13:55


## 命令格式

./coscli lsparts cos://<bucket-name>[/prefix/] [flag]

lsparts 命令包含以下参数：

参数格式 参数用途 示例
cos://<bucket-name>指定需要访问的存储桶。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag。使用桶别名访问：cos://example-alias

使用桶名称访问：cos://examplebucket-1250000000
/prefix/可选参数。指定某一文件夹/picture/

lsparts 命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法
无--include 包含特定模式的文件
无--exclude 排除特定模式的文件
无--limit 指定列出的最大数量（0 - 1000）
无--upload-id 上传记录 id。当传入 uploadid 时，需指定具体文件，仅展示 uploadid 对应的文件碎片信息，未传入 uploadid 时，展示指定 prefix 下正在进行中的分块上传任务

**说明：**

关于分块上传的更多信息，请参见 [分块上传](https://cloud.tencent.com/document/product/436/14112)。

关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。

## 操作示例

### 列出 bucket1桶内的所有正在进行中的分块上传任务

./coscli lsparts cos://bucket1

返回的结果示例如下，输出的信息包括：对象键（对象在存储桶中的唯一标识）、分块上传的 ID、分块上传的起始时间、桶内碎片总数量。

 KEY | UPLOAD ID | INITIATE TIME

---------------+-------------------------------------+----------------------------

 test.txt | 1671191183635d2b71b1d68a0********** | 2022-01-01T00:00:00.000Z

---------------+-------------------------------------+----------------------------

 TOTAL: 1

 ----------------------------

### 列出 bucket1桶内 test.txt 文件 upload_id 为 1671191183635d2b71b1d68a0********** 的所有上传碎片

./coscli lsparts cos://bucket1/test.txt --upload-id="1671191183635d2b71b1d68a0**********"

返回的结果示例如下，输出的信息包括：PARTNUMBER（块的编号）、ETAG（块的 MD-5 算法校验值）、LastModified（分块最后被修改时间）、SIZE（分块大小）。

 PARTNUMBER | ETAG | LAST MODIFIED | SIZE

-------------+------------------------------------+---------------------------+------------

 1 | "58f06dd588d8ffb3beb46ada6309436b" | 2024-12-17T16:34:48+08:00 | 32.00 MB

 2 | "58f06dd588d8ffb3beb46ada6309436b" | 2024-12-17T16:34:48+08:00 | 32.00 MB

 3 | "58f06dd588d8ffb3beb46ada6309436b" | 2024-12-17T16:34:48+08:00 | 32.00 MB

 4 | "58f06dd588d8ffb3beb46ada6309436b" | 2024-12-17T16:34:48+08:00 | 32.00 MB

-------------+------------------------------------+---------------------------+------------

 TOTAL: 4

 -------------
