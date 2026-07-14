<!-- source: https://cloud.tencent.com/document/product/436/121098 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:54:41+08:00 -->

# 文档预览 JS SDK 接入

最近更新时间：2026-04-10 16:39:32


## 功能说明

通过使用 JS-SDK，网页开发者可以自定义界面显示、页面状态、监听事件等能力，为用户提供更优质的网页体验。

## 实现原理

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/e4aaaf20b650c7f8ea38c76f76b05249.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/e4aaaf20b650c7f8ea38c76f76b05249.png)

## 使用环境

平台 支持浏览器
iOS Safari、QQ 内置浏览器、QQ 小程序、微信内置浏览器、微信小程序（仅支持 webview 方式接入）
Android QQ 内置浏览器、QQ 小程序、微信内置浏览器、微信小程序（仅支持 webview 方式接入）
Windows Chrome、QQ 浏览器（非兼容模式）、Edge、火狐、IE11
Mac OS X Chrome、Safari、QQ 浏览器、Edge、火狐

## 前提条件

使用该功能需提前通过 [控制台](https://cloud.tencent.com/document/product/460/46499) 或 [接口](https://cloud.tencent.com/document/product/460/103608) 开通文档处理服务。

## 接入步骤

### 1. 下载

请下载最新版本的 [JS-SDK 包](https://cosbrowser.cloud.tencent.com/code/doc-preview/ci-doc-preview-sdk.zip)。历史版本前往 [更新日志](https://cloud.tencent.com/document/product/460/75908)。

### 2. 引入 JS-SDK

在需要调用的页面引入如下 JS-SDK。示例中`${version}`表示版本号，请根据下载的实际版本号填写。

<script src="sdk-${version}.js"></script>

### 3. 获取在线文档预览地址

#### 方法一：使用 JS-SDK 获取（支持 sdk-v0.1.1及以上版本）

通过 JS-SDK（v0.1.1及以上版本）获取在线文档预览地址，示例如下：

var url = await COSDocPreviewSDK.getPreviewUrl( {

 objectUrl: 'https://examplebucket-1250000000.cos.ap-shanghai.myqcloud.com/test.pptx',

 credentials: { // 如果预览文件是私有的，则需要携带访问凭证。

 secretId: '',

 secretKey: '',

 authorization: 'q-sign-algorithmxxxxxxxxxxxxxxx',

 },

 copyable: 0, // 是否可以复制文件内容

 htmlwaterword: '' // 水印内容

})

console.log(url)

配置项说明如下：

配置项 说明 类型 是否必选
objectUrl 需要预览的对象地址，例如：`https://examplebucket-1250000000.cos.ap-shanghai.myqcloud.com/test.pptx`String 是
credentials 如果预览的对象是私有，则需要传入 credentials 作为访问凭证。可以传入计算好的 [请求签名](https://cloud.tencent.com/document/product/460/6968) Authorization，也可以传入用户的 secretId 和 secretKey（固定密钥放在前端会有安全风险，不推荐此方式）Object 否
credentials.authorization 对象下载签名，详情请参见 [请求签名](https://cloud.tencent.com/document/product/460/6968) 文档 String 否
credentials.secretId 用户的 secretId，可前往访问管理控制台中的 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取 String 否
credentials.secretKey 用户的 secretKey，可前往访问管理控制台中的 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取 String 否
copyable 是否可复制。默认为可复制，填入值为1；不可复制，填入值为0 Int 否
htmlwaterword 水印文字，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39) 的 Base64编码，默认为空 String 否
htmlfillstyle 水印 RGBA（颜色和透明度），需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39) 的 Base64编码，默认为：rgba(192,192,192,0.6)String 否
htmlfront 水印文字样式，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39) 的 Base64编码，默认为：bold 20px Serif String 否
htmlrotate 旋转角度，0 - 360，默认315度 Int 否
htmlhorizontal 水印文字水平间距，单位 px，默认为50 Int 否
htmlvertical 水印文字垂直间距，单位 px，默认为100 Int 否

#### 方法二：直接请求获取

##### 请求示例

GET /<ObjectKey>?ci-process=doc-preview&dstType=html&weboffice_url=1&sign=AuthString HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

##### 请求参数

参数名称 描述 类型 是否必选
ci-process 预览固定参数，值为 doc-preview String 是
dstType 预览类型，如需预览生成类型为 html 则填入 html String 是
weboffice_url 是否获取预览链接。填入值为1会返回预览链接和 Token 信息；填入值为2只返回 Token 信息；不传会直接预览 Int 否
tokenuid 是否获取 token。根据传入的 tokenuid、文件信息等生成 Token，返回 Token 和有效期；如果不传则不会返回 Token 信息 String 否
sign 对象下载签名，如果预览的对象为私有读时，需要传入签名，详情请参见 [请求签名](https://cloud.tencent.com/document/product/460/6968) 文档

注意：需要进行 urlencode String 否
copyable 是否可复制。默认为可复制，填入值为1；不可复制，填入值为0 Int 否
htmlwaterword 水印文字，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39) 的 Base64编码，默认为空 String 否
htmlfillstyle 水印 RGBA（颜色和透明度），需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39) 的 Base64编码，默认为：rgba(192,192,192,0.6)String 否
htmlfront 水印文字样式，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39) 的 Base64编码，默认为：bold 20px Serif String 否
htmlrotate 旋转角度，0 - 360，默认315度 Int 否
htmlhorizontal 水印文字水平间距，单位 px，默认为50 Int 否
htmlvertical 水印文字垂直间距，单位 px，默认为100 Int 否

##### 响应示例

HTTP/1.1 200 OK

Content-Type: text/html

Content-Length: 478

Date: Thu, 25 Feb 2021 07:44:37 GMT

Status: 200 OK

x-cos-request-id: NjAzNzU1NjVfY2MxZTIzMDlfNzc5NF8yMDQ5****

{

 "PreviewUrl": "https://prvsh.myqcloud.com/office/p/xxxx?_w_provider=XXX"

}

### 4. 初始化

通过初始化配置，JS-SDK 会在配置的 mount 节点下创建一个 iframe，并自动初始化相关数据和事件。

var demo = COSDocPreviewSDK.config({

 url: '在线文档预览地址', // 步骤3中获取到的在线文档预览地址

})

// 如果需要对 iframe 进行特殊的处理，可以通过以下方式拿到 iframe 的 dom 对象

console.log(demo.iframe)

// 打开文档结果

demo.on('fileOpen', function(data) {

 console.log(data.success)

})

### 5. 挂载节点

挂载节点指 JS-SDK 插入 iframe 时挂载的节点。在初始化时，JS-SDK 挂载节点为可配置项。

<div class="custom-mount"></div>

var demo = COSDocPreviewSDK.config({

 url: '在线文档预览地址', // 步骤3中获取到的在线文档预览地址

 mount: document.querySelector('.custom-mount') // 挂载节点，默认会挂载到 body 下，可根据需要自定义加载节点

})

JS-SDK 初始化完成后会自动在挂载节点下面插入一个 iframe。

<div class="custom-mount">

 <iframe src="..."></iframe>

</div>

### 6. Token 鉴权

不使用 Token 时，默认使用文档的签名有效期鉴权，过期则无法预览文件。 使用 Token 鉴权可以在预览期间持续进行 Token 鉴权和 Token 续期，由业务侧自主控制预览授权。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/12c6e5b55126ed39bd154f143656370b.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/12c6e5b55126ed39bd154f143656370b.png)

Token 鉴权与续期分为以下三个步骤，详情请参见 [Demo 示例](https://github.com/tencentyun/cos-demo/blob/main/doc-preview/token-refresh-preview.html)。

1. 获取 Token **请求示例**

GET /<ObjectKey>?ci-process=doc-preview&dstType=html&weboffice_url=2&tokenuid=test&sign=AuthString HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

**响应示例**

HTTP/1.1 200 OK

Content-Type: text/html

Content-Length: 108

Date: Tue, 21 Jun 2022 10:41:10 GMT

Status: 200 OK

x-cos-request-id: NjJiMWEwNDZfMTgyMjYyNjRfYmRlYl9iNTAw****

{

 Token: "ChAJj2vNRiHTc8reToMmJ7T2EJ7FxpUGGhS1mPJanpN03u8PSB17/YKBA/Vo****"

 TokenExpireTime: "1655808670"

}

2. 设置 Token

**说明**

避免 Token 刷新过于频繁，推荐设置的超时时间（timeout）为 10 分钟以上。为避免 refresh 请求超时，JS-SDK 会提前几分钟去更新 Token。

var demo = COSDocPreviewSDK.config({

 url: '在线文档预览地址', // 步骤3中获取到的在线文档预览地址

})

// 设置Token

demo.setToken({

 token: 'yourToken', // 填入获取到的token

 timeout: 10 * 60 * 1000, // token超时时间，单位为毫秒，避免频繁续期，建议设置 10 分钟及以上，JS-SDK将在超时前调用更新Token的方法（refreshToken）

});

3. 配置 refreshToken 方法，超时自动续期 Token refreshToken 方法需要请求**您的服务端封装的更新 Token 的方法**，服务端可以封装上述的获取 Token 的方法（参考 [获取 Token Demo](https://github.com/tencentyun/cos-demo/blob/main/doc-preview/token-refresh-preview.html)）。 以服务端方法`http://your.server.com/refreshToken`为例，配置 refreshToken 函数如下：

// 获取 Token 函数，返回同步对象或 Promise 实例，暂不支持 aysnc 函数写法。

const refreshToken = function () {

 // 可以返回 Promise 实例或者 return { token, timeout }

 return new Promise(function (resolve, reject) {

 // 调用服务端封装的方法，获取token信息

 $.get('http://your.server.com/refreshToken').then((tokenInfo) => {

 resolve({

 token: tokenInfo.token, // 必需：您需要设置的 Token

 timeout: 10 * 60 * 1000, // 必需：Token 超时时间，单位毫秒

 });

 }).catch((err) => {

 reject(err);

 });

 });

};

var demo = COSDocPreviewSDK.config({

 url: '在线文档预览地址',

 refreshToken // Token 超时自动更新的回调方法

})

// 首次进入，需要设置 Token

demo.setToken({

 token: 'yourToken', // 填入获取到的token

 timeout: 10 * 60 * 1000 // token超时时间，单位为毫秒

});

## 实际案例

文字文件在线预览案例，参考 [DOC 预览案例](https://github.com/tencentyun/cos-demo/blob/main/doc-preview/doc-to-html-preview.html)。

演示文件在线预览案例，参考 [PPT 预览案例](https://github.com/tencentyun/cos-demo/blob/main/doc-preview/ppt-to-html-preview.html)。

表格文件在线预览案例，参考 [Excel 预览案例](https://github.com/tencentyun/cos-demo/blob/main/doc-preview/xls-to-html-preview.html)。

PDF 文件在线预览案例，参考 [PDF 预览案例](https://github.com/tencentyun/cos-demo/blob/main/doc-preview/pdf-to-html-preview.html)。

Token 鉴权与续期案例，参考 [Token 鉴权与续期案例](https://github.com/tencentyun/cos-demo/blob/main/doc-preview/token-refresh-preview.html)。
