<!-- source: https://cloud.tencent.com/document/product/436/111672 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:32:18+08:00 -->

# AI 通用接口示例

最近更新时间：2026-06-11 15:48:12


## 简介

本文档提供关于 AI 相关通用接口 API 概览以及 SDK 示例代码。

**注意：**

此 demo 适用接口为：图片上色、图像超分、商品抠图、图像增强、图像智能裁剪、图像修复、人脸智能美颜、人脸特效。

该功能需要 COS Java SDK v5.6.193及以上版本。旧版本 SDK 该接口可能未覆盖或缺少更新参数，使用时建议升级到 [最新版本](https://cloud.tencent.com/document/product/460/49286)。

## 请求示例

### 下载时处理

public static void getGoodsMatting(COSClient client) {

 //图片所在 bucket 名称

 String bucketName = "demo-1234567890";

 //图片在 bucket 中的相对位置，比如根目录下 file 文件夹中的 demo.png 路径为 file/demo.png

 String key = "car.jpg";

 GetObjectRequest getObj = new GetObjectRequest(bucketName, key);

 //具体参数请参考 API 接口不同，对应的 ci-process 内容和使用的参数有区别

 getObj.putCustomQueryParameter("ci-process", "GoodsMatting");

 getObj.putCustomQueryParameter("center-layout", "1");

 ObjectMetadata object = client.getObject(getObj, new File("demo.jpg"));

}

### 云上数据处理

public static void postGoodsMatting(COSClient client) { String bucketName = "demo-1234567890"; String key = "car.jpg"; ImageProcessRequest imageReq = new ImageProcessRequest(bucketName, key); ​ PicOperations picOperations = new PicOperations(); picOperations.setIsPicInfo(1); List<PicOperations.Rule> ruleList = new LinkedList<>(); PicOperations.Rule rule1 = new PicOperations.Rule(); rule1.setBucket(bucketName); rule1.setFileId("cat2.jpg"); rule1.setRule("ci-process=GoodsMatting&center-layout=1&padding-layout=20x10"); ruleList.add(rule1); picOperations.setRules(ruleList); imageReq.setPicOperations(picOperations); CIUploadResult ciUploadResult = client.processImage(imageReq); System.out.println(Jackson.toJsonString(ciUploadResult));}

### 上传时处理

**注意：**

此处上传时处理为简单上传，不支持分片上传，大文件建议使用分片上传后调用云上处理接口。

public static void putGoodsMatting(COSClient cosClient) { String bucketName = "demo-1234567890"; String key = "car3.jpg"; File localFile = new File("car.jpg"); PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile); PicOperations picOperations = new PicOperations(); picOperations.setIsPicInfo(1); List<PicOperations.Rule> ruleList = new LinkedList<>(); PicOperations.Rule rule1 = new PicOperations.Rule(); rule1.setBucket(bucketName); rule1.setFileId(key); rule1.setRule("ci-process=GoodsMatting&center-layout=1&padding-layout=20x10"); ruleList.add(rule1); picOperations.setRules(ruleList); putObjectRequest.setPicOperations(picOperations); PutObjectResult putObjectResult = cosClient.putObject(putObjectRequest); CIUploadResult ciUploadResult = putObjectResult.getCiUploadResult(); System.out.println(Jackson.toJsonString(putObjectResult));}

#### 返回结果说明

成功： 返回任务详情响应包装类，下载时处理为 ObjectMetadata 对象,云上数据处理和上传时处理为 CIUploadResult 对象。

失败： 发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。详情请参见 [异常处理](https://cloud.tencent.com/document/product/436/35218)。

### 第三方资源

部分接口支持参数 detect-url，以图像超分接口为例。**在创建 CosClient 时，需要关闭 RequestPath 校验**。

public class AISuperResolutionDemo {

 public static void main(String[] args) {

 // 1 初始化用户身份信息（secretId, secretKey）。

 COSClient cosClient = getCosClient("sid", "skey", "region");

 // 2 调用要使用的方法。

 getAISuperResolution(cosClient);

 cosClient.shutdown();

 }

 public static COSClient getCosClient(String secretId, String secretKey, String _region) {

 // 1 初始化用户身份信息（secretId, secretKey）。

 COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);

 // 2 设置 bucket 的区域, CI 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224

 // clientConfig 中包含了设置 region, https(默认 https), 超时, 代理等 set 方法, 使用可参见源码或者常见问题 Java SDK 部分。

 Region region = new Region(_region);

 ClientConfig clientConfig = new ClientConfig(region);

 clientConfig.setCheckRequestPath(false);

 // 3 生成 cos 客户端。

 return new COSClient(cred, clientConfig);

 }

 public static void getAISuperResolution(COSClient client) {

 //图片所在 bucket 名称

 String bucketName = "demo-1234567890";

 //图片在 bucket 中的相对位置，比如根目录下 file 文件夹中的 demo.png 路径为 file/demo.png

 //使用 detect-url 参数时 这里设置为空字符串 部分接口有限制 key 和 detect-url 不可同时存在

 String key = "";

 GetObjectRequest getObj = new GetObjectRequest(bucketName, key);

 //具体参数请参考 API

 getObj.putCustomQueryParameter("ci-process", "AISuperResolution");

 getObj.putCustomQueryParameter("detect-url", "https://demo-1234567890.cos.ap-chongqing.myqcloud.com/1.jpg");

 ObjectMetadata object = client.getObject(getObj, new File("demo.png"));

 }

}
