<!-- source: https://cloud.tencent.com/document/product/436/40548 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:04:08+08:00 -->

# 多 AZ 特性概述

最近更新时间：2026-03-03 16:35:42


## 简介

多 AZ（Multiple Availability Zones）是由 [腾讯云对象存储](https://cloud.tencent.com/product/cos) 推出的多 AZ 存储架构，该架构将客户数据分散存储在城市中多个不同的数据中心，当某个数据中心因自然灾害、断电等极端情况导致整体故障时，仍能为客户提供稳定可靠的存储服务。多 AZ 存储提供99.9999999999%（12个9）的数据设计可靠性和高达99.995%的服务设计可用性。用户在上传数据时，只需指定对象的存储类型，即可将对象存放到多 AZ 的地域。

**注意：**

目前仅支持在**北京、广州、上海、中国香港、新加坡、上海金融**地域创建多 AZ 存储桶，其他地域后续将陆续支持。

多 AZ 存储产生的存储容量费用比单 AZ 高，详情请参见各地域 [产品定价](https://cloud.tencent.com/document/product/436/6239)。

开启存储桶的多 AZ 配置后，不支持关闭。

## 使用场景

多 AZ 存储架构提供数据中心级别的容灾能力，以下是多 AZ 存储的几个使用场景：

**灾难恢复：**在发生自然灾害如地震、洪水等不可预测事件时，多 AZ 存储能够在不同地理位置的数据中心之间实现数据的自动备份和恢复，减少灾难带来的损失。

**高可用性应用：**对于电商平台、在线游戏、社交网络等需要保证高可用性的互联网服务，多 AZ 存储可以提供更稳定的服务，即使在某个数据中心出现问题时，也能快速切换到其他数据中心，保障用户体验。

**关键业务数据保护：**对于金融、医疗、政府等对数据安全性和业务连续性要求高的行业，多 AZ 存储可以确保在某个数据中心发生故障时，其他数据中心的数据依然安全、业务不中断。

## 优势介绍

当您将数据存储在多 AZ 地域时，数据会被打散成若干个分块，同时按照纠删码算法计算出对应的校验码分块。原始数据分块和校验码分块会被打散并均分存储到该地域的不同数据中心中，实现同城容灾。当某个数据中心不可用时，另外其他数据中心的数据依旧可以正常读取和写入，保障客户数据持久存储不丢失，维持客户业务数据连续性和高可用。使用对象存储多 AZ 具有以下优势：

**同城容灾**：提供跨数据中心的容灾。多 AZ 存储架构下，对象数据会被存储在同个地域不同数据中心的不同设备中。当一个数据中心出现故障时，冗余数据中心保持可用，用户业务不受影响，数据不丢失。

**稳定持久**：采用纠删码冗余存储的方式，提供了高达99.9999999999%的数据设计可靠性；数据分块存储，并发读写，提供高达99.995%的服务设计可用性。

**便捷易用**：通过对象存储类型指定您的数据存储于何种存储架构，您可以指定存储桶内的任意对象存储到多 AZ 架构中，让使用更为简单。

## 原理介绍

AZ 是 Availability Zone （可用区）的缩写，指的是云服务提供的在物理上隔离、电力和网络独立的区域。多个 AZ 之间互相独立，因此跨 AZ 部署能提高服务的可用性和容灾能力。

对于多 AZ 存储，COS 存储引擎部署在3个环境独立的 AZ 上。用户上传的数据将被切片存储在3个 AZ 的多个节点中。基于 EC 纠删码算法，原始数据会被切分为 N 个数据块，再由算法生成 M 个校验块，由此产生了多个存储分块。COS 将这些存储分块打散分布在3个 AZ 的不同机架服务器上，就实现了多 AZ 存储。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/ab4780ee5ce697f6455361e9b0da13fa.jpeg)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/ab4780ee5ce697f6455361e9b0da13fa.jpeg)

当机房故障导致部分节点、可用区损坏时，部分分块不可用，多 AZ 存储仍可以利用备 AZ 其他分块保证用户读、写数据成功，确保客户业务连续不中断。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/83f0815c0f2c8f866bcaaa044f6f95c3.jpeg)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/83f0815c0f2c8f866bcaaa044f6f95c3.jpeg)

## 多 AZ 存储和单 AZ 存储对比

多 AZ 存储和单 AZ 存储的 数据持久性、服务可用性、地域、存储类型对比和部分功能限制如下表所示。

**对比项****多 AZ 存储****单 AZ 存储****相关文档**
**数据设计持久性**99.9999999999% （12个9）99.999999999%（11个9）-
**服务设计可用性**高达99.995%高达99.99%-
**地域**当前仅支持北京、上海、广州、中国香港、新加坡、上海金融地域 全部地域-
**存储类型**标准存储（多 AZ）（MAZ_STANDARD）

低频存储（多 AZ）（MAZ_STANDARD_IA）

归档存储（多 AZ）（MAZ_ARCHIVE）

智能分层存储（多 AZ）（MAZ_INTELLIGENT_TIERING）标准存储（STANDARD）

低频存储（STANDARD_IA）

归档存储（ARCHIVE）

深度归档存储（DEEP_ARCHIVE）

智能分层存储（INTELLIGENT_TIERING）[存储类型概述](https://cloud.tencent.com/document/product/436/33417#.E5.AD.98.E5.82.A8.E7.B1.BB.E5.9E.8B.E5.AF.B9.E6.AF.94)
**功能限制****版本控制**开启版本控制后，不支持暂停 开启版本控制后，支持暂停[版本控制概述](https://cloud.tencent.com/document/product/436/19883)

[设置版本控制](https://cloud.tencent.com/document/product/436/19881)
**回收站**开启回收站后，不支持暂停 开启回收站后，支持暂停-
**对象锁定**当前暂不支持开启对象锁定 支持开启对象锁定，当前仅对白名单客户开放[对象锁定概述](https://cloud.tencent.com/document/product/436/55294)

[设置对象锁定](https://cloud.tencent.com/document/product/436/55293)
**批量处理**暂不支持批量恢复归档类型对象 支持批量数据复制、批量恢复归档类型对象、批量删除[批量处理概述](https://cloud.tencent.com/document/product/436/38601)

[批量处理](https://cloud.tencent.com/document/product/436/38605)
**Select**不支持 支持[Select 概述](https://cloud.tencent.com/document/product/436/37635)

[检索数据](https://cloud.tencent.com/document/product/436/37642)
**API**不支持用 JSON API 上传/下载对象，请升级至 XML API XML API、JSON API 均支持，推荐使用 XML API[API 文档简介](https://cloud.tencent.com/document/product/436/7751)

## 使用方法

用户可以为存储桶开启多 AZ 配置，在已开启多 AZ 配置的存储桶中上传对象，可以将对象的存储类型设置为多 AZ。用户在上传对象时，指定对象的存储类型即可将对象存放到多 AZ 存储架构中。 简而言之，您只需要执行以下两步即可将文件存储到多 AZ 架构中：

1. 创建存储桶，并在创建时开启多 AZ 配置。存储桶的创建指引，可参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。

2. 上传文件，并在上传时指定文件存储类型。文件的上传指引可参见 [上传对象](https://cloud.tencent.com/document/product/436/13321) 文档。

**说明：**

存储桶多 AZ 配置开启后，无法进行修改，请谨慎配置。原先已创建的存储桶默认未开启多 AZ 配置，仅新创建的存储桶可以开启。

如果您希望将存量数据存储于多 AZ 存储桶中，可以新建一个开启多 AZ 配置的存储桶，同时使用 COS Batch 的批量复制功能，将存量存储桶中的文件批量复制到新存储桶中。COS Batch 的使用指引，可参见 [批量处理](https://cloud.tencent.com/document/product/436/38605) 操作文档。
