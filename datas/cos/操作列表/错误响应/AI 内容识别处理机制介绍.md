<!-- source: https://cloud.tencent.com/document/product/436/121110 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:51:39+08:00 -->

# AI 内容识别处理机制介绍

最近更新时间：2025-12-30 10:10:52


## 简介

数据万象提供了一套便捷的 AI 处理机制，通过这套机制可以对存储在对象存储 COS 中的图片、文字等进行一系列的 AI 内容识别处理操作。

AI 处理机制分为以下三种方式：

方式 类别 说明
下载时处理 同步处理 在图片的 URL 后加上 AI 处理参数 。
上传时处理 持久化处理 上传图片时，在请求包头部中加入 Pic-Operations 项并设置好相应的 AI 处理参数 。
云上数据处理 持久化处理 针对 COS 上已经存在的图片进行处理，处理方式与上传时处理类似，在请求包头部中加入 Pic-Operations 项并设置好相应的 AI 处理参数 。

## 处理方式一：下载时处理

您可以通过在图片的 URL 后加上 AI 处理处理参数参数，实现访问图片的时候同步获取到处理后的图片。

### 请求语法

GET /<ObjectKey>?<AI处理参数> HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

### 示例

GET /<ObjectKey>?ci-process=AISuperResolution HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

### 响应

HTTP/1.1 200 OK

Content-Type: image/png

Content-Length: 98645

Date: Tue, 23 Apr 2022 09:06:16 GMT

Status: 200 OK

x-cos-request-id: NWFjMzQ0MDZfOTBmYTUwXzZkZV8z****

[pic-content]

处理后的图片直接返回至响应体。

## 处理方式二：上传时处理

上传时处理功能可以帮助使用者在上传时实现图片处理。您只需要在请求包头部中加入 Pic-Operations 项并设置好相应的 ，就可在图片上传时实现相应的 AI 内容内容识别识别处理，并可将原图和处理结果存入到 COS。

### 请求语法

PUT /<ObjectKey> HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Authorization: Auth String

Pic-Operations: <PicOperations>

**说明：**

Authorization: 携带鉴权信息，用于验证请求的合法性的请求头，Pic-Operations 头部需签入签名信息中，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

### 请求内容

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。 除公共头部外，还需要传入如下头部：

头部名称 描述 类型
Pic-Operations 对图片进行操作的参数 String

Pic-Operations 为 json 格式的字符串，具体参数如下：

参数名称 类型 是否必选 描述
is_pic_info Int 否 是否返回原图信息，0不返回原图信息，1返回原图信息，默认为0。
rules Array 否 处理规则，一条规则对应一个处理结果（目前支持五条规则），不填则不进行图片处理。

rules（json 数组）中每一项具体参数如下：

参数名称 类型 是否必选 描述
bucket String 否 存储结果的目标存储桶名称，格式为 BucketName-AppId，如果不指定的话默认保存到当前存储桶。
fileid String 是 处理后文件的保存路径及名称。名称规则说明：

例如源文件的路径及文件名为：/p1/test1.jpg。

1. 以/开头为绝对路径，例如 fileid 值为 /p2/test2.jpg 时，表示在 p2 文件夹中存储了一个文件名为 test2.jpg 的文件。

2. 不以/开头为相对路径，例如 fileid 值为 p2/test2.jpg 时，表示在 p1 文件夹中新建了一个 p2 文件夹，然后在 p2 文件夹中存储了一个文件名为 test2.jpg 的文件。

3. 注意：请不要以/结尾，否则会产生空文件名。

4. 如希望修复后的图片覆盖原图，请将 fileid 字段设置为<ObjectKey>。
rule String 是 处理参数，示例：ci-process=AIImageColoring。

### 示例

#### 请求

PUT /<ObjectKey> HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Authorization: Auth String

Pic-Operations:

{

"is_pic_info": 1,

"rules": [{

"fileid": "exampleobject",

"rule": "ci-process=AIImageColoring"

}]

}

#### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 645

Date: Tue, 23 Apr 2022 09:06:16 GMT

Status: 200 OK

Server: tencent-ci

x-cos-request-id: NWFjMzQ0MDZfOTBmYTUwXzZkZV8z****

<UploadResult>

 <OriginalInfo>

 <Key>ObjectKey</Key>

 <Location>examplebucket-1250000000.cos.ap-chengdu.myqcloud.com/filename.jpg</Location>

 <ETag>"ed60e3598e6862d8c8443a06acfb2153"</ETag>

 </OriginalInfo>

 <ProcessResults>

 <Object>

 <Key>exampleobject</Key>

 <Location>examplebucket-1250000000.cos.ap-chengdu.myqcloud.com/exampleobject</Location>

 <Format/>

 <Size>354256</Size>

 <ETag>"521451f63c331becf533e466732c1091"</ETag>

 </Object>

 </ProcessResults>

</UploadResult>

## 处理方式三：云上数据处理

### 请求

#### 请求语法

POST /<ObjectKey>?image_process HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Authorization: Auth String

Pic-Operations: <PicOperations>

**说明：**

Authorization: 携带鉴权信息，用于验证请求的合法性的请求头，Pic-Operations头部需签入签名信息中，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。 除公共头部外，还需要传入如下头部：

头部名称 描述 类型
Pic-Operations 对图片进行操作的参数 String

Pic-Operations 为 json 格式的字符串，具体参数如下：

参数名称 类型 是否必选 描述
is_pic_info Int 否 是否返回原图信息，0不返回原图信息，1返回原图信息，默认为0。
rules Array 否 处理规则，一条规则对应一个处理结果（目前支持五条规则），不填则不进行图片处理。

rules（json 数组）中每一项具体参数如下：

参数名称 类型 是否必选 描述
bucket String 否 存储结果的目标存储桶名称，格式为 BucketName-AppId，如果不指定的话默认保存到当前存储桶。
fileid String 是 处理后文件的保存路径及名称。名称规则说明：

例如源文件的路径及文件名为：/p1/test1.jpg。

1. 以/开头为绝对路径，例如 fileid 值为 /p2/test2.jpg 时，表示在 p2 文件夹中存储了一个文件名为 test2.jpg 的文件。

2. 不以/开头为相对路径，例如 fileid 值为 p2/test2.jpg 时，表示在 p1 文件夹中新建了一个 p2 文件夹，然后在 p2 文件夹中存储了一个文件名为 test2.jpg 的文件。

3. 注意：请不要以/结尾，否则会产生空文件名。

4. 如希望修复后的图片覆盖原图，请将 fileid 字段设置为<ObjectKey>。
rule String 是 处理参数，示例为：ci-process=AIImageColoring。

### 示例

#### 请求

POST /<ObjectKey>?image_process HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Content-length: Size

Authorization: Auth String

Pic-Operations:

{

"rules": [{

"fileid": "exampleobject",

"rule": "ci-process=AIImageColoring"

}]

}

处理后的图片存至存储桶，并以fileid字段的值作为对象名称。

#### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 645

Date: Tue, 23 Apr 2022 09:06:16 GMT

Status: 200 OK

Server: tencent-ci

x-cos-request-id: NWFjMzQ0MDZfOTBmYTUwXzZkZV8z****

<UploadResult>

 <OriginalInfo>

 <Key>ObjectKey</Key>

 <Location>examplebucket-1250000000.cos.ap-chengdu.myqcloud.com/filename.jpg</Location>

 <ETag>"ed60e3598e6862d8c8443a06acfb2153"</ETag>

 </OriginalInfo>

 <ProcessResults>

 <Object>

 <Key>exampleobject</Key>

 <Location>examplebucket-1250000000.cos.ap-chengdu.myqcloud.com/exampleobject</Location>

 <Format/>

 <Size>354256</Size>

 <ETag>"521451f63c331becf533e466732c1091"</ETag>

 </Object>

 </ProcessResults>

</UploadResult>
