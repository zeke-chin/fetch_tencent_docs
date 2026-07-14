<!-- source: https://cloud.tencent.com/document/product/582/11524 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T19:02:21+08:00 -->

# 在 Windows 客户端上使用 CFS 文件系统

最近更新时间：2026-04-09 14:25:38


## 前提条件

创建文件系统前，确认已有可用的 VPC 及子网，建议设置 Windows 云服务器与 CFS 文件系统的 VPC 在同一可用区内，以降低网络延迟，获得更好的使用体验。若无 VPC 及子网，请参见 [快速配置私有网络](https://cloud.tencent.com/document/product/215/30716) 进行配置。

创建文件系统前，确认已有可用的 Windows 云服务器。若无，请参见 [快速配置 Windows 云服务器](https://cloud.tencent.com/document/product/213/2764) 进行购买配置。登录云服务器需要使用管理员账号（统一为 Administrator）和购买时设置的密码。

Turbo 系列文件系统暂不支持 Windows 操作系统云服务器挂载，只支持 Linux 操作系统云服务器挂载。如您想了解，请参见 [在 Linux 客户端上使用 CFS Turbo 文件系统](https://cloud.tencent.com/document/product/582/54765)。

## 操作步骤

### 步骤1：创建文件系统及挂载点

详细步骤请参见 [创建文件系统及挂载点](https://cloud.tencent.com/document/product/582/9132)。

### 步骤2：连接实例

[使用标准方式登录 Windows 实例](https://cloud.tencent.com/document/product/213/57778)，如需使用其他登录方式，请参见 [登录 Windows 实例](https://cloud.tencent.com/document/product/213/35703)。

### 步骤3：验证网络通信

挂载前，需确认客户端与文件系统网络是否连通。在 Windows 客户端启用 Telnet 服务，通过 telnet 命令验证（例如 telnet 192.168.1.1 445），不同文件协议需要开放的端口如下表所示：

文件系统协议 客户端开放端口 确认网络连通性
NFS 3.0 111、892、2049 telnet <文件系统 IP 地址> 111

telnet <文件系统 IP 地址> 892

telnet <文件系统 IP 地址> 2049
CIFS/SMB 445 telnet <文件系统 IP 地址> 445

**说明：**

Windows 暂时不支持使用 NFSv4协议挂载。如果连接失败，请检查客户端安全组配置，确保已放通文件系统 IP 地址对应端口的出入方向流量，更多信息请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。

### 步骤4：挂载文件系统

**说明：**

推荐 Windows 客户端使用 SMB 协议挂载文件系统，Linux 客户端使用 NFS 协议挂载文件系统。

#### 挂载 SMB 文件系统

通过 CFS 控制台挂载

通过命令行挂载

通过图形界面挂载

您可以通过 CFS 控制台在云服务器上安装 SMB 客户端，并挂载相应的文件系统，具体操作步骤请参见 [使用控制台挂载文件系统](https://cloud.tencent.com/document/product/582/106911)。

1. 允许 Guest 访问 SMB 协议文件系统。如果您是首次挂载，且操作系统为 Win10 、 Windows Server 2019及更高版本，请以管理员身份使用 cmd 或 PowerShell 运行以下内容修改注册表，等待服务完全重启，再执行第2步；如果您的操作系统为 Win Server 2016或更早的版本，可直接跳到第2步。

**PowerShell**

reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" /v "AllowInsecureGuestAuth" /t REG_DWORD /d 1 /f

reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" /v "RequireSecuritySignature" /t REG_DWORD /d 0 /f

net stop lanmanworkstation /y ; net start lanmanworkstation ; net start SessionEnv

**cmd**

reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" /v "AllowInsecureGuestAuth" /t REG_DWORD /d 1 /f && reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" /v "RequireSecuritySignature" /t REG_DWORD /d 0 /f && net stop lanmanworkstation /y && net start lanmanworkstation && net start SessionEnv

**说明：**

Win10、Windows Server 2019及更高版本的操作系统，需要允许 Guest 访问 SMB。关于此权限相关的改变，微软官方说明如下：[Guest access in SMB2 disabled by default in Windows](https://learn.microsoft.com/en-us/windows-server/storage/file-server/enable-insecure-guest-logons-smb2-and-smb3?tabs=group-policy) 和 [Overview of Server Message Block signing](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/overview-server-message-block-signing#policy-locations-for-smb-signing)。

2. 挂载文件系统。以管理员身份打开 cmd 命令行工具，使用以下命令挂载文件系统。

net use <需要挂载的盘符>: \\<挂载点IP地址>\<挂载点ID>

:: net use x: \\192.xxx.xxx.xxx\abcdefgh

**注意：**

挂载命令可在 [文件存储控制台 > 文件系统 ID > 文件系统挂载点](https://console.cloud.tencent.com/cfs) 页面一键复制，默认挂载盘符为“ x: ”，您可根据需要进行替换。

共享目录名称与挂载点外网 IP 地址之间有一个空格，注意不要遗漏。

3. 验证读写正确性。查看**文件管理器**>**此电脑**，当**网络位置**显示为下图，说明已连接到 CFS 文件系统。进入文件系统中新建文件，验证读写的正确性。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/a39ae7809c146b41e99994a1e702dccf.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/a39ae7809c146b41e99994a1e702dccf.png)

1. 单击

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/b9a64b8d69f6b1fdc1003f337f12e2ce.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/b9a64b8d69f6b1fdc1003f337f12e2ce.png)

，进入开始菜单界面。

2. 搜索“此电脑”，单击右键，选择**映射网络驱动器**。

3. 在弹出的窗口中，选择“驱动器”盘符，在“文件夹”填写`\\<挂载点 IP 地址>\<挂载点 ID>` ，单击**完成**。

**注意：**

`\\<挂载点 IP 地址>\<挂载点 ID>` 可在 [文件存储控制台 > 文件系统 ID > 文件系统挂载点](https://console.cloud.tencent.com/cfs) 页面复制。

建议勾选登录时重新连接，避免重启机器或重新登录后出现断连。

4. 查看**文件管理器**>**此电脑**，当**网络位置**显示为下图，说明已连接到 CFS 文件系统。进入文件系统中新建文件并写入数据，验证读写的正确性。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/a39ae7809c146b41e99994a1e702dccf.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/a39ae7809c146b41e99994a1e702dccf.png)

#### 挂载 NFS 文件系统

通过 CFS 控制台挂载

通过命令行挂载

通过图形界面挂载

您可以通过 CFS 控制台在云服务器上安装 NFS 客户端，并挂载相应的文件系统，具体操作步骤请参见 [使用控制台挂载文件系统](https://cloud.tencent.com/document/product/582/106911)。

1. 开启 NFS 服务。以管理员身份使用 PowerShell 执行以下命令开启 NFS 服务。

Install-WindowsFeature -Name NFS-Client

2. 验证 NFS 服务是否启用。使用 cmd 执行 `mount -h` 验证服务是否启用，若返回 NFS 相关信息，则表示 NFS 客户端正常运行中。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/7f6a0362e92f6c11df3a62e7e6822454.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/7f6a0362e92f6c11df3a62e7e6822454.png)

3. 添加匿名用户和用户组。以管理员身份运行 cmd，执行如下指令，修改注册表，允许匿名用户/用户组访问，并将 mount 的 Lock 参数置为1。

reg add "HKLM\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Users\Default\Mount" /v Locking /t REG_DWORD /d 1 /f && reg add "HKLM\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Users\Default\Mount" /v AnonymousGID /t REG_DWORD /d 0 /f && reg add "HKLM\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Users\Default\Mount" /v AnonymousUID /t REG_DWORD /d 0 /f && reg add "HKLM\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default" /v AnonymousGID /t REG_DWORD /d 0 /f && reg add "HKLM\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default" /v AnonymousUID /t REG_DWORD /d 0 /f

4. 生效注册表。执行如下命令，重启 NFS 客户端服务，使修改的注册表生效。您也可通过重启 Windows 系统，使修改的注册表生效。

net stop nfsclnt && net stop nfsrdr && net start nfsrdr && net start nfsclnt

**注意：**

重启服务因 Windows 操作系统自身的问题，有概率使注册表并未完全更新生效，优先建议您进行重启机器的操作。

5. 挂载文件系统。以管理员身份打开 cmd 命令行工具，使用以下命令挂载文件系统。

:: 通用标准型/通用性能型NFS协议挂载命令

mount -o nolock mtype=hard <挂载点IP地址>:/<挂载点ID> <需要挂载的盘符>:

:: 例如：mount -o nolock mtype=hard 10.xxx.xxx.xxx:/abcdefgh x:


:: 通用标准型（增强型）/通用性能型（增强型）挂载命令

mount -o nolock mtype=hard <挂载点IP地址>:/! <需要挂载的盘符>:

:: mount -o nolock mtype=hard 172.xxx.xxx.xxx:/! x:

**注意：**

挂载命令可登录 [文件存储控制台 > 文件系统 ID > 文件系统挂载点](https://console.cloud.tencent.com/cfs) 页面一键复制，默认挂载盘符为“ x: ”，您可根据需要进行替换。

Windows 系统仅支持通过 NFS 协议挂载通用标准型（增强型）和通用性能型（增强型）存储类型，执行挂载命令时，无需拼接挂载点 ID，而使用英文感叹号“!”作为占位符。

6. 验证读写正确性。查看**文件管理器**>**此电脑**，当**网络位置**显示为下图，说明已连接到 CFS 文件系统。进入文件系统中新建文件，验证读写的正确性。

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/365f5e25d21ae801cfaaf7165fd15abd.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/365f5e25d21ae801cfaaf7165fd15abd.png)

1. 开启 NFS 服务。登录云服务器，单击

![Image 12](https://qcloudimg.tencent-cloud.cn/image/document/a6ffd38d6fced00789c2d77ee6e543d3.png)

![Image 13](https://qcloudimg.tencent-cloud.cn/image/document/a6ffd38d6fced00789c2d77ee6e543d3.png)

 ，选择**控制面板**>**程序-启用或关闭 Windows 功能**>**添加角色和功能**。在弹出的**添加角色和功能向导**窗口，保持默认配置，单击**下一页**直到**功能**界面，勾选 **NFS 客户端**，单击**下一页**。在**确认**界面单击**安装**。

![Image 14](https://qcloudimg.tencent-cloud.cn/image/document/14b40c1e764cafd77bdc310fb12c229b.png)

![Image 15](https://qcloudimg.tencent-cloud.cn/image/document/14b40c1e764cafd77bdc310fb12c229b.png)

**说明：**

Windows 家庭版不包含 NFS 客户端选项，请使用 Windows Server 版操作系统或 Windows 专业版。

如您此前开启过 NFS 服务，可跳过此步骤。

2. 验证 NFS 服务是否启用。使用 cmd 执行 `mount -h` 验证 NFS 服务是否启动。若返回 NFS 相关信息则表示 NFS 客户端正常运行中。

![Image 16](https://qcloudimg.tencent-cloud.cn/image/document/d22b2d4d451ca57b014ae5cbea20ecfe.png)

![Image 17](https://qcloudimg.tencent-cloud.cn/image/document/d22b2d4d451ca57b014ae5cbea20ecfe.png)

3. 添加匿名用户和用户组。以管理员身份运行 cmd，执行如下指令，修改注册表，允许匿名用户/用户组访问，并将 mount 的 Lock 参数置为1。

reg add "HKLM\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Users\Default\Mount" /v Locking /t REG_DWORD /d 1 /f && reg add "HKLM\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Users\Default\Mount" /v AnonymousGID /t REG_DWORD /d 0 /f && reg add "HKLM\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Users\Default\Mount" /v AnonymousUID /t REG_DWORD /d 0 /f && reg add "HKLM\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default" /v AnonymousGID /t REG_DWORD /d 0 /f && reg add "HKLM\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default" /v AnonymousUID /t REG_DWORD /d 0 /f

4. 生效注册表。执行如下命令，重启 NFS 客户端服务，使修改的注册表生效。您也可通过重启 Windows 系统，使修改的注册表生效。

net stop nfsclnt && net stop nfsrdr && net start nfsrdr && net start nfsclnt

**注意：**

重启服务因 Windows 操作系统自身的问题，有概率使注册表并未完全更新生效，优先建议您进行重启机器的操作。

5.  在弹出的窗口中，选择“驱动器”盘符，在“文件夹”填写`\\<挂载点 IP 地址>\<挂载点 ID>` ，单击**完成**。

**注意：**

`\\<挂载点 IP 地址>\<挂载点 ID>` 可登录 [文件存储控制台 > 文件系统 ID > 文件系统挂载点](https://console.cloud.tencent.com/cfs) 页面获取，需要在格式上略作调整。例如，挂载命令为 mount -o nolock mtype=hard 10.xxx.xxx.xxx:/abcdefgh x: 时，挂载点 IP 地址为 10.xxx.xxx.xxx，挂载点 ID 为 abcdefgh，则拼接后“文件夹”处应填写`\\10.xxx.xxx.xxx\abcdefgh`。

建议勾选登录时重新连接，避免重启机器或重新登录后出现断连。

6. 验证读写正确性。查看**文件管理器**>**此电脑**，当网络位置显示为下图，说明已连接到 CFS 文件系统。进入文件系统中新建文件，验证读写的正确性。

![Image 18](https://qcloudimg.tencent-cloud.cn/image/document/d3cdf38f17ff1a33c71151ec4acad2da.png)

![Image 19](https://qcloudimg.tencent-cloud.cn/image/document/d3cdf38f17ff1a33c71151ec4acad2da.png)

### 步骤5：卸载文件系统

通过命令行卸载

通过图形界面卸载

如果您需要卸载文件系统，以管理员身份使用 cmd 执行如下命令。其中 "目录名称" 为挂载的盘符（如“ x: ”），或者文件系统的完整路径。

**卸载 SMB 文件系统**：

`net use x: /del`

**卸载 NFS 文件系统**：

sudo umount x:

如果您需要卸载文件系统，断开连接，只需鼠标右键单击对应的盘，在菜单中单击**断开连接**，即可断开文件系统的连接。

![Image 20](https://qcloudimg.tencent-cloud.cn/image/document/ec6d4f4caa2aab1ba8f0247d449cfa4d.png)

![Image 21](https://qcloudimg.tencent-cloud.cn/image/document/ec6d4f4caa2aab1ba8f0247d449cfa4d.png)

### 步骤6：删除资源

**注意：**

文件系统删除后，资源不可恢复，建议您删除文件系统之前，使用快照备份资源。

您可以从腾讯云控制台删除文件系统。进入腾讯云 [文件存储控制台](https://console.cloud.tencent.com/cfs/fs)，选中需要删除的文件系统，单击**删除**并**确认**，即可删除文件系统。

## 常见问题

### Telnet 不是内部或外部命令，也不是可执行的程序或批处理文件

**原因**：Telnet 服务未启用。

**解决方法**：打开**控制面板**>**程序-启用或关闭 Windows 功能**>**添加角色和功能**，保持默认设置，单击**下一步**直到**功能**界面，找到并勾选 **Telnet Client**选项，等待安装完成即可。

![Image 22](https://qcloudimg.tencent-cloud.cn/image/document/d4e9e226a64ab3082b1e4f9b508240cb.png)

![Image 23](https://qcloudimg.tencent-cloud.cn/image/document/d4e9e226a64ab3082b1e4f9b508240cb.png)

### 挂载 NFS/SMB 文件系统，发生系统错误：53

**原因**：未找到网络路径

网络未连通。

注册表未正确配置 Workstation 或 Lanmanworkstation。

**解决方法**：

执行 `ping <文件系统 IP 地址>` 判断网络是否连通，执行 `telnet <文件系统 IP 地址> {特定端口：NFS：111、892、2049；SMB：445}` 判断 NFS/SMB 服务是否可用。

若网络未连通，请检查云服务器和文件系统实例是否在同一个 VPC 中，VPC 路由表及子网 ACL 规则是否双向放开。

若端口未连通，请检查云服务器安全组以及 CFS 实例权限组是否双向放开对应端口。

排除网络问题后检查注册表编辑器：

挂载 SMB 协议文件系统，请导航到 HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters。其中 AllowInsecureGuestAuth 应该显示值为1；RequireSecuritySignature 应该显示值为0。如不是，请修改，必要时请通过重启机器使注册表生效。

挂载 NFS 协议文件系统，请导航到 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Users\Default\Mount。其中 Locking 应该显示值为1；AnonymousGID 和 AnonymousUID 应显示值为0。如不是，请修改，必要时请通过重启机器使注册表生效。

上述情况均无问题，请检查是否是 Windows 防火墙，在保证网络安全前提下，关闭防火墙后再次尝试挂载。

### 挂载 NFS/SMB 文件系统，发生系统错误：85

**原因**：本地设备名（目标盘符）已在使用中。

**解决方法**：请更换目标盘符后重新挂载。

### 挂载 NFS/SMB 文件系统，发生系统错误：1272或在文件系统中创建文件提示无权限操作

![Image 24](https://qcloudimg.tencent-cloud.cn/image/document/4f54963f6fe63d9b064057020cf28ea5.png)

![Image 25](https://qcloudimg.tencent-cloud.cn/image/document/4f54963f6fe63d9b064057020cf28ea5.png)

**原因**：Win10 或 Windows Server 2019及更高版本的操作系统，需要允许 Guest 访问 SMB/NFS。

**解决方法**：参考系统错误53检查注册表是否生效，若未生效，请修改注册表。

SMB 文件系统：修改注册表允许 Guest 访问 SMB，请参见 [挂载 SMB 文件系统-通过命令行挂载](https://cloud.tencent.com/document/product/582/11524#JKLix2vXZQpVhHsZRinE3) 中的步骤1 。

NFS 文件系统：修改注册表允许匿名用户/用户组访问 NFS，请参见 [挂载 NFS 文件系统-通过命令行挂载](https://cloud.tencent.com/document/product/582/11524#SHcmcgGSr19I_DoqXm8pS) 中的步骤3。

### 手动挂载 NFS 文件系统后，挂载能够成功，但是显示红叉，访问速度非常慢，且无法断连

![Image 26](https://qcloudimg.tencent-cloud.cn/image/document/d7ea8ed51ed3b206c24ca75986b36279.png)

![Image 27](https://qcloudimg.tencent-cloud.cn/image/document/d7ea8ed51ed3b206c24ca75986b36279.png)

**原因**：Windows 资源管理器会定期检测网络驱动器状态，若 NFS 响应延迟过长，可能误判为断开。

**解决方法**：

Windows 建议挂载 SMB 协议文件系统；若必须使用 NFS 协议文件系统，建议使用控制台方式重新挂载。

无法断连问题可通过重启机器解决。
