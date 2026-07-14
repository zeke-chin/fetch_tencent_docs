<!-- source: https://cloud.tencent.com/document/product/436/63676 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:13:18+08:00 -->

# 获取预签名 URL - signurl

最近更新时间：2026-02-06 10:27:11


## 命令格式

./coscli signurl cos://<bucket-name>/<key> [flag]

signurl 命令包含以下参数：

参数格式 参数用途 示例
cos://<bucket-name>/<key>指定需要存储桶中的对象。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag。使用桶别名访问：cos://example-alias/test.txt

使用桶名称访问：cos://examplebucket-1250000000/test.txt

signurl 命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法
-t--time 设置 URL 过期时间（默认1000s）
无--simple-output 启用简易输出模式，默认值为 false。当设置为 true 时，仅输出签名 URL，简化返回结果。

**说明：**

关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。

## 操作示例

### 获取 bucket1 桶内 picture.jpg 的预签名 URL

./coscli signurl cos://bucket1/picture.jpg

返回的结果示例如下：

INFO[2026-02-04 11:36:10] Signed URL:

INFO[2026-02-04 11:36:10] https://bucket1-1234124.cos.ap-guangzhou.myqcloud.com/picture.jpg?q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1770176170%3B1770186170&q-key-time=1770176170%3B1770186170&q-header-list=host&q-url-param-list=&q-signature=****************************************

### 获取 bucket2 桶内 picture.jpg 的预签名 URL，并设置 URL 的过期时间为1314秒

./coscli signurl cos://bucket2/picture.jpg --time 1314

返回的结果示例如下：

INFO[2026-02-04 11:36:10] Signed URL:

INFO[2026-02-04 11:36:10] https://bucket2-1234124.cos.ap-guangzhou.myqcloud.com/picture.jpg?q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1770176170%3B1770186170&q-key-time=1770176170%3B1770186170&q-header-list=host&q-url-param-list=&q-signature=****************************************

### 获取 bucket3 桶内 picture.jpg 的预签名 URL，并使用简易模式输出

./coscli signurl cos://bucket3/picture.jpg --simple-output

返回的结果示例如下：

https://bucket3-1234124.cos.ap-guangzhou.myqcloud.com/picture.jpg?q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1770176267%3B1770186267&q-key-time=1770176267%3B1770186267&q-header-list=host&q-url-param-list=&q-signature=****************************************
