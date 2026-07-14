<!-- source: https://cloud.tencent.com/document/product/436/8282 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:39:15+08:00 -->

# PUT Bucket policy

最近更新时间：2025-01-20 18:52:32


## 功能描述

PUT Bucket policy 请求可以向 Bucket 写入权限策略。当存储桶已存在权限策略时，该请求上传的策略将覆盖原有的权限策略。如果需要增量写入策略，可以先调用 [GET Bucket Policy](https://cloud.tencent.com/document/product/436/8276 "https://cloud.tencent.com/document/product/436/8276") 获取之前的策略，在之前的策略上再添加新策略，然后再调用 PUT Bucket Policy。

**注意：**

每个主账号，创建的存储桶 ACL 规则数量最多为1000条。

请求体中 Statement 的单条策略长度不得超过4095字节。

## 授权说明

授权策略中 action 设置为 cos:PutBucketPolicy 。查看所有 [action](https://cloud.tencent.com/document/product/598/69901 "https://cloud.tencent.com/document/product/598/69901")。

## 请求

#### 请求示例

PUT /?policy HTTP/1.1

Host:<BucketName-APPID>.cos.<Region>.myqcloud.com

Date: date

Content-Type:application/json

Content-MD5:MD5

Authorization: Auth String

**说明：**

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF "https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF") 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83 "https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83") 文档；<Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224 "http://cloud.tencent.com/document/product/436/6224") 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778 "https://cloud.tencent.com/document/product/436/7778") 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728 "https://cloud.tencent.com/document/product/436/7728") 文档。

#### 请求体

下面的示例表示给主账号100000000001下的子账号100000000011授权，以允许访问存储桶名为 examplebucket-1250000000 中的对象列表。关于访问策略中的元素介绍，请参见 [访问策略语言概述](https://cloud.tencent.com/document/product/436/18023 "https://cloud.tencent.com/document/product/436/18023")，以及授权策略示例请参见 [COS API 授权策略使用指引](https://cloud.tencent.com/document/product/436/31923 "https://cloud.tencent.com/document/product/436/31923")。

{

 "Statement": [

 {

 "Principal": {

 "qcs": [

 "qcs::cam::uin/100000000001:uin/100000000011"

 ]

 },

 "Effect": "allow",

 "Action": [

 "name/cos:GetBucket"

 ],

 "Resource": [

 "qcs::cos:ap-guangzhou:uid/1250000000:examplebucket-1250000000/*"

 ]

 }

 ],

 "version": "2.0"

}

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729 "https://cloud.tencent.com/document/product/436/7729") 文档。

#### 响应体

该请求的响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730 "https://cloud.tencent.com/document/product/436/7730") 文档。

## 实际案例

#### 请求

PUT /?policy HTTP/1.1

Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com

Authorization:q-sign-algorithm=sha1&q-ak= ************************************ &q-sign-time=1484813288;32557709288&q-key-time=1484813288;32557709288&q-header-list=host&q-url-param-list=policy&q-signature= ****************************************

Content-Type: application/json

Content-Length: 233

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

 ]

 }

 ],

 "version": "2.0"

}

#### 响应

HTTP/1.1 204 No Content

Content-Type: application/xml

Content-Length: 0

Connection: keep-alive

Date: Thu Jan 19 16:19:22 2017

Server: tencent-cos

x-cos-request-id: NTg4MDc2OGFfNDUyMDRlXzc3NTlf****
