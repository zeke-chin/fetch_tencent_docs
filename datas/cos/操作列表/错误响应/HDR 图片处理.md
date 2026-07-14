<!-- source: https://cloud.tencent.com/document/product/436/119427 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:47:01+08:00 -->

# HDR 图片处理

最近更新时间：2026-06-26 15:34:02


## 功能描述

HDR（High Dynamic Range Imaging），高动态范围成像，是一种能够显示更大曝光动态范围的图像，它能保留图像中的更多细节和色彩信息，使图像的明暗差别更明显、色彩更丰富，从而提供更真实和丰富的视觉体验。

数据万象支持在进行图片基础处理（如缩放、裁剪等）时保留图片原有的 HDR 信息，使处理后的图片依然能展示出 HDR 效果。该功能支持以下处理方式：

下载时处理

上传时处理

云上数据处理

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/436/31923) 的 action 中添加对应的权限。对象存储支持的所有操作接口请参见 [COS action](https://cloud.tencent.com/document/product/598/69901)。

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

该接口需要与 [基础图片处理](https://cloud.tencent.com/document/product/460/6924) 搭配使用，请先确认基础图片处理相关限制条件。详情请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620#Image-processing)。

不支持处理 COS 上的归档存储类型和深度归档存储类型的图片，如果需要处理此类型文件，请先 [恢复归档文件](https://cloud.tencent.com/document/product/436/12633)。

当前仅支持处理部分 HDR 类别如下：

JPG/JPEG：Ultra HDR（ISO 标准的 GainMap HDR）

HEIF/HEIC：10-bit 原生 HDR、Apple 标准的 GainMap HDR

AVIF：10-bit 原生 HDR

## 费用说明

HDR 图片为付费服务，与基础图片处理搭配使用时，将产生 HDR 图片处理费用，如果处理结果图为 HEIF/HEIC 或 AVIF 格式，将产生图片高级压缩和 HDR 图片处理两项费用，详细计费说明可参见 [图片处理费用](https://cloud.tencent.com/document/product/460/58117)。

通过下载时处理的方式，且通过外网进行下载，调用会产生 [数据万象流量费用](https://cloud.tencent.com/document/product/460/58122)。

如果图片为 COS 上的低频存储类型，调用接口会产生 [COS 低频数据取回费用](https://cloud.tencent.com/document/product/436/53862#.E6.95.B0.E6.8D.AE.E5.8F.96.E5.9B.9E.E5.AE.9A.E4.BB.B7)。

## 接口示例

### 方式一：下载时处理

GET /<ObjectKey>?imageMogr2/hdr/<mode> HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

### 方式二：上传时处理

PUT /<ObjectKey> HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

Pic-Operations:

{

 "is_pic_info": 1,

 "rules": [{

 "bucket":"examplebucket-1250000000",

 "fileid": "exampleobject",

 "rule": "imageMogr2/hdr/<mode>"

 }]

}

### 方式三：云上数据处理

POST /<ObjectKey>?image_process HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Content-length: <Size>

Authorization: <Auth String>

Pic-Operations:

{

 "is_pic_info": 1,

 "rules": [{

 "bucket":"examplebucket-1250000000",

 "fileid": "exampleobject",

 "rule": "imageMogr2/hdr/<mode>"

 }]

}

**说明：**

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档），Pic-Operations 头部需签入签名信息中。

Pic-Operations 为 json 格式的字符串，具体参数信息可参见 [图片持久化处理](https://cloud.tencent.com/document/product/460/18147) 文档。

当 fileid 与 ObjectKey 相同时，处理后的图片将覆盖原图存储；不相同时将分别存储原图和处理后图片。

fileid 的值需要经过 URLEncode。

## 参数说明

数据万象通过 imageMogr2 提供一系列的图片处理操作，HDR 图片处理的参数为`hdr`，需要搭配其他 imageMogr2处理参数一起使用。

参数 含义 默认值 类型 是否必选
ObjectKey 对象文件名，例如 folder/sample.jpg。无 String 是
/hdr/<mode>在原图为 HDR 图片（10-bit 色深或带有 GainMap）时该参数才有意义，需要搭配 `imageMogr2`的其他处理参数一起使用，<mode>值可取0、1：

0：处理后不保留 HDR 信息，图片在处理后将降级为 SDR 图片。

1：处理后按原图的 HDR 类型保留 HDR 信息，当前支持 JPG、HEIF、AVIF 三种格式的 HDR 图片，具体可见上方表格。0 Int 否
/ignore-error/1 当处理参数中携带此参数时，针对文件过大、参数超限等导致处理失败的场景，会直接返回原图而不报错 无 String 否

**说明：**

要处理 HEIF/HEIC 或 AVIF 格式的图片，需开启 [图片高级压缩功能](https://cloud.tencent.com/document/product/460/47501)。

## 实际案例

### 案例一：下载时处理（缩放宽高）

访问 HDR 图片时进行缩放宽高的操作，缩放为原图50%并输出为 HDR 图片，示例如下：

http://example-12500000.cos.ap-shanghai.myqcloud.com/sample.avif?imageMogr2/thumbnail/!50p/hdr/1

### 案例二：上传时处理（缩放）

上传 HDR 图片时进行缩放宽高的操作，缩放为原图50%并保留 HDR 信息，将缩放后的 HDR 图片保存至同一存储桶，示例如下：

#### 请求

PUT /sample.jpg HTTP/1.1

Host: examplebucket-1250000000.cos.ap-shanghai.myqcloud.com

Date: Wed, 28 Oct 2025 20:32:00 GMT

Authorization: q-sign-algorithm=sha1&q-ak=AKID****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff905****

Pic-Operations: {"is_pic_info":1,"rules":[{"bucket":"examplebucket-1250000000","fileid":"output/sample_hdr.jpg","rule":"imageMogr2/thumbnail/!50p/hdr/1"}]}

Content-Length: 64

[图片二进制内容]

#### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 645

Date: Wed, 28 Oct 2025 20:32:00 GMT

Server: tencent-ci

x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<UploadResult>

 <OriginalInfo>

 <Key>sample.jpg</Key>

 <Location>examplebucket-1250000000.cos.ap-shanghai.myqcloud.com/sample.jpg</Location>

 <ETag>"580cd6930444576523c25f86ce2af9b1fc2d5484"</ETag>

 <ImageInfo>

 <Format>JPEG</Format>

 <Width>4000</Width>

 <Height>3000</Height>

 <Quality>95</Quality>

 <Ave>0xa18454</Ave>

 <Orientation>1</Orientation>

 <FrameCount>1</FrameCount>

 </ImageInfo>

 </OriginalInfo>

 <ProcessResults>

 <Object>

 <Key>output/sample_hdr.jpg</Key>

 <Location>examplebucket-1250000000.cos.ap-shanghai.myqcloud.com/output/sample_hdr.jpg</Location>

 <Format>JPEG</Format>

 <Width>2000</Width>

 <Height>1500</Height>

 <Size>1024000</Size>

 <Quality>95</Quality>

 <ETag>"eaa4e3d8fd498bbc63be3b71c46b9c61f23e3f0c"</ETag>

 <FrameCount>1</FrameCount>

 </Object>

 </ProcessResults>

</UploadResult>

## 注意事项

为了避免未授权人员通过访问不携带处理参数的链接实现访问和下载原图的情况，您可将处理参数签入到请求签名中。签入后，用户去掉处理参数直接访问原图将返回 403 错误。

### 签入方法

在计算请求签名时，将图片处理参数整体作为一个 URL 请求参数参与签名计算，其中处理参数为 key，value 为空字符串。

以 `imageMogr2/thumbnail/!50p/hdr/1` 为例，签名计算过程如下：

##### **步骤1：生成 UrlParamList 和 HttpParameters**

将处理参数整体作为 key，按照 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档中的规则进行 UrlEncode 编码并转换为小写：

原始 key：`imageMogr2/thumbnail/!50p/hdr/1`

UrlEncode 后（小写）：`imagemogr2%2fthumbnail%2f%2150p%2fhdr%2f1`

UrlParamList：`imagemogr2%2fthumbnail%2f%2150p%2fhdr%2f1`

HttpParameters：`imagemogr2%2fthumbnail%2f%2150p%2fhdr%2f1=`

##### **步骤2：拼入 HttpString 参与签名计算**

将上述 HttpParameters 填入 HttpString 的对应位置：

get\n/{ObjectKey}\nimagemogr2%2fthumbnail%2f%2150p%2fhdr%2f1=\n{HttpHeaders}\n

其余签名步骤（SignKey、StringToSign、Signature）与标准流程一致。

##### **步骤3：拼接最终 URL**

将签名结果和处理参数拼入 URL 时，注意对签名字段的值和处理参数的 key 分别进行 UrlEncode：

https://{BucketName-APPID}.cos.{Region}.myqcloud.com/{ObjectKey}?q-sign-algorithm=sha1&q-ak={SecretId}&q-sign-time={KeyTime}&q-key-time={KeyTime}&q-header-list=host&q-url-param-list=imagemogr2%252fthumbnail%252f%252150p%252fhdr%252f1&q-signature={Signature}&imageMogr2%2Fthumbnail%2F%2150p%2Fhdr%2F1=

**说明：**

q-url-param-list 的值中 % 需再次编码为 %25（即 %2f 变为 %252f），这是因为它作为 URL 参数值需要做一次 UrlEncode。

处理参数追加到 URL 末尾时，也需要进行 UrlEncode（如 / 编码为 %2F，! 编码为 %21），并以 key= 的格式拼接。

建议使用 COS 各语言 SDK 提供的预签名 URL 方法，将处理参数通过 Params 参数传入，SDK 会自动完成编码和签名计算。

签名的详细计算方法请参考 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。
