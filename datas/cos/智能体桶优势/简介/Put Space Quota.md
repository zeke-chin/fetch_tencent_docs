<!-- source: https://cloud.tencent.com/document/product/436/133860 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:35:24+08:00 -->

# Put Space Quota

最近更新时间：2026-07-09 15:06:03


## 功能描述

设置指定空间的存储配额。

## 请求

### 请求语法

PUT /<SpaceId>/?space-quota HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Content-Type: application/xml

Content-Length: Content Length

Authorization: Auth String

[Request Body]

**说明：**

SpaceId: 对应 ObjectKey 一级目录，需要预先通过 PUT Object 接口上传大小为空的一级目录对象来创建对应的 SpaceId。

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 smhxxxxxxxxxxxxx-1250000000；<Region> 为可用地域，可参见 [产品概述](https://cloud.tencent.com/document/product/436/132574) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求参数

此接口无请求参数。

### 请求体

提交 **application/xml** 请求数据，包含要设置的 Space 的空间配额信息。

<SpaceQuota>

 <Capacity>1099511627776</Capacity>

</SpaceQuota>

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
SpaceQuota 无 包含 Put Space Quota 操作的所有请求信息 Container 是

Container 节点 SpaceQuota 的内容：

节点名称（关键字）父节点 描述 类型 是否必选
Capacity SpaceQuota 配额大小，单位为字节（字符串）。必须为有效的非负整数，且不超过 9223372036854775807（int64 最大值）number 是

## 响应

### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

### 响应体

请求成功，返回 **application/xml** 数据，包含 Space 的 Quota 信息。

<SpaceQuota>

 <QuotaId>12345</QuotaId>

 <Capacity>102400</Capacity>

</SpaceQuota>

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型
SpaceQuota 无 保存 Put Space Quota 结果的所有信息 Container

Container 节点 SpaceQuota 的内容：

节点名称（关键字）父节点 描述 类型
QuotaId SpaceQuota 配额的唯一标识符 string
Capacity SpaceQuota 配额容量，单位为字节 number

## 实际案例

### 请求

PUT /test-space/?space-quota HTTP/1.1

Host: smhxxx-1250000000.cos.ap-chengdu.myqcloud.com

Content-Type: application/xml

Content-Length: 64

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1566302375;1566309575&q-key-time=1566302375;1566309575&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=delete&q-signature=****************************************

<SpaceQuota>

 <Capacity>102400</Capacity>

</SpaceQuota>

### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 118

Date: Tue, 20 Aug 2019 11:59:35 GMT

x-cos-request-id: NWQ1YmUwYTdfM2FiMDJhMDlfYzczN18zMGM1****

<SpaceQuota>

 <QuotaId>1</QuotaId>

 <Capacity>102400</Capacity>

</SpaceQuota>
