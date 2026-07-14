<!-- source: https://cloud.tencent.com/document/product/436/7738 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:38:18+08:00 -->

# PUT Bucket

最近更新时间：2025-12-30 15:06:31


## 功能描述

PUT Bucket 接口请求可以在指定账号下创建一个存储桶。该 API 接口不支持匿名请求，您需要使用带 Authorization 签名认证的请求才能创建新的 Bucket 。创建存储桶的用户默认成为存储桶的持有者。

**说明**

创建存储桶时，如果没有指定访问权限，则默认使用私有读写（private）权限。

如需创建多 AZ 存储桶，那么应当通过请求体指示存储桶配置，否则无需传入请求体。

## 授权说明

授权策略中 action 设置为 cos:PutBucket 。查看所有 [action](https://cloud.tencent.com/document/product/598/69901)。

## 请求

#### 请求示例

**示例一**

PUT / HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Content-Length: 0

Authorization: Auth String

**示例二**

PUT / HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Content-Type: application/xml

Content-Length: Content Length

Content-MD5: MD5

Authorization: Auth String

[Request Body]

**说明**

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；<Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

此接口无请求参数。

#### 请求头

此接口除使用公共请求头部外，还支持以下请求头部，了解公共请求头部详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

名称 描述 类型 是否必选
x-cos-tagging 在创建存储桶的同时，为存储桶添加标签，最多可设置50个标签。例如 `key1=value1&key2=value2`string 否

**访问控制列表（ACL）相关头部**

在创建存储桶时可以通过指定下列请求头部来设置存储桶的访问权限：

名称 描述 类型 是否必选
x-cos-acl 定义存储桶的访问控制列表（ACL）属性。枚举值请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E9.A2.84.E8.AE.BE.E7.9A.84-acl) 文档中存储桶的预设 ACL 部分，如 private，public-read 等，默认为 private Enum 否
x-cos-grant-read 赋予被授权者读取存储桶的权限，格式为 id="[OwnerUin]"，如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，如 `id="100000000001",id="100000000002"`string 否
x-cos-grant-write 赋予被授权者写入存储桶的权限，格式为 id="[OwnerUin]"，如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，如 `id="100000000001",id="100000000002"`string 否
x-cos-grant-read-acp 赋予被授权者读取存储桶的访问控制列表（ACL）和存储桶策略（Policy）的权限，格式为 id="[OwnerUin]"，如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，如 `id="100000000001",id="100000000002"`string 否
x-cos-grant-write-acp 赋予被授权者写入存储桶的访问控制列表（ACL）和存储桶策略（Policy）的权限，格式为 id="[OwnerUin]"，如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，如 `id="100000000001",id="100000000002"`string 否
x-cos-grant-full-control 赋予被授权者操作存储桶的所有权限，格式为 id="[OwnerUin]"，如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，如 `id="100000000001",id="100000000002"`string 否

#### 请求体

仅当需要创建多 AZ 存储桶时提交 **application/xml** 请求数据，包含创建存储桶的配置信息，否则无需传入请求体。

<CreateBucketConfiguration>

 <BucketAZConfig>string</BucketAZConfig>

</CreateBucketConfiguration>

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
CreateBucketConfiguration 无 包含 PUT Bucket 操作的所有请求信息 Container 否

**Container 节点 CreateBucketConfiguration 的内容：**

节点名称（关键字）父节点 描述 类型 是否必选
BucketAZConfig CreateBucketConfiguration 存储桶 AZ 配置，指定为 MAZ 以创建多 AZ 存储桶 string 是

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

此接口响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：简单案例（单 AZ 存储桶）

##### 请求

PUT / HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Sun, 26 May 2019 14:51:38 GMT

Content-Length: 0

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature=****************************************

Connection: close

##### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Sun, 26 May 2019 14:51:37 GMT

Server: tencent-cos

x-cos-request-id: NWNlYWE3ZjlfZDQyNzVkNjRfMzg1N18yNzFh****

#### 案例二：指定公有读并授权特定用户读取权限和写入对象

##### 请求

PUT / HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Fri, 14 Jun 2019 13:48:59 GMT

x-cos-acl: public-read

x-cos-grant-write: id="100000000002"

x-cos-grant-read-acp: id="100000000002"

Content-Length: 0

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1560520139;1560527339&q-key-time=1560520139;1560527339&q-header-list=content-length;date;host;x-cos-acl;x-cos-grant-read-acp;x-cos-grant-write&q-url-param-list=&q-signature=****************************************

Connection: close

##### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Fri, 14 Jun 2019 13:49:00 GMT

Server: tencent-cos

x-cos-request-id: NWQwM2E1Y2NfZjBhODBiMDlfOTM1YV83NDRi****

#### 案例三：创建多 AZ 存储桶

##### 请求

PUT / HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Thu, 04 Jun 2020 06:06:09 GMT

Content-Type: application/xml

Content-Length: 96

Content-MD5: R1ES/YbddhKJK/wcN+f4yg==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1591250769;1591257969&q-key-time=1591250769;1591257969&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=&q-signature=****************************************

Connection: close

<CreateBucketConfiguration>

 <BucketAZConfig>MAZ</BucketAZConfig>

</CreateBucketConfiguration>

##### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Thu, 04 Jun 2020 06:06:10 GMT

Server: tencent-cos

x-cos-request-id: NWVkODhmNTFfM2JiODJhMDlfMjg4NmFfMzA5ZmE2****

#### 案例四：创建存储桶同时添加存储桶标签

以下请求示例，用于在北京地域创建存储桶 `examplebucket-1250000000`，同时为存储桶添加两个存储桶标签 `<a,a>` 和 `<b,b>`。

##### 请求

PUT / HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

x-cos-tagging: a=a&b=b

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1667446950;1668447000&q-key-time=1667446950;1668447000&q-url-param-list=&q-header-list=host;x-cos-tagging&q-signature=****************************************

##### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: keep-alive

Date: Thu, 03 Nov 2022 03:43:30 GMT

Server: tencent-cos

x-cos-request-id: NjM2MzM4ZTJfZDRiNTE0M********
