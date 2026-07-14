<!-- source: https://cloud.tencent.com/document/product/436/30752 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:04:49+08:00 -->

# ACL

最近更新时间：2026-05-27 17:52:33


## 基本概念

访问控制列表（ACL）使用 XML 语言描述，是与资源关联的一个指定被授权者和授予权限的列表，每个存储桶和对象都有与之关联的 ACL，支持向匿名用户或其他腾讯云的主账号授予基本的读写权限。

**注意：**

使用与资源关联的 ACL 管理有一些限制：

资源的拥有者始终对资源具备 FULL_CONTROL 权限，无法撤销或修改。

匿名用户无法成为资源拥有者，此时对象资源的拥有者属于存储桶的创建者（腾讯云主账号）。

仅可对腾讯云访问管理（Cloud Access Management，CAM）主账号或预设用户组授予权限，无法授予自定义用户组权限，不推荐授予子用户权限。

不支持对权限附加条件。

不支持显示拒绝的权限。

一个资源最多可以拥有100条 ACL 策略。

## 适用场景

**注意：**

开放匿名用户访问（公有读）属于高危操作，有流量盗刷的风险；必须使用公有读时，可 [设置防盗链](https://cloud.tencent.com/document/product/436/13319) 进行安全防护。

当您仅需要为存储桶和对象设置一些简单的访问权限或开放匿名访问，可以选择 ACL。但在更多的情况下，推荐您优先使用存储桶策略或用户策略，灵活程度更高。ACL 的适用场景包括：

仅设置简单的访问权限。

在控制台快速设置访问权限。

需要将某个对象、目录或存储桶开放给所有互联网匿名用户访问，ACL 操作更为便捷。

## ACL 的元素

### 身份 Grantee

支持的被授权身份可以是某个 CAM 主账号，或者是某个预设的 CAM 用户组。

**注意：**

当您授予了其他腾讯云主账号访问权限时，这个被授权的主账号可以授权其名下的子用户、用户组或角色的访问权限。

对象存储（Cloud Object Storage，COS）完全不建议您对匿名用户或 CAM 用户组授予 WRITE、WRITE_ACP 或 FULL_CONTROL 权限。一旦授权后，用户组可以对您的资源进行上传、下载、删除等行为，这将会给您带来数据丢失、扣费等风险。

在存储桶或对象的 ACL 中支持授予的身份包括：

跨账号：请使用主账号的 ID，通过**账号中心**的 [账号信息](https://console.cloud.tencent.com/developer) 获得账号 ID，例如100000000001。

预设用户组：请使用 URI 标签标记预设的用户组，支持的用户组包括：

匿名用户组 -`http://cam.qcloud.com/groups/global/AllUsers` 该组代表了任何人都可以无需授权而访问资源，无论请求已签名或者未签名。

认证用户组 -`http://cam.qcloud.com/groups/global/AuthenticatedUsers` 该组代表所有经过腾讯云 CAM 账户认证的用户都可以访问资源。

### 操作 Permission

腾讯云 COS 在资源 ACL 上支持的操作实际上是一系列的操作集合，对于存储桶和对象 ACL 来说分别代表不同的含义。

#### **存储桶的操作**

下表列出了支持在存储桶 ACL 中设置的操作列表：

操作集 描述 许可的行为
READ 列出对象 HeadBucket、GetBucketObjectVersions、ListMultipartUploads
WRITE 上传、覆盖和删除对象 PutObject、PutObjectCopy、PostObject、InitiateMultipartUpload、UploadPart、UploadPartCopy、CompleteMultipartUpload、 DeleteObject
READ_ACP 读取存储桶的 ACL GetBucketACL
WRITE_ACP 写入存储桶的 ACL PutBucketACL
FULL_CONTROL 以上四种权限的集合 以上所有行为的集合

**注意：**

请谨慎授予存储桶 WRITE、WRITE_ACP 或 FULL_CONTROL 权限。授予存储桶 WRITE 权限将允许被授权者覆盖或删除已有的任何对象。

#### **对象的操作**

下表列出了支持在对象 ACL 中设置的操作列表：

操作集 描述 许可的行为
READ 读取对象 GetObject、GetObjectVersion、HeadObject
READ_ACP 读取对象的 ACL GetObjectACL、GetObjectVersionACL
WRITE_ACP 写入对象的 ACL PutObjectACL、PutObjectVersionACL
FULL_CONTROL 以上三种权限的集合 以上所有行为的集合

**说明：**

对象不支持授予 WRITE 操作集。

### 预设的 ACL

COS 支持一系列预设的 ACL 进行授权，方便简单权限的描述。使用预设 ACL 描述时，需要在 PUT Bucket/Object 或 PUT Bucket/Object acl 中携带 x-cos-acl 头部并描述所需权限，如果同时在请求正文中携带了 XML 的描述内容，我们将优先选择头部中的描述并忽略请求正文中的 XML 描述。

#### **存储桶的预设 ACL**

预设名称 描述
private 创建者（主账号）具备 FULL_CONTROL 权限，其他人没有权限（默认）
public-read 创建者具备 FULL_CONTROL 权限，匿名用户组具备 READ 权限
public-read-write 创建者和匿名用户组都具备 FULL_CONTROL 权限，通常不建议授予此权限
authenticated-read 创建者具备 FULL_CONTROL 权限，认证用户组具备 READ 权限

#### **对象的预设 ACL**

预设名称 描述
default 空描述，此时根据各级目录的显式设置及存储桶的设置来确定是否允许请求（默认）
private 创建者（主账号）具备 FULL_CONTROL 权限，其他人没有权限
public-read 创建者具备 FULL_CONTROL 权限，匿名用户组具备 READ 权限
authenticated-read 创建者具备 FULL_CONTROL 权限，认证用户组具备 READ 权限
bucket-owner-read 创建者具备 FULL_CONTROL 权限，存储桶拥有者具备 READ 权限
bucket-owner-full-control 创建者和存储桶拥有者都具备 FULL_CONTROL 权限

**说明：**

对象不支持授予 public-read-write 权限。

## 示例

### 存储桶的 ACL

在创建存储桶时，COS 将创建一个默认的 ACL 以赋予资源拥有者对资源的完全控制权限（FULL_CONTROL），示例如下：

<AccessControlPolicy>

 <Owner>

 <ID>Owner-Cononical-CAM-User-Id</ID>

 </Owner>

 <AccessControlList>

 <Grant>

 <Grantee>

 <ID>Owner-Cononical-CAM-User-Id</ID>

 </Grantee>

 <Permission>FULL_CONTROL</Permission>

 </Grant>

 </AccessControlList>

</AccessControlPolicy>

### 对象的 ACL

**在创建对象时，COS 默认不会创建 ACL，此时对象的拥有者为存储桶拥有者**。对象继承存储桶的权限，与存储桶的访问权限一致。由于对象没有默认的 ACL，其将遵循存储桶策略（Bucket Policy）中对访问者和其行为的定义，来判断请求是否被许可。详情请参见 [访问策略语言概述](https://cloud.tencent.com/document/product/436/18023) 文档。

如果您需要对对象授予其他访问权限，您可以在此基础上添加更多的 ACL 来描述对象的访问权限。例如授予匿名用户只读单个对象的权限，示例如下：

<AccessControlPolicy>

 <Owner>

 <ID>Owner-Cononical-CAM-User-Id</ID>

 </Owner>

 <AccessControlList>

 <Grant>

 <Grantee>

 <ID>Owner-Cononical-CAM-User-Id</ID>

 </Grantee>

 <Permission>FULL_CONTROL</Permission>

 </Grant>

 <Grant>

 <Grantee>

 <URI>http://cam.qcloud.com/groups/global/AllUsers</URI>

 </Grantee>

 <Permission>READ</Permission>

 </Grant>

 </AccessControlList>

</AccessControlPolicy>

## 使用方法

### 使用对象存储控制台

#### 设置存储桶访问权限

您可以通过对象存储控制台来设置或修改存储桶的访问权限。对象存储 COS 支持设置两种权限类型：

**公共权限**：私有读写、公有读私有写和公有读写。关于公共权限的说明，请参见存储桶概述中的 [权限类别](https://cloud.tencent.com/document/product/436/13312#.E6.9D.83.E9.99.90.E7.B1.BB.E5.88.AB)。

**用户权限**：主账号默认拥有存储桶所有权限（即完全控制）。另外 COS 支持添加子账号有数据读取、数据写入、权限读取（即授予用户读取“存储桶访问权限”的权限）、权限写入（即授予用户写入“存储桶访问权限”的权限），甚至**完全控制**的最高权限。

**说明：**

当存储桶为私有读写或对指定账号授予用户权限，请求对象时需携带签名用于身份验证，关于签名说明，请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778)。

当存储桶为公有读私有写或公有读写时，请求对象时无需携带签名，匿名用户可直接通过链接访问对象，您的数据会存在泄露风险，请谨慎设置。

##### 单个授权

1.登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。

2.在左侧导航栏中，单击**存储桶列表**。

3.找到您需要设置或修改访问权限的存储桶，单击其存储桶名称。

4.在存储桶配置页面，单击**权限管理**>**存储桶访问权限**，对存储桶的公共权限和用户权限（例如添加子账号，子账号 ID 可在 [访问管理](https://console.cloud.tencent.com/cam) 控制台查看）进行设置。

**注意：**

若您必须使用公有读私有写或公有读写权限且未配置默认告警，则推荐开启告警策略。若已配置，则无需配置且不提示。

5.单击**保存**，即可完成存储桶访问权限设置。

##### 批量授权

1.登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。

2.在左侧导航栏中，单击**存储桶列表**。

3.单击列表上方的**授权管理**。

4.在弹窗中选择希望授权的存储桶。然后对存储桶的公共权限和用户权限（例如添加子账号，子账号 ID 可在 [访问管理](https://console.cloud.tencent.com/cam) 控制台查看）进行设置。

**注意：**

授权管理将同时修改公共权限和用户权限。

若您只需修改用户权限，请务必先检查您之前存储桶的公共权限和当前配置是否一致，否则会覆盖之前的权限。

5.配置完成后，单击**确定**，即可完成多个存储桶的访问权限设置。

#### 设置对象的访问权限

对象存储（Cloud Object Storage，COS）提供基于对象维度的访问权限设置，且该权限优先级高于存储桶的访问权限。

**说明：**

对象的访问权限只在用户通过默认域名访问时有效。通过 CDN 加速域名和自定义域名访问时，以存储桶访问权限为准。

访问策略规则存在数量限制，详情请参见 [规格与限制](https://cloud.tencent.com/document/product/436/14518)。

##### 操作步骤

1.登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。

2.在左侧导航栏中，单击**存储桶列表**，进入存储桶列表页面。

3.找到对象所在的存储桶，单击其存储桶名称，进入存储桶管理页面。

4.在左侧导航栏中，选择**文件列表**，进入文件列表页面。

5.找到需要设置权限的对象，并单击右侧的**详情**，进入文件详情页。（若是文件夹，可单击右侧的**设置权限**）。

6.在“对象访问权限”栏中，根据实际需求，设置访问权限。

COS 支持为对象设置两种权限类型：

**公共权限**：包括继承权限、私有读写、公有读私有写。关于公共权限的说明，请参见对象概述中的 [权限类别](https://cloud.tencent.com/document/product/436/13324#.E8.AE.BF.E9.97.AE.E6.9D.83.E9.99.90.E7.B1.BB.E5.9E.8B)。

**用户权限**：主账号默认拥有对象所有权限（即完全控制）。

7.单击**保存**，即可设置对象的访问权限。

若您需要对多个对象进行批量设置或修改访问权限，可勾选多个对象，并单击上方的**更多操作**>**修改访问权限**即可设置。

### 使用 REST API/SDK

您可以通过以下 API 管理存储桶/对象 ACL：

管理存储桶 ACL

[PUT Bucket acl](https://cloud.tencent.com/document/product/436/7737)

[GET Bucket acl](https://cloud.tencent.com/document/product/436/7733)

管理对象 ACL

[PUT Object acl](https://cloud.tencent.com/document/product/436/7748)

[GET Object acl](https://cloud.tencent.com/document/product/436/7744)

您可以直接调用 SDK 管理存储桶/对象 ACL，详情请参见下列各语言 SDK 文档：

[Android](https://cloud.tencent.com/document/product/436/41912)、[C](https://cloud.tencent.com/document/product/436/41925)、[C++](https://cloud.tencent.com/document/product/436/51344)、[.NET(C#)](https://cloud.tencent.com/document/product/436/42610)、[Go](https://cloud.tencent.com/document/product/436/55472)、[iOS](https://cloud.tencent.com/document/product/436/86154)、[Java](https://cloud.tencent.com/document/product/436/50708)、[JavaScript](https://cloud.tencent.com/document/product/436/57426)、[Node.js](https://cloud.tencent.com/document/product/436/51854)、[PHP](https://cloud.tencent.com/document/product/436/41898)、[Python](https://cloud.tencent.com/document/product/436/44355)、[小程序](https://cloud.tencent.com/document/product/436/110937)。

### 使用工具

您可以使用工具管理存储桶/对象 ACL，例如 [COSBrowser](https://cloud.tencent.com/document/product/436/11366)、[COSCMD](https://cloud.tencent.com/document/product/436/10976)、[COSCLI](https://cloud.tencent.com/document/product/436/63143)，更多工具介绍请参见 [工具概览](https://cloud.tencent.com/document/product/436/6242)。
