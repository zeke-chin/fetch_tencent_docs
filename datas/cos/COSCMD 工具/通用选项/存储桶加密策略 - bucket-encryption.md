<!-- source: https://cloud.tencent.com/document/product/436/123504 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:13:57+08:00 -->

# 存储桶加密策略 - bucket-encryption

最近更新时间：2026-03-12 17:34:22


## 命令格式

./coscli bucket-encryption --method [method] cos://<bucket-name>

bucket-encryption 命令包含以下参数：

参数格式 参数用途 示例
cos://<bucket-name>指定需要访问的存储桶。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag 使用桶别名访问：cos://example-alias

使用桶名称访问：cos://examplebucket-1250000000

bucket-encryption 命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法
无--method 指定需要进行的操作，包括 put（设置存储桶加密策略）、get（查询存储桶加密策略）、delete（删除存储桶加密策略）
无--sse-algorithm 加密算法（AES256, SM4, KMS）
无--kms-master-key-id KMS 主密钥 ID
无--kms-algorithm KMS 加密算法（AES256, SM4）

**说明：**

关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。

## 操作示例

### 设置存储桶加密策略

设置桶别名为 example-alias 的存储桶加密策略。命令如下：

./coscli bucket-encryption --method put cos://example-alias --sse-algorithm KMS

### 查询存储桶加密策略

查询桶别名为 example-alias 的加密策略信息。

./coscli bucket-encryption --method get cos://example-alias

输出以下结果。

 SECTION | KEY | VALUE

-------------+------------+---------------------------------------

 Encryption | Algorithm | KMS

+ +------------+--------------------------------------+

 | KMS Key ID | **********-****-****-****-**********

+ +------------+--------------------------------------+

 | Status | Enabled

-------------+------------+---------------------------------------

COS Bucket Encryption Configuration

Encryption Details:

 - Type: Server-Side Encryption with KMS-Managed Keys (SSE-KMS)

 - Description: Tencent Cloud Key Management System (KMS) manages encryption keys

 - KMS Key ID: **********-****-****-****-**********

 - Key Type: Customer Master Key (CMK)

### 删除存储桶加密策略

**注意：**

存储桶加密策略删除后将不再生效，如需使用需重新配置，请谨慎操作。

删除桶别名为 example-alias 的存储桶加密策略。命令如下：

./coscli bucket-encryption --method delete cos://example-alias
