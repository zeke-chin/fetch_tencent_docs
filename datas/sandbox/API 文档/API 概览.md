<!-- source: https://cloud.tencent.com/document/product/1814/124833 -->
<!-- fetcher: jina -->

# API 概览

最近更新时间：2026-01-29 01:08:06


## API密钥相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
| --- | --- | --- |
| [CreateAPIKey](https://cloud.tencent.com/document/api/1814/124822) | 创建新的API密钥 | 20 |
| [DeleteAPIKey](https://cloud.tencent.com/document/api/1814/124821) | 删除API密钥 | 20 |
| [DescribeAPIKeyList](https://cloud.tencent.com/document/api/1814/124820) | 获取API密钥列表 | 20 |

## 沙箱实例相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
| --- | --- | --- |
| [AcquireSandboxInstanceToken](https://cloud.tencent.com/document/api/1814/124818) | 获取沙箱实例的访问Token | 100 |
| [DescribeSandboxInstanceList](https://cloud.tencent.com/document/api/1814/124817) | 查询沙箱实例列表 | 20 |
| [PauseSandboxInstance](https://cloud.tencent.com/document/api/1814/127876) | 暂停沙箱实例 | 20 |
| [ResumeSandboxInstance](https://cloud.tencent.com/document/api/1814/127875) | 恢复沙箱实例 | 20 |
| [StartSandboxInstance](https://cloud.tencent.com/document/api/1814/124816) | 启动沙箱实例 | 100 |
| [StopSandboxInstance](https://cloud.tencent.com/document/api/1814/124815) | 停止沙箱实例 | 100 |
| [UpdateSandboxInstance](https://cloud.tencent.com/document/api/1814/124814) | 更新沙箱实例 | 20 |

## 沙箱工具相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
| --- | --- | --- |
| [CreateSandboxTool](https://cloud.tencent.com/document/api/1814/124812) | 创建沙箱工具 | 20 |
| [DeleteSandboxTool](https://cloud.tencent.com/document/api/1814/124811) | 删除沙箱工具 | 20 |
| [DescribeSandboxToolList](https://cloud.tencent.com/document/api/1814/124810) | 查询沙箱工具列表 | 20 |
| [UpdateSandboxTool](https://cloud.tencent.com/document/api/1814/124809) | 更新沙箱工具 | 20 |

## 镜像预热相关接口

| 接口名称 | 接口功能 | 频率限制（次/秒） |
| --- | --- | --- |
| [CreatePreCacheImageTask](https://cloud.tencent.com/document/api/1814/127508) | 创建预热镜像任务 | 20 |
| [DescribePreCacheImageTask](https://cloud.tencent.com/document/api/1814/127507) | 查询镜像预热任务信息 | 20 |

> 注意：
>
>
> 以上给出的接口频率限制维度为`API + 接入地域 + 子账号`，有关限频更多说明参考：[API 频率限制说明](https://cloud.tencent.com/document/product/1278/109059)
