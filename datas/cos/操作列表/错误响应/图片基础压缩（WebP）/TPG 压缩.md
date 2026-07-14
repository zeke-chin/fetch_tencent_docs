<!-- source: https://cloud.tencent.com/document/product/436/113316 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:45:57+08:00 -->

# TPG 压缩

最近更新时间：2025-09-19 15:44:52


## 功能描述

图片压缩指在图片质量保持不变的情况，尽可能的减小图片大小，以达到节省图片存储空间、减少图片访问流量、提升图片访问速度的效果。

[数据万象（Cloud Infinite，CI）](https://cloud.tencent.com/document/product/460/6962) 产品推出了 TPG 压缩功能，可将图片转换为 TPG 格式，它是腾讯推出的自研图片格式，能支持动图，目前 QQ 浏览器、QQ 空间等产品已默认支持 tpg 图片，在图片质量相同的情况下，图片大小比 GIF 格式图片减少90%以上，比 PNG 图片小50%以上。

**说明：**

TPG 是腾讯自研的图片格式，使用前请确认图片加载环境已支持 TPG 解码，腾讯云数据万象提供集成 TPG 解码器的 [iOS](https://cloud.tencent.com/document/product/460/47732)、[Android](https://cloud.tencent.com/document/product/460/47737) 终端 SDK，可帮助您快速接入和使用 TPG，其他 TPG SDK 的下载与接入说明可参考 [TPG SDK](https://cloud.tencent.com/document/product/875/18366)。

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加对应的权限，数据万象支持的所有操作接口请参见 [action](https://cloud.tencent.com/document/product/598/98114)。

下载时处理：授权策略中 action 设置为 `cos:GetObject`。

上传时处理：授权策略中 action 设置为 `cos:PutObject`。

云上数据处理：授权策略中 action 设置为 `cos:PutObject`。

**说明：**

GetObject 对应的 resource 为源文件，PutObject 对应的 resource 为转存的文件。

## 服务开通

使用该功能需提前 [绑定存储桶](https://cloud.tencent.com/document/product/460/46483)，开通数据万象服务。

使用该功能需提前通过 [控制台](https://cloud.tencent.com/document/product/460/47501) 开通图片高级压缩功能。

**注意：**

数据万象绑定后，如果您手动对存储桶进行数据万象的解绑操作，将无法继续使用该功能。

## 使用限制

使用该接口时，请先确认相关限制条件。详情请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620#Image-processing)。

不支持处理 COS 上的归档存储类型和深度归档存储类型的图片，如果需要处理此类型文件，请先 [恢复归档文件](https://cloud.tencent.com/document/product/436/12633)。

## 费用说明

TPG 压缩为付费服务，计费项为图片高级压缩费用，具体费用请参见 [图片处理费用](https://cloud.tencent.com/document/product/460/58117)，产生的费用将由数据万象收取。

如果采用下载时处理的方式，且通过外网进行下载，调用会产生 [流量费用](https://cloud.tencent.com/document/product/460/58122)。

如果图片为 COS 上的低频存储类型，调用接口会产生 [COS 低频数据取回费用](https://cloud.tencent.com/document/product/436/53862#.E6.95.B0.E6.8D.AE.E5.8F.96.E5.9B.9E.E5.AE.9A.E4.BB.B7)。

## 接口示例

#### 下载时处理

GET /<ObjectKey>?imageMogr2/format/tpg HTTP/1.1

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

 "fileid": "exampleobject",

 "rule": "imageMogr2/format/tpg"

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

 "fileid": "exampleobject",

 "rule": "imageMogr2/format/tpg"

}]

}

**说明：**

Authorization：携带鉴权信息，用于验证请求的合法性，Pic-Operations 头部需写入签名信息中，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

Pic-Operations 为 json 格式的字符串，具体参数信息可参考 [图片持久化处理](https://cloud.tencent.com/document/product/460/18147)。

当 `fileid` 与 `ObjectKey` 相同时，处理后的图片将覆盖原图存储；不相同时将分别存储原图和处理后图片。

`fileid` 的值需要经过 URLEncode。

##### 处理参数说明

参数 含义 类型 是否必选
ObjectKey 对象文件名，例如 folder/sample.jpg。String 是
/format/<Format>压缩格式，此处为 tpg。String 是

## 实际案例

**说明：**

本篇文档中的实际案例仅包含**下载时处理**，该类处理不会保存处理后的图片至存储桶。如有保存需求，请使用 [上传时处理](https://cloud.tencent.com/document/product/460/60526#2.-.E4.B8.8A.E4.BC.A0.E6.97.B6.E5.A4.84.E7.90.86)或 [云上数据处理](https://cloud.tencent.com/document/product/460/60526#3.-.E4.BA.91.E4.B8.8A.E6.95.B0.E6.8D.AE.E5.A4.84.E7.90.86)方式。

假设原图格式为 png，图片大小为1335.2KB，如下图所示：

![Image 2: img](https://qcloudimg.tencent-cloud.cn/image/document/6e50a43514b498d3f2b9ab894692f9f0.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/6e50a43514b498d3f2b9ab894692f9f0.png)

将原图转换为 tpg 格式，请求 URL 如下：

http://example-1258125638.cos.ap-shanghai.myqcloud.com/sample.png?imageMogr2/format/tpg

**压缩率对比**

格式 图片大小
png（原图）1335.2KB
tpg 36.67KB（压缩率97.3%）
