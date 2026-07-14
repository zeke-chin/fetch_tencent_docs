<!-- source: https://cloud.tencent.com/document/product/436/133861 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:36:08+08:00 -->

# Delete Object Recursive

最近更新时间：2026-07-09 15:06:03


## 功能描述

递归删除整个目录树（包括所有子文件和子目录）。

**注意：**

当 COS Agent Bucket 收到删除请求或 COS Agent Bucket 正在删除对象时可能会返回错误。如果在删除操作开始之前发生错误，则会收到标准的错误返回。如果在删除操作执行期间发生错误，则依然会返回 HTTP 200 OK，并将错误作为响应体返回。这意味着 HTTP 200 OK 响应既可以包含成功也可以包含错误，在使用此接口时应当进一步根据响应体的内容来判断删除请求的成功与失败并正确地处理结果。

删除后无法恢复，请谨慎操作。

## 请求

### 请求语法

DELETE /<ObjectKey>?recursive HTTP/1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Authorization: Auth String

**说明：**

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 smhxxxxxxxxxxxxx-1250000000；<Region> 为可用地域，可参见 [产品概述](https://cloud.tencent.com/document/product/436/132574) 文档。

ObjectKey：对象路径。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求参数

名称 描述 类型 是否必选
recursive 启用递归删除整个目录树。无需赋值，只需在 URL 中出现即可。固定值 是

### 请求体

此接口无请求体。

## 响应

### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

### 响应体

请求成功，返回 **application/xml** 数据。

<DeleteResult>

 <Deleted>

 <Key>key</Key>

 </Deleted>

</DeleteResult>

具体的节点描述如下：

节点名称（关键字）父节点 描述 类型
DeleteResult 无 保存 Delete Object Recursive 结果的所有信息 Container

Container 节点 DeleteResult 的内容：

节点名称（关键字）父节点 描述 类型
Deleted DeleteResult 删除成功的对象条目 Container
Key Deleted 删除成功的对象路径。string

## 实际案例

### 请求

DELETE /myspace/bbb?recursive HTTP/1.1

Host: smhxxx-1250000000.cos.ap-chengdu.myqcloud.com

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1566302375;1566309575&q-key-time=1566302375;1566309575&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=delete&q-signature=****************************************

### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Transfer-Encoding: chunked

Connection: keep-alive

Date: Tue, 20 Aug 2019 11:59:35 GMT

x-cos-request-id: NWQ1YmUwYTdfM2FiMDJhMDlfYzczN18zMGM1****

<DeleteResult>

 <Deleted>

 <Key>myspace/bbb</Key>

 </Deleted>

</DeleteResult>
