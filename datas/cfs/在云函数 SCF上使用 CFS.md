<!-- source: https://cloud.tencent.com/document/product/582/47148 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T22:11:18+08:00 -->

# 在云函数 SCF上使用 CFS

最近更新时间：2026-03-24 10:30:21


## 操作场景

[云函数（Serverless Cloud Function，SCF）](https://cloud.tencent.com/product/scf) 是腾讯云为企业和开发者们提供的无服务器执行环境，帮助您在无需购买和管理服务器的情况下运行代码。您只需使用平台支持的语言编写核心代码并设置代码运行的条件，即可在腾讯云基础设施上弹性、安全地运行代码。SCF 是实时文件处理和数据处理等场景下理想的计算平台。

SCF 是服务级别的计算资源，它的快速迭代、极速部署的特性天然需要存储与计算分离，而文件存储（Cloud File Storage，CFS）提供的高性能共享存储服务为 SCF 最佳的存储方案。只需几步简单配置，您的函数即可轻松访问存储在 CFS 文件系统中的文件。

云函数 SCF 使用文件存储 CFS 的优势如下：

函数执行空间不受限。

多个函数可共用一个文件系统，实现文件共享。

## 操作步骤

### 关联授权策略

**注意：**

如需使用 CFS 功能，云函数需要能够操作您的 CFS 资源的权限。如您使用的账号未赋予云函数权限，可能出现函数无法保存，CFS 相关功能无法使用等问题。

请参考以下步骤为账号进行授权操作：

如您的账号为主账号，请参见 [修改角色](https://cloud.tencent.com/document/product/598/19389) 为 `SCF_QcsRole` 角色关联 `QcloudCFSReadOnlyAccess` 策略。关联成功则如下图所示：

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/a7626583b2a31f398d6b24aeaa071da6.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/a7626583b2a31f398d6b24aeaa071da6.png)

如您使用账号为子账号，则请联系主账号并参见 [子用户权限设置](https://cloud.tencent.com/document/product/598/36256) 为您的子账号关联 `QcloudCFSReadOnlyAccess` 策略。关联成功则如下图所示：

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/51c0e6af903dff6f2ec04cf12c55bca7.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/51c0e6af903dff6f2ec04cf12c55bca7.png)

### 创建 CFS 文件系统

具体操作请参考 [创建 CFS 文件系统](https://cloud.tencent.com/document/product/582/9132) 。

**注意：**

目前云函数仅支持添加网络类型为 VPC 的 CFS 文件系统作为挂载点。请在创建的 CFS 文件系统时，选择与函数相同的 VPC，以确保网络能够互通。

### 挂载并使用 CFS 文件系统

1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf/index)，选择左侧导航栏中的 [函数服务](https://console.cloud.tencent.com/scf/list)。

2. 在**函数服务**页面，单击需要使用 CFS 存储的函数名，进入**函数管理**页面。

3. 选择**函数配置**页签，单击右上角的**编辑**。

4. 在**网络配置**中，勾选启用并选择 CFS 文件系统所在的 VPC。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/f05057bdf2ec230fa6fffb6cc06f1530.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/f05057bdf2ec230fa6fffb6cc06f1530.png)

5. 在**文件系统**中单击**添加文件系统**，并按照以下信息进行挂载。如下图所示：

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/193a558e955b5a1568ae949f37a5936d.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/193a558e955b5a1568ae949f37a5936d.png)

**文件系统类型**：目前仅支持挂载使用 CFS 通用系列，CFS Turbo 系列正在灰度中。

**文件系统 ID**：在下拉列表中选择需挂载的文件系统。如果您未提前创建，可以**新建文件系统**。

**挂载点 ID**：在下拉列表中选择对应文件系统的挂载点 ID。

**远程目录**：云函数需要访问 CFS 文件系统的远端目录，由文件系统和远端子目录两部分组成，远端子目录路径必须存在。

**本地目录**：为本地文件系统的挂载路径，推荐挂载到 `/home/` 、`/mnt/` 或 `/data/` 目录的子目录挂载。

6. 单击页面下方的**保存**即可完成配置。您在 SCF 中对本地目录执行的读写操作，等同于在远端目录进行读写操作。

7. 为了验证是否挂载成功，您可以在**函数管理**>**函数代码**中部署并测试以下程序，观察远程目录的目录结构是否被成功返回。

import os

def main_handler(event, context):

 a=os.listdir("/mnt")

 return(a)

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/a604bd7b993ce1da70fe588cf0d1790f.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/a604bd7b993ce1da70fe588cf0d1790f.png)

### SCF 使用 CFS 文件系统性能测试

您可以使用此 [脚本](https://github.com/tencentyun/scf_cfs_demo) 测试云函数 SCF 使用 CFS 时的读写性能。
