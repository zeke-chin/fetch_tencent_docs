<!-- source: https://cloud.tencent.com/document/product/436/113309 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:45:08+08:00 -->

# 获取图片 EXIF

最近更新时间：2025-09-19 15:44:52


## 功能概述

EXIF（Exchangeable Image File）全称为可交换图像文件，可记录数码照片的拍摄参数、缩略图及其他属性信息。腾讯云数据万象通过 **EXIF** 接口获取 EXIF 信息。

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加 `cos:GetObject` 权限。对象存储支持的所有操作接口请参见 [COS action](https://cloud.tencent.com/document/product/598/69901)。

**说明：**

GetObject 对应的 resource 为源文件。

## 服务开通

首次使用该功能时将默认为您开通数据万象，同时该存储桶将自动绑定数据万象，无需角色授权，即可直接使用。

**注意：**

数据万象绑定后，如果您手动对存储桶进行数据万象的解绑操作，将无法继续使用该功能。

## 使用限制

使用该接口时，请先确认相关限制条件。详情请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620)。

支持获取 JPG、PNG、BMP、WebP、TIFF、AVIF、HEIF 格式图片的 EXIF 信息。

**注意：**

如图片无 EXIF 信息，将返回`{"error" : "no exif data"}`。

## 费用说明

该接口为付费服务，产生的费用将由数据万象收取，详细计费说明可参见 [图片处理费用](https://cloud.tencent.com/document/product/460/58117)。

如果采用下载时处理的方式，且通过外网进行下载，调用会产生 [流量费用](https://cloud.tencent.com/document/product/460/58122)。

## 接口示例

GET /<ObjectKey>?exif HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

## 处理参数说明

### **请求参数**

**操作名称**：exif。

参数 含义 类型 是否必选
ObjectKey 对象文件名，例如 folder/sample.jpg。String 是

### 响应

返回的内容为图片的 EXIF 信息，有关 EXIF 的更新信息，请参见 [EXIF 说明](https://ci-official-diagram-1258125638.cos.ap-nanjing.myqcloud.com/DC-008-Translation-2016-E.pdf)。

#### 响应示例

{

 "ApertureValue": {

 "val": "483328/65536"

 },

 "ColorSpace": {

 "val": "sRGB"

 },

 "CustomRendered": {

 "val": "0"

 },

 "DateTime": {

 "val": "2018:09:03 17:37:06"

 },

 "DateTimeOriginal": {

 "val": "2018:09:03 17:37:06"

 },

 "ExifVersion": {

 "val": "48 50 51 48"

 },

 "ExposureBiasValue": {

 "val": "0/1"

 },

 "ExposureMode": {

 "val": "0"

 },

 "ExposureProgram": {

 "val": "8"

 },

 "ExposureTime": {

 "val": "1/200"

 },

 "FNumber": {

 "val": "13/1"

 }

内容较多其他信息已省略

}

## 实际案例

### 案例一：公有读

#### 请求

http://examples-1251000004.cos.ap-shanghai.myqcloud.com/sample.jpeg?exif

#### 响应

{

 "ColorSpace": {

 "val": "sRGB"

 }

}

### 案例二：私有读、携带签名

获取方式同上，仅增加签名部分，并与获取参数以“&”连接，示例如下：

http://examples-1251000004.cos.ap-shanghai.myqcloud.com/sample.jpeg?q-sign-algorithm=<signature>&exif

**说明：**

`<signature>`为签名部分，获取方式请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778)。

## 注意事项

为了避免未授权人员通过访问不携带处理参数的链接实现访问和下载原图的情况，您可同时将处理参数签入到请求签名中，处理参数整体是参数的 key，value 为空，如下是简单的示例（仅做样式参考，可能已经过期无法直接访问），详细计算方法请参见 [请求签名](https://cloud.tencent.com/document/product/436/14114)。

http://examples-1251000004.cos.ap-shanghai.myqcloud.com/sample.jpeg?q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1593342360;1593342720&q-key-time=1593342360;1593342720&q-header-list=&q-url-param-list=watermark%252f1%252fimage%252fahr0cdovl2v4yw1wbgvzlteyntewmdawmdqucgljc2gubxlxy2xvdwquy29tl3nodwl5aw4uanbn%252fgravity%252fsoutheast&q-signature=****************************************&watermark/1/image/aHR0cDovL2V4YW1wbGVzLTEyNTEwMDAwMDQucGljc2gubXlxY2xvdWQuY29tL3NodWl5aW4uanBn/gravity/southeast
