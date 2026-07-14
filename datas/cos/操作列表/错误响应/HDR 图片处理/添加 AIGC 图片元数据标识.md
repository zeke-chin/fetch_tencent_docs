<!-- source: https://cloud.tencent.com/document/product/436/124900 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:47:10+08:00 -->

# 添加 AIGC 图片元数据标识

最近更新时间：2025-11-11 18:11:12


## 功能概述

腾讯云数据万象通过 **imageMogr2**接口提供为图片添加 AIGC 元数据标识的能力。该功能支持以下处理方式：

上传时处理

云上数据处理

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加对应的权限，具体请参见 [COS action](https://cloud.tencent.com/document/product/598/69901)，数据万象支持的所有操作接口请参见 [action](https://cloud.tencent.com/document/product/598/98114)。

上传时处理：授权策略中 action 设置为 `cos:PutObject`。

云上数据处理：授权策略中 action 设置为 `cos:PutObject`。

**注意：**

PutObject 对应的 resource 为转存的文件。

## 服务开通

首次使用该功能时将默认为您开通数据万象，同时该存储桶将自动绑定数据万象，即可直接使用。

**注意：**

数据万象绑定后，如果您手动对存储桶进行数据万象的解绑操作，将无法继续使用该功能。

## 使用限制

图片格式限制：JPG/JPEG、PNG、AVIF。

更多使用限制，详情请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620#Image-processing)。

## 费用说明

该接口为付费服务，将产生图片基础处理费用，具体的费用明细及免费额度，可参见 [图片处理费用](https://cloud.tencent.com/document/product/460/58117)。

## 接口示例

### 方式一：上传时处理

图片上传的请求包与 COS V5上传文件接口一致，只在请求包头部增加图片处理参数。

也支持 COS V5的分块上传功能，您在使用 COS V5的 [Complete Multipart Upload](https://cloud.tencent.com/document/product/436/7742) 接口时只需在请求包头部中加入 Pic-Operations 项，即可实现处理。

PUT /<ObjectKey> HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Authorization: Auth String

Pic-Operations:

{

 "is_pic_info": 1,

 "rules": [{

 "fileid": "exampleobject",

 "rule": "imageMogr2/AIGCMetadata/Label/<Label>

 /ContentProducer/<ContentProducer>

 /ProduceID/<ProduceID>

 /ReservedCode1/<ReservedCode1>

 /ContentPropagator/<ContentPropagator>

 /PropagateID/<PropagateID>

 /ReservedCode2/<ReservedCode2>"

 }]

}

### 方式二：云上数据处理

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

 "rule": "imageMogr2/AIGCMetadata/Label/<Label>

 /ContentProducer/<ContentProducer>

 /ProduceID/<ProduceID>

 /ReservedCode1/<ReservedCode1>

 /ContentPropagator/<ContentPropagator>

 /PropagateID/<PropagateID>

 /ReservedCode2/<ReservedCode2>"

 }]

}

**说明：**

<ObjectKey>：对象文件名，例如 folder/sample.jpg。

Authorization: 携带鉴权信息，用于验证请求的合法性的请求头，Pic-Operations 头部需签入签名信息中，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

### 处理参数说明

AIGC 打标参数通过请求头中的 Pic-Operations 字段进行使用，Pic-Operations 请求头的值为 json 格式的字符串，具体参数如下：

参数名称 描述 类型 是否必选
is_pic_info 是否返回原图信息，0不返回原图信息，1返回原图信息，默认为0。Int 否
rules 处理规则，一条规则对应一个处理结果（最多支持五条规则）。Array 是

rules 中每一项具体参数如下：

参数名称 描述 类型 是否必选
bucket 存储图片的存储桶名称。String 是
fileid 处理后文件的保存路径及名称。

当 `fileid` 与 `ObjectKey` 相同时，处理后的文件将覆盖原文件存储；不相同时将分别存储原文件和处理后文件。

**名称规则说明：**

名称需要经过 URLEncode。

以`/`开头为绝对路径，例如 `fileid` 值为 /p2/test2.jpg 时，表示在 p2文件夹中存储了一个文件名为 test2.jpg 的文件。

不以`/`开头为相对路径，例如 `fileid` 值为 p2/test2.jpg 时，表示在 ObjectKey 所在的文件夹中新建了一个 p2文件夹，然后在 p2文件夹中存储了一个文件名为 test2.jpg 的文件。

**注意：请不要以**`/`**结尾，否则会产生空文件名。**String 是
rule 具体的AIGC元数据标识的参数内容，格式为：`imageMogr2/AIGCMetadata/Label/<Label>/ContentProducer/<ContentProducer>/ProduceID/<ProduceID>/ReservedCode1/<ReservedCode1>/ContentPropagator/<ContentPropagator>/PropagateID/<PropagateID>/ReservedCode2/<ReservedCode2>`

可通过 [管道操作符](https://cloud.tencent.com/document/product/460/15293) 与图片裁剪、格式转换等图片基础处理一同使用。String 是

rule 中 AIGC 打标参数的具体说明（不同参数间通过反斜杠/分隔）：

参数 含义 类型 是否必选
imageMogr2/AIGCMetadata AIGC 打标固定字段，必填。String 是
/Label/<Label>AIGC 元数据中的Label字段，用于表示内容是否为AI生成合成的，填写的值需要经过 [URL 安全的 Base64编码](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39)。String 是
/ContentProducer/<ContentProducer>AIGC 元数据中的ContentProducer字段，用于表示AI生产方的业务标识，填写的值需要经过 [URL 安全的 Base64编码](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39)。String 是
/ProduceID/<ProduceID>AIGC 元数据中的ProduceID字段，用于表示AI生产方的文件标识，填写的值需要经过 [URL 安全的 Base64编码](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39)。String 是
/ReservedCode1/<ReservedCode1>AIGC 元数据中的 ReservedCode1字段，用于表示AI生产方提供的防止数据篡改的标识，填写的值需要经过 [URL 安全的 Base64编码](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39)。String 否
/ContentPropagator/<ContentPropagator>AIGC 元数据中的 ContentPropagator 字段，用于表示 AI 传播方的业务标识，填写的值需要经过 [URL 安全的 Base64编码](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39)。String 否
/PropagateID/<PropagateID>AIGC 元数据中的 PropagateID 字段，用于表示AI传播方的文件标识，填写的值需要经过 [URL 安全的 Base64编码](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39)。String 否
/ReservedCode2/<ReservedCode2>AIGC 元数据中的 ReservedCode2字段，用于表示 AI 传播方提供的防止数据篡改的标识，填写的值需要经过 [URL 安全的 Base64编码](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39)。String 否

### 返回内容

<UploadResult>

 <OriginalInfo>

 <Key>exampleobject</Key>

 <Location>examplebucket-1250000000.cos.ap-chengdu.myqcloud.com/exampleobject.jpg</Location>

 <ETag>&quot;580cd6930*******fc2d5484&quot;</ETag>

 <ImageInfo>

 <Md5>80cd6930*******fc2d5</Md5>

 <Format>JPEG</Format>

 <Width>640</Width>

 <Height>427</Height>

 <Quality>100</Quality>

 <Ave>0xa18454</Ave>

 <Orientation>1</Orientation>

 <FrameCount>1</FrameCount>

 <BitDepth>8</BitDepth>

 <VerticalDpi>0</VerticalDpi>

 <HorizontalDpi>0</HorizontalDpi>

 </ImageInfo>

 </OriginalInfo>

 <ProcessResults>

 <Object>

 <Key>test.png</Key>

 <Location>examplebucket-1250000000.cos.ap-chengdu.myqcloud.com/test.png</Location>

 <Format>png</Format>

 <Md5>6930*******fc2</Md5>

 <Width>640</Width>

 <Height>427</Height>

 <Size>463092</Size>

 <Quality>100</Quality>

 <ETag>&quot;eaa4e3d8f*******61f23e3f0c&quot;</ETag>

 <FrameCount>1</FrameCount>

 <BitDepth>8</BitDepth>

 <VerticalDpi>0</VerticalDpi>

 <HorizontalDpi>0</HorizontalDpi>

 <AIGCMetadata>

 <Label>1</Label>

 <ContentProducer>0012AF****</ContentProducer>

 <ProduceID>test-1</ProduceID>

 <ReservedCode1>***</ReservedCode1>

 <ContentPropagator>0012AF****</ContentPropagator>

 <PropagateID>test-1</PropagateID>

 <ReservedCode2>***</ReservedCode2>

 </AIGCMetadata>

 </Object>

 </ProcessResults>

</UploadResult>

响应包体具体数据内容如下：

参数名称 类型 描述
UploadResult Container 处理结果信息

 UploadResult 节点内容：

参数名称 类型 描述
OriginalInfo Container 原图信息
ProcessResults Container 处理图信息

 OriginalInfo 节点内容：

节点名称 类型 描述
Key String 原图文件名
Location String 原图路径
ImageInfo Container 原图图片信息
ETag String 原图 ETag 信息（若处理结果图覆盖原图则为结果图 ETag 信息）

 ImageInfo 节点内容：

节点名称 类型 描述
Md5 String 校验值，Md5用于文件完整性校验、避免重复上传和标识文件的唯一性
Format String 图片格式
Width Int 图片宽度
Height Int 图片高度
Quality Int 图片质量
Ave String 图片主色调，格式为：0xRRGGBB （RR、GG、BB都是十六进制数，表示红、绿、蓝三种颜色）
Orientation Int 图片的EXIF旋转角度
FrameCount Int 图片的帧数。静态图为1，动图为对应的帧数.
BitDepth Int 图像每个颜色通道所使用的比特数，反映图像的色彩精度
VerticalDpi Int 图像垂直方向的分辨率
HorizontalDpi Int 图像水平方向的分辨率

 ProcessResults 节点内容：

节点名称 类型 描述
Object Container 每一个图片处理结果

 Object 节点内容：

节点名称 类型 描述
Key String 文件名
Location String 图片路径
Format String 图片格式
Md5 String 校验值，Md5用于文件完整性校验、避免重复上传和标识文件的唯一性
Width Int 图片宽度
Height Int 图片高度
Size Int 图片大小
Quality Int 图片质量
FrameCount Int 图片的帧数。静态图为1，动图为对应的帧数。
BitDepth String 图像每个颜色通道所使用的比特数，反映图像的色彩精度。
VerticalDpi Int 图像垂直方向的分辨率。
HorizontalDpi Int 图像水平方向的分辨率。
ETag Int 处理结果图 ETag 信息。
AIGCMetadata Container 已打上的 AIGC 元数据标识内容。

## 实际案例

上传一张 AI 生成的图片到存储桶 examplebucket-1250000000中，同时进行元数据打标和转换图片格式为 webp

#### 请求

PUT /filename.jpg HTTP/1.1

Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com

Date: Wed, 28 Oct 2025 20:32:00 GMT

Authorization:q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=****************************************

Pic-Operations:{"rules":[{"bucket":"examplebucket-1250000000","fileid":"test.webp","rule":"imageMogr2/format/webp/AIGCMetadata/Label/MQ/ContentProducer/MDAxMioqKg/ProduceID/dGVzdA/ReservedCode1/MTIz/ContentPropagator/MDAxMioqKg/PropagateID/dGVzdA/ReservedCode2/MTIz"}]}

Content-Length: 64

[Object]

#### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 645

Date: Wed, 28 Oct 2025 20:32:00 GMT

Status: 200 OK

x-cos-request-id: NWFjMzQ0MDZfOTBmYTUwXzZkZV8z****


<UploadResult>

 <OriginalInfo>

 <Key>filename.jpg</Key>

 <Location>examplebucket-1250000000.cos.ap-chengdu.myqcloud.com/filename.jpg</Location>

 <ETag>&quot;580cd6930444576523c25f86ce2af9b1fc2d5484&quot;</ETag>

 <ImageInfo>

 <Format>PNG</Format>

 <Width>640</Width>

 <Height>427</Height>

 <Quality>100</Quality>

 <Ave>0xa18454</Ave>

 <Orientation>1</Orientation>

 <FrameCount>1</FrameCount>

 <BitDepth>8</BitDepth>

 <VerticalDpi>0</VerticalDpi>

 <HorizontalDpi>0</HorizontalDpi>

 </ImageInfo>

 </OriginalInfo>

 <ProcessResults>

 <Object>

 <Key>test.png</Key>

 <Location>examplebucket-1250000000.cos.ap-chengdu.myqcloud.com/test.webp</Location>

 <Format>png</Format>

 <Width>640</Width>

 <Height>427</Height>

 <Size>463092</Size>

 <Quality>100</Quality>

 <ETag>&quot;eaa4e3d8fd498bbc63be3b71c46b9c61f23e3f0c&quot;</ETag>

 <FrameCount>1</FrameCount>

 <BitDepth>8</BitDepth>

 <VerticalDpi>0</VerticalDpi>

 <HorizontalDpi>0</HorizontalDpi>

 <AIGCMetadata>

 <Label>1</Label>

 <ContentProducer>0012***</ContentProducer>

 <ProduceID>test</ProduceID>

 <ReservedCode1>MTIz</ReservedCode1>

 <ContentPropagator>0012***</ContentPropagator>

 <PropagateID>test</PropagateID>

 <ReservedCode2>MTIz</ReservedCode2>

 </AIGCMetadata>

 </Object>

 </ProcessResults>

</UploadResult>
