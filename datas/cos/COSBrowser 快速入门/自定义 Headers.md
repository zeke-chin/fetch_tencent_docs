<!-- source: https://cloud.tencent.com/document/product/436/13361 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:02:04+08:00 -->

# 自定义 Headers

最近更新时间：2025-02-27 17:30:22


## 简介

对象的 HTTP 头部（元数据头部 ）是服务器以 HTTP 协议传送 HTML 资料到浏览器前所送出的字符串。通过修改 HTTP 头部（元数据头部），可以改变页面的响应形式，或者传达配置信息，例如修改缓存时间、修改对象的 HTTP 头部不会修改对象本身。

**说明：**

 归档存储、深度归档存储类型的对象，仅支持在上传时设置自定义 Headers，不支持对已上传的对象设置自定义 Headers。

## 操作步骤

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。

2. 在左侧导航栏中，单击**存储桶列表**，进入存储桶列表页面。

3. 找到对象所在的存储桶，单击其**存储桶名称**，进入存储桶管理页面。

4. 在左侧导航栏中，单击**文件列表**，进入文件列表页面。

5. 找到需要自定义头部的对象，在其右侧操作栏中，选择**更多**>**自定义头部**进行设置。若您需要对多个对象自定义头部，可勾选多个对象，并选择上方的**更多操作**>**自定义头部**进行设置。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/1bd84ca989953e546b850cc18810f59c.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/1bd84ca989953e546b850cc18810f59c.png)

6. 在弹出的窗口中，选择需要设置的元数据头部参数类型，输入对应的元数据值，单击**确定**即可。 COS 提供了以下6种对象 HTTP 头部标识供配置。头部配置说明如下：

HTTP 头部 说明 示例
Content-Type 文件的 MIME 信息 Content-Type: image/jpeg，表示内容类型为 JPEG 格式的图像。
Cache-Control 文件的缓存机制 Cache-Control: no-cache：表示不可直接使用缓存，而是先到服务端验证 Object 是否已更新。如果 Object 已更新，表明缓存已过期，需从服务端重新下载 Object；如果 Object 未更新，表明缓存未过期，此时将使用本地缓存。

Cache-Control: max-age=200，表示缓存内容的相对过期时间，单位为秒。
Content-Disposition MIME 协议的扩展 Content-Disposition: inline，表示直接预览文件内容。

Content-Disposition: attachment，表示以原文件名的形式下载到浏览器指定路径。

Content-Disposition: attachment; filename="FileName"，表示以自定义文件名的形式下载到浏览器指定路径。FileName 用于自定义下载后的文件名称，例如 example.jpg。如果附件名为中文，则需要经过 URL 编码，示例为`attachment; filename* = UTF-8' '%E4%B8%AD%E6%96%87.txt`
Content-Encoding 文件的编码格式 Content-Encoding: gzip，表示响应内容经过 Gzip 压缩。

**注意：**

如果修改了 Header 中的 Content-Encoding 为 gzip，但是文件本身没有提前使用 gzip 压缩过，会出现解码错误。
Expires 用来控制缓存的失效日期 Expires: Wed, 21 Oct 2015 07:28:00 GMT，表示缓存内容的过期时间为 2015年10月21日07:28:00 GMT。
x-cos-meta-[自定义后缀]用户自定义内容 x-cos-meta-via: homepage，表示该请求或响应是通过“homepage”这个来源或页面发起的。

**注意：**

用户自定义元数据头部固定格式为 `x-cos-meta-[自定义后缀]`，其中自定义后缀支持减号（-）、数字、英文（a～z）。英文字符的大写字母会被转成小写字母，不支持下划线（_）在内的其他字符。

用户自定义元数据头部没有数量限制，单条大小限制2KB，所有 `x-cos-meta-[自定义后缀]` 头部的总大小不超过4KB。

## 示例

在 APPID 为 1250000000，创建存储桶名称为 examplebucket-1250000000。存储桶根目录下上传了对象 `exampleobject.txt`。

### 未自定义对象的 HTTP 头部

未自定义对象的 HTTP 头部时，浏览器或客户端下载时得到的对象头部范例如下：

#### 请求

GET /exampleobject.txt HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Fri, 10 Apr 2020 09:35:16 GMT

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1586511316;1586518516&q-key-time=1586511316;1586518516&q-header-list=date;host&q-url-param-list=&q-signature=****************************************

Connection: close

#### 响应

HTTP/1.1 200 OK

Content-Type: text/plain

Access-Control-Allow-Origin: *

Last-Modified: Fri, 10 Apr 2020 09:35:05 GMT

### 自定义对象的 HTTP 头部

参见 [操作步骤](https://cloud.tencent.com/document/product/436/13361#step)，添加如下自定义头部配置：

参数 值
Content-Type image/jpeg
Cache-Control no-cache
Content-Disposition attachment; filename* = UTF-8' '%E4%B8%AD%E6%96%87.jpeg
x-cos-meta-md5 1234

再次发起请求，浏览器或客户端得到的对象头部范例如下：

#### 请求

GET /exampleobject.txt HTTP/1.1

Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com

Date: Fri, 10 Apr 2020 09:35:16 GMT

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1586511316;1586518516&q-key-time=1586511316;1586518516&q-header-list=date;host&q-url-param-list=&q-signature=****************************************

Connection: close

#### 响应

HTTP/1.1 200 OK

Cache-Control: no-cache

Content-Type: image/jpeg

Content-Disposition: attachment; filename* = UTF-8' '%E4%B8%AD%E6%96%87.jpeg

x-cos-meta-md5: 1234

Access-Control-Allow-Origin: *

Last-Modified: Fri, 10 Apr 2020 09:35:05 GMT

由此可见，当使用自定义头部时，可以改变页面的响应形式。
