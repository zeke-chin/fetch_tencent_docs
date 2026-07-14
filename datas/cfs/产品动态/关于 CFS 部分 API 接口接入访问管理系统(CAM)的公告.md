<!-- source: https://cloud.tencent.com/document/product/582/109027 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T19:00:26+08:00 -->

# 关于 CFS 部分 API 接口接入访问管理系统(CAM)的公告

最近更新时间：2024-10-10 17:27:31


# 变更内容

本次计划接入鉴权的接口列表如下：

DescribeVipStatus

DescribeCfsPrepayDeductionRules

DescribeStatistics

DescribeCfsSnapshotOverview

DescribeCfsServiceStatus

DescribeCfsFileSystemsStatistics

DescribeAvailableZoneInfo

DescribeAutoSnapshotPolicies

# **变更时间**

北京时间：2024-10-23（周三） 11:00:00 - 2024-10-23 11:30:00

# 变更影响范围

如您的子账户未包含这类接口的授权，通过 API 或者控制台调用这类接口时，会有相关的权限不足报错提示。

**说明：**

1. 此类接口均为公共类的查询类接口，即使未有授权，也不影响实际业务数据流的访问。

2. 如果您的子账户被授予了 QcloudCFSFullAccess或QcloudCFSReadOnlyAccess 的策略，此次变更不影响您的使用。

3. 如果您的子账户被授予了 describe* 的授权，此次变更也不影响您的使用。

# 建议处理方式

如您的账户因此次变更造成了权限不足无法访问的报错，建议您按照如下方案进行调整。

## 方法1：

参考 [通过策略生成器创建自定义策略](https://cloud.tencent.com/document/product/598/37739) ，选择对应的 API 接口，创建新的自定义策略，并将此新策略关联至所需要的用户/用户组。

## 方法2：

可进入 [CAM 策略管理页面](https://console.cloud.tencent.com/cam/policy)，对过往的策略新增相关的接口授权，原有绑定此策略的用户/用户组即可正常访问。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/1a9c13d96a4c53e5a87fbf1bb872d613.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/1a9c13d96a4c53e5a87fbf1bb872d613.png)
