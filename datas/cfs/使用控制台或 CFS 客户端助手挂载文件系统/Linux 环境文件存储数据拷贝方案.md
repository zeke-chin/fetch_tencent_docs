<!-- source: https://cloud.tencent.com/document/product/582/83114 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T22:09:25+08:00 -->

# Linux 环境文件存储数据拷贝方案

最近更新时间：2026-03-04 15:41:38


## 使用场景

在日常文件存储使用中，频繁的数据拷贝是常见需求。为提升操作效率，本文将介绍如何在 Linux 操作系统下，快速进行数据拷贝的推荐方案。

**场景一：CFS 文件系统之间、文件系统内不同目录、文件系统和云硬盘间的数据同步**。

**方法一**：当需要详细的过程报告和可视化的操作界面时，推荐使用 [腾讯云云迁移 CMG - 文件存储批量迁移](https://cloud.tencent.com/document/product/659/116592)。云迁移服务支持可视化图表实时查看迁移进度，支持跨时段分批次迁移、定时迁移等，相较于使用 rclone 更加便捷友好。

**方法二**：对于少量文件的简单拷贝，使用 cp 命令即可高效完成。当处理海量文件时，cp 命令单线程的运行模式会成为性能瓶颈，显著降低拷贝效率。因此，本文推荐采用更具优势的 rclone 并发拷贝方案，可自动利用系统资源实现拷贝加速，详情请参见 [操作说明](https://cloud.tencent.com/document/product/582/83114#.E6.93.8D.E4.BD.9C.E8.AF.B4.E6.98.8E)。

**场景二：主流云厂商与腾讯云 CFS 文件系统之间、腾讯云不同账号下 CFS 文件系统之间的数据同步。**

**方法**：当您需要将阿里云、华为云、AWS 等其他云厂商的文件系统数据迁移至腾讯云 CFS 文件系统，或者在腾讯云不同账号下的 CFS 文件系统之间进行数据同步，推荐使用 [腾讯云云迁移 CMG - 文件存储批量迁移](https://cloud.tencent.com/document/product/659/116592)。

**场景三：文件系统与对象存储之间的数据同步。**

**方法一**：当涉及需要将文件存储 CFS 和对象存储进行数据拷贝，可使用 [数据迁移服务](https://cloud.tencent.com/document/product/582/80360)。此服务仅支持对象存储数据迁移至文件存储 CFS 中，如需文件传输到对象存储，可参考方法二。

**方法二**：可使用对象存储提供的各类基础工具进行数据上传、下载的操作。推荐使用的工具链接如下：[COSBrowser](https://cloud.tencent.com/document/product/436/11366)、[COSCMD](https://cloud.tencent.com/document/product/436/10976)。

## 操作说明

此操作步骤面向场景一的方法二，其余场景和方法可参考上述链接进行操作。

### 注意事项

rclone 是一款高效的跨平台与云存储数据迁移工具，但其核心功能是传输文件内容与部分元数据，不能用于保留或还原 Unix 文件所有权（UID/GID）。如需完整保留包括权限、ACL 等在内的所有 POSIX 元数据，建议您使用 cp -a、rsync -a 或 tar 等专门工具。

rclone 不保留文件所有权与用户/组信息。当您从 Linux/Unix 系统向文件存储迁移数据时，文件的原始“属主”信息会丢失。在目标端，所有文件都会显示为执行 rclone 命令的用户所有。如果您迁移的是多用户环境下的数据（如 /home 目录），这将导致权限混乱，后续需手动重新分配所有权。

rclone 没有通用机制来保留或还原以下安全与权限属性，因此不应依赖它来完成此类迁移：

POSIX 文件权限位：文件的标准读写执行（rwx）权限。

扩展属性：如访问控制列表（ACL）、SELinux 安全上下文以及其他扩展属性（xattr）。这意味着依赖严格权限控制（如600）的配置文件，其安全状态在迁移后可能失效。

rclone 通常会尽力保留文件的修改时间，不保留访问时间。如果您的业务逻辑对文件时间戳有精确依赖，请在迁移后进行验证。

rclone 对符号链接的处理根据操作场景有所不同，此行为差异源于跨网络拷贝时链接目标路径可能失效的假设，详情请参见 [rclone options](https://rclone.org/commands/rclone/)。

单主机挂载迁移场景：当一台主机同时挂载源文件系统与目标文件系统并进行数据迁移时，符号链接将被保持为其原始链接形式。

双主机跨地域拷贝场景：两台主机分别挂载位于不同地域的源文件系统与目标文件系统，并通过网络使用 rclone 进行数据拷贝。在该场景下，源端的符号链接传输至目标端后，将转变为以 .rclonelink为后缀的普通文件。此类场景常见于将本地文件存储数据迁移至云上 CFS 文件存储的场景，通常需借助专线、对等连接或云联网等方式打通云上服务器与本地服务器之间的网络。

### 前置条件

在通过 rclone 进行迁移前，需确保云服务器上已存在可供迁移的源端与目标端目录。若源端 CFS 与目标端 CFS（或 CFS 与 CVM）位于不同 VPC 中，您可借助 [云联网](https://cloud.tencent.com/document/product/877/18768) 服务实现跨 VPC 网络互通，从而完成跨 VPC 的目录挂载与访问。此步骤为跨 VPC 迁移的必要前提。

### 操作步骤

1. 下载安装 rclone 工具。

**方法一**：通过腾讯云镜像服务下载（**推荐**）：

**注意：**

因涉及到请求腾讯云内网的镜像源，仅腾讯云的云服务器可使用，通过此方式的下载速度会快于从官网直接下载。

wget http://mirrors.tencentyun.com/install/cfsturbo-client//migrate_tools/rclone-v1.70.1-linux-amd64.zip && unzip rclone-v1.70.1-linux-amd64.zip && chmod 0755 ./rclone-*/rclone && cp ./rclone-*/rclone /usr/bin/ && rm -rf ./rclone-*

**方法二**：通过官网链接下载安装：

wget https://downloads.rclone.org/v1.70.1/rclone-v1.70.1-linux-amd64.zip --no-check-certificate && unzip rclone-v1.70.1-linux-amd64.zip && chmod 0755 ./rclone-*/rclone && cp ./rclone-*/rclone /usr/bin/ && rm -rf ./rclone-*

2. 执行命令，进行数据同步。

rclone copy /mnt/src /mnt/dst -Pvv --transfers 32 --metadata --checkers 64 --links --create-empty-src-dirs --retries=3 --modify-window=1s

若需要后台拷贝可参考如下指令：

nohup rclone copy /mnt/src /mnt/dst -vv --transfers 32 --checkers 64 --links --create-empty-src-dirs --retries 3 --modify-window=1s >> /path/to/copy.log

**说明：**

1.  参数说明如下，transfers 和 checkers 数目可以根据系统规格自行配置：

transfers：传输文件的并发数量（建议不超过核心数的2倍）。

checkers：扫描本地文件的并发数量（建议不超过核心数的2倍）。

P：实时展示数据拷贝进度（500ms，若不加则为1分钟刷新一次）。

links：复制软链接。

metadata：复制文件和目录的元数据信息

vv：打印拷贝日志。

create-empty-src-dirs：针对空目录也执行拷贝。

retries：对失败的拷贝进行自动重试的次数（可根据实际需要调整数值）。

modify-window=1s：rclone 默认先根据文件大小、名称和 mtime 等元数据信息比对，若出现不一致再进行 MD5 值比对。此参数将 mtime 的变化容忍度设置为1s(若不设置默认为1ns)。因 Turbo 文件系统 mtime 的精度为秒级，如果涉及到拷贝到 Turbo 文件系统，为降低不必要的 MD5 比对，建议加上此参数。

2. 此工具重复运行可自动进行增量同步，识别增量的方式为全局扫描。

3. 等待数据完成同步后，可通过日志查看不同文件的迁移任务结果。
