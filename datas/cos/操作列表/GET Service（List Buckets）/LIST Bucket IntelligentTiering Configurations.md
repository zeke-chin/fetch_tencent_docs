<!-- source: https://cloud.tencent.com/document/product/436/106783 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:40:07+08:00 -->

# LIST Bucket IntelligentTiering Configurations

最近更新时间：2024-11-04 20:24:12


## 功能描述

List Bucket IntelligentTiering Configurations 用于请求返回一个存储桶中的所有智能分层配置，包括低频层规则（id 为 default）、归档及深度归档层规则（id 非 default）。每一个存储桶中最多配置1000条规则。

**注意：**

调用该请求时，请确保您有足够的权限对存储桶的智能分层配置进行操作。

存储桶所有者默认拥有该权限，如您无该项权限，请先向存储桶所有者申请该项操作的权限。

## 请求

#### 请求示例

GET /?intelligent-tiering HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Authorization: Auth String

**说明：**

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；<Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

<ListBucketIntelligentTieringConfigurationOutput>

 <IntelligentTieringConfiguration>

 <Id>default</Id>

 <Status>Enabled</Status>

 <Tiering>

 <AccessTier>INFREQUENT</AccessTier>

 <Days>30</Days>

 <RequestFrequent>1</RequestFrequent>

 </Tiering>

 </IntelligentTieringConfiguration>

 <IntelligentTieringConfiguration>

 <Id></Id>

 <Status></Status>

 <Filter>

 <And>

 <Prefix>string</Prefix>

 <Tag>

 <Key>string</Key>

 <Value>string</Value>

 </Tag>

 <Tag>

 <Key>string</Key>

 <Value>string</Value>

 </Tag>

 </And>

 </Filter>

 <Tiering>

 <AccessTier>ARCHIVE_ACCESS</AccessTier>

 <Days></Days>

 </Tiering>

 <Tiering>

 <AccessTier>DEEP_ARCHIVE_ACCESS</AccessTier>

 <Days></Days>

 </Tiering>

 </IntelligentTieringConfiguration>

 <IntelligentTieringConfiguration>

 <Id></Id>

 <Status></Status>

 <Filter>

 <And>

 <Prefix>string</Prefix>

 <Tag>

 <Key>string</Key>

 <Value>string</Value>

 </Tag>

 <Tag>

 <Key>string</Key>

 <Value>string</Value>

 </Tag>

 </And>

 </Filter>

 <Tiering>

 <AccessTier>ARCHIVE_ACCESS</AccessTier>

 <Days></Days>

 </Tiering>

 <Tiering>

 <AccessTier>DEEP_ARCHIVE_ACCESS</AccessTier>

 <Days></Days>

 </Tiering>

 </IntelligentTieringConfiguration>

</ListBucketIntelligentTieringConfigurationOutput>

具体的节点描述如下：

名称 父节点 描述 类型
ListBucketIntelligentTieringConfigurationOutput 无 存储桶中所有智能分层配置规则的列表 Container
IntelligentTieringConfiguration ListBucketIntelligentTieringConfigurationOutput 包含智能分层配置的详细信息，其 XML 结构请参见

[GET Bucket IntelligentTiering](https://cloud.tencent.com/document/product/436/48349)Container

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

### 请求

下述请求示例展示了从存储桶 `examplebucket-1250000000` 中获取智能分层配置规则。

GET /?intelligent-tiering HTTP/1.1

Date: Mon, 28 Aug 2018 02:53:38 GMT

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1503895278;1503895638&q-key-time=1503895278;1503895638&q-header-list=host&q-url-param-list=inventory&q-signature=****************************************

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

### 响应

请求后，COS 返回以下响应，表明当前该存储桶内存在低频层规则default、归档及深度归档层规则 rule1 和 rule2 。

**低频规则 default**

连续30天无访问，智能分层对象从高频访问层转换为低频访问层。

**归档及深度归档层规则 rule1**

针对存储桶 examplebucket-1250000000 中前缀为 folder1 的智能分层对象生效。

连续100天无访问，智能分层对象从低频访问层转换为归档层。

连续200天无访问，智能分层对象从归档层转换为深度归档层。

**归档及深度归档层规则 rule2**

针对存储桶 examplebucket-1250000000 中前缀为 folder2 的智能分层对象生效。

连续91天无访问，智能分层对象从低频访问层转换为归档层。

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 331

Date: Mon, 28 Aug 2018 02:53:39 GMT

Server: tencent-cos

x-cos-request-id: NTlhMzg1ZWVfMjQ4OGY3MGFfMWE1NF8****

<ListBucketIntelligentTieringConfigurationOutput>

 <IntelligentTieringConfiguration>

 <Id>default</Id>

 <Status>Enabled</Status>

 <Tiering>

 <AccessTier>INFREQUENT</AccessTier>

 <Days>30</Days>

 <RequestFrequent>1</RequestFrequent>

 </Tiering>

 </IntelligentTieringConfiguration>

 <IntelligentTieringConfiguration>

 <Id>rule1</Id>

 <Status>Enabled</Status>

 <Filter>

 <Prefix>folder1</Prefix>

 </Filter>

 <Tiering>

 <AccessTier>ARCHIVE_ACCESS</AccessTier>

 <Days>100</Days>

 </Tiering>

 <Tiering>

 <AccessTier>DEEP_ARCHIVE_ACCESS</AccessTier>

 <Days>200</Days>

 </Tiering>

 </IntelligentTieringConfiguration>

 <IntelligentTieringConfiguration>

 <Id>rule2</Id>

 <Status>Enabled</Status>

 <Filter>

 <Prefix>folder2</Prefix>

 </Filter>

 <Tiering>

 <AccessTier>ARCHIVE_ACCESS</AccessTier>

 <Days>91</Days>

 </Tiering>

 </IntelligentTieringConfiguration>

</ListBucketIntelligentTieringConfigurationOutput>
