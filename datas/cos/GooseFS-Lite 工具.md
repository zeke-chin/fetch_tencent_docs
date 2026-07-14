<!-- source: https://cloud.tencent.com/document/product/436/115507 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:14:33+08:00 -->

# GooseFS-Lite 工具

最近更新时间：2026-04-17 15:50:22


## 功能说明

GooseFS-Lite 工具支持将 [对象存储（Cloud Object Storage，COS）](https://cloud.tencent.com/product/cos)存储桶挂载到本地，像使用本地文件系统一样直接操作腾讯云对象存储中的对象，相比于 COSFS 工具，GooseFS-Lite 可提供更高的大文件读写速度，不受本地磁盘的性能限制。GooseFS-Lite 支持 POSIX 文件系统的主要功能，例如文件顺序、随机读，顺序写、目录操作等功能。

## 使用限制

**GooseFS-Lite 仅适合挂载后对文件进行简单的管理，不支持本地文件系统的一些功能用法。**请注意以下使用限制：

不支持对文件进行随机写和 truncate 操作。

多个客户端挂载同一个 COS 存储桶时，依赖用户自行协调多个客户端的行为。例如避免多个客户端写同一个文件等。

文件/文件夹的 rename 操作非原子操作。

不支持读取和 rename 当前挂载点正在写入的文件。

元数据操作如 list directory，性能较差，因为需要远程访问 COS 服务器。

不支持 soft/hard link。

追加写性能较差，涉及服务端数据拷贝和下载被追加文件。

不建议在小内存场景使用，例如在容器内存或者 CVM 内存小于2G的情况。

容器环境目前只支持 [腾讯云容器服务（Tencent Kubernetes Engine，TKE）](https://cloud.tencent.com/product/tke)内使用，非 TKE 容器暂不支持。

不建议在大量随机读且对性能有较高要求的场景中使用。

**注意：**

外网挂载和非低频存储的追加写操作，会产生下载流量费用。

## 使用环境

[KonaJDK 11](https://github.com/Tencent/TencentKona-11/wiki/Installation-Guide)

Linux X86_64

## 使用方法

### 步骤1：安装依赖

#### **CentOS/TencentOS Server**

yum install -y fuse-devel

#### **Ubuntu**

apt install -y libfuse-dev

#### 其他 Linux 发行版

编译安装 libfuse 2.9.7

wget "https://github.com/libfuse/libfuse/releases/download/fuse-2.9.7/fuse-2.9.7.tar.gz"

tar xvf fuse-2.9.7.tar.gz

cd fuse-2.9.7

./configure

make -j8

make install

### 步骤2：安装 GooseFS-Lite

将 GooseFS-Lite 安装到当前目录，并将 `goosefs-lite` 软链到 `/usr/bin/goosefs-lite`，方便后续直接使用 goosefs-lite 命令。

curl -fssL https://downloads.tencentgoosefs.cn/goosefs-lite/install.sh | sh -x

cd goosefs-lite-*

sudo bash bin/install.sh

### 步骤3：安装 KonaJDK11

在 `goosefs-lite-<具体版本号>` 目录下（以1.0.6版本为例，在 `goosefs-lite-1.0.6` 目录下）使用如下命令安装 KonaJDK 到 **/usr/local/konajdk11**下：

sudo bash bin/install-jdk.sh https://github.com/Tencent/TencentKona-11/releases/download/kona11.0.22/TencentKona-11.0.22.b1-jdk_linux-x86_64.tar.gz

如下所示，有两种方式可以选择：

一：使用 KonaJDK 的下载链接，二：将自行下载 KonaJDK 安装包到指定目录。使用如下命令安装，即可让 goosefs-lite 自动使用该 Java 运行环境。

Usage:

Command: install-jdk.sh http[s]://host/path

Example: install-jdk.sh https://github.com/Tencent/TencentKona-11/releases/download/kona11.0.22/TencentKona-11.0.22.b1-jdk_linux-x86_64.tar.gz

or

Command: install-jdk.sh /path/to/jdk.tar.gz

Example: install-jdk.sh /Downloads/TencentKona-11.0.22.b1-jdk_linux-x86_64.tar.gz

如果希望更灵活地安装 Java 环境，可以参考 [手动安装 JDK](https://github.com/Tencent/TencentKona-11/wiki/Installation-Guide)。并在 **conf/goosefs-env.sh**中修改环境变量使其生效。

### 步骤4：修改配置文件

在 `goosefs-lite-<具体版本号>` 目录下（以1.0.6版本为例，在 `goosefs-lite-1.0.6` 目录下）修改配置文件有以下两种方式：

使用 sed 修改以下三个参数，其中 SECRET_ID、SECRET_KEY 和 REGION 按照实际填写：

将 fs.cosn.userinfo.secretKey 配置为腾讯云密钥 Key。

将 fs.cosn.userinfo.secretId 配置为腾讯云密钥 ID。

将 fs.cosn.bucket.region 配置为存储桶地域。

sed -i '/<name>fs.cosn.userinfo.secretId<\/name>/{N;s/<value>[^<]*<\/value>/<value>$SECRET_ID<\/value>/}' conf/core-site.xml

sed -i '/<name>fs.cosn.userinfo.secretKey<\/name>/{N;s/<value>[^<]*<\/value>/<value>$SECRET_KEY<\/value>/}' conf/core-site.xml

sed -i '/<name>fs.cosn.bucket.region<\/name>/{N;s/<value>[^<]*<\/value>/<value>$REGION<\/value>/}' conf/core-site.xml

也可使用 vim 编辑 conf/core-site.xml 文件，修改参数。

将 fs.cosn.userinfo.secretKey 配置为腾讯云密钥 Key。

将 fs.cosn.userinfo.secretId 配置为腾讯云密钥 ID。

将 fs.cosn.bucket.region 配置为存储桶地域。

#### 配置文件描述

在 `goosefs-lite-<具体版本号>/conf` 目录下（以1.0.6版本为例，在 `goosefs-lite-1.0.6/conf` 目录下），可以看到以下文件：

**acl-site.properties**：指定**目录**的权限、用户名、组名、类似 Linux POSIX 语义的0755、uid、gid 等。

**说明：**

acl-site 配置的格式为 `path=mode:user_name:group_name`，例如要给 /mnt/goosefs-lite/test_dir 路径配置 755 mode、root 用户、root 用户组，则在配置文件中配置 `/mnt/goosefs-lite/test_dir=755:root:root` 即可。

如需使用 ACL 配置，需要在挂载时携带 `-o default_permissions` 参数，由内核（VFS）​ 基于文件元数据的 mode/uid/gid 做标准 Unix 权限检查。同时，需要在挂载前在 **goosefs-lite.properties**配置文件中修改或增加配置项 `goosefs.lite.posix.acl.manager.enabled` 为 `true`。例如将 testbucket-1250000000挂载至 /mnt/datadisk0/goosefs-lite-mnt 的命令如下：`./bin/goosefs-lite mount -o "allow_other,default_permissions" /mnt/datadisk0/goosefs-lite-mnt cosn://testbucket-1250000000/`

**core-site.xml**：Hadoop-COS 的配置文件（goosefs-lite 的数据流基于 Hadoop-COS，因此参数和配置文件几乎通用）

**goosefs-env.sh**：各类环境变量，如 JVM 参数等。

**goosefs-lite.properties**：goosefs-lite 相关配置。

**log4j.properties**：日志配置。如需要开启 debug 日志，可取消注释该文件最后一行，重新挂载即可。

**注意：**

建议用户尽量避免在配置中使用永久密钥，采取配置子账号密钥或者临时密钥的方式有助于提升业务安全性。为子账号授权时建议按需授权子账号可执行的操作和资源，避免发生预期外的数据泄露。

如果您一定要使用永久密钥，建议对永久密钥的权限范围进行限制，可通过限制永久密钥的可执行操作、资源范围和条件（访问 IP 等），提升使用安全性。

### 步骤5：将存储桶挂载到本地目录

在 `goosefs-lite-<具体版本号>` 目录下（以1.0.6版本为例，在 `goosefs-lite-1.0.6` 目录下）执行如下命令，将密钥文件中配置的存储桶挂载到指定目录：

 ./bin/goosefs-lite mount <MountPoint> cosn://<BucketName>/

其中：

<MountPoint> 为本地挂载目录（例如 `/mnt/goosefs-lite-mnt-dir`），此目录必须为空，否则无法挂载。

<BucketName> 为存储桶名称（例如 examplebucket-1250000000）。

**示例：**

mkdir -p /mnt/goosefs-lite-mnt

./bin/goosefs-lite mount /mnt/goosefs-lite-mnt/ cosn://examplebucket-1250000000/

查看本地挂载点和对应的 COS 存储桶，输出信息依次为进程 ID、本地挂载点和 COS 路径：

$ ./bin/goosefs-lite stat

pid mount_point cos_path

13815 /mnt/goosefs-lite-mnt/ cosn://examplebucket-1250000000/

如果您需要在命令行中，同时指定多个挂载参数，可以使用逗号分隔多个参数，如下命令设置挂载点只读，且允许其他用户访问挂载点：

./bin/goosefs-lite mount -o "ro,allow_other" mnt/ cosn://examplebucket-1250000000/

其中：

-o allow_other：如果要允许其他用户访问挂载文件夹，可以在运行 GooseFS-Lite 的时候指定该参数。

-o ro：将挂载点设置为只读，不允许写入和删除操作。

**说明：**

单个参数可通过 `-o` 指定，例如 `-o ro`；多个参数可通过逗号分隔，例如 `-o "ro,allow_other"`。

### 步骤6：卸载挂载点

**说明：**

卸载 GooseFS-Lite 挂载点将立即中断所有通过该路径访问 COS 的读写操作，操作前检查当前无业务进程正在使用该挂载目录。

在 `goosefs-lite-<具体版本号>` 目录下（以1.0.6版本为例，在 `goosefs-lite-1.0.6` 目录下），执行如下命令，即可卸载挂载点：

$ ./bin/goosefs-lite umount /mnt/goosefs-lite-mnt

Unmount fuse at /mnt/goosefs-lite-mnt/ (PID: 17206).

# 如果卸载异常，可以使用以下命令强制卸载

$ sudo umount -l /mnt/goosefs-lite-mnt

### 步骤7：参数调优

GooseFS-Lite 包含两个配置文件，分别为 conf/core-site.xml 及 conf/goosefs-lite.properties。

您可以通过修改 conf/core-site.xml 调优上传、下载带宽。常用参数如下，更多参数可参见 [Hadoop-COS](https://cloud.tencent.com/document/product/436/6884) 文档。

属性键 说明 默认值 必填项
fs.cosn.useHttps 配置是否使用 HTTPS 作为与 COS 后端的传输协议。true 否
fs.cosn.upload.part.size 分块上传的每个 part size 的大小。由于 COS 的分块上传最多只能支持10000块，因此需要预估最大可能使用到的单文件大小。 例如，part size 为8MB时，最大能够支持78GB的单文件上传。 part size 最大可以支持到2GB，即单文件最大可支持19TB。8388608（8MB）否
fs.cosn.upload_thread_pool 文件流式上传到 COS 时，并发上传的线程数目。32 否
fs.cosn.read.ahead.block.size 预读块的大小。1048576（1MB）否
fs.cosn.read.ahead.queue.size 预读队列的长度。6 否

您可以通过修改 conf/goosefs-lite.properties 对 GooseFS-Lite 的行为进行调整。常用参数如下：

属性 说明 默认值 必填项
goosefs.fuse.list.entries.cache.enabled 是否开启客户端 List 缓存 true 否
goosefs.fuse.list.entries.cache.max.size 客户端 List 最大缓存的条目数，单位：条 100000 否
goosefs.fuse.list.entries.cache.max.expiration.time 客户端 List 缓存的有效时间，单位：ms 15000 否
goosefs.fuse.async.release.max.wait.time open 和 rename 操作的文件正在被写入时，等待写入操作完成的时间，单位：ms 5000 否
goosefs.fuse.umount.timeout 卸载文件系统时，等待未完成操作的时间，单位：ms 120000 否

当您的读取和写入并发度较大，您可以通过如下方式，调整 GooseFS-Lite 最大 JVM 运行内存，避免 FullGC 和 OutOfMemoryError。JVM 默认值为 `-Xmx512m  -XX:MaxDirectMemorySize=512m  -XX:+UseG1GC -XX:G1HeapRegionSize=32m`，调整方式如下：

export JAVA_OPTS=" -Xms2G -Xmx2G"

./bin/goosefs-lite mount /mnt/goosefs-lite-mnt/ cosn://examplebucket-1250000000/

ps -ef|grep goosefs-lite|grep -v grep

## 常见问题

### 缺少 libfuse 库文件，如何处理？

![Image 2: img](https://qcloudimg.tencent-cloud.cn/image/document/efc79d9ef5d723afe7463e493762f805.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/efc79d9ef5d723afe7463e493762f805.png)

需要安装 libfuse，请参照以下方式进行操作：

**方式一**

1. 执行如下命令，安装 fuse-devel。

如果是 CentOS 或者 TencentOS 系统，执行如下命令：

yum install fuse-devel

如果是 Ubuntu 系统，执行如下命令：

apt install libfuse-dev

2. 安装完成后，执行如下命令，查看安装是否成功。

find / -name libfuse.so*

**方式二**

更新旧版本 libfuse.so.2.9.2，安装步骤如下：

**说明：**

CentOS 7默认安装的是 libfuse.so.2.9.2。

1. 下载 [libfuse 源码](https://github.com/libfuse/libfuse/releases/tag/fuse-2.9.7)，并编译生成 libfuse.so.2.9.7。

tar -zxvf fuse-2.9.7.tar.gz

cd fuse-2.9.7/ && ./configure && make && make install

echo -e '\n/usr/local/lib' >> /etc/ld.so.conf

ldconfig

2. 编译及生成 libfuse.so.2.9.7后，按照以下步骤进行替换：

2.1 执行以下命令，查找旧版本 libfuse.so.2.9.2库链接。

find / -name libfuse.so*

2.2 执行以下命令，将 libfuse.so.2.9.7拷贝至旧版本库 libfuse.so.2.9.2所在位置。

cp /usr/local/lib/libfuse.so.2.9.7 /usr/lib64/

2.3 执行以下命令， 删除旧版本 libfuse.so 库的所有链接。

rm -f /usr/lib64/libfuse.so

rm -f /usr/lib64/libfuse.so.2

2.4 执行以下命令，建立与被删除旧版本链接类似的 libfuse.so.2.9.7库链接。

ln -s /usr/lib64/libfuse.so.2.9.7 /usr/lib64/libfuse.so

ln -s /usr/lib64/libfuse.so.2.9.7 /usr/lib64/libfuse.so.2

### 如何配置开机挂载？

1. 编辑文件 /usr/lib/systemd/system/goosefs-lite.service，增加如下内容。您可以将 examplebucket-1250000000 换为您的存储桶：注意，以下 JAVA_OPTS 中 -Xms 和 -Xmx 配置的内存值不能超过所在节点的物理内存上限的50%。如节点物理内存16GB，那么建议最多配置 -Xms8G -Xmx8G。

下面以 goosefs-lite-1.0.6版本为例：

[Unit]

Description=The Tencent Cloud GooseFS Lite for COS

Requires=network-online.target

After=network-online.target

[Service]

Type=forking

User=root

Environment="JAVA_OPTS=-Xms2G -Xmx4G -XX:MaxDirectMemorySize=1G -XX:+UseG1GC -XX:G1HeapRegionSize=32m"

ExecStart=/usr/local/goosefs-lite-1.0.6/bin/goosefs-lite mount /mnt/goosefs-mnt cosn://examplebucket-1250000000/

ExecStop=/usr/local/goosefs-lite-1.0.6/bin/goosefs-lite umount /mnt/goosefs-mnt

Restart=always

RestartSec=5

[Install]

WantedBy=multi-user.target

2. 执行如下命令，执行挂载命令和查看后台 Daemon 进程状态。

# 让 goosefs-lite 的 systemd 配置生效

systemctl daemon-reload

# 启动后台 Fuse 进程

systemctl start goosefs-lite

# 查看后台 Daemon 进程状态

systemctl status goosefs-lite

# 查看挂载点列表

/usr/local/goosefs-lite-1.0.6/bin/goosefs-lite stat

# 如果是修改 systemd 配置，则在修改后 reload 并 restart。

设置为开机启动时尝试挂载：

systemctl enable goosefs-lite

3. 卸载挂载点，重启机器，并查看 Fuse 进程状态。

# 执行卸载，注意：请勿在数据写入的时卸载，否则会导致数据不完整

systemctl stop goosefs-lite

# 重启操作系统，请谨慎操作，不要影响业务

reboot -h now

# 查看后台 Daemon 进程状态

systemctl status goosefs-lite

# 查看挂载点列表

/usr/local/goosefs-lite-1.0.6/bin/goosefs-lite stat

### GooseFS-Lite 每天在某个时间段里 CPU 使用率较高，且向 COS 发出大量 Head、List 请求，产生大量请求次数费用，该怎么处理？

这通常是由于您机器上存在定时扫盘任务导致的，Linux 系统上常见的扫盘程序是 updatedb，您可以将 GooseFS-Lite 挂载点目录，添加到 updatedb 的配置文件 /etc/updatedb.conf 文件的 PRUNEPATHS 配置项中，避免该程序的扫盘行为。此外，您可以使用 Linux 工具 auditd，查找访问 GooseFS-Lite 挂载点的程序。

**操作步骤如下**：

1. 安装 auditd。

如果是 Ubuntu 系统，执行如下命令：

apt-get install auditd -y

如果是 CentOS 系统，执行如下命令：

yum install audit audit-libs

2. 启动 auditd 服务。

systemctl start auditd

systemctl enable auditd

3. 监控挂载目录。

**说明：**

`-w` 指定 GooseFS-Lite 挂载目录，`-k` 为输出在 audit 日志中的 key。

auditctl -w /usr/local/service/mnt/ -k goosefs_lite_mnt

4. 根据日志确定访问程序。

audit 的日志目录： /var/log/audit，查询命令如下：

ausearch -i|grep 'goosefs_lite_mnt'

5. 停止 auditd 服务。

如果您需要停止 auditd 服务，可以使用如下命令：

/sbin/service auditd stop

**注意：**

如果访问挂载点的程序一直在运行，新启动的 auditd，并不会监控到该程序的访问行为；程序中关于挂载目录的多次调用，只会记录第一次。

### GooseFS-Lite 安装时报“cannot allocate memory”错误，如何处理？

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/7ba228414fcac396e3945a3a698b3067.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/7ba228414fcac396e3945a3a698b3067.png)

该报错主要是因为 GooseFS-Lite 运行过程中分配内存异常报错，一般为申请内存大于实际可用内存。

您可以进入 ./bin/goosefs-lite 文件中修改 JAVA_OPTS 参数配置为合理内存数值，至少需要保证申请的内存数量小于实例可用内存数量。

### 怎么查看最新包版本？

执行如下命令，返回值即最新版本号。

curl -fsSL [https://downloads.tencentgoosefs.cn/goosefs-lite/LATEST_VERSION](https://downloads.tencentgoosefs.cn/goosefs-lite/LATEST_VERSION)

### 如何查看日志？

问题的排查需要依赖日志，以下是相关日志所在位置。

对于**goosefs-lite 1.0.3版本**及以上，默认日志目录在`/data/goosefs/logs/fuse` 下。

例如：您挂载 goosefs-lite 的用户为 root，挂载点路径为`/data1/data2`，那么日志路径为：`/data/goosefs/logs/fuse/root/data1/data2`。

对于 **goosefs-lite 1.0.0-1.0.2版本**，默认日志目录在`/data/goosefs/logs` 下。

另一种查看挂载点日志路径的方式，首先重新挂载，然后 `ps aux | grep ${MOUNT_POINT}`，从输出中可以看到 Error_File 或者 goosefs.logs.dir，这个路径的父目录则是该挂载点的全部日志所在位置。

系统日志：如果是 CentOS 或者 tlinux 系统，则是 `/var/log/message*`，如果是 Ubuntu，则是 `/var/log/syslog`。

**如果是需要开启 debug 日志，进入 conf/log4j.properties，注释最下面一行内容，重新挂载即可。**

**注意：**

开启 debug 日志会影响性能，正常情况无需开启。

### 挂载失败报错“Name or service not known”，如何处理？

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/0261a886cebd1278b2d763b2a4c30820.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/0261a886cebd1278b2d763b2a4c30820.png)

通常是因为无法解析域名，可以通过 ping 对应的域名尝试。如上图所示报错，可执行如下命令：

ping VM-36-104-centos

如果同样返回失败。可以通过修改 `/etc/hosts` 的方式，配置对应的 IP。一般可以配 `127.0.0.1`。

**操作步骤如下：**

1. 在 `/etc/hosts` 文件中添加一行。这里的 VM-36-104-centos 替换成您的主机名。

127.0.0.1 VM-36-104-centos

2. 之后重新 ping 测试，确认可以正常解析后，重新挂载即可。

### 默认环境 JDK 不是 KonaJDK11，怎么使用 GooseFS-Lite？

1. 下载 [KonaJDK11](https://github.com/Tencent/TencentKona-11/releases) 的包，并解压。

2. 复制 konajdk 中 java 二进制程序的绝对路径。例如，解压的 jdk 在 `/root/konajdk11`下。

# 确定 java 版本

/root/konajdk11/bin/java -version

# 修改当前 shell 的 JAVA 环境变量，不影响其他 shell 和进程

export JAVA=/root/konajdk11/bin/java

# 挂载

goosefs-lite mount /mnt cosn://bucket-appid

3. 使用 `ps aux | grep goosefs-lite`，可以看到进程开头是 `/root/konajdk11/bin/java`，说明已经使用了我们指定的 java 版本，操作完成。

### 挂载点本来是正常的，使用过程中突然无法正常使用了，如何处理？

假设当前的问题挂载点是 `/tmp/mount_point`。

1. 首先 `ps aux | grep /tmp/mount_point` 查看当前是否有进程正在使用这个挂载点，包括 goosefs-lite。如果有，使用 kill 命令杀掉对应的进程。

2. 使用 ls 尝试访问挂载点，如果返回为空，说明挂载点已经卸载成功。接着重新挂载即可。

ls /mount_point

3. 如果抛出 **transport is not connected**之类的错误，则需要执行 `umount -l /mount_point` 强制卸载。（此命令执行需要 root 权限）

通常这类情况是进程被 kill -9 或系统 oom-killer 导致。可以在系统日志或者 goosefs-lite 日志中找到。

4. 观察挂载点日志目录（/data/goosefs/logs/fuse/$USER/$MOUNT_POINT）下是否有 hs_error 开头的日志（文件中描述程序退出前的堆栈及原因）。

### 抛异常：Unsupported or unrecognized SSL message，如何处理？

当前环境不支持关闭 https 模式，需要修改配置。解决方式为在 `core-site.xml` 配置文件中，增加如下内容：

`<property>`

```<name>`fs.cosn.useHttps`</name>`

```<value>``false``</value>`

`</property>`

### GooseFS-Lite 怎么使用内网域名访问 COS？

在 `core-site.xml` 配置文件中，将 `fs.cosn.bucket.region` 属性删除，并添加 `fs.cosn.bucket.endpoint_suffix` 参数（如果您使用的是 goosefs-lite 1.0.12及以上版本，则添加 `fs.cosn.custom.endpoint_suffix` 参数）。

想了解更多参数，可以阅读以下文档：

[GitHub - tencentyun/hadoop-cos](https://github.com/tencentyun/hadoop-cos)

[对象存储 Hadoop 工具](https://cloud.tencent.com/document/product/436/6884)

### 挂载的时候或者使用过程中出现403 Forbidden，如何处理？

通常日志中 ERROR 类型日志会描述缺少什么权限，按需补充即可。

注意：对于 head bucket 权限，需要设置到桶级别而不能仅仅路径级别，例如，`cosn://bucket-appid/path` 这种是不生效的，必须是 `cosn://bucket-appid`。此权限不会暴露桶内有哪些对象。

### 报错 “fuse: failed to open /dev/fuse Operation not permitted”，如何处理？

1. 检查是否拥有 root 权限。

2. 如果是容器中，检查容器启动时是否带有 --privileged ，如果没有，加上。

3. 检查 fuse 内核模块是否安装：执行命令 `lsmod | grep fuse` ，查看是否有返回结果，如果没有说明 fuse 内核模块缺失。

### 文件写入失败，报错“ part num: 10001, the parameter partNumber is not valid.”，如何处理？

这种情况说明分块上传的块数超出限制了，COS 最大只支持1万个 part 上传。所以 goosefs-lite 默认最大支持8MB*10000（约78GB）的文件。如果需要支持更大的文件，需要调整参数 fs.cosn.upload.part.size。例如，fs.cosn.upload.part.size 修改为16777216（即16MB），则可以支持16MB*10000的大文件。
