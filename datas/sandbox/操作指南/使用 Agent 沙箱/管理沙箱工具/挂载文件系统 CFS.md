<!-- source: https://cloud.tencent.com/document/product/1814/129845 -->
<!-- fetcher: jina -->

# 挂载文件系统 CFS

最近更新时间：2026-03-27 18:02:01


## 功能描述

Agent 沙箱服务（AGS）提供了与腾讯云文件存储（CFS）的无缝集成能力。通过挂载功能，您可以将 CFS 实例的指定路径映射为沙箱内的本地文件目录，使 Agent 能够像操作本地文件一样读写云端数据，实现数据的持久化保存、多实例共享及跨任务流转。

## 场景介绍

#### **跨实例文件共享场景**

Agent 沙箱服务支持同一沙箱工具下的所有实例挂载相同的 CFS 路径，以满足数据与文件持久化存储和共享的需求。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/2c854f3b747ee8ae0956cb4dda0703b6.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/2c854f3b747ee8ae0956cb4dda0703b6.png)

#### **跨实例文件隔离场景**

Agent 通常需要为每个用户的会话（Session）分配独立的沙箱执行环境。在此场景中，数据安全与隐私是首要挑战。当多个用户并发使用同一 Agent 沙箱工具时，必须确保不同用户间**完全隔离**：**用户 A 绝不能访问到用户 B 的代码或数据**。因此可通过配置 `subpath` 的方式实现不同用户间的数据隔离。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/b8d7031f5b49147d2e43ebf8c02b00a6.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/b8d7031f5b49147d2e43ebf8c02b00a6.png)

## 操作步骤

**说明：**

AGS 基于 PrivateLink [私有连接](https://cloud.tencent.com/document/product/1451/57268) 提供 CFS 挂载能力。使用该功能时，AGS 会在您首次绑定 CFS 实例时，在您的账号下为该实例创建 [终端节点服务](https://cloud.tencent.com/document/product/1451/57404)，并关联到您指定的 CFS 实例。

**请注意：**

1. AGS 的 CFS 挂载功能依赖终端节点服务，请确保在沙箱的使用过程中**不要删除对应的终端节点服务**，否则会导致沙箱实例创建和访问异常。

2. AGS 会在您删除最后一个引用该 CFS 实例的沙箱工具时，尝试删除对应的终端节点服务。如果此时该终端节点服务被您的其他服务所使用，将会导致沙箱工具删除失败，此时请您在删除所有关联的终端节点后，再尝试删除沙箱工具。

### **步骤1：**为**沙箱工具配置 CFS 配置**

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/2009259b0da2e972e73a366808d3ce9e.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/2009259b0da2e972e73a366808d3ce9e.png)

**参数名称****是否必填****参数说明**
名称 是 该字段用于定义 **CFS 路径与沙箱本地路径的挂载映射关系**。

在**跨实例文件隔离**场景下，该字段将作为沙箱实例创建时的关键配置项，用于指定实例级别的存储挂载。
文件系统 是 CFS 实例名称，可下拉选择。
CFS 路径 是 CFS 实例下的指定路径，**请确保路径一定存在**。
挂载路径 是 沙箱本地挂载点路径。
读写权限 是 挂载读写权限。

### **步骤2：创建沙箱实例**

沙箱实例默认继承沙箱工具的挂载配置，同时也可以在创建时**声明 MountOptions**来覆盖沙箱工具的部分配置。

**注意：**

1. 未使用 `MountOptions` 覆盖挂载配置的实例，则继承沙箱工具上配置的参数进行挂载。

2. 挂载读写权限 `ReadOnly` 仅支持使用 `true` 覆盖 `false`，即沙箱实例不得声明高于沙箱工具中定义的读写权限。

#### **腾讯云 SDK**

创建实例时，可以通过 `MountOptions` 修改沙箱工具指定的 CFS 挂载配置。其中 `SubPath` 为新增字段，对于 `cfs1` 中定义的存储路径，可通过 `SubPath` 字段进行路径追加，从而达到同一个沙箱工具中不同实例挂载到不同 CFS 子路径的目的，常用于跨实例文件隔离的场景。

字段名 类型 是否必填 说明 示例
Name*string 是 匹配工具预定义的 `StorageMount` 名称。"cfs1"
MountPath*string 否 覆写工具默认的本地挂载路径。"/workspace/data", "/mnt/data"
ReadOnly*bool 否 覆写挂载权限，true 表示只读挂载。true, false
SubPath*string 否 子目录隔离，实现实例级别的目录隔离。"user-123", "project-alpha"

// 实例化一个请求对象,每个接口都会对应一个request对象

// request := ags.NewStartSandboxInstanceRequest()

...

request.MountOptions = []*ags.MountOption {

 &ags.MountOption {

 Name: common.StringPtr("cfs1"),

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
name string 是 匹配工具预定义的 StorageMount 名称。"cfs1"
mountPath string 否 覆写工具默认的本地挂载路径。"/workspace/data", "/mnt/data"
readOnly string 否 覆写挂载权限，true 表示只读挂载。true, false
subPath string 否 子目录隔离，实现实例级别的目录隔离。"user-123", "project-alpha"

**注意：**

E2B SDK 中的 `metadata["x-mounts"]`中，所有字段名为小驼峰（camelCase）风格，而腾讯云 SDK 为大驼峰（PascalCase）风格。

# 创建沙箱实例，配置subpath

from e2b import Sandbox

import json

sandbox = Sandbox.create(

 template="my-template",

 metadata={

 "x-mounts": json.dumps([

 {

 "name": "cfs1", # 必需：匹配工具配置的存储名称

 "mountPath": "/workspace/data", # 可选：自定义挂载路径

 "readOnly": False, # 可选：读写权限

 "subPath": "user-123" # 可选：子目录隔离

 },

 {

 "name": "cfs2", # 只指定必需字段

 "mountPath": "/mnt/data" # 自定义日志路径

 },

 {

 "name": "cfs3", # 只读挂载

 "readOnly": True # 只读权限

 }

 ])

 }

)

#### API 接口

API 接口详细信息请参见 [StorageMount](https://cloud.tencent.com/document/api/1814/124823#StorageMount)。
