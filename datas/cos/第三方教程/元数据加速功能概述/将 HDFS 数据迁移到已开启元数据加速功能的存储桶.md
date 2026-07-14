<!-- source: https://cloud.tencent.com/document/product/436/75942 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:23:05+08:00 -->

# 将 HDFS 数据迁移到已开启元数据加速功能的存储桶

最近更新时间：2024-11-21 17:22:32


## 简介

元数据加速是由腾讯云对象存储（Cloud Object Storage，COS）服务提供的高性能文件系统功能。元数据加速底层采用了云 HDFS 卓越的元数据管理功能，支持用户通过文件系统语义访问对象存储服务，系统设计指标可以达到百 GB 级别带宽、10万级 QPS 以及 ms 级延迟。存储桶在开启元数据加速后，可以广泛应用于大数据、高性能计算、机器学习、AI 等场景。有关元数据加速的详细介绍，请参见 [元数据加速](https://cloud.tencent.com/document/product/436/56971)。

通过元数据加速服务，COS 提供了 Hadoop 文件系统的语义，因此利用 [Hadoop Distcp 工具](https://cloud.tencent.com/document/product/436/50272) 可以便于在对象存储 COS 与其他 Hadoop 文件系统之间进行双向的数据迁移，本文重点介绍如何通过 Hadoop Distcp 工具将本地 HDFS 中的文件迁移到 COS 元数据加速存储桶中。

## 迁移环境准备

### 迁移工具准备

1. 下载下表中的 jar 包工具，并且放置到迁移集群提交机的本地目录下，例如 /data01/jars。

腾讯云 EMR 环境

自建 Hadoop/CDH 等环境

**安装说明：**

jar 包文件名 说明 下载地址
cos-distcp COSDistCp 相关包，拷贝数据到 COSN。注意根据 Hadoop 版本选择不同的 jar 包 请参见 [COSDistCp 工具](https://cloud.tencent.com/document/product/436/50272)
chdfs_hadoop_plugin_network OFS 插件，建议选择最新稳定版本下载[点击下载](https://github.com/tencentyun/chdfs-hadoop-plugin/tree/master/jar)

#### **软件依赖**

Hadoop-2.6.0及以上版本、Hadoop-COS 插件8.1.5及以上版本，同时 cos_api-bundle 插件版本与 Hadoop-COS 版本对应，详情请参见 [COSN github releases](https://github.com/tencentyun/hadoop-cos/releases)确认。

#### **安装说明**

在 Hadoop 环境下，安装以下插件：

jar 包文件名 说明 下载地址
cos-distcp COSDistCp 相关包，拷贝数据到 COSN。注意根据 Hadoop 版本选择不同的 jar 包 请参见 [COSDistCp 工具](https://cloud.tencent.com/document/product/436/50272)
chdfs_hadoop_plugin_network OFS 插件，建议选择最新稳定版本下载[点击下载](https://github.com/tencentyun/chdfs-hadoop-plugin/tree/master/jar)
Hadoop-COS Version >= 8.1.5 请参见 [Hadoop-COS 工具](https://cloud.tencent.com/document/product/436/6884#.E4.B8.8B.E8.BD.BD.E4.B8.8E.E5.AE.89.E8.A3.85)
cos_api-bundle 版本需与 Hadoop-COS 对应[点击下载](https://github.com/tencentyun/hadoop-cos/releases)

**注意：**

Hadoop-cos 自8.1.5版本开始支持 `cosn://bucketname-appid/` 方式访问元数据加速桶。

元数据加速功能只能在创建存储桶时开启，开启后不支持关闭，请结合您的业务情况慎重考虑是否开启，同时注意旧版本的 Hadoop-cos 包不能正常访问已开启元数据加速功能的存储桶。

2. 创建元数据加速存储桶，配置元数据加速桶 HDFS 协议，并为迁移集群所在的节点开启读写访问权限。详细步骤请参见 [使用 HDFS 协议访问已开启元数据加速的存储桶](https://cloud.tencent.com/document/product/436/68700) 中的“创建存储桶并配置 HDFS 协议”章节。

3. 修改迁移集群的配置文件 `core-site.xml` ，修改内容请参见 [使用 HDFS 协议访问已开启元数据加速的存储桶](https://cloud.tencent.com/document/product/436/68700) 中的“配置计算集群访问 COS”章节，修改完成后下发配置到所有的节点上。如果只是迁移数据，则不用重启大数据组件。

4. 验证迁移集群可以通过内网访问元数据加速存储桶，详细步骤请参见 [使用 HDFS 协议访问已开启元数据加速的存储桶](https://cloud.tencent.com/document/product/436/68700) 中的“验证环境”章节。通过迁移集群提交验证是否能成功访问元数据加速存储桶。

## 存量迁移

### 步骤一：确定迁移目录

一般情况下，迁移数据会先从 HDFS 存储数据开始迁移，会选定源 HDFS 集群待迁移的目录，目标段保持和源路径相同，如下所示：

假设需要将 HDFS 路径 `hdfs:///data/user/target` 迁移到 `cosn://{bucketname-appid}/data/user/target`。

为了保证迁移过程中，源端目录的文件不发生改变，会采用 HDFS 的快照功能，先给待迁移的目录打上快照，以当前日期作为快照文件名。

hdfs dfsadmin -disallowSnapshot hdfs:///data/user/

hdfs dfsadmin -allowSnapshot hdfs:///data/user/target

hdfs dfs -deleteSnapshot hdfs:///data/user/target yymmdd(例如: 20241112)

hdfs dfs -createSnapshot hdfs:///data/user/target yymmdd(例如: 20241112)

参考成功示例：

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/3758c1928321835d4562bbc648e53eb4.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/3758c1928321835d4562bbc648e53eb4.png)

如果不想做快照，可直接以源端 target 文件进行迁移。

### 步骤二：使用 COSDistCp 迁移

启动 COSDistCp 任务，将文件从源 HDFS 复制到目标 COS 桶上。

COSDistCp 为 MapReduce 任务，MapReduce 任务打印日志中会提示 MR 任务执行成功与否。如果失败可查看 YARN 页面，将日志或异常信息提供到 COS 进行排查。通过 COSDistCp 工具执行迁移任务分为如下步骤：

1. 创建临时目录。

hadoop fs -libjars /data01/jars/chdfs_hadoop_plugin_network-2.8.jar -mkdir cosn://bucket-appid/distcp-tmp

2. 运行 COSDistCp 任务。

nohup hadoop jar /data01/jars/cos-distcp-1.10-2.8.5.jar -libjars /data01/jars/chdfs_hadoop_plugin_network-2.8.jar --src=hdfs:///data/user/target/.snapshot/{当前日期} --dest=cosn://{bucket-appid}/data/user/target --temp=cosn://bucket-appid/distcp-tmp/ --preserveStatus=ugpt --skipMode=length-checksum --checkMode=length-checksum --cosChecksumType=CRC32C --taskNumber 6 --workerNumber 32 --bandWidth 200 >> ./distcp.log &

参数说明如下，您可根据实际情况进行调整：

--taskNumber=VALUE 指定拷贝进程数，示例：--taskNumber=10。

--workerNumber=VALUE 指定拷贝线程数，COSDistCp 在每个拷贝进程中创建该参数大小的拷贝线程池。示例：--workerNumber=4。

--bandWidth 限制读取每个迁移文件的带宽，单位为：MB/s，默认-1，不限制读取带宽。示例：--bandWidth=10。

--cosChecksumType=CRC32C, 默认采用 CRC32C，但是需要 HDFS 集群支持 COMPOSITE_CRC32 校验，依赖 Hadoop 版本3.1.1+，如果 HDFS 版本低于3.1.1，此参数需要改为--cosChecksumType=CRC64。

**注意：**

COSDistCp 迁移的总带宽限制计算公式为：taskNumber x workerNumber x bandWidth，您可以将 workerNumber 设置为 1，通过参数 taskNumber 控制迁移并发数，以及参数 bandWidth 控制单个并发的带宽。

在拷贝任务结束时，任务日志会输出文件拷贝的统计信息，相关计数器如下：

其中 FILES_FAILED 代表失败的个数，若无 FILES_FAILED 统计项则说明全部迁移成功。

CosDistCp Counters

 BYTES_EXPECTED=10198247

 BYTES_SKIPPED=10196880

 FILES_COPIED=1

 FILES_EXPECTED=7

 FILES_FAILED=1

 FILES_SKIPPED=5

具体输出结果统计项说明如下：

统计项 说明
BYTES_EXPECTED 根据源目录统计的需拷贝的文件总大小，单位：字节
FILES_EXPECTED 根据源目录统计的需拷贝文件数，包含目录文件
BYTES_SKIPPED 长度或校验和值相等，不拷贝的文件总大小，单位：字节
FILES_SKIPPED 长度或校验和值相等，不拷贝的源文件数
FILES_COPIED 拷贝成功的源文件数
FILES_FAILED 拷贝失败的源文件数
FOLDERS_COPIED 拷贝成功的目录数
FOLDERS_SKIPPED 跳过的目录数

3. 失败文件重迁移。

COSDistCp 工具不但可以解决大部分文件的迁移效率问题，同时也可以采用 `--delete` 参数支持 HDFS 和 COS 数据的完全一致。使用 `--delete` 参数时，需要携带 `--deleteOutput=/xxx(自定义)` 参数，但不可以携带 `--diffMode`参数。

nohup hadoop jar /data01/jars/cos-distcp-1.10-2.8.5.jar -libjars /data01/jars/chdfs_hadoop_plugin_network-2.8.jar --src=--src=hdfs:///data/user/target/.snapshot/{当前日期} --dest=cosn://{bucket-appid}/data/user/target --temp=cosn://bucket-appid/distcp-tmp/ --preserveStatus=ugpt --skipMode=length-checksum --checkMode=length-checksum --cosChecksumType=CRC32C --taskNumber 6 --workerNumber 32 --bandWidth 200 --delete --deleteOutput=/dele-xx >> ./distcp.log &

运行完成后，会将 HDFS 和 COS 的差异数据移动到 `trash` 目录下，并且在 `/xxx/failed` 目录下生成移动文件清单。删除 `trash` 目录下的数据可以采用 `hadoop fs -rm URL` 或者`hadoop fs -rmr URL`。

## 增量迁移

如果每一轮迁移过后，还存在更新的增量数据需要迁移，只需要重复执行全量迁移中的步骤即可，直到数据均已完成迁移。
