<!-- source: https://cloud.tencent.com/document/product/436/10865 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:11:17+08:00 -->

# Java 安装与配置

最近更新时间：2024-03-25 14:34:51


## Windows

#### 1. 下载 JDK

进入 [Oracle 官方网站](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) 下载合适的 JDK 版本。

#### 2. 安装

根据提示一步步安装，安装过程中可以自定义安装目录（默认安装到 C 盘），例如我们选择的安装目录为：`D:\Program Files\Java\jdk1.8.0_31`和`D:\Program Files\Java\jre1.8.0_31`。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/d55b52f3a4af03559efdb06be754b5f0.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/d55b52f3a4af03559efdb06be754b5f0.png)

#### 3. 配置

安装完成后，右键单击**计算机 > 属性 > 高级系统设置 > 环境变量 > 系统变量 > 新建**，分别配置软件。 变量名(N)：**JAVA_HOME**

变量值(V)：`D:\Program Files\Java\jdk1.8.0_31`（请根据您的实际安装路径进行配置）。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/878204f15347b093a7875e872430815f.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/878204f15347b093a7875e872430815f.png)

 变量名(N)：**CLASSPATH**

变量值(V)：`.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;`（注意变量值开头有`.`）。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/0129aaae74a96925cddb6a68c8eddc96.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/0129aaae74a96925cddb6a68c8eddc96.png)

 变量名(N)：**Path** 变量值(V)：`%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;`

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/0be59ad9c736ca2b55b1b026482b77f8.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/0be59ad9c736ca2b55b1b026482b77f8.png)

**注意：**

如果 Path 变量已有值，可以在其末尾添加分号（;），然后继续添加新的变量值。

#### 4. 测试

测试配置是否成功：单击**开始（或快捷键：Win+R）> 运行（输入 cmd）> 确定（或按 Enter 键）**，输入命令 javac 并回车。若出现如下图所示信息，则说明环境变量配置成功。

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/79d63d09bc9fa6ceff59d3faab0fb72a.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/79d63d09bc9fa6ceff59d3faab0fb72a.png)

## Linux

由于使用 yum 或者 apt-get 命令 安装 openjdk 可能存在类库不全，从而导致用户在安装后运行相关工具时可能报错的问题，所以此处我们推荐采用手动解压安装的方式来安装 JDK。具体步骤如下：

#### 1.下载 JDK

进入 [Oracle 官方网站](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) 下载合适的 JDK 版本，准备安装。

**注意**

下面以 jdk-8u151-linux-x64.tar.gz 为例，如果您下载的是其他版本，请注意文件后缀为 .tar.gz 即可。

#### 2. 创建目录

执行如下命令，在 /usr/ 目录下创建 java 目录。

mkdir /usr/java

cd /usr/java

将下载的文件 jdk-8u151-linux-x64.tar.gz 复制到 /usr/java/ 目录下。

#### 3. 解压 JDK

执行如下命令，解压文件：

tar -zxvf jdk-8u151-linux-x64.tar.gz

#### 4. 设置环境变量

编辑 /etc/profile 文件，在 profile 文件中添加如下内容并保存：

# set java environment

JAVA_HOME=/usr/java/jdk1.8.0_151

JRE_HOME=/usr/java/jdk1.8.0_151/jre

CLASS_PATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib

PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin

export JAVA_HOME JRE_HOME CLASS_PATH PATH

**注意**

其中 JAVA_HOME，JRE_HOME 请根据自己的实际安装路径及 JDK 版本配置。

使之修改生效，执行如下：

source /etc/profile

#### 5. 测试

执行如下命令进行测试：

java -version

若显示 Java 版本信息，则说明 JDK 安装成功：

java version "1.8.0_151"

Java(TM) SE Runtime Environment (build 1.8.0_151-b12)

Java HotSpot(TM) 64-Bit Server VM (build 25.151-b12, mixed mode)
