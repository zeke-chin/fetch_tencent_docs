<!-- source: https://cloud.tencent.com/document/product/436/112176 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:20:17+08:00 -->

# 使用自定义 SCF 函数配置 COS 存储桶加密配置巡检实践

最近更新时间：2025-08-26 17:50:22


## 简介

您可使用自定义 SCF 函数，配置 COS 存储桶加密巡检。配置成功后，您的存储桶可实现审计和治理。了解更多请参见 [配置审计](https://cloud.tencent.com.cn/document/faq/1579/82727)。

## 准备工作

下载 [Inspecting-cos-bucket-encryption.zip 压缩包](https://cosbrowser-1253960454.cos.ap-shanghai.myqcloud.com/software/Inspecting-cos-bucket-encryption/Inspecting-cos-bucket-encryption.zip)。

## 操作步骤

### 步骤1：创建云函数

1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default)，在左侧导航栏中单击**函数服务**，进入函数列表页。

2. 创建云函数。单击**新建**，创建云函数。需要配置以下选项：

选择模板：模板类型选择**从头开始**。

基础配置：

函数类型：选择**事件函数**。

函数名称：可使用默认函数名称，或自定义函数名称。

地域：选择**存储桶所在地域**。以下将以**广州**为例，进行说明。

运行环境：选择 **Go 1**。

时区：使用默认的设置 **UTC**。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/9f69abb186b3b5491a5da2ea6d5d4dda.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/9f69abb186b3b5491a5da2ea6d5d4dda.png)

函数代码：

提交方法：选择**本地上传 zip 包**，上传准备工作中下载的 zip 包。

执行方法：使用默认的设置 **main**。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/b09de3aa98047b0258524072acdde465.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/b09de3aa98047b0258524072acdde465.png)

日志配置：无需设置。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/0eb025be40ec09248b44dad78034fc5a.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/0eb025be40ec09248b44dad78034fc5a.png)

 高级配置：单击**高级配置**选项，并展开配置详情。在**权限配置**中，单击**启用**运行角色。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/5312eba49da768a6111f2e5ac311d97d.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/5312eba49da768a6111f2e5ac311d97d.png)

3. 同意授权，并**提交**。

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/6dbfbd21b8618c1d42c8096137c6dcd1.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/6dbfbd21b8618c1d42c8096137c6dcd1.png)

4. 单击**新建运行角色。**

![Image 12](https://qcloudimg.tencent-cloud.cn/image/document/8c977d210540bef04a46e7cab2979917.png)

![Image 13](https://qcloudimg.tencent-cloud.cn/image/document/8c977d210540bef04a46e7cab2979917.png)

### 步骤2：**新建自定义角色**

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam)，单击**角色**>**新建角色**>**腾讯云产品服务**。在**新建自定义角色**页面中，产品服务搜索并选择**云函数（scf）**，单击**下一步**。

![Image 14](https://qcloudimg.tencent-cloud.cn/image/document/4406bfcad2cc99217ad575175a99be40.png)

![Image 15](https://qcloudimg.tencent-cloud.cn/image/document/4406bfcad2cc99217ad575175a99be40.png)

2. 在策略列表中搜索 **QcloudCOSBucketConfigRead** 策略和 **QcloudConfigFullAccess**策略并勾选。完成后单击**下一步**。

![Image 16](https://qcloudimg.tencent-cloud.cn/image/document/097bb3a3ddf33d5d5f79a804db9d6ad4.png)

![Image 17](https://qcloudimg.tencent-cloud.cn/image/document/097bb3a3ddf33d5d5f79a804db9d6ad4.png)

3. 可根据实际情况选择是否配置角色标签。此步骤非必要。完成后，单击**下一步**。

4. 在**审阅**页面，设置角色名称，单击**完成**。至此，已完成新建自定义角色的全部操作。

![Image 18](https://qcloudimg.tencent-cloud.cn/image/document/497024d615be0c810c7c8243cd95589a.png)

![Image 19](https://qcloudimg.tencent-cloud.cn/image/document/497024d615be0c810c7c8243cd95589a.png)

5. 返回云函数创建页面。在权限配置的运行角色里，刷新运行角色。随后，选择之前新建的角色。

![Image 20](https://qcloudimg.tencent-cloud.cn/image/document/bfa832cd3aa7c51833aabe38bac26555.png)

![Image 21](https://qcloudimg.tencent-cloud.cn/image/document/bfa832cd3aa7c51833aabe38bac26555.png)

6. 勾选服务协议。完成以上配置后，勾选协议。单击**完成**，云函数的创建成功。

![Image 22](https://qcloudimg.tencent-cloud.cn/image/document/18fe46289ae6b5b6bb544ba83b73ecc0.png)

![Image 23](https://qcloudimg.tencent-cloud.cn/image/document/18fe46289ae6b5b6bb544ba83b73ecc0.png)

### 步骤3：新建自定义规则

1. 在 [配置审计](https://console.cloud.tencent.com/cfa/) 控制台，单击**规则**页面。选择**新建规则**>**新建自定义规则**，进入规则配置页面。

![Image 24](https://qcloudimg.tencent-cloud.cn/image/document/a34dc13e269ec3c72acf874b74cbcdbe.png)

![Image 25](https://qcloudimg.tencent-cloud.cn/image/document/a34dc13e269ec3c72acf874b74cbcdbe.png)

2. 在自定义规则配置中的**基本属性**页面**，**配置基本信息，选择刚刚部署好的云函数，并单击**下一步**。

![Image 26](https://qcloudimg.tencent-cloud.cn/image/document/23055398f9f24a0603fe499c14f8a788.png)

![Image 27](https://qcloudimg.tencent-cloud.cn/image/document/23055398f9f24a0603fe499c14f8a788.png)

3. 在**关联资源**页面，按资源类型选择 **COS 对象存储**。

![Image 28](https://qcloudimg.tencent-cloud.cn/image/document/819ffd52868f45c59391f29a24c5fd62.png)

![Image 29](https://qcloudimg.tencent-cloud.cn/image/document/819ffd52868f45c59391f29a24c5fd62.png)

**按标签**。如果需要巡检指定标签的存储桶，可以在对象存储 COS 控制台 [存储桶列表页](https://console.cloud.tencent.com/cos/bucket)，对需要巡检的存储桶设置标签 。

 进入存储桶列表页。

![Image 30](https://qcloudimg.tencent-cloud.cn/image/document/8da5166e94cd250fe1050b20e8e3607c.png)

![Image 31](https://qcloudimg.tencent-cloud.cn/image/document/8da5166e94cd250fe1050b20e8e3607c.png)

设置存储桶的标签。

![Image 32](https://qcloudimg.tencent-cloud.cn/image/document/520cdafb368a9dc7d1b5b360d7b49a3c.png)

![Image 33](https://qcloudimg.tencent-cloud.cn/image/document/520cdafb368a9dc7d1b5b360d7b49a3c.png)

选择对应的标签，完成操作。

![Image 34](https://qcloudimg.tencent-cloud.cn/image/document/a6efbf9503030312c98b036ac9c26041.png)

![Image 35](https://qcloudimg.tencent-cloud.cn/image/document/a6efbf9503030312c98b036ac9c26041.png)

**按地域**。如果需要巡检指定地域的桶可配置此字段。例如：需要巡检广州地域的存储桶，可以在**按地域**下拉菜单中选择广州。

![Image 36](https://qcloudimg.tencent-cloud.cn/image/document/593b9fd2d32d674ef83462f64a658856.png)

![Image 37](https://qcloudimg.tencent-cloud.cn/image/document/593b9fd2d32d674ef83462f64a658856.png)

4. 在完成上一步骤配置后，单击**下一步，**进入**触发机制：**

**规则触发机制**：选择**周期执行**。

**规则触发条件**：根据实际情况选择，最小可选择**1 小时**。

![Image 38](https://qcloudimg.tencent-cloud.cn/image/document/7880e0441de42eb2df2f41943474a86d.png)

![Image 39](https://qcloudimg.tencent-cloud.cn/image/document/7880e0441de42eb2df2f41943474a86d.png)

5. **参数设置**：无需配置，跳过。

6. **预览并保存**：无需配置，直接单击确认。至此，已完成了自定义规则的新建。

### 步骤5：设置投递服务

1. 在 [配置审计](https://console.cloud.tencent.com/cfa) 控制台，单击**设置**>**投递服务**。开启后，配置巡检的结果将投递至 CLS。

**注意：**

如果您还未开启配置审计服务，请根据提示开通即可。

目前巡检结果仅支持每天凌晨零点15分定时投递。

2. 详细配置如下：

**选择投递类型**：选择**日志服务 CLS**。

**投递服务名称**：自定义即可。

**投递内容：**选择**配置变更历史**。

**日志主题**：选择**使用已有**或新建均可。下文将以使用已有为例进行说明。

**地域**：选择日志主题所在的地域。

**日志主题名称**：按需配置日志主题的名称。

![Image 40](https://qcloudimg.tencent-cloud.cn/image/document/d51c657b3fba85960f31d5ba9710b4b9.png)

![Image 41](https://qcloudimg.tencent-cloud.cn/image/document/d51c657b3fba85960f31d5ba9710b4b9.png)

至此，您已完成全部配置。

3. 在[配置审计](https://console.cloud.tencent.com/cfa)控制台，单击**规则，**可查看实践结果如下。

![Image 42](https://qcloudimg.tencent-cloud.cn/image/document/f7557b3b7d3683d4b80decb9ebaa6f84.png)

![Image 43](https://qcloudimg.tencent-cloud.cn/image/document/f7557b3b7d3683d4b80decb9ebaa6f84.png)
