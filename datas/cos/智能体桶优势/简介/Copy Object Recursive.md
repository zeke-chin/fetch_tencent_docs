<!-- source: https://cloud.tencent.com/document/product/436/133866 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:35:47+08:00 -->

# Copy Object Recursive

最近更新时间：2026-07-09 15:06:03


## 功能描述

递归复制将整个目录树（包括所有子文件和子目录）复制到目标位置。

**注意：**

当 COS Agent Bucket 收到复制请求或 COS Agent Bucket 正在复制对象时可能会返回错误。如果在复制操作开始之前发生错误，则会收到标准的错误返回。如果在复制操作执行期间发生错误，则依然会返回 HTTP 200 OK，并将错误作为响应体返回。这意味着 HTTP 200 OK 响应既可以包含成功也可以包含错误，在使用此接口时应当进一步根据响应体的内容来判断复制请求的成功与失败并正确地处理结果。

## 请求

### 请求语法

PUT /<ObjectKey>?recursive HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

x-cos-copy-source: <BucketName-APPID>.cos.<Region>.myqcloud.com/<SourceObjectKey>

Authorization: Auth String

**说明：**

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 smhxxxxxxxxxxxxx-1250000000；<Region> 为可用地域，可参见 [产品概述](https://cloud.tencent.com/document/product/436/132574) 文档。

ObjectKey：目标对象路径。

SourceObjectKey：移动对象路径。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求参数

名称 描述 类型 是否必选
recursive 启用递归目录复制模式。无需赋值，只需在 URL 中出现即可。无值 是
conflict_resolution_strategy 冲突解决策略。递归目录移动可选值为 ask、rename，默认为 ask。

ask: 冲突时返回 HTTP 409 Conflict 及 SameNameDirectoryOrFileExists 错误码。

rename: 冲突时自动重命名最后一级目录。string 否

### 请求体

此接口无请求体。

## 响应

### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

### 响应体

请求成功，返回 **application/xml** 数据。

<CopyObjectResult>

 <ETag>&#34;etag-value&#34;</ETag>

 <LastModified>2025-01-15T10:30:00Z</LastModified>

 <CRC64>xxx</CRC64>

</CopyObjectResult>

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型
CopyObjectResult 无 保存 Copy Object Recursive 结果的所有信息 Container

Container 节点 CopyObjectResult 的内容：

节点名称（关键字）父节点 描述 类型
ETag CopyObjectResult 目标对象的 ETag 值（带双引号）。string
LastModified CopyObjectResult 目标对象的最后修改时间，RFC 3339 格式。date
CRC64 CopyObjectResult 目标对象的 CRC64 值。integer

## 实际案例

### 案例一：简单案例

#### 请求

PUT /myspace/bbb?recursive HTTP/1.1

Host: smhxxx-1250000000.cos.ap-chengdu.myqcloud.com

x-cos-copy-source: smhxxx-1250000000.cos.ap-chengdu.myqcloud.com/myspace/aaa

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1566302375;1566309575&q-key-time=1566302375;1566309575&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=delete&q-signature=****************************************

#### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Transfer-Encoding: chunked

Connection: keep-alive

Date: Tue, 20 Aug 2019 11:59:35 GMT

x-cos-request-id: NWQ1YmUwYTdfM2FiMDJhMDlfYzczN18zMGM1****

<CopyObjectResult>

 <ETag>&#34;d-1780579801973809791&#34;</ETag>

 <LastModified>2026-06-04T13:30:01Z</LastModified>

 <CRC64>5404623458528365127</CRC64>

</CopyObjectResult>

### 案例二：递归复制时，目标位置已存在

#### 请求

PUT /myspace/bbb?recursive HTTP/1.1

Host: smhxxx-1250000000.cos.ap-chengdu.myqcloud.com

x-cos-copy-source: smhxxx-1250000000.cos.ap-chengdu.myqcloud.com/myspace/aaa

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1566302375;1566309575&q-key-time=1566302375;1566309575&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=delete&q-signature=****************************************

#### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Transfer-Encoding: chunked

Connection: keep-alive

Date: Tue, 20 Aug 2019 11:59:35 GMT

x-cos-request-id: NWQ1YmUwYTdfM2FiMDJhMDlfYzczN18zMGM1****

<Error>

 <Code>FileAlreadyExists</Code>

 <Message>The destination directory already exists. Recursive directory copy does not support overwriting an existing destination directory. Use conflict_resolution_strategy=rename to auto-rename, or remove the existing destination first.</Message>

 <Resource>/smh26zn7j7lfnwnc-1251081331/myspace/bbb</Resource>

</Error>
