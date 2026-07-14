<!-- source: https://cloud.tencent.com/document/product/436/40603 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:16:19+08:00 -->

# Hadoop 文件系统与 COS 之间的数据迁移

最近更新时间：2024-08-07 18:00:51


## 简介

Hadoop Distcp（Distributed copy）主要是用于 Hadoop 文件系统内部或之间进行大规模数据复制的工具，它基于 Map/Reduce 实现文件分发、错误处理以及最终的报告生成。由于利用了 Map/Reduce 的并行处理能力，每个 Map 任务负责完成源路径中部分文件的复制，因此它可以充分利用集群资源来快速完成集群或 Hadoop 文件系统之间的大规模数据迁移。

由于 Hadoop-COS 实现了 Hadoop 文件系统的语义，因此利用 Hadoop Distcp 工具可以方便地在对象存储（Cloud Object Storage，COS）与其他 Hadoop 文件系统之间进行双向的数据迁移，本文就以 HDFS 为例，介绍 Hadoop 文件系统与 COS 之间利用 Hadoop Distcp 工具完成数据迁移的方式。

## 前提条件

1. Hadoop 集群中已经安装 [Hadoop-COS](https://cloud.tencent.com/document/product/436/6884#.E4.B8.8B.E8.BD.BD.E4.B8.8E.E5.AE.89.E8.A3.85) 插件，并且正确配置了 COS 的访问密钥等。可使用如下 Hadoop 命令检查 COS 访问是否正常：

hadoop fs -ls cosn://examplebucket-1250000000/

如果能够正确地列出 COS Bucket 中的文件列表，则表示 Hadoop-COS 安装和配置正确，可以进行以下实践步骤。

2. COS 的访问账户必须要具备读写 COS 存储桶中目标路径的权限。

**注意：**

您可以按需授予子账号读写 COS 存储桶内资源的权限，建议按照 [最小权限原则](https://cloud.tencent.com/document/product/436/38618) 和 [子用户授权指南](https://cloud.tencent.com/document/product/598/36256) 进行授权，以下几种是常见预设策略：

[QcloudCOSDataFullControl](https://console.cloud.tencent.com/cam/policy/detail/5294998&QcloudCOSDataFullControl&2)：数据全读写权限，包含读、写、列出文件列表以及删除操作，建议谨慎授予。

[QcloudCOSDataReadOnly](https://console.cloud.tencent.com/cam/policy/detail/5295051&QcloudCOSDataReadOnly&2)：数据只读权限。

[QcloudCOSDataWriteOnly](https://console.cloud.tencent.com/cam/policy/detail/5295044&QcloudCOSDataWriteOnly&2)：数据只写权限。

如果需要使用自定义监控能力，需要授权腾讯云可观测平台指标上报和读取接口操作权限，请谨慎授予 [QcloudMonitorFullAccess](https://console.cloud.tencent.com/cam/policy/detail/276210&QcloudMonitorFullAccess&2) 或者按需授予 [腾讯云可观测平台接口](https://cloud.tencent.com/document/product/248/45428) 权限。

## 实践步骤

### 将 HDFS 中的数据复制到 COS 的存储桶中

通过 Hadoop Distcp 将本地 HDFS 集群中`/test`目录下的文件迁移到 COS 的 hdfs-test-1250000000 存储桶中。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/769d893f5509a810955d9cf7c7970646.jpeg)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/769d893f5509a810955d9cf7c7970646.jpeg)

1. 执行如下命令启动迁移：

hadoop distcp hdfs://10.0.0.3:9000/test cosn://hdfs-test-1250000000/

Hadoop Distcp 会启动 MapReduce 作业来执行文件复制任务，完成后会输出简单报表信息，如下图所示：

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/53651f051ce3bd6965cc21a8fe79acce.jpeg)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/53651f051ce3bd6965cc21a8fe79acce.jpeg)

2. 执行`hadoop fs -ls -R cosn://hdfs-test-1250000000/`命令可以列出刚才已迁移到存储桶 hdfs-test-1250000000 的目录和文件。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/fc16a6993f4ec00455a35f7db7bc315e.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/fc16a6993f4ec00455a35f7db7bc315e.png)

### 将 COS 中存储桶的文件复制到本地 HDFS 集群

Hadoop Distcp 是一个支持不同集群和文件系统之间复制数据的工具，因此，将 COS 存储桶中的对象路径作为源路径，HDFS 的文件路径作为目标路径即可将 COS 中的数据文件复制到本地 HDFS：

hadoop distcp cosn://hdfs-test-1250000000/test hdfs://10.0.0.3:9000/

### 指定配置 Distcp 命令行参数进行 HDFS 和 COS 之间的数据迁移

**说明：**

该命令行配置支持双向操作，可支持 HDFS 数据迁移到 COS，也可以将 COS 数据迁移到 HDFS。

用户可直接配置以下命令：

hadoop distcp -Dfs.cosn.impl=org.apache.hadoop.fs.CosFileSystem -Dfs.cosn.bucket.region=ap-XXX -Dfs.cosn.userinfo.secretId=AK**XXX -Dfs.cosn.userinfo.secretKey=XXXX -libjars /home/hadoop/hadoop-cos-2.6.5-shaded.jar cosn://bucketname-appid/test/ hdfs:///test/

参数说明如下：

Dfs.cosn.impl：始终配置为 org.apache.hadoop.fs.CosFileSystem。

Dfs.cosn.bucket.region：填写存储桶所在地域，可在 COS 控制台存储桶列表中查看。

Dfs.cosn.userinfo.secretId：填写存储桶拥有者账号下的 SecretId，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中获取。

Dfs.cosn.userinfo.secretKey：填写存储桶拥有者账号下的 secretKey，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中获取。

libjars：指定 Hadoop-COS jar 包位置。Hadoop-COS jar 包可前往 [Github 仓库](https://github.com/tencentyun/hadoop-cos)下载 release 版本。

**说明：**

其他参数请参考 [Hadoop 工具](https://cloud.tencent.com/document/product/436/6884) 文档。

## Hadoop distcp 的扩展参数

Hadoop distcp 工具支持丰富的运行参数。例如，可以通过`-m`来指定最大用于并行复制的 Map 任务数目，`-bandwidth`来限制每个 map 所使用的最大带宽等。具体可参考 Apache Hadoop distcp 工具的官方文档：[DistCp Guide](https://hadoop.apache.org/docs/current/hadoop-distcp/DistCp.html)。

## 常见问题

### **hadoop distcp**出现找不到或者无法加载主类的情况，如何处理？

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/10f1ad59c3f1a6b1ff088e8390dcc227.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/10f1ad59c3f1a6b1ff088e8390dcc227.png)

distcp 位于 Hadoop 的核心库中，相关的类主要包含在"hadoop-common" jar包中。检查该 jar 包完整性，若不完整需重新下载；或者使用`hadoop jar`命令参数指定目标类。
