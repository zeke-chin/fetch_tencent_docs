<!-- source: https://cloud.tencent.com/document/product/436/106996 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:36:31+08:00 -->

# 图片文字识别（OCR）

最近更新时间：2024-06-06 16:01:03


## 简介

本文档提供关于图片文字识别(OCR)的相关 API 概览以及 SDK 示例代码。

**注意：**

COS 小程序 SDK 版本需要大于等于 v1.1.1。

API 操作描述
[图片文字识别(OCR)](https://cloud.tencent.com/document/product/460/63227)通用文字识别功能（Optical Character Recognition，OCR）基于行业前沿的深度学习技术，将图片上的文字内容，智能识别为可编辑的文本，可应用于随手拍扫描、纸质文档电子化、电商广告审核等多种场景，大幅提升信息处理效率。

## 图片文字识别(OCR)

#### 功能说明

通用文字识别功能（Optical Character Recognition，OCR）基于行业前沿的深度学习技术，将图片上的文字内容，智能识别为可编辑的文本，可应用于随手拍扫描、纸质文档电子化、电商广告审核等多种场景，大幅提升信息处理效率。

#### 使用示例

function cOSOCR() {

 // sdk引入以及初始化请参考：https://cloud.tencent.com/document/product/436/31953

 const config = {

 // 需要替换成您自己的存储桶信息

 Bucket: 'examplebucket-1250000000', // 存储桶，必须字段

 Region: 'COS_REGION', // 存储桶所在地域，必须字段 如 ap-beijing

 };

 cos.request(

 {

 Bucket: config.Bucket,

 Region: config.Region,

 Method: 'GET', // 固定值，必须

 Key: 'ci/0.jpg', // 对象文件名，例如：folder/document.jpg；与detect-url二选一传递

 Query: {

 // 数据万象处理能力，图片文字识别固定为OCR;是否必传：是

 'ci-process': 'OCR',

 // 您可以通过填写 detect-url 处理任意公网可访问的图片链接。不填写 detect-url 时，后台会默认处理 Key ，填写了 detect-url 时，后台会处理 detect-url 链接，无需再填写 Key。detect-url 示例：http://www.example.com/abc.jpg ，需要进行 UrlEncode，处理后为http%25253A%25252F%25252Fwww.example.com%25252Fabc.jpg;是否必传：否

 // 'detect-url': '',

 // ocr的识别类型，有效值为general，accurate，efficient，fast，handwriting。general表示通用印刷体识别；accurate表示印刷体高精度版；efficient表示印刷体精简版；fast表示印刷体高速版；handwriting表示手写体识别。默认值为general。;是否必传：否

 type: 'general',

 // type值为general时有效，表示识别语言类型。支持自动识别语言类型，同时支持自选语言种类，默认中英文混合(zh)，各种语言均支持与英文混合的文字识别。可选值：zh：中英混合zh_rare：支持英文、数字、中文生僻字、繁体字，特殊符号等auto：自动mix：混合语种jap：日语kor：韩语spa：西班牙语fre：法语ger：德语por：葡萄牙语vie：越语may：马来语rus：俄语ita：意大利语hol：荷兰语swe：瑞典语fin：芬兰语dan：丹麦语nor：挪威语hun：匈牙利语tha：泰语hi：印地语ara：阿拉伯语;是否必传：否

 'language-type': 'zh',

 // type值为general，fast时有效，表示是否开启PDF识别，有效值为true和false，默认值为false，开启后可同时支持图片和PDF的识别。;是否必传：否

 ispdf: false,

 // type值为general，fast时有效，表示需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且ispdf参数值为true时有效，默认值为1。;是否必传：否

 // 'pdf-pagenumber': 0,

 // type值为general，accurate时有效，表示识别后是否需要返回单字信息，有效值为true和false，默认为false;是否必传：否

 isword: false,

 // type值为handwriting时有效，表示是否开启单字的四点定位坐标输出，有效值为true和false，默认值为false。;是否必传：否

 'enable-word-polygon': false,

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

 }

 );

}

cOSOCR();

#### 参数说明

cos.request 方法参数说明：

参数名称 参数描述 类型 是否必填
Bucket 存储桶的名称，命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式 String 是
Region 存储桶所在地域，枚举值请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224 "https://cloud.tencent.com/document/product/436/6224")String 是
Method 固定值：GET String 是
Key 对象文件名，例如：folder/document.jpg String 是
Query 其他请求参数 Container 是

Query 参数说明：

参数名称 参数描述 类型 是否必填
ci-process 数据万象处理能力，图片文字识别固定为 OCR String 是
detect-url 您可以通过填写 detect-url 处理任意公网可访问的图片链接。不填写 detect-url 时，后台会默认处理 Key ，填写了 detect-url 时，后台会处理 detect-url 链接。

detect-url 示例：`http://www.example.com/abc.jpg` ，需要进行 UrlEncode，处理后为`http%25253A%25252F%25252Fwww.example.com%25252Fabc.jpg`String 否
type OCR的识别类型，默认值为general。有效值有：

general：表示通用印刷体识别。

accurate：表示印刷体高精度版。

efficient：表示印刷体精简版。

fast：表示印刷体高速版。

handwriting：表示手写体识别。String 否
languageType type值为general时有效，表示识别语言类型。支持自动识别语言类型，同时支持自选语言种类，默认中英文混合(zh)。

各种语言均支持与英文混合的文字识别。可选值有：

zh：中英混合

zh_rare：支持英文、数字、中文生僻字、繁体字，特殊符号等

auto：自动

mix：混合语种

jap：日语

kor：韩语

spa：西班牙语

fre：法语

ger：德语

por：葡萄牙语

vie：越语

may：马来语

rus：俄语

ita：意大利语

hol：荷兰语

swe：瑞典语

fin：芬兰语

dan：丹麦语

nor：挪威语

hun：匈牙利语

tha：泰语

hi：印地语

ara：阿拉伯语 String 否
ispdf type 值为 general，fast 时有效，表示是否开启 PDF 识别，有效值为 true 和 false，默认值为 false，开启后可同时支持图片和 PDF 的识别。boolean 否
pdfPagenumber type 值为 general，fast 时有效，表示需要识别的 PDF 页面的对应页码，仅支持 PDF 单页识别，当上传文件为 PDF 且 ispdf 参数值为 true 时有效，默认值为1。Integer 否
isword type 值为 general，accurate 时有效，表示识别后是否需要返回单字信息，有效值为 true 和false，默认为 false。boolean 否
enableWordPolygon type 值为 handwriting 时有效，表示是否开启单字的四点定位坐标输出，有效值为 true 和false，默认值为 false。boolean 否

#### 回调函数说明

function(err, data) { ... }

参数名称 参数描述 类型
err 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功则为空，更多详情请参见 [错误码](https://cloud.tencent.com/document/product/460/8523 "https://cloud.tencent.com/document/product/460/8523")Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
data 请求成功时返回的对象，如果请求发生错误，则为空 Object
- statusCode 请求返回的 HTTP 状态码，例如200、403、404等 Number
- headers 请求返回的头部信息 Object
- Response 响应结果，详情请参见[图片文字识别(OCR)](https://cloud.tencent.com/document/product/460/63227#.E5.93.8D.E5.BA.94)Object

#### 相关链接

[API 文档](https://cloud.tencent.com/document/product/460/63227 "https://cloud.tencent.com/document/product/460/63227")[功能指南](https://cloud.tencent.com/document/product/460/96719 "https://cloud.tencent.com/document/product/460/96719")
