<!-- source: https://cloud.tencent.com/document/product/436/57435 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:23:37+08:00 -->

# 对象访问 URL

最近更新时间：2024-08-13 11:18:21


## 简介

本文介绍对象存储 COS 通过 Go SDK 实现生成对象访问 URL 的示例代码和描述。

## 注意事项

2024年1月1日后创建的桶 [不支持使用默认域名在浏览器预览文件](https://cloud.tencent.com/document/product/436/96243)，建议您配置自定义域名，详情请参见 [存储桶切换自定义域名](https://cloud.tencent.com/document/product/436/102509)。

如果您的文件是**私有读**权限，那么本接口生成的 URL 不能直接用于访问资源。

此接口是单纯的客户端逻辑，因此不需要特殊授权。

COS Go SDK 版本需要大于等于 v0.7.26。

## 相关示例

功能名称 描述 示例代码
对象访问 URL 实现生成对象访问 URL 的功能[GitHub完整示例](https://github.com/tencentyun/cos-go-sdk-v5/blob/master/example/object/get_object_url.go)

## 使用案例

### 获取对象访问 URL

#### 方法原型

func (s *ObjectService) GetObjectURL(key string) *url.URL

#### 请求示例

package main

import (

 "fmt"

 "github.com/tencentyun/cos-go-sdk-v5"

 "net/http"

 "net/url"

 "os"

)

func main() {

 // 存储桶名称，由 bucketname-appid 组成，appid 必须填入，可以在 COS 控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket

 // 替换为用户的 region，存储桶 region 可以在 COS 控制台“存储桶概览”查看 https://console.cloud.tencent.com/ ，关于地域的详情见 https://cloud.tencent.com/document/product/436/6224 。

 u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")

 b := &cos.BaseURL{BucketURL: u}

 client := cos.NewClient(b, &http.Client{

 Transport: &cos.AuthorizationTransport{

 // 通过环境变量获取密钥

 // 环境变量 SECRETID 表示用户的 SecretId，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi

 SecretID: os.Getenv("SECRETID"), // 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140

 // 环境变量 SECRETKEY 表示用户的 SecretKey，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi

 SecretKey: os.Getenv("SECRETKEY"), // 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140

 },

 })

 key := "exampleobject"

 ourl := client.Object.GetObjectURL(key)

 fmt.Println(ourl)

}

#### 参数说明

参数名称 参数描述 类型 是否必填
Key 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg` 中，对象键为 doc/pic.jpg String 是

#### 返回结果说明

该方法返回值为对象访问的 URL。
