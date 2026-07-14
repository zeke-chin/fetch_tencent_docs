<!-- source: https://cloud.tencent.com/document/product/436/115665 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:22:28+08:00 -->

# 创建元数据加速桶并开启 HDFS 协议

最近更新时间：2025-01-14 11:53:43


## 使用 HDFS 协议访问的优势

元数据加速功能底层采用了云 HDFS 卓越的元数据管理功能，支持用户通过文件系统语义访问对象存储服务，系统设计指标可以达到百 GB 级别带宽、十万级 QPS 以及毫秒级延迟。

开启元数据加速的存储桶，完全兼容 HCFS（Hadoop Compatible File System，HCFS） 协议，可以采用原生的 HDFS 接口直接访问。

对比使用 [Hadoop 工具](https://cloud.tencent.com/document/product/436/6884) 访问普通 COS 桶，使用 HDFS 协议访问时无需在工具内部将 HCFS 接口适配为 COS 的 Restful 接口，省去了协议转换开销，更能提供原生 HDFS 的一些功能，例如目录原子高效 Rename、文件 Atime、Mtime 更新、高效目录 DU 统计、Posix ACL 权限支持等原生特性。

**注意：**

由于元数据加速桶底层架构，推荐您使用 HDFS 协议访问元数据桶，而非对象存储 Restful 接口，以实现最优性能实践。

## 步骤一：创建元数据加速桶

参考 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 登录 [对象存储控制台](https://console.cloud.tencent.com/cos/bucket) 创建存储桶并开启**元数据加速**。若您未授权 HDFS 服务角色，需要先单击**立即授权**进入 [授权角色](https://console.cloud.tencent.com/cam/role/grant?roleName=CHDFS_QCSLinkedRoleInMetaMgmt&serviceLinkedRole=1)。**同意授权**后才可创建成功。

**说明：**

若您需频繁使用对象存储语义进行读写，**不推荐**开启元数据加速功能。

元数据桶部分管理功能受限，具体限制请参见 [使用限制说明](https://cloud.tencent.com/document/product/436/56971#.E4.BD.BF.E7.94.A8.E9.99.90.E5.88.B6)。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/fce74f886eaa375bbf43023364d39b4c.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/fce74f886eaa375bbf43023364d39b4c.png)

## 步骤二：开启 HDFS 协议访问

1. 找到已创建的元数据加速桶，单击存储桶名称，进入存储桶详情页。

2. 在左侧菜单栏中，选择**湖存储配置 > 元数据加速能力**，可以看到**元数据加速能力**已开启，并且看到默认的存储桶挂载点信息。如下图所示：

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/ef88c9e4ef99ec5e04210bef17c0d37b.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/ef88c9e4ef99ec5e04210bef17c0d37b.png)

3. 在 **HDFS 元数据权限配置**栏中，单击**新增权限配置**，配置以下参数，完成后单击**保存**即可。

**VPC 网络名称/ID**选择计算集群所在的 VPC 网络地址。

**节点 IP 地址**填写 VPC 网段下需要放通的 IP 地址或者 IP 地址段。

**访问类型**选择可读可写或只读。

**说明：**

使用 HDFS 协议访问时，元数据加速桶会先校验计算节点 IP 是否满足该配置，使用前请您确保该配置项已配置正确。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/a3648d21c6382ffda06ad89cbd39e3ab.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/a3648d21c6382ffda06ad89cbd39e3ab.png)

4. 根据您的需求，可在 **HDFS 元数据鉴权配置**中选择**不鉴权**、**POSIX 鉴权**、**Ranger 鉴权**三种文件系统鉴权方式。单击**编辑**进入修改页面。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/ddae3334de1e9eff30b28465b6595bcd.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/ddae3334de1e9eff30b28465b6595bcd.png)

**说明：**

若您需要使用 POSIX 鉴权，您可在 **HDFS 用户配置**中配置超级用户列表，如下图所示。

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/4747ec303d42adcbcb2a838a3d8e29c0.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/4747ec303d42adcbcb2a838a3d8e29c0.png)

若您需要了解更多 Ranger 鉴权的说明，请参见 [COS Ranger 权限体系解决方案](https://cloud.tencent.com/document/product/436/51125)。
