<!-- source: https://cloud.tencent.com/document/product/436/63679 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:12:22+08:00 -->

# 生成与修改配置文件 - config

最近更新时间：2026-03-12 17:34:22


## 命令格式

以下 config 命令用于生成与修改配置文件：

./coscli config [command] [flag]

**说明：**

正确填写各配置项后，您可以使用`./coscli config show` 来查看配置信息。

关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。

生成的配置文件，默认网络传输协议为 https。如需更改为 http，可直接进入配置文件进行修改即可。

修改配置文件后，原配置将无法使用，请谨慎操作。

config 命令包含以下子命令：

command 名称 command 用途
add 添加一个新的存储桶配置。
delete 删除一个已经存在的存储桶配置。
init 交互式地生成配置文件。
set 修改配置文件 base 组中的一个或多个配置项。base 组包含 `secretid`、`secretkey`、`sessiontoken`、`mode`、`cvmrolename` 信息。
show 打印指定配置文件中的信息。

config 及其子命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法。
-c--config-path 指定要使用的配置文件路径。

config add 子命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法。
-a--alias 存储桶别名。
-b--bucket 存储桶名称。
-r--region 存储桶地域。
-o--ofs 元数据加速桶标记。详情请参见 [元数据加速概览](https://cloud.tencent.com/document/product/436/56971)。

**注意：**

如果您需要指定存储桶的 endpoint，可以使用通用 flag `-e` 或 `--endpoint`，详见 [通用选项介绍](https://cloud.tencent.com/document/product/436/71763)。

config delete 子命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法。
-a--alias 存储桶别名。

config set 子命令包含以下可选 flag：

flag 简写 flag 全称 flag 用途
-h--help 查看该命令的具体用法。
无--secret_id 设置 secret ID。可从 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 中创建并获取。
无--secret_key 设置 secret key。可从 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 中创建并获取。
-t--session_token 设置临时密钥 token。关于临时密钥的更多信息，请参见 [使用临时密钥访问 COS](https://cloud.tencent.com/document/product/436/68283)。
无--mode 设置身份模式，支持枚举值 `SecretKey` 和 `CvmRole`。可以为空，空值默认为 `SecretKey`，表示使用密钥请求 COS。当 mode 为 `CvmRole` 时，表示用 [管理实例角色](https://cloud.tencent.com/document/product/213/47668) 请求 COS。
无--cvm_role_name 设置 CVM 角色实例名称，详情请参见 [管理实例角色](https://cloud.tencent.com/document/product/213/47668)。
无--close_auto_switch_host 设置是否关闭自动切换备份域名。可选值 true、false，可以为空 。

若不设置或值为 false，则会进行备份域名切换。

若设置为 true，则不进行备份域名切换。
无--disable_encryption 设置是否关闭密钥加密。默认为 false，若设置为 true，则不加密配置文件中的密钥相关信息。
无--disable_auto_fetch_bucket_type 设置是否禁用自动获取存储桶类型，可选值 true、false。

若不设置或值为 false，则会自动获取存储桶类型（请确保您所使用的账号已拥有 `cos:HeadBucket` 权限）。

若设置为 true，则不自动获取存储桶类型，会使用用户配置文件中的存储桶类型（例如配置文件中 Bucket 配置项 ofs 设置为 true，则存储桶类型为 ofs；若设置为 false，则存储桶类型为 cos）

## 操作示例

### 添加一个新的存储桶配置

./coscli config add -b examplebucket3-1250000000 -r ap-chengdu -e cos.ap-chengdu.myqcloud.com -a bucket3

### 删除一个已经存在的存储桶配置

./coscli config delete -a bucket3

### 修改默认配置文件中的 session-token

./coscli config set --session_token test-token123

### 打印指定配置文件中的信息

./coscli config show -c /your/config/path.yaml

### 修改默认配置文件中的 mode 和 cvmrolename

./coscli config set --mode CvmRole --cvm_role_name testName
