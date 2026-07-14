<!-- source: https://cloud.tencent.com/document/product/582/38145 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T22:11:48+08:00 -->

# API 概览

最近更新时间：2026-06-02 01:25:15


## 密钥相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
| --- | --- | --- |
| [CreateAccessCert](https://cloud.tencent.com/document/api/582/115736) | 创建访问凭证 | 20 |

## 快照相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
| --- | --- | --- |
| [DeleteAutoSnapshotPolicy](https://cloud.tencent.com/document/api/582/80209) | 删除快照策略 | 20 |
| [DescribeAutoSnapshotPolicies](https://cloud.tencent.com/document/api/582/80208) | 查询文件系统快照策略列表信息 | 20 |
| [DescribeCfsSnapshotOverview](https://cloud.tencent.com/document/api/582/80207) | 文件系统快照概览 | 20 |
| [DescribeCfsSnapshots](https://cloud.tencent.com/document/api/582/80206) | 查询快照列表 | 20 |
| [DescribeSnapshotOperationLogs](https://cloud.tencent.com/document/api/582/80205) | 查询快照操作日志 | 20 |
| [UnbindAutoSnapshotPolicy](https://cloud.tencent.com/document/api/582/80204) | 解绑快照策略 | 20 |
| [UpdateCfsSnapshotAttribute](https://cloud.tencent.com/document/api/582/80202) | 更新文件系统快照信息 | 20 |
| [BindAutoSnapshotPolicy](https://cloud.tencent.com/document/api/582/80211) | 文件系统绑定快照策略 | 20 |
| [CreateAutoSnapshotPolicy](https://cloud.tencent.com/document/api/582/80210) | 创建定期快照策略 | 20 |
| [UpdateAutoSnapshotPolicy](https://cloud.tencent.com/document/api/582/80203) | 更新定期快照策略 | 20 |

## 权限组相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
| --- | --- | --- |
| [CreateCfsPGroup](https://cloud.tencent.com/document/api/582/38161) | 创建权限组 | 20 |
| [CreateCfsRule](https://cloud.tencent.com/document/api/582/38160) | 创建权限组规则 | 20 |
| [DeleteCfsPGroup](https://cloud.tencent.com/document/api/582/38159) | 删除权限组 | 20 |
| [DeleteCfsRule](https://cloud.tencent.com/document/api/582/38158) | 删除权限组规则 | 20 |
| [DescribeCfsPGroups](https://cloud.tencent.com/document/api/582/38157) | 查询权限组列表 | 20 |
| [DescribeCfsRules](https://cloud.tencent.com/document/api/582/38156) | 查询权限组规则 | 20 |
| [OverrideCfsRules](https://cloud.tencent.com/document/api/582/131443) | 批量覆盖式创建权限组规则 | 20 |
| [UpdateCfsPGroup](https://cloud.tencent.com/document/api/582/38155) | 更新权限组信息 | 20 |
| [UpdateCfsRule](https://cloud.tencent.com/document/api/582/38154) | 更新权限组规则 | 20 |
| [UpdateCfsFileSystemPGroup](https://cloud.tencent.com/document/api/582/38167) | 更新文件系统的权限组 | 20 |

## 文件系统相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
| --- | --- | --- |
| [CreateCfsSnapshot](https://cloud.tencent.com/document/api/582/80200) | 创建文件系统快照 | 20 |
| [DeleteCfsFileSystem](https://cloud.tencent.com/document/api/582/38173) | 删除文件系统 | 20 |
| [DeleteCfsSnapshot](https://cloud.tencent.com/document/api/582/80199) | 删除文件系统快照 | 20 |
| [DeleteUserQuota](https://cloud.tencent.com/document/api/582/82655) | 删除文件系统配额 | 20 |
| [DescribeCfsFileSystemClients](https://cloud.tencent.com/document/api/582/47581) | 查询文件系统客户端 | 20 |
| [DescribeCfsFileSystems](https://cloud.tencent.com/document/api/582/38170) | 查询文件系统 | 20 |
| [DescribeMountTargets](https://cloud.tencent.com/document/api/582/38169) | 查询文件系统挂载点 | 20 |
| [DescribeUserQuota](https://cloud.tencent.com/document/api/582/82654) | 查询文件系统配额 | 20 |
| [SetUserQuota](https://cloud.tencent.com/document/api/582/82653) | 设置文件系统配额 | 20 |
| [UpdateCfsFileSystemName](https://cloud.tencent.com/document/api/582/38168) | 更新文件系统名 | 20 |
| [UpdateCfsFileSystemSizeLimit](https://cloud.tencent.com/document/api/582/38166) | 更新文件系统存储容量限制 | 20 |
| [CreateCfsFileSystem](https://cloud.tencent.com/document/api/582/38174) | 创建文件系统 | 10 |
| [UpdateFileSystemBandwidthLimit](https://cloud.tencent.com/document/api/582/101428) | 更新文件系统吞吐 | 20 |
| [DoDirectoryOperation](https://cloud.tencent.com/document/api/582/122412) | 目录操作接口 | 20 |

## 服务相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
| --- | --- | --- |
| [DescribeAvailableZoneInfo](https://cloud.tencent.com/document/api/582/38171) | 查询区域可用情况 | 20 |
| [DescribeCfsServiceStatus](https://cloud.tencent.com/document/api/582/38164) | 查询CFS服务状态 | 20 |
| [SignUpCfsService](https://cloud.tencent.com/document/api/582/38163) | 开通CFS服务 | 20 |

## 生命周期相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
| --- | --- | --- |
| [ApplyPathLifecyclePolicy](https://cloud.tencent.com/document/api/582/122054) | 配置生命周期策略关联目录 | 20 |
| [DescribeLifecyclePolicies](https://cloud.tencent.com/document/api/582/122046) | 查询生命周期管理策略 | 20 |
| [CreateLifecyclePolicy](https://cloud.tencent.com/document/api/582/122051) | 创建生命周期策略 | 20 |
| [DeleteLifecyclePolicy](https://cloud.tencent.com/document/api/582/122049) | 删除生命周期管理策略 | 20 |
| [ModifyLifecyclePolicy](https://cloud.tencent.com/document/api/582/122044) | 更新生命周期策略 | 20 |
| [CreateLifecycleDataTask](https://cloud.tencent.com/document/api/582/122052) | 创建数据管理任务 | 20 |
| [DescribeLifecycleDataTask](https://cloud.tencent.com/document/api/582/122047) | 查询生命周期任务的接口 | 20 |
| [StopLifecycleDataTask](https://cloud.tencent.com/document/api/582/122043) | 终止生命周期任务的接口 | 20 |

## 其他接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
| --- | --- | --- |
| [CreateLifecyclePolicyDownloadTask](https://cloud.tencent.com/document/api/582/122056) | 创建下载生命周期文件列表任务 | 20 |

## 扩容相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
| --- | --- | --- |
| [ModifyFileSystemAutoScaleUpRule](https://cloud.tencent.com/document/api/582/90591) | 更新文件系统自动扩容策略 | 20 |
| [ScaleUpFileSystem](https://cloud.tencent.com/document/api/582/90456) | 文件系统存储量扩容 | 20 |

## 数据迁移相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
| --- | --- | --- |
| [CreateMigrationTask](https://cloud.tencent.com/document/api/582/90217) | 创建迁移任务 | 20 |
| [DeleteMigrationTask](https://cloud.tencent.com/document/api/582/90216) | 删除迁移任务 | 20 |
| [DescribeBucketList](https://cloud.tencent.com/document/api/582/90215) | 获取对象存储桶列表 | 20 |
| [DescribeMigrationTasks](https://cloud.tencent.com/document/api/582/90214) | 获取迁移任务列表 | 20 |
| [StopMigrationTask](https://cloud.tencent.com/document/api/582/90213) | 终止迁移任务 | 20 |

## 数据流动相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
| --- | --- | --- |
| [CreateDataFlow](https://cloud.tencent.com/document/api/582/122053) | 创建数据流动 | 20 |
| [DescribeDataFlow](https://cloud.tencent.com/document/api/582/122048) | 查询数据流动信息 | 20 |
| [DeleteDataFlow](https://cloud.tencent.com/document/api/582/122050) | 删除数据流动 | 20 |
| [ModifyDataFlow](https://cloud.tencent.com/document/api/582/122045) | 修改数据流动相关参数 | 20 |

## 数据检索相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
| --- | --- | --- |
| [DeleteDataRetrieval](https://cloud.tencent.com/document/api/582/132387) | 删除数据检索 | 20 |
| [DescribeDataRetrieval](https://cloud.tencent.com/document/api/582/132386) | 查询数据检索 | 20 |
| [RunDataRetrievalTask](https://cloud.tencent.com/document/api/582/132383) | 执行数据检索任务 | 20 |
| [CreateDataRetrieval](https://cloud.tencent.com/document/api/582/132388) | 创建数据检索 | 20 |
| [DescribeDataRetrievalTask](https://cloud.tencent.com/document/api/582/132385) | 查询数据检索任务 | 20 |
| [ModifyDataRetrieval](https://cloud.tencent.com/document/api/582/132384) | 修改数据检索 | 20 |

> 注意：
>
>
> 以上给出的接口频率限制维度为`API + 接入地域 + 子账号`，有关限频更多说明参考：[API 频率限制说明](https://cloud.tencent.com/document/product/1278/109059)
