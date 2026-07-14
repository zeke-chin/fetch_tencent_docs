<!-- source: https://cloud.tencent.com/document/product/436/35059 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:23:38+08:00 -->

Title: 对象存储 预签名 URL_腾讯云

URL Source: https://cloud.tencent.com/document/product/436/35059

Markdown Content:
腾讯云
大模型
最新活动
产品
解决方案
定价
企业中心
云市场
开发者
更多
域名
中国站
文档
备案
控制台
登录
免费注册
对象存储
动态与公告
产品简介
购买指南
快速入门
操作指南
工具指南
实践教程
数据湖存储
向量存储与检索
智能体存储
数据处理
功能体验
故障处理
API 文档
SDK 文档
SDK 概览
准备工作
Android SDK
C SDK
iOS SDK
C++ SDK
.NET(C#) SDK
Flutter SDK
Go SDK
快速入门
Go SDK 常见问题
存储桶操作
对象操作
上传对象
下载对象
复制与移动对象
列出对象
删除对象
判断对象是否存在
查询对象元数据
对象访问 URL
预签名 URL
恢复归档对象
服务端加密
客户端加密
异地容灾
数据管理
访问管理
数据校验
云查毒
图片处理
媒体处理
内容审核
AI 内容识别
文档预览
文件处理
智能检索 MetaInsight
任务与工作流
设置访问域名（CDN/全球加速）
异常处理
Java SDK
JavaScript SDK
Node.js SDK
PHP SDK
Python SDK
React Native SDK
小程序 SDK
鸿蒙(Harmony) SDK
终端 SDK 质量优化
错误码
常见问题
相关协议
附录
联系我们
词汇表
文档中心入门中心API 中心SDK 中心文档活动我的反馈
文档反馈官招募中，报名立赚积分兑换代金券！> HOT
文档中心>对象存储>SDK 文档>Go SDK>对象操作>预签名 URL
预签名 URL

最近更新时间：2026-04-14 15:06:42

我的收藏
本页目录：
简介
注意事项
相关示例
获取请求预签名 URL
方法原型
参数说明
返回结果说明
使用案例：永久密钥预签名上传请求
使用案例：永久密钥预签名下载请求
使用案例：临时密钥预签名上传请求
使用案例：临时密钥预签名下载请求
使用案例：自定义域名预签名下载请求
使用案例：预签名添加请求参数或请求头部
使用案例：通过预签名分块上传文件
简介
Go SDK 提供获取请求预签名 URL 接口，详细操作请查看本文示例。
关于使用预签名 URL 上传的说明请参见 预签名授权上传，使用预签名 URL 下载的说明请参见 预签名授权下载。
注意事项
2024年1月1日后创建的桶 不支持使用默认域名在浏览器预览文件，建议您配置自定义域名，详情请参见 存储桶切换自定义域名。
建议用户使用临时密钥生成预签名，通过临时授权的方式进一步提高预签名上传、下载等请求的安全性。申请临时密钥时，请遵循 最小权限原则，防止泄露目标存储桶或对象之外的资源。
如果您一定要使用永久密钥来生成预签名，建议永久密钥的权限范围仅限于上传或下载操作，以规避风险。
相关示例
功能名称

描述

示例代码


生成预签名 URL

对象存储（Cloud Object Storage，COS）支持使用预签名 URL 进行对象的上传、下载，原理是将签名嵌入 URL 生成签名链接。

﻿GitHub 完整示例﻿


分块上传预签名 URL

通过预签名 URL 进行对象的分块上传，包括初始化分块，上传分块，完成分块的预签名生成。

﻿GitHub 完整示例﻿
获取请求预签名 URL
方法原型
func (s *ObjectService) GetPresignedURL(ctx context.Context, httpMethod, key, ak, sk string, expired time.Duration, opt interface{}, signHost ...bool) (*url.URL, error)
参数说明
type PresignedURLOptions struct {
    Query      *url.Values
    Header     *http.Header
}
参数名称

类型

描述


httpMethod

string

HTTP 请求方法


key

string

对象键（Key）是对象在存储桶中的唯一标识，详情请参见 对象键（注意：用户无需对 key 进行编码操作）


ak

string

SecretId


sk

string

SecretKey


expired

time.Duration

签名有效时长


opt

interface{}

扩展项，建议填写 *PresignedURLOptions 类型的参数。可填 nil


PresignedURLOptions

struct

指定签入的请求参数和请求头部


Query

struct

签名中要签入的请求参数


Header

struct

签名中要签入的请求头部


signHost

bool

可选参数，默认为 true，获取签名时是否签入 Header Host；您也可以选择不签入 Header Host，但可能导致请求失败或安全漏洞
返回结果说明
该方法返回值为预签名的下载 URL。
使用案例：永久密钥预签名上传请求
package main
﻿

import (
        "context"
        "github.com/tencentyun/cos-go-sdk-v5"
        "net/http"
        "net/url"
        "os"
        "strings"
        "time"
)
﻿

func main() {
        // 存储桶名称，由 bucketname-appid 组成，appid 必须填入，可以在 COS 控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket
        // 替换为用户的 region，存储桶 region 可以在 COS 控制台“存储桶概览”查看 https://console.cloud.tencent.com/ ，关于地域的详情见 https://cloud.tencent.com/document/product/436/6224 。
        u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
        b := &cos.BaseURL{BucketURL: u}
        client := cos.NewClient(b, &http.Client{
                Transport: &cos.AuthorizationTransport{
                        // 通过环境变量获取密钥
                        // 环境变量 SECRETID 表示用户的 SecretId，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
                        SecretID: os.Getenv("SECRETID"),  // 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
                        // 环境变量 SECRETKEY 表示用户的 SecretKey，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
                        SecretKey: os.Getenv("SECRETKEY"),  // 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
                },
        })
﻿

        // 通过环境变量获取密钥
        // 环境变量 SECRETID 表示用户的 SecretId，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
        ak := os.Getenv("SECRETID")  // 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
        // 环境变量 SECRETKEY 表示用户的 SecretKey，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
        sk := os.Getenv("SECRETKEY")  // 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
﻿

        name := "exampleobject"
        ctx := context.Background()
        f := strings.NewReader("test")
﻿

        // 1. 通过普通方式上传对象
        _, err := client.Object.Put(ctx, name, f, nil)
        if err != nil {
                panic(err)
        }
        // 获取预签名 URL
        presignedURL, err := client.Object.GetPresignedURL(ctx, http.MethodPut, name, ak, sk, time.Hour, nil)
        if err != nil {
                panic(err)
        }
        // 2. 通过预签名方式上传对象
        data := "test upload with presignedURL"
        f = strings.NewReader(data)
        req, err := http.NewRequest(http.MethodPut, presignedURL.String(), f)
        if err != nil {
                panic(err)
        }
        // 用户可自行设置请求头部
        req.Header.Set("Content-Type", "text/html")
        _, err = http.DefaultClient.Do(req)
        if err != nil {
                panic(err)
        }
}
使用案例：永久密钥预签名下载请求
package main
﻿

import (
        "bytes"
        "context"
        "errors"
        "github.com/tencentyun/cos-go-sdk-v5"
        "io"
        "net/http"
        "net/url"
        "os"
        "time"
)
﻿

func main() {
        // 存储桶名称，由 bucketname-appid 组成，appid 必须填入，可以在 COS 控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket
        // 替换为用户的 region，存储桶 region 可以在 COS 控制台“存储桶概览”查看 https://console.cloud.tencent.com/ ，关于地域的详情见 https://cloud.tencent.com/document/product/436/6224 。
        u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
        b := &cos.BaseURL{BucketURL: u}
        client := cos.NewClient(b, &http.Client{
                Transport: &cos.AuthorizationTransport{
                        // 通过环境变量获取密钥
                        // 环境变量 SECRETID 表示用户的 SecretId，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
                        SecretID: os.Getenv("SECRETID"),  // 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
                        // 环境变量 SECRETKEY 表示用户的 SecretKey，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
                        SecretKey: os.Getenv("SECRETKEY"),  // 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
                },
        })
﻿

        // 通过环境变量获取密钥
        // 环境变量 SECRETID 表示用户的 SecretId，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
        ak := os.Getenv("SECRETID")  // 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
        // 环境变量 SECRETKEY 表示用户的 SecretKey，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
        sk := os.Getenv("SECRETKEY") // 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
        name := "exampleobject"
        ctx := context.Background()
        // 1. 通过普通方式下载对象
        resp, err := client.Object.Get(ctx, name, nil)
        if err != nil {
                panic(err)
        }
        bs, _ := io.ReadAll(resp.Body)
        resp.Body.Close()
        // 获取预签名 URL
        presignedURL, err := client.Object.GetPresignedURL(ctx, http.MethodGet, name, ak, sk, time.Hour, nil)
        if err != nil {
                panic(err)
        }
        // 2. 通过预签名 URL下载对象
        resp2, err := http.Get(presignedURL.String())
        if err != nil {
                panic(err)
        }
        bs2, _ := io.ReadAll(resp2.Body)
        resp2.Body.Close()
        if bytes.Compare(bs2, bs) != 0 {
                panic(errors.New("content is not consistent"))
        }
}
使用案例：临时密钥预签名上传请求
package main
﻿

import (
    "context"
    "fmt"
    "github.com/tencentyun/cos-go-sdk-v5"
    "net/http"
    "net/url"
    "os"
    "time"
    "strings"
)
// 通过 tag 的方式，用户可以将请求参数或者请求头部放进签名中。
type URLToken struct {
    SessionToken string `url:"x-cos-security-token,omitempty" header:"-"`
}
﻿

func main() {
    // 请替换成您的临时密钥
    tak := os.Getenv("SECRETID")	// 用户的临时密钥SecretId，授权遵循最小权限指引，降低使用风险。临时密钥获取可参见 https://cloud.tencent.com/document/product/436/14048
    tsk := os.Getenv("SECRETKEY")	// 用户的临时密钥SecretKey，授权遵循最小权限指引，降低使用风险。临时密钥获取可参见 https://cloud.tencent.com/document/product/436/14048
    token := &URLToken{
        SessionToken: "<token>",
    }
    u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
    b := &cos.BaseURL{BucketURL: u}
    c := cos.NewClient(b, &http.Client{})
﻿

    name := "exampleobject"
    ctx := context.Background()
﻿

    // 方法1 通过 PresignedURLOptions 设置 x-cos-security-token
    // PresignedURLOptions 提供用户添加请求参数和请求头部
    opt := &cos.PresignedURLOptions{
        Query:  &url.Values{},
        Header: &http.Header{},
    }
    opt.Query.Add("x-cos-security-token", "<token>")
    // 获取预签名
    presignedURL, err := c.Object.GetPresignedURL(ctx, http.MethodPut, name, tak, tsk, time.Hour, opt)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    // 通过预签名方式上传对象
    data := "test upload with presignedURL"
    f := strings.NewReader(data)
    req, err := http.NewRequest(http.MethodPut, presignedURL.String(), f)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
    }
    _, err = http.DefaultClient.Do(req)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
    }
﻿

    // 方法2 通过 tag 设置 x-cos-security-token
    // 获取预签名
    presignedURL, err = c.Object.GetPresignedURL(ctx, http.MethodPut, name, tak, tsk, time.Hour, token)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    f = strings.NewReader(data)
    req, err = http.NewRequest(http.MethodPut, presignedURL.String(), f)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
    }
    _, err = http.DefaultClient.Do(req)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
    }
}
使用案例：临时密钥预签名下载请求
package main
﻿

import (
    "context"
    "fmt"
    "github.com/tencentyun/cos-go-sdk-v5"
    "net/http"
    "net/url"
    "os"
    "time"
)
// 通过 tag 的方式，用户可以将请求参数或者请求头部放进签名中。
type URLToken struct {
    SessionToken string `url:"x-cos-security-token,omitempty" header:"-"`
}
﻿

func main() {
    // 替换成您的临时密钥
    tak := os.Getenv("SECRETID")	// 用户的临时密钥SecretId，授权遵循最小权限指引，降低使用风险。临时密钥获取可参见 https://cloud.tencent.com/document/product/436/14048
    tsk := os.Getenv("SECRETKEY")	// 用户的临时密钥SecretKey，授权遵循最小权限指引，降低使用风险。临时密钥获取可参见 https://cloud.tencent.com/document/product/436/14048
    token := &URLToken{
        SessionToken: "<token>",
    }
    u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
    b := &cos.BaseURL{BucketURL: u}
    c := cos.NewClient(b, &http.Client{})
﻿

    name := "exampleobject"
    ctx := context.Background()
﻿

    // 方法1 通过 PresignedURLOptions 设置 x-cos-security-token
    // PresignedURLOptions 提供用户添加请求参数和请求头部
    opt := &cos.PresignedURLOptions{
        Query:  &url.Values{},
        Header: &http.Header{},
    }
    opt.Query.Add("x-cos-security-token", "<token>")
    // 获取预签名
    presignedURL, err := c.Object.GetPresignedURL(ctx, http.MethodGet, name, tak, tsk, time.Hour, opt)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    // 通过预签名访问对象
    resp, err := http.Get(presignedURL.String())
    if err != nil {
        fmt.Printf("Error: %v\n", err)
    }
    defer resp.Body.Close()
    fmt.Println(presignedURL.String())
    fmt.Printf("resp:%v\n", resp)
﻿

    // 方法2 通过 tag 设置 x-cos-security-token
    // 获取预签名
    presignedURL, err = c.Object.GetPresignedURL(ctx, http.MethodGet, name, tak, tsk, time.Hour, token)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    // 通过预签名访问对象
    resp, err = http.Get(presignedURL.String())
    if err != nil {
        fmt.Printf("Error: %v\n", err)
    }
    defer resp.Body.Close()
    fmt.Println(presignedURL.String())
    fmt.Printf("resp:%v\n", resp)
}
使用案例：自定义域名预签名下载请求
package main
﻿

import (
    "context"
    "fmt"
    "github.com/tencentyun/cos-go-sdk-v5"
    "net/http"
    "net/url"
    "os"
    "time"
)
func main() {
    // 通过环境变量获取密钥
    // 环境变量 SECRETID 表示用户的 SecretId，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
    ak := os.Getenv("SECRETID") // 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
    // 环境变量 SECRETKEY 表示用户的 SecretKey，登录访问管理控制台查看密钥，https://console.cloud.tencent.com/cam/capi
    sk := os.Getenv("SECRETKEY")  // 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
    // 修改成用户的自定义域名
    u, _ := url.Parse("https://<自定义域名>")
    b := &cos.BaseURL{BucketURL: u}
    c := cos.NewClient(b, &http.Client{})
﻿

    name := "exampleobject"
    ctx := context.Background()
﻿

    // 获取预签名
    presignedURL, err := c.Object.GetPresignedURL(ctx, http.MethodGet, name, ak, sk, time.Hour, nil)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    // 通过预签名访问对象
    resp, err := http.Get(presignedURL.String())
    if err != nil {
        fmt.Printf("Error: %v\n", err)
    }
    defer resp.Body.Close()
    fmt.Println(presignedURL.String())
    fmt.Printf("resp:%v\n", resp)
}
使用案例：预签名添加请求参数或请求头部
package main
﻿

import (
    "context"
    "fmt"
    "github.com/tencentyun/cos-go-sdk-v5"
    "net/http"
    "net/url"
    "os"
    "time"
)
func main() {
    // 替换成您的临时密钥
    tak := os.Getenv("SECRETID")   // 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
    tsk := os.Getenv("SECRETKEY")  // 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
    u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
    b := &cos.BaseURL{BucketURL: u}
    c := cos.NewClient(b, &http.Client{})
﻿

    name := "exampleobject"
    ctx := context.Background()
﻿

    // PresignedURLOptions 提供用户添加请求参数和请求头部
    opt := &cos.PresignedURLOptions{
        // http 请求参数，传入的请求参数需与实际请求相同，能够防止用户篡改此 HTTP 请求的参数
        Query:  &url.Values{},
        // http 请求头部，传入的请求头部需包含在实际请求中，能够防止用户篡改签入此处的 HTTP 请求头部
        Header: &http.Header{},
    }
    // 添加请求参数, 返回的预签名 url 将包含该参数
    opt.Query.Add("x-cos-security-token", "<token>")
    // 添加请求头部，返回的预签名 url 只是将请求头部设置到签名里，请求时还需要自行设置对应的 header。
    opt.Header.Add("Content-Type", "text/html")
﻿

    // SDK 默认签入 Header Host，不传递 signHost 参数或者 SignHost = true 时，表示签入 Header Host。
    // signHost = false 时，表示不签入 Header Host，不签入 Header Host 可能导致请求失败或安全漏洞。
    var signHost bool = true
    // 获取预签名, 签名中携带host。
    presignedURL, err := c.Object.GetPresignedURL(ctx, http.MethodPut, name, tak, tsk, time.Hour, opt, signHost)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    // 通过预签名访问对象
    req, _ := http.NewRequest(http.MethodPut, presignedURL.String(), strings.NewReader("test"))
    // 请求时需要设置对应 header
    req.Header.Set("Content-Type", "text/html")
    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
    }
    defer resp.Body.Close()
    fmt.Println(presignedURL.String())
    fmt.Printf("resp:%v\n", resp)
}
使用案例：通过预签名分块上传文件
package main
﻿

import (
	"bytes"
	"context"
	"encoding/xml"
	"fmt"
	"io"
	"io/ioutil"
	"math/rand"
	"net/http"
	"net/url"
	"os"
	"time"
﻿

	"github.com/tencentyun/cos-go-sdk-v5"
)
﻿

func logStatus(err error) {
	if err == nil {
		return
	}
	if cos.IsNotFoundError(err) {
		fmt.Println("WARN: Resource is not existed")
	} else if e, ok := cos.IsCOSError(err); ok {
		fmt.Printf("ERROR: Code: %v\n", e.Code)
		fmt.Printf("ERROR: Message: %v\n", e.Message)
		fmt.Printf("ERROR: Resource: %v\n", e.Resource)
		fmt.Printf("ERROR: RequestId: %v\n", e.RequestID)
	} else {
		fmt.Printf("ERROR: %v\n", err)
	}
}
﻿

func main() {
	ak := os.Getenv("SECRETID")
	sk := os.Getenv("SECRETKEY")
﻿

	// 存储桶名称，由 bucketname-appid 组成
	u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
	b := &cos.BaseURL{BucketURL: u}
	c := cos.NewClient(b, &http.Client{
		Transport: &cos.AuthorizationTransport{
			SecretID:  ak,
			SecretKey: sk,
		},
	})
﻿

	name := "test/multipart_presigned_example"
	ctx := context.Background()
﻿

	// ===================== Step 1: InitiateMultipartUpload 预签名 =====================
	// InitiateMultipartUpload 需要 POST 方法，query 参数带 uploads
	initOpt := &cos.PresignedURLOptions{
		Query: &url.Values{},
	}
	initOpt.Query.Set("uploads", "")
﻿

	initPresignedURL, err := c.Object.GetPresignedURL(ctx, http.MethodPost, name, ak, sk, time.Hour, initOpt)
	if err != nil {
		logStatus(err)
		return
	}
	fmt.Printf("InitMultipartUpload PresignedURL: %s\n\n", initPresignedURL.String())
﻿

	// 使用预签名 URL 发起 InitiateMultipartUpload 请求
	initReq, _ := http.NewRequest(http.MethodPost, initPresignedURL.String(), nil)
	initResp, err := http.DefaultClient.Do(initReq)
	if err != nil {
		fmt.Printf("InitiateMultipartUpload request failed: %v\n", err)
		return
	}
	defer initResp.Body.Close()
﻿

	initBody, _ := ioutil.ReadAll(initResp.Body)
	if initResp.StatusCode != 200 {
		fmt.Printf("InitiateMultipartUpload failed, status: %s, body: %s\n", initResp.Status, string(initBody))
		return
	}
﻿

	var initResult cos.InitiateMultipartUploadResult
	if err := xml.Unmarshal(initBody, &initResult); err != nil {
		fmt.Printf("Parse InitiateMultipartUpload response failed: %v\n", err)
		return
	}
	uploadID := initResult.UploadID
	fmt.Printf("InitiateMultipartUpload 成功, UploadID: %s\n\n", uploadID)
﻿

	// ===================== Step 2: UploadPart 预签名 =====================
	// 模拟 3 个分块，每块 1MB 随机数据
	partCount := 3
	partSize := 1 * 1024 * 1024 // 1MB
	parts := make([]cos.Object, 0, partCount)
﻿

	for i := 1; i <= partCount; i++ {
		// 生成预签名 URL，query 参数带 partNumber 和 uploadId
		partOpt := &cos.PresignedURLOptions{
			Query: &url.Values{},
		}
		partOpt.Query.Set("partNumber", fmt.Sprintf("%d", i))
		partOpt.Query.Set("uploadId", uploadID)
﻿

		partPresignedURL, err := c.Object.GetPresignedURL(ctx, http.MethodPut, name, ak, sk, time.Hour, partOpt)
		if err != nil {
			logStatus(err)
			return
		}
		fmt.Printf("UploadPart %d PresignedURL: %s\n\n", i, partPresignedURL.String())
﻿

		// 生成随机数据
		data := make([]byte, partSize)
		rand.Read(data)
﻿

		// 使用预签名 URL 上传分块
		partReq, _ := http.NewRequest(http.MethodPut, partPresignedURL.String(), bytes.NewReader(data))
		partReq.ContentLength = int64(len(data))
		partResp, err := http.DefaultClient.Do(partReq)
		if err != nil {
			fmt.Printf("UploadPart %d request failed: %v\n", i, err)
			return
		}
		io.Copy(ioutil.Discard, partResp.Body)
		partResp.Body.Close()
﻿

		if partResp.StatusCode != 200 {
			fmt.Printf("UploadPart %d failed, status: %s\n", i, partResp.Status)
			return
		}
﻿

		etag := partResp.Header.Get("ETag")
		fmt.Printf("UploadPart %d 成功, ETag: %s\n\n", i, etag)
		parts = append(parts, cos.Object{
			PartNumber: i,
			ETag:       etag,
		})
	}
﻿

	// ===================== Step 3: CompleteMultipartUpload 预签名 =====================
	completeOpt := &cos.PresignedURLOptions{
		Query: &url.Values{},
	}
	completeOpt.Query.Set("uploadId", uploadID)
﻿

	completePresignedURL, err := c.Object.GetPresignedURL(ctx, http.MethodPost, name, ak, sk, time.Hour, completeOpt)
	if err != nil {
		logStatus(err)
		return
	}
	fmt.Printf("CompleteMultipartUpload PresignedURL: %s\n\n", completePresignedURL.String())
﻿

	// 构造 CompleteMultipartUpload 的 XML Body
	completeBody := &cos.CompleteMultipartUploadOptions{
		Parts: parts,
	}
	xmlData, err := xml.Marshal(completeBody)
	if err != nil {
		fmt.Printf("Marshal CompleteMultipartUpload body failed: %v\n", err)
		return
	}
﻿

	// 使用预签名 URL 完成分块上传
	completeReq, _ := http.NewRequest(http.MethodPost, completePresignedURL.String(), bytes.NewReader(xmlData))
	completeReq.Header.Set("Content-Type", "application/xml")
	completeResp, err := http.DefaultClient.Do(completeReq)
	if err != nil {
		fmt.Printf("CompleteMultipartUpload request failed: %v\n", err)
		return
	}
	defer completeResp.Body.Close()
﻿

	completeRespBody, _ := ioutil.ReadAll(completeResp.Body)
	if completeResp.StatusCode != 200 {
		fmt.Printf("CompleteMultipartUpload failed, status: %s, body: %s\n", completeResp.Status, string(completeRespBody))
		return
	}
﻿

	var completeResult cos.CompleteMultipartUploadResult
	if err := xml.Unmarshal(completeRespBody, &completeResult); err != nil {
		fmt.Printf("Parse CompleteMultipartUpload response failed: %v\n", err)
		return
	}
﻿

	fmt.Printf("分块上传完成!\n")
	fmt.Printf("  Location: %s\n", completeResult.Location)
	fmt.Printf("  Bucket:   %s\n", completeResult.Bucket)
	fmt.Printf("  Key:      %s\n", completeResult.Key)
	fmt.Printf("  ETag:     %s\n", completeResult.ETag)
}
﻿

上一篇: 对象访问 URL
下一篇: 恢复归档对象
文档内容是否对您有帮助？
有帮助没帮助

如果遇到产品相关问题，您可咨询 在线客服寻求帮助。

对象存储 相关文档
产品简介
地域和访问域名
功能概览
快速入门
计费概述
免费额度
工具概览
API 简介
SDK 概览
Copyright © 2013-2026 Tencent Cloud. All Rights Reserved. 腾讯云 版权所有
深圳市腾讯计算机系统有限公司ICP备案/许可证号：粤B2-20090059
粤公网安备44030502008569号

腾讯云计算（北京）有限责任公司京ICP证150476号 | 京ICP备11018762号
中国站
咨询
