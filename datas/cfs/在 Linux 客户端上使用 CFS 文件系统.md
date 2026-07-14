<!-- source: https://cloud.tencent.com/document/product/582/11523 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T19:02:24+08:00 -->

# 在 Linux 客户端上使用 CFS 文件系统

最近更新时间：2025-09-22 16:01:31


## 前提条件

创建文件系统前，确认已有可用的 VPC 及子网，建议设置 Linux 云服务器与 CFS 文件系统的 VPC 在同一可用区内，以降低网络延迟，获得更好的使用体验。若无 VPC 及子网，请参见 [快速配置私有网络](https://cloud.tencent.com/document/product/215/30716) 进行配置。

创建文件系统前，确认已有可用的 Linux云服务器，若无 Linux 云服务器，请参见 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936) 进行购买配置。登录 CVM 需要使用管理员账号（统一为 root，Ubuntu 系统用户为 ubuntu）和购买时设置的密码。

创建 CFS Turbo 文件系统，请参见 [在 Linux 客户端上使用 CFS Turbo 文件系统](https://cloud.tencent.com/document/product/582/54765) 进行配置。

## 操作步骤

### 步骤1：创建文件系统及挂载点

详细步骤请参见 [创建文件系统及挂载点](https://cloud.tencent.com/document/product/582/9132) 文档。

### 步骤2：连接实例

本部分操作介绍登录 Linux 云服务器的常用方法。此处介绍控制台登录，更多登录方式请参见 [登录 Linux 实例](https://cloud.tencent.com/doc/product/213/5436)。

1. 在 [云服务器](https://console.cloud.tencent.com/cvm/index) 列表的操作列，单击**登录**即可通过 VNC 连接至 Linux 云服务器。

2. 输入账号和密码即可登录。登录模式为独享，即同一时间只有一个用户可以使用控制台登录。

### 步骤3：验证网络通信

挂载前，确认客户端与文件系统网络是否连通。使用 telnet 命令验证，如 telnet 192.168.1.1 111。不同文件协议需要开放的端口如下表所示：

文件系统协议 客户端开放端口 确认特定端口连通性
NFS 3.0 111，892和2049 telnet <文件系统 IP 地址> 111

telnet <文件系统 IP 地址> 892

telnet <文件系统 IP 地址> 2049
NFS 4.0 2049 telnet <文件系统 IP 地址> 2049
SMB/CIFS 445 telnet <文件系统 IP 地址> 445

**说明：**

如果连接失败，请检查客户端安全组配置，确保已放通文件系统IP地址对应端口的出入方向流量，更多信息请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。

### 步骤4：挂载文件系统

#### 挂载 NFS 文件系统

通过控制台挂载

通过命令行挂载

您可以通过 CFS 控制台在云服务器上安装 NFS 客户端，并挂载相应的文件系统，具体操作步骤请参见 [使用控制台挂载文件系统](https://cloud.tencent.com/document/product/582/106911)。

1. 安装并启动 NFS 客户端。根据操作系统类型，使用以下命令在客户端安装 `nfs-utils` 或 `nfs-common`。

TencentOS、OpenCloudOS 及 CentOS：

sudo yum install nfs-utils

Ubuntu 及 Debian：

sudo apt-get install nfs-common

2. 创建待挂载目标目录。

mkdir <待挂载目标目录>

# mkdir /localfolder/

# mkdir -p /localfolder/test

3. 挂载文件系统。推荐使用 NFS 3.0协议挂载，以获得更好的性能。如果您的应用依赖文件锁，即需要使用多台云服务器同时编辑同个文件，请使用 NFS 4.0协议挂载。更多信息请参见 [NFS 客户端挂载参数说明](https://cloud.tencent.com/document/product/582/113840)。

# NFS 3.0 挂载根目录（推荐）：

sudo mount -t nfs -o vers=3,nolock,proto=tcp,noresvport <挂载点IP>:/<挂载点ID>/ /localfolder

# NFS 3.0 挂载子目录：

sudo mount -t nfs -o vers=3,nolock,proto=tcp,noresvport <挂载点IP>:/<挂载点ID>/subfolder /localfolder推荐

# NFS 4.0 挂载根目录：

sudo mount -t nfs -o vers=4.0,noresvport <挂载点IP>:/ /localfolder

# NFS 4.0 挂载子目录：

sudo mount -t nfs -o vers=4.0,noresvport <挂载点IP>:/subfolder /localfolder

挂载点 IP：指创建文件系统时，自动生成的挂载点 IP。

“localfolder” 指用户本地自己创建的目录；“subfolder” 指用户在 CFS 文件系统里创建的子目录。如不指定“subfolder ”，默认挂载的是文件系统的根目录`/`。 在文件系统中创建子目录后，可以挂载该子目录。

**注意：**

挂载命令可登录 [文件存储控制台 > 文件系统名称 > 挂载点信息](https://console.cloud.tencent.com/cfs) 一键复制。

由于部分旧版本文件系统不支持 noresvport 参数，挂载命令请以控制台显示为准。建议启用 noresvport，以便在网络重连时将使用新的 TCP 端口，保障在网络异常到恢复期间、客户端和文件系统的连接不会中断。

部分旧版本 Linux 内核需要使用 vers=4挂载，若使用 vers=4.0挂载有异常，可以尝试修改为 vers=4。

4. 查看挂载点信息。挂载完成后，请使用`mount -l`或`df -h`命令查看已挂载的文件系统：

# 列出当前已挂载的文件系统信息

mount -l

# 使用 grep 筛选相应的文件系统类型

mount -l | grep nfs

mount -l | grep lustre

# 查看磁盘空间使用情况

df -h

**注意：**

为避免后续误操作，非特殊需求情况下强烈建议不要对已挂载 CFS 文件系统或其他文件系统的目录重复执行挂载（mount）操作。

当待挂载目录存在重叠、包含关系，`df -h` 无法显示所有文件系统挂载结果，建议结合 `mount -l`，查看所有挂载点信息。

#### 挂载 SMB/CIFS 文件系统

通过控制台挂载

通过命令行挂载

您可以通过 CFS 控制台在云服务器上安装 SMB/CIFS 客户端，并挂载相应的文件系统，具体操作步骤请参见 [使用控制台挂载文件系统](https://cloud.tencent.com/document/product/582/106911)。

1. 安装并启动 CIFS 客户端。根据操作系统类型，使用以下命令在客户端安装`cifs-utils`或`nfs-common`。

TencentOS、OpenCloudOS 及 CentOS：

sudo yum install cifs-utils -y

Ubuntu 及 Debian：

sudo apt-get install cifs-utils -y

2. 创建待挂载目标目录。

mkdir <待挂载目标目录>

# mkdir /localfolder/

# mkdir -p /localfolder/test

3. 挂载文件系统。推荐使用 NFS 3.0协议挂载，以获得更好的性能。如果您的应用依赖文件锁，即需要使用多台云服务器同时编辑同个文件，请使用 NFS 4.0协议挂载。更多信息请参见 [NFS 客户端挂载参数说明](https://cloud.tencent.com/document/product/582/113840)。

# NFS 3.0 挂载根目录（推荐）：

sudo mount -t nfs -o vers=3,nolock,proto=tcp,noresvport <挂载点IP>:/<挂载点ID>/ /localfolder

# NFS 3.0 挂载子目录：

sudo mount -t nfs -o vers=3,nolock,proto=tcp,noresvport <挂载点IP>:/<挂载点ID>/subfolder /localfolder推荐

# NFS 4.0 挂载根目录：

sudo mount -t nfs -o vers=4.0,noresvport <挂载点IP>:/ /localfolder

# NFS 4.0 挂载子目录：

sudo mount -t nfs -o vers=4.0,noresvport <挂载点IP>:/subfolder /localfolder

挂载点 IP：指创建文件系统时，自动生成的挂载点 IP。

“localfolder” 指用户本地自己创建的目录；“subfolder” 指用户在 CFS 文件系统里创建的子目录。如不指定“subfolder”，默认挂载的是文件系统的根目录`/`。 在文件系统中创建子目录后，可以挂载该子目录。

**注意：**

挂载命令可登录 [文件存储控制台 > 文件系统名称 > 挂载点信息](https://console.cloud.tencent.com/cfs) 一键复制。

由于部分旧版本文件系统不支持 noresvport 参数，挂载命令请以控制台显示为准。建议启用 noresvport，以便在网络重连时将使用新的 TCP 端口，保障在网络异常到恢复期间、客户端和文件系统的连接不会中断。

部分旧版本 Linux 内核需要使用 vers=4挂载，若使用 vers=4.0挂载有异常，可以尝试修改为 vers=4。

4. 查看挂载点信息。挂载完成后，请使用 `mount -l` 或 `df -h` 命令查看已挂载的文件系统：

# 列出当前已挂载的文件系统信息

mount -l

# 使用 grep 筛选相应的文件系统类型

mount -l | grep nfs

mount -l | grep lustre

# 查看磁盘空间使用情况

df -h

**注意：**

为避免后续误操作，非特殊需求情况下强烈建议不要对已挂载 CFS 文件系统或其他文件系统的目录重复执行挂载（mount）操作。

当待挂载目录存在重叠、包含关系，`df -h` 无法显示所有文件系统挂载结果，建议结合 `mount -l`，查看所有挂载点信息。

### 步骤5：卸载共享目录

当某些情况下需要卸载共享目录，请使用如下命令。其中“localfolder” 指用户本地自己创建的用于挂载 CFS 文件系统的目录。

sudo umount /localfolder

### 步骤6：删除资源

**注意：**

文件系统删除后，资源不可恢复，建议您删除文件系统之前，使用快照功能备份资源。

您可以从腾讯云控制台删除文件系统。进入腾讯云 [文件存储控制台](https://console.cloud.tencent.com/cfs/fs)，选中需要删除的文件系统，单击**删除**并**确认**，即可删除文件系统。

## CFS 自助检测

当您遇到挂载失败，可以按照如下流程进行排查：

1. 登录挂载失败的云服务器，执行`mount -l`，确认当前已挂载的文件系统中不包含需要挂载的 CFS 文件系统。

2. 当报错为`mount.nfs: mount point /localfolder does not exist`，说明本地目录不存在，您可以创建本地目录，再重新执行挂载命令。

3. 当报错为`mount.nfs: mounting 10.xxx.xxx.xxx:/abcdefgh/subfolder failed, reason given by server: No such file or directory`，说明 CFS 文件系统中并不存在指定的子目录，您可以先挂载根目录`/`，挂载成功后创建子目录，再重新挂载子目录。

4. 当报错为`mount.nfs: Connection timed out`，您可以在控制台使用 [CFS 自助检测](https://console.cloud.tencent.com/cfs/) 功能，选择需要挂载的云服务器及对应的 CFS 文件系统，执行检测，根据检查报告对操作系统内核、网络、端口、权限组等进行排查。如您无法自助解决相关问题，请及时通过 [工单系统](https://console.cloud.tencent.com/workorder/category?level1_id=83&level2_id=458&source=14&data_title=%E6%96%87%E4%BB%B6%E5%AD%98%E5%82%A8&step=1) 进行反馈。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/ff266dd60aa864d387312a560e457b72.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/ff266dd60aa864d387312a560e457b72.png)
