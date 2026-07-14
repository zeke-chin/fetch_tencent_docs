<!-- source: https://cloud.tencent.com/document/product/436/65760 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:19:33+08:00 -->

# 对象访问 URL

最近更新时间：2024-08-13 17:46:41


## 简介

本文档提供关于生成对象访问 URL 的示例代码。

## 注意事项

2024年1月1日后创建的桶 [不支持使用默认域名在浏览器预览文件](https://cloud.tencent.com/document/product/436/96243)，建议您配置自定义域名，详情请参见 [存储桶切换自定义域名](https://cloud.tencent.com/document/product/436/102509)。

本文档中生成的访问对象 URL 方法，仅适用于通过默认域名访问公有读对象。

当对象为私有读对象时，请参见 [生成预签名 URL](https://cloud.tencent.com/document/product/436/47238) 文档生成。

## 相关示例

功能名称 描述 示例代码
对象访问 URL 实现生成对象访问 URL 的功能[GitHub完整示例](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/QCloudCSharpSDK/COSXMLDemo/Object/GetObjectUrl.cs)

## 前期准备：初始化 COS 服务实例

public class DownloadObject{ private CosXml cosXml; //将服务用户设置成数据成员 // 初始化COS服务实例 private void InitCosXml() { string region = Environment.GetEnvironmentVariable("COS_REGION"); CosXmlConfig config = new CosXmlConfig.Builder() .SetRegion(region) // 设置默认的地域, COS 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224 .Build(); string secretId = Environment.GetEnvironmentVariable("SECRET_ID"); // 云 API 密钥 SecretId, 获取 API 密钥请参照 https://console.cloud.tencent.com/cam/capi string secretKey = Environment.GetEnvironmentVariable("SECRET_KEY"); // 云 API 密钥 SecretKey, 获取 API 密钥请参照 https://console.cloud.tencent.com/cam/capi long durationSecond = 600; //每次请求签名有效时长，单位为秒 QCloudCredentialProvider qCloudCredentialProvider = new DefaultQCloudCredentialProvider(secretId, secretKey, durationSecond); this.cosXml = new CosXmlServer(config, qCloudCredentialProvider); }}

## 使用案例

### 获取对象访问 URL

//当对象 ACL 属性设置为“公有读”时，可以通过以下 SDK 接口生成的 URL 直接访问对象（仅支持生成 COS 默认源站域名的 URL）。

public void GetObjectUrl(){ try { // 存储桶名称，此处填入格式必须为 bucketname-APPID, 其中 APPID 获取参考 https://console.cloud.tencent.com/developer string bucket = "examplebucket-1250000000"; string key = "exampleobject"; //对象键 // 生成链接（默认域名访问） String url = cosXml.GetObjectUrl(bucket, key); Console.WriteLine("Object Url is: " + url); } catch (COSXML.CosException.CosClientException clientEx) { Console.WriteLine("CosClientException: " + clientEx); } catch (COSXML.CosException.CosServerException serverEx) { Console.WriteLine("CosServerException: " + serverEx.GetInfo()); }}
