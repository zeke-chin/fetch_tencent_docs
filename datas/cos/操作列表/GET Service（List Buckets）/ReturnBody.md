<!-- source: https://cloud.tencent.com/document/product/436/97529 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:41:47+08:00 -->

# ReturnBody

最近更新时间：2025-11-07 15:55:22


## 系统变量

上传回调 ReturnBody 支持使用的系统变量如下表所示：

**注意：**

exif、videoinfo、imageinfo 信息的获取依赖 [数据万象（Cloud Infinite，CI](https://cloud.tencent.com/document/product/460/60140)）服务的能力。获取这三类变量，会由 CI 服务收取相应的费用，详情可参考 [数据万象计费概述](https://cloud.tencent.com/document/product/460/6970)。

变量名 变量说明 是否包含子变量 是否必选
bucket 对象上传的目标存储桶。否 否
object 对象上传到存储桶内，使用的对象名称。否 否
size 对象大小，单位为 Byte。否 否
region 对象上传的存储桶所在地域。否 否
mimeType 对象元数据 Content-Type。否 否
exif 如果上传的对象为图片类型，支持查看图片的 exif 信息，变量填写格式为 `${exif.子变量}`。

**注意：**

为了避免 ReturnBody 携带的内容太多，影响接口性能，不建议直接填写`${exif}`，建议写明具体的子变量。是 否
videoInfo 如果上传的对象为音视频类型，支持查看音视频资源的元信息。变量填写格式为 `${videoInfo.子变量}`。

**注意：**

为了避免 ReturnBody 携带的内容太多，影响接口性能，不建议直接填写`${videoInfo}`，建议写明具体的子信息项。是 否
imageInfo 如果上传的对象为图片类型，支持查看图片的基本信息，变量填写格式为 `${imageInfo.子变量}`。

**注意：**

为了避免 ReturnBody 携带的内容太多，影响接口性能，不建议直接填写`${imageInfo}`，建议写明具体的子变量。是 否

其中，使用 exif、imageInfo、videoInfo 变量时，需要注意以下几点：

这三类变量仅支持在国内公有云地域使用。

获取这三类变量依赖数据万象（Cloud Infinite，CI）服务的能力。用户需要开通 CI 服务，并保证 COS 服务角色有权调用 CI 服务。获取这三类变量，会由CI 服务收取相应的费用，详情可参考 [数据万象计费概述](https://cloud.tencent.com/document/product/460/6970)。

支持子变量，例如`${变量名.子变量}`、`${变量名.二级子变量}`。并且，为了避免 ReturnBody 携带的内容太多，影响接口性能，**不建议**直接填写`${imageInfo}`，建议写明具体的子变量。

变量支持的具体子变量，可参考数据万象和媒体处理服务的产品文档：

**注意：**

exif、imageInfo 变量仅支持图片文件，videoInfo 仅支持音视频文件，格式不符将导致回调失败（错误码 203）。

exif：[获取图片 EXIF](https://cloud.tencent.com/document/product/460/6926)

imageInfo： [获取图片基本信息](https://cloud.tencent.com/document/product/460/6927)

videoInfo：[获取媒体信息](https://cloud.tencent.com/document/product/460/124610)

## 使用步骤

### 步骤一：构造 ReturnBody 参数

1. 将希望获取的对象信息以 json 格式表示。如下示例中 bucket、key、myfilesize、height 为用户可自定义的参数名称，变量名使用 `${}`包裹，变量名对应的值是需要获取的回调信息。ReturnBody 支持的变量名，请参见上方的 [系统变量](https://cloud.tencent.com/document/product/436/97529#system_var)。示例如下：

# 图片信息获取示例

{

 "bucket": "${bucket}",

 "key": "${object}",

 "myfilesize": "${size}",

 "height": "${imageInfo.height}"

}

# 视频信息获取示例 参照 [获取媒体信息](https://cloud.tencent.com/document/product/460/124610) 中 magicvar = 1 时的响应的内容

{

 "bucket":"${bucket}",

 "key":"${object}",

 "myfilesize":"${size}",

 "video_duration":"${videoInfo.format.duration}",

 "video_bitrate":"${videoInfo.format.bit_rate}"

}

2. 将以上 json 格式转换为字符串，并进行 Base64 编码。

# 图片信息获取示例

eyJidWNrZXQiOiAiJHtidWNrZXR9IiwgImtleSI6ICIke29iamVjdH0iLCAibXlmaWxlc2l6ZSI6ICIke3NpemV9IiwgImhlaWdodCI6ICIke2ltYWdlSW5mby5oZWlnaHR9In0=

# 视频信息获取示例

ewogICAgImJ1Y2tldCI6ICIke2J1Y2tldH0iLAogICAgImtleSI6ICIke29iamVjdH0iLAogICAgIm15ZmlsZXNpemUiOiAiJHtzaXplfSIsCiAgICAidmlkZW9fZHVyYXRpb24iOiAiJHt2aWRlb0luZm8uZm9ybWF0LmR1cmF0aW9ufSIsCiAgICAidmlkZW9fYml0cmF0ZSI6ICIke3ZpZGVvSW5mby5mb3JtYXQuYml0X3JhdGV9Igp9

### 步骤二：在上传对象的请求中携带 ReturnBody 参数

1. [PUT Object](https://cloud.tencent.com/document/product/436/7749) 请求中，通过请求头部 `x-cos-return-body` 传入 Base64 编码的结果。请求示例如下：

PUT /<ObjectKey> HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Content-Type: Content Type

Content-Length: Content Length

Content-MD5: MD5

x-cos-return-body: eyJidWNrZXQiOiAiJHtidWNrZXR9IiwgImtleSI6ICIke29iamVjdH0iLCAibXlmaWxlc2l6ZSI6ICIke3NpemV9IiwgImhlaWdodCI6ICIke2ltYWdlSW5mby5oZWlnaHR9In0=

Authorization: Auth String

[Object Content]

2. [POST Object](https://cloud.tencent.com/document/product/436/14690) 请求中，通过表单字段 `x-cos-return-body` 传入 Base64 编码的结果。

POST / HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Thu, 29 Aug 2019 07:39:34 GMT

Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryZBPbaoYE2gqeB21N

Content-Length: 1119

Connection: close

------WebKitFormBoundaryZBPbaoYE2gqeB21N

Content-Disposition: form-data; name="q-sign-algorithm"

sha1

------WebKitFormBoundaryZBPbaoYE2gqeB21N

Content-Disposition: form-data; name="q-ak"

AKIDLdDGwRp0KIuI9sZDeJG3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

------WebKitFormBoundaryZBPbaoYE2gqeB21N

Content-Disposition: form-data; name="q-key-time"

1759216346;1759217246

------WebKitFormBoundaryZBPbaoYE2gqeB21N

Content-Disposition: form-data; name="q-signature"

71f6d4a559axxxxxxxxxxxxxxxxxxxxxxxxx

------WebKitFormBoundaryZBPbaoYE2gqeB21N

Content-Disposition: form-data; name="policy"

eyJleHBpcmF0aW9uIjoiMjAyNS0wOS0zMFQwNzoyNzoyNi4wMDBaIiwiY29uZGl0aW9ucyI6W3sicS1zaWduLWFsZ29yaXRobSI6InNoYTEifSx7InEtYWsiOiJBS0lETGRER3dScDBLSXVJOXNaRGVKRzN4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHgifSx7InEtc2lnbi10aW1lIjoiMTc1OTIxNjM0NjsxNzU5MjE3MjQ2In0seyJidWNrZXQiOiJleGFtcGxlYnVja2V0LTEyNTAwMDAwMDAifSx7ImtleSI6ImV4YW1wbGVvYmplY3QifV19

------WebKitFormBoundaryZBPbaoYE2gqeB21N

Content-Disposition: form-data; name="x-cos-security-token"

ZflOqzkNb2266djz4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

------WebKitFormBoundaryZBPbaoYE2gqeB21N

Content-Disposition: form-data; name="key"

exampleobject

------WebKitFormBoundaryZBPbaoYE2gqeB21N

Content-Disposition: form-data; name="x-cos-return-body"

ewogICAgImJ1Y2tldCI6ICIke2J1Y2tldH0iLAogICAgImtleSI6ICIke29iamVjdH0iLAogICAgIm15ZmlsZXNpemUiOiAiJHtzaXplfSIsCiAgICAidmlkZW9fZHVyYXRpb24iOiAiJHt2aWRlb0luZm8uZm9ybWF0LmR1cmF0aW9ufSIsCiAgICAidmlkZW9fYml0cmF0ZSI6ICIke3ZpZGVvSW5mby5mb3JtYXQuYml0X3JhdGV9Igp9

------WebKitFormBoundaryZBPbaoYE2gqeB21N

Content-Disposition: form-data; name="file"; filename="example.mp4"

Content-Type: video/mp4

[Object Content]

------WebKitFormBoundaryZBPbaoYE2gqeB21N--

3. [Complete Multipart Upload](https://cloud.tencent.com/document/product/436/7742) 请求中，通过请求头部 x-cos-return-body 传入 Base64 编码的结果。

POST /exampleobject?uploadId=UploadId HTTP/1.1

Host: exmaplebucket-1250000000.cos.region.myqcloud.com

x-cos-return-body: ewogICAgImJ1Y2tldCI6ICIke2J1Y2tldH0iLAogICAgImtleSI6ICIke29iamVjdH0iLAogICAgIm15ZmlsZXNpemUiOiAiJHtzaXplfSIsCiAgICAidmlkZW9fZHVyYXRpb24iOiAiJHt2aWRlb0luZm8uZm9ybWF0LmR1cmF0aW9ufSIsCiAgICAidmlkZW9fYml0cmF0ZSI6ICIke3ZpZGVvSW5mby5mb3JtYXQuYml0X3JhdGV9Igp9

Date: GMT Date

Content-Type: application/xml

Content-Length: Content Length

Content-MD5: MD5

Authorization: Auth String

[Request Body]

### 步骤三：获取请求返回中的 ReturnBody 信息

1. [PUT Object](https://cloud.tencent.com/document/product/436/7749) 的返回，将按照 json 格式在响应体中返回对象信息。响应示例如下：

HTTP/1.1 200 OK

x-cos-request-id: NWU5MDNkZjVfYzVjNzJhMDlfMjVhNzNfMWMy****

{

 "bucket": "examplebucket-1250000000000",

 "height": "887",

 "key": "test.jpeg",

 "myfilesize": "214513"

}

2. [POST Object](https://cloud.tencent.com/document/product/436/14690) 的返回，将按照 json 格式在响应体中返回对象信息。响应示例如下：

HTTP/1.1 201 OK

x-cos-request-id: NWU5MDNkZjVfYzVjNzJhMDlfMjVhNzNfMWMy****

{

 "bucket": "examplebucket-1250000000000",

 "key": "test.mp4",

 "myfilesize": "214513",

 "video_duration": 1000,

 "video_bitrate": 1000

}

3. [Complete Multipart Upload](https://cloud.tencent.com/document/product/436/7742) 请求本身返回了 xml 请求体，其中包含了分块上传的相关的重要信息。因此，ReturnBody 相关信息（对象信息、ReturnBody 计算是否成功等）会被放在 XML 字段 ReturnBodyResult 中，返回给用户。

ReturnBodyResult 节点说明如下：

节点名称（关键字）父节点 描述 类型
ReturnBodyResult CompleteMultipartUploadResult ReturnBody 的结果信息。Container
Status CompleteMultipartUploadResult.ReturnBodyResult ReturnBody 获取是否成功。枚举值支持 200、203。

200表示上传成功、获取 ReturnBody 成功；

203表示上传成功，获取 ReturnBody 失败。Integer
Error CompleteMultipartUploadResult.ReturnBodyResult Status 为203时，说明获取 ReturnBody 失败。返回 Error，说明回调失败信息。Container
Code CompleteMultipartUploadResult.ReturnBodyResult 回调失败信息的错误码，例如 GetReturnBodyFailed。String
Message CompleteMultipartUploadResult.ReturnBodyResult ReturnBody 获取失败的错误信息。String
ReturnBody CompleteMultipartUploadResult.ReturnBodyResult Status 为200时，说明上传成功、回调成功，返回 ReturnBody。内容为 ReturnBody 的 json 字符串 Base64 编码后的字符串。String

响应示例如下：

HTTP/1.1 200 OK

Content-Type: application/xml

<CompleteMultipartUploadResult>

 <Location>http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject</Location>

 <Bucket>examplebucket-1250000000</Bucket>

 <Key>exampleobject</Key>

 <ETag>"aa259a62513358f69e98e******"</ETag>

 <ReturnBodyResult>

 <Status>200|203</Status>

 <!--Status为203时，说明ReturnBody失败，返回 Error-->

 <Error>

 <Code>GetReturnBodyFailed</Code>

 <Message>Invalid return body params.</Message>

 </Error>

 <!--Status为200时，说明上传成功、ReturnBody计算成功，返回 json 字符串 base64 编码后的结果。-->

 <ReturnBody>

 eyJhIjogImIifQ==

 </ReturnBody>

 </ReturnBodyResult>

</CompleteMultipartUploadResult>

## 返回码

在上传请求中使用 ReturnBody 参数后，返回码主要有以下几种情况：

上传请求成功，获取 ReturnBody 成功，返回200。

上传请求成功，获取 ReturnBody 失败：

失败原因 返回码 ErrorCode Message
ReturnBody 参数不合法。203 GetReturnBodyFailed Invalid return body params.
调用数据万象服务，由于访问无权限、未开通服务等原因导致参数获取失败。203 GetReturnBodyFailed Error status from ci: ${code}, should return 200 OK.

其中，`${code}`为数据服务返回的错误码，例如 400、403等。

上传失败。将不会触发 ReturnBody 计算，返回的错误码和信息遵循普通上传请求的规则。

## 最佳实践

详情请参见 [如何在上传文件请求回包中返回文件信息](https://cloud.tencent.com/document/product/436/102797)。
