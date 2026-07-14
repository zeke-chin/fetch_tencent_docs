<!-- source: https://cloud.tencent.com/document/product/436/133863 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:35:45+08:00 -->

# Get Space Extension

最近更新时间：2026-07-09 15:06:03


## 功能描述

查询指定空间的扩展属性。

## 请求

### 请求语法

GET /<SpaceId>/?space-extension HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Authorization: Auth String

**说明：**

SpaceId: 对应 ObjectKey 一级目录，需要预先通过 PUT Object 接口上传大小为空的一级目录对象来创建对应的 SpaceId。

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 smhxxxxxxxxxxxxx-1250000000；<Region> 为可用地域，可参见 [产品概述](https://cloud.tencent.com/document/product/436/132574) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求参数

此接口无请求参数。

### 请求体

此接口无请求体。

## 响应

### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

### 响应体

请求成功，返回 **application/xml** 数据，包含 Space 的扩展属性。

<SpaceExtension>

 <IsPublicRead>false</IsPublicRead>

 <RecognizeSensitiveContent>false</RecognizeSensitiveContent>

 <SpaceTag>personal</SpaceTag>

</SpaceExtension>

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型
SpaceExtension 无 保存 Get Space Extension 结果的所有信息 Container

Container 节点 SpaceExtension 的内容：

节点名称（关键字）父节点 描述 类型
IsPublicRead SpaceExtension 是否为公有读，当空间设置为公有读时，通过 [智能媒资托管](https://cloud.tencent.com/document/product/1339) 接口请求该空间时，部分读接口无需指定访问令牌。详情请参见 [查询租户空间属性](https://cloud.tencent.com/document/product/1339/71152) 。Boolean
RecognizeSensitiveContent SpaceExtension 是否检测敏感内容 Boolean
SpaceTag SpaceExtension 空间标签 string

## 实际案例

### 请求

GET /test-space/?space-extension HTTP/1.1

Host: smhxxx-1250000000.cos.ap-chengdu.myqcloud.com

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1566302375;1566309575&q-key-time=1566302375;1566309575&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=delete&q-signature=****************************************

### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 118

Date: Tue, 20 Aug 2019 11:59:35 GMT

x-cos-request-id: NWQ1YmUwYTdfM2FiMDJhMDlfYzczN18zMGM1****

<SpaceExtension>

 <IsPublicRead>false</IsPublicRead>

 <RecognizeSensitiveContent>false</RecognizeSensitiveContent>

 <SpaceTag>personal</SpaceTag>

</SpaceExtension>
