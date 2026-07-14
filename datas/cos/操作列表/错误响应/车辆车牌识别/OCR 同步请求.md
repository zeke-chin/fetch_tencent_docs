<!-- source: https://cloud.tencent.com/document/product/436/115974 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:52:40+08:00 -->

# OCR 同步请求

最近更新时间：2025-08-22 15:29:11


## 功能描述

通用文字识别功能（Optical Character Recognition，OCR）基于行业前沿的深度学习技术，将图片上的文字内容，智能识别为可编辑的文本，可应用于随手拍扫描、纸质文档电子化、电商广告审核等多种场景，大幅提升信息处理效率。

**注意：**

本接口属于 GET 请求，为同步请求方式，需携带签名，具体签名设置请参见 [请求签名](https://cloud.tencent.com/document/product/460/6968)。

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加 `ci:CreateOCRJob`权限。数据万象支持的所有操作接口请参见 [CI action](https://cloud.tencent.com/document/product/598/98114)。

## 服务开通

使用该功能需提前 [绑定存储桶](https://cloud.tencent.com/document/product/460/46483)，开通数据万象服务。

**注意：**

数据万象绑定后，如果您手动对存储桶进行数据万象的解绑操作，将无法继续使用该功能。

## 使用限制

使用该接口时，请先确认相关限制条件。详情请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620#content-recognition)。

## 费用说明

该接口为付费服务，产生的费用将由数据万象收取，详细计费说明可参见 [内容识别费用](https://cloud.tencent.com/document/product/460/58118)。

## 请求

### 请求示例

原图存储在 COS：

GET /<ObjectKey>?ci-process=OCR&type=general&language-type=zh&ispdf=true&pdf-pagenumber=1&isword=false&enable-word-polygon=false HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

原图来自其他链接：

GET /?ci-process=OCR&detect-url=<detect-url>&type=general&language-type=zh&ispdf=true&pdf-pagenumber=1&isword=false&enable-word-polygon=false HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

**说明：**

Authorization: Auth String，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

### 请求参数

参数名称 描述 类型 是否必选
ObjectKey 对象文件名，例如：folder/document.jpg String 否
ci-process 数据万象处理能力，图片文字识别固定为 OCR String 是
detect-url 您可以通过填写 detect-url 处理任意公网可访问的图片链接。不填写 detect-url 时，后台会默认处理 ObjectKey ，填写了 detect-url 时，后台会处理 detect-url 链接，无需再填写 ObjectKey

detect-url 示例：`http://www.example.com/abc.jpg` ，需要进行 UrlEncode，处理后为http%3A%2F%2Fwww.example.com%2Fabc.jpg。String 否
type ocr 的识别类型，有效值为 general，accurate，efficient，fast，handwriting

general 表示通用印刷体识别

accurate 表示印刷体高精度版

efficient 表示印刷体精简版

fast 表示印刷体高速版

handwriting 表示手写体识别

默认值为 general String 否
l

anguage-type type 值为 general时有效，表示识别语言类型

支持自动识别语言类型，同时支持自选语言种类，默认中英文混合(zh)，各种语言均支持与英文混合的文字识别

可选值：

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
ispdf type 值为 general，fast 时有效，表示是否开启 PDF 识别，有效值为 true 和 false，默认值为false，开启后可同时支持图片和 PDF 的识别 Boolean 否
pdf-pagenumber type 值为 general，fast 时有效，表示需要识别的 PDF 页面的对应页码，仅支持 PDF 单页识别，当上传文件为 PDF 且 ispdf 参数值为 true 时有效，默认值为1 Integer 否
isword type 值为 general，accurate 时有效，表示识别后是否需要返回单字信息，有效值为 true 和 false，默认为 false Boolean 否
enable-word-polygon type 值为 handwriting 时有效，表示是否开启单字的四点定位坐标输出，有效值为 true 和 false，默认值为 false Boolean 否

### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 非公共头部

该请求操作无特殊的请求头部信息。

### 请求体

该请求无请求体。

## 响应

### 响应头

#### 公共响应头

该响应包含公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 特有响应头

该响应无特殊的响应头。

### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

<Response>

 <TextDetections>

 <DetectedText></DetectedText>

 <Confidence></Confidence>

 <Polygon>

 <X></X>

 <Y></Y>

 </Polygon>

 <ItemPolygon>

 <X></X>

 <Y></Y>

 <Width></Width>

 <Height></Height>

 </ItemPolygon>

 <Words>

 <Confidence></Confidence>

 <Character></Character>

 <WordCoordPoint>

 <WordCoordinate>

 <X></X>

 <Y></Y>

 </WordCoordinate>

 </WordCoordPoint>

 </Words>

 </TextDetections>

 <Language></Language>

 <Angel></Angel>

 <PdfPageSize></PdfPageSize>

 <RequestId></RequestId>

</Response>

具体的数据内容如下：

节点名称（关键字）父节点 描述 类型
Response 无 保存结果的容器 Container

Response 的内容：

节点名称（关键字）父节点 描述 类型
TextDetections Response 检测到的文本信息，包括文本行内容、置信度、文本行坐标以及文本行旋转纠正后的坐标 Container
Language Response 检测到的语言类型，目前支持的语言类型参考入参 language-type 说明 String
Angel Response 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负 Float
PdfPageSize Response 图片为 PDF 时，返回 PDF 的总页数，默认为0 Integer
RequestId Response 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId String

TextDetections节点的内容：

节点名称（关键字）父节点 描述 类型
DetectedText TextDetections 识别出的文本行内容 String
Confidence TextDetections 置信度 0 ~100 Integer
Polygon TextDetections 文本行坐标，以四个顶点坐标表示

注意：此字段可能返回 null，表示取不到有效值 Container
ItemPolygon TextDetections 文本行在旋转纠正之后的图像中的像素坐标，表示为（左上角 x, 左上角 y，宽 width，高 height）Container
Words TextDetections 识别出来的单字信息包括单字（包括单字 Character 和单字置信度 confidence）， 支持识别的接口：general、accurate Container
WordPolygon TextDetections 字的坐标数组，以四个顶点坐标表示。注意：此字段可能返回 null，表示取不到有效值。支持识别的类型：handwriting Container

Polygon 节点的内容：

节点名称（关键字）父节点 描述 类型
X Polygon 横坐标 Integer
Y Polygon 纵坐标 Integer

ItemPolygon 节点的内容：

节点名称（关键字）父节点 描述 类型
X ItemPolygon 左上角 x Integer
Y ItemPolygon 左上角 y Integer
Width ItemPolygon 宽 width Integer
Height ItemPolygon 高 height Integer

Words 节点的内容：

节点名称（关键字）父节点 描述 类型
Confidence Words 置信度 0 ~100 Integer
Character Words 候选字 Character String
WordCoordPoint Words 单字在原图中的四点坐标， 支持识别的接口：general、accurate Container

WordCoordPoint 节点的内容：

节点名称（关键字）父节点 描述 类型
WordCoordinate WordCoordPoint 单字在原图中的坐标，以四个顶点坐标表示，以左上角为起点，顺时针返回 Container

WordCoordinate 节点的内容：

节点名称（关键字）父节点 描述 类型
X WordCoordinate 横坐标 Integer
Y WordCoordinate 纵坐标 Integer

WordPolygon节点的内容：

节点名称（关键字）父节点 描述 类型
LeftTop WordPolygon 左上顶点坐标 Container
RightTop WordPolygon 左上顶点坐标 Container
RightBottom WordPolygon 左上顶点坐标 Container
LeftBottom WordPolygon 左上顶点坐标 Container

LeftTop，RightTop，RightBottom，LeftBottom 节点的内容：

节点名称（关键字）父节点 描述 类型
X WordCoordinate 横坐标 Integer
Y WordCoordinate 纵坐标 Integer

### 错误码

常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/460/8523) 文档。

## 实际案例

**使用模板ID**

### 请求

GET /<ObjectKey>?ci-process=OCR&type=general&language-type=zh&ispdf=true&isword=true HTTP/1.1

Authorization:q-sign-algorithm=sha1&q-ak= ************************************ &q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature= ****************************************

Host:bucket-1250000000.cos.ap-beijing.myqcloud.com

### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 414641

Date: Thu, 15 Jun 2017 12:37:29 GMT

Server: tencent-ci

x-cos-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>

 <Angel>359.99</Angel>

 <Language>mix</Language>

 <PdfPageSize>0</PdfPageSize>

 <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=</RequestId>

 <TextDetections>

 <Confidence>99</Confidence>

 <DetectedText>你好</DetectedText>

 <ItemPolygon>

 <Height>64</Height>

 <Width>123</Width>

 <X>140</X>

 <Y>167</Y>

 </ItemPolygon>

 <Polygon>

 <X>140</X>

 <Y>167</Y>

 </Polygon>

 <Polygon>

 <X>263</X>

 <Y>167</Y>

 </Polygon>

 <Polygon>

 <X>263</X>

 <Y>231</Y>

 </Polygon>

 <Polygon>

 <X>140</X>

 <Y>231</Y>

 </Polygon>

 <Words>

 <Character>你</Character>

 <Confidence>99</Confidence>

 <WordCoordPoint>

 <WordCoordinate>

 <X>212</X>

 <Y>167</Y>

 </WordCoordinate>

 <WordCoordinate>

 <X>341</X>

 <Y>167</Y>

 </WordCoordinate>

 <WordCoordinate>

 <X>341</X>

 <Y>231</Y>

 </WordCoordinate>

 <WordCoordinate>

 <X>212</X>

 <Y>231</Y>

 </WordCoordinate>

 </WordCoordPoint>

 </Words>

 <Words>

 <Character>好</Character>

 <Confidence>99</Confidence>

 <WordCoordPoint>

 <WordCoordinate>

 <X>341</X>

 <Y>167</Y>

 </WordCoordinate>

 <WordCoordinate>

 <X>263</X>

 <Y>167</Y>

 </WordCoordinate>

 <WordCoordinate>

 <X>263</X>

 <Y>231</Y>

 </WordCoordinate>

 <WordCoordinate>

 <X>341</X>

 <Y>230</Y>

 </WordCoordinate>

 </WordCoordPoint>

 </Words>

 </TextDetections>

 <TextDetections>

 <Confidence>99</Confidence>

 <DetectedText>再见</DetectedText>

 <ItemPolygon>

 <Height>43</Height>

 <Width>245</Width>

 <X>526</X>

 <Y>1444</Y>

 </ItemPolygon>

 <Polygon>

 <X>526</X>

 <Y>1444</Y>

 </Polygon>

 <Polygon>

 <X>771</X>

 <Y>1444</Y>

 </Polygon>

 <Polygon>

 <X>771</X>

 <Y>1487</Y>

 </Polygon>

 <Polygon>

 <X>526</X>

 <Y>1487</Y>

 </Polygon>

 <Words>

 <Character>再</Character>

 <Confidence>99</Confidence>

 <WordCoordPoint>

 <WordCoordinate>

 <X>564</X>

 <Y>1444</Y>

 </WordCoordinate>

 <WordCoordinate>

 <X>608</X>

 <Y>1444</Y>

 </WordCoordinate>

 <WordCoordinate>

 <X>608</X>

 <Y>1487</Y>

 </WordCoordinate>

 <WordCoordinate>

 <X>564</X>

 <Y>1487</Y>

 </WordCoordinate>

 </WordCoordPoint>

 </Words>

 <Words>

 <Character>见</Character>

 <Confidence>99</Confidence>

 <WordCoordPoint>

 <WordCoordinate>

 <X>608</X>

 <Y>1444</Y>

 </WordCoordinate>

 <WordCoordinate>

 <X>641</X>

 <Y>1444</Y>

 </WordCoordinate>

 <WordCoordinate>

 <X>641</X>

 <Y>1487</Y>

 </WordCoordinate>

 <WordCoordinate>

 <X>608</X>

 <Y>1487</Y>

 </WordCoordinate>

 </WordCoordPoint>

 </Words>

 </TextDetections>

</Response>
