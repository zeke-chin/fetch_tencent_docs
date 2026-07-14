<!-- source: https://cloud.tencent.com/document/product/436/113318 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:46:07+08:00 -->

# SVG 压缩

最近更新时间：2025-09-19 15:44:52


## 功能描述

图片压缩指在图片质量保持不变的情况，尽可能的减小图片大小，以达到节省图片存储空间、减少图片访问流量、提升图片访问速度的效果。

[数据万象（Cloud Infinite，CI）](https://cloud.tencent.com/document/product/460/6962) 产品推出了 SVG 压缩功能，可以在不影响显示效果的情况下，通过一定的优化算法删除 SVG 文件中的冗余信息，最终达到减少 SVG 文件体积的目的。

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加对应的权限。对象存储支持的所有操作接口请参见 [COS action](https://cloud.tencent.com/document/product/598/69901)。

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

支持格式：仅支持将 SVG 格式图片作为输入。

体积限制：处理图片原图大小不超过32MB。

不支持处理 COS 上的归档存储类型和深度归档存储类型的图片，如果需要处理此类型文件，请先 [恢复归档文件](https://cloud.tencent.com/document/product/436/12633)。

## 费用说明

SVG 压缩为付费服务，计费项为图片高级压缩费用，具体费用请参见 [图片处理费用](https://cloud.tencent.com/document/product/460/58117)，产生的费用将由数据万象收取。

如果采用下载时处理的方式，且通过外网进行下载，调用会产生 [流量费用](https://cloud.tencent.com/document/product/460/58122)。

如果图片为 COS 上的低频存储类型，调用接口会产生 [COS 低频数据取回费用](https://cloud.tencent.com/document/product/436/53862#.E6.95.B0.E6.8D.AE.E5.8F.96.E5.9B.9E.E5.AE.9A.E4.BB.B7)。

## 接口示例

#### 下载时处理

GET /<ObjectKey>?imageMogr2/format/svgc HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Authorization: <Auth String>

#### 上传时处理

PUT /<ObjectKey> HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

Pic-Operations:

{

"is_pic_info": 0,

"rules": [{

 "fileid": "exampleobject",

 "rule": "imageMogr2/format/svgc"

}]

}

#### 云上数据处理

POST /<ObjectKey>?image_process HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Content-length: <Size>

Authorization: <Auth String>

Pic-Operations:

{

"is_pic_info": 0,

"rules": [{

 "fileid": "exampleobject",

 "rule": "imageMogr2/format/svgc"

}]

}

**说明：**

Authorization：携带鉴权信息，用于验证请求的合法性，Pic-Operations 头部需写入签名信息中，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

Pic-Operations 为 json 格式的字符串，具体参数信息可参考 [图片持久化处理](https://cloud.tencent.com/document/product/460/18147)。

当 `fileid` 与 `ObjectKey` 相同时，处理后的图片将覆盖原图存储；不相同时将分别存储原图和处理后图片。

`fileid` 的值需要经过 URLEncode。

##### 处理参数说明

参数 含义 类型 是否必选
ObjectKey 对象文件名，例如 folder/sample.svg String 是
/format/<Format>压缩格式，此处为 svgc String 是
