<!-- source: https://cloud.tencent.com/document/product/436/19888 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:40:49+08:00 -->

# GET Bucket versioning

最近更新时间：2025-07-24 18:30:42


## 功能描述

GET Bucket versioning 接口用于实现获得存储桶的版本控制信息。

## 授权说明

[授权策略](https://cloud.tencent.com/document/product/436/31923) 中 action 设置为 cos:GetBucketVersioning 。查看所有 [action](https://cloud.tencent.com/document/product/598/69901)。

#### 细节分析

1. 获取存储桶版本控制的状态，需要有该存储桶的读权限。

2. 有三种版本控制状态：未启用版本控制、启用版本控制和暂停版本控制。

如果您从未在存储桶上启用版本控制，则响应为：

<VersioningConfiguration/>

如果您启用了存储桶的版本控制功能，则响应为：

<VersioningConfiguration>

 <Status>Enabled</Status>

</VersioningConfiguration>

如果您暂停了存储桶的版本控制功能，则响应为：

<VersioningConfiguration>

 <Status>Suspended</Status>

</VersioningConfiguration>

## 请求

#### 请求示例

GET /?versioning HTTP 1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT date

Authorization: Auth String

**说明：**

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，详情请参见 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；<Region> 为 COS 的可用地域，详情请参见 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

<VersioningConfiguration>

 <Status>Enabled</Status>

</VersioningConfiguration>

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型
VersioningConfiguration 无 说明版本控制的具体信息 Container
Status VersioningConfiguration 说明版本控制的状态，枚举值：Suspended（暂停版本控制）、Enabled（启用版本控制）Enum

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

GET /?versioning HTTP/1.1

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

Date: Wed, 23 Aug 2017 08:15:16 GMT

Server: tencent-cos

x-cos-request-id: NTk5ZDM5OTRfZDNhZDM1MGFfMjYyMTFfZmU3****

<?xml version='1.0' encoding='utf-8' ?>

<VersioningConfiguration>

 <Status>Enabled</Status>

</VersioningConfiguration>
