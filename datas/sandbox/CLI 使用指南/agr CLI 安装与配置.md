<!-- source: https://cloud.tencent.com/document/product/1814/132205 -->
<!-- fetcher: jina -->

# agr CLI 安装与配置

最近更新时间：2026-06-30 15:33:00


## 前提条件

已获取腾讯云 `SecretId` 和 `SecretKey`。

安装环境可以访问 GitHub Releases、执行 `go install`，或者从源码执行 `make build`。

如果运行环境的 Home 目录不可写，请提前准备一个可写配置路径，并在命令中通过 `--config` 显式传入。

## 步骤 1：安装 agr CLI

公开仓库与安装脚本请参见 [TencentCloudAgentRuntime/ags-cli](https://github.com/TencentCloudAgentRuntime/ags-cli)。安装后请执行 `agr version -o json` 验证命令已加入 `PATH`。

### 方式一：使用脚本快速安装

#### 国内推荐使用以下脚本

curl -fsSL https://dl.tencentags.com/agr-cli/latest/install.sh | sh

agr version -o json --non-interactive

#### 海外可使用 Github 脚本安装（可选）

curl -fsSL https://github.com/TencentCloudAgentRuntime/ags-cli/releases/latest/download/install.sh | sh

agr version -o json --non-interactive

如果不希望直接执行网络脚本，也可以从 [GitHub Releases 页面](https://github.com/TencentCloudAgentRuntime/ags-cli/releases)下载对应平台的压缩包后手动安装。

### 方式二：使用 `go install`

go install github.com/TencentCloudAgentRuntime/ags-cli/cmd/agr@latest

agr version -o json --non-interactive

### 方式三：从源码构建

git clone https://github.com/TencentCloudAgentRuntime/ags-cli.git

cd ags-cli

make build

sudo cp agr /usr/local/bin/agr

agr version -o json --non-interactive

`agr version -o json` 返回 `Version`、`Commit` 和 `BuildTime` 字段，可用于确认当前安装版本。

## 步骤 2：写入本地凭据

`agr init` 只写本地 CLI 配置，不会创建远端资源。

export TENCENTCLOUD_SECRET_ID="<your-secret-id>"

export TENCENTCLOUD_SECRET_KEY="<your-secret-key>"

agr init \

 --secret-id "$TENCENTCLOUD_SECRET_ID" \

 --secret-key "$TENCENTCLOUD_SECRET_KEY" \

 --non-interactive

默认配置文件路径为 `~/.agr/config.toml`。若 Home 目录不可写，可显式指定路径：

agr --config /path/to/agr-config.toml init \

 --secret-id "$TENCENTCLOUD_SECRET_ID" \

 --secret-key "$TENCENTCLOUD_SECRET_KEY" \

 --non-interactive

`agr init` 支持的命令参数可通过以下命令查看：

agr init --help

agr --help

`agr init --help` 会显示命令自身参数，以及 `Global Flags` 小节中的全局参数。CLI 支持的全局参数包括 `--config`、`--cloud-endpoint`、`--domain`、`--region`、`--secret-id`、`--secret-key`、`--non-interactive` 和 `-o/--output`。

## 步骤 3：通过 `agr config set` 调整默认值

`agr config set` 使用扁平键名，不使用 TOML 路径。CLI 支持的键包括：

`secret_id`

`secret_key`

`default_user`

`output`

`region`

`domain`

`cloud_endpoint`

例如：

agr config set region ap-shanghai

agr config set domain tencentags.com

agr config set secret_id "$TENCENTCLOUD_SECRET_ID"

agr config set secret_key "$TENCENTCLOUD_SECRET_KEY"

agr config set default_user user

`agr config set secret_id ...` 会把值写入配置文件中的 `[auth]` 段，`agr config set default_user ...` 会写入 `[sandbox]` 段，但命令行仍然使用扁平键名。

**注意：**

不要写成 `agr config set auth.secret_id ...` 这类 TOML 路径。

如果使用了自定义配置路径，请在同一条命令上附带 `--config /path/to/agr-config.toml`。

## 步骤 4：查看当前配置

完成初始化后，可先查看配置文件路径和当前配置值，再用 `agr status` 检查配置是否已被 CLI 识别。

agr config path

agr config show -o json

agr status -o json

`agr config show -o json` 用于确认配置值及其来源。`agr status -o json` 用于确认 CLI 是否已经识别这些配置。返回结果中可重点确认以下字段：

`Data.ConfigFound`

`Data.ConfigLoaded`

`Data.Auth.SecretId.Present`

`Data.Auth.SecretKey.Present`

`Data.Region`

`Data.Domain`

如果使用了自定义配置路径，检查时需带上同一个 `--config` 参数。

## 步骤 5：诊断鉴权与连通性

当 `agr status` 已经能看到本地配置，但业务命令仍然失败时，使用 `agr doctor` 诊断。

agr doctor -o json

`agr doctor` 输出按检查项组织的结果，常见检查包括：

`SecretId`

`SecretKey`

`TokenCache`

`ConfigFilePermission`

`Connectivity`

如果返回 `AUTH_FAILED` 或其他鉴权类错误，可继续执行：

agr explain AUTH_FAILED -o json

`agr explain` 返回错误含义、退出码、受影响命令以及建议修复动作。

## 认证与配置入口

`agr` CLI 不提供 `agr auth` 或 `agr auth whoami` 子命令。认证与本地配置请使用以下入口：

`agr init`：首次写入本地凭据。

`agr config path`：查看配置文件路径。

`agr config show`：查看当前配置值及其来源。

`agr config set`：按扁平键名更新配置文件中的默认值。

`agr status`：检查配置是否被 CLI 识别。

`agr doctor`：诊断鉴权与连通性。

全局参数发现：`agr init --help` 的 `Global Flags` 小节，以及顶层 `agr --help`。

如果您在旧示例或其他材料中看到 `agr auth` 写法，请以 `agr --help`、`agr init --help` 和 `agr config --help` 的输出为准。

## 验证结果

当以下条件全部满足时，表示安装与配置已完成：

`agr version -o json` 能正常返回版本信息。

`agr status -o json` 显示 `ConfigFound: true` 且凭据字段为 `Present: true`。

`agr doctor -o json` 的 `Connectivity` 检查通过，或失败原因已明确指向待修复的凭据/网络问题。

## 清理或回滚

如果只是临时验证本地环境，完成后可删除测试配置并清理环境变量：

rm -f ~/.agr/config.toml

unset TENCENTCLOUD_SECRET_ID

unset TENCENTCLOUD_SECRET_KEY

如果使用了自定义配置路径，请将 `~/.agr/config.toml` 替换为实际文件路径。
