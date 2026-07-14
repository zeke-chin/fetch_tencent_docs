<!-- source: https://cloud.tencent.com/document/product/436/68284 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:05:33+08:00 -->

# 使用预签名 URL 访问 COS

最近更新时间：2024-06-21 11:13:01


## 使用场景

使用预签名 URL 进行下载，获取临时 URL 用于临时分享文件、文件夹。或使用长期有效的预签名 URL 用于长期分享文件，详情请参见 [文件分享](https://cloud.tencent.com/document/product/436/68284#%E6%96%87%E4%BB%B6%E5%88%86%E4%BA%AB)。

使用预签名 URL 进行上传，详情请参见 [上传文件](https://cloud.tencent.com/document/product/436/68284#%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6)。

## 文件分享（下载文件）

COS 支持对象的分享，您可以使用预签名 URL 将文件、文件夹限时分享给其他用户。其原理是将签名嵌入拼接在对象 URL 之后，得到**预签名 URL，**有关签名生成算法请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778)。其中签名携带了身份信息，因此得到预签名 URL 的用户可以下载对象。

例如，对象 URL 为： `https://test-12345678.cos.ap-beijing.myqcloud.com/test.png`

拼接了签名值的对象 URL 预签名为：

`https://test-12345678.cos.ap-beijing.myqcloud.com/test.png?q-sign-algorithm=sha1&q-ak=xxxxx&q-sign-time=1638417770;1638421370&q-key-time=1638417770;1638421370&q-header-list=host&q-url-param-list=&q-signaturexxxxxfxxxxxx6&x-cos-security-token=xxxxxxxxxxxx`

### 注意事项

存储桶默认为私有读，直接通过对象 URL 下载会提示访问失败。

如果您一定要使用永久密钥来生成预签名，建议永久密钥的权限范围仅限于上传或下载操作，以规避风险。并且所生成的签名有效时长设置为完成本次上传或下载操作所需的最短期限，因为，当指定预签名 URL 的有效时间过期后，请求会中断。

申请新的签名后，需要重新执行失败请求，不支持断点续传。

以下提供的文件分享方法，本质上都是在自动生成签名，并拼接到对象 URL 后面，生成后为临时链接，可以直接用于下载或预览。

### 方式一：快速获取临时链接作为预签名 URL

您可以通过控制台或 COSBrowser 工具快速获取对象的临时链接。有效期为1 - 2小时。

#### 控制台（Web 页面）

1. 登录 [COS 控制台](https://console.cloud.tencent.com/cos5)，单击存储桶名称，进入“文件列表”，单击对象**详情**。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/f0a4459b6c633ff8aea444521f4dc591.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/f0a4459b6c633ff8aea444521f4dc591.png)

2. 进入对象详情页面，复制临时链接，有效期为1小时。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/b3d283d1c99fb7e149817b3fcf2cce61.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/b3d283d1c99fb7e149817b3fcf2cce61.png)

#### COSBrowser（桌面端）

参见 COSBrowser 桌面端使用说明中的 [生成文件链接](https://cloud.tencent.com/document/product/436/38103#url) 获取对象的临时链接。使用主账号密钥可获取最长2小时的临时链接，使用子账号密钥可获取最长1.5天的临时链接。

### 方式二：获取自定义时长的临时链接作为预签名 URL

您可以通过两种方式获取自定义时长的对象临时链接：使用签名工具、使用 SDK 批量获取预签名 URL。

#### 使用签名工具

**适合对编程不熟悉的用户，**操作步骤如下：

1. 获取文件链接。登录 [COS 控制台](https://console.cloud.tencent.com/cos5)，单击存储桶名称，进入“文件列表”，单击对象**详情**。进入对象详情页面，复制不带签名的“对象地址”。

2. 从 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。

3. 单击 [COS 签名工具](https://cos5.cloud.tencent.com/static/cos-sign/)，获取签名链接。有效时间支持天、小时、分钟、秒级别，默认选中小时。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/eee468660e47d28b978dea44bc7412b8.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/eee468660e47d28b978dea44bc7412b8.png)

4. 点击生成签名，在右侧的结果反馈中可获取带签名的临时文件链接。

#### 使用 SDK 批量获取预签名 URL

**适合批量获取临时链接、有编程基础的用户。**您可以使用临时密钥或永久密钥用于生成预签名 URL。两者的区别在于，临时密钥的最长时效不超过36小时，永久密钥不会过期，这间接影响了预签名 URL 的有效期。

若需要时间更长的临时链接，可以使用 SDK 通过控制签名时长实现生成预签名 URL。生成方法请参见 [预签名授权下载](https://cloud.tencent.com/document/product/436/14116)，可根据您熟悉的开发语言选择合适的实现方式。

**使用永久密钥生成预签名 URL（任意时长）**

永久密钥不会过期，预签名 URL 的有效期取决于您设置的签名有效期。您可以直接调用 SDK 的预签名 URL 方法。操作步骤如下：

1. 输入 secret_id、secret_key、region 等初始化 client。

2. 输入您的存储桶名称、对象名称、签名有效期，生成自定义时长的预签名 URL。详情请参见下列各语言 SDK 文档：

[Android SDK](https://cloud.tencent.com/document/product/436/46421)[C SDK](https://cloud.tencent.com/document/product/436/35560)[C++ SDK](https://cloud.tencent.com/document/product/436/35163)[.NET SDK](https://cloud.tencent.com/document/product/436/32873)
[Go SDK](https://cloud.tencent.com/document/product/436/35059)[iOS SDK](https://cloud.tencent.com/document/product/436/46388)[Java SDK](https://cloud.tencent.com/document/product/436/35217)[JavaScript SDK](https://cloud.tencent.com/document/product/436/35651)
[Node.js SDK](https://cloud.tencent.com/document/product/436/36121)[PHP SDK](https://cloud.tencent.com/document/product/436/34284)[Python SDK](https://cloud.tencent.com/document/product/436/35153)[小程序 SDK](https://cloud.tencent.com/document/product/436/36162)

**使用临时密钥生成预签名 URL（不超过36小时）**

在前端直传的场景中，经常需要使用到临时密钥。关于临时密钥的说明和生成指引您可以参考：

[使用临时密钥访问COS](https://cloud.tencent.com/document/product/436/68283)

[临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048)

[用于前端直传 COS 的临时密钥安全指引](https://cloud.tencent.com/document/product/436/40265)

临时密钥最长为36小时，预签名 URL 的有效期会取您设置的签名有效期和临时密钥有效期的最小值。假设您设置的签名有效期为 X，临时密钥的有效期为 Y，链接的实际生效时间为 T：

T=min(X,Y)；由于 X<=36，所以 T<=36。

使用临时密钥生成预签名 URL，需要两步：

1. [获取临时密钥](https://cloud.tencent.com/document/product/436/14048#.E8.8E.B7.E5.8F.96.E4.B8.B4.E6.97.B6.E5.AF.86.E9.92.A5)。

2. 获取临时密钥后，可以使用与永久密钥类似的函数生成预签名 URL。需要注意的是，使用临时密钥初始化 client，不仅需要输入 SecretId、SecretKey 还需要输入 token，并且携带参数`x-cos-security-token`。详情请参见下列各语言 SDK 文档：

[Android SDK](https://cloud.tencent.com/document/product/436/46421)[C SDK](https://cloud.tencent.com/document/product/436/35560)[C++ SDK](https://cloud.tencent.com/document/product/436/35163)[.NET SDK](https://cloud.tencent.com/document/product/436/32873)
[Go SDK](https://cloud.tencent.com/document/product/436/35059)[iOS SDK](https://cloud.tencent.com/document/product/436/46388)[Java SDK](https://cloud.tencent.com/document/product/436/35217)[JavaScript SDK](https://cloud.tencent.com/document/product/436/35651)
[Node.js SDK](https://cloud.tencent.com/document/product/436/36121)[PHP SDK](https://cloud.tencent.com/document/product/436/34284)[Python SDK](https://cloud.tencent.com/document/product/436/35153)[小程序 SDK](https://cloud.tencent.com/document/product/436/36162)

## 文件夹分享

文件夹是一种特殊的对象，原理同文件分享一致，您可以通过控制台或 COSBrowser 工具获取临时链接分享文件夹，详情请参见 [分享文件夹](https://cloud.tencent.com/document/product/436/60351)。

## 上传文件

如果您希望第三方可以上传对象到存储桶，又不希望对方使用 CAM 账户或临时密钥等方式时，您可以使用预签名 URL 的方式将签名提交给第三方，以供完成临时的上传操作。收到有效预签名 URL 的任何人都可以上传对象。

**说明：**

如果您一定要使用永久密钥来生成预签名，建议永久密钥的权限范围仅限于上传或下载操作，以规避风险。并且所生成的签名有效时长设置为完成本次上传或下载操作所需的最短期限，因为，当指定预签名 URL 的有效时间过期后，请求会中断；申请新的签名后，需要重新执行失败请求，不支持断点续传。

### 方式一：使用 SDK 生成预签名 URL（推荐）

各语言 SDK 提供了生成上传预签名 URL 的方法，生成方法可参考 [预签名授权上传](https://cloud.tencent.com/document/product/436/14114)，选择您熟悉的开发语言。

### 方式二：自行拼接预签名 URL

预签名 URL 实际上就是在对象 URL 之后拼接了签名；因此，您也可以通过 SDK、签名生成工具等，自行生成签名，将 URL 与签名拼接成签名链接用于对象上传。然而，由于签名生成算法较为复杂，一般情况下不推荐这种使用方式。
