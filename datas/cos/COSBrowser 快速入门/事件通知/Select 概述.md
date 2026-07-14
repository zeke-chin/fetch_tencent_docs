<!-- source: https://cloud.tencent.com/document/product/436/37635 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:02:37+08:00 -->

# Select 概述

最近更新时间：2026-03-26 10:52:02


## 使用限制

使用 COS Select 时存在以下限制：

您必须拥有所查询对象的 `cos:GetObject` 权限，主账号默认拥有该权限。

仅支持标准存储类型的对象检索。

SQL 表达式的最大长度为256KB。

检索结果中单条记录的最大长度为1MB。

COS Select 功能目前支持的 SQL 子句：

SELECT 语句

FROM 子句

WHERE 子句

LIMIT 子句

**说明：**

有关 SQL 子句的详细信息，请参见 [Select 命令](https://cloud.tencent.com/document/product/436/37636)。

COS Select 目前支持的函数如下：

聚合函数：例如 AVG 函数、COUNT 函数、MAX 函数、MIN 函数、SUM 函数。

条件函数：例如 COALESCE 函数、NULLIF 函数。

转换函数：例如 CAST 函数。

日期函数：例如 DATE_ADD 函数、DATE_DIFF 函数、EXTRACT 函数、TO_STRING 函数、TO_TIMESTAMP 函数、UTCNOW 函数。

字符串函数：例如 CHAR_LENGTH 函数、CHARACTER_LENGTH 函数、LOWER 函数、SUBSTRING 函数、TRIM 函数、UPPER 函数。

**说明：**

有关 SQL 函数的详细信息，请参见 [SQL 函数](https://cloud.tencent.com/document/product/436/37637)。

COS Select 目前支持以下运算符：

逻辑运算符：`AND，NOT，OR`

比较运算符：`<，>，<=，>=，=，<>，!=，BETWEEN，IN`

模式匹配运算符：`LIKE`

数学运算符：`+，-，*，%`

**说明：**

有关运算符的详细信息，您可以参见 [运算符](https://cloud.tencent.com/document/product/436/37640)。

## 发起检索请求

您可以使用控制台、API、SDK 等多种方式发起检索请求：

使用控制台，您可参见 [检索数据](https://cloud.tencent.com/document/product/436/37642) 文档进行操作。

使用 API，请参见 [SELECT Object Content](https://cloud.tencent.com/document/product/436/37641) API 文档。

使用 SDK，您可以前往 [SDK 概览](https://cloud.tencent.com/document/product/436/6474) 选择所需的 SDK 接口。

## 常见问题

如果在尝试执行查询时遇到问题，COS Select 将返回错误代码和关联的错误消息。有关错误代码和描述的列表，请参见 [特殊错误码](https://cloud.tencent.com/document/product/436/37641#errorcode)。
