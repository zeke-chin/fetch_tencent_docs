<!-- source: https://cloud.tencent.com/document/product/436/123119 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:27:10+08:00 -->

# 图片文字识别（OCR）

最近更新时间：2025-09-10 19:27:33


## 简介

本文档提供关于通用文字识别的 API 概览以及 SDK 示例代码。

API 说明
[通用文字识别](https://cloud.tencent.com/document/product/436/64324)通用文字识别功能（Optical Character Recognition，OCR）基于行业前沿的深度学习技术，将图片上的文字内容，智能识别为可编辑的文本，可应用于随手拍扫描、纸质文档电子化、电商广告审核等多种场景，大幅提升信息处理效率。

## 通用文字识别

#### 功能说明

通用文字识别。

#### 方法原型

func (s *CIService) OcrRecognition(ctx context.Context, key string, opt *OcrRecognitionOptions) (*OcrRecognitionResult, *Response, error)

#### 请求示例

obj := "pic/ocr.png"

opt := &cos.OcrRecognitionOptions{

 Type: "general",

 LanguageType: "zh",

 Isword: true,

 EnableWordPolygon: true,

}

res, _, err := c.CI.OcrRecognition(context.Background(), obj, opt)

#### 参数说明

type OcrRecognitionOptions struct {

  Type       string `url:"type,omitempty"`

  LanguageType   string `url:"language-type,omitempty"`

  Ispdf       bool  `url:"ispdf,omitempty"`

  PdfPageNumber   int  `url:"pdf-pagenumber,omitempty"`

  Isword      bool  `url:"isword,omitempty"`

  EnableWordPolygon bool  `url:"enable-word-polygon,omitempty"`

}

参数名称 参数描述 是否必填
key 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名`examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/pic/pic.jpg`中，对象键为 pic/pic.jpg 是
Type OCR 的识别类型，有效值为 general，accurate，efficient，fast，handwriting。general 表示通用印刷体识别；accurate 表示印刷体高精度版；efficient 表示印刷体精简版；fast 表示印刷体高速版；handwriting 表示手写体识别。默认值为 general。否
LanguageType type 值为 general 时有效，表示识别语言类型。支持自动识别语言类型，同时支持自选语言种类，默认中英文混合(zh)，各种语言均支持与英文混合的文字识别。可选值请参见 [可识别的语言类型](https://cloud.tencent.com/document/product/460/63227#bdfce6d2-5bdb-4a94-b61a-a648116a2d5c)。否
Ispdf type 值为 general、fast 时有效，表示是否开启 PDF 识别，有效值为 true 和 false，默认值为 false，开启后可同时支持图片和 PDF 的识别。否
PdfPageNumber type 值为 general、fast 时有效，表示需要识别的 PDF 页面的对应页码，仅支持 PDF 单页识别，当上传文件为 PDF 且 ispdf 参数值为 true 时有效，默认值为1。否
Isword type 值为 general、accurate 时有效，表示识别后是否需要返回单字信息，有效值为 true 和 false，默认为 false。否
EnableWordPolygon type 值为 handwriting 时有效，表示是否开启单字的四点定位坐标输出，有效值为 true 和 false，默认值为 false。否

#### 结果说明

type OcrRecognitionResult struct {

 XMLName xml.Name `xml:"Response"`

 TextDetections []TextDetections `xml:"TextDetections,omitempty"`

 Language string `xml:"Language,omitempty"`

 Angel float64 `xml:"Angel,omitempty"`

 PdfPageSize int `xml:"PdfPageSize,omitempty"`

 RequestId string `xml:"RequestId,omitempty"`

}

type TextDetections struct {

 DetectedText string `xml:"DetectedText,omitempty"`

 Confidence int `xml:"Confidence,omitempty"`

 Polygon []Polygon `xml:"Polygon,omitempty"`

 ItemPolygon []ItemPolygon `xml:"ItemPolygon,omitempty"`

 Words []Words `xml:"Words,omitempty"`

 WordPolygon []WordPolygon `xml:"WordPolygon,omitempty"`

}

type Polygon struct {

 X int `xml:"X,omitempty"`

 Y int `xml:"Y,omitempty"`

}

type ItemPolygon struct {

 X int `xml:"X,omitempty"`

 Y int `xml:"Y,omitempty"`

 Width int `xml:"Width,omitempty"`

 Height int `xml:"Height,omitempty"`

}

type Words struct {

 Confidence int `xml:"Confidence,omitempty"`

 Character string `xml:"Character,omitempty"`

 WordCoordPoint *WordCoordPoint `xml:"WordCoordPoint,omitempty"`

}

type WordCoordPoint struct {

 WordCoordinate []Polygon `xml:"WordCoordinate,omitempty"`

}

type WordPolygon struct {

 LeftTop *Polygon `xml:"LeftTop,omitempty"`

 RightTop *Polygon `xml:"RightTop,omitempty"`

 RightBottom *Polygon `xml:"RightBottom,omitempty"`

 LeftBottom *Polygon `xml:"LeftBottom,omitempty"`

}

参数名称 参数描述
TextDetections 检测到的文本信息，包括文本行内容、置信度、文本行坐标以及文本行旋转纠正后的坐标。
Language 检测到的语言类型，目前支持的语言类型可参考入参 language-type 说明。
Angel 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。
PdfPageSize 图片为 PDF 时，返回 PDF 的总页数，默认为0。
RequestId 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
DetectedText 识别出的文本行内容。
Confidence 置信度 0 - 100。
Polygon 文本行坐标，以顶点坐标表示 注意：此字段可能返回 null，表示取不到有效值。
ItemPolygon 文本行在旋转纠正之后的图像中的像素坐标，表示为（左上角 x, 左上角 y，宽 width，高 height）。
Words 识别出来的单字信息包括单字（包括单字 Character 和单字置信度 confidence），支持识别的接口：general、accurate。
WordPolygon 字的坐标数组，以四个顶点坐标表示。

注意：此字段可能返回 null，表示取不到有效值。支持识别的类型：handwriting。
X 横坐标。
Y 纵坐标。
Width 宽 width。
Height 高 height。
Confidence 置信度 0 - 100。
Character 识别出来的单词信息。
WordCoordPoint 单字在原图中的四点坐标，支持识别的接口：general、accurate。
WordCoordinate 单字在原图中的坐标，以四个顶点坐标表示，以左上角为起点，顺时针返回。
LeftTop 左上顶点坐标。
RightTop 右上顶点坐标。
RightBottom 右下顶点坐标。
LeftBottom 左下顶点坐标。
