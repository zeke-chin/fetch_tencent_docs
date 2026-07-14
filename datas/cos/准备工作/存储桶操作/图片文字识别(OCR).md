<!-- source: https://cloud.tencent.com/document/product/436/110235 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:07:48+08:00 -->

# 图片文字识别(OCR)

最近更新时间：2024-08-22 16:09:42


## 简介

本文档提供关于图片文字识别(OCR)的相关 API 概览以及 SDK 示例代码。

API 操作描述
[图片文字识别(OCR)](https://cloud.tencent.com/document/product/460/63227)通用文字识别功能（Optical Character Recognition，OCR）基于行业前沿的深度学习技术，将图片上的文字内容，智能识别为可编辑的文本，可应用于随手拍扫描、纸质文档电子化、电商广告审核等多种场景，大幅提升信息处理效率。

## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API](https://cos-android-sdk-doc-1253960454.file.myqcloud.com/)。

### 图片文字识别(OCR)

#### 功能说明

通用文字识别功能（Optical Character Recognition，OCR）基于行业前沿的深度学习技术，将图片上的文字内容，智能识别为可编辑的文本，可应用于随手拍扫描、纸质文档电子化、电商广告审核等多种场景，大幅提升信息处理效率。

**注意：**

COS Android SDK 版本需要大于等于 v5.9.32。

#### 示例代码

// 存储桶名称，格式为 BucketName-APPID

String bucket = "examplebucket-1250000000";

COSOCRRequest request = new COSOCRRequest(bucket, "folder/document.jpg");

request.detectUrl = "http://www.example.com/abc.jpg";// 设置您可以通过填写 detect-url 处理任意公网可访问的图片链接。不填写 detect-url 时，后台会默认处理 ObjectKey ，填写了 detect-url 时，后台会处理 detect-url 链接，无需再填写 ObjectKey detect-url 示例：http://www.example.com/abc.jpg

request.type = "general";// 设置ocr的识别类型，有效值为general，accurate，efficient，fast，handwriting。general表示通用印刷体识别；accurate表示印刷体高精度版；efficient表示印刷体精简版；fast表示印刷体高速版；handwriting表示手写体识别。默认值为general。

request.languageType = "auto";// 设置type值为general时有效，表示识别语言类型。支持自动识别语言类型，同时支持自选语言种类，默认中英文混合(zh)，各种语言均支持与英文混合的文字识别。可选值：zh：中英混合zh_rare：支持英文、数字、中文生僻字、繁体字，特殊符号等auto：自动mix：混合语种jap：日语kor：韩语spa：西班牙语fre：法语ger：德语por：葡萄牙语vie：越语may：马来语rus：俄语ita：意大利语hol：荷兰语swe：瑞典语fin：芬兰语dan：丹麦语nor：挪威语hun：匈牙利语tha：泰语hi：印地语ara：阿拉伯语

request.ispdf = false;// 设置type值为general，fast时有效，表示是否开启PDF识别，有效值为true和false，默认值为false，开启后可同时支持图片和PDF的识别。

request.pdfPagenumber = 1;// 设置type值为general，fast时有效，表示需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且ispdf参数值为true时有效，默认值为1。

request.isword = false;// 设置type值为general，accurate时有效，表示识别后是否需要返回单字信息，有效值为true和false，默认为false

request.enableWordPolygon = false;// 设置type值为handwriting时有效，表示是否开启单字的四点定位坐标输出，有效值为true和false，默认值为false。

cosXmlService.cOSOCRAsync(request, new CosXmlResultListener() {

 @Override

 public void onSuccess(CosXmlRequest request, CosXmlResult cosResult) {

 // result 图片文字识别(OCR）的结果

 // 详细字段请查看api文档或者SDK源码

 COSOCRResult result = (COSOCRResult) cosResult;

 }

 @Override

 public void onFail(CosXmlRequest request, CosXmlClientException clientException, CosXmlServiceException serviceException) {

 if (clientException != null) {

 clientException.printStackTrace();

 } else {

 serviceException.printStackTrace();

 }

 }

});

**说明：**

更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/Android/app/src/androidTest/java/com/tencent/qcloud/cosxml/cssg/ai/COSOCRSnippet.java) 查看。
