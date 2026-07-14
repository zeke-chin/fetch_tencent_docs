<!-- source: https://cloud.tencent.com/document/product/436/43816 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:21:31+08:00 -->

# 将个人计算机中的文件备份到 COS

最近更新时间：2024-08-01 17:10:01


## 前言

数据无价，相信很多人都深有体会。数码照片、电子文档、工作产出、游戏存档，哪一样丢失都很头疼。除了硬盘故障导致的文件丢失，人为的误操作、计算机宕机或软件崩溃导致的单一文件丢失，以及被要求“回滚版本”却发现没有保存历史版本的尴尬，都是工作和生活中令人头疼不已的问题。因此，备份的重要性，毋庸置疑。

说起备份，很多人想到的就是使用移动硬盘或者在局域网内搭建 NAS 存储，然后将文件往里面上传就行了。但实际上真的这么简单吗？

备份，其实是一个系统工程。除了将文件复制到备份媒介上，还需要验证备份内容的准确性。而复制与验证这两项工作，还需要定期去执行，这样在发生文件丢失时，才能最大限度挽回损失。此外，备份媒介也是需要去维护的，需要及时将损坏的硬盘进行替换。

综上所述，那么有没有简单的办法可以保证文件的安全呢？答案是肯定的。

随着云服务的发展，我们有可靠的企业级云存储服务，腾讯云对象存储（Cloud Object Storage，COS）就是这样一类服务；随着国家提速降费的号召，宽带越来越快，而且越来越便宜，让我们将文件备份上云成为现实。接下来，我们就需要一款软件，打通计算机中的文件和云存储，将我们的文件定期自动备份到云上，并定期验证备份文件的准确性。

## 软件介绍

[Arq® Backup](https://www.arqbackup.com/) 是一款支持 Windows 和 macOS 系统的商业备份软件，该软件在系统后台运行，根据配置每隔一段时间自动备份指定的目录，同时软件会保留每个时间点备份的文件，因此可以轻松的找到某个文件的历史版本。此外，每个时间点的备份只会备份有差异的文件，对于不同路径的重复文件也只备份一次，使备份体积尽可能小，备份速度尽可能快。在将备份文件传输到网络之前，软件会基于用户输入的密码对备份文件进行加密，保证其在网络传输过程中或在云端存储中都不会被盗用，保证用户敏感数据的安全性。

Arq® Backup 商业授权为49.99美元每个用户，用户购买后可以在单台计算机上使用，同时软件提供30天免费使用，可以试用后再购买。

**说明：**

Arq® Backup 软件目前暂时没有简体中文版，软件的下载、购买和相关说明均可在该软件 [官方网站](https://www.arqbackup.com/) 内查看。

## 准备腾讯云对象存储

**说明：**

若您目前已经在使用 COS，请忽略步骤1 - 2。

1. [注册腾讯云账号](https://cloud.tencent.com/document/product/378/17985) 并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

2. 登录 [对象存储 COS 控制台](https://console.cloud.tencent.com/cos5)，按照提示开通 COS。

3. 在对象存储 COS 控制台中，单击左侧导航栏的**存储桶列表**，然后单击**创建存储桶**，主要配置信息如下：

所属地域：可以根据您所在地就近选择，但是请不要选择金融地域，目前我们对于西南地区有价格上的优惠，因此也可以选择“成都”或“重庆”享受更优惠的价格。例如选择成都地域。

名称：存储桶名称，例如 “backups”。

请求域名：将**请求域名**地址复制保存。 其他配置项保持默认，创建存储桶的详细步骤，请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。

4. 登录 [API 密钥管理控制台](https://console.cloud.tencent.com/cam/capi) ，创建并记录密钥信息 SecretId 和 SecretKey。

## 安装并配置 Arq® Backup

**说明：**

本文以 Windows 的 Arq® Backup 6.2.11版本为例。

1. 从 [Arq® Backup 官网](https://www.arqbackup.com/) 下载软件。

2. 按提示完成软件安装，安装完成后软件会自动启动，首次启动时会提示登录，此时输入邮箱地址并单击 **Start Trial**。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/36e9b14f41e81c682489b506bc31f7b3.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/36e9b14f41e81c682489b506bc31f7b3.png)

3. 在 **Backup** 界面中单击 **Create a new backup plan**，添加备份计划。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/586da5524facebe0924c1beb6db8c8e7.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/586da5524facebe0924c1beb6db8c8e7.png)

4. 在跳转界面，选择需要备份的目录，可以选择所有硬盘或指定目录。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/a89654bb0026f40a1e3035e6aac7c58a.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/a89654bb0026f40a1e3035e6aac7c58a.png)

5. 单击 **Add storage location**，添加备份存储位置，如下图所示。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/276ca95922834197125ee0fe425776d2.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/276ca95922834197125ee0fe425776d2.png)

6. 此处我们选择 **S3-Compatible Server**。

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/08d8273f348749678caaf67419aab946.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/08d8273f348749678caaf67419aab946.png)

7. 在跳转界面中按照以下说明进行配置。配置完毕后，单击 **Continue**。

Server URL：输入上文记录的请求域名中，从`cos`开始的部分，并在前面加上`https://`，例如 `https://cos.ap-chengdu.myqcloud.com`，请注意这里不包含存储桶名称。

Region：输入地域简称，本文举例为成都地域，地域简称为ap-chengdu。更多介绍请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。

Access Key ID：上文记录的密钥信息中的 SecretId。

Secret Access Key：上文记录的密钥信息中的 SecretKey。

8. 在随后的界面中选择 **Use an existing bucket**，并选择上文创建的存储桶，例如 **backups-1250000000**，然后单击 **Save**。

![Image 12](https://qcloudimg.tencent-cloud.cn/image/document/9975a2a7a8ac87539296c961c8d7f17e.png)

![Image 13](https://qcloudimg.tencent-cloud.cn/image/document/9975a2a7a8ac87539296c961c8d7f17e.png)

9. （可选）选择是否加密备份数据，此处我们选择**开启**按钮。

![Image 14](https://qcloudimg.tencent-cloud.cn/image/document/220cea8bd37cba437866c1c3c5992a8d.png)

![Image 15](https://qcloudimg.tencent-cloud.cn/image/document/220cea8bd37cba437866c1c3c5992a8d.png)

10. 在弹窗中设置用于加密的密码。输入两次用于加密备份文件的密码，并单击 **OK**。**注意请牢记备份密码，否则将无法从备份恢复文件！**

![Image 16](https://qcloudimg.tencent-cloud.cn/image/document/fdf7a23039f0207a3223b4fde94f8170.png)

![Image 17](https://qcloudimg.tencent-cloud.cn/image/document/fdf7a23039f0207a3223b4fde94f8170.png)

11. （可选）设置备份周期。

![Image 18](https://qcloudimg.tencent-cloud.cn/image/document/508573f49e54403583326146966be391.png)

![Image 19](https://qcloudimg.tencent-cloud.cn/image/document/508573f49e54403583326146966be391.png)

12. 单击 **Save**保存设置，然后单击 **Back Up Now**开始备份。

![Image 20](https://qcloudimg.tencent-cloud.cn/image/document/23db1f57fbe3b53a5e03ae8613bda505.png)

![Image 21](https://qcloudimg.tencent-cloud.cn/image/document/23db1f57fbe3b53a5e03ae8613bda505.png)

## 从备份中恢复文件

1. 在主界面左侧 **Backup** 列表中，单击 **Restore**。

![Image 22](https://qcloudimg.tencent-cloud.cn/image/document/71e002a55b997c11930df1f9458624c6.png)

![Image 23](https://qcloudimg.tencent-cloud.cn/image/document/71e002a55b997c11930df1f9458624c6.png)

2. 如果按照上面第9步设置了加密备份数据，则需要输入密码。

![Image 24](https://qcloudimg.tencent-cloud.cn/image/document/9de2b5e31c6d9e19e9f71adc3031d149.png)

![Image 25](https://qcloudimg.tencent-cloud.cn/image/document/9de2b5e31c6d9e19e9f71adc3031d149.png)

3. 选择要恢复的目录或文件，以及保存恢复目录或文件的位置，单击 **Restore** 开始恢复。

![Image 26](https://qcloudimg.tencent-cloud.cn/image/document/78f5e186600f701fec18b03ac191dd6c.png)

![Image 27](https://qcloudimg.tencent-cloud.cn/image/document/78f5e186600f701fec18b03ac191dd6c.png)

4. 恢复操作默认是从最新的备份中恢复，如果有需要，可以从快照中找到历史版本的备份，并从历史版本的备份中恢复。单击 **Snapshots** 查看历史快照。

![Image 28](https://qcloudimg.tencent-cloud.cn/image/document/6ce512197cab1b4b7bbad1734dad08ea.png)

![Image 29](https://qcloudimg.tencent-cloud.cn/image/document/6ce512197cab1b4b7bbad1734dad08ea.png)

5. 选择历史快照。

![Image 30](https://qcloudimg.tencent-cloud.cn/image/document/b3f182bc6d2212ae95e7283b414d5250.png)

![Image 31](https://qcloudimg.tencent-cloud.cn/image/document/b3f182bc6d2212ae95e7283b414d5250.png)

6. 选择要恢复的历史目录或文件，以及保存恢复目录或文件的位置，单击 **Restore** 开始恢复。

7. 等待界面提示恢复完成，即可到刚才指定的目录中查看恢复的文件。

## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击“[此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406)”一键启动，立即使用！
