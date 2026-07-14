<!-- source: https://cloud.tencent.com/document/product/436/8280 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:39:05+08:00 -->

# PUT Bucket lifecycle

最近更新时间：2026-05-27 17:52:34


## 功能描述

COS 支持用户以生命周期配置的方式来管理 Bucket 中 Object 的生命周期。生命周期配置包含一个或多个将应用于一组对象规则的规则集（其中每个规则为 COS 定义一个操作）。 这些操作分为以下两种：

**转换操作：**定义对象转换为另一个存储类的时间。例如，您可以选择在对象创建30天后将其转换为低频存储（STANDARD_IA，适用于不常访问）存储类别。同时也支持将数据沉降到智能分层存储（INTELLIGENT_TIERING，访问模式不固定）和归档存储（ARCHIVE，成本更低）。具体参数查看请求示例说明中 Transition 项。

**过期操作：**指定 Object 的过期时间。COS 将会自动为用户删除过期的 Object。

**注意：**

如果该 Bucket 已配置生命周期，使用该接口创建新的配置的同时则会覆盖原有的配置。

同一条生命周期规则中不可同时支持 Days 和 Date 参数，请分成两条规则分别传入，具体请参见下文 [实际案例](https://cloud.tencent.com/document/product/436/8280#.E5.AE.9E.E9.99.85.E6.A1.88.E4.BE.8B)。

开启了 [多 AZ](https://cloud.tencent.com/document/product/436/40548) 配置的存储桶，不支持将多 AZ 存储类型沉降到单 AZ 存储类型。

每个存储桶最多可添加1000条生命周期规则。

基于访问时间（Access Time，Atime）的生命周期规则当前白名单开放，仅支持沉降到低频存储，不兼容 MAZ 存储桶，不支持标签筛选和对象大小筛选，更多限制及说明可参考 [基于访问时间的生命周期规则](https://cloud.tencent.com/document/product/436/107738)。

## 授权说明

[授权策略](https://cloud.tencent.com/document/product/436/31923) 中 action 设置为 cos:PutBucketLifecycle。查看所有 [action](https://cloud.tencent.com/document/product/598/69901)。

## 请求

#### 请求示例

PUT /?lifecycle HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Content-Length: length

Date: GMT Date

Authorization: Auth String

Content-MD5: MD5

**说明：**

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；<Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该 API 接口请求的请求体具体节点内容为：

<LifecycleConfiguration>

 <Rule>

 <ID>String</ID>

 <Filter>

 <And>

 <Prefix>String</Prefix>

 <PrefixNotEquals>String</PrefixNotEquals>

 <Tag>

 <Key>String</Key>

 <Value>String</Value>

 </Tag>

 <ObjectSizeGreaterThan>Integer</ObjectSizeGreaterThan>

 <ObjectSizeLessThan>Integer</ObjectSizeLessThan>

 </And>

 </Filter>

 <Status>String</Status>

 <Transition>

 <Days>Integer</Days>

 <StorageClass>String</StorageClass>

 </Transition>

 <NoncurrentVersionExpiration>

 <NoncurrentDays>Integer</NoncurrentDays>

 </NoncurrentVersionExpiration>

 </Rule>

 <Rule>

 <ID>String</ID>

 <Filter>

 <Prefix>String</Prefix>

 </Filter>

 <Status>String</Status>

 <Transition>

 <Days>Integer</Days>

 <StorageClass>String</StorageClass>

 </Transition>

 <NoncurrentVersionTransition>

 <NoncurrentDays>Integer</NoncurrentDays>

 <StorageClass>String</StorageClass>

 </NoncurrentVersionTransition>

 </Rule>

 <Rule>

 <ID>String</ID>

 <Filter>

 <Prefix>String</Prefix>

 </Filter>

 <Status>String</Status>

 <Expiration>

 <ExpiredObjectDeleteMarker>Boolean</ExpiredObjectDeleteMarker>

 </Expiration>

 <NoncurrentVersionExpiration>

 <NoncurrentDays>Integer</NoncurrentDays>

 </NoncurrentVersionExpiration>

 <AbortIncompleteMultipartUpload>

 <DaysAfterInitiation>Integer</DaysAfterInitiation>

 </AbortIncompleteMultipartUpload>

 </Rule>

 <Rule>

 <ID>String</ID>

 <Filter>

 <And>

 <Prefix>String</Prefix>

 <PrefixNotEquals>String</PrefixNotEquals>

 </And>

 </Filter>

 <Status>String</Status>

 <Transition>

 <AccessFrequency>

 <AccessCountLessThan>Container</AccessCountLessThan>

 <RecentDays>Integer</RecentDays>

 </AccessFrequency>

 <StorageClass>String</StorageClass>

 </Transition>

 <NoncurrentVersionTransition>

 <AccessFrequency>

 <AccessCountLessThan>Container</AccessCountLessThan>

 <RecentDays>Integer</RecentDays>

 </AccessFrequency>

 <StorageClass>String</StorageClass>

 </NoncurrentVersionTransition>

 </Rule>

</LifecycleConfiguration>

具体内容描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
LifecycleConfiguration 无 生命周期配置 Container 是
Rule LifecycleConfiguration 规则描述 Container 是
ID LifecycleConfiguration.Rule 用于唯一地标识规则，长度不能超过255个字符 String 否
Filter LifecycleConfiguration.Rule Filter 用于描述规则影响的 Object 集合 Container 否
And LifecycleConfiguration.Rule

.Filter 对象筛选器中的一个子集，仅当需要指定多种筛选规则时才需要此元素，例如：同时指定 Prefix 和 Tag 筛选，或同时指定多个 Tag 筛选。Container 否
Prefix LifecycleConfiguration.Rule

.Filter.And 指定规则所适用的前缀。匹配前缀的对象受该规则影响，Prefix 最多只能有一个 String 否
PrefixNotEquals LifecycleConfiguration.Rule.Filter.And 筛选 Prefix 不匹配该字符串的 Objects。PrefixNotEquals 最多只能有一个，且覆盖范围是 Prefix 的子集。String 否
ObjectSizeGreaterThan LifecycleConfiguration.Rule .Filter.And 筛选条件，指定规则所适用的对象的大小必须大于某值（不包括等于），单位为 Bytes。

**注意：**

ObjectSizeGreaterThan 的值必须大于等于65536。

若规则的 Filter 包含关于对象大小的筛选条件，则该规则不支持同时包含删除碎片（AbortIncompleteMultipartUpload）、清理删除标记（ExpiredObjectDeleteMarker）。Integer 否
ObjectSizeLessThan LifecycleConfiguration.Rule .Filter.And 筛选条件，指定规则所适用的对象必须小于某值（不包括等于），单位为 Bytes。

**注意：**

ObjectSizeLessThan 的值必须大于等于65537。

ObjectSizeLessThan 的值必须大于 ObjectSizeGreaterThan。

若规则的 Filter 包含关于对象大小的筛选条件，则该规则不支持同时包含删除碎片（AbortIncompleteMultipartUpload）、清理删除标记（ExpiredObjectDeleteMarker）。Integer 否
Tag LifecycleConfiguration.Rule

.Filter.And 标签集合，最多支持10个标签。Container 否
Key LifecycleConfiguration.Rule

.Filter.And.Tag 标签的 Key，长度不超过128字节，支持英文字母、数字、空格、加号、

减号、下划线、等号、点号、冒号、斜线。String 否
Value LifecycleConfiguration.Rule

.Filter.And.Tag 标签的 Value，长度不超过256字节, 支持英文字母、数字、空格、加号、

减号、下划线、等号、点号、冒号、斜线。String 否
Status LifecycleConfiguration.Rule 指明规则是否启用，枚举值：Enabled，Disabled。String 是
Expiration LifecycleConfiguration.Rule 规则过期属性。可同时配置 Transition（规则转换属性） 或者选择其中一种属性进行配置。Container 否
ExpiredObjectDeleteMarker LifecycleConfiguration.Rule

.Expiration 删除无历史版本的删除标记。枚举值：true、false。

true：表示删除无历史版本的删除标记。

false：表示不删除无历史版本的删除标记。

**注意：**

同一条规则中不支持同时设置删除当前版本的参数。

同一条规则中必须同时设置删除历史版本的规则（NoncurrentVersionsExpiration），本参数才能正常生效。Boolean 否
Transition LifecycleConfiguration.Rule 规则转换属性，用于描述对象何时进行存储类型的转换和转换的存储类型。可同时配置 Expiration（规则过期属性） 或者选择其中一种属性进行配置。Container 否
Days LifecycleConfiguration.Rule

.Transition 或 Expiration 指明规则对应的动作在对象最后的修改日期过后多少天操作：

如果是 Transition，该字段有效值是非负整数。最大支持3650天。

如果是 Expiration，该字段有效值为正整数，最大支持3650天。Integer 否
AccessFrequency Transition 或 NoncurrentVersionTransition 指定基于访问时间的生命周期规则。配置此字段后，不支持配置最后修改时间相关的字段（Days 和 NoncurrentDays）。

**说明：**

基于访问时间的生命周期规则，详情请参见 [基于访问时间的生命周期规则](https://cloud.tencent.com/document/product/436/107738)。Container 否
RecentDays AccessFrequency 表示连续访问天数，天数范围不得超过365。需同时配置 AccessCountLessThan，表示指定文件在连续访问天数内、访问次数低于多少次来判断是否沉降对象。不支持配置最后修改时间相关的字段（Days 和 NoncurrentDays）。Integer 是
AccessCountLessThan AccessFrequency 表示访问对象的次数，默认值为1。需同时配置 RecentDays，表示指定文件在连续访问天数内、访问次数低于多少次来判断是否沉降对象。不支持配置最后修改时间相关的字段（Days 和 NoncurrentDays）。Container 是
AbortIncompleteMultipartUpload LifecycleConfiguration.Rule 清理未完成的分块上传和文件碎片。Container 否
DaysAfterInitiation LifecycleConfiguration.Rule

.AbortIncompleteMultipartUpload 指明分片上传开始后多少天内必须完成上传。Integer 是
NoncurrentVersionExpiration LifecycleConfiguration.Rule 指明非当前版本对象何时过期。Container 否
NoncurrentVersionTransition LifecycleConfiguration.Rule 指明非当前版本对象何时进行存储类型的转换和转换的存储类型。Container 否
NoncurrentDays LifecycleConfiguration.Rule

.NoncurrentVersionExpiration

或 NoncurrentVersionTransition 指明规则对应的动作在对象变成非当前版本多少天后执行

如果是 Transition，该字段有效值是非负整数。最大支持3650天。

如果是 Expiration，该字段有效值为正整数，最大支持3650天。Integer 否
StorageClass LifecycleConfiguration.Rule

Transition 或 NoncurrentVersionTransition 指定 Object 沉降后的存储类型，枚举值： STANDARD_IA，MAZ_STANDARD_IA，INTELLIGENT_TIERING，MAZ_INTELLIGENT_TIERING，ARCHIVE，DEEP_ARCHIVE。关于存储类型的介绍，请参见 [存储类型概述](https://cloud.tencent.com/document/product/436/33417)。String 是

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

### 案例一：基于最后修改时间沉降对象

#### 请求

PUT /?lifecycle HTTP/1.1

Host:examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Wed, 16 Aug 2017 11:59:33 GMT

Authorization:q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1502855771;1502935771&q-key-time=1502855771;1502935771&q-header-list=content-md5;host&q-url-param-list=lifecycle&q-signature=****************************************

Content-MD5: LcNUuow8OSZMrEDnvndw1Q==

Content-Length: 348

Content-Type: application/x-www-form-urlencoded

<LifecycleConfiguration>

 <Rule>

 <ID>id1</ID>

 <Filter>

 <Prefix>documents/</Prefix>

 </Filter>

 <Status>Enabled</Status>

 <Transition>

 <Days>100</Days>

 <StorageClass>ARCHIVE</StorageClass>

 </Transition>

 </Rule>

 <Rule>

 <ID>id2</ID>

 <Filter>

 <Prefix>logs/</Prefix>

 </Filter>

 <Status>Enabled</Status>

 <Transition>

 <Days>10</Days>

 <StorageClass>STANDARD_IA</StorageClass>

 </Transition>

 </Rule>

</LifecycleConfiguration>

#### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 0

Date: Wed, 16 Aug 2017 11:59:33 GMT

Server: tencent-cos

x-cos-request-id: NTk5NDMzYTRfMjQ4OGY3Xzc3NGRf****

### 案例二：基于访问时间沉降对象

#### 请求

PUT /?lifecycle HTTP/1.1

Host:examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Wed, 16 Aug 2020 11:59:33 GMT

Authorization:q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1502855771;1502935771&q-key-time=1502855771;1502935771&q-header-list=content-md5;host&q-url-param-list=lifecycle&q-signature=****************************************

Content-MD5: LcNUuow8OSZMrEDnvndw1Q==

Content-Length: 348

Content-Type: application/x-www-form-urlencoded

<LifecycleConfiguration>

 <Rule>

 <ID>id1</ID>

 <Filter>

 <Prefix>documents/</Prefix>

 </Filter>

 <Status>Enabled</Status>

 <Transition>

 <AccessFrequency>

 <AccessCountLessThan>2</AccessCountLessThan>

 <RecentDays>7</RecentDays>

 </AccessFrequency>

 <StorageClass></StorageClass>

 </Transition>

 <NoncurrentVersionTransition>

 <AccessFrequency>

 <AccessCountLessThan>2</AccessCountLessThan>

 <RecentDays>7</RecentDays>

 </AccessFrequency>

 <StorageClass></StorageClass>

 </NoncurrentVersionTransition>

 </Rule>

</LifecycleConfiguration>

#### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 0

Date: Wed, 16 Aug 2020 11:59:33 GMT

Server: tencent-cos

x-cos-request-id: NTk5NDMzYTRfMjQ4OGY3Xzc3NGRf****
