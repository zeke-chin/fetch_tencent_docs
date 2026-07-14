<!-- source: https://cloud.tencent.com/document/product/436/107029 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:37:53+08:00 -->

# 文档转 HTML

最近更新时间：2024-11-19 10:06:53


## 简介

本文档提供关于文档转 HTML的相关 API 概览以及 SDK 示例代码。

**注意：**

COS 小程序 SDK 版本需要大于等于 v1.1.1。

API 操作描述
[文档转html同步请求](https://cloud.tencent.com/document/product/460/52518 "https://cloud.tencent.com/document/product/460/52518")文档转 HTML 功能支持对多种文档类型的文件生成 HTML 格式预览，满足 PC、App 等多个用户端的文档在线浏览需求，适用于在线教育、企业 OA、在线知识库、网盘文档预览等业务场景。

## 文档转 html 同步请求

#### 功能说明

文档转 HTML 功能支持对多种文档类型的文件生成 HTML 格式预览，满足 PC、App 等多个用户端的文档在线浏览需求，适用于在线教育、企业 OA、在线知识库、网盘文档预览等业务场景。

#### 使用示例

function getDocHtmlPreviewUrl() {

 // sdk引入以及初始化请参考：https://cloud.tencent.com/document/product/436/31953

 const config = {

 // 需要替换成您自己的存储桶信息

 Bucket: 'examplebucket-1250000000', // 存储桶，必须字段

 Region: 'COS_REGION', // 存储桶所在地域，必须字段 如 ap-beijing

 };

 const ObjectKey = "test.docx";

 const key = `${ObjectKey}` // ObjectKey:{ObjectKey};

 const host = `${config.Bucket}.cos.${config.Region}.myqcloud.com`;

 const url = `https://${host}/${key}`;


 cos.request(

 {

 Method: 'GET', // 固定值，必须

 Key: key, // 必须

 Url: url, // 请求的url，必须

 Query: {

 // 数据万象处理能力，文档 HTML 预览固定为 doc-preview;是否必传：是

 "ci-process": "doc-preview",

 // 转换输出目标文件类型，文档 HTML 预览固定为 html（需为小写字母）;是否必传：是

 dstType: "html",

 // 是否获取预览链接。填入值为1会返回预览链接和Token信息；填入值为2只返回Token信息；不传会直接预览;是否必传：否

 'weboffice_url': 1,

 // 指定目标文件类型，支持的文件类型请见下方;是否必传：否

 srcType: "",

 // 对象下载签名，如果预览的对象为私有读时，需要传入签名，详情请参见 请求签名 文档注意：需要进行 urlencode;是否必传：否

 sign: "",

 // 是否可复制。默认为可复制，填入值为1；不可复制，填入值为0;是否必传：否

 copyable: "",

 // 自定义配置参数，json结构，需要经过 URL 安全 的 Base64 编码，默认配置为：{ commonOptions: { isShowTopArea: true, isShowHeader: true, language: "zh" }}，支持的配置参考 自定义配置项说明。htmlParams支持的特殊配置：语言切换，通过 commonOptions 的 language 参数指定预览语言，支持"zh"、"en“，默认为"zh"。;是否必传：否

 htmlParams: "",

 // 水印文字，需要经过 URL 安全 的 Base64 编码，默认为空;是否必传：否

 htmlwaterword: "",

 // 水印 RGBA（颜色和透明度），需要经过 URL 安全 的 Base64 编码，默认为：rgba(192,192,192,0.6);是否必传：否

 htmlfillstyle: "",

 // 水印文字样式，需要经过 URL 安全 的 Base64 编码，默认为：bold 20px Serif;是否必传：否

 htmlfront: "",

 // 水印文字旋转角度，0 - 360，默认315度;是否必传：否

 htmlrotate: "",

 // 水印文字水平间距，单位 px，默认为50;是否必传：否

 htmlhorizontal: "",

 // 水印文字垂直间距，单位 px，默认为100;是否必传：否

 htmlvertical: "",

 },

 },

 function (err, data) {

 if (err) {

 // 处理请求失败

 console.log(err);

 } else {

 // 处理请求成功

 console.log(data.Response);

 }

 },

 );

}

getDocHtmlPreviewUrl()

#### 参数说明

cos.request 方法参数说明：

参数名称 参数描述 类型 是否必填
Method 固定值：GET String 是
Url 请求url，固定值 String 是
Key{ObjectKey}String 是
Query 请求参数 Object 否

Query 参数说明：

参数名称 参数描述 类型 是否必填
ci-process 数据万象处理能力，文档 HTML 预览固定为 doc-preview String 是
dstType 转换输出目标文件类型，文档 HTML 预览固定为 html（需为小写字母）String 是
weboffice_url 是否获取预览链接。填入值为 1 会返回预览链接和Token信息；填入值为 2 只返回Token信息；不传会直接预览 String 否
srcType 指定目标文件类型，支持的文件类型请见下方 String 否
sign 对象下载签名，如果预览的对象为私有读时，需要传入签名，详情请参见 请求签名 文档注意：需要进行 urlencode String 否
copyable 是否可复制。默认为可复制，填入值为1；不可复制，填入值为0 String 否
htmlParams 自定义配置参数，json结构，需要经过 URL 安全 的 Base64 编码，默认配置为：{ commonOptions: { isShowTopArea: true, isShowHeader: true, language: "zh" }}，支持的配置参考 自定义配置项说明。htmlParams支持的特殊配置：语言切换，通过 commonOptions 的 language 参数指定预览语言，支持"zh"、"en"，默认为"zh"。String 否
htmlwaterword 水印文字，需要经过 URL 安全 的 Base64 编码，默认为空 String 否
htmlfillstyle 水印 RGBA（颜色和透明度），需要经过 URL 安全 的 Base64 编码，默认为：rgba(192,192,192,0.6)String 否
htmlfront 水印文字样式，需要经过 URL 安全 的 Base64 编码，默认为：bold 20px Serif String 否
htmlrotate 水印文字旋转角度，0 - 360，默认315度 String 否
htmlhorizontal 水印文字水平间距，单位 px，默认为50 String 否
htmlvertical 水印文字垂直间距，单位 px，默认为100 String 否

#### 回调函数说明

function(err, data) { ... }

参数名称 参数描述 类型
err 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功则为空，更多详情请参见 [错误码](https://cloud.tencent.com/document/product/460/8523 "https://cloud.tencent.com/document/product/460/8523")Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
data 请求成功时返回的对象，如果请求发生错误，则为空 Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
- Response 响应结果，详情请参见 [文档转html同步请求](https://cloud.tencent.com/document/product/460/52518#.E5.93.8D.E5.BA.94 "https://cloud.tencent.com/document/product/460/52518#.E5.93.8D.E5.BA.94")Object

#### 相关链接

[API 文档](https://cloud.tencent.com/document/product/460/52518 "https://cloud.tencent.com/document/product/460/52518")

[功能指南](https://cloud.tencent.com/document/product/460/47495 "https://cloud.tencent.com/document/product/460/47495")
