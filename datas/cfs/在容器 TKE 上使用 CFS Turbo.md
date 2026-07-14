<!-- source: https://cloud.tencent.com/document/product/582/56768 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T22:11:26+08:00 -->

# 在容器 TKE 上使用 CFS Turbo

最近更新时间：2026-03-24 10:30:21


## 简介

本文为您介绍如何使用 CFS Turbo 对接容器服务（Tencent Kubernetes Engine，TKE）集群。

## 前提条件

TKE 的宿主机节点满足 Turbo 系列兼容的操作系统。

## 操作步骤

### 安装并设置 CFS 扩展组件

1. 进入[TKE 集群列表页](https://console.cloud.tencent.com/tke2/cluster?rid=1)，单击目标 TKE 集群 ID，进入集群详情页。

2. 在左侧选择**组件管理**，在组件页面单击**新建**。

3. 勾选**存储**>**CFSTurbo**，单击**完成**即可创建组件。

### 创建 **PersistentVolume**

1. 进入[TKE 集群列表页](https://console.cloud.tencent.com/tke2/cluster?rid=1)，单击使用 CFS 的 TKE 集群 ID，进入集群详情页。

2. 在左侧选择**存储**，在 **PersistentVolume**页面单击**新建**，配置参数如下：

**来源设置**：选择**静态创建**。

**名称**：填写名称。

**Provisioner**：选择 **文件存储 CFS Turbo**。

**读写权限**：文件存储 CFS Turbo 仅支持**多机读写**。

**是否指定 StorageClass**：选择**不指定**，对应 YAML 文件中的 `storageClassName` 字段取值为空字符串。

填写 CFS Turbo 根目录和子目录。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/11d65b5c8624ce848c41b98b0534aec4.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/11d65b5c8624ce848c41b98b0534aec4.png)

3. 单击**创建 PersistentVolume**，即可完成创建。

### 创建 **PersistentVolumeClaim**

1. 进入[TKE 集群列表页](https://console.cloud.tencent.com/tke2/cluster?rid=1)，单击使用 CFS 的 TKE 集群 ID，进入集群详情页。

2. 在左侧选择**存储**，在 **PersistentVolumeClaim**页面单击**新建**，配置参数如下：

**Provisioner**：选择**文件存储 CFS Turbo**。

**读写权限**：文件存储 CFS Turbo 仅支持**多机读写**。

**是否指定 StorageClass**：如果当前集群内没有满足条件的 PV 可选，请选择**不指定**StorageClass。

**是否指定 PersistentVolume**：选择**指定**，并关联上一步创建的 **PersistentVolume**。PersistentVolume 需要与指定的 StorageClass 相同并且状态为 Available 和 Released。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/0ce15d23d4b7456e6d688c69d276f6e0.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/0ce15d23d4b7456e6d688c69d276f6e0.png)

3. 单击**创建 PersistentVolumeClaim**，即可完成创建。

### 创建工作负载

1. 进入[TKE 集群列表页](https://console.cloud.tencent.com/tke2/cluster?rid=1)，单击使用 CFS 的 TKE 集群 ID，进入集群详情页。

2. 在左侧选择**工作负载**，在**Deployment**页面单击**新建**。

3. 在新建工作负载页面单击**添加数据卷**。

4. 在新增数据卷弹窗中，数据卷类型选择**使用已有 PVC**，并选择上述已创建的 PVC，填写数据卷名称，单击**确认**。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/15d100294ea1553fedce411aedf76eea.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/15d100294ea1553fedce411aedf76eea.png)

5. 在**实例内容器**的**挂载点**中，单击**添加挂载点**，选择上方创建的数据卷，设置数据卷挂载到容器中的路径。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/1a0ef8691f111451fdba19aa81d7bef9.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/1a0ef8691f111451fdba19aa81d7bef9.png)

### 登录容器查看挂载情况

1. 进入[TKE 集群列表页](https://console.cloud.tencent.com/tke2/cluster?rid=1)，单击使用 CFS 的 TKE 集群 ID，进入集群详情页。

2. 在左侧选择**工作负载**，在 **Deployment**页面单击新建的工作负载名称。

3. 进入 **Pod 管理**页面，在操作栏单击**登录**。

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/9837ad1546703d81b644900c4a86eb35.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/9837ad1546703d81b644900c4a86eb35.png)

4. 在**容器登录**弹窗中，单击 **OrcaTerm 登录**。登录后执行`df -h`即可看到挂载的 CFS 文件系统。

![Image 12](https://qcloudimg.tencent-cloud.cn/image/document/eb202d4e589fc39ed33360e0690e95df.png)

![Image 13](https://qcloudimg.tencent-cloud.cn/image/document/eb202d4e589fc39ed33360e0690e95df.png)

## 补充：基于自建容器使用 CFS Turbo

### 前提条件

### 容器宿主机节点满足 Turbo 系列兼容的操作系统。

已在所有容器宿主机节点安装 Turbo 的私有客户端，推荐使用 pshell 工具进行批量操作。

相关的操作系统兼容列表及私有客户端安装方式，可参见 [在 Linux 客户端上使用 CFS Turbo 文件系统](https://cloud.tencent.com/document/product/582/54765) 文档。

### 配置 kubectl 连接集群

您可参见 [TKE 连接集群](https://cloud.tencent.com/document/product/457/32191)，配置 kubectl，以管理容器集群。

### 通过 YAML 文件创建挂载 Turbo 的 Pod

1. 阅读 [TKE Turbo 插件的说明文档](https://github.com/TencentCloud/kubernetes-csi-tencentcloud/blob/master/docs/README_CFSTURBO.md)。

2. 进入 `kubernetes-csi-tencentcloud/deploy/cfsturbo/kubernetes/` 目录，分别将 csi-node-rbac.YAML、csi-node.YAML 和 csidriver-new.YAML 文件上传至 kubectl 管理节点。

3. 进入 `kubernetes-csi-tencentcloud/deploy/cfsturbo/examples/` 目录，下载 pv.YAML、pvc.YAML、pod.YAML 这三个示例文件。

4. 根据实际 PV、PVC、Pod 的相关属性（如名称、镜像地址等），修改 pv.YAML、pvc.YAML、pod.YAML 文件。

5. YAML 示例如下：

apiVersion: v1

kind: PersistentVolume

metadata:

 name: csi-cfsturbo-pv

spec:

 accessModes:

 - ReadWriteMany

 capacity:

 storage: 10Gi

 csi:

 driver: com.tencent.cloud.csi.cfsturbo

 # volumeHandle in PV must be unique, use pv name is better

 volumeHandle: csi-cfsturbo-pv

 volumeAttributes:

 # cfs turbo proto

 proto: lustre

 # cfs turbo rootdir

 rootdir: /cfs

 # cfs turbo fsid (not cfs id)

 fsid: xxxxxxxx

 # cfs turbo server ip

 host: 10.0.1.16

 # cfs turbo subPath

 path: /

 storageClassName: ""

---

apiVersion: v1

kind: PersistentVolumeClaim

metadata:

 name: csi-cfsturbo-pvc

spec:

 accessModes:

 - ReadWriteMany

 resources:

 requests:

 storage: 10Gi

 # You can specify the pv name manually or just let kubernetes to bind the pv and pvc.

 volumeName: csi-cfsturbo-pv

 # cfsturbo only supports static provisioning, the StorageClass name should be empty.

 storageClassName: ""

---

apiVersion: apps/v1

kind: Deployment

metadata:

 labels:

 k8s-app: csi-cfsturbo-pod

 name: csi-cfsturbo-pod

spec:

 replicas: 1

 selector:

 matchLabels:

 k8s-app: csi-cfsturbo-pod

 template:

 metadata:

 labels:

 k8s-app: csi-cfsturbo-pod

 spec:

 containers:

 - image: nginx

 name: csi-cfsturbo-pod

 volumeMounts:

 - mountPath: /csi-cfsturbo

 name: csi-cfsturbo

 volumes:

 - name: csi-cfsturbo

 persistentVolumeClaim:

 # Replaced by your pvc name.

 claimName: csi-cfsturbo-pvc

以此挂载指令为例：

sudo mount.lustre -o sync,user_xattr 10.0.xx.xx@tcp0:/xxxxxxxx/cfs /path/to/mount

关键参数说明如下：

proto：lustre，请保持此参数不要进行修改。

rootdir：/cfs，请保持此参数不要进行修改。

fsid：xxxxxxxx，此处的 fsid 不是 CFSID，需要填写挂载路径里的信息。

host：10.0.1.16，挂载点 IP。

path：可根据实际需要挂载的子目录进行调整，若直接挂载根目录则填写"/"。

6. 在上传脚本文件的目录下，依次执行以下命令。

配置 RBAC、CSI 插件。

kubectl apply -f csi-node-rbac.YAML && kubectl apply -f csidriver-new.YAML && kubectl apply -f csi-node.YAML

创建 PV、PVC、Pod。

kubectl create -f pv.YAML && kubectl create -f pvc.YAML && kubectl create -f pod.YAML

7. 执行以下命令，查看 Pod 状态。

kubectl get pod -n default -o wide

返回如下结果，即表示创建成功：

![Image 14](https://qcloudimg.tencent-cloud.cn/image/document/8d7a65c436a09b7e4b74d2bb2ceac6d2.png)

![Image 15](https://qcloudimg.tencent-cloud.cn/image/document/8d7a65c436a09b7e4b74d2bb2ceac6d2.png)

若状态（STATUS）持续为 ContainerCreating ，即表示创建失败。您可进入[TKE 集群列表页](https://console.cloud.tencent.com/tke2/cluster?rid=1)，单击使用 CFS 的 TKE 集群 ID，进入集群详情页。在左侧菜单栏单击**事件**，查看失败原因。
