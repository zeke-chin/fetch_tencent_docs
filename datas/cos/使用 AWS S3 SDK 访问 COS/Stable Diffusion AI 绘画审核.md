<!-- source: https://cloud.tencent.com/document/product/436/122410 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:18:54+08:00 -->

# Stable Diffusion AI 绘画审核

最近更新时间：2025-12-30 10:10:52


## 概述

腾讯云 Serverless 应用中心 提供了 stable-diffusion-webui 项目的 Serverless 化部署能力。该应用创建成功后，您可以使用 stable diffusion webui 的全部能力，例如文生图、图生图，以及 Lora、ControlNet 等高阶能力。本文将介绍如何通过图片审核服务对应用生成的图片做内容合规检测。

## 前提条件

登录 [Serverless 应用控制台](https://console.cloud.tencent.com/sls)，开通 Serverless 产品服务。

开通对象存储产品服务，并创建一个存储桶，详见 [新手指引](https://cloud.tencent.com/document/product/436/38484)。

进入 [数据万象控制台](https://console.cloud.tencent.com/ci)，开通数据万象服务。

## 操作步骤

### 步骤一：通过 Stable Diffusion AI 应用生成图片

#### 创建 Stable Diffusion AI 应用

1. 登录 Serverless 控制台，选择左侧导航栏中的 [Serverless 应用](https://console.cloud.tencent.com/sls)，在 Serverless 应用页面，单击**新建应用**。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/8075ec966945568d4eade6b295eb693e.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/8075ec966945568d4eade6b295eb693e.png)

2. 在**新建应用**页面，根据页面相关信息提示进行配置:

**创建方式**：选择**应用市场**。

**模板**：选择 **Stable Diffusion AI 绘画**。如下图所示：

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/ca254b8a50a5b4384b922c47166273b7.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/ca254b8a50a5b4384b922c47166273b7.png)

3. 单击**下一步**，根据页面相关信息提示进行配置：

**应用名**：例如 “aigc-auditing-server”。

**地域**：例如 “北京”。

**应用类型**：选择 **SD API（无Web UI）**的方式，通过 API 调用。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/58b88a1ec54097b3cd592d53adb20e40.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/58b88a1ec54097b3cd592d53adb20e40.png)

4. 单击**完成**，查看**部署日志**页面，等待部署，即可完成应用创建、函数创建以及 API 网关触发器创建。函数服务显示正常，即创建完成，如下图所示：

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/b14dfd9028a9bb33c6e8d4ebcdc1313f.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/b14dfd9028a9bb33c6e8d4ebcdc1313f.png)

#### 使用 Stable Diffusion AI 应用生成图片

您可以使用平台测试模板或API接口两种方式生成图片：

##### 使用平台测试模板生成图片

通过控制台中的应用测试页面，您可以测试生成图片，按如下配置：

**请求方式**：POST

**path**: /sdapi/v1/txt2img

**Content-Type**: application/json

**body**: 传入绘图的参数，如 prompt

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/893109f746fbddb5baf76042092eba1c.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/893109f746fbddb5baf76042092eba1c.png)

##### 使用API接口生成图片（以 Python 为例）

url：设置函数服务的访问路径。

body：设置绘图参数。

图像转换可以安装 pillow，推荐使用 pip 安装。

pip install pillow

代码示例：

import json

import requests

import io

import base64

from PIL import Image, PngImagePlugin

url = "https://service.*********.tencentcs.com/release/"

# 文生图接口

path='sdapi/v1/txt2img'

# 绘图参数

body = {

 "prompt": "1 girl, upper body, look at viewer",

 "steps": 20

 }

# API请求

response = requests.post(url=f'{url}{path}', json=body)

r = response.json()

# 保存生成的图片

if 'images' in r:

 for i in r['images']:

 image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

 png_payload = {

 "image": "data:image/png;base64," + i

 }

 response2 = requests.post(url=f'{url}sdapi/v1/png-info', json=png_payload)

 pnginfo = PngImagePlugin.PngInfo()

 pnginfo.add_text("parameters", response2.json().get("info"))

 image.save('output.png', pnginfo=pnginfo)

生成图片示例如下所示：

![Image 12](https://qcloudimg.tencent-cloud.cn/image/document/bf31db3304f430894ade5c8475df8da1.png)

![Image 13](https://qcloudimg.tencent-cloud.cn/image/document/bf31db3304f430894ade5c8475df8da1.png)

![Image 14](https://qcloudimg.tencent-cloud.cn/image/document/901df453db1d56791e0e4040943c5dc7.png)

![Image 15](https://qcloudimg.tencent-cloud.cn/image/document/901df453db1d56791e0e4040943c5dc7.png)

更多细节可参考 [部署 Stable Diffusion AI 绘画应用（自定义模型版）](https://cloud.tencent.com/document/product/1154/95431)。

### 步骤二：通过数据万象图片审核接口进行审核

#### 图片审核概述

[图片批量审核接口](https://cloud.tencent.com/document/product/460/63594) 支持同步、异步请求方式，您可以通过本接口对多个图片文件进行内容审核，该接口属于 POST 请求。

#### 图片审核调用示例（以Python为例）

依赖 qcloud_cos 使用 pip 安装（推荐）。

pip install -U cos-python-sdk-v5

代码示例：

import sys import os import logging import base64 from qcloud_cos import CosConfig from qcloud_cos import CosS3Client from qcloud_cos.cos_comm import CiDetectType

# 正常情况日志级别使用 INFO，需要定位时可以修改为 DEBUG，此时 SDK 会打印和服务端的通信信息

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 设置用户属性, 包括 secret_id, secret_key, region等。Appid 已在 CosConfig 中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成。

secret_id = os.environ['COS_SECRET_ID'] # 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见：https://cloud.tencent.com/document/product/598/37140

 secret_key = os.environ['COS_SECRET_KEY'] # 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见：https://cloud.tencent.com/document/product/598/37140

 region = 'ap-beijing' # 替换为用户的 region，已创建桶归属的 region 可以在控制台查看：https://console.cloud.tencent.com/cos5/bucket token = None # 如果使用永久密钥不需要填入 token，如果使用临时密钥需要填入，临时密钥生成和使用指引参见：https://cloud.tencent.com/document/product/436/14048

 scheme = 'https' # 指定使用 http/https 协议来访问 COS，默认为 https，可不填

 bucket_name='test' # 指定cos桶中bucket的名称

 config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme) client = CosS3Client(config) # 创建 cos client

 img_path='./output.png' # 生成的图片路径

 with open(img_path, 'rb') as file: data = file.read() base64_data = base64.b64encode(data).decode("utf-8") # 将数据转换为Base64编码 response = client.ci_auditing_image_batch( # 调用审核接口 Bucket=bucket_name, DetectType=CiDetectType.PORN, Input=[ { 'Content':base64_data, #图像数据的base64编码 } ] ) print(response)

其他细节，请参考 [图片批量审核](https://cloud.tencent.com/document/product/460/63594) 。

#### 图片审核结果

![Image 16](https://qcloudimg.tencent-cloud.cn/image/document/48b9a8ebe257c54262ad6d86ba5de027.png)

![Image 17](https://qcloudimg.tencent-cloud.cn/image/document/48b9a8ebe257c54262ad6d86ba5de027.png)
