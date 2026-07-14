<!-- source: https://cloud.tencent.com/document/product/436/106771 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:17:51+08:00 -->

# HLS 视频加密播放实践

最近更新时间：2024-09-09 10:45:42


## 视频加密能力简介

视频加密是指对视频中的内容进行加密处理，加密后的视频无法分发给无访问权限的用户观看，即使视频被下载到本地，视频本身也是被加密的，无法正常播放和二次分发，从而保障您的视频版权不受到非法侵犯，有效防止视频泄露和盗链问题。视频加密可广泛用于在线教育及财经等领域。

## **方案架构**

整体方案架构包含视频加密与播放加密后的视频两大部分流程说明。

### **视频加密流程**

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/fccdbbaa4274efe73939224793f2888b.png)

****

**视频加密**

1.上传视频：业务APP通过控制台、服务端 API 等方式，将视频上传到COS。

2.触发视频处理：上传视频后，触发视频处理。触发后，视频在转码的过程中进行加密。

3.获取加密密钥：视频转码并加密，从数据万象密钥管理模块获取加密密钥。

4.加密后的视频写入存储：视频转码并加密后，输出的视频内容被写入到COS存储中。

### 播放加密后的视频

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/982341bef08d4cdf2f9a78913594ffff.png)

**解密视频并播放**

1.将加密视频URL添加上签名token：向业务侧APP服务发起请求，在播放地址后拼接签名token。

2.下载加密后的视频内容：接收业务侧播放器请求，如有CDN存在，CDN回源COS，下载加密后的视频内容。

3.获取解密密钥：业务侧播放器携带含签名token的url从数据万象密钥管理模块请求解密密钥。

4.解密并播放：播放器获取密钥后，解密视频并播放。

**说明：**

业务方需开通腾讯云数据万象服务（CI）、存储服务（COS）。

## 接入指引

基于上述原理架构，进行如下操作步骤，便可以实现对视频的加密与解密播放。

### 步骤一：上传视频，转码为 HLS 加密视频

1.**上传视频**：在对象存储控制台 [存储桶列表](https://console.cloud.tencent.com/cos/bucket)，进入要存储视频的存储桶，上传要转码的视频到存储桶。

2.**创建自定义模板**：左侧菜单找到**任务和工作流>模板配置**，选择音视频转码，单击创建转码模板，在弹窗里**封装格式**选择 **HLS**，并配置其他转码选项（可保留默认配置），该模板可用于后续创建任务和创建工作流。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/c64f39f90ccc2766839df01e3413c15f.png)

在最后一步的高级设置里**开启视频加密**，点击**完成**。

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/ff0155c7c5431d141ac1388cd6831bd2.png)

3.**创建转码任务**：到**任务和工作流>任务管理**点击**创建任务**，**任务类型**选择**音视频转码，**选择刚创建的**HLS加密模板**，选择**目标存储桶和文件名**后，点击**确定。**

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/29d824a0fe9f061e0fe0c7ee5ee1c7cb.png)

4.**找到转码后的视频文件**：等任务执行完成后，找到**创建任务**时填的目标路径，可看到生成后的.m3u8 和 .ts 后缀的**加密视频文件。**

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/2e44d515cfa45059eceaf3db810fee24.png)

5.复制播放密钥：到 [对象存储控制台](https://console.cloud.tencent.com/cos/bucket)，桶详情页面的**数据处理>媒体处理**，在上方选中**媒体处理**页签。编辑**开启媒体处理**，并生成和复制**播放密钥**。用于后续 token 服务搭建。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/e36fcd7494c3d3aa0a9a10c591d950d7.png)

### 步骤二：搭建用于获取 token 的服务

HLS 加密视频播放流程里，需要开发者自行搭建服务，用于获取 HLS 播放 token 和签名。

#### token 计算规则

HLS 播放 token 采用 JWT（JSON Web Token），一种由 Header、PayLoad 和 Signature 组合得到的数字令牌。

#### token **计算公式**

1.计算 Signature：Signature = HMACSHA256(base64UrlEncode(Header) + "." + base64UrlEncode(Payload), Key)

2.计算 Token： Token = base64UrlEncode(Header) + '.' + base64UrlEncode(Payload) + '.' + base64UrlEncode(Signature)

#### **Payload 的参数说明**

以上 Payload 的参数说明如下：

节点名称（关键字）父节点 描述 类型 是否必选
Type 无 token 类型，固定值为 CosCiToken String 是
AppId 无 用户的 appId String 是
BucketId 无 需要播放的文件所在的 BucketId String 是
Object 无 需要播放的文件名 String 是
Issuer 无 token 颁发者，固定为 client String 是
IssuedTimeStamp 无 token 颁发秒级时间戳 int 是
ExpireTimeStamp 无 token 过期秒级时间戳，默认1天过期 int 否
UsageLimit 无 token 使用次数限制，默认限制100次 int 是
ProtectContentKey 无 是否加密解密密钥（播放时解密ts视频流的密钥），1表示对解密密钥加密，0表示不对解密密钥加密。 默认为0 int 否
ProtectSchema 无 保护模式，仅支持 rsa1024 ，则表示使用 RSA 非对称加密的方式保护，公私钥对长度为1024bit String 否（当 ProtectContentKey=1 时必选）
PublicKey 无 公钥。1024 bit 的 RSA 公钥，需使用 Base64 进行编码 String 否（当 ProtectContentKey=1 时必选）

#### token **计算步骤**

按照以上计算规则，这里提供一个计算过程的例子，假设某用户 需要播放 test-125000000 桶下的 hls_test.m3u8 加密视频，示例如下：

#### **1. 计算 Header**

Header 是 JSON 格式，表示 JWT 使用的算法信息，固定使用如下内容：

{

 // 加密的算法，固定为 HS256

 "alg": "HS256",

 // 类型，固定为 JWT

 "typ": "JWT"

}

#### **2. 计算 Payload**

PayLoad 是 JSON 格式，是播放器签名参数的内容，格式例如：

{

 // 固定为 CosCiToken，必填参数

 Type: "CosCiToken",

 // app id，必填参数

 AppId: "",

 // 播放文件所在的BucketId，必填参数

 BucketId: "",

 // 需要播放的文件名

 Object: "",

 // 固定为client，必填参数

 Issuer: "client",

 // token颁发时间戳，必填参数

 IssuedTimeStamp: Number,

 // token过期时间戳，非必填参数，默认1天过期

 ExpireTimeStamp: Number,

 // token使用次数限制，非必填参数，默认限制100次

 UsageLimit: 100,

 // 保护模式，填写为 rsa1024 ，则表示使用 RSA 非对称加密的方式保护，公私钥对长度为 1024 bit

 ProtectSchema: "rsa1024",

 // 公钥。1024 bit 的 RSA 公钥，需使用 Base64 进行编码

 PublicKey: "",

 // 是否加密解密密钥（播放时解密ts视频流的密钥），1表示对解密密钥加密，0表示不对解密密钥加密。

 ProtectContentKey: 0

}

示例：

{

 Type: "CosCiToken",

 AppId: "125000000",

 BucketId: "test-125000000",

 Object: "hls_test.m3u8",

 Issuer: "client",

 IssuedTimeStamp: 1697094000,

 ExpireTimeStamp: 1697122800,

 UsageLimit: 3,

 ProtectSchema: "rsa1024",

 PublicKey: "NS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlHZk1BMEdDU3FHU0liM0RRRUJBUVVBQTRHTkFEQ0JpUUtCZ1FDa1M1TU1QS0k0eStudnU1V0E3amdGV0ZzYQoybXpqK0d1WWVjcVZreDJNaE1kbmZDcG0yL1JqNDdMbi9pYnFlSUJGNmxWZnZTbTdJTlBXNHNYWG9KMS9UK1lhClM0WHowTVBuSjZOemJHQTZSYm5FdTNlMkx4UnZXNTBPZXJaUnFwNlpOY21JR3prZHVjRXhhMDh4VmkzVHdGNGEKQjc4ZXFMdmlRSm5uTkFYWEl3SURBUUFCCi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQ==",

 ProtectContentKey: 1

}

经过 base64UrlEncode 后的结果是： eyJUeXBlIjoiQ29zQ2lUb2tlbiIsIkFwcElkIjoiMTI1MDAwMDAwIiwiQnVja2V0SWQiOiJ0ZXN0LTEyNTAwMDAwMCIsIk9iamVjdCI6Imhsc190ZXN0Lm0zdTgiLCJJc3N1ZXIiOiJjbGllbnQiLCJJc3N1ZWRUaW1lU3RhbXAiOjE2OTcwOTQwMDAsIk5vdEJlZm9yZVRpbWVTdGFtcCI6MCwiRXhwaXJlVGltZVN0YW1wIjoxNjk3MTIyODAwLCJSYW5kb20iOjAsIlVzYWdlTGltaXQiOjMsIlByb3RlY3RTY2hlbWEiOiJyc2ExMDI0IiwiUHVibGljS2V5IjoiTlMwdExTMUNSVWRKVGlCUVZVSk1TVU1nUzBWWkxTMHRMUzBLVFVsSFprMUJNRWREVTNGSFUwbGlNMFJSUlVKQlVWVkJRVFJIVGtGRVEwSnBVVXRDWjFGRGExTTFUVTFRUzBrMGVTdHVkblUxVjBFM2FtZEdWMFp6WVFveWJYcHFLMGQxV1dWamNWWnJlREpOYUUxa2JtWkRjRzB5TDFKcU5EZE1iaTlwWW5GbFNVSkdObXhXWm5aVGJUZEpUbEJYTkhOWVdHOUtNUzlVSzFsaENsTTBXSG93VFZCdVNqWk9lbUpIUVRaU1ltNUZkVE5sTWt4NFVuWlhOVEJQWlhKYVVuRndObHBPWTIxSlIzcHJaSFZqUlhoaE1EaDRWbWt6VkhkR05HRUtRamM0WlhGTWRtbFJTbTV1VGtGWVdFbDNTVVJCVVVGQ0NpMHRMUzB0UlU1RUlGQlZRa3hKUXlCTFJWa3RMUzB0TFE9PSIsIlByb3RlY3RDb250ZW50S2V5IjoxLCJSZXF1ZXN0QXBwSWQiOiIiLCJSZXF1ZXN0QnVja2V0IjoiIn0

#### **3. 计算 Signature**

签名 Signature 是对 Header、Payload 内容，用播放密钥 playKey 算一个哈希值签名放在 token 里，用于保证参数不被篡改。计算签名用的 playKey 是存储桶的播放密钥，需要到 COS 控制台存储桶详情里的数据处理->媒体处理，获取播放密钥。

签名计算规则是：Signature = HMACSHA256(base64UrlEncode(Header) + "." + base64UrlEncode(Payload), playKey)

示例：以播放密钥作为 playKey（即 92552049b9a64ad3b3e45af066f387cd33）进行 HMAC 计算，Signature 是： 4fRr2czM2vQx8lmhQ6zChN29oFmPrmu5X5ouIo01dkc。

#### **4. 合并得到 token**

用英文字符 . 合并3个字符串，得到 token。

示例：eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJUeXBlIjoiQ29zQ2lUb2tlbiIsIkFwcElkIjoiMTI1MDAwMDAwIiwiQnVja2V0SWQiOiJ0ZXN0LTEyNTAwMDAwMCIsIk9iamVjdCI6Imhsc190ZXN0Lm0zdTgiLCJJc3N1ZXIiOiJjbGllbnQiLCJJc3N1ZWRUaW1lU3RhbXAiOjE2OTcwOTQwMDAsIk5vdEJlZm9yZVRpbWVTdGFtcCI6MCwiRXhwaXJlVGltZVN0YW1wIjoxNjk3MTIyODAwLCJSYW5kb20iOjAsIlVzYWdlTGltaXQiOjMsIlByb3RlY3RTY2hlbWEiOiJyc2ExMDI0IiwiUHVibGljS2V5IjoiTlMwdExTMUNSVWRKVGlCUVZVSk1TVU1nUzBWWkxTMHRMUzBLVFVsSFprMUJNRWREVTNGSFUwbGlNMFJSUlVKQlVWVkJRVFJIVGtGRVEwSnBVVXRDWjFGRGExTTFUVTFRUzBrMGVTdHVkblUxVjBFM2FtZEdWMFp6WVFveWJYcHFLMGQxV1dWamNWWnJlREpOYUUxa2JtWkRjRzB5TDFKcU5EZE1iaTlwWW5GbFNVSkdObXhXWm5aVGJUZEpUbEJYTkhOWVdHOUtNUzlVSzFsaENsTTBXSG93VFZCdVNqWk9lbUpIUVRaU1ltNUZkVE5sTWt4NFVuWlhOVEJQWlhKYVVuRndObHBPWTIxSlIzcHJaSFZqUlhoaE1EaDRWbWt6VkhkR05HRUtRamM0WlhGTWRtbFJTbTV1VGtGWVdFbDNTVVJCVVVGQ0NpMHRMUzB0UlU1RUlGQlZRa3hKUXlCTFJWa3RMUzB0TFE9PSIsIlByb3RlY3RDb250ZW50S2V5IjoxLCJSZXF1ZXN0QXBwSWQiOiIiLCJSZXF1ZXN0QnVja2V0IjoiIn0.4fRr2czM2vQx8lmhQ6zChN29oFmPrmu5X5ouIo01dkc

#### token 服务代码实现

HLS 播放 token 是在 HLS 加密视频播放步骤里需要用于拼接播放链接的参数，采用 JWT（JSON Web Token）格式计算得出，是一种由 Header、PayLoad 和 Key 计算并组合得到的数字令牌。token 服务可以参考 [Nodejs 示例](https://github.com/tencentyun/cos-demo/tree/main/server/hls-decrypt-token/nodejs)、[Go 示例](https://github.com/tencentyun/cos-demo/tree/main/server/hls-decrypt-token/go)。

### 步骤三：播放 HLS 加密视频

获取播放器签名 token 后，您可以分别使用 [Web 端播放 HLS 加密视频](https://cloud.tencent.com/document/product/460/104024)、[Android 端播放 HLS 加密视频](https://cloud.tencent.com/document/product/460/104146)、[iOS 端播放 HLS 加密视频](https://cloud.tencent.com/document/product/460/104147) 和 [小程序端播放 HLS 加密视频](https://cloud.tencent.com/document/product/460/104568)的播放器 Demo 进行验证，具体内容请参考 Demo 的源码。

## 费用说明

视频 HLS 加密将收取 [转码费用](https://cloud.tencent.com/document/product/460/58120#9f3ec255-b086-48aa-b92d-ce5240a36fb5)

[对象存储相关费用](https://cloud.tencent.com/document/product/436/53482 "https://cloud.tencent.com/document/product/436/53482")
