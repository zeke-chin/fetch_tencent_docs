<!-- source: https://cloud.tencent.com/document/product/436/119347 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:45:48+08:00 -->

# 图片基础压缩（WebP）

最近更新时间：2025-09-19 15:44:52


## 功能描述

图片压缩指在图片质量保持不变的情况，尽可能地减小图片大小，以达到节省图片存储空间、减少图片访问流量、提升图片访问速度的效果。

[数据万象（Cloud Infinite，CI）](https://cloud.tencent.com/document/product/460/6962) 产品推出了 WebP 压缩功能，可将图片转换为 WebP 压缩图片格式，其在压缩方面相比 JPG 格式更优越。在相同图片质量的情况下，WebP 格式图片要比 JPG 格式图片减小25%以上，可以适配多终端使用场景。

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加对应的权限。对象存储支持的所有操作接口请参见 [COS action](https://cloud.tencent.com/document/product/598/69901)。

下载时处理：授权策略中 action 设置为 `cos:GetObject`。

上传时处理：授权策略中 action 设置为 `cos:PutObject`。

云上数据处理：授权策略中 action 设置为 `cos:PutObject`。

**说明：**

GetObject 对应的 resource 为源文件，PutObject 对应的 resource 为转存的文件。

## 服务开通

首次使用该功能时将默认为您开通数据万象，同时该存储桶将自动绑定数据万象，无需角色授权，即可直接使用。

**注意：**

数据万象绑定后，如果您手动对存储桶进行数据万象的解绑操作，将无法继续使用该功能。

## 使用限制

使用该接口时，请先确认相关限制条件。详情请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620#Image-processing)。

## 费用说明

WebP 压缩为付费服务，费用同基础图片处理，具体费用请参见 [图片处理费用](https://cloud.tencent.com/document/product/460/58117)，产生的费用将由数据万象收取。

如果采用下载时处理的方式，且通过外网进行下载，调用会产生 [流量费用](https://cloud.tencent.com/document/product/460/58122)。

**说明：**

图片转换为 WebP 格式后，部分浏览器无法读取 WebP 图片的 exif 信息，导致没有旋转。您可参见 [旋转](https://cloud.tencent.com/document/product/460/36542) 文档，增加 auto-orient 参数，对原图旋转后再进行压缩。

WebP 压缩默认继承原始图片的质量参数。您可参见 [质量变换](https://cloud.tencent.com/document/product/460/36544) 文档，通过修改图片质量来调节压缩率。

## 接口示例

### 下载时处理

GET /<ObjectKey>?imageMogr2/format/webp HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

### 上传时处理

PUT /<ObjectKey> HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

Pic-Operations:

{

"is_pic_info": 1,

"rules": [{

 "fileid": "exampleobject",

 "rule": "imageMogr2/format/webp"

}]

}

### 云上数据处理

POST /<ObjectKey>?image_process HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Content-length: <Size>

Authorization: <Auth String>

Pic-Operations:

{

"is_pic_info": 1,

"rules": [{

 "fileid": "exampleobject",

 "rule": "imageMogr2/format/webp"

}]

}

**说明**

Authorization: 携带鉴权信息，用于验证请求的合法性的请求头，Pic-Operations 头部需签入签名信息中，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

Pic-Operations 为 json 格式的字符串，具体参数信息请参见 [图片处理机制介绍](https://cloud.tencent.com/document/product/460/18147#.E4.B8.8A.E4.BC.A0.E6.97.B6.E5.A4.84.E7.90.86)。

当 fileid 与 ObjectKey 相同时，处理后的图片将覆盖原图存储；不相同时将分别存储原图和处理后图片。

fileid 的值需要经过 URLEncode。

## 处理参数说明

参数 含义 类型 是否必选
ObjectKey 对象文件名，例如 folder/sample.jpg。String 是
/format/<Format>压缩格式，此处为 webp。String 是

## 实际案例

**说明：**

本篇文档中的实际案例仅包含**下载时处理**，该类处理不会保存处理后的图片至存储桶。如有保存需求，请使用**上传时处理**或**云上数据处理**方式。

假设原图格式为 PNG，图片大小为1335.2KB，如下图所示：

![Image 2: img](https://qcloudimg.tencent-cloud.cn/image/document/ebd33004038e3b702491780bcb08b26a.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/ebd33004038e3b702491780bcb08b26a.png)

将原图转换为 WebP 格式，请求 URL 如下：

http://example-1258125638.cos.ap-shanghai.myqcloud.com/sample.png?imageMogr2/format/webp

效果如下：

![Image 4: img](https://qcloudimg.tencent-cloud.cn/image/document/859a05ca0b503f4314daf93d83c63a3f.webp)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/859a05ca0b503f4314daf93d83c63a3f.webp)

**压缩率对比**

格式 图片大小
PNG（原图）1335.2KB
WebP 65KB（压缩率95.13%）
