<!-- source: https://cloud.tencent.com/document/product/582/85846 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T22:10:42+08:00 -->

# 通用型 CFS 实践指南

最近更新时间：2026-03-24 10:30:21


## 概述

本文主要基于 通用型文件系统的 NFS 协议的特性，介绍在使用时重点需要关注的使用方法和姿势，以便提供更适合用户业务场景的服务。

## 场景一：客户端内核选择

### 背景说明

NFS 客户端是基于内核态的客户端，因部分内核版本的缺陷，会导致 NFS 服务无法正常使用，为了保证您更好的使用体验，请使用我们推荐的内核版本。

### 常见问题及修复建议

#### **内核网络栈缺陷导致文件系统无响应（优先级：高）**

当系统的内核版本为2.6.32-696 ~ 2.6.32-696.10.1（包括2.6.32-696，但不包括2.6.32-696.10.1）时，NFS 服务端繁忙，内核请求重传，有概率触发内核网络栈缺陷，造成操作无响应。当操作无响应时，请重启 CVM 实例。更多信息，请参见 [RHEL6.9:NFSv4 TCP transport stuck in FIN_WAIT_2 forever](https://access.redhat.com/solutions/3053801)。

#### **内核缺陷导致文件系统无响应（优先级：高）**

当系统的内核版本为以下几个版本时，NFS 服务端故障转移，可能造成 NFS 客户端的打开、读、写操作出现死锁情况，从而导致文件系统持续无响应。当操作无响应时，请重启 CVM 实例。更多信息，请参见 [RHEL7:NFSv4 client loops with WRITE/NFS4ERR_STALE_STATEID - if NFS server restarts multiple times within the grace period](https://access.redhat.com/solutions/1427473)。

操作系统类型 版本号
Red Hat Enterprise Linux 6、CentOS 6 2.6.32-696.3.1.el6
Red Hat Enterprise Linux 7、CentOS 7 3.10.0-229.11.1.el7之前的所有内核版本
Ubuntu 15.10 Linux 4.2.0-18-generic

当系统的内核版本为以下几个版本时，网络发生分区或抖动，造成连接重连，NFS 客户端可能由于没有正确处理错误码而持续无响应。

现象是文件系统无响应且系统 message 中反复打印 bad sequence-id error。当操作无响应时，请重启 CVM 实例。更多信息，请参见 [RHEL6/RHEL7:NFS4 client receiving NFS4ERR_BAD_SEQID drops nfs4 stateowner resulting in infinite loop of READ/WRITE+NFS4ERR_BAD_STATEID](https://access.redhat.com/solutions/3073231)。

操作系统类型 版本号
Red Hat Enterprise Linux 6、CentOS 6 2.6.32-696.16.1.el6之前的所有内核版本
Red Hat Enterprise Linux 7、CentOS 7 3.10.0-693.el7之前的所有内核版本

当操作系统内核版本为 CentOS 和 Red Hat Enterprise Linux 5.11.x 所有内核时，执行`ls`命令、包含通配符 `*` 或 `?`的命令以及其他需要对目录进行遍历的操作，均会由于内核缺陷导致卡顿或无响应。请您升级内核版本，以避免此问题。

#### **不支持**`chown`**命令和系统调用（优先级：低）**

系统的内核版本为2.6.32时，不支持 NFS 客户端执行 `chown` 命令和系统调用。

#### **ls 操作无法终止（优先级：低）**

当系统的内核版本为2.6.32-696.1.1.el6及之前版本时，在系统中执行`ls`操作的同时还在进行添加、删除文件、子目录操作，将导致`ls`操作永远无法终止。请升级内核版本，避免此问题。

当系统的内核版本为4.18.0-305.12.1时，目录遍历操作如`ls`等，可能无法终止，请升级内核至4.18.0-305.19.1或以上版本修复此问题。

### NFS 推荐使用的内核镜像

#### **Linux 系统镜像**

操作系统类型 操作系统版本
CentOS CentOS 7.5 64位：3.10.0-862.14.4.el7.x86_64及以上

CentOS 7.6 64位：3.10.0-957.21.3.el7.x86_64及以上

CentOS 7.7 64位：3.10.0-1062.18.1.el7.x86_64及以上

CentOS 8.x 64位：4.18.0-147.5.1.el8_1.x86_64及以上
Tencent OS Linux TencentOS Server 2.2(Tkernel 3)

TencentOS Server 2.4 (Tkernel 4)

TencentOS Server 2.6(Final)

TencentOS Server 3.1(Tkernel 4)
Debian Debian 9.6 64位：4.9.0-8-amd64及以上

Debian 9.8 64位：4.9.0-8-amd64及以上

Debian 9.10 64位：4.9.0-9-amd64及以上
Ubuntu Ubuntu 14.04 64位：4.4.0-93-generic 及以上

Ubuntu 16.04 64位：4.4.0-151-generic 及以上

Ubuntu 18.04 64位：4.15.0-52-generic 及以上

Ubuntu 20.04 64位：5.4.0-31-generic 及以上
OpenSuse OpenSuse 42.3 64位：4.4.90-28-default及以上
Suse Enterprise Server 12 SP2 64位：4.4.74-92.35-default 及以上

Enterprise Server 12 SP4 64位：4.12.14-95.16-default 及以上
CoreOS CoreOS 1745.7.0 64位：4.19.56-coreos-r1及以上

CoreOS 2023.4.0 64位：4.19.56-coreos-r1及以上

#### **Windows 系统镜像**

操作系统类型 操作系统版本
Windows Server 2012 Windows Server 2012 R2数据中心版64位中文版

Windows Server 2012 R2数据中心版64位英文版
Windows Server 2016 Windows Server 2016数据中心版64位中文版

Windows Server 2016数据中心版64位英文版
Windows Server 2019 Windows Server 2019数据中心版64位中文版

Windows Server 2019数据中心版64位英文版

## 场景二：多进程或客户端并发写

### 背景说明

NFS 文件协议不提供强一致性的文件锁定机制，文件扩展和写入均非原子操作，因此，在多进程或多客户端并发写同一个文件的场景中，各进程或客户端维护各自的文件指针，默认缓存文件数据，最终导致不同客户端或进程查看到的文件状态可能不一致。常见问题包括写覆盖（后写入覆盖前写入）、内容交叉（写入操作交叉执行）、串行异常（类似串行写入，但无法保证顺序正确）等。

### 使用建议

**（推荐）**优化工作流，安排不同进程或客户端写入各自独立的文件，通过合并程序定期将这些文件合并为最终输出，完全避免并发写入冲突，提供最佳性能和数据一致性。

**（推荐）**换用自动加锁/解锁、并发读写一致性更高的 CFS Turbo文件系统​。

当不同客户端必须写入同一文件时，请采用以下多重保障措施：

挂载配置优化：使用 NFSv4代替 NFSv3协议挂载，添加 noac 挂载选项，确保文件状态实时同步。挂载命令可参考：

mount -t nfs -o vers=4.0,proto=tcp,noac,noresvport 10.XX.XX.XX:/ /localfolder

程序层手动加锁：在写入代码中使用 flock 系统调用实现互斥锁，并使用追加写入 O_APPEND 模式打开文件，确保严格遵循“获取锁→写入→释放锁”的工作流程。在程序中手动加锁可参考：

import os

import fcntl

O_WRONLY = os.O_WRONLY # 以只写方式打开文件

O_APPEND = os.O_APPEND # 以追加方式打开文件

O_DIRECT = getattr(os, 'O_DIRECT', 0o40000) # 尝试获取系统的 O_DIRECT 常量，如果不存在则设置为默认值 0o40000

SEEK_END = os.SEEK_END # 以文件尾为参考点

 # 假定并发写入的文件为 file1

filename = '/root/cfs/file1'

try:

 fd = os.open(filename, O_WRONLY | O_APPEND | O_DIRECT)


 # 尝试获取文件锁

 try:

 fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)

 print("Successfully acquired lock")


 # 定位到文件尾

 os.lseek(fd, 0, SEEK_END)


 # 写入数据

 data = b"hello world"

 os.write(fd, data)


 except BlockingIOError:

 print("File is locked by another process")

 # 如果文件被锁，则退出

 exit(1)

 finally:

 # 释放文件锁

 fcntl.flock(fd, fcntl.LOCK_UN)

 print("Lock released")


finally:

 if 'fd' in locals():

 os.close(fd)

**注意：**

高并发场景下，锁等待会导致明显的延迟增加，可能会显著影响文件系统读写性能，请根据业务实际需求酌情设置。
