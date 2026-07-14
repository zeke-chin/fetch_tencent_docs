<!-- source: https://cloud.tencent.com/document/product/436/123505 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:14:09+08:00 -->

# 清单 - inventory

最近更新时间：2026-03-12 17:34:22


## 命令格式

./coscli inventory --method [method] cos://<bucket-name>

inventory 命令包含以下参数：

参数格式 参数用途 示例
cos://<bucket-name>指定需要访问的存储桶。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag 使用桶别名访问：cos://example-alias

使用桶名称访问：cos://examplebucket-1250000000

inventory 命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法
无--method 指定需要进行的操作，包括 put（设置存储桶清单）、get（查询存储桶清单）、delete（删除存储桶清单）、list（列出存储桶清单）、post（发起一次性清单）
无--task-id 清单任务 ID
无--configuration 清单配置（支持 JSON 格式、XML 格式或直接指定文件路径，例如 /data/configuration.txt 需要指定为`file:///data/configuration.txt`）

**说明：**

关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。

## 操作示例

### 设置存储桶清单

设置桶别名为 example-alias 的清单。命令如下（具体格式可参考 [设置存储桶清单](https://cloud.tencent.com/document/product/436/33707)）：

./coscli inventory --method put cos://example-alias --task-id list4 --configuration "<InventoryConfiguration>...</InventoryConfiguration>"

### 查询存储桶清单

查询桶别名为 example-alias 的 list4清单任务。

./coscli inventory --method get cos://example-alias --task-id list4

输出以下结果。

 SECTION | KEY | VALUE

------------------+-------------------+------------------------------------------------

 Basic | ID | list4

+ +-------------------+-----------------------------------------------+

 | Enabled | false

+ +-------------------+-----------------------------------------------+

 | Included Versions | All

+-----------------+-------------------+-----------------------------------------------+

 | |

+-----------------+-------------------+-----------------------------------------------+

 Schedule | Frequency | Weekly

+-----------------+-------------------+-----------------------------------------------+

 | |

+-----------------+-------------------+-----------------------------------------------+

 Destination | Bucket | qcs::cos:ap-nanjing::test-125000000

+ +-------------------+-----------------------------------------------+

 | Format | CSV

+ +-------------------+-----------------------------------------------+

 | Account ID | 100000000

+ +-------------------+-----------------------------------------------+

 | Prefix | list4

+-----------------+-------------------+-----------------------------------------------+

 | |

+-----------------+-------------------+-----------------------------------------------+

 Filter | Prefix | myPrefix

+ +-------------------+-----------------------------------------------+

 | Tag | age=18

+ +-------------------+-----------------------------------------------+

 | Period | 2026-01-18 to 2019-09-17

+-----------------+-------------------+-----------------------------------------------+

 | |

+-----------------+-------------------+-----------------------------------------------+

 Optional Fields | Field | Size

+ + +-----------------------------------------------+

 | | ETag

+ + +-----------------------------------------------+

 | | StorageClass

+ + +-----------------------------------------------+

 | | IsMultipartUploaded

+ + +-----------------------------------------------+

 | | Tag

+ + +-----------------------------------------------+

 | | LastModifiedDate

------------------+-------------------+------------------------------------------------

Inventory Configuration Details

### 删除存储桶清单

**注意：**

清单删除后无法恢复，请谨慎操作。

删除桶别名为 example-alias 的 list4清单任务。命令如下：

./coscli inventory --method delete cos://example-alias --task-id list4

### 列出所有存储桶清单

列出桶别名为 example-alias 的所有清单任务。

./coscli inventory --method list cos://example-alias

输出以下结果。

 ID | STATUS | SCHEDULE | INCLUDEDOBJECTVERSIONS | DESTINATION | FILTER | FIELDS

--------+----------+-------------------+------------------------+-------------------------------------------------------+----------------------------------+----------------------

 list1 | Enabled | Frequency: Daily | All | Bucket: qcs::cos:ap-nanjing::test-125000000 | Period: 2019-09-17 to 2019-09-17 | Size

 | | | | Format: CSV | | ETag

 | | | | Account: 1000000000 | | StorageClass

 | | | | Prefix: list1 | | IsMultipartUploaded

 | | | | | | ReplicationStatus

 | | | | | | LastModifiedDate

--------+----------+-------------------+------------------------+-------------------------------------------------------+----------------------------------+----------------------

 list3 | Disabled | Frequency: Weekly | All | Bucket: qcs::cos:ap-nanjing::test-125000000 | Period: 2026-01-18 to 2019-09-17 | Size

 | | | | Format: CSV | | ETag

 | | | | Account: 1000000000 | | StorageClass

 | | | | Prefix: list3 | | IsMultipartUploaded

 | | | | | | ReplicationStatus

 | | | | | | LastModifiedDate

--------+----------+-------------------+------------------------+-------------------------------------------------------+----------------------------------+----------------------

 list4 | Disabled | Frequency: Weekly | All | Bucket: qcs::cos:ap-nanjing::test-125000000 | Prefix: myPrefix | Size

 | | | | Format: CSV | Tags: age=18 | ETag

 | | | | Account: 1000000000 | Period: 2026-01-18 to 2019-09-17 | StorageClass

 | | | | Prefix: list4 | | IsMultipartUploaded

 | | | | | | Tag

 | | | | | | LastModifiedDate

--------+----------+-------------------+------------------------+-------------------------------------------------------+----------------------------------+----------------------

Detailed COS Bucket Inventory Configurations

Total inventory configurations: 3

### 发起一次性清单

为桶别名为 example-alias 发起一次性清单任务。命令如下（具体格式可参考 [发起一次性清单任务](https://cloud.tencent.com/document/product/436/83382)）：

./coscli inventory --method post cos://example-alias --task-id list4 --configuration "<InventoryConfiguration>...</InventoryConfiguration>"
