<!-- source: https://cloud.tencent.com/document/product/436/106784 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:40:09+08:00 -->

# DELETE BucketIntelligentTiering

最近更新时间：2025-06-11 18:13:31


## 功能描述

DELETE Bucket intelligenttiering 用于删除存储桶中的智能分层归档层及深度归档层规则，用户需提供待删除的规则名称。

**注意：**

调用该请求时，请确保具有 DeleteBucketIntelligentTiering 权限。

存储桶所有者默认拥有该权限，如您无该项权限，请先向存储桶所有者申请该项操作的权限。

## 授权说明

授权策略中 action 设置为 cos:DeleteBucketIntelligentTiering。查看所有 [action](https://cloud.tencent.com/document/product/598/69901)。

## 请求

#### 请求示例

DELETE /?intelligent-tiering&id=Id HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Authorization: Auth String

**说明：**

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；<Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

调用 DELETE Bucket intelligenttiering 需要使用规则名称参数，名称仅支持指定为非default，用于删除归档及深度归档层规则。

参数 描述 类型 是否必选
id 智能分层规则名称清单任务的名称，id设置为非 default 的字符串，表示该规则为归档层、深度归档层转换规则。String 是

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该响应体返回为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

下述请求示例展示了从存储桶`examplebucket-1250000000`中删除智能分层归档及深度归档层规则 rule1。

DELETE /?intelligent-tiering&id=rule1 HTTP/1.1

Date: Mon, 28 Aug 2018 02:53:38 GMT

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1503901499;1503901859&q-key-time=1503901499;1503901859&q-header-list=host&q-url-param-list=inventory&q-signature=****************************************

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

#### 响应

上述请求后，COS 返回 204 No Content 的响应表明已成功删除了该存储桶内的智能分层规则 rule1。

HTTP/1.1 204 No Content

Server: tencent-cos

Date: Mon, 28 Aug 2018 02:53:40 GMT

x-cos-id-2:0dfafa/DAPDIFdafdsfDdfSFFfdfKKJdafasiuKJK2

x-cos-request-id: NTlhM2I3M2JfMjQ4OGY3MGFfMWE1NF84****
