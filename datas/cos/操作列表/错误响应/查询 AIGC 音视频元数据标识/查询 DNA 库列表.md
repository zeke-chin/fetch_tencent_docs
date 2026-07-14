<!-- source: https://cloud.tencent.com/document/product/436/115313 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:49:42+08:00 -->

# 查询 DNA 库列表

最近更新时间：2025-08-29 15:03:52


## 功能描述

获取 DNA 库列表

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加 `ci:DescribeMediaDnaDbs`。数据万象支持的所有操作接口请参见 [CI action](https://cloud.tencent.com/document/product/598/98114)。

## 服务开通

使用该功能需提前 [绑定存储桶](https://cloud.tencent.com/document/product/460/46483)，开通数据万象服务。

使用该功能需提前通过 [控制台](https://cloud.tencent.com/document/product/460/87745) 或 [接口](https://cloud.tencent.com/document/product/460/72823) 开通媒体处理服务 。

**注意：**

数据万象绑定后，如果您手动对存储桶进行数据万象的解绑操作，将无法继续使用该功能。

## 使用限制

使用该接口时，请先确认相关限制条件。详情请参见 [使用限制](https://cloud.tencent.com/document/product/460/36620#Media-processing)。

## 请求

#### 请求示例

GET /dnadb?ids=<ids>&pageNumber=<pageNumber>&pageSize=<pageSize> HTTP/1.1

Host: <BucketName-APPID>.ci.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

**说明：**

Authorization: Auth String，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求参数

参数的具体内容如下：

参数名称 描述 类型 是否必选
ids DNA库 ID，支持以`,`符号分割字符串，最多填20个 String 否
pageNumber 第几页，默认值1 Int 否
pageSize 每页个数，默认值10, 最大值100 Int 否

#### 请求体

该请求无请求体。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

<Response>

 <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=</RequestId>

 <TotalCount>2</TotalCount>

 <PageNumber>1</PageNumber>

 <PageSize>10</PageSize>

 <DNADbConfig>

 <BucketId>test-1234567890</BucketId>

 <Region>ap-chongqing</Region>

 <DNADbId>xxx1</DNADbId>

 <DNADbName>测试1</DNADbName>

 <Capacity>10000</Capacity>

 <Description>这是测试库1</Description>

 <CreateTime>2023-06-05T11:35:24+0800</CreateTime>

 <UpdateTime>2023-06-30T16:15:20+0800</UpdateTime>

 </DNADbConfig>

 <DNADbConfig>

 <BucketId>test-1234567890</BucketId>

 <Region>ap-chongqing</Region>

 <DNADbId>xxx2</DNADbId>

 <DNADbName>测试2</DNADbName>

 <Capacity>10000</Capacity>

 <Description>这是测试库2</Description>

 <CreateTime>2023-06-05T11:35:24+0800</CreateTime>

 <UpdateTime>2023-06-25T17:21:20+0800</UpdateTime>

 </DNADbConfig>

 <NonExistIDs>A</NonExistIDs>

 <NonExistIDs>B</NonExistIDs>

 <NonExistIDs>C</NonExistIDs>

</Response>

具体的数据内容如下：

节点名称（关键字）父节点 描述 类型
Response 无 保存结果的容器 Container

Container 节点 Response 的内容：

节点名称（关键字）父节点 描述 类型
RequestId Response 请求的唯一 ID String
TotalCount Response 库总数 Int
PageNumber Response 当前页数，同请求中的 pageNumber Int
PageSize Response 每页个数，同请求中的 pageSize Int
DNADbConfig Response 库的详细信息 Container 数组
NonExistIDs Response 查询的 ID 中不存在的库，所有 ID 都存在时不返回 String 数组

Container 节点 DNADbConfig 的内容：

节点名称（关键字）父节点 描述 类型
BucketId Response.DNADbConfig 存储桶 ID String
Region Response.DNADbConfig 存储桶所在园区 String
DNADbId Response.DNADbConfig DNA 库 ID String
DNADbName Response.DNADbConfig DNA 库名称 String
Capacity Response.DNADbConfig DNA 库容量 Int
Description Response.DNADbConfig DNA 库描述 String
UpdateTime Response.DNADbConfig DNA 更新时间 String
CreateTime Response.DNADbConfig DNA 创建时间 String

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

GET /dnadb?ids=xxx1,xxx2,A,B,C HTTP/1.1

Accept: */*

Authorization: q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=****************************************

Host: test-1234567890.ci.ap-chongqing.myqcloud.com

#### 响应

HTTP/1.1 200 OK

Content-Type: application/xml

Content-Length: 666

Connection: keep-alive

Date: Mon, 28 Jun 2022 15:23:12 GMT

Server: tencent-ci

x-ci-request-id: NjMxMDJhYTNfMThhYTk0MGFfYmU1OV8zZjc=

<Response>

 <RequestId>NjMxMDJhYTNfMThhYTk0MGFfYmU1OV8zZjc=</RequestId>

 <TotalCount>2</TotalCount>

 <PageNumber>1</PageNumber>

 <PageSize>10</PageSize>

 <DNADbConfig>

 <BucketId>test-1234567890</BucketId>

 <Region>ap-chongqing</Region>

 <DNADbId>xxx1</DNADbId>

 <DNADbName>测试1</DNADbName>

 <Capacity>10000</Capacity>

 <Description>这是测试库1</Description>

 <CreateTime>2023-06-05T11:35:24+0800</CreateTime>

 <UpdateTime>2023-06-30T16:15:20+0800</UpdateTime>

 </DNADbConfig>

 <DNADbConfig>

 <BucketId>test-1234567890</BucketId>

 <Region>ap-chongqing</Region>

 <DNADbId>xxx2</DNADbId>

 <DNADbName>测试2</DNADbName>

 <Capacity>10000</Capacity>

 <Description>这是测试库2</Description>

 <CreateTime>2023-06-05T11:35:24+0800</CreateTime>

 <UpdateTime>2023-06-25T17:21:20+0800</UpdateTime>

 </DNADbConfig>

 <NonExistIDs>A</NonExistIDs>

 <NonExistIDs>B</NonExistIDs>

 <NonExistIDs>C</NonExistIDs>

</Response>
