<!-- source: https://cloud.tencent.com/document/product/436/10866 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:11:27+08:00 -->

# Python 安装与配置

最近更新时间：2024-05-13 11:05:31


## 通过安装包安装

### 1. 下载

进入 [Python 官方网站](https://www.python.org/downloads/)，根据自己使用的操作系统，选择下载合适的安装包。

**注意：**

Python 官方已于2020年1月1日停止对 Python2 的维护，建议安装使用 Python3。

### 2. 安装

下载安装包后，根据安装包的引导即可完成 Python 开发环境的安装。

**说明：**

Windows 系统用户在安装时要注意勾选"Add Python to environment variables"选项。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/982453db8e29f650c270f38784e0790b.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/982453db8e29f650c270f38784e0790b.png)

### 3. 验证

在终端中执行以下命令查看 Python 版本：

python -V

若终端输出 Python 版本号则证明安装成功。

**说明：**

Windows 系统用户在安装完毕后，可能需要重启计算机。

### 4. 环境变量配置

在 Windows 系统中，若在执行以上命令时终端提示"不是内部或外部命令"，请在**计算机 > 属性 > 高级系统设置 > 环境变量 > 系统变量(S)**中编辑 "Path"，增加 Python 的安装路径，如下图所示：

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/b541bde279a2e769e75d1e71b387dd51.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/b541bde279a2e769e75d1e71b387dd51.png)

## 通过包管理器安装

### Mac OS

使用 Mac OS 的用户可以先安装 [HomeBrew](https://brew.sh/)，再通过 HomeBrew 来安装 Python：

brew install python

### Ubuntu

使用 Ubuntu 的用户可以使用 Ubuntu 自带的 apt（Advanced Packaging Tool）包管理器来安装 Python：

sudo apt-get install python

### CentOS

使用 CentOS 的用户可以使用 CentOS 自带的 yum（Yellow dog Updater, Modified）包管理器来安装 Python：

sudo yum install -y python
