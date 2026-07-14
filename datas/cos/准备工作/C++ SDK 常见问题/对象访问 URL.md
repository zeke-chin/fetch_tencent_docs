<!-- source: https://cloud.tencent.com/document/product/436/109477 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:15:49+08:00 -->

# 对象访问 URL

最近更新时间：2024-11-15 21:48:58


## 简介

本文介绍对象存储 COS 通过 C++ SDK 实现生成对象访问 URL 的示例代码和描述。

## 注意事项

2024年1月1日后创建的桶 [不支持使用默认域名在浏览器预览文件](https://cloud.tencent.com/document/product/436/96243)，建议您配置自定义域名，详情请参见 [存储桶切换自定义域名](https://cloud.tencent.com/document/product/436/102509)。

如果您的文件是**私有读**权限，那么本接口生成的 URL 不能直接用于访问资源。

此接口是单纯的客户端逻辑，因此不需要特殊授权。

## 相关示例

功能名称 描述 示例代码
对象访问 URL 实现生成对象访问 URL 的功能[GitHub完整示例](https://github.com/tencentyun/cos-cpp-sdk-v5/blob/master/demo/object_op_demo/get_object_url_demo.cpp)

## 前期准备

## 创建 CosAPI

调用 COS 的接口之前，必须先创建一个 CosAPI 的实例。这个实例用来后续调用请求。

qcloud_cos::CosAPI InitCosAPI() {

 uint64_t appid = 12500000000;

 std::string region = "ap-guangzhou";// bucket 的地域，请参见 https://cloud.tencent.com/document/product/436/62

 std::string secret_id = "************************************"; //用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140

 std::string secret_key = "************************************"; //用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140


 qcloud_cos::CosConfig config(appid, secret_id, secret_key, region);

 qcloud_cos::CosAPI cos_tmp(config);

 return cos_tmp;

}

### 使用临时密钥创建 CosAPI

如果要使用临时密钥请求 COS，则需要用临时密钥创建 CosAPI 实例。

qcloud_cos::CosAPI InitCosAPI() {

 // 需要已经获取到临时密钥的结果：tmp_secret_id、tmp_secret_key、

 // 临时密钥的生成参见 https://cloud.tencent.com/document/product/436/14048#cos-sts-sdk

 uint64_t appid = 12500000000;

 std::string region = "ap-guangzhou";

 std::string tmp_secret_id = "************************************";

 std::string tmp_secret_key = "************************************";

 std::string tmp_token = "token";


 qcloud_cos::CosConfig config(appid, tmp_secret_id, tmp_secret_key, region);

 config.SetTmpToken(tmp_token);

 qcloud_cos::CosAPI cos_tmp(config);

 return cos_tmp;

}

## **使用案例**

### 获取对象访问 URL

#### 方法原型

std::string CosAPI::GetObjectUrl(const std::string& bucket,

 const std::string& object, bool https,

 const std::string& region)

#### 请求示例

void GetObjectUrlDemo(qcloud_cos::CosAPI& cos) {

 std::string object_name = "test.txt";

 bool is_https = true; // 是否为 https

 std::string object_url = cos.GetObjectUrl(bucket_name, object_name, is_https);

 std::cout << "=======================GetObjectUrl=========================" << std::endl;

 std::cout << "object url=[" << object_url << "]" << std::endl;

 std::cout << "============================================================" << std::endl;

}

#### 参数说明

参数名称 描述 类型
bucket_name Bucket 的命名格式为 BucketName-APPID ，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83)string
object_name 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/picture.jpg` 中，对象键为 doc/picture.jpg，详情请参见 [对象键](https://cloud.tencent.com/document/product/436/13324)string
is_https 是否为 https，默认为false bool
region 存储桶地域，可以不传，默认为 CosAPI 实例中的 region string

#### 返回结果说明

返回对象访问 URL。
