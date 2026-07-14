<!-- source: https://cloud.tencent.com/document/product/436/32493 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:39:30+08:00 -->

# GET Bucket referer

最近更新时间：2026-02-10 17:15:21


## 功能描述

GET Bucket referer 接口用于读取存储桶 Referer 白名单或者黑名单。

## 请求

### 请求示例

GET /?referer HTTP 1.1

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com

Date: GMT Date

Authorization: Auth String

**说明：**

Host: <BucketName-APPID>.cos.<Region>.myqcloud.com，其中 <BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；<Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。

Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

### 请求体

该请求的请求体为空。

## 响应

### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

### 响应体

该响应体返回为 application/xml 数据，包含完整节点数据的内容展示如下：

<RefererConfiguration>

 <Status>Enabled</Status>

 <RefererType>White-List</RefererType>

 <DomainList>

 <Domain>*.qq.com</Domain>

 <Domain>*.qcloud.com</Domain>

 </DomainList>

 <EmptyReferConfiguration>Allow</EmptyReferConfiguration>

</RefererConfiguration>

具体的节点描述如下：

名称 父节点 描述 类型
RefererConfiguration 无 防盗链配置信息 Container
Status RefererConfiguration 是否开启防盗链，枚举值：Enabled，Disabled String
RefererType RefererConfiguration 防盗链类型，枚举值：Black-List，White-List String
DomainList RefererConfiguration 生效域名列表。 支持多个域名且为前缀匹配， 支持带端口的域名和 IP， 支持通配符`*`，做二级域名或多级域名的通配 Container
Domain DomainList 单条生效域名，例如 `www.qq.com`，`192.168.1.2:8080`， `*.qq.com`String
EmptyReferConfiguration RefererConfiguration 是否允许空 Referer 访问，枚举值：Allow，Deny，默认值为 Deny String

### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

### 请求

GET /?referer HTTP 1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Fri, 25 Feb 2017 04:10:22 GMT

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1547105134;32526689134&q-key-time=1547105134;32620001134&q-header-list=content-md5;content-type;host&q-url-param-list=referer&q-signature=****************************************

### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 260

Connection: keep-alive

Date: Fri, 25 Feb 2017 04:10:22 GMT

Server: tencent-cos

x-cos-request-id: NTg3ZjFjMmJfOWIxZjRlXzZmNDhf****

<RefererConfiguration>

 <Status>Enabled</Status>

 <RefererType>White-List</RefererType>

 <DomainList>

 <Domain>*.qq.com</Domain>

 <Domain>*.qcloud.com</Domain>

 </DomainList>

 <EmptyReferConfiguration>Allow</EmptyReferConfiguration>

</RefererConfiguration>
