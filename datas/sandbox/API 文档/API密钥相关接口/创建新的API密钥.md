<!-- source: https://cloud.tencent.com/document/product/1814/124822 -->
<!-- fetcher: jina -->

# 创建新的API密钥

最近更新时间：2025-11-07 10:12:52


## 1. 接口描述

接口请求域名： ags.tencentcloudapi.com 。

创建新的API密钥，用于调用Agent Sandbox接口。相较于腾讯云Secret ID Secret Key支持调用所有接口使用，仅有部分接口支持使用API密钥调用。

默认接口请求频率限制：20次/秒。

 推荐使用 API Explorer

[点击调试](https://console.cloud.tencent.com/api/explorer?Product=ags&Version=2025-09-20&Action=CreateAPIKey)

 API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数和部分公共参数，完整公共参数列表见 [公共请求参数](https://cloud.tencent.com/document/api/1814/124827)。

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| Action | 是 | String | [公共参数](https://cloud.tencent.com/document/api/1814/124827)，本接口取值：CreateAPIKey。 |
| Version | 是 | String | [公共参数](https://cloud.tencent.com/document/api/1814/124827)，本接口取值：2025-09-20。 |
| Region | 否 | String | [公共参数](https://cloud.tencent.com/document/api/1814/124827)，此参数为可选参数。 |
| Name | 否 | String | API密钥名称，方便用户记忆 示例值：LocalDev |

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| Name | String | 用户传入的API密钥名称，方便用户记忆 示例值：LocalDev |
| APIKey | String | 生成的API密钥，仅返回此一次，后续无法获取 示例值：ark_abce1958asjwi |
| KeyId | String | API密钥ID 示例值：ark-9ijnhy66 |
| RequestId | String | 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。 |

## 4. 示例

### 示例1 创建API密钥

#### 输入示例


```
POST / HTTP/1.1
Host: ags.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateAPIKey
<公共请求参数>

{
    "Name": "LocalDev"
}
```

#### 输出示例


```json
{
    "Response": {
        "APIKey": "ark_nXe8gccx2MGJ0oZ3bCf3Rq1I6bMtLEbJKB5k1NPK_rg",
        "KeyId": "ark-3edcft6y",
        "Name": "str",
        "RequestId": "fb33859c-a89b-4626-bee1-bab5e53803b3"
    }
}
```

## 5. 开发者资源

### 腾讯云 API 平台

[腾讯云 API 平台](https://cloud.tencent.com/api) 是综合 API 文档、错误码、API Explorer 及 SDK 等资源的统一查询平台，方便您从同一入口查询及使用腾讯云提供的所有 API 服务。

### API Inspector

用户可通过 [API Inspector](https://cloud.tencent.com/document/product/1278/49361) 查看控制台每一步操作关联的 API 调用情况，并自动生成各语言版本的 API 代码，也可前往 [API Explorer](https://cloud.tencent.com/document/product/1278/46697) 进行在线调试。

### SDK

云 API 3.0 提供了配套的开发工具集（SDK），支持多种编程语言，能更方便的调用 API。

*   Tencent Cloud SDK 3.0 for Python: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-python/-/blob/master/tencentcloud/ags/v20250920/ags_client.py), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-python/blob/master/tencentcloud/ags/v20250920/ags_client.py), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-python/blob/master/tencentcloud/ags/v20250920/ags_client.py)
*   Tencent Cloud SDK 3.0 for Java: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-java/-/blob/master/src/main/java/com/tencentcloudapi/ags/v20250920/AgsClient.java), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-java/blob/master/src/main/java/com/tencentcloudapi/ags/v20250920/AgsClient.java), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-java/blob/master/src/main/java/com/tencentcloudapi/ags/v20250920/AgsClient.java)
*   Tencent Cloud SDK 3.0 for PHP: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-php/-/blob/master/src/TencentCloud/Ags/V20250920/AgsClient.php), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-php/blob/master/src/TencentCloud/Ags/V20250920/AgsClient.php), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-php/blob/master/src/TencentCloud/Ags/V20250920/AgsClient.php)
*   Tencent Cloud SDK 3.0 for Go: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-go/-/blob/master/tencentcloud/ags/v20250920/client.go), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-go/blob/master/tencentcloud/ags/v20250920/client.go), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-go/blob/master/tencentcloud/ags/v20250920/client.go)
*   Tencent Cloud SDK 3.0 for Node.js: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-nodejs/-/blob/master/src/services/ags/v20250920/ags_client.ts), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-nodejs/blob/master/src/services/ags/v20250920/ags_client.ts), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-nodejs/blob/master/src/services/ags/v20250920/ags_client.ts)
*   Tencent Cloud SDK 3.0 for .NET: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-dotnet/-/blob/master/TencentCloud/Ags/V20250920/AgsClient.cs), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-dotnet/blob/master/TencentCloud/Ags/V20250920/AgsClient.cs), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-dotnet/blob/master/TencentCloud/Ags/V20250920/AgsClient.cs)
*   Tencent Cloud SDK 3.0 for C++: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-cpp/-/blob/master/ags/src/v20250920/AgsClient.cpp), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-cpp/blob/master/ags/src/v20250920/AgsClient.cpp), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-cpp/blob/master/ags/src/v20250920/AgsClient.cpp)
*   Tencent Cloud SDK 3.0 for Ruby: [CNB](https://cnb.cool/tencent/cloud/api/sdk/tencentcloud-sdk-ruby/-/blob/master/tencentcloud-sdk-ags/lib/v20250920/client.rb), [GitHub](https://github.com/TencentCloud/tencentcloud-sdk-ruby/blob/master/tencentcloud-sdk-ags/lib/v20250920/client.rb), [Gitee](https://gitee.com/TencentCloud/tencentcloud-sdk-ruby/blob/master/tencentcloud-sdk-ags/lib/v20250920/client.rb)

### 命令行工具

*   [Tencent Cloud CLI 3.0](https://cloud.tencent.com/document/product/440/6176)

## 6. 错误码

以下仅列出了接口业务逻辑相关的错误码，其他错误码详见 [公共错误码](https://cloud.tencent.com/document/api/1814/124832#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。

| 错误码 | 描述 |
| --- | --- |
| FailedOperation | 操作失败。 |
| InternalError | 内部错误。 |
| InvalidParameter | 参数错误。 |
| InvalidParameterValue | 参数取值错误。 |
| LimitExceeded.APIKeyQuota | 账号下 API 密钥数量达到上限 |
| UnsupportedOperation | 操作不支持。 |
