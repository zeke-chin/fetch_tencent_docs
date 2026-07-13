<!-- source: https://cloud.tencent.com/document/product/1814/126941 -->
<!-- fetcher: jina -->

# 挂载文件系统 COSFS

最近更新时间：2025-12-29 20:50:51


## 功能描述

Agent 沙箱服务（AGS）提供了与腾讯云对象存储（COS）的无缝集成能力。通过挂载功能，您可以将 COS 存储桶的指定路径映射为沙箱内的本地文件目录，使 Agent 能够像操作本地文件一样读写云端数据，实现数据的持久化保存、多实例共享及跨任务流转。

## 场景介绍

#### **跨实例文件共享场景**

Agent 沙箱服务支持同一沙箱工具下的所有实例挂载相同的 COS 路径，以满足数据与文件持久化存储和共享的需求。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/881b58612a0f7442dfb0066330988954.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/881b58612a0f7442dfb0066330988954.png)

#### **跨实例文件隔离场景**

Agent 通常需要为每个用户的会话（Session）分配独立的沙箱执行环境。在此场景中，数据安全与隐私是首要挑战。当多个用户并发使用同一 Agent 沙箱工具时，必须确保不同用户间**完全隔离**：**用户 A 绝不能访问到用户 B 的代码或数据**。因此可通过配置 `subpath` 的方式实现不同用户间的数据隔离。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/d42ae4dfa8706c3c1195c6ab85fc47fd.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/d42ae4dfa8706c3c1195c6ab85fc47fd.png)

## 操作步骤

以下步骤仅描述文件系统相关配置。

### **步骤1：为沙箱工具配置 CAM 角色**

为了保障不同的沙箱工具具备不同的 COS 存储桶权限，沙箱服务需要您为每个沙箱工具配置允许其访问 COS 的权限，即自定义角色。

1. **新建沙箱工具**，操作步骤请参见 [创建沙箱工具](https://cloud.tencent.com/document/product/1814/123820)。

2. **新建 CAM 角色**。

2.1 进入 [访问管理控制台 > 角色](https://console.cloud.tencent.com/cam/role)。

2.2 单击**新建角色**，选择**腾讯云产品服务**。

2.3 在**新建自定义角色**页面，产品服务选择**Agent 沙箱服务 (ags)**，可选择的使用案例选择 **Agent 沙箱服务**。单击**下一步。**

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/86c73c6316e8fc5cbfed28bf80310eac.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/86c73c6316e8fc5cbfed28bf80310eac.png)

2.4 选择您需要的 COS 策略，并完成新建。

3. 在新建沙箱工具步骤中，配置 CAM 角色，配置您创建的 CAM 角色。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/e2659af6e26c8d6395acf95a60e2d650.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/e2659af6e26c8d6395acf95a60e2d650.png)

### **步骤2：**为**沙箱工具配置 COS 配置**

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/fe0e27febb7a2fa81a2ed29d50e3a011.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/fe0e27febb7a2fa81a2ed29d50e3a011.png)

**参数名称****是否必填****参数说明**
名称 是 该字段用于定义 **COS 存储桶路径与沙箱本地路径的挂载映射关系**。

在**跨实例文件隔离**场景下，该字段将作为沙箱实例创建时的关键配置项，用于指定实例级别的存储挂载。
存储桶名称 是 COS 存储桶实例名称，可下拉选择。
存储路径 是 COS 存储桶下的指定路径。
挂载路径 是 沙箱本地挂载点路径。
读写权限 是 挂载读写权限。

### **步骤3：创建沙箱实例**

沙箱实例默认继承沙箱工具的挂载配置，同时也可以在创建时**声明 MountOptions**来覆盖沙箱工具的部分配置。

**注意：**

1. 未使用 `MountOptions` 覆盖挂载配置的实例，则集成沙箱工具上配置的参数进行挂载。

2. 挂载读写权限 `ReadOnly` 仅支持使用 `true` 覆盖 `false`，即沙箱实例不得声明高于沙箱工具中定义的读写权限。

#### **腾讯云 SDK**

创建实例时，可以通过 `MountOptions` 修改沙箱工具指定的 COS 挂载配置。其中 `SubPath` 为新增字段，对于 `cosfilesystem1` 中定义的存储路径，可通过 `SubPath` 字段进行路径追加，从而达到同一个沙箱工具中不同实例挂载到不同 COS 子路径的目的，常用于跨实例文件隔离的场景。

字段名 类型 是否必填 说明 示例
Name*string 是 匹配工具预定义的 `StorageMount` 名称。"cosfilesystem1"
MountPath*string 否 覆写工具默认的本地挂载路径。"/workspace/data", "/mnt/data"
ReadOnly*bool 否 覆写挂载权限，true 表示只读挂载。true, false
SubPath*string 否 子目录隔离，实现实例级别的目录隔离。"user-123", "project-alpha"

// 实例化一个请求对象,每个接口都会对应一个request对象

// request := ags.NewStartSandboxInstanceRequest()

...

request.MountOptions = []*ags.MountOption {

 &ags.MountOption {

 Name: common.StringPtr("cosfilesystem1"),

 MountPath: common.StringPtr("/mnt/data"),

 SubPath: common.StringPtr("user-123"),

 ReadOnly: common.BoolPtr(true),

 },

}

...

// 返回的resp是一个StartSandboxInstanceResponse的实例，与请求对象对应

// response, err := client.StartSandboxInstance(request)

#### **E2B SDK**

E2B 原生不支持 `MountOptions` 字段，AGS 可以支持 E2B SDK 通过 `metadata["x-mounts"]` 传递 JSON 格式的挂载配置：

字段名 类型 是否必填 说明 示例
name string 是 匹配工具预定义的 StorageMount 名称。"cosfilesystem1"
mountPath string 否 覆写工具默认的本地挂载路径。"/workspace/data", "/mnt/data"
readOnly string 否 覆写挂载权限，true 表示只读挂载。true, false
subPath string 否 子目录隔离，实现实例级别的目录隔离。"user-123", "project-alpha"

**注意：**

E2B SDK 中的`metadata["x-mounts"]`中，所有字段名为小驼峰（camelCase）风格，而腾讯云 SDK 为大驼峰（PascalCase）风格。

# 创建沙箱实例，配置subpath

from e2b import Sandbox

import json

sandbox = Sandbox.create(

 template="my-template",

 metadata={

 "x-mounts": json.dumps([

 {

 "name": "cosfilesystem1", # 必需：匹配工具配置的存储名称

 "mountPath": "/workspace/data", # 可选：自定义挂载路径

 "readOnly": False, # 可选：读写权限

 "subPath": "user-123" # 可选：子目录隔离

 },

 {

 "name": "cosfilesystem2", # 只指定必需字段

 "mountPath": "/mnt/data" # 自定义日志路径

 },

 {

 "name": "cosfilesystem3", # 只读挂载

 "readOnly": True # 只读权限

 }

 ])

 }

)

#### ****
