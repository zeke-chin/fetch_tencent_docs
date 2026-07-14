<!-- source: https://cloud.tencent.com/document/product/436/111865 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:13:27+08:00 -->

# 列出目录下内容并统计 - lsdu

最近更新时间：2025-04-17 18:19:12


## 命令格式

./coscli lsdu cos://<bucket-name>[/prefix/] [flags]

lsdu 命令包含以下参数：

参数格式 参数用途 示例
cos://<bucket-name>指定需要访问的存储桶。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag 使用桶别名访问：cos://example-alias

使用桶名称访问：cos://examplebucket-1250000000
/prefix/可选参数。指定某一文件夹/picture/

lsdu 命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法
无--include 包含特定模式的文件
无--exclude 排除特定模式的文件

## 操作示例

### 获取 bucket1桶根目录下的统计信息

./coscli lsdu cos://bucket1/

返回的信息包括：目录或 object 名，总计对象数量，总计大小。示例如下：

 NAME | OBJECTS COUNT | TOTAL SIZE

---------------------+---------------+-------------

 300123/ | 1 | 300.00 MB

 300s/ | 1 | 100.00 MB

 300u/ | 301 | 8.22 GB

 activity/ | 35 | 129.08 KB

 test/ | 1 | 3 B

 test100/ | 20 | 20.00 GB

 test5/ | 6 | 9.00 GB

 testrm/ | 1 | 0 B

 10GB_file | 1 | 11.72 GB

 1GB_file | 1 | 1.00 GB

### 获取 bucket1桶 picture 目录下的统计信息

./coscli lsdu cos://bucket1/picture/

**说明：**

文件较多时此命令耗时会较长，建议后台执行。
