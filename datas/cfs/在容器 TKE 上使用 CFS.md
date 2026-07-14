<!-- source: https://cloud.tencent.com/document/product/582/36929 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T22:11:08+08:00 -->

# 在容器 TKE 上使用 CFS

最近更新时间：2026-03-24 10:30:21


## 操作场景

文件存储（Cloud File Storage，CFS）在容器环境如下主要适用于两类场景：

### 场景一：POD/容器数据的持久化存储，推荐使用动态挂载 CFS

CFS 可提供一个持久化存储的空间，当 POD/容器销毁时，数据仍然保存；当 POD/容器再次启动时，可通过 PVC 快速挂载原空间，实现数据的读写操作。 相比于其他方案，单 FS 实例可同时支持多个 POD/容器的数据存储，并支持根据 CFS 实例中的不同子目录，分配给不同的 POD。CFS 通用标准型/性能型按照实际使用容量进行计费，且无最小购买容量要求，可降低用户大规模容器持久化数据存储的成本。

### 场景二：多 POD/容器的数据共享，推荐使用静态挂载 CFS

CFS 通过 NFS/私有协议提供了一个共享访问的目录空间给多个 POD/容器，实现数据资源的高效共享，相比于其他方案，能提供更高的带宽和 IOPS 能力。

本文将重点介绍基于腾讯云控制台，部署容器 workload 的方法。具体的 YAML 写法，可参考通过控制台创建 StorageClass 后自动生成 YAML 文件。

**注意：**

使用前，需确保容器服务 （Tencent Kubernetes Engine，TKE）集群的 CSI 组件在1.0.4版本以上。若版本不对，可在 TKE 控制台上进行更新，CSI 组件的更新不影响容器的正常使用。

## 操作步骤

### 动态挂载 CFS

**说明：**

POD/容器数据的持久化存储场景，推荐此方式进行挂载。

1. 创建 StorageClass，具体操作请参见 [通过控制台创建 StorageClass](https://cloud.tencent.com/document/product/457/44235#.E6.8E.A7.E5.88.B6.E5.8F.B0.E6.93.8D.E4.BD.9C.E6.8C.87.E5.BC.95) 文档。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/ec519a17857d3dc3c2e186872347bb18.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/ec519a17857d3dc3c2e186872347bb18.png)

相关的关键配置项如下：

配置项 配置项.说明
实例创建模式 此场景选择共享实例。
可用区 建议选择与容器宿主机相同的可用区，以便获得更好的性能。
存储类型 根据实际性能需求可选择通用标准型存储和通用性能型存储。
挂载选项 根据实际情况，选择合适的挂载参数，默认可保持为空。
协议版本 在非多个同时修改/编辑的场景下，建议使用 NFS V3协议，以便得到更好的性能。
回收策略 可根据实际需要，选择删除和保留，为避免数据误删优先建议选择保留。

**说明：**

详细参数请参见 [StorageClass 管理文件存储模板](https://cloud.tencent.com/document/product/457/44235)

2. 创建 PVC，具体操作请参见 [创建 PVC](https://cloud.tencent.com/document/product/457/44236#createPVC2) 文档。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/2e686d6364e3701ac35c723e5f85ea00.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/2e686d6364e3701ac35c723e5f85ea00.png)

相关的关键配置项如下：

配置项 配置项说明
命名空间 根据实际需要选择不同的命名空间。
Storageclass 选择刚才创建的 StorageClass。
是否指定PersistentVolume 动态创建可不指定 PV。

说明：基于 CFS 共享型实例的 StorageClass，在创建 PVC 时，若不指定 PV，CSI 插件会在创建 PVC 的同时，自动创建一个按量付费的 CFS 实例，此实例会随着 PVC 的删除而删除，故需谨慎处理基于此方式创建的 PVC。

3. 创建 Deployment，具体操作请参见 [创建 Deployment](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment) 文档。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/bacec3f9d1ed30ec756a3b3bc26c1d47.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/bacec3f9d1ed30ec756a3b3bc26c1d47.png)

相关的关键配置项如下：

配置项 配置项说明
数据卷 根据实际需求，对数据卷进行命名，并选中刚创建的 PVC。
挂载点 选择对应的数据卷，指定在容器本地的挂载路径。在共享 CFS 实例的动态创建方式下，需要指定具体的环境变量，CSI 插件会基于配置的环境变量的变量值，在所选 PVC 对应的 CFS 实例里创建目录供容器挂载。

4. 配置完成后，单击**创建 Workload**，系统将基于此配置创建容器，并挂载 CFS。

### 静态挂载 CFS

**说明：**

多 POD/容器的数据共享场景，推荐此方式进行挂载。

1. 创建 StorageClass，具体操作请参见 [通过控制台创建 StorageClass](https://cloud.tencent.com/document/product/457/44235#.E6.8E.A7.E5.88.B6.E5.8F.B0.E6.93.8D.E4.BD.9C.E6.8C.87.E5.BC.95) 文档。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/b2a7376888af4b400546ef4f85a6c4be.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/b2a7376888af4b400546ef4f85a6c4be.png)

相关的关键配置项如下：

配置项 配置项.说明
实例创建模式 此场景选择共享实例。
可用区 建议选择与容器宿主机相同的可用区，以便获得更好的性能。
存储类型 根据实际性能需求可选择通用标准型存储和通用性能型存储。
挂载选项 根据实际情况，选择合适的挂载参数，默认可保持为空。
协议版本 在非多个同时修改/编辑的场景下，建议使用 NFS V3协议，以便得到更好的性能。
回收策略 可根据实际需要，选择删除和保留，为避免数据误删优先建议选择保留。

**说明：**

详细参数请参见 [StorageClass 管理文件存储模板](https://cloud.tencent.com/document/product/457/44235)。

2. 创建 PV，具体操作请参见 [静态创建 PV](https://cloud.tencent.com/document/product/457/44236#pv) 文档。

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/c55569187b12d842211ee3f52d3df3a0.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/c55569187b12d842211ee3f52d3df3a0.png)

相关的关键配置项如下：

配置项 配置项说明
来源设置 选择静态创建，即指定某个 CFS 实例配置 PV。
StorageClass 选择刚才创建的 StorageClass。
选择 CFS 选择一个指定的 CFS。说明：静态创建时需要保证已经有一个 CFS 实例，同时该 CFS 实例需与容器在同一个 VPC 网络环境。
CFS 子目录 CFS 可以允许挂载子目录，用户可根据实际需要选择不同的子目录绑定至一个或多个 PV 上，实现不同程度的数据共享。

3. 创建 PVC，具体操作请参见 [创建 PVC](https://cloud.tencent.com/document/product/457/44236#createPVC2) 文档。

![Image 12](https://qcloudimg.tencent-cloud.cn/image/document/f764b26551e992a974436ae4dacd81c5.png)

![Image 13](https://qcloudimg.tencent-cloud.cn/image/document/f764b26551e992a974436ae4dacd81c5.png)

配置项 配置项说明
命名空间 根据实际需要选择不同的命名空间。
Storageclass 选择刚才创建的 StorageClass。
是否指定PersistentVolume 选择指定，并选择刚才创建的 PV。

4. 创建 Deployment，具体操作请参见 [创建 Deployment](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment) 文档。

![Image 14](https://qcloudimg.tencent-cloud.cn/image/document/e0c7f2a0fbd1ac07e0fce1b682d91f8a.png)

![Image 15](https://qcloudimg.tencent-cloud.cn/image/document/e0c7f2a0fbd1ac07e0fce1b682d91f8a.png)

相关的关键配置项如下：

配置项 配置项说明
数据卷 根据实际需求，对数据卷进行命名，并选中刚创建的 PVC。
挂载点 选择对应的数据卷，指定在容器本地的挂载路径。对于自动创建子目录的场景，目前有两种方案可以使用。

方案一，挂载点选择subPath，直接填写希望挂载的路径名称如 test，则 CSI 插件会自动在文件系统根路径下创建 test 目录，并自动挂载至容器的指定目录下。

方案二，添加环境变量，并给环境变量赋值。挂载点选择 subPathExpr，并选择对应的环境变量。则 CSI 插件将会以该环境变量的变量值作为目录名，自动在文件系统的根路径下创建该目录，并自动挂载至容器的指定目录下。

5. 配置完成后，单击**创建 Workload**，系统将基于此配置创建容器，并挂载 CFS。
