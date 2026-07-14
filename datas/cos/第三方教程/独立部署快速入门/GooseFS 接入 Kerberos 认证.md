<!-- source: https://cloud.tencent.com/document/product/436/113333 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:24:37+08:00 -->

# GooseFS 接入 Kerberos 认证

最近更新时间：2026-03-12 17:34:22


# 概述

Kerberos 是大数据生态系统中广泛应用的统一认证服务，GooseFS 作为大数据和数据湖场景下的加速存储服务，支持集群节点和用户访问接入 Kerberos 认证服务中。本文将详细介绍如何配置 GooseFS 接入 Kerberos 认证服务以及如何使用 Hadoop Delegation Token 认证。

# GooseFS 接入 Kerberos 的认证架构

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/177ef00ebf12b5686f3dca4034d5023e.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/177ef00ebf12b5686f3dca4034d5023e.png)

## GooseFS Kerberos 认证优势

与 HDFS 接入 Kerberos 的认证架构和流程基本一致，在 HDFS 上启用了 Kerberos 认证流程的应用可以很容易地迁移到 GooseFS。

支持 Hadoop 的 Delegation Token 认证机制，因此可以很好地兼容 Hadoop 生态的应用作业。

## 配置 GooseFS 接入 Kerberos 认证

### 前提条件

GooseFS 1.3.0 及以上版本；

JDK 1.8 的环境，JDK 11 及以上暂时不兼容；

确保环境中已存在 Kerberos KDC 服务，并且 GooseFS 以及应用客户端能够正常访问 Kerberos KDC 服务相关端口。

### 在 Kerberos KDC 中创建 GooseFS 相关的身份信息

首先，我们需要在 Kerberos KDC 中创建 GooseFS 集群 Server 与 Client 相关的 Kerberos 身份信息，然后才能继续后续的接入配置。这里我们在 **Kerberos KDC 服务器**上借助 `kadmin.local` 交互式工具来完成创建：

**注意：**

`kadmin.local` 工具需要 root/sudo 权限执行。

$ sudo kadmin.local

如果执行成功，则进入了 kadmin 的交互式 shell 环境中：

Authenticating as principal root/admin@GOOSEFS.COM with password.

kadmin.local:

其中，`kadmin.local` 表示该交互式执行环境的命令提示符。

#### 创建 GooseFS Server / Client 相关的身份信息

如下通过一个简单测试集群以及应用场景样例来介绍整个 Kerberos 的配置过程。

1. 集群环境说明 采用单 Master 双 Worker 的 Standalone 部署架构：

Master（JobMaster）：172.16.0.1

Worker1（JobWorker1）：172.16.0.2

Worker2（JobWorker2）：172.16.0.3

Client：172.16.0.4

2. 在 `kadmin.local` 中创建 Server 和 Client 身份认证相关信息：

kadmin.local: addprinc -randkey goosefs/172.16.0.1@GOOSEFS.COM

kadmin.local: addprinc -randkey client/172.16.0.4@GOOSEFS.COM

**注意：**

此处使用 `-randkey` 选项的原因在于 GooseFS 无论 Server 还是 Client 登录均使用 `keytab` 文件认证，不使用明文密码。若身份信息需要用于 password 登录场景，则可以去掉该选项。

3. 生成导出每个身份对应的 `keytab` 文件：

kadmin.local: xst -k goosefs_172_16_0_1.keytab goosefs/172.16.0.1@GOOSEFS.COM

kadmin.local: xst -k client_172_16_0_4.keytab client/172.16.0.4@GOOSEFS.COM

### 配置 GooseFS Server/Client 接入使用 Kerberos 认证

1. 将上述导出 `keytab` 文件分发到对应的机器上，此处建议的路径是 `${GOOSEFS_HOME}/conf/`：

$ scp goosefs_172_16_0_1.keytab <username>@172.16.0.1:${GOOSEFS_HOME}/conf/

$ scp goosefs_172_16_0_1.keytab <username>@172.16.0.2:${GOOSEFS_HOME}/conf/

$ scp goosefs_172_16_0_1.keytab <username>@172.16.0.3:${GOOSEFS_HOME}/conf/

$ scp client_172_16_0_4.keytab <username>@172.16.0.4:${HOME}/.goosefs/

2. 在对应机器上，将 Server Principal KeyTab 文件的所属用户/用户组修改为 GooseFS Server 启动时所使用的用户及用户组（其目的是为了让 GooseFS 启动时有足够的权限读取）。

$ chown <GooseFS_USER>:<GOOSEFS_USERGROUP> goosefs_172_16_0_1.keytab

$ # 同时修改 Unix 访问权限位

$ chmod 0440 goosefs_172_16_0_1.keytab

3. 将 Client 的 KeyTab 的所属用户/用户组修改为发起 GooseFS 请求的客户端账户。其目的同样是为了保证 Client 有足够的权限读取该文件。

$ chown <client_user>:<client_usergroup> client_172_16_0_4.keytab

$ # 同时修改 Unix 访问权限位

$ chmod 0440 client_172_16_0_4.keytab

#### Server 和 Client 端 GooseFS 配置

1. Master/Worker Server 的 goosefs-site.properties

# Security properties

# Kerberos properties

goosefs.security.authorization.permission.enabled=true

goosefs.security.authentication.type=KERBEROS

goosefs.security.kerberos.unified.instance.name=172.16.0.1

goosefs.security.kerberos.server.principal=goosefs/172.16.0.1@GOOSEFS.COM

goosefs.security.kerberos.server.keytab.file=${GOOSEFS_HOME}/conf/goosefs_172_16_0_1.keytab

配置完成 GooseFS Server 端的认证配置后，重启整个集群以使得配置生效。

2. Client 的 goosefs-site.properties

# Security properties

# Kerberos properties

goosefs.security.authorization.permission.enabled=true

goosefs.security.authentication.type=KERBEROS

goosefs.security.kerberos.unified.instance.name=172.16.0.1

goosefs.security.kerberos.server.principal=goosefs/172.16.0.1@GOOSEFS.COM

goosefs.security.kerberos.client.principal=client/172.16.0.4@GOOSEFS.COM

goosefs.security.kerberos.client.keytab.file=${GOOSEFS_HOME}/conf/client_172_16_0_4.keytab

**注意：**

Client 端需要指定 Server 的 principal。其原因为在 Kerberos 认证体系中，KDC 需要知道当前 Client 所访问的 Service，而 GooseFS 是通过 Server 的 principal 区分 Client 当前请求的 Service。

至此，GooseFS 接入 Kerberos 的基础认证完毕，后续客户端发起的请求都将经过 Kerberos 进行身份认证。

# GooseFS 接入 Hadoop Delegation Token 认证

虽然理论上可以单独使用 Kerberos 进行身份认证，但在 Hadoop 这样的大规模分布式系统中，如果对于每个 MapReduce 作业，所有工作任务都需要请求 TGT，那么 Kerberos 的 KDC 一定会成为整个系统运行的瓶颈。如下图所示：

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/0138f380c1c87de50208aad140b55af5.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/0138f380c1c87de50208aad140b55af5.png)

如果一个 YARN 集群中 NodeManager 节点数达到几百上千个时，同时并行运行了多个 IO 密集型作业任务，那么每个执行节点在正常访问 GooseFS 中的文件所需向 Kerberos KDC 发起的凭据请求会产生巨大的 DDoS 攻击。

因此，Hadoop 社区补充设计了 Delegation Token 这种轻量级的认证机制来避免这种大规模且频繁的 Kerberos 认证请求。Kerberos 是三方认证，而 Delegation Token 在完成提交作业时的首次 Kerberos 认证以后，Master 会颁发一个 Delegation Token 给客户端缓存住，后续的每个请求都可以通过出示 Delegation Token 来认证，因此 Delegation Token 认证机制只涉及两方。具体的认证过程如下：

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/23a598f4516afa1910acfb2d68d6fab9.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/23a598f4516afa1910acfb2d68d6fab9.png)

1. 在向 YARN 提交一个计算作业的时候，YARN Client（这里面也加载 GooseFS 的Client）会通过 Kerberos 认证以后，向 GooseFS 的 Master 申请一个 Delegation Token，然后添加到 YARN 的 Resource Manager 的 Delegation Token 更新服务中；

2. 当 YARN 的 ResourceManager（实际是 ApplicationMaster ） 把分派给 NodeManager 创建的 Container 开始执行以后，每个 Task 都会携带这个 Delegation Token 去访问 GooseFS 集群。值得注意的是，由于是两方认证，因此 Client 不仅需要与 GooseFS Master 完成认证，还会隐式携带 BlockAccessToken去访问 Worker 集群，BlockAccessToken 是在每次访问一个文件时，由 Master 返回，其中会携带认证所需的身份信息和权限信息，以便于 Worker 判断是否允许 Client 读写指定的 Block；

3. YARN 的 Delegation Token 更新服务会定时更新 Token，直到 Token 的最大生命周期结束。

**注意：**不同于 Kerberos 等通用的三方认证方案，Delegation Token 认证机制一定是 Hadoop 生态所特有的，因此只能使用在 Hadoop 生态的大数据环境中，且每个 Delegation Token 都有最大生命周期限制，因此对于常驻作业（例如实时流计算作业），应当谨慎设置 Delegation Token 的最大生命周期，一般默认是 7 天。

## Delegation Token 相关的配置

如果需要使用 Delegation Token，除了需要基本的 Hadoop 的 Kerberos 和 Delegation Token 的认证环境以外，**还需要满足使用的是 GooseFS 1.4.5 及以上的版本**，**同时在**`${GOOSEFS_HOME}/conf/goosefs-site.properties`**中添加如下配置**：

# Security properties

# Kerberos properties

goosefs.security.authorization.permission.enabled=true

goosefs.security.authentication.type=KERBEROS

goosefs.security.kerberos.unified.instance.name=172.16.0.1

goosefs.security.kerberos.server.principal=goosefs/172.16.0.1@GOOSEFS.COM

goosefs.security.kerberos.client.principal=client/172.16.0.1@GOOSEFS.COM

goosefs.security.kerberos.client.keytab.file=${GOOSEFS_HOME}/conf/client_172_16_0_1.keytab

``

`# hadoop token相关配置`

`goosefs.security.authentication.block.access.token.enabled=true`

goosefs.security.delegation.token.lifetime.ms=7d

goosefs.security.delegation.token.renew.interval.ms=1d

然后，将所有配置分发到 Master/Worker 和 Client 的节点上即可启用 Hadoop Delegation Token 的认证配置。

**注意：**

在开启了 Hadoop Delegation Token 认证的环境中，如果中途关掉 Hadoop Delegation Token，由于 Master 已经将 DelegationTokenManager 的信息写入到元数据的 Checkpoint 和 Journal 中，因此需要重新 Format 集群，才能完成关闭 Hadoop Delegation Token 重启 GooseFS 集群生效。

## 使用示例

以下是一个示例集群和作业简单演示一下 Hadoop Delegation Token 生效和生命周期的测试。

测试环境：

EMR V3.6.0 环境，默认开启了 Kerberos 认证，开启高可用架构；

GooseFS-1.4.5 版本，GooseFS-1.4.5 的 client 放到了 ${HADOOP_HOME}/share/hadoop/common/lib 下面；

配置如下：

goosefs.security.authorization.permission.enabled=true

# kerberos

goosefs.security.authentication.type=KERBEROS

goosefs.security.kerberos.unified.instance.name=172.16.16.77

goosefs.security.kerberos.server.principal=hadoop/172.16.16.77@EMR-012XFAQZ

goosefs.security.kerberos.server.keytab.file=/usr/local/service/goosefs/conf/emr.keytab

goosefs.security.kerberos.client.principal=hadoop/172.16.16.77@EMR-012XFAQZ

goosefs.security.kerberos.client.keytab.file=/usr/local/service/goosefs/conf/emr.keytab

# delegation token

goosefs.security.authentication.block.access.token.enabled=true

goosefs.security.delegation.token.lifetime.ms=7d

goosefs.security.delegation.token.renew.interval.ms=1d

然后，可以执行一个 TestDFSIO：

hadoop jar /usr/local/service/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-2.8.5.jar TestDFSIO -Dfs.defaultFS=gfs://172.16.16.77:9200/ -write -nrFiles 1 -fileSize 10MB

由于 Token 的生命周期和刷新周期都是默认的，且在整个作业的运行周期范围内，因此预期是可以正常运行的，如下所示：

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/6240a5396e21bc631ffcfb36882ccc4f.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/6240a5396e21bc631ffcfb36882ccc4f.png)

 然后修改 Token 的生命周期，修改到一个很小的值，例如100ms，注意需要重启所有的 GooseFS Server，然后再执行上述测试命令，预期是会报错：

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/3f04d572792e0a4725c1f8498db7dea9.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/3f04d572792e0a4725c1f8498db7dea9.png)

如上图所示，因为 Token 的生命周期被设置到了一个很小的值，不足以运行完测试作业，因此报了 Token 过期，且不可再续期的错误。
