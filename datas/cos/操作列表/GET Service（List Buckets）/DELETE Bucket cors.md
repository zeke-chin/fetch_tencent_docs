<!-- source: https://cloud.tencent.com/document/product/436/8283 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:39:05+08:00 -->

# DELETE Bucket cors

最近更新时间：2024-11-15 21:48:53


## 功能描述

DELETE Bucket cors 请求用于删除存储桶的跨域资源共享（CORS）访问控制。

## 授权说明

授权策略中 action 设置为 cos:DeleteBucketCORS 。查看所有 [action](https://cloud.tencent.com/document/product/598/69901)。

## 请求

#### 请求示例

DELETE /?cors HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Authorization: Auth String

**说明**

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，详情请参见 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；<Region> 为 COS 的可用地域，详情请参见 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

此接口响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

DELETE /?cors HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Thu, 09 Jul 2020 11:52:50 GMT

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1594295570;1594302770&q-key-time=1594295570;1594302770&q-header-list=date;host&q-url-param-list=cors&q-signature=****************************************

Connection: close

#### 响应

HTTP/1.1 204 No Content

Connection: close

Date: Thu, 09 Jul 2020 11:52:50 GMT

Server: tencent-cos

x-cos-request-id: NWYwNzA1MTJfNjRiODJhMDlfMWMyMzlfMWMyNzhl****

x-cos-trace-id: OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODczNTBmNjMwZmQ0MTZkMjg0NjlkNTYyNmY4ZTRkZTk0NzJmZTI0ZmJhYTZmZjYyNmU5ZGNlZDI5YjkyODkwYjNhYjJkOWQzYWJlOGRjYzY5N2ZlMGJhZjdlNDA4YjkzODc=

Content-Length: 0
