<!-- source: https://cloud.tencent.com/document/product/436/7749 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:41:37+08:00 -->

# PUT Object

最近更新时间：2026-06-11 16:51:03


## 功能描述

PUT Object 接口请求可以将本地的对象（Object）上传至指定存储桶中，该 API 的请求者需要对存储桶有写入权限。若无权限请参见 [设置访问权限](https://cloud.tencent.com/document/product/436/13315)。如想以网页表单（HTML Form）的形式上传至指定存储桶中，请使用 [POST Object](https://cloud.tencent.com/document/product/436/14690)。

## 注意事项

PUT Object 接口最大支持上传5GB文件。如需上传大于5GB的文件，请使用 [分块上传](https://cloud.tencent.com/document/product/436/14112) 的 API 接口。

请求头的 Content-Length 值小于实际请求体（body）中传输的数据长度，COS 仍将成功创建文件，但对象大小只等于 Content-Length 中定义的大小，其他数据将被丢弃。

对象存储中没有文件夹和目录的概念，将对象上传到指定的文件夹或路径，通过`/`实现。

对象键设置为 doc/picture.png，表示将 picture.png 对象上传到 doc 文件夹。

对象键设置为 doc/，表示创建一个名为 doc 的文件夹。更多说明请参见 [文件夹和目录](https://cloud.tencent.com/document/product/436/13324#.E6.96.87.E4.BB.B6.E5.A4.B9.E5.92.8C.E7.9B.AE.E5.BD.95)。

如果试图添加已存在的同名对象，则新上传的对象将覆盖原来的对象，成功时返回200 OK。若要求不覆盖之前版本，需打开版本控制，详情请参见 [版本控制](https://cloud.tencent.com/document/product/436/19881)。

启用存储桶版本控制 ：上传对象时，对象存储将自动为要添加的对象生成唯一的版本 ID，且响应头部在响应中返回 x-cos-version-id 标识。

暂停存储桶版本控制 ：上传对象时，对象存储始终将 null 用作在存储桶中的对象版本 ID，且响应头部在响应中不返回 x-cos-version-id 标识。

## 授权说明

在您进行 [授权策略](https://cloud.tencent.com/document/product/436/31923) 时，action 需要设置为 `cos:PutObject`，示例如下。

{

 "version": "2.0",

 "statement": [

 {

 "action": [

 "name/cos:PutObject"

 ],

 "effect": "allow",

 "resource": [

 "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/*"

 ]

 }

 ]

}

对象存储的更多 action，请参见 [支持 CAM 的业务接口](https://cloud.tencent.com/document/product/598/69901)。

## 请求

### 请求语法

PUT /<ObjectKey> HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Content-Type: Content Type

Content-Length: Content Length

Content-MD5: MD5

Authorization: Auth String

[Object Content]

**说明：**

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参见 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；<Region> 为 COS 的可用地域，可参见 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求参数

此接口无请求参数。

### 请求头

此接口除使用公共请求头部外，还支持以下请求头部，了解公共请求头部详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 常规请求头

名称 描述 类型 是否必选
Cache-Control RFC 2616中定义的缓存指令，将作为对象元数据保存。string 否
Content-Disposition RFC 2616中定义的文件名称，将作为对象元数据保存。

例如：

inline：直接预览文件内容。

attachment：以原文件名的形式下载到浏览器指定路径。

attachment; filename="FileName"：以自定义文件名的形式下载到浏览器指定路径。FileName 用于自定义下载后的文件名称，例如 example.jpg。string 否
Content-Encoding RFC 2616中定义的编码格式，将作为对象元数据保存。string 否
Content-Type RFC 2616中定义的 HTTP 请求内容类型（MIME），此头部用于描述待上传对象的内容类型，将作为对象元数据保存。

例如：application/xml 或 image/jpeg。string 是
Expires RFC 2616中定义的缓存失效时间，是绝对日期和时间，将作为对象元数据保存。string 否
Transfer-Encoding RFC 2616中定义的传输编码格式，如果希望在上传时分块传输，则指定 Transfer-Encoding: chunked 请求头部，不能指定 Content-Length 请求头部。string 否

#### **专用请求头**

在上传对象时可以通过指定下列请求头部来设置对象的元数据、存储类型、流量控制、标签：

名称 描述 类型 是否必选
x-cos-meta-[自定义后缀]用户自定义元数据头部。例如 `x-cos-meta-test: test metadata`。

**注意：**

用户自定义元数据头部固定格式为 `x-cos-meta-[自定义后缀]`，其中自定义后缀支持减号（-）、数字、英文（a～z）。英文字符的大写字母会被转成小写字母，不支持下划线（_）在内的其他字符。

用户自定义元数据头部没有数量限制，单条大小限制2KB，所有 `x-cos-meta-[自定义后缀]` 头部的总大小不超过4KB。string 否
x-cos-storage-class 对象存储类型，默认值为 STANDARD。

参考值有：

STANDARD：标准存储

STANDARD_IA：低频存储

ARCHIVE：归档存储

DEEP_ARCHIVE：深度归档存储

MAZ_STANDARD：标准存储（多 AZ）

MAZ_STANDARD_IA：低频存储（多 AZ）

MAZ_ARCHIVE：归档存储（多 AZ）

INTELLIGENT_TIERING：智能分层存储

MAZ_INTELLIGENT_TIERING：智能分层存储（多 AZ）

**注意：**

部分存储类型仅对特定地域开放，请检查您当前存储桶所属地域是否适用，详情请参见 [存储类型概述](https://cloud.tencent.com/document/product/436/33417) 文档。如需指定 MAZ 存储类型，需在 [创建存储桶](https://cloud.tencent.com/document/product/436/14106) 时开启 MAZ 配置。如需指定智能分层存储类型，则需开启 [智能分层存储](https://cloud.tencent.com/document/product/436/47802) 配置。enum 否
x-cos-traffic-limit 针对本次上传进行流量控制的限速值，必须为数字，单位默认为 bit/s。限速值设置范围为819200 - 838860800，即800Kb/s - 800Mb/s，如果超出该范围将返回400错误。integer 否
x-cos-tagging 对象的标签集合，最多可设置10个标签（例如，Key1=Value1 & Key2=Value2）。标签集合中的 Key 和 Value 必须先进行 URL 编码。string 否
x-cos-forbid-overwrite**针对未开启版本控制的存储桶**，上传文件时，用于指定上传操作时是否禁止覆盖同名对象：

不携带 x-cos-forbid-overwrite 头部或指定为 false 时，默认覆盖同名 Object。

指定 x-cos-forbid-overwrite 为 true 时，表示禁止覆盖同名 Object。

**注意：**

当存储桶的版本控制是开启状态时，x-cos-forbid-overwrite 请求头部设置无效，即允许覆盖同名对象。string 否

#### **访问控制列表（ACL）请求头**

在上传对象时可以通过指定下列请求头部来设置对象的访问权限：

名称 描述 类型 是否必选
x-cos-acl 定义对象的访问控制列表（ACL）属性。默认为 default。枚举值请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E9.A2.84.E8.AE.BE.E7.9A.84-acl) 文档中对象的预设 ACL 部分。

参考值有：

default：继承权限

private：私有读写

public-read ：公有读私有写

**注意：**

如果您不需要进行对象 ACL 控制，请设置为 default 或者此项不进行设置，默认继承存储桶权限。enum 否
x-cos-grant-read 赋予被授权者读取对象的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 `id="100000000001",id="100000000002"`。string 否
x-cos-grant-read-acp 赋予被授权者读取对象的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 `id="100000000001",id="100000000002"`。string 否
x-cos-grant-write-acp 赋予被授权者写入对象的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 `id="100000000001",id="100000000002"`。string 否
x-cos-grant-full-control 赋予被授权者操作对象的所有权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如 `id="100000000001",id="100000000002"`。string 否

#### **服务端加密（SSE）请求头**

在上传对象时可以通过指定 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7728#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8) 来设置服务端加密。不设置默认为不加密。

### 请求体

此接口请求的请求体为对象（文件）内容。

## 响应

### 响应头

此接口除返回公共响应头部外，还返回以下响应头部，了解公共响应头部详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### **版本控制相关头部**

在启用版本控制的存储桶中上传对象，将返回下列响应头部。设置版本控制权限，详情请参见 [版本控制](https://cloud.tencent.com/document/product/436/19881)。

名称 描述 类型
x-cos-version-id 对象的版本 ID。string

#### **服务端加密（SSE）相关头部**

如果在上传对象时使用了服务端加密，则此接口将返回服务端加密专用头部，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7729#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

### 响应体

此接口响应体为空。

## 使用案例

**注意：**

API explorer 中会将常用且有功能的请求头部作为输入参数使用，使用时请留意。

### 案例一：简单案例（未启用版本控制）

#### 请求

PUT /exampleobject HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Fri, 10 Apr 2020 09:35:05 GMT

Content-Type: image/jpeg

Content-Length: 16

Content-MD5: 7o3pGNBWQBRbGPcPTDqmAg==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1586511305;1586518505&q-key-time=1586511305;1586518505&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=&q-signature=****************************************

Connection: close

[Object Content]

#### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Fri, 10 Apr 2020 09:35:05 GMT

ETag: "ee8de918d05640145b18f70f4c3aa602"

Server: tencent-cos

x-cos-hash-crc64ecma: 16749565679157681890

x-cos-request-id: NWU5MDNkYzlfNjRiODJhMDlfMzFmYzhfMTFm****

### 案例二：使用请求头部指定元数据和 ACL

当需要设定对象的元数据或 [控制访问权限](https://cloud.tencent.com/document/product/436/30749) 时，可通过设置对应的请求头进行控制。

#### 请求

PUT /exampleobject HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Fri, 10 Apr 2020 09:35:28 GMT

Content-Type: image/jpeg

Cache-Control: max-age=86400

Content-Disposition: attachment; filename=example.jpg

x-cos-meta-example-field: example-value

x-cos-acl: public-read

Content-Length: 16

Content-MD5: 7o3pGNBWQBRbGPcPTDqmAg==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1586511328;1586518528&q-key-time=1586511328;1586518528&q-header-list=cache-control;content-disposition;content-length;content-md5;content-type;date;host;x-cos-acl;x-cos-meta-example-field&q-url-param-list=&q-signature=****************************************

Connection: close

[Object Content]

#### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Fri, 10 Apr 2020 09:35:28 GMT

ETag: "ee8de918d05640145b18f70f4c3aa602"

Server: tencent-cos

x-cos-hash-crc64ecma: 16749565679157681890

x-cos-request-id: NWU5MDNkZTBfZjhjMDBiMDlfNzdmN18xMGFi****

### 案例三：使用服务端加密 SSE-COS

当需要将对象 [服务端加密](https://cloud.tencent.com/document/product/436/18145) 时，可通过设置对应的请求头进行控制。

#### 请求

PUT /exampleobject HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Fri, 10 Apr 2020 09:35:49 GMT

Content-Type: image/jpeg

x-cos-server-side-encryption: AES256

Content-Length: 16

Content-MD5: 7o3pGNBWQBRbGPcPTDqmAg==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1586511349;1586518549&q-key-time=1586511349;1586518549&q-header-list=content-length;content-md5;content-type;date;host;x-cos-server-side-encryption&q-url-param-list=&q-signature=****************************************

[Object Content]

#### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Fri, 10 Apr 2020 09:35:49 GMT

ETag: "ee8de918d05640145b18f70f4c3aa602"

Server: tencent-cos

x-cos-hash-crc64ecma: 16749565679157681890

x-cos-request-id: NWU5MDNkZjVfYzVjNzJhMDlfMjVhNzNfMWMy****

x-cos-server-side-encryption: AES256

### 案例四：使用服务端加密 SSE-KMS

#### 请求

PUT /exampleobject HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Fri, 10 Apr 2020 09:36:00 GMT

Content-Type: image/jpeg

x-cos-server-side-encryption: cos/kms

x-cos-server-side-encryption-cos-kms-key-id: 48ba38aa-26c5-11ea-855c-52540085****

x-cos-server-side-encryption-context: eyJhdXRob3IiOiJmeXNudGlhbiIsImNvbXBhbnkiOiJUZW5jZW50In0=

Content-Length: 16

Content-MD5: 7o3pGNBWQBRbGPcPTDqmAg==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1586511360;1586518560&q-key-time=1586511360;1586518560&q-header-list=content-length;content-md5;content-type;date;host;x-cos-server-side-encryption;x-cos-server-side-encryption-context;x-cos-server-side-encryption-cos-kms-key-id&q-url-param-list=&q-signature=****************************************

Connection: close

[Object Content]

#### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Fri, 10 Apr 2020 09:36:01 GMT

ETag: "840af7c921f4b3230049af8663145bd0"

Server: tencent-cos

x-cos-hash-crc64ecma: 16749565679157681890

x-cos-request-id: NWU5MDNlMDFfOThjMjJhMDlfMjhhMl8xNTlm****

x-cos-server-side-encryption: cos/kms

x-cos-server-side-encryption-cos-kms-key-id: 48ba38aa-26c5-11ea-855c-52540085****

### 案例五：使用服务端加密 SSE-C

#### 请求

PUT /exampleobject HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Fri, 10 Apr 2020 09:36:12 GMT

Content-Type: image/jpeg

x-cos-server-side-encryption-customer-algorithm: AES256

x-cos-server-side-encryption-customer-key: MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=

x-cos-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==

Content-Length: 16

Content-MD5: 7o3pGNBWQBRbGPcPTDqmAg==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1586511372;1586518572&q-key-time=1586511372;1586518572&q-header-list=content-length;content-md5;content-type;date;host;x-cos-server-side-encryption-customer-algorithm;x-cos-server-side-encryption-customer-key;x-cos-server-side-encryption-customer-key-md5&q-url-param-list=&q-signature=****************************************

Connection: close

[Object Content]

#### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Fri, 10 Apr 2020 09:36:13 GMT

ETag: "582d9105f71525f3c161984bc005efb5"

Server: tencent-cos

x-cos-hash-crc64ecma: 16749565679157681890

x-cos-request-id: NWU5MDNlMGNfZTFjODJhMDlfMzVlMDFfZTk1****

x-cos-server-side-encryption-customer-algorithm: AES256

x-cos-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==

### 案例六：启用版本控制

#### 请求

PUT /exampleobject HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Fri, 10 Apr 2020 09:36:34 GMT

Content-Type: image/jpeg

Content-Length: 16

Content-MD5: 7o3pGNBWQBRbGPcPTDqmAg==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1586511394;1586518594&q-key-time=1586511394;1586518594&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=&q-signature=****************************************

Connection: close

[Object Content]

#### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Fri, 10 Apr 2020 09:36:35 GMT

ETag: "ee8de918d05640145b18f70f4c3aa602"

Server: tencent-cos

x-cos-hash-crc64ecma: 16749565679157681890

x-cos-request-id: NWU5MDNlMjNfMThiODJhMDlfNGQ1OF8xMWY4****

x-cos-version-id: MTg0NDUxNTc1NjIzMTQ1MDAwODg

### 案例七：暂停版本控制

#### 请求

PUT /exampleobject HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Fri, 10 Apr 2020 09:37:07 GMT

Content-Type: image/jpeg

Content-Length: 16

Content-MD5: 7o3pGNBWQBRbGPcPTDqmAg==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1586511427;1586518627&q-key-time=1586511427;1586518627&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=&q-signature=****************************************

Connection: close

[Object Content]

#### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Fri, 10 Apr 2020 09:37:07 GMT

ETag: "ee8de918d05640145b18f70f4c3aa602"

Server: tencent-cos

x-cos-hash-crc64ecma: 16749565679157681890

x-cos-request-id: NWU5MDNlNDNfZTZjNzJhMDlfMmYwMDlfMTVi****

### 案例八：使用 chunked 传输编码分块传输

本案例请求中使用 Transfer-Encoding: chunked 编码，案例描述的是 HTTP 请求中的原始数据，在使用过程中根据不同语言和库将有不同的调用方法，请开发者查阅语言和库的相关文档。

#### 请求

PUT /exampleobject HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Thu, 08 Aug 2019 09:15:29 GMT

Content-Type: text/plain

Transfer-Encoding: chunked

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1565255729;1565262929&q-key-time=1565255729;1565262929&q-header-list=content-type;date;host;transfer-encoding&q-url-param-list=&q-signature=****************************************

11

[Chunked Content]

b

[2nd chunk]

b

[3rd chunk]

b

[4th chunk]

0

#### 响应

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Thu, 08 Aug 2019 09:15:29 GMT

ETag: "aa488bb80185a6be87f4a7b936a80752"

Server: tencent-cos

x-cos-hash-crc64ecma: 7188322482464764960

x-cos-request-id: NWQ0YmU4MzFfNzFiNDBiMDlfMWJhYTlfMTY2Njll****

### 案例九：使用 x-cos-forbid-overwrite 防覆盖头部

本案例在上传对象请求中携带了 x-cos-forbid-overwrite 头部且值指定为 true，代表禁止覆盖同名对象。

#### 请求

PUT /exampleobject HTTP/1.1

x-cos-forbid-overwrite: true

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Fri, 10 Apr 2020 09:37:07 GMT

Content-Type: image/jpeg

Content-Length: 16

Content-MD5: 7o3pGNBWQBRbGPcPTDqmAg==

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1586511427;1586518627&q-key-time=1586511427;1586518627&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=&q-signature=****************************************

Connection: close

[Object Content]

#### 响应

如果存储桶中不存在同名对象，则上传对象成功。

HTTP/1.1 200 OK

Content-Length: 0

Connection: close

Date: Fri, 10 Apr 2020 09:37:07 GMT

ETag: "aa488bb80185a6be87f4a7b936a80752"

Server: tencent-cos

x-cos-hash-crc64ecma: 7188322482464764960

x-cos-request-id: NWQ0YmU4MzFfNzFiNDBiMDlfMWJhYTlfMTY2Njll****

如果存储桶中存在同名对象，则会返回报错。

HTTP/1.1 409 Conflict

Content-Length: 417

Content-Type: application/xml

Date: Fri, 10 Apr 2020 09:37:07 GMT

Server: tencent-cos

x-cos-request-id: NjgyZDUwYWVfYzkyZGI1MDlfZDki*****

x-cos-trace-id: OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxO*******

<?xml version='1.0' encoding='utf-8' ?>

<Error>

 <Code>FileAlreadyExists</Code>

 <Message>File already exists.</Message>

 <Resource>/exampleobject</Resource>

 <RequestId>NjgyZDUwYWVfYzkyZGI1MDlfZDk3NV8*****</RequestId>

 <TraceId>OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWV****</TraceId>

</Error>

## 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 附录：PUT Object 接口对应各语言的 SDK

SDK 文档链接
Android SDK[Android SDK 上传对象](https://cloud.tencent.com/document/product/436/46415)
C SDK[C SDK 上传对象](https://cloud.tencent.com/document/product/436/65655)
C++ SDK[C++ SDK 上传对象](https://cloud.tencent.com/document/product/436/35161)
.NET(C#) SDK[.NET(C#) 上传对象](https://cloud.tencent.com/document/product/436/47231)
Flutter SDK[Flutter SDK 上传对象](https://cloud.tencent.com/document/product/436/86287)
Go SDK[Go SDK 上传对象](https://cloud.tencent.com/document/product/436/65644)
iOS SDK[iOS SDK 上传对象](https://cloud.tencent.com/document/product/436/46381)
Java SDK[Java SDK 上传对象](https://cloud.tencent.com/document/product/436/65935)
JavaScript SDK[JavaScript SDK 上传对象](https://cloud.tencent.com/document/product/436/64960)
Node.js SDK[Node.js SDK 上传对象](https://cloud.tencent.com/document/product/436/64980)
PHP SDK[PHP SDK 上传对象](https://cloud.tencent.com/document/product/436/64283)
Python SDK[Python SDK 上传对象](https://cloud.tencent.com/document/product/436/65820)
React Native SDK[React Native 上传对象](https://cloud.tencent.com/document/product/436/86699)
小程序 SDK[小程序 SDK 上传对象](https://cloud.tencent.com/document/product/436/64991)
