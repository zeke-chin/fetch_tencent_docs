<!-- source: https://cloud.tencent.com/document/product/436/111493 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:22:41+08:00 -->

# 使用 Hadoop Shell 访问 COS 元数据加速存储桶

最近更新时间：2026-03-24 16:49:22


## 操作场景

对于一些比较简单的文件操作，可以直接通过命令行的方式来完成。本文指导您如何通过 Hadoop Shell，以命令行的方式来访问元数据加速桶。

## 前提条件

确保已经开通元数据加速服务，并且进行了正确的环境部署和 HDFS 协议配置。具体部署和配置，详情请参见 [使用 HDFS 协议访问已开启元数据加速的存储桶](https://cloud.tencent.com/document/product/436/68700)。

登录任意一台完成了环境部署和 HDFS 协议配置的服务器，进入命令行界面。

## 支持的操作

1. 详细的 Hadoop 命令行文档，请参见 [Hadoop Shell 命令](https://hadoop.apache.org/docs/r1.0.4/cn/hdfs_shell.html)。

2. 下面列举一些常用的文件操作。

### **遍历目录(list)**

hadoop fs -ls cosn://examplebucket-1250000000/

### **创建目录(mkdir)**

hadoop fs -mkdir -p cosn://examplebucket-1250000000/test_01/xxx

### 上传文件

hadoop fs -put ./len1m.txt cosn://examplebucket-1250000000/test_01/xxx/len1m_1.txt

### 下载文件

hadoop fs -get cosn://examplebucket-1250000000/test_01/xxx/len1m_1.txt ./len1m_1.txt

### 删除文件

**注意：**

文件被删除后，其对应的数据将无法再被访问。

hadoop fs -rm cosn://examplebucket-1250000000/test_01/xxx/len1m_1.txt

### 删除目录

**注意：**

目录被删除后，将无法再被访问。

hadoop fs -rm -r cosn://examplebucket-1250000000/test_01/xxx

### 目录统计(du)

hadoop fs -du cosn://examplebucket-1250000000/test_01

### 文件校验和

hadoop fs -checksum cosn://examplebucket-1250000000/test_01/xxx/len1m_1.txt
