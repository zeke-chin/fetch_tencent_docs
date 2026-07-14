<!-- source: https://cloud.tencent.com/document/product/436/19223 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:40:49+08:00 -->

# PUT Bucket replication

最近更新时间：2025-09-01 17:29:31


## 功能描述

PUT Bucket replication 用于向已启用版本控制的存储桶中配置存储桶复制规则。如果存储桶已经配置了存储桶复制规则，那么该请求会替换现有配置。

**注意：**

使用该接口时，需确保源存储桶和目标存储桶已经开启版本控制，开启版本控制的 API 文档请参见 [PUT Bucket versioning](https://cloud.tencent.com/document/product/436/19889) 接口文档。

如果已存在多条存储桶复制规则，调用此接口会覆盖掉已有的存储桶复制规则。

## 授权说明

[授权策略](https://cloud.tencent.com/document/product/436/31923) 中 action 设置为 `cos:PutBucketReplication`。查看所有 [action](https://cloud.tencent.com/document/product/598/69901)。

## 请求

#### 请求示例

PUT /?replication HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Content-MD5: MD5

Authorization: Auth String

request body

**说明：**

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，详情请参见 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；<Region> 为 COS 的可用地域，详情请参见 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

用户在请求体中设置存储桶复制的具体配置信息。配置信息包括存储桶复制规则的启用状态、优先级、复制内容、筛选范围、目标存储桶的存储桶名称和存储地域等信息。

<ReplicationConfiguration>

 <Role>qcs::cam::uin/OwnerUin:uin/SubUin</Role>

 <Rule>

 <Status>String</Status>

 <Priority>Integer</Priority>

 <ID>String</ID>

 <Prefix>String</Prefix>

 <Destination>

 <Bucket>qcs::cos:Region::BucketName-APPID</Bucket>

 <StorageClass>String</StorageClass>

 <EncryptionConfiguration>

 <ReplicaKmsKeyID>String</ReplicaKmsKeyID>

 </EncryptionConfiguration>

 </Destination>

 <DeleteMarkerReplication>

 <Status>String</Status>

 </DeleteMarkerReplication>

 <SourceSelectionCriteria>

 <SseKmsEncryptedObjects>

 <Status>String</Status>

 </SseKmsEncryptedObjects>

 </SourceSelectionCriteria>

 </Rule>

</ReplicationConfiguration>

具体内容描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
ReplicationConfiguration 无 说明所有复制配置信息 Container 是
Role ReplicationConfiguration 发起者身份标识：`qcs::cam::uin/<OwnerUin>:uin/<SubUin>`，其中 <OwnerUin> 为主账号 UIN，<SubUin> 可以是主账号 UIN 或已被授权的子账号 UIN String 是
Rule ReplicationConfiguration 具体配置信息，最多支持1000个 Container 是
ID ReplicationConfiguration.Rule 用来标注具体 Rule 的名称 String 否
Status ReplicationConfiguration.Rule 标识 Rule 是否生效，枚举值：Enabled、Disabled String 否
Priority ReplicationConfiguration.Rule 执行优先级，用于处理目标存储桶相同、复制规则命中同一个对象的情况

**注意：**

支持设置1 - 1000范围内的正整数，不同规则的 Priority 值不可重复。

存储桶复制规则必须全部携带 Priority 或全部不携带 Priority。

所有规则都携带 Priority 时，当目标存储桶相同时，不同规则的筛选 prefix 可以存在重叠。不同规则命中同一个对象时，会优先触发 Priority 值最小的规则。

所有规则都不携带 Priority 时，不同规则的筛选 Prefix 不允许重叠。Integer 否。同一个存储桶的规则必须全部包含 Priority 或者全部不包含 Priority。
Filter ReplicationConfiguration.Rule 筛选待复制对象。存储桶功能将复制符合 Filter 中设置的前缀、标签的对象 Container 否
And ReplicationConfiguration.Rule 筛选待复制对象时，如果同时需要前缀与对象标签条件，或需要使用多个对象标签条件时，需要用 And 包装 Container 否
Prefix ReplicationConfiguration.Rule 或

ReplicationConfiguration.Rule.Filter 或ReplicationConfiguration.Rule.Filter.And 需要复制的对象前缀 String 否
Tag ReplicationConfiguration.Rule.Filter.And 筛选待复制对象时，可以用对象标签（支持多个）作为过滤条件，最多支持填入10个标签。添加标签作为筛选条件后，同步删除标记选项必须置为 false Container 否
Key ReplicationConfiguration.Rule.Filter.And.Tag 筛选标签的 Key 值 String 否
Value ReplicationConfiguration.Rule.Filter.And.Tag 筛选标签的 Value 值 String 否
Destination ReplicationConfiguration.Rule 目标存储桶信息 Container 是
Bucket ReplicationConfiguration.Rule.Destination 资源标识符：`qcs::cos:<Region>::<BucketName-APPID>`，详情请参见 [资源描述方式](https://cloud.tencent.com/document/product/598/10606)。String 是
StorageClass ReplicationConfiguration.Rule.Destination 目标存储类型，代表存储到目标存储桶使用的存储类型。例如 `STANDARD`、`STANDARD_IA` 等，详情请参见 [存储类型概述](https://cloud.tencent.com/document/product/436/33417)。

**说明：**

满足以下任意一种情况，则 StorageClass 为必选参数：

源存储桶或目标存储桶，一个是多 AZ 桶、一个是单 AZ 桶。

源存储桶和目标存储桶，一个开启了智能分层，一个未开启智能分层。

如果不填写 StorageClass 参数，投递到目标存储桶的存储类型默认和源存储桶保持一致。String 否
EncryptionConfiguration Destination 当 SseKmsEncryptedObjects.Status 设置为 Enabled 后，必须包含此字段。用于设置复制到目标桶的 KMS 加密对象所使用的 KMS 密钥 String 否
ReplicaKmsKeyID EncryptionConfiguration KMS 密钥。您可通过 [KMS 控制台](https://console.cloud.tencent.com/kms2) 创建 KMS 密钥并获取 KMS 密钥 ID，更多信息请参见 [创建密钥](https://cloud.tencent.com/document/product/573/8875) 和 [查看密钥](https://cloud.tencent.com/document/product/573/38386)String 否
DeleteMarkerReplication ReplicationConfiguration.Rule 是否同步删除标记 Container 否
Status ReplicationConfiguration.Rule.DeleteMarkerReplication 是否同步删除标记，支持 `Disabled` 或 `Enabled`。默认值为 `Enabled`，即同步删除标记 String 否
SourceSelectionCriteria ReplicationConfiguration.Rule 用于说明存储桶复制规则支持复制的对象的额外条件。当前，仅支持选择是否复制 KMS 加密的对象 Container 否
SseKmsEncryptedObjects ReplicationConfiguration.Rule.SourceSelectionCriteria 选择是否复制 KMS 加密的对象 Container 否
Status ReplicationConfiguration.Rule.SseKmsEncryptedObjects 选择是否复制 KMS 加密的对象，支持枚举值 `Enabled` 和 `Disabled`String 否

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

### 案例一：根据前缀筛选的存储桶复制规则

#### 请求

以下请求是对存储桶 `originbucket-1250000000` 添加一条存储桶复制配置。该存储桶复制配置中，指定复制对象前缀为 `testPrefix` 的对象，目标存储桶为广州的 `destinationbucket-1250000000`。

PUT /?replication HTTP/1.1

Date: Mon, 28 Aug 2017 02:53:38 GMT

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1503888878;1503889238&q-key-time=1503888878;1503889238&q-header-list=host&q-url-param-list=replication&q-signature=****************************************

Content-MD5: AAq9nzrpsz5LJ4UEe1f6Q==

Host: originbucket-1250000000.cos.ap-guangzhou.myqcloud.com

Content-Length: 312

<ReplicationConfiguration>

 <Role>qcs::cam::uin/100000000001:uin/100000000001</Role>

 <Rule>

 <Status>Enabled</Status>

 <ID>RuleId_01</ID>

 <Prefix>testPrefix</Prefix>

 <Destination>

 <Bucket>qcs::cos:ap-guangzhou::destinationbucket-1250000000</Bucket>

 </Destination>

 </Rule>

</ReplicationConfiguration>

#### 响应

上述请求后，COS 返回以下响应，表明当前该跨地域配置已经成功设置完毕。

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 0

Connection: keep-alive

Date: Fri, 14 Apr 2019 07:06:19 GMT

Server: tencent-cos

x-cos-bucket-region: ap-guangzhou

x-cos-request-id: NWQwMzQ3NmJfMjRiMjU4NjRfOTM4NV82ZDU1****

x-cos-trace-id: OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODc0OWRkZjk0ZDM1NmI1M2E2MTRlY2MzZDhmNmI5MWI1OWE4OGMxZjNjY2JiNTBmMTVmMWY1MzAzYzkyZGQ2ZWM4MzUyZTg1NGRhNWY0NTJiOGUyNTViYzgyNzgxZTEwOTY=

### 案例二：根据标签筛选的存储桶复制规则

#### 请求

以下 PUT Bucket replication 请求向存储桶 `originbucket-1250000000`中添加一条存储桶复制配置。该存储桶复制配置中，指定复制前缀为`test1`、标签为`<111, 232>`的对象，目标存储桶为广州的 `destinationbucket-1250000000`。设置标签筛选后，规则内的同步删除对象必须置为 Disabled。

PUT /?replication HTTP/1.1

Host: originbucket-1250000000.cos.ap-guangzhou.myqcloud.com

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1667303319;1668303369&q-key-time=1667303319;1668303369&q-url-param-list=replication&q-header-list=content-md5;host&q-signature=****************************************

Content-Md5: Hmy/6lHINHLKhp/PY****

Content-Length: 674

Content-Type: application/x-www-form-urlencoded

<ReplicationConfiguration>

 <Role>qcs::cam::uin/100000000001:uin/100000000001</Role>

 <Rule>

 <Status>Enabled</Status>

 <Filter>

 <And>

 <Prefix>test1</Prefix>

 <Tag>

 <Key>111</Key>

 <Value>232</Value>

 </Tag>

 </And>

 </Filter>

 <Destination>

 <Bucket>qcs::cos:ap-guangzhou::destinationbucket-1250000000</Bucket>

 <StorageClass>Standard</StorageClass>

 </Destination>

 <DeleteMarkerReplication>

 <Status>Disabled</Status>

 </DeleteMarkerReplication>

 </Rule>

</ReplicationConfiguration>

#### 响应

上述请求后，COS 返回以下响应，表明当前该跨地域配置已经成功设置完毕。

HTTP/1.1 200 OK

Content-Length: 0

Connection: keep-alive

Date: Tue, 01 Nov 2022 11:49:48 GMT

Server: tencent-cos

x-cos-bucket-region: ap-guangzhou

x-cos-request-id: NjM2MTA3ZGNfNmE1MGI3MDlfYWU5N1*******

### 案例三：设置多个复制到同一目标存储桶、筛选前缀有重叠的规则，通过 Priority 设置生效的优先级

#### 请求

以下 PUT Bucket replication 请求向存储桶 `originbucket-1250000000`中添加两条存储桶复制配置规则。

规则1：指定复制前缀为 `test1`、标签为`<a,a>`的对象，目标存储桶为广州的 `destinationbucket-1250000000`，目标存储类型为`Standard`，规则内的同步删除对象必须置为 Disabled，Priority 为1。

规则2:指定复制前缀为 `test1`、标签为`<b,b>`的对象，目标存储桶为广州的 `destinationbucket-1250000000`，目标存储类型为`Standard_IA`，规则内的同步删除对象必须置为 Disabled，Priority 为2。

用户向存储桶 `originbucket-1250000000`上传对象 `test1/temp.txt`，上传同时打标签`<a,a>`和`<b,b>`，此时根据 Priority，规则1优先生效，复制到存储桶 `destinationbucket-1250000000`对象的类型为 `Standard`。

PUT /?replication HTTP/1.1

Host: originbucket-1250000000.cos.ap-guangzhou.myqcloud.com

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1667309117;1668309167&q-key-time=1667309117;1668309167&q-url-param-list=replication&q-header-list=content-md5;host&q-signature=****************************************

Content-Md5: OngWIL6wb2pnJZHk*****

Content-Length: 1351

Content-Type: application/x-www-form-urlencoded

<ReplicationConfiguration>

 <Role>qcs::cam::uin/100000000001:uin/100000000001</Role>

 <Rule>

 <Status>Enabled</Status>

 <Priority>1</Priority>

 <Filter>

 <And>

 <Prefix>test1</Prefix>

 <Tag>

 <Key>a</Key>

 <Value>a</Value>

 </Tag>

 </And>

 </Filter>

 <Destination>

 <Bucket>qcs::cos:ap-guangzhou::destinationbucket-1250000000</Bucket>

 <StorageClass>Standard</StorageClass>

 </Destination>

 <DeleteMarkerReplication>

 <Status>Disabled</Status>

 </DeleteMarkerReplication>

 </Rule>

 <Role>qcs::cam::uin/100000000001:uin/100000000001</Role>

 <Rule>

 <Status>Enabled</Status>

 <Priority>2</Priority>

 <Filter>

 <And>

 <Prefix>test1</Prefix>

 <Tag>

 <Key>b</Key>

 <Value>b</Value>

 </Tag>

 </And>

 </Filter>

 <Destination>

 <Bucket>qcs::cos:ap-guangzhou::destinationbucket-1250000000</Bucket>

 <StorageClass>Standard_IA</StorageClass>

 </Destination>

 <DeleteMarkerReplication>

 <Status>Disabled</Status>

 </DeleteMarkerReplication>

 </Rule>

</ReplicationConfiguration>

#### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: keep-alive

Date: Tue, 01 Nov 2022 13:26:23 GMT

Server: tencent-cos

x-cos-bucket-region: ap-guangzhou

x-cos-request-id: NjM2MTFlN2ZfYjA1MGI3MDlfMjQ2ZmZfOWE******
