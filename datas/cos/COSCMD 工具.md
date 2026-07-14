<!-- source: https://cloud.tencent.com/document/product/436/10976 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:12:05+08:00 -->

# COSCMD 工具

最近更新时间：2026-07-08 12:05:36


## 功能说明

使用 COSCMD 工具，用户可通过简单的命令行指令实现对对象（Object）的批量上传、下载、删除等操作。

## 使用环境

#### 系统环境

支持 Windows、Linux 和 macOS 系统。

**说明：**

请保证本地字符格式为 UTF-8，否则操作中文版的文件会出现异常。

请确保本机时间已经与国际标准时间校准，如误差过大，将导致无法正常使用。

#### 软件依赖

Python 2.7和 Python 3。

最新版本的 pip。

**说明：**

建议用户直接安装集成 pip 的 Python 版本。

Python 版本为3.12时，pip 安装依赖库时容易失败，建议使用 [源码安装](https://cloud.tencent.com/document/product/436/10976#2.-.E6.BA.90.E7.A0.81.E5.AE.89.E8.A3.85.EF.BC.88.E4.B8.8D.E6.8E.A8.E8.8D.90.EF.BC.89)。

#### 安装及配置

环境安装与配置详细操作请参见 [Python 安装与配置](https://cloud.tencent.com/document/product/436/10866)。

pip 环境安装与配置详细操作请参见 [官网 pip 安装说明](https://pip.pypa.io/en/stable/installation/)。

## 下载与安装

下面为用户提供以下三种方式安装 COSCMD。

#### 方式一： 通过 pip 安装（推荐）

1. 执行以下 `pip` 命令进行安装。

pip install coscmd

安装成功之后，用户可以通过 `-v` 或者 `--version` 命令查看当前的版本信息。

**注意：**

使用 Windows 安装后，需要将 `C:\\python_install_dir` 和 `C:\\python_install_dir\\Scripts` 两个路径加入到环境变量中。

2. 安装完成后，执行以下命令进行更新。

pip install coscmd -U

#### 方式二：源码安装

**注意：**

Python 版本为3.12时，pip 安装依赖库时容易失败，建议使用该方法安装。

源码下载地址：[单击此处](https://github.com/tencentyun/coscmd)。

git clone https://github.com/tencentyun/coscmd.git

cd coscmd

python setup.py install

#### 方式三：离线安装

**注意：**

如果您的目标机器无法联网安装，可以先找一台可以联网的机器下载离线安装包，再将离线安装包拷贝到无法联网的目标机器进行安装。

请确保两台机器的 Python 版本保持一致，否则会出现安装失败的情况。

# 在有外网的机器下运行如下命令

mkdir coscmd-packages

pip download coscmd -d coscmd-packages

tar -czvf coscmd-packages.tar.gz coscmd-packages

# 将安装包拷贝到没有外网的机器后运行如下命令

tar -xzvf coscmd-packages.tar.gz

pip install coscmd --no-index -f coscmd-packages

## 配置参数

### 查看 help 选项

用户可通过 `-h` 或 `--help` 命令来查看工具的 help 信息和用法。

coscmd -h

help 信息如下所示：

usage: coscmd [-h] [-d] [-s] [-b BUCKET] [-r REGION] [-c CONFIG_PATH]

 [-l LOG_PATH] [--log_size LOG_SIZE]

 [--log_backup_count LOG_BACKUP_COUNT] [-v]

 {config,upload,download,delete,abort,copy,move,list,listparts,info,restore,signurl,createbucket,deletebucket,putobjectacl,getobjectacl,putbucketacl,getbucketacl,putbucketversioning,getbucketversioning,probe}

 ...

an easy-to-use but powerful command-line tool. try 'coscmd -h' to get more

informations. try 'coscmd sub-command -h' to learn all command usage, likes

'coscmd upload -h'

positional arguments:

 {config,upload,download,delete,abort,copy,move,list,listparts,info,restore,signurl,createbucket,deletebucket,putobjectacl,getobjectacl,putbucketacl,getbucketacl,putbucketversioning,getbucketversioning,probe}

 config Config your information at first

 upload Upload file or directory to COS

 download Download file from COS to local

 delete Delete file or files on COS

 abort Aborts upload parts on COS

 copy Copy file from COS to COS

 move move file from COS to COS

 list List files on COS

 listparts List upload parts

 info Get the information of file on COS

 restore Restore

 signurl Get download url

 createbucket Create bucket

 deletebucket Delete bucket

 putobjectacl Set object acl

 getobjectacl Get object acl

 putbucketacl Set bucket acl

 getbucketacl Get bucket acl

 putbucketversioning

 Set the versioning state

 getbucketversioning

 Get the versioning state

 probe Connection test

optional arguments:

 -h, --help show this help message and exit

 -d, --debug Debug mode

 -s, --silence Silence mode

 -b BUCKET, --bucket BUCKET

 Specify bucket

 -r REGION, --region REGION

 Specify region

 -c CONFIG_PATH, --config_path CONFIG_PATH

 Specify config_path

 -l LOG_PATH, --log_path LOG_PATH

 Specify log_path

 --log_size LOG_SIZE specify max log size in MB (default 1MB)

 --log_backup_count LOG_BACKUP_COUNT

 specify log backup num

 -v, --version show program's version number and exit

除此之外，用户还可以在每个命令后（不加参数）输入 `-h` 查看该命令的具体用法，如下所示。

# 查看 upload 命令使用方法

coscmd upload -h

### 使用 config 命令生成配置文件

**注意：**

建议用户通过 [临时密钥](https://cloud.tencent.com/document/product/436/14048) 使用工具，通过临时授权的方式进一步提高工具使用的安全性。申请临时密钥时，请遵循 [最小权限指引原则](https://cloud.tencent.com/document/product/436/38618)，防止泄露目标存储桶或对象之外的资源。

如果您一定要使用永久密钥，建议遵循 [最小权限指引原则](https://cloud.tencent.com/document/product/436/38618) 对永久密钥的权限范围进行限制。

config 命令可以在 `~/.cos.conf` 自动生成配置文件，命令具体格式如下。

coscmd config [OPTION]...<FILE>...

 [-h] --help

 [-a] <SECRET_ID>

 [-s] <SECRET_KEY>

 [-t] <TOKEN>

 [-b] <BucketName-APPID>

 [-r] <REGION> | [-e] <ENDPOINT>

 [-m] <MAX_THREAD>

 [-p] <PART_SIZE>

 [--do-not-use-ssl]

 [--anonymous]

**说明：**

其中 "[]" 中的字段为选项， "<>" 的字段为需要填写的参数。

参数配置说明如下。

选项 参数说明 有效值 是否必选
-a 密钥 ID 请前往 [API 密钥控制台](https://console.cloud.tencent.com/cam/capi) 获取。字符串 是
-s 密钥 Key 请前往 [API 密钥控制台](https://console.cloud.tencent.com/cam/capi) 获取。字符串 是
-t 临时密钥 token，当使用临时密钥时需要配置，设置 x-cos-security-token 头部。字符串 否
-b 指定的存储桶名称，存储桶的命名格式为 BucketName-APPID，请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83)。初次配置使用时，您需要在 COS 控制台创建一个存储桶，用于配置工具。字符串 是
-r 存储桶所在地域，请参见 [地域和访问域名](https://cloud.tencent.com/doc/product/436/6224)。字符串 是
-e 设置请求的 ENDPOINT，设置 ENDPOINT 参数后，REGION 参数会失效。当您使用的是默认域名，则此处配置格式为 `cos.<region>.myqcloud.com`；当您使用全球加速域名，则配置为 `cos.accelerate.myqcloud.com`。字符串 否
-m 指定多线程操作的最大线程数（默认为5）。如果上传文件缓慢，可适当调高该值。线程数取决于机器性能，假设机器支持最大线程数为30，则将并发线程调整为30，可充分利用机器性能，执行命令为 `coscmd config -m 30`。数字 否
-p 分块操作的单块大小（单位MB，默认为1MB，范围为1 - 1000）。如果上传文件缓慢，可适当调高该值。数字 否
--do-not-use-ssl 使用 HTTP 协议，而不使用 HTTPS。字符串 否
--anonymous 匿名操作（不携带签名）。字符串 否

config 命令的使用示例如下：

coscmd config -a AChT4ThiXAbpBDEFGhT4ThiXAbp**** -s WE54wreefvds3462refgwewe**** -b configure-bucket-1250000000 -r ap-chengdu

### 生成配置文件

COSCMD 工具在运行时会从配置文件读取所需的必要信息，COSCMD 默认读取的配置文件的路径为`~/.cos.conf`。如需更改配置文件的路径，请参见 [指定配置文件和日志文件路径的命令](https://cloud.tencent.com/document/product/436/10976#.E6.8C.87.E5.AE.9A.E9.85.8D.E7.BD.AE.E6.96.87.E4.BB.B6.E5.92.8C.E6.97.A5.E5.BF.97.E6.96.87.E4.BB.B6.E8.B7.AF.E5.BE.84.E7.9A.84.E5.91.BD.E4.BB.A4)。

**说明：**

配置前，您需要先在 COS 控制台创建一个用于配置参数的存储桶（例如 configure-bucket-1250000000），请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。然后创建密钥信息，请参见 [主账号访问密钥管理](https://cloud.tencent.com/document/product/598/40488)。

一个配置文件的示例如下所示。

[common]

secret_id = ************************************

secret_key = ************************************

bucket = configure-bucket-1250000000

region = ap-chengdu

max_thread = 5

part_size = 1

retry = 5

timeout = 60

schema = https

verify = md5

anonymous = False

**说明：**

配置文件中 `timeout` 项，单位为秒，指读写数据的超时时间。

配置文件中 `schema` 项，可选值为 http、https，默认为 https。

配置文件中 `anonymous` 项，可选值为 True、False，表示是否使用匿名模式，即签名保持为空。

更多配置参数说明，请使用命令 `coscmd config -h` 查看。

## 通用命令

### 指定 Bucket 和 Region 的命令

用户若不指定存储桶名称和所属地域执行命令，则默认对配置参数时所填的存储桶有效。当需要对不同存储桶执行操作时，需要指定存储桶名称和所属地域。

**说明：**

通过 `-b <BucketName-APPID>` 参数指定存储桶名称，存储桶的命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式。

通过 `-r <region>` 指定 Region，可以指定存储桶的所属地域。

命令格式。

coscmd -b <BucketName-APPID> -r <region> <action> ...

操作示例：创建一个名称为 examplebucket-1250000000、所属地域为北京的存储桶。

coscmd -b examplebucket-1250000000 -r ap-beijing createbucket

操作示例：将 D 盘下的文件 picture.jpg 上传到名称为 examplebucket-1250000000的存储桶。

coscmd -b examplebucket-1250000000 -r ap-beijing upload D:/picture.jpg /

### 指定配置文件和日志文件路径的命令

用户若不指定配置文件的路径，则会使用默认的配置文件路径 `~/.cos.conf`。若不指定日志文件的路径，则会使用默认的日志文件路径 `~/.cos.log`。

**说明：**

通过 `-c <conf_path>` 参数指定配置文件路径，COSCMD 在运行时会从此路径读取配置信息。

通过 `-l <log_conf>` 参数指定日志路径，COSCMD 会将运行过程中产生的日志输出到此路径下的日志文件中。

命令格式。

coscmd -c <conf_path> -l <log_conf> <action> ...

操作示例：指定配置文件路径为 /data/home/cos_conf，日志输出路径为 /data/home/cos_log，创建一个名称为 examplebucket-1250000000、所属地域为北京的存储桶。

coscmd -c /data/home/cos_conf -l /data/home/cos_log -b examplebucket-1250000000 -r ap-beijing createbucket

### Debug 模式执行命令

在各命令前加上 `-d` 或者 `--debug`，在命令执行的过程中，会显示详细的操作信息 ，示例如下。

命令格式。

coscmd -d upload <localpath> <cospath>

操作示例：上传时输出详细信息。

coscmd -d upload -rs D:/folder/ /

### Silence 模式执行命令

在各命令前加上 `-s` 或者 `--silence`，在命令执行的过程中，将不会再输出任何信息 。

**说明：**

该命令需满足最低版本为1.8.6.24。

命令格式。

coscmd -s upload <localpath> <cospath>

操作示例。

coscmd -s upload D:/picture.jpg /

## 常用存储桶命令

### 创建存储桶

**说明：**

执行创建存储桶命令时，请携带参数 `-b <BucketName-APPID>` 指定存储桶名称和 `-r <Region>` 指定所属地域。若直接执行 coscmd createbucket，则会报错，原因是不指定存储桶名称和所属地域，则相当于对已存在的存储桶（即配置参数时所填的存储桶）进行创建。

命令格式。

coscmd -b <BucketName-APPID> createbucket

操作示例：创建一个名称为 examplebucket-1250000000，所属地域为北京的存储桶。

coscmd -b examplebucket-1250000000 -r ap-beijing createbucket

### 删除存储桶

**说明：**

`coscmd deletebucket` 的用法仅对配置参数时的存储桶有效。建议配合 `-b <BucketName-APPID>` 指定 Bucket 和 `-r <region>` 指定 Region 使用。

命令格式。

coscmd -b <BucketName-APPID> deletebucket

操作示例：删除空的存储桶。

coscmd -b examplebucket-1250000000 -r ap-beijing deletebucket

操作示例：强制删除非空的存储桶。

coscmd -b examplebucket-1250000000 -r ap-beijing deletebucket -f

**注意：**

使用 `-f` 参数则会强制删除该存储桶，包括所有文件、开启版本控制之后历史文件夹、上传产生的碎片，请谨慎操作。

## 常用对象命令

### 上传文件

命令格式。

coscmd upload <localpath> <cospath>

**注意：**

请将 "<>" 中的参数替换为您需要上传的本地文件路径（localpath），以及 COS 上存储的路径（cospath）。

COSCMD 不支持上传软链接，请使用 COSCLI 工具，详情请参见 [上传下载或拷贝文件 - cp](https://cloud.tencent.com/document/product/436/63669)。

操作示例：将 D 盘的 picture.jpg 文件上传到 COS 的 doc 目录下。

coscmd upload D:/picture.jpg doc/

操作示例：将 D 盘的 doc 文件夹下的 picture.jpg 文件上传到 COS 的 doc 目录下。

coscmd upload D:/doc/picture.jpg doc/

操作示例：指定对象类型，上传一个归档类型的文件到 COS 的 doc 目录下。

coscmd upload D:/picture.jpg doc/ -H "{'x-cos-storage-class':'Archive'}"

**注意：**

使用 -H 参数设置 HTTP header 时，请务必保证格式为 JSON，示例：`coscmd upload -H "{'x-cos-storage-class':'Archive','Content-Language':'zh-CN'}" <localpath> <cospath>`。更多头部请参见 [PUT Object](https://cloud.tencent.com/document/product/436/7749) 文档。

操作示例：设置 meta 元属性，上传一个文件到 COS 的 doc 目录下。

coscmd upload D:/picture.jpg doc/ -H "{'x-cos-meta-example':'example'}"

操作示例：指定上传限速为 800Kb/s，将 D 盘的 doc 文件夹下的 file.zip 文件上传到 COS 的 doc 目录下。

coscmd upload D:/doc/file.zip doc/ -H "{'x-cos-traffic-limit':'819200'}"

**说明：**

通过 -H 参数指定请求头部 x-cos-traffic-limit 进行限速，限速值设置范围为819200 - 838860800，单位默认为 bit/s，即800Kb/s - 800Mb/s，如果超出该范围将返回400错误。

### 上传文件夹

命令格式。

coscmd upload -r <localpath> <cospath>

**注意：**

Windows 用户推荐在系统自带的 cmd 工具或 PowerShell 上使用 COSCMD 的 upload 命令，其他工具（如 git bash）对命令路径的解析策略与 PowerShell 不同，可能会导致用户的文件被上传到错误的路径上去。

操作示例：将 D 盘的 doc 文件夹及其文件上传到 COS 根路径。

coscmd upload -r D:/doc /

操作示例：将 D 盘的 doc 文件夹中的文件、子文件夹上传到 COS 的 test 路径下，不包括 doc 文件夹本身。

coscmd upload -r D:/doc test

操作示例：同步上传，跳过 md5、文件大小相同的同名文件。

coscmd upload -rs D:/doc doc

**注意：**

使用 -s 参数可以使用同步上传，跳过上传 md5一致的文件（COS 上的原文件必须是由1.8.3.2版本之后的 COSCMD 上传的，默认带有 x-cos-meta-md5的 header）。

操作示例：同步上传，跳过文件大小相同的同名文件。

coscmd upload -rs --skipmd5 D:/doc doc

**注意：**

使用 -s 参数可以使用同步上传，且带上 --skipmd5参数后，将只对比同名文件的大小，如果大小相同则跳过上传。

操作示例：同步上传，并删除 “D 盘 doc 文件夹中已经删除的文件”。

coscmd upload -rs --delete D:/doc /

**说明：**

例如当天 D 盘 doc 文件夹中的文件与 COS 中 doc 路径下的文件已同步上传，源端与目标端一致。第二天用户把 D 盘 doc 文件夹中的 A 文件删除了，此时执行以上命令，会删除 COS 中 doc 路径下的 A 文件，最终实现 D 盘 doc 文件夹中的文件与 COS 中 doc 路径下的文件保持一致。

操作示例：D 盘 doc 文件夹中 .txt 和 .doc 后缀的文件选择忽略上传。

coscmd upload -rs D:/doc / --ignore *.txt,*.doc

操作示例：D 盘 doc 文件夹中 .txt 后缀的文件选择忽略上传。

coscmd upload -rs D:/doc / --ignore "*.txt"

**注意：**

在上传文件夹时，使用 `--ignore` 参数可以忽略某一类文件，使用 `--include` 参数可以过滤某一类文件，支持 shell 通配规则，支持多条规则，用逗号 `,` 分隔。当忽略一类后缀时，必须使用 `""`包裹。

如果您希望使用 `--ignore` 过滤特定文件夹内的所有文件，需要使用绝对路径，并在路径前后加入 `""`。例如 `coscmd upload -rs D:/doc / --ignore "D:/doc/ignore_folder/*"`。

操作示例：D 盘 doc 文件夹中 .txt 和 .doc 的后缀文件上传。

coscmd upload -rs D:/doc / --include *.txt,*.doc

操作示例：D 盘 doc 文件夹中 .txt 后缀的文件上传。

coscmd upload -rs D:/doc / --include "*.txt"

**注意：**

当上传大于一定阈值（100MB）的文件，COSCMD 即采用分块上传方式，命令用法和简单上传一致，即 `coscmd upload <localpath> <cospath>`。如果您使用的是1.8.6.31以下版本（不包括1.8.6.31版本），则该阈值为10MB。

COSCMD 支持大文件断点上传功能；当分块上传大文件失败时，重新上传该文件只会上传失败的分块，而不会从头开始（请保证重新上传的文件的目录以及内容和上传的目录保持一致）。

COSCMD 分块上传时会对每一块进行 MD5校验。

COSCMD 上传默认会携带 `x-cos-meta-md5`的头部，值为该文件的 md5值，如果带上 --skipmd5参数则不携带该头部。

### 查询文件列表

查询命令如下：

命令格式。

coscmd list <cospath>

操作示例：递归查询该存储桶下 doc/ 前缀下所有的文件列表。

coscmd list doc/

操作示例：递归查询该存储桶下所有的文件列表、文件数量和文件大小。

coscmd list -ar

操作示例：递归查询 examplefolder 前缀的所有文件列表。

coscmd list examplefolder/ -ar

操作示例：查询该存储桶下所有文件的历史版本。

coscmd list -v

**说明：**

请将 "<>" 中的参数替换为您需要查询文件列表的 COS 上文件的路径（cospath）。`<cospath>` 为空默认查询当前存储桶根目录。

使用 `-a` 查询全部文件。

使用 `-r` 递归查询，并且会在末尾返回列出文件的数量和大小之和。

使用 `-n num` 设置查询数量的最大值。

### 查看文件信息

命令如下：

命令格式。

coscmd info <cospath>

操作示例：查看 doc/picture.jpg 的元信息。

coscmd info doc/picture.jpg

**说明：**

请将 "<>" 中的参数替换为您需要显示的 COS 上文件的路径（cospath）。

### 下载文件或文件夹

#### 下载文件

命令格式。

coscmd download <cospath> <localpath>

**注意：**

请将 "<>" 中的参数替换为您需要下载的 COS 上文件的路径（cospath），以及本地存储路径（localpath）。

操作示例：下载 COS 上的 doc/picture.jpg 到 D:/picture.jpg。

coscmd download doc/picture.jpg D:/picture.jpg

操作示例：下载 COS 上的 doc/picture.jpg 到 D 盘。

coscmd download doc/picture.jpg D:/

操作示例：下载一个带有版本 ID 的 picture.jpg 文件到 D 盘。

coscmd download picture.jpg --versionId MTg0NDUxMzc2OTM4NTExNTg7Tjg D:/

操作示例：指定下载单链接限速为 800Kb/s，下载 COS 上的 doc/picture.jpg 到 D:/picture.jpg。

coscmd download doc/picture.jpg D:/picture.jpg -H "{'x-cos-traffic-limit':'819200'}"

**说明：**

通过 -H 参数指定请求头部 x-cos-traffic-limit 进行限速，限速值设置范围为819200 - 838860800，单位默认为bit/s，即800Kb/s - 800Mb/s，如果超出该范围将返回400错误。

#### 下载文件夹

命令格式。

coscmd download -r <cospath> <localpath>

操作示例：下载 doc 目录为 D:/folder/doc。

coscmd download -r doc D:/folder/

操作示例：下载根目录文件，但跳过根目录下的 doc 目录。

coscmd download -r / D:/ --ignore "doc/*"

操作示例：覆盖下载当前存储桶根目录下所有的文件。

coscmd download -rf / D:/examplefolder/

**注意：**

若本地存在同名文件，则会下载失败，需要使用 `-f` 参数覆盖本地文件。

操作示例：同步下载当前 bucket 根目录下所有的文件，跳过 md5校验相同的同名文件。

coscmd download -rs / D:/examplefolder

**注意：**

使用 `-s` 或者 `--sync` 参数，可以在下载文件夹时跳过本地已存在的相同文件（前提是下载的文件是通过 COSCMD 的 upload 接口上传的，文件携带有 `x-cos-meta-md5` 头部）。

操作示例：同步下载当前 bucket 根目录下所有的文件，跳过文件大小相同的同名文件。

coscmd download -rs --skipmd5 / D:/examplefolder

操作示例：同步下载，并删除 “COS 存储桶中 doc 路径下已删除的文件”。

coscmd download -rs --delete / D:/doc

**说明：**

例如，当天 D 盘 doc 文件夹中的文件与 COS 中 doc 路径下的文件已同步下载，源端与目标端一致。第二天用户把 COS 中 doc 路径下的 A 文件删除了，此时执行以上命令，并按照窗口提示输入`y`（确定）后，会删除 D 盘 doc 文件夹下的 A 文件，最终实现 D 盘 doc 文件夹中的文件与 COS 中 doc 路径下的文件保持一致。

操作示例：忽略 .txt 和 .doc 的后缀文件。

coscmd download -rs / D:/examplefolder --ignore *.txt,*.doc

操作示例：忽略 .txt 后缀的文件。

coscmd download -rs / D:/examplefolder --ignore "*.txt"

**注意：**

在上传文件夹时，使用 `--ignore` 参数可以忽略某一类文件，使用 `--include` 参数可以过滤某一类文件，支持 shell 通配规则，支持多条规则，用逗号 `,` 分隔。当忽略一类后缀时，必须 使用`""`包裹。

如果您希望使用 `--ignore` 过滤特定目录内的所有文件，需要使用绝对路径，并在路径前后加入 `""`。例如 `coscmd upload -rs D:/doc / --ignore "D:/doc/ignore_folder/*"`。

操作示例：过滤 .txt 和 .doc 的后缀文件。

coscmd download -rs / D:/examplefolder --include *.txt,*.doc

操作示例：过滤 .txt 后缀的文件。

coscmd download -rs / D:/examplefolder --include "*.txt"

**注意：**

老版本的 mget 接口已经废除，download 接口使用分块下载，请使用 download 接口。

### 获取带签名的下载 URL

命令格式。

coscmd signurl <cospath>

操作示例：生成 doc/picture.jpg 路径带签名的 URL。

coscmd signurl doc/picture.jpg

操作示例：生成 doc/picture.jpg 路径带100s 签名的 URL。

coscmd signurl doc/picture.jpg -t 100

**说明：**

请将 "<>" 中的参数替换为您需要获取下载 URL 的 COS 上文件的路径（cospath）。

使用 `-t time` 设置该 URL 中签名的有效时间（单位为秒）, 默认为10000s。

### 删除文件或文件夹

#### 删除文件

命令格式。

coscmd delete <cospath>

**注意：**

请将 "<>" 中的参数替换为您需要删除的 COS 上文件的路径（cospath），工具会提示用户是否确认进行删除操作。

操作示例：删除 doc/exampleobject.txt。

coscmd delete doc/exampleobject.txt

操作示例：删除带有版本 ID 的文件。

coscmd delete doc/exampleobject.txt --versionId MTg0NDUxMzc4ODA3NTgyMTErEWN

#### 删除文件夹

命令格式。

coscmd delete -r <cospath>

操作示例：删除 doc 目录。

coscmd delete -r doc

操作示例：删除 folder/doc 目录。

coscmd delete -r folder/doc

操作示例：删除 doc 文件夹下的所有版本控制文件。

coscmd delete -r doc/ --versions

**说明：**

批量删除需要输入 `y` 确定，使用 `-f` 参数则可以跳过确认直接删除。

需注意，执行删除文件夹命令，将会删除当前文件夹及其文件。但删除版本控制的文件，需要指定版本 ID 进行删除。

### 查询分块上传文件碎片

命令格式。

coscmd listparts <cospath>

操作示例：查询 doc/ 前缀的文件碎片。

coscmd listparts doc/

### 清除分块上传文件碎片

命令格式。

coscmd abort

操作示例：消除所有上传文件碎片。

coscmd abort

### 复制文件或文件夹

#### 复制文件

命令格式。

coscmd copy <sourcepath> <cospath>

操作示例：在同个存储桶内进行复制，将 examplebucket-1250000000存储桶下的 picture.jpg 文件复制到 doc 文件夹下。

coscmd -b examplebucket-1250000000 -r ap-chengdu copy examplebucket-1250000000.cos.ap-chengdu.myqcloud.com/picture.jpg doc/

操作示例：在不同存储桶内进行复制，复制 examplebucket2-1250000000存储桶下的 doc/picture.jpg 对象到 examplebucket1-1250000000存储桶的 doc/examplefolder/。

coscmd -b examplebucket1-1250000000 -r ap-guangzhou copy examplebucket2-1250000000.cos.ap-beijing.myqcloud.com/doc/picture.jpg doc/examplefolder/

修改存储类型，将复制后的对象所对应的存储类型改为低频存储。

coscmd -b examplebucket1-1250000000 -r ap-guangzhou copy examplebucket2-1250000000.cos.ap-beijing.myqcloud.com/doc/picture.jpg doc/examplefolder/ -H "{'x-cos-storage-class':'STANDARD_IA'}"

修改存储类型，将复制后的对象所对应的存储类型改为归档存储，并重命名为 photo.jpg。

coscmd -b examplebucket1-1250000000 -r ap-guangzhou copy examplebucket2-1250000000.cos.ap-beijing.myqcloud.com/doc/picture.jpg doc/examplefolder/photo.jpg -H "{'x-cos-storage-class':'Archive'}"

#### 复制文件夹

命令格式。

coscmd copy -r <sourcepath> <cospath>

操作示例：复制 examplebucket2-1250000000存储桶下的 examplefolder 目录到 examplebucket1-1250000000存储桶的 doc 目录。

coscmd -b examplebucket1-1250000000 -r ap-guangzhou copy -r examplebucket2-1250000000.cos.ap-guangzhou.myqcloud.com/examplefolder doc/

**说明：**

请将 "<>" 中的参数替换为您需要复制的 COS 上文件的路径（sourcepath），和您需要复制到 COS 上文件的路径（cospath）。

sourcepath 的格式为：`<BucketName-APPID>.cos.<region>.myqcloud.com/<cospath>`。

使用 -d 参数可以设置 `x-cos-metadata-directive` 参数，可选值为 Copy 和 Replaced，默认为 Copy。

使用 -H 参数设置 HTTP header 时，请务必保证格式为 JSON，示例：`coscmd copy -H -d Replaced "{'x-cos-storage-class':'Archive','Content-Language':'zh-CN'}" <localpath> <cospath>`。更多头部请参见 [PUT Object - Copy](https://cloud.tencent.com/document/product/436/10881) 文档。

### 移动文件或文件夹

**注意：**

移动命令的 `<sourcepath>` 和 `<cospath>` 不能相同，否则会导致文件被删除。原因在于 move 命令会先复制，再删除，`<sourcepath>` 路径下的文件最终会被删除。

#### 移动文件

命令格式。

coscmd move <sourcepath> <cospath>

操作示例：在同个存储桶内进行移动，将 examplebucket-1250000000存储桶下的 picture.jpg 移动到 doc 文件夹下。

coscmd -b examplebucket-1250000000 -r ap-chengdu move examplebucket-1250000000.cos.ap-chengdu.myqcloud.com/picture.jpg doc/

操作示例：在不同存储桶内进行移动，移动 examplebucket2-1250000000存储桶下的 picture.jpg 对象到 examplebucket1-1250000000存储桶的 doc/folder/。

coscmd -b examplebucket1-1250000000 -r ap-guangzhou move examplebucket2-1250000000.cos.ap-beijing.myqcloud.com/picture.jpg doc/folder/

操作示例：将移动到目标存储桶中的对象所对应的存储类型修改为低频存储。

coscmd -b examplebucket1-1250000000 -r ap-guangzhou move examplebucket2-1250000000.cos.ap-beijing.myqcloud.com/picture.jpg doc/folder/ -H "{'x-cos-storage-class':'STANDARD_IA'}"

操作示例：将移动到目标存储桶中的对象所对应的存储类型修改为归档存储。

coscmd -b examplebucket1-1250000000 -r ap-guangzhou move examplebucket2-1250000000.cos.ap-beijing.myqcloud.com/data/exampleobject data/examplefolder/exampleobject -H "{'x-cos-storage-class':'Archive'}"

#### 移动文件夹

命令格式。

coscmd move -r <sourcepath> <cospath>

操作示例：移动 examplebucket2-1250000000存储桶下的 examplefolder 目录到 examplebucket1-1250000000存储桶的 doc 目录。

coscmd -b examplebucket1-1250000000 -r ap-guangzhou move -r examplebucket2-1250000000.cos.ap-guangzhou.myqcloud.com/examplefolder doc/

**说明：**

请将 "<>" 中的参数替换为您需要移动的 COS 上文件的路径（sourcepath），和您需要移动到 COS 上文件的路径（cospath）。

sourcepath 的格式为：`<BucketName-APPID>.cos.<region>.myqcloud.com/<cospath>`。

使用 -d 参数可以设置 `x-cos-metadata-directive` 参数，可选值为 Copy 和 Replaced，默认为 Copy。

使用 -H 参数设置 HTTP header 时，请务必保证格式为 JSON，示例：`coscmd move -H -d Replaced "{'x-cos-storage-class':'Archive','Content-Language':'zh-CN'}" <sourcepath> <cospath>`。更多头部请参见 [PUT Object - copy](https://cloud.tencent.com/document/product/436/10881) 文档。

### 设置对象访问权限

命令格式。

coscmd putobjectacl --grant-<permissions> <UIN> <cospath>

**说明：**

对象访问权限支持设置为--grant-read（即授予用户读权限）、--grant-full-control（即授予用户完全控制的权限）。对于文件夹则还可以设置为--grant-write（即授予用户写权限）。

操作示例：授予账号100000000001拥有 picture.jpg 的读取权限。

coscmd putobjectacl --grant-read 100000000001 picture.jpg

操作示例：查询文件的访问权限。

coscmd getobjectacl picture.jpg

### 开启/暂停版本控制

命令格式。

coscmd putbucketversioning <status>

操作示例：开启版本控制。

coscmd putbucketversioning Enabled

操作示例：暂停版本控制。

coscmd putbucketversioning Suspended

操作示例：查询版本控制。

coscmd getbucketversioning

**注意：**

请将 "<>" 中的参数替换为您需要版本控制状态（status）。

一旦您对存储桶启用了版本控制，它将无法返回到未启用版本控制状态（初始状态）。但是，您可以对该存储桶暂停版本控制，这样后续上传的对象将不会产生多个版本。

### 恢复归档文件

恢复归档文件命令格式。

coscmd restore <cospath>

操作示例：快速取回模式回热 picture.jpg，有效期3天。

coscmd restore -d 3 -t Expedited picture.jpg

批量恢复归档文件命令格式。

coscmd restore -r <cospath>

操作示例：快速取回模式回热 examplefolder/ 目录，有效期3天。

coscmd restore -r -d 3 -t Expedited examplefolder/

**说明：**

请将 "<>" 中的参数替换为您需要查询文件列表的 COS 上文件的路径（cospath）。

使用 `-d <day>` 设置临时副本的过期时间，默认值：7。

使用 `-t <tier>` 指定恢复模式，枚举值：Expedited （快速取回模式），Standard （标准取回模式），Bulk（批量取回模式），默认值：Standard。

## 常见问题

如您在使用 COSCMD 工具过程中，有相关的疑问，请参见 [COSCMD 工具类常见问题](https://cloud.tencent.com/document/product/436/30744)。

## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击 [此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406) 一键启动，立即使用！
