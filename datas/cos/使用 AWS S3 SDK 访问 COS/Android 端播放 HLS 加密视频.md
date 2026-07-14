<!-- source: https://cloud.tencent.com/document/product/436/106773 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:18:07+08:00 -->

# Android 端播放 HLS 加密视频

最近更新时间：2025-08-29 15:03:52


## 前提条件

创建加密视频，搭建 token 服务，详情请参见 [HLS 视频加密播放实践](https://cloud.tencent.com/document/product/460/59291)。

## Android 端播放指引

Android 端使用 ci-assistor.aar 中封装好的 CIPlayerAssistor 和 CIMediaInfo 对象来播放 m3u8 文件，用户按照如下规则传入参数，即可实现播放功能。

1. 集成 CIPlayerAssistor SDK。

集成 SDK：将 [ci-assistor.aar](https://github.com/tencentyun/CIPlayerAssistor_Android/blob/main/app/libs/ci-assistor.aar) 复制到 `app/libs` 目录。

在 `app/build.gradle` 中添加依赖：

dependencies{

 implementation 'org.nanohttpd:nanohttpd:2.3.1'}

2. 构造 CIMediaInfo 对象，参数说明如下。

参数名 说明 是否必填 类型 默认值
mediaObjectKey 视频资源唯一标识，例如hls/encrypt/test.m3u8 是 string 无
setPlayUrl 设置最终的播放 url 是 function 无

3. 使用 CIPlayerAssistor 获取最终的播放 url。

// 1. 初始化万象播放协助器，例如可以在 APP 启动时

CIPlayerAssistor.getInstance().init(context);

// 2. 获取最终的播放 url

String playerUrl = CIPlayerAssistor.getInstance().buildPlayerUrl(ciMediaInfo);

// 3. 注意：不再使用播放器助手后，请释放 CIPlayerAssistor 资源，例如 APP 退出时

CIPlayerAssistor.getInstance().destroy();

完整的 Android 端示例请参考如下代码。

// 初始化万象播放协助器，例如可以在 APP 启动时

CIPlayerAssistor.getInstance().init(context);

// 媒体资源标识，请替换成您业务的媒体资源标识，此处媒体资源标识仅为示例

String mediaObjectKey = "hls/encrypt/test.m3u8";

// CIMediaInfo 实例，可用于请求 PlayUrl

CIMediaInfo ciMediaInfo = new CIMediaInfo(mediaObjectKey);

// 从业务服务器获取 PlayUrl: 自行实现 getPlayUrl 方法(可参考下一块代码示例)

String playUrl = getPlayUrl(ciMediaInfo.getMedia(), ciMediaInfo.getPublicKey());

// 给 ciMediaInfo 设置获取到的 PlayUrl

ciMediaInfo.setPlayUrl(playUrl);

// 获取最终的播放 url（此链接只能播放一次，请不要重复使用，buildPlayerUrl 非耗时方法，可以多次调用）

String playerUrl = CIPlayerAssistor.getInstance().buildPlayerUrl(ciMediaInfo);

// 将 playerUrl 设置给播放器即可，demo 中演示了 exoplayer 和腾讯云播放器

// 以下以 exoplayer 作为代码示例

PlayerView playerView = view.findViewById(R.id.video_view);

ExoPlayer player = new ExoPlayer.Builder(getActivity()).build();

playerView.setPlayer(player);

MediaItem mediaItem = MediaItem.fromUri(playerUrl);

HlsMediaSource mediaSource = new HlsMediaSource.Factory(dataType ->

 new DefaultHttpDataSource.Factory().createDataSource()createMediaSource(mediaItem);

player.prepare(mediaSource);

player.play();

// 注意：不再使用播放器助手后，请释放 CIPlayerAssistor 资源，例如 APP 退出时

CIPlayerAssistor.getInstance().destroy();

从业务服务器获取 token 和签名的示例代码如下。

/**

 * 从业务服务器获取 PlayUrl

 */

private String getPlayUrl(String mediaObjectKey, String publicKey) {

 HttpURLConnection urlConnection = null;

 try {

 // 该 url 仅为示例，请替换成您业务的 url，具体实现请参考 “业务后端示例代码”

 URL url = new URL("https://cos.cloud.tencent.com/samples/hls/getPlayUrl");

 urlConnection = (HttpURLConnection) url.openConnection();

 urlConnection.setRequestMethod("POST");

 urlConnection.setDoOutput(true);

 urlConnection.setRequestProperty("Content-Type", "application/json");

 JSONObject jsonObject = new JSONObject();

 // 添加键值对到 JSONObject

 jsonObject.put("objectKey", mediaObjectKey);

 jsonObject.put("protectContentKey", 1);

 jsonObject.put("publicKey", publicKey);

 // 将 JSONObject 转换为字符串

 String jsonInputString = jsonObject.toString();

 byte[] input = jsonInputString.getBytes("utf-8");

 urlConnection.getOutputStream().write(input, 0, input.length);

 int status = urlConnection.getResponseCode();

 if (status != 200) {

 throw new RuntimeException("HttpResponseCode: " + status);

 } else {

 BufferedReader br = new BufferedReader(new InputStreamReader(urlConnection.getInputStream(), "utf-8"));

 StringBuilder response = new StringBuilder();

 String responseLine;

 while ((responseLine = br.readLine()) != null) {

 response.append(responseLine.trim());

 }

 String responseString = response.toString();

 Log.d("getPlayUrl：", responseString);

 JSONObject json = new JSONObject(responseString);

 String playUrl = json.getString("playUrl");

 // 在这里你可以使用 playUrl

 return playUrl;

 }

 } catch (Exception e) {

 e.printStackTrace();

 throw new RuntimeException(e);

 } finally {

 if (urlConnection != null) {

 urlConnection.disconnect();

 }

 }

}

## Demo 体验

我们提供了终端播放 HLS 私有加密视频的示例，请参见 [CIPlayerAssistor Demo](https://github.com/tencentyun/CIPlayerAssistor_Android)。
