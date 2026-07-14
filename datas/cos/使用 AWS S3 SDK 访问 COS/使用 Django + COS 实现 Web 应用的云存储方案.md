<!-- source: https://cloud.tencent.com/document/product/436/93212 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:22:06+08:00 -->

# 使用 Django + COS 实现 Web 应用的云存储方案

最近更新时间：2025-06-30 14:49:01


## 简介

[Django](https://www.djangoproject.com/) 是一个基于 Python 的开源 Web 应用框架，它的出现极大地简化了 Web 应用的开发过程。为了更好地满足现代 Web 应用的需求，Django 提供了很多扩展功能，其中包括云存储。

本文主要介绍如何使用 COS 插件实现远程附件功能，将 Django 应用的数据存储在腾讯云 [对象存储（Cloud Object Storage，COS）](https://cloud.tencent.com/product/cos)上。

## 前提条件

已有 COS 存储桶。如无，可参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 操作指引。

已创建服务器。例如云服务器（Cloud Virtual Machine，CVM）。相关指引可参见 [CVM 产品文档](https://cloud.tencent.com/document/product/213)。

## 环境依赖

Python 版本：大于等于3.8版本。本文以 Python 3.12.0版本举例说明。

COS Python 版本：大于等于1.9.31版本。安装方法请参见 [COS Python SDK 快速入门](https://cloud.tencent.com/document/product/436/12269)。本文以 COS Python 1.9.31版本举例说明。

Django 版本：大于等于2.2，小于3.3版本。本文以3.2.18版本举例说明。

## 实践步骤

### 创建 COS 存储桶

1. 创建一个访问权限为**公有读私有写**的存储桶，存储桶的地域建议与运行 Django 的 CVM 地域相同，创建详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。

2. 在存储桶列表中找到刚刚创建的存储桶，并获取存储桶名称，例如 examplebucket-1250000000。

### 创建 Django

1. 前往 [PyCharm 官网](https://www.jetbrains.com.cn/en-us/pycharm/download/#section=windows)，并按照您所使用的 CVM 系统选择对应的 PyCharm 版本。

2. 在 CVM 中安装后打开 PyCharm，单击 NEW project 或者 create project，选择下面的 Django。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/c13447ffc7dd4d4571bae080d910e357.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/c13447ffc7dd4d4571bae080d910e357.png)

3. 创建后，在您的目录下找到并打开 setting.py 文件。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/aa954f17708eef79539d414a8b640c27.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/aa954f17708eef79539d414a8b640c27.png)

4. 将以下代码复制粘贴进去，并按照参数说明进行 COS 服务配置。

DEFAULT_FILE_STORAGE = "django_cos_storage.TencentCOSStorage"

TENCENTCOS_STORAGE = {

 "BUCKET": "xxx",

 "CONFIG": {

 "Region": "ap-guangzhou",

 "SecretId": "xxxx",

 "SecretKey": "xxxx",

 }

}

参数说明如下：

配置项 配置值
Bucket 创建存储桶时自定义的名称，例如 examplebucket-1250000000。
Region 创建存储桶时所选择的地域。
SecretId 访问密钥信息，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中创建和获取，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。详情请参见 [子账号访问密钥管理](https://cloud.tencent.com/document/product/598/37140)。
SecretKey 访问密钥信息，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中创建和获取，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。详情请参见 [子账号访问密钥管理](https://cloud.tencent.com/document/product/598/37140)。

### 下载和配置 COS 插件

1. 前往 [Github](https://github.com/Tencent-Cloud-Plugins/tencentcloud-django-plugin-cos/archive/refs/heads/master.zip) 下载 COS 插件。下载后将 django_cos_storage 这个目录解压到 django 项目的目录下。

**说明：**

如需查看其插件信息，打开 terminal，输入 `pip freeze`，即可查看其模块信息。

2. 在 django_cos_storage 目录下创建一个 py 文件，例如 COSStorage.py。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/81ddf6a13636a4b26f658e62b7d10c32.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/81ddf6a13636a4b26f658e62b7d10c32.png)

将以下代码复制粘贴进去。

from .storage import TencentCOSStorage

from functools import wraps

def decorator(cls):

 instance = None

 @wraps(cls)

 def inner(*args,**kwargs):

 nonlocal instance

 if not instance:

 instance = cls(*args,**kwargs)

 return instance

 return inner

@decorator

class QFStorage:

 def  __init__ (self):

 pass

 self.storage =TencentCOSStorage()

 self.bucket =self.storage.bucket

 self.client =self.storage.client

 #上传对象

 def upload_file(self, Key, LocalFilePath, PartSize=1, MAXThread=5, EnableMD5=False):

 try:

 response =self.client.upload_file(

 Bucket=self.bucket,

 Key=Key,

 LocalFilePath=LocalFilePath,

 PartSize=PartSize,

 MAXThread=MAXThread,

 EnableMD5=EnableMD5

 )

 return response

 except Exception as e:

 print('上传对象失败，error:',e)

 return None

3. 打开 app_cos 目录下的 views.py。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/1ee5cc59079b2d29e8442e5bf3af514a.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/1ee5cc59079b2d29e8442e5bf3af514a.png)

将以下代码复制粘贴进去。

from django.shortcuts import render,redirect

from django.http import HttpResponse

from django_cos_storage.COSStorage import QFStorage

from django.conf import settings

#上传对象

def upload_file_view(request):

 response = QFStorage().upload_file(

 Key='1.png',

 LocalFilePath=settings.BASE_DIR / 'cessu/1.png'

 )

 if response:

 return HttpResponse('上传文件成功！')

 return HttpResponse('上传文件失败')

**注意：**

这里示例中 `cessu/1.png` 表示要上传的本地文件`1.png`位于项目目录下的 `cessu` 文件夹中 。上传成功后，您可以在 COS 存储桶的 cessu 文件夹中找到图片1.png。

4. 在 djangoProject2 目录下找到并打开 urls.py。

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/53df27ec25123607d6dffae9793f82c2.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/53df27ec25123607d6dffae9793f82c2.png)

将代码复制粘贴进去。

from django.contrib import admin

from django.urls import path

from app_cos.views import *

urlpatterns = [

 path('admin/', admin.site.urls),

 path('upload_file/', upload_file_view),

]

5. 在 terminal 中输入 `python manage.py migrate`并执行。

6. 在 terminal 中输入 `python manage.py createsuperuser`，按照提示输入账号密码即可。

**注意：**

如果执行`python manage.py createsuperuser`时提示缺少 pkg_resources，请执行安装命令`pip install setuptools`进行解决。

![Image 12](https://qcloudimg.tencent-cloud.cn/image/document/0fc0e0b50100a3ffb46f79ac6740f3e4.png)

![Image 13](https://qcloudimg.tencent-cloud.cn/image/document/0fc0e0b50100a3ffb46f79ac6740f3e4.png)

7. 然后在 terminal 中输入 `python .\manage.py runserver` 运行。

![Image 14](https://qcloudimg.tencent-cloud.cn/image/document/b7caa7d0e649954e0cafa7ae87c8b51d.png)

![Image 15](https://qcloudimg.tencent-cloud.cn/image/document/b7caa7d0e649954e0cafa7ae87c8b51d.png)

8. 打开网站`http://127.0.0.1:8000/admin/`，并输入刚才设置的账号密码即可完成登录。

![Image 16](https://qcloudimg.tencent-cloud.cn/image/document/bd0440bb625fca1217b378b807507488.png)

![Image 17](https://qcloudimg.tencent-cloud.cn/image/document/bd0440bb625fca1217b378b807507488.png)

**注意：**

若打开网站提示报错如下：

![Image 18](https://qcloudimg.tencent-cloud.cn/image/document/fbf77ff4a41763535528cdda736d43c5.png)

![Image 19](https://qcloudimg.tencent-cloud.cn/image/document/fbf77ff4a41763535528cdda736d43c5.png)

 返回 pycharm，重新打开 terminal，依次输入如下：

python manage.py makemigrations

python manage.py migrate

最后在 terminal 中输入 `python .\manage.py runserver` 运行，然后打开 `http://127.0.0.1:8000/admin/` 即可。

### 验证 Django 附件存储到 COS

1. 访问 `http://127.0.0.1:8000/upload_file`，完成上传文件操作。当提示如下图所示，则表示上传成功。

![Image 20](https://qcloudimg.tencent-cloud.cn/image/document/b51379e0990fe5bda2f93f6b77286a7e.png)

![Image 21](https://qcloudimg.tencent-cloud.cn/image/document/b51379e0990fe5bda2f93f6b77286a7e.png)

2. 登录 COS 控制台，选择之前创建的存储桶，在 cessu 路径下即可看到已上传的图片。

## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击“[此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406)”一键启动，立即使用！
