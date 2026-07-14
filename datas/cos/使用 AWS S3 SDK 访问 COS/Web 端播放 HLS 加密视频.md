<!-- source: https://cloud.tencent.com/document/product/436/106772 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:18:02+08:00 -->

# Web 端播放 HLS 加密视频

最近更新时间：2025-08-29 15:03:52


## 前提条件

1. **创建加密视频**、**搭建 token 服务**，详情请参见 [HLS 视频加密播实践](https://cloud.tencent.com/document/product/460/59291)。

2. **配置 CORS 规则**：由于 Web 端播放会对播放地址 ajax 跨域请求，需要在 COS 控制台或 CDN 控制台配置 [CORS 规则](https://cloud.tencent.com/document/product/436/11488)，允许播放页跨域访问资源。

## Web 端播放指引

1. **下载播放代码库**：首先下载 [JS 播放代码库](https://cosbrowser.cloud.tencent.com/code/hls/cos_hls.zip)，解压得到 cos_hls.js、jsencrypt.js 和 hls.js。

2. **引入到播放页面**：根据播放器种类，在自己页面中引入文件，目前支持三种类型（hls.js/tcplayer/video.js）。

**hls.js 引用示例**：

<script src="./hls.js"></script>

<script src="./cos_hls_sdk.js"></script>

**tcplayer 引用示例**：

<link href="https://web.sdk.qcloud.com/player/tcplayer/release/v5.1.0/tcplayer.min.css" rel="stylesheet">

<script src="https://web.sdk.qcloud.com/player/tcplayer/release/v5.1.0/libs/hls.min.1.1.7.js"></script>

<script src="https://web.sdk.qcloud.com/player/tcplayer/release/v5.1.0/tcplayer.v5.1.0.min.js"></script>

<script src="./cos_hls_sdk.js"></script>

**video.js 引用示例**：

<link href="https://vjs.zencdn.net/8.11.8/video-js.css" rel="stylesheet" />

<script src="https://vjs.zencdn.net/8.11.8/video.js"></script>

<script src="./cos_hls_sdk.js"></script>

3. **调用播放的方法**：前端使用 cos_hls.js 文件封装好的 cosHls 对象来播放加密的 m3u8视频文件，cosHls 对象的 play 方法**参数说明**如下：

参数名 说明 是否必填 类型 默认值
container video 标签的默认值 是 String 无
playerType 播放器种类（hls.js/tcplayer/video.js）是 String 无
playerOptions 播放器参数，在创建播放器是（hls.js/tcplayer/video.js）传入。否 Object 无

**调用播放的代码示例**：

<script>

// 请求服务端获取带有 token 和 签名 的 playUrl

const getPlayUrl = function (opt) {

 return new Promise(function (resolve, reject) {

 var xhr = new XMLHttpRequest();

 xhr.withCredentials = true;

 xhr.open('POST', `/hls/getPlayUrl`, true);

 xhr.setRequestHeader('Content-Type', 'application/json')

 xhr.onload = function () {

 var r = JSON.parse(xhr.responseText);

 resolve(r.playUrl);

 };

 xhr.onerror = function () {

 reject('get getPlayUrl error');

 };

 var data = {

 objectKey: opt.objectKey,

 publicKey: opt.publicKey,

 protectContentKey: opt.protectContentKey,

 };

 xhr.send(JSON.stringify(data));

 });

};

// 播放视频

const playVideo = async function () {

 const params = CosHlsSdk.createTokenParams();

 const opt = {

 // 这里根据业务需要，可以传自己业务逻辑里的视频 id，方便服务端知晓是播放哪个 objectKey

 objectKey: 'encrypt/bunny.m3u8',

 // publicKey、protectContentKey 是需要透传到服务端的参数

 publicKey: params.publicKey,

 protectContentKey: params.protectContentKey,

 };

 const playUrl = await getPlayUrl(opt);

 const { player } = CosHlsSdk.play({

 container: '#container',

 playerType: 'hls.js',

 playUrl: playUrl,

 playerOptions: {}, // 对应的播放器初始化参数

 });

 console.log(player);

};

playVideo();

</script>

如以上示例，hls/token 接口的参数 src 、publicKey、ProtectContentKey 不需要用户填写，SDK 会自动生成，只需要传递给 token 接口。

4. **完整的代码示例**：请参见 [完整源码](https://github.com/tencentyun/cos-demo/tree/main/hls-encrypt/web-private-encrypt)。

**注意：**

兼容性说明：当前示例在大部分浏览器场景下**默认是私有加密**，当检测到部分环境（iOS Safari 或 WebView）不兼容 Media Source Extensions 对象时，会自动降级为**标准加密**。

## Demo 体验

您可在线体验 HLS 私有加密播放功能，单击前往 [HLS 加密视频播放体验地址](https://cos.cloud.tencent.com/samples/hls/private-encrypt/)。
