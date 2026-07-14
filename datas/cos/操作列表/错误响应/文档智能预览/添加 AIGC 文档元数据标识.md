<!-- source: https://cloud.tencent.com/document/product/436/124904 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:55:06+08:00 -->

# 添加 AIGC 文档元数据标识

最近更新时间：2025-11-11 18:11:12


## 功能描述

腾讯云数据万象支持通过异步任务的方式，为文档添加 AIGC 元数据标识。

**注意：**

任务记录保留一个月，请及时保存任务记录。建议配置回调进行任务结果查询。

## 授权说明

通过子账号使用时，需要在 [授权策略](https://cloud.tencent.com/document/product/460/104297) 的 action 中添加 `ci:CreateDocProcessJobs` 权限。数据万象支持的所有操作接口请参见 [action](https://cloud.tencent.com/document/product/598/98114)。

子账号使用异步处理接口时，需要授予 `cam:PassRole` 权限，异步处理接口会通过 CAM 的“角色”进行 COS 的资源读写操作，PassRole 权限用于传递角色， 具体请参见 [访问管理 > 写操作 > PassRole 接口](https://cloud.tencent.com/document/product/598/69872#.E5.86.99.E6.93.8D.E4.BD.9C)。

## 服务开通

使用该功能需将 [存储桶绑定数据万象](https://cloud.tencent.com/document/product/460/97479)。

使用该功能需提前通过 [控制台](https://cloud.tencent.com/document/product/460/46499) 或 [接口](https://cloud.tencent.com/document/product/460/103608) 开通文档处理服务。

**注意：**

数据万象绑定后，如果您手动对存储桶进行数据万象的解绑操作，将无法继续使用该功能。

## 使用限制

文档格式限制：pdf、md、xmind、docx、pptx、xlsx、dotx、potx、xltx。

文档大小限制：不超过50MB。

接口请求默认并发数：100。

同时可处理的任务并发数：10。

地域限制：支持中国大陆公有云地域。

## 费用说明

该功能为付费服务，产生的费用将由数据万象收取，详细计费说明请参见 [文档处理费用](https://cloud.tencent.com/document/product/460/58121)。

## 请求

#### 请求示例

POST /doc_jobs HTTP/1.1

Host: <BucketName-APPID>.ci.<Region>.myqcloud.com

Date: <GMT Date>

Authorization: <Auth String>

Content-Length: <length>

Content-Type: application/xml

<body>

**说明：**

Authorization: Auth String，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有如下请求体。

<Request>

 <Tag>DocAIGCMetadata</Tag>

 <Input>

 <Object>contract.pdf</Object>

 </Input>

 <Operation>

 <Output>

 <Region>ap-chongqing</Region>

 <Bucket>output-bucket-125000000</Bucket>

 <Object>processed/contract_v2.pdf</Object>

 </Output>

 <DocAIGCMetadata>

 <AIGCMetadata>

 <Label>1</Label>

 <ContentProducer></ContentProducer>

 <ProduceID></ProduceID>

 <ReservedCode1></ReservedCode1>

 <ContentPropagator></ContentPropagator>

 <PropagateID></PropagateID>

 <ReservedCode2></ReservedCode2>

 </AIGCMetadata>

 <DocAIGCMetadata/>

 </Operation>

</Request>

具体的数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
Request 无 保存请求的容器 Container 是

Container 类型 Request 的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
Tag Request 创建任务的 Tag，目前仅支持：DocAIGCMetadata String 是
Input Request 待操作的文件对象 Container 是
Operation Request 操作规则 Container 是

Container 类型 Input 的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
Object Request.Input 输入文件所在存储桶中的文件路径 String 是

Container 类型 Operation 的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
DocAIGCMetadata Request.Operation 当 Tag 为 DocAIGCMetadata 时有效，用于指定文档 AIGC 标识内容的参数 Container 是
Output Request.Operation 结果输出地址 Container 是

Container 类型 DocAIGCMetadata 的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
AIGCMetadata Request.Operation.DocAIGCMetadata 包含文档 AIGC 标识内容的具体参数 Container 是

Container 类型 AIGCMetadata 的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
Label Request.Operation.DocAIGCMetadata.AIGCMetadata 生成合成标签要素，用于表示文档属于、可能、疑似为人工智能生成合成的属性信息

长度限制：2048个 UTF-8字符数

字符限制：GB18030—2022（ASCII）中码位为0x21 - 0x7E 的字符，即包含阿拉伯数字、大小写英文及可打印字符 String 是
ContentProducer Request.Operation.DocAIGCMetadata.AIGCMetadata 生成合成服务提供者要素，内容为文档生成合成服务提供者的名称或编码

长度限制：2048个 UTF-8字符数

字符限制：GB18030—2022（ASCII）中码位为0x21 - 0x7E 的字符，即包含阿拉伯数字、大小写英文及可打印字符 String 否
ProduceID Request.Operation.DocAIGCMetadata.AIGCMetadata 内容制作编号要素，内容为文档生成合成服务提供者对该内容的唯一编号

支持通配符：

${InputName}: COS 源文件名，不带后缀，不带路径

${InputNameAndExt}: COS 源文件名，带后缀，不带路径

${JobId}: 添加 AIGC 元数据信息的执行任务 id

${InputPath}: COS源文件路径，不包含文件名

长度限制：2048个 UTF-8字符数

字符限制：GB18030—2022（ASCII）中码位为0x21 - 0x7E 的字符，即包含阿拉伯数字、大小写英文及可打印字符 String 否
ReservedCode1 Request.Operation.DocAIGCMetadata.AIGCMetadata 预留字段1，内容为用户自主开展安全防护，保护内容、标识完整性的信息。需经过 base64编码后传入

长度限制（base64编码前）：2048个 UTF-8字符数

字符限制（base64编码前）：GB18030—2022（ASCII）中码位为0x21 - 0x7E 的字符，即包含阿拉伯数字、大小写英文及可打印字符 String 否
ContentPropagator Request.Operation.DocAIGCMetadata.AIGCMetadata 内容传播服务提供者要素，内容为文档传播服务提供者的名称或编码

长度限制：2048个 UTF-8字符数

字符限制：GB18030—2022（ASCII）中码位为0x21 - 0x7E 的字符，即包含阿拉伯数字、大小写英文及可打印字符 String 否
PropagateID Request.Operation.DocAIGCMetadata.AIGCMetadata 内容传播编号要素，内容为文档传播服务提供者对该文档的唯一编号

支持通配符：

${InputName}: COS 源文件名，不带后缀，不带路径

${InputNameAndExt}: COS 源文件名，带后缀，不带路径

${JobId}: 添加 AIGC 元数据信息的执行任务 id

${InputPath}: COS 源文件路径，不包含文件名

长度限制：2048个 UTF-8字符数

字符限制：GB18030—2022（ASCII）中码位为0x21 - 0x7E 的字符，即包含阿拉伯数字、大小写英文及可打印字符 String 否
ReservedCode2 Request.Operation.DocAIGCMetadata.AIGCMetadata 预留字段2，内容为用户自主开展安全防护，保护内容、标识完整性的信息。需经过 base64编码后传入

长度限制（base64编码前）：2048个 UTF-8字符数

字符限制（base64编码前）：GB18030—2022（ASCII）中码位为0x21 - 0x7E 的字符，即包含阿拉伯数字、大小写英文及可打印字符 String 否

Container 类型 Output 的具体数据描述如下：

节点名称（关键字）父节点 描述 类型 是否必选
Region Request.Operation.Output 存储桶的地域 String 是
Bucket Request.Operation.Output 存储结果的存储桶 String 是
Object Request.Operation.Output 输出文件路径。

**非表格文件输出文件名需包含 ${Number} 或 ${Page} 参数。**多个输出文件，${Number} 表示序号从1开始，${Page} 表示序号与预览页码一致。

${Number} 表示多个输出文件，序号从1开始，例如输入 abc_${Number}.jpg，预览某文件5 - 6页，则输出文件名为 abc_1.jpg，abc_2.jpg

${Page} 表示多个输出文件，序号与预览页码一致，例如输入 abc_${Page}.jpg，预览某文件5-6页，则输出文件名为 abc_5.jpg，abc_6.jpg

**表格文件输出路径需包含 ${SheetID} 占位符，输出文件名必须包含 ${Number} 参数。**

例如 `/${SheetID}/abc_${Number}.jpg`，先根据 Excel 转换的表格数，生成对应数量的文件夹，再在对应的文件夹下，生成对应数量的图片文件 String 是

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

<Response>

 <JobsDetail>

 <Code>Success</Code>

 <CreationTime>2025-08-27T15:23:10+0800</CreationTime>

 <EndTime>-</EndTime>

 <Input>

 <Region>ap-chongqing</Region>

 <BucketId>bucket-125000000</BucketId>

 <Object>contract.pdf</Object>

 </Input>

 <JobId>j8d1218rughoehnoewij53ba9c6f</JobId>

 <Message/>

 <Operation>

 <DocAIGCMetadata>

 <AIGCMetadata>

 <Label>1</Label>

 <ContentProducer></ContentProducer>

 <ProduceID></ProduceID>

 <ReservedCode1></ReservedCode1>

 <ContentPropagator></ContentPropagator>

 <PropagateID></PropagateID>

 <ReservedCode2></ReservedCode2>

 </AIGCMetadata>

 </DocAIGCMetadata>

 <Output>

 <Region>ap-chongqing</Region>

 <Bucket>output-bucket-125000000</Bucket>

 <Object>processed/contract_v2.pdf</Object>

 </Output>

 </Operation>

 <State></State>

 <Tag>DocAIGCMetadata</Tag>

 </JobsDetail>

</Response>

具体的数据内容如下：

节点名称（关键字）父节点 描述 类型
Response 无 保存结果的容器 Container

Container 节点 Response 的内容：

节点名称（关键字）父节点 描述 类型
JobsDetail Response 任务的详细信息 Container

Container 节点 JobsDetail 的内容：

节点名称（关键字）父节点 描述 类型
Code Response.JobsDetail 错误码，只有 State 为 Failed 时生效 String
Message Response.JobsDetail 错误描述，只有 State 为 Failed 时生效 String
JobId Response.JobsDetail 新创建任务的 ID String
Tag Response.JobsDetail 新创建任务的 Tag：DocAIGCMetadata String
State Response.JobsDetail 任务状态

Submitted：已提交，待执行

Running：执行中

Success：执行成功

Failed：执行失败

Pause：任务暂停，当暂停队列时，待执行的任务会变为暂停状态

Cancel：任务被取消执行 String
CreationTime Response.JobsDetail 任务的创建时间 String
QueueId Response.JobsDetail 任务所属的队列 ID String
Input Response.JobsDetail 该任务的输入文件路径 Container
Operation Response.JobsDetail 该任务的规则 Container

Container 节点 Input 的内容：

节点名称（关键字）父节点 描述 类型 是否必选
Region Request.Operation.Output 存储桶的地域 String 是
BucketId Request.Operation.Output 输入文件所在的存储桶 String 是
Object Request.Operation.Output 存储桶中的文件路径 String 是

Container 节点 Operation 的内容：

节点名称（关键字）父节点 描述 类型
DocAIGCMetadata Response.JobsDetail.Operation 文档 AIGCMetadata 添加任务参数 Container
Output Response.JobsDetail.Operation 文件的输出地址 Container

Container 节点 DocAIGCMetadata 的内容：同上面请求中的 Request.Operation.DocAIGCMetadata 节点。

Container 节点 Output 的内容：同上面请求中的 Request.Operation.Output 节点。

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

POST /doc_jobs HTTP/1.1

Connection: keep-alive

Accept-Encoding: gzip, deflate

Accept: */*

User-Agent: cos-python-sdk-v5.3.2

Host: examplebucket-1250000000.ci.ap-chongqing.myqcloud.com

Content-Type: application/xml

Content-Length: 546

Authorization: Authorization

<?xml version="1.0" encoding="UTF-8" ?>

<Request>

 <Input>

 <Object>1.doc</Object>

 </Input>

 <Operation>

 <Output>

 <Region>ap-chongqing</Region>

 <Object>big/test-${Number}</Object>

 <Bucket>examplebucket-1250000000</Bucket>

 </Output>

 <DocAIGCMetadata>

 <AIGCMetadata>

 <Label>label</Label>

 <ContentProducer>testProducer</ContentProducer>

 <ProduceID>testProduceId</ProduceID>

 <ReservedCode1>dGVzdA==</ReservedCode1>

 <ContentPropagator>testPropagator</ContentPropagator>

 <PropagateID>testPropagatorId</PropagateID>

 <ReservedCode2>dGVzdA==</ReservedCode2>

 </AIGCMetadata>

 </DocAIGCMetadata>

 </Operation>

 <Tag>DocAIGCMetadata</Tag>

</Request>

#### 响应

HTTP/1.1 200 OK

Date: Mon, 27 Jul 2020 07:20:08 GMT

Content-Type: application/xml

Content-Length: 863

Connection: keep-alive

Server: tencent-ci

x-ci-request-id: NWYxZTgwMjhfYzc2OTQzNjRfMzUx****

<?xml version="1.0" encoding="utf-8"?>

<Response>

 <JobsDetail>

 <Code>Success</Code>

 <CreationTime>2020-07-27T15:20:08+0800</CreationTime>

 <EndTime>-</EndTime>

 <Input>

 <Region>ap-chongqing</Region>

 <BucketId>examplebucket-1250000000</Bucket>

 <Object>processed/contract_v2.pdf</Object>

 </Input>

 <JobId>d99b3127ecfd911eab5e60dedb7c395dd</JobId>

 <Message/>

 <Operation>

 <DocAIGCMetadata>

 <AIGCMetadata>

 <Label>label</Label>

 <ContentProducer>testProducer</ContentProducer>

 <ProduceID>testProduceId</ProduceID>

 <ReservedCode1>dGVzdA==</ReservedCode1>

 <ContentPropagator>testPropagator</ContentPropagator>

 <PropagateID>testPropagatorId</PropagateID>

 <ReservedCode2>dGVzdA==</ReservedCode2>

 </AIGCMetadata>

 </DocAIGCMetadata>

 <Output>

 <Bucket>examplebucket-1250000000</Bucket>

 <Object>big/test-${Number}</Object>

 <Region>ap-chongqing</Region>

 </Output>

 </Operation>

 <QueueId>p532fdead78444e649e1a4467c1cd19d3</QueueId>

 <State>Submitted</State>

 <Tag>DocAIGCMetadata</Tag>

 </JobsDetail>

</Response>
