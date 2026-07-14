<!-- source: https://cloud.tencent.com/document/product/436/63668 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:12:37+08:00 -->

# 查询存储桶或文件列表 - ls

最近更新时间：2026-02-06 18:10:01


## 命令格式

./coscli ls [cos://<bucket-name>[/prefix/]] [flag]

ls 命令包含以下参数：

参数格式 参数用途 示例
cos://<bucket-name>可选参数。指定需要访问的存储桶。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag 使用桶别名访问：cos://example-alias

使用桶名称访问：cos://examplebucket-1250000000
/prefix/可选参数。指定某一文件夹/picture/

ls 命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法
无--include 包含特定模式的文件
无--exclude 排除特定模式的文件
-r--recursive 是否递归地遍历文件夹，并列出所有文件
无--limit 指定列出的最大数量（传`0`或不传则默认限制为10000个文件。当设置为`-1` 时，可拉取所有 COS 文件）
无--all-versions 列举对象的所有版本，仅当 bucket 开启版本控制后可用， 列出历史版本参数增加显示字段`VersionId`, `IsLatest`, `Delete Marker`

**说明：**

`--include` 和`--exclude`支持标准正则表达式的语法，您可以使用它来过滤出符合特定条件的文件。

使用 zsh 时，您可能需要在 pattern 串的两端加上双引号。

./coscli ls cos://bucket1 -r --include ".*\.mp4$"

关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。

## 操作示例

### 列出当前账号下所有存储桶

./coscli ls

返回的信息包括：桶名称，地域，创建时间，存储桶总数。示例如下：

 BUCKET NAME | REGION | CREATE DATE

--------------------------------+-----------------+-----------------------

 examplebucket-1250000000 | ap-nanjing | 2022-01-01T00:00:00Z

--------------------------------+-----------------+-----------------------

 TOTAL BUCKETS: | 2

 ------------------+-----------------------

### 列出文件

#### 列出 bucket1存储桶中的所有文件

./coscli ls cos://bucket1

返回的信息包括：对象键（对象在存储桶中的唯一标识），存储类型，最近更新时间，对象大小，对象总数。示例如下：

 KEY | TYPE | LAST MODIFIED | ETAG | SIZE | RESTORESTATUS

-------------+----------+---------------------------+------------------------------------+-----------------+----------------

 test.txt | STANDARD | 2024-06-05T15:03:37+08:00 | "a3bc6c9058109f8da48d41a5ab9abc7c" | 4.88 KB |

-------------+----------+---------------------------+------------------------------------+-----------------+----------------

 TOTAL OBJECTS: | 1

 ------------------+----------------

#### 列出 bucket1存储桶中 picture 文件夹下的所有文件和文件夹

./coscli ls cos://bucket1/picture/

普通列出仅返回查询路径所在层级的数据，不对子路径进行展开。示例如下：

 KEY | TYPE | LAST MODIFIED | ETAG | SIZE | RESTORESTATUS

-------------------------+----------+---------------------------+------------------------------------+-----------------+----------------

 picture/a4431470f55662 | STANDARD | 2024-06-05T15:03:58+08:00 | "ed0430c5f27e76605e0555c260478112" | 358.00 B |

 picture/e98c6cefa4abd6 | STANDARD | 2024-06-05T15:03:58+08:00 | "bd5a4bd7248e7dfdb796383bee60470b" | 53.00 B |

-------------------------+----------+---------------------------+------------------------------------+-----------------+----------------

 TOTAL OBJECTS: | 3

 ------------------+----------------

#### 递归列出 bucket1存储桶中 picture 文件夹下的所有文件

./coscli ls cos://bucket1/picture/ -r

如果查询路径所在层级有子路径，递归列出会对所有子路径进行扫描，返回查询路径层级下的所有文件。示例如下：

 KEY | TYPE | LAST MODIFIED | ETAG | SIZE | RESTORESTATUS

------------------------------+----------+---------------------------+------------------------------------+-----------------+----------------

 picture/subfolder | DIR | | | |

 picture/subfolder/pic2.png | STANDARD | 2024-06-05T15:03:58+08:00 | "bd5a4bd7248e7dfdb796383bee60470b" | 53.00 B |

------------------------------+----------+---------------------------+------------------------------------+-----------------+----------------

 TOTAL OBJECTS: | 3

 ------------------+----------------

#### 递归列出 bucket1存储桶中所有的 .mp4类型文件

./coscli ls cos://bucket1 -r --include ".*\.mp4$"

#### 递归列出 bucket1存储桶中的所有不是 .mp4类型的文件

./coscli ls cos://bucket1 -r --exclude ".*\.mp4$"

#### 递归列出 bucket1存储桶中 picture 文件夹下所有以 test 开头并且类型不是 .jpg 的文件

./coscli ls cos://bucket1/picture -r --include "^picture/test.*" --exclude ".*\.jpg$"

### 列出历史版本

#### 列出 bucket1存储桶中的所有历史版本

./coscli ls cos://bucket1/ -r --all-versions

如果查询路径所在层级有子路径，递归列出会对所有子路径进行扫描，返回查询路径层级下的所有文件的所有历史版本。示例如下：

 KEY | TYPE | VERSIONID | ISLATEST | DELETE MARKER | LAST MODIFIED | ETAG | SIZE

--------------------------------+----------+-----------------------------+----------+---------------+---------------------------+------------------------------------+----------

 cmd/cmd/abort.go | STANDARD | MTg0NDUwMDM1MjIxMDM3MDI1MDM | false | false | 2025-02-26T14:33:25+08:00 | "c9bfc40db6669e9a7aee03abcd8b66e8" | 1.89 KB

 cmd/cmd/abort_test.go | STANDARD | MTg0NDUwMDM1MjIxMDM3MjgxODI | false | false | 2025-02-26T14:33:25+08:00 | "52166b1c60e4089a4652546c0350d2c7" | 4.89 KB

 cmd/cmd/bucket_tagging.go | STANDARD | MTg0NDUwMDM1MjIxMDM3MjY3MDI | false | false | 2025-02-26T14:33:25+08:00 | "edad62e08bf65a5bff81304e2b40ac1a" | 3.82 KB

 cmd/cmd/bucket_versioning.go | STANDARD | MTg0NDUwMDM1MjIxMDM2MTkzMzU | false | false | 2025-02-26T14:33:25+08:00 | "50a6b0e2e218c437ccdabe2c762aaef1" | 1.86 KB

 cmd/cmd/buket_tagging_test.go | STANDARD | MTg0NDUwMDM1MjIxMDM2MTY4MDc | false | false | 2025-02-26T14:33:25+08:00 | "cd11257b22c9816df105da15f3ceb70f" | 8.23 KB

 cmd/cmd/abort.go | | MTg0NDUwMDM1MjIwNjcyNTcxMDA | true | true | 2025-02-26T14:34:02+08:00 | |

 cmd/cmd/abort_test.go | | MTg0NDUwMDM1MjIwNjcxNzE5NDY | true | true | 2025-02-26T14:34:02+08:00 | |

 cmd/cmd/bucket_tagging.go | | MTg0NDUwMDM1MjIwNjcyNjczNzI | true | true | 2025-02-26T14:34:02+08:00 | |

 cmd/cmd/bucket_versioning.go | | MTg0NDUwMDM1MjIwNjY3ODc4NzM | true | true | 2025-02-26T14:34:02+08:00 | |

 cmd/cmd/buket_tagging_test.go | | MTg0NDUwMDM1MjIwNjY3ODYyMDI | true | true | 2025-02-26T14:34:02+08:00 | |

--------------------------------+----------+-----------------------------+----------+---------------+---------------------------+------------------------------------+----------

 TOTAL OBJECTS: | 10

 -------------------------------------+----------
