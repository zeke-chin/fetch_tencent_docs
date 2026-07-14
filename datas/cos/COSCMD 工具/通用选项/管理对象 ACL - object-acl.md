<!-- source: https://cloud.tencent.com/document/product/436/123453 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:13:45+08:00 -->

# 管理对象 ACL - object-acl

最近更新时间：2025-09-16 14:34:12


## 命令格式

./coscli object-acl --method [method] cos://<bucket-name>/object

object-acl 命令包含以下参数：

参数格式 参数用途 示例
cos://<bucket-name>指定需要访问的存储桶。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag 使用桶别名访问：cos://example-alias

使用桶名称访问：cos://examplebucket-1250000000

object-acl 命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法
无--method 指定需要进行的操作，包括 put（设置对象 ACL）、get（查询对象 ACL）
无--acl 设置文件的 ACL，例如 private，public-read
无--grant-read 赋予被授权者读取对象的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 id="100000000001",id="100000000002"。
无--grant-read-acp 赋予被授权者读取对象的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 id="100000000001",id="100000000002"。
无--grant-write-acp 赋予被授权者写入对象的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 id="100000000001",id="100000000002"。
无--grant-full-control 赋予被授权者操作对象的所有权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 id="100000000001",id="100000000002"。

**说明：**

关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。

## 操作示例

### 设置对象 ACL

赋予100000000013、100000000012读取桶别名为 example-alias下的 object 对象的权限。命令如下：

./coscli object-acl --method put cos://example-alias/object --grant-read="id=\"100000000013\",id=\"100000000012\""

### 查询对象 ACL

查询桶别名为 example-alias下的 object 对象的权限列表。

./coscli object-acl --method get cos://example-alias/object

输出以下结果。

 SECTION | KEY | VALUE

-----------+--------------+----------------------------------------------

 Owner | UIN |

+ +--------------+---------------------------------------------+

 | ID | qcs::cam::uin/1000000000:uin/1000000000

+ +--------------+ +

 | Display Name |

+----------+--------------+---------------------------------------------+

 | |

+----------+--------------+---------------------------------------------+

 Grant #1 | Permission | READ

+ +--------------+---------------------------------------------+

 | Grantee Type | CanonicalUser

+ +--------------+---------------------------------------------+

 | ID | qcs::cam::uin/100000000013:uin/100000000013

+ +--------------+ +

 | Display Name |

+----------+--------------+---------------------------------------------+

 | |

+----------+--------------+---------------------------------------------+

 Grant #2 | Permission | READ

+ +--------------+---------------------------------------------+

 | Grantee Type | CanonicalUser

+ +--------------+---------------------------------------------+

 | ID | qcs::cam::uin/100000000012:uin/100000000012

+ +--------------+ +

 | Display Name |

-----------+--------------+----------------------------------------------

Access Control List (ACL) Information

Summary:

 - Owner: qcs::cam::uin/1000000000:uin/1000000000 (UIN: )

 - Total Grants: 2

 - Permissions:

 - READ: 2 grants
