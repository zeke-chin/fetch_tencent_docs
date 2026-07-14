<!-- source: https://cloud.tencent.com/document/product/436/113323 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:46:40+08:00 -->

# 通过 API 使用极智压缩

最近更新时间：2025-09-29 10:31:32


## 功能描述

极智压缩通过智能判断图片的主观质量进行自动调节，在不改变图片原格式的基础上，使图片体积相比原图有显著的降低，同时在视觉效果上可以最大程度贴近原图，帮助您减少图片访问流量、提升图片访问速度。该功能支持以下处理方式：

下载时处理

上传时处理

云上数据处理

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加对应的权限。对象存储支持的所有操作接口请参见 [COS action](https://cloud.tencent.com/document/product/598/69901)，数据万象支持的所有操作接口请参见 [CI action](https://cloud.tencent.com/document/product/598/98114)。通过不同方式使用此功能时，授权策略如下：

下载时处理：授权策略中 action 设置为 `cos:GetObject`、`ci:SetImageSlim`。

上传时处理：授权策略中 action 设置为 `cos:PutObject`、`ci:SetImageSlim`。

云上数据处理：授权策略中 action 设置为 `cos:PutObject`、`ci:SetImageSlim`。

**说明：**

GetObject 对应的 resource 为源文件，PutObject 对应的 resource 为转存的文件。

## 服务开通

使用该功能需提前 [绑定存储桶](https://cloud.tencent.com/document/product/460/46483)，开通数据万象服务。

使用该功能需提前通过 [控制台](https://cloud.tencent.com/document/product/460/95007) 或 [接口](https://cloud.tencent.com/document/product/460/95042) 开通极智压缩 API 使用功能。

**注意：**

数据万象绑定后，如果您手动对存储桶进行数据万象的解绑操作，将无法继续使用该功能。

## 使用限制

使用该接口时，请先确认相关限制条件。详情请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620#Image-processing)。

不支持处理 COS 上的归档存储类型和深度归档存储类型的图片，如果需要处理此类型文件，请先 [恢复归档文件](https://cloud.tencent.com/document/product/436/12633)。

## 费用说明

图片极智压缩为付费服务，产生的费用将由数据万象收取，详细计费说明可参见 [图片处理费用](https://cloud.tencent.com/document/product/460/58117)。

如果采用下载时处理的方式，且通过外网进行下载，调用会产生 [流量费用](https://cloud.tencent.com/document/product/460/58122)。

如果图片为 COS 上的低频存储类型，调用接口会产生 [COS 低频数据取回费用](https://cloud.tencent.com/document/product/436/53862#.E6.95.B0.E6.8D.AE.E5.8F.96.E5.9B.9E.E5.AE.9A.E4.BB.B7)。

## 接口形式

#### 下载时处理

GET /<ObjectKey>?imageSlim HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

#### 上传时处理

PUT /<ObjectKey> HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Authorization: Auth String

Pic-Operations:

{

 "is_pic_info": 1,

 "rules": [{

 "fileid": "exampleobject.jpg",

 "rule": "imageSlim"

 }]

}

#### 云上数据处理

POST /<ObjectKey>?image_process HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Content-length: Size

Authorization: Auth String

Pic-Operations:

{

 "is_pic_info": 1,

 "rules": [{

 "fileid": "exampleobject.jpg",

 "rule": "imageSlim"

 }]

}

**说明：**

Authorization: 携带鉴权信息，用于验证请求的合法性的请求头，Pic-Operations 头部需签入签名信息中，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

Pic-Operations 为 json 格式的字符串，具体参数信息请参见 [图片处理机制介绍](https://cloud.tencent.com/document/product/436/54050)。

当 `fileid`与 `ObjectKey` 相同时，处理后的图片将覆盖原图存储；不相同时将分别存储原图和处理后图片。

`fileid` 的值需要经过 URLEncode。

## 处理参数说明

参数 含义 类型 是否必选
ObjectKey 对象文件名，例如 folder/sample.jpg。String 是
imageSlim 固定参数，表示极智压缩。-是

**说明：**

使用下载时处理时，可通过 X-Slimflag 响应头部来判断图片是否已压缩，该响应头包含以下三个值：

0：表示压缩失败；

1：表示压缩成功；

2：表示未进行压缩，返回了原图。

## 实际案例

**说明：**

本篇文档中的实际案例仅包含**下载时处理**，该类处理不会保存处理后的图片至存储桶。如有保存需求，您可查阅 [图片处理机制介绍](https://cloud.tencent.com/document/product/460/18147) 文档并配置 [上传时处理](https://cloud.tencent.com/document/product/460/94856#2.-.E4.B8.8A.E4.BC.A0.E6.97.B6.E5.A4.84.E7.90.86) 或 [云上数据处理](https://cloud.tencent.com/document/product/460/94856#3.-.E4.BA.91.E4.B8.8A.E6.95.B0.E6.8D.AE.E5.A4.84.E7.90.86)。

假设原图格式为 png，图片大小为1335.2KB，如下图所示：

![Image 2: img](https://qcloudimg.tencent-cloud.cn/image/document/659c94759b701f0b6cedae4c9d238590.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/659c94759b701f0b6cedae4c9d238590.png)

将图片进行极智压缩处理，请求 URL 如下：

http://example-1258125638.cos.ap-shanghai.myqcloud.com/sample.png?imageSlim

效果如下：

![Image 4: img](https://qcloudimg.tencent-cloud.cn/image/document/fe23cb99ad5153e693d8b0acb82a1ae7.webp)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/fe23cb99ad5153e693d8b0acb82a1ae7.webp)

**压缩率对比**

格式 图片大小
png（原图）1335.2KB
png（极智压缩图）549KB（压缩率58.88%）
