<!-- source: https://cloud.tencent.com/document/product/436/54233 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:10:35+08:00 -->

# CKafka 消息备份

最近更新时间：2025-07-28 11:55:41


## 简介

CKafka 消息备份是腾讯云对象存储（Cloud Object Storage，COS）基于 [云函数（Serverless Cloud Function，SCF）](https://cloud.tencent.com/document/product/583) 为用户提供的 CKafka 消息转存至 COS 的功能，可以协助用户将 CKafka 消息进行转存以便于对数据进行分析与下载等操作。

CKafka 是基于开源 Apache Kafka 消息队列引擎，提供高吞吐性能、高可扩展性的消息队列服务，详情请参见 [CKafka 产品概述](https://cloud.tencent.com/document/product/597/10066)。

用户在指定存储桶配置了备份函数规则后，当 CKafka 实例产生消息时，云函数会按照一定的时间粒度获取消息并转存至 COS 存储桶中。

## 注意事项

若您此前在对象存储控制台上为存储桶添加了 CKafka 消息备份规则，可以在 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default) 上看到您所创建的 CKafka 消息备份函数，请**不要**删除该函数，否则可能导致您的规则不生效。

当前功能仅支持 COS 与 SCF 均相同的地域，部分地域（例如重庆地域）不支持使用，具体以 COS、SCF 控制台上显示的地域为准。

## 操作步骤

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。

2. 在左侧导航中，单击**应用集成**>**数据备份**，找到 **CKafka 消息备份**。

3. 单击**配置备份规则**，进入规则配置页面。

4. 单击**添加函数**。

**注意：**

如果您尚未开通云函数服务，请前往 [云函数控制台](https://console.cloud.tencent.com/scf) 开通云函数服务，按照提示完成服务授权即可。

5. 在弹出的窗口中，配置如下信息。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/3f0f97a82ab8910a3e7779e81c9b15c6.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/3f0f97a82ab8910a3e7779e81c9b15c6.png)

**函数名称**：作为函数的唯一标识名称，创建后不可修改。您可以在 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default) 上查看该函数。

**关联存储桶**：存放 CKafka 消息的 COS 存储桶。

**时间粒度**：根据消息量的大小，选取汇聚消息的时间间隔，时间间隔为5 - 15分钟不等。为保证转存性能，聚合文件数量与 Partition 数量、partition_max 设置数值有关。有关 Partition 的说明，请参见 [分区](https://cloud.tencent.com/document/product/597/32544#F)。

**SCF 授权**：CKafka 消息备份需要授权云函数从您的 CKafka 服务中读取相关实例消息，并将消息转存至您指定的存储桶中。因此需要添加此授权。

6. 单击**下一步**，进行 CKafka 配置，配置项说明如下。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/20027342b49c23e02bf37fc7a030d81f.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/20027342b49c23e02bf37fc7a030d81f.png)

**实例选择**：选择消息来源的 CKafka 实例，仅支持同地域的 CKafka 实例。

**主题选择**：选择消息来源的主题。

**起始位置**：消息转储备份时历史消息的处理方式，topic offset 设置。

**访问地址**：必须为 VPC 内网访问地址，基础网络的 CKafka 实例请添加路由策略，具体请参考 [添加路由策略](https://cloud.tencent.com/document/product/597/36348)。

**注意：**

对应的 VPC 子网中必须有可用的 IP，且必须支持 DHCP。

7. 单击**下一步**，进行投递配置，配置项说明如下。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/ad71620c990cfec201d30fc39ff4bdc8.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/ad71620c990cfec201d30fc39ff4bdc8.png)

**投递的路径**：备份文件的投递路径前缀，默认保存在存储桶根目录。如果选择指定前缀，则投递前缀不能以 / 开头，且必须以 / 结尾。

8. 添加配置后，单击**确认**，稍等片刻，即可看到函数已添加完成。

9. 您可以对新创建的函数进行如下操作：

单击**日志**，查看 CKafka 消息备份的历史运行情况。当备份出现报错时，您还可以通过单击**日志**，快速跳转到云函数控制台查看日志错误详情。

单击**详情**，可查看函数、触发器的详细信息。

单击**更多**>**编辑**，修改 CKafka 消息备份规则。

单击**更多**>**删除**，删除不使用的 CKafka 消息备份规则。
