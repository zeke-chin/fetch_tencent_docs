<!-- source: https://cloud.tencent.com/document/product/436/56215 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:37:47+08:00 -->

# POST Object 常见异常

最近更新时间：2022-06-09 14:42:36


## 故障现象

使用 COS API 进行 POST 请求时，返回如下异常错误码：

[Condition key q-ak doesn&apos;t match the value XXXXXX](https://cloud.tencent.com/document/product/436/56215#AccessDenied_q-ak)

[You post object request has been expired, expiration time: 1621188104 but the time now : 1621245817](https://cloud.tencent.com/document/product/436/56215#AccessDenied_Expiration)

[The Signature you specified is invalid.](https://cloud.tencent.com/document/product/436/56215#SignatureDoesNotMatch_POSTSignature)

[You must provide condition if you specify a policy in post object request.](https://cloud.tencent.com/document/product/436/56215#InvalidPolicyDocument_JSONFormat)

[Condition key bucket doesn&apos;t match the value [bucket-appid]](https://cloud.tencent.com/document/product/436/56215#AccessDenied_BucketNotConsistent)

[Condition key key doesn&apos;t match the value XXXXX](https://cloud.tencent.com/document/product/436/56215#AccessDenied_Condition)

[The body of your POST request is not well-formed multipart/form-data.](https://cloud.tencent.com/document/product/436/56215#MalformedPOSTRequest_POSTBody)

## 故障定位及处理

### Message 为 “Condition key q-ak doesn&apos;t match the value XXXXXX”

当您使用 COS API 进行 POST 请求出现如下信息时：

<Code>AccessDenied</Code>

<Message>Condition key q-ak doesn&apos;t match the value XXXXXX</Message>

#### 可能原因

q-ak 参数输入错误。

#### 解决方法

1. 登录访问管理控制台，进入 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面，查看密钥信息。

2. 根据查看的密钥信息，确认 q-ak 参数是否输入错误。

是，请将 q-ak 参数修改为正确的 SecretId。

否，请 [联系我们](https://cloud.tencent.com/document/product/436/37708)。

### Message 为 “You post object request has been expired, expiration time: 1621188104 but the time now : 1621245817”

当您使用 COS API 进行 POST 请求出现如下信息时：

<Code>AccessDenied</Code>

<Message>You post object request has been expired, expiration time: 1621188104 but the time now : 162124581 7</Message>

#### 可能原因

Policy 中的 expiration 值已过期。

#### 解决方法

请修改 Policy 中的 expiration 值。

**注意**

 expiration 值需要晚于当前时间，建议设置为当前时间+30分钟（UTC 时间）。

### Message 为 “The Signature you specified is invalid.”

当您使用 COS API 进行 POST 请求出现如下信息时：

<Code>SignatureDoesNotMatch</Code>

<Message>The Signature you specified is invalid.</Message>

#### 可能原因

签名计算错误。

#### 解决方法

请参考 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档，检查 POST 签名串生成规则是否正确。

是，请 [联系我们](https://cloud.tencent.com/document/product/436/37708)。

否，请使用 [在线辅助工具：COS 签名工具](https://cloud.tencent.com/document/product/436/30442) 重新计算 POST 请求签名。

### Message 为 “You must provide condition if you specify a policy in post object request.”

当您使用 COS API 进行 POST 请求出现如下信息时：

<Code>InvalidPolicyDocument</Code>

<Message>You must provide condition if you specify a policy in post object request.</Message>

#### 可能原因

Policy 格式错误。

#### 解决方法

请参考 [POST Object](https://cloud.tencent.com/document/product/436/14690) 文档，将 Policy 格式修改为标准 JSON 格式。

### Message 为 “Condition key bucket doesn&apos;t match the value [bucket-appid]”

当您使用 COS API 进行 POST 请求出现如下信息时：

<Code>AccessDenied</Code>

<Message>Condition key bucket doesn&apos;t match the value [bucket-appid]</Message>

#### 可能原因

Policy 中的 bucket 与请求 bucket 不一致。

#### 解决方法

请使用 Policy 中的 bucket 进行请求。

### Message 为 “Condition key key doesn&apos;t match the value XXXXX”

当您使用 COS API 进行 POST 请求出现如下信息时：

<Code>AccessDenied</Code>

<Message>Condition key key doesn&apos;t match the value XXXXX</Message>

#### 可能原因

上传的内容不符合 policy 规则。

#### 解决方法

根据 Policy 的 Condition，上传符合该条件的内容。

### Message 为 “The body of your POST request is not well-formed multipart/form-data.”

当您使用 COS API 进行 POST 请求出现如下信息时：

<Code>MalformedPOSTRequest</Code>

<Message>The body of your POST request is not well-formed multipart/form-data.</Message>

#### 可能原因

POST body 格式不符合规范。

#### 解决方法

参考 [POST Object](https://cloud.tencent.com/document/product/436/14690) 文档，优化 body 格式。
