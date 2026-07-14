<!-- source: https://cloud.tencent.com/document/product/436/102873 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:14:47+08:00 -->

# COS 策略生成工具

最近更新时间：2026-04-10 16:39:32


## 功能概述

COS 策略生成工具是腾讯云对象存储（Cloud Object Storage，COS）为用户提供的 Web 端工具，支持图形化配置，一键生成 JSON 格式的策略。

针对不同策略类型，在填入指定参数后，可以一键生成结构化的JSON策略语法，便于后端处理。目前支持三种策略类型的 JSON，分别是用户策略、存储桶策略、STS策略。

关于各策略类型的概述和相关信息，请参见 [用户策略（CAM策略）](https://cloud.tencent.com/document/product/436/68280)**、**[存储桶策略（Bucket Policy）](https://cloud.tencent.com/document/product/436/18031)**、**[使用临时密钥访问COS](https://cloud.tencent.com/document/product/436/68283)。

## 注意事项

本策略生成工具不识别和提示您填写的错误参数。若您生成的 JSON 格式策略需要实际生效，请务必按照您的业务需求进行准确填写。

本策略生成工具将识别您填写的不合法参数，并进行相应的提示。但仍可能生成一个无法实际生效的策略。

本策略生成工具将识别及提示您尚未填写的必填参数项，且如果您未完成必填参数项的填写，您将无法生成 JSON 格式的策略。

## 工具地址

1. 您可以单击 [COS策略生成工具](https://cos.cloud.tencent.com/tools/cos?tab=calculate) 直接进入该页面。

2. 通过 [对象存储控制台](https://console.cloud.tencent.com/cos5) 访问该页面，详情可参考 [操作步骤](https://cloud.tencent.com/document/product/436/102873#.E4.BD.BF.E7.94.A8.E6.96.B9.E6.B3.95)。

## 适用场景

COS 策略生成工具适用于以下情况：

熟悉用户策略、存储桶策略、STS 策略，但不熟悉 JSON 语法的用户。

需要通过 [API](https://cloud.tencent.com/document/product/436/8282) 或 [SDK](https://cloud.tencent.com/document/product/436/6474) 添加用户策略、存储桶策略、STS 策略的用户。

需要批量添加用户策略、存储桶策略、STS 策略的用户。

### 用户策略（CAM策略）

用户可以在 [CAM](https://cloud.tencent.com/document/product/598/10583) 中，对于主账号名下的不同类型用户，授予不同的权限。这些权限通过访问策略语言描述，并以用户为出发点进行授权，因此被称为**用户策略**。更多内容可参考 [用户策略](https://cloud.tencent.com/document/product/436/68280) 文档。

**说明：**

用户策略需要撰写完成后，再对子用户、用户组或角色执行关联操作。

用户策略不支持将操作和资源权限授予匿名用户。

当您关心用户能做什么，推荐用户策略时，可通过查找 CAM 用户，并检查其所属用户组的权限来了解用户能做什么。推荐场景有：

要配置对象存储（Cloud Object Storage，COS）服务级权限时，例如创建桶（PutBucket）、列举桶（GetService）。

需要使用主账号下所有 COS 桶和对象。

要对主账号下的大量 CAM 用户授予相同权限。

### 存储桶策略（Bucket Policy）

存储桶策略作用于配置的存储桶和存储桶内对象，您可以通过存储桶策略为 CAM 子账号、其他主账号、甚至匿名用户授权存储桶及存储桶内对象的操作权限。更多内容可参考 [存储桶策略](https://cloud.tencent.com/document/product/436/18031) 文档。

当您关心谁能访问这个 COS 桶时，推荐使用存储桶策略。可通过查找存储桶，并检查存储桶策略来了解谁能访问。推荐场景有：

针对某个存储桶进行授权。

相比 ACL，存储桶策略更加灵活。

相比用户策略，存储桶策略支持跨账号授权及匿名用户授权。

### STS策略

STS 策略与临时密钥相关。临时密钥是由 [安全凭证服务（Security Token Service,STS）](https://cloud.tencent.com/document/product/1312/48195) 提供的临时访问凭证，在申请临时密钥过程中，可以通过设置 Policy 参数（即STS策略），限制操作和资源，为临时密钥增加临时策略约束使用者的权限。更多内容可参考 [使用临时密钥访问COS](https://cloud.tencent.com/document/product/436/68283) 、[临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048)和 [用于前端直传 COS 的临时密钥安全指引](https://cloud.tencent.com/document/product/436/40265)文档。

**注意：**

申请临时密钥之前，您必须拥有访问管理（Cloud Access Management，CAM）用户（腾讯云主账号或子账号）。

临时密钥的推荐场景有：

授权第三方临时访问COS。例如，用户开发了客户端 App，将数据存储在 COS 存储桶上，此时将永久密钥直接存放在APP客户端不安全，但又需要授予客户端上传、下载权限。

前端数据直传等临时授权。可参考[Web 端直传实践](https://cloud.tencent.com/document/product/436/9067)、[小程序直传实践](https://cloud.tencent.com/document/product/436/34929)、[移动应用直传实践](https://cloud.tencent.com/document/product/436/9068)、[Flutter 直传实践](https://cloud.tencent.com/document/product/436/95265)、[uni-app 直传实践](https://cloud.tencent.com/document/product/436/71469)使用临时密钥。

## 操作步骤

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。

2. 在左侧导航栏中，单击**常用工具 > 策略生成工具**。

3. 在 [策略生成工具](https://cos.cloud.tencent.com/tools/cos?tab=calculate) 页面，根据所选的策略类型，按以下说明选择填写各项参数。

**注意：**

当您在授权时，请**务必**根据业务需要，按照 [最小权限原则](https://cloud.tencent.com/document/product/436/38618) 进行授权，限定用户执行受限的操作（如仅授权读操作），访问指定前缀的资源。

若您直接授予其他用户所有资源`(resource:*)`，或者所有操作`(action:*)`权限，则可能会因权限范围过大导致预期外的越权操作，引起**数据安全风险**。

CAM策略

存储桶策略

STS策略

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/0f95e4d1c1f5e7e7f5f65cf00c6d111e.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/0f95e4d1c1f5e7e7f5f65cf00c6d111e.png)

1. 在当前页面，选择策略类型为 **CAM策略** 。

2. 参数字段说明如下，关于配置项的更多说明请参见 [访问管理授权指南](https://cloud.tencent.com/document/product/598/34545) 、[访问管理策略语法结构](https://cloud.tencent.com/document/product/598/10604) 和 [访问策略语言概述](https://cloud.tencent.com/document/product/436/18023)。

**参数名称****是否必填****字段名****说明**
效力 是 Effect 支持选择“允许”或“拒绝”，对应策略语法中的“Allow”和“Deny”。
资源路径 是 Resource 资源路径由 **地域、存储桶名称、具体路径**组成，支持添加整个存储桶或者指定资源

**整个存储桶：**若您希望配置将资源范围指定为整个存储桶，仅需填写地域、存储桶名称。

**指定资源：**若您希望将资源范围限定到指定文件夹，需要指定地域、存储桶名称、具体路径。

**说明：**

地域、存储桶名称和具体路径等信息，可参考当前表格的对应参数说明进行填写。
地域 是/存储桶的所在地域，例如 ap-beijing。关于地域的更多信息请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。
存储桶名称 是/存储桶名称由自定义名称和 APPID 两部分构成，例如 examplebucket-1250000000。关于存储桶名称和 APPID 的更多信息请参见 [存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 、[APPID](https://cloud.tencent.com/document/product/436/44352#appid)、[对象存储API术语信息](https://cloud.tencent.com/document/product/436/7751#.E6.9C.AF.E8.AF.AD.E4.BF.A1.E6.81.AF)。
具体路径 是/具体的资源路径。

若您不指定具体路径，默认为“*”。

若您希望指定具体路径，需要填写。例如：

需要指定存储桶中的/folder/文件夹下所有对象，填写 folder/*

需要指定存储桶中的/folder/exampleobject对象，填写 folder/exampleobject

需要指定存储桶中的所有以.txt为后缀对象，填写 *.txt
操作 是 Action 添加、删除您需要授权的操作。关于操作的更多信息请参见[操作列表](https://cloud.tencent.com/document/product/436/10111)。
条件 否 Condition 授予权限时指定条件，例如限制用户来访 IP。更多条件说明请参见 [条件键说明及使用示例](https://cloud.tencent.com/document/product/436/71307)。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/c5c5145ebed04f06de58ca9aebfd5f0b.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/c5c5145ebed04f06de58ca9aebfd5f0b.png)

1. 在当前页面，选择策略类型为 **存储桶策略** 。

2. 参数字段说明如下，关于配置项的更多说明请参见 [添加存储桶策略](https://cloud.tencent.com/document/product/436/33369) 和 [访问策略语言概述](https://cloud.tencent.com/document/product/436/18023)。

**参数名称****是否必填****字段名****说明**
效力 是 Effect 支持选择“允许”或“拒绝”，对应策略语法中的“Allow”和“Deny”。
用户 是 Principal 支持添加、删除被授权用户，包括所有用户(*)、主账号、子账号和云服务，配置项说明如下：

**所有用户：**若您希望为**匿名用户**开放操作权限，可以选择此项。配置后，请求对象时无需携带签名，所有用户可直接通过链接访问对象，存在**数据泄露风险**，请谨慎设置。

**主账号：**若您希望为**指定主账号**开放操作权限，可以选择此项。选择后需要进一步指定具体主账号 UIN。

**子账号：**若您希望为**指定子账号**开放操作权限，可以选择此项。选择后需要进一步指定具体子账号 UIN。

**云服务：**若您希望为**指定云服务**开放操作权限，可以选择此项。选择后需要进一步指定具体云服务。
资源 是 Resource 资源用六段式描述，支持添加整个存储桶或者指定资源，配置项说明如下：

**整个存储桶：**若您希望配置存储桶配置相关的权限，或者将资源范围指定为整个存储桶，可以选择此项。

**指定资源：**若您希望将资源范围限定到指定文件夹，可以选择此项。选择后，需要在“资源路径”进一步指定具体的目录。

**说明：**

选择后需要填写地域、主账号UIN、存储桶名称和资源路径等信息，可参考当前表格的对应参数说明进行填写。
策略 ID 否 Sid 当前策略规则的 ID，仅支持英文。如不显式指定该字段，将自动创建随机字符串。
地域 是/存储桶的所在地域，例如 ap-beijing。关于地域的更多信息请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。
主账号 UIN 是/若您选择的用户为“子账号”或者“云服务”，需要填写主账号UIN。关于UIN的概念请参见 [UIN](https://cloud.tencent.com/document/product/436/44352#uin)。
存储桶名称 是/存储桶名称由自定义名称和 APPID 两部分构成，例如 examplebucket-1250000000。关于存储桶名称和 APPID 的更多信息请参见 [存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 、[APPID](https://cloud.tencent.com/document/product/436/44352#appid)、[对象存储API术语信息](https://cloud.tencent.com/document/product/436/7751#.E6.9C.AF.E8.AF.AD.E4.BF.A1.E6.81.AF)。
资源路径 是/具体的资源路径。

若您选择的资源为“整个存储桶”，资源路径默认为整个桶。

若您选择的资源为“指定资源”，需要填写具体的资源路径。例如：

需要指定存储桶中的/folder/文件夹下所有对象，填写 folder/*

需要指定存储桶中的/folder/exampleobject对象，填写 folder/exampleobject

需要指定存储桶中的所有以.txt为后缀对象，填写 *.txt
操作 是 Action 添加、删除您需要授权的操作。关于操作的更多信息请参见[操作列表](https://cloud.tencent.com/document/product/436/10111)。

**注意：**

CDN 服务账号仅支持 GetObject、HeadObject、OptionsObject操作。
条件 否 Condition 授予权限时指定条件，例如限制用户来访 IP。更多条件说明请参见 [条件键说明及使用示例](https://cloud.tencent.com/document/product/436/71307)。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/35bb6eed9d4c706d566a004f28b72934.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/35bb6eed9d4c706d566a004f28b72934.png)

1. 在当前页面，选择策略类型为 **STS策略** 。

2. 参数字段说明如下，关于配置项的更多说明请参见 [获取联合身份临时访问凭证](https://cloud.tencent.com/document/product/1312/48195#2.-.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0) 和 [访问策略语言概述](https://cloud.tencent.com/document/product/436/18023)。

**参数名称****是否必填****字段名****说明**
效力 是 Effect 支持选择“允许”或“拒绝”，对应策略语法中的“Allow”和“Deny”。
资源路径 是 Resource 资源路径由 **地域、存储桶名称、具体路径**组成，支持添加整个存储桶或者指定资源

**整个存储桶：**若您希望配置将资源范围指定为整个存储桶，仅需填写地域、存储桶名称。

**指定资源：**若您希望将资源范围限定到指定文件夹，需要指定地域、存储桶名称、具体路径。

**说明：**

地域、存储桶名称和具体路径等信息，可参考当前表格的对应参数说明进行填写。
地域 是/存储桶的所在地域，例如 ap-beijing。关于地域的更多信息请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。
存储桶名称 是/存储桶名称由自定义名称和 APPID 两部分构成，例如 examplebucket-1250000000。关于存储桶名称和 APPID 的更多信息请参见 [存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 、[APPID](https://cloud.tencent.com/document/product/436/44352#appid)、[对象存储API术语信息](https://cloud.tencent.com/document/product/436/7751#.E6.9C.AF.E8.AF.AD.E4.BF.A1.E6.81.AF)。
具体路径 是/具体的资源路径。

若您不指定具体路径，默认为“*”。

若您希望指定具体路径，需要填写。例如：

需要指定存储桶中的/folder/文件夹下所有对象，填写 folder/*

需要指定存储桶中的/folder/exampleobject对象，填写 folder/exampleobject

需要指定存储桶中的所有以.txt为后缀对象，填写 *.txt
操作 是 Action 添加、删除您需要授权的操作。关于操作的更多信息请参见[操作列表](https://cloud.tencent.com/document/product/436/10111)。
条件 否 Condition 授予权限时指定条件，例如限制用户来访 IP。更多条件说明请参见 [条件键说明及使用示例](https://cloud.tencent.com/document/product/436/71307)。

4. 单击生成策略。

右侧的结果反馈中将展示JSON格式的策略。该工具支持多次生成策略，并且提供一键复制和一键清除的能力。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/fe66e0dca871ee9f68098c80e8471e0f.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/fe66e0dca871ee9f68098c80e8471e0f.png)
