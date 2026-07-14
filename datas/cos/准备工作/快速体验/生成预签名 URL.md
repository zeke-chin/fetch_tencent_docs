<!-- source: https://cloud.tencent.com/document/product/436/112228 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T22:15:25+08:00 -->

# 生成预签名 URL

最近更新时间：2024-11-06 09:45:32


## 简介

本文档提供关于生成对象预签名链接的示例代码。

关于使用预签名 URL 上传的说明请参见 [预签名授权上传](https://cloud.tencent.com/document/product/436/14114)， 使用预签名 URL 下载的说明请参见 [预签名授权下载](https://cloud.tencent.com/document/product/436/14116)。

**说明**

建议用户使用临时密钥生成预签名，通过临时授权的方式进一步提高预签名上传、下载等请求的安全性。申请临时密钥时，请遵循 [最小权限指引原则](https://cloud.tencent.com/document/product/436/38618)，防止泄露目标存储桶或对象之外的资源。

如果您一定要使用永久密钥来生成预签名，建议永久密钥的权限范围仅限于上传或下载操作，以规避风险。

## 生成对象预签名链接

#### 示例代码一：生成预签名上传链接

// 存储桶名称，由 bucketname-appid 组成，appid 必须填入，可以在 COS 控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket

let bucket = "examplebucket-1250000000";

//对象在存储桶中的位置标识符，即称对象键

let cosPath = "exampleobject.txt";

let request = new PresignedUrlRequest(bucket, cosPath, http.RequestMethod.PUT);try { let result = await CosXmlBaseService.default().buildPresignedUrl(request) // result为签名的上传链接

 if(result){

 // 进行数据上传 let httpRequest = http.createHttp(); try { let data = await httpRequest.request(result, { method: http.RequestMethod.PUT, extraData: 'data to put' }); httpRequest.destroy(); } catch (err) {

 httpRequest.destroy(); // 上传异常处理 }}} catch (e) { // 异常处理}

#### 示例代码二：生成预签名下载链接

// 存储桶名称，由 bucketname-appid 组成，appid 必须填入，可以在 COS 控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket

let bucket = "examplebucket-1250000000";

//对象在存储桶中的位置标识符，即称对象键

let cosPath = "exampleobject.txt";

let request = new PresignedUrlRequest(bucket, cosPath, http.RequestMethod.GET);try { let result = await CosXmlBaseService.default().buildPresignedUrl(request) // result为签名的下载链接

 if(result){

 // 进行数据下载 let httpRequest = http.createHttp(); try { let data = await httpRequest.request(result, { method: http.RequestMethod.GET }); httpRequest.destroy(); } catch (err) {

 httpRequest.destroy(); // 下载异常处理 }}} catch (e) { // 异常处理}
