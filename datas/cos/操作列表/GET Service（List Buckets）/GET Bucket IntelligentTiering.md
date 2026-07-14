<!-- source: https://cloud.tencent.com/document/product/436/48349 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:40:00+08:00 -->

# GET Bucket IntelligentTiering

最近更新时间：2025-06-11 18:19:01


## 功能描述

GET Bucket IntelligentTiering 接口用于查询存储桶的智能分层配置信息。用户在发起该请求时，需要用户提供规则名称，发起该请求时需获得请求签名，表明该请求已获得许可。

**说明：**

只有主账号或者被授权 GET Bucket IntelligentTiering 接口权限的子账号可以调用该接口。

id 为 default，用于查询低频层规则；id 非 default，用于查询归档及深度归档层规则。

获取 id 为 default 的规则，

如果您从未在存储桶上启用智能分层存储配置，则响应为404：

<?xml version='1.0' encoding='utf-8' ?>

<Error>

<Code>IntelligentTieringConfigurationNotFoundError</Code>

<Message>The Intelligenttiering configuration was not found.</Message>

</Error>

如果您启用了存储桶的智能分层配置，则响应为200：

<IntelligentTieringConfiguration>

 <Id>default</Id>

 <Status>Enabled</Status>

 <Tiering>

 <AccessTier>INFREQUENT</AccessTier>

 <Days>30|60|90</Days>

 </Tiering>

</IntelligentTieringConfiguration>

## 授权说明

授权策略中 action 设置为 cos:GetBucketIntelligentTiering。查看所有 [action](https://cloud.tencent.com/document/product/598/69901)。

## id 为 default（查询低频层规则）

### 请求

#### 请求示例

GET /?intelligent-tiering&id=default HTTP 1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT date

Authorization: Auth String

**说明：**

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；<Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

调用 GET Bucket IntelligentTiering 需要使用规则名称参数，低频层规则名称固定为 default。

参数 描述 类型 是否必选
id 智能分层规则名称清单任务的名称，id 设置为 default，表示查询低频层规则。String 是

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

### 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

<IntelligentTieringConfiguration>

 <Id>default</Id>

 <Status>Enabled</Status>

 <Tiering>

 <AccessTier>INFREQUENT</AccessTier>

 <Days>30|60|90</Days>

 <RequestFrequent>1</RequestFrequent>

 </Tiering>

</IntelligentTieringConfiguration>

具体的节点描述如下：

名称 父节点 描述 类型
IntelligentTieringConfiguration 无 智能分层存储配置的具体信息 Container
Id IntelligentTieringConfiguration 说明智能分层存储配置规则名称，低频层规则固定为 default。String
Status IntelligentTieringConfiguration 说明智能分层规则是否开启，枚举值：Enabled、Disabled。当 id 为 default 时，仅支持设置 Enabled Enum
Tiering IntelligentTieringConfiguration 指定智能分层规则中有关数据转换的配置信息 Container
AccessTier IntelligentTieringConfiguration.Tiering id为 default 时，用于表示低频层级，枚举值：INFREQUENT。Enum
Days IntelligentTieringConfiguration.Tiering 指定智能分层存储规则中标准层数据转换为低频层数据的天数限制，默认值为30天，支持选择30、60、90 Int
RequestFrequent IntelligentTieringConfiguration.Tiering 指定配置中标准层数据转换为低频层数据的访问次数限制，默认值为1，和天数搭配使用可以实现转换效果。

例如设置该参数为1，访问天数为30，代表连续30天访问次数小于1次的对象会从标准层降到低频层。Int

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

### 实际案例

#### 请求

GET /?intelligenttiering&id=default HTTP/1.1

Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com

Connection: keep-alive

Accept-Encoding: gzip, deflate

Accept: */*

User-Agent: python-requests/2.12.4

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1480932292;1981012292&q-key-time=1480932292;1981012292&q-url-param-list=versioning&q-header-list=host&q-signature=****************************************

#### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 120

Connection: keep-alive

Date: Sun, 23 Aug 2020 08:15:16 GMT

Server: tencent-cos

x-cos-request-id: NTk5ZDM5OTRfZDNhZDM1MGFfMjYyMTFfZmU3****

<IntelligentTieringConfiguration>

 <Id>default</Id>

 <Status>Enabled</Status>

 <Tiering>

 <AccessTier>INFREQUENT</AccessTier>

 <Days>30</Days>

 <RequestFrequent>1</RequestFrequent>

 </Tiering>

</IntelligentTieringConfiguration>

## id 非 default（查询归档层及深度归档层规则）

### 请求

#### 请求示例

GET /?intelligent-tiering&id=Id HTTP 1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT date

Authorization: Auth String

**说明：**

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；<Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

调用 GET Bucket IntelligentTiering 需要使用规则名称参数，低频层规则名称固定为default，名称非default的表示归档及深度归档层规则。

参数 描述 类型 是否必选
id 智能分层规则名称清单任务的名称，id设置为非default的字符串，表示该规则为归档层、深度归档层转换规则。String 是

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

### 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

<IntelligentTieringConfiguration>

 <Id>rule1</Id>

 <Status>Enabled</Status>

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

 ...

 </And>

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

具体的节点描述如下：

名称 父节点 描述 类型
IntelligentTieringConfiguration 无 智能分层规则的详细信息。Container
Id IntelligentTieringConfiguration 智能分层规则名称清单任务的名称，id 设置为非 default 的字符串，表示该规则为归档层、深度归档层转换规则。String
Status IntelligentTieringConfiguration 说明智能分层规则是否开启，枚举值：Enabled、Disabled。

当id 为 default 时，仅支持设置 Enabled。Enum
Filter IntelligentTieringConfiguration 筛选待分析对象。id 非 default 时，归档及深度归档层规则将针对符合 Filter 中设置的前缀、标签的对象生效。Container
And IntelligentTieringConfiguration.Filter 筛选条件，如果同时需要前缀与对象标签条件，需要用 And 包装。Container
Prefix IntelligentTieringConfiguration.Filter.And 筛选对象前缀，最多指定一个前缀。String
Tag IntelligentTieringConfiguration.Filter.And 筛选待分析对象时，可以用对象标签（支持多个）作为过滤条件。Container
Tiering IntelligentTieringConfiguration 指定智能分层存储配置中有关数据转换的配置信息。Container
AccessTier IntelligentTieringConfiguration.Tiering id 非 default 时，用于指定归档或深度归档层级，枚举值：ARCHIVE_ACCESS、DEEP_ARCHIVE_ACCESS Enum
Days IntelligentTieringConfiguration.Tiering id 非 default 时，指定智能分层存储配置中数据转换为归档层或深度归档层的天数限制。

归档层(ARCHIVE_ACCESS)支持设置范围为91～730。

深度归档层(DEEP_ARCHIVE_ACCESS)支持设置范围为180～730。

同一条规则中，深度归档层的天数必须大于归档层的天数。Int

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

### 实际案例

#### 请求

GET /?intelligent-tiering&id=rule1 HTTP/1.1

Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com

Connection: keep-alive

Accept-Encoding: gzip, deflate

Accept: */*

User-Agent: python-requests/2.12.4

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1480932292;1981012292&q-key-time=1480932292;1981012292&q-url-param-list=versioning&q-header-list=host&q-signature=****************************************

#### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 120

Connection: keep-alive

Date: Sun, 23 Aug 2020 08:15:16 GMT

Server: tencent-cos

x-cos-request-id: NTk5ZDM5OTRfZDNhZDM1MGFfMjYyMTFfZmU3****

<IntelligentTieringConfiguration>

 <Id>rule1</Id>

 <Status>Enabled</Status>

 <Tiering>

 <AccessTier>ARCHIVE_ACCESS</AccessTier>

 <Days>100</Days>

 </Tiering>

 <Tiering>

 <AccessTier>DEEP_ARCHIVE_ACCESS</AccessTier>

 <Days>200</Days>

 </Tiering>

</IntelligentTieringConfiguration>
