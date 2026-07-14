<!-- source: https://cloud.tencent.com/document/product/436/57422 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:12:47+08:00 -->

# 对象访问 URL

最近更新时间：2025-05-21 18:53:13


## 简介

本文介绍对象存储 COS 通过小程序 SDK 实现生成对象访问 URL 的示例代码和描述。

## 注意事项

2024年1月1日后创建的桶 [不支持使用默认域名在浏览器预览文件](https://cloud.tencent.com/document/product/436/96243)，建议您配置自定义域名，详情请参见 [存储桶切换自定义域名](https://cloud.tencent.com/document/product/436/102509)。

如果您的文件是**私有读**权限，那么本接口生成的 URL 不能直接用于访问资源。

此接口是单纯的客户端逻辑，因此不需要特殊授权。

## 功能说明

获取对象访问的 URL，该接口不会判断对象是否真实存在。

**说明：**

如何使生成的对象 URL 在浏览器中打开是预览，而不是下载：在获取的 url 后拼接参数 response-content-disposition=inline。

如何使生成的对象 URL 在浏览器中打开是下载，而不是预览：在获取的 url 后拼接参数 response-content-disposition=attachment。

下载时如何重命名文件：在获取的 URL 后拼接参数 filename，例如 response-content-disposition=attachment;filename=自定义文件名。

若使用临时密钥生成预签名 URL，请确保申请临时密钥的 action 添加了 `"name/cos:GetObject"` 权限。

## 前期准备

开始使用前，确保您已经完成了 [白名单配置](https://cloud.tencent.com/document/product/436/31953#.E5.B0.8F.E7.A8.8B.E5.BA.8F.E5.9F.9F.E5.90.8D.E7.99.BD.E5.90.8D.E5.8D.95.E9.85.8D.E7.BD.AE) 并完成了 [SDK 初始化](https://cloud.tencent.com/document/product/436/31953)。

## 使用案例

获取可在小程序下载的 url：

cos.getObjectUrl(

 {

 Bucket: 'examplebucket-1250000000', // 填入您自己的存储桶，必须字段

 Region: 'COS_REGION', // 存储桶所在地域，例如 ap-beijing，必须字段

 Key: '头像.jpg', // 存储在桶里的对象键（例如1.jpg，a/b/test.txt），支持中文，必须字段

 Sign: true, // 获取带签名的对象 URL

 },

 function (err, data) {

 if (err) return console.log(err);

 /* url为对象访问 url */

 var url = data.Url;

 /* 复制 downloadUrl 的值到浏览器打开会自动触发下载 */

 var downloadUrl =

 data.Url +

 (data.Url.indexOf('?') > -1 ? '&' : '?') +

 'response-content-disposition=attachment;filename=图片.jpg'; // 补充强制下载的参数并重命名下载后的文件

 }

);

#### 参数说明

参数名 参数描述 类型 是否必填
Bucket 存储桶的名称，命名规则为 BucketName-APPID，此处填写的存储桶名称必须为此格式 String 是
Region 存储桶所在地域，枚举值请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)String 是
Key 对象键（Object 的名称），对象在存储桶中的唯一标识，详情请参见 [对象概述](https://cloud.tencent.com/document/product/436/13324)String 是
Sign 是否返回带有签名的 Url，默认为 true，当对象为私有读时，获取到不带签名的 url 依然没有权限访问 Boolean 否
Protocol 可选填为 `http:` 或 `https:`，默认为 `http:`（带冒号）String 否
Domain 存储桶访问域名，默认为 {BucketName-APPID}.cos.{Region}.myqcloud.com String 否
Method 操作方法，例如 GET，POST，DELETE，HEAD 等 HTTP 方法，默认为 GET String 否
Query 签名中要签入的请求参数，{key: 'val'} 的格式 Object 否
Headers 签名中要签入的请求头部，{key: 'val'} 的格式 Object 否
Expires 签名几秒后失效，默认为 900 秒

**注意：**

因临时密钥和签名均有有效期，若用临时密钥生成预签名 URL，其实际有效期是临时密钥有效期和签名有效期中较短的那个时长。Number 否

#### 回调函数说明

function(err, data) { ... }

参数名 参数描述 类型
err 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功则为空，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档 Object
data 请求成功时返回的对象，如果请求发生错误，则为空 Object
- Url 计算得到的 Url String
