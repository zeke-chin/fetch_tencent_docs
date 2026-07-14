<!-- source: https://cloud.tencent.com/document/product/436/107599 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:09:13+08:00 -->

# 文档转 HTML

最近更新时间：2024-11-11 15:53:52


## 简介

本文档提供关于文档预览同步请求的 API 概览以及 SDK 示例代码。

API 说明
[文档转 HTML](https://cloud.tencent.com/document/product/436/54059)文档转 HTML 功能支持对多种文档类型的文件生成 HTML 格式预览，满足 PC、App 等多个用户端的文档在线浏览需求，适用于在线教育、企业 OA、在线知识库、网盘文档预览等业务场景。

## 文档转 HTML

#### 功能说明

支持对多种文档类型的文件生成 HTML 格式预览。

#### 方法原型

def ci_doc_preview_html_process(self, Bucket, Key, SrcType=None, Copyable='1', DstType='html', HtmlParams=None, HtmlWaterword=None, HtmlFillStyle=None,

 HtmlFront=None, HtmlRotate=None, HtmlHorizontal=None, HtmlVertical=None, HtmlTitle=None, **kwargs):

#### 请求示例

def ci_doc_preview_to_html_process(): # 文档预览同步接口（生成html） html_params = { 'commonOptions': { 'isShowTopArea': 'true', 'isShowHeader': 'true', 'isBrowserViewFullscreen': 'true', 'isIframeViewFullscreen': 'true', }, 'wordOptions': { 'isShowDocMap': 'true', 'isBestScale': 'true', 'isShowBottomStatusBar': 'true', } } html_params_json = json.dumps(html_params) response = client.ci_doc_preview_html_process( Bucket=bucket_name, Key='1.txt', SrcType='txt', DstType='html', HtmlParams=base64.urlsafe_b64encode(html_params_json.encode('utf-8')).decode('utf-8').rstrip('='), HtmlWaterword=base64.urlsafe_b64encode("watermark".encode('utf-8')).decode('utf-8').rstrip('='), HtmlFillStyle=base64.urlsafe_b64encode("rgba(192,192,192,0.6)".encode('utf-8')).decode('utf-8').rstrip('='), HtmlFront=base64.urlsafe_b64encode("bold 20px Serif".encode('utf-8')).decode('utf-8').rstrip('='), HtmlRotate="180", HtmlHorizontal="100", HtmlVertical="50", HtmlTitle=base64.urlsafe_b64encode("title".encode('utf-8')).decode('utf-8').rstrip('='), ) print(response) response['Body'].get_stream_to_file('result.html')

#### 参数说明

名称 参数说明 类型 是否必选
Bucket 对象所在存储桶 String 是
Key 对象名 String 是
SrcType 指定目标文件类型，支持的文件类型请见 [文档转 HTML](https://cloud.tencent.com/document/product/436/54059) 文档 String 否
Copyable 是否可复制。默认为可复制，填入值为1；不可复制，填入值为0 String 否
DstType 转换输出目标文件类型，文档 HTML 预览固定为 html（需为小写字母）String 否
HtmlParams 自定义配置参数，json结构，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39) 的 Base64 编码，默认配置为：{ commonOptions: { isShowTopArea: true, isShowHeader: true } }，支持的配置参考 [自定义配置项说明](https://cloud.tencent.com/document/product/436/59408#.E8.87.AA.E5.AE.9A.E4.B9.89.E9.85.8D.E7.BD.AE.E9.80.89.E9.A1.B9)String 否
HtmlWaterword 水印文字，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39) 的 Base64 编码，默认为空 String 否
HtmlFillStyle 水印 RGBA（颜色和透明度），需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39) 的 Base64 编码，默认为：rgba(192,192,192,0.6)String 否
HtmlFront 水印文字样式，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39) 的 Base64 编码，默认为：bold 20px Serif String 否
HtmlRotate 水印文字旋转角度，0 - 360，默认315度 String 否
HtmlHorizontal 水印文字水平间距，单位 px，默认为50 String 否
HtmlVertical 水印文字垂直间距，单位 px，默认为100 String 否
HtmlTitle 自定义返回 html 的 title 信息，默认为“腾讯云-数据万象”，可输入自定义字符串并配合通配符使用，需要经过 [URL安全](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39)的 Base64 编码。

通配符包括以下两种：

${InputName}：输入文件的文件名（不包括后缀）

${InputNameAndExt}：输入文件的文件名（包括后缀）

例如：需要设置的 Title 信息为: “万象标题 ${InputName}”，则 Base64 编码为 5LiH6LGh5qCH6aKYICR7SW5wdXROYW1lfQ，HtmlTitle=5LiH6LGh5qCH6aKYICR7SW5wdXROYW1lfQ String 否

#### 返回结果说明

response 为响应头与响应体的集合， 数据类型为 dict。

##### 响应头

返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

##### 响应体

[html-content]
