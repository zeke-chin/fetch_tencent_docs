<!-- source: https://cloud.tencent.com/document/product/436/8276 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:39:20+08:00 -->

# GET Bucket policy

最近更新时间：2025-09-01 17:29:31


## 功能描述

GET Bucket policy 请求可以向 Bucket 读取权限策略。

## 授权说明

授权策略中 action 设置为 cos:GetBucketPolicy 。查看所有 [action](https://cloud.tencent.com/document/product/598/69901)。

## 请求

#### 请求示例

GET /?policy HTTP/1.1

Host:<BucketName-APPID>.cos.<Region>.myqcloud.com

Date:date

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

响应返回权限策略。

{

 "Statement": [

 {

 "Principal": {

 "qcs": [

 "qcs::cam::uin/100000000001:uin/100000000001"

 ]

 },

 "Effect": "allow",

 "Action": [

 "name/cos:GetBucket"

 ],

 "Resource": [

 "qcs::cos:ap-guangzhou:uid/1250000000:examplebucket-1250000000/*"

 ],

 "Sid":"policy01"

 }

 ],

 "version": "2.0"

}

具体的节点描述如下：

名称 父节点 描述 类型
Sid 无 策略 Id。String

关于访问策略中的更多元素介绍，请参见 [访问策略语言概述](https://cloud.tencent.com/document/product/436/18023)。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

GET /?policy HTTP/1.1

Host:examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com

Authorization:q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1484814099;32557710099&q-key-time=1484814099;32557710099&q-header-list=host&q-url-param-list=policy&q-signature=****************************************

#### 响应

HTTP/1.1 200 OK

Content-Type: application/json

Content-Length: 237

Connection: keep-alive

Date: Thu Jan 19 16:21:46 2017

Server: tencent-cos

x-cos-request-id: NTg4MDc3MWFfOWIxZjRlXzZmNDVf****

{

 "Statement": [

 {

 "Principal": {

 "qcs": [

 "qcs::cam::uin/100000000001:uin/100000000001"

 ]

 },

 "Effect": "allow",

 "Action": [

 "name/cos:GetBucket"

 ],

 "Resource": [

 "qcs::cos:ap-guangzhou:uid/1250000000:examplebucket-1250000000/*"

 ],

 "Sid":"policy01"

 }

 ],

 "version": "2.0"

}
