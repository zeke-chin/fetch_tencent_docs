<!-- source: https://cloud.tencent.com/document/product/436/90191 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:20:02+08:00 -->

# 使用 KMS 白盒密钥保护 COS SecretKey 最佳实践

最近更新时间：2024-12-19 14:38:12


## KMS 白盒密钥简介

KMS 白盒密钥用于保护端上的敏感根密钥信息，例如 API SecretKey、用户内部系统使用的鉴权密钥或 token、其它本地敏感根密钥信息等，**实现全链路无敏感密钥信息明文**。将算法与密钥进行混淆融合，以查找表的形式有效保护密钥信息，在不暴露任何密钥的情况下实现加密与解密，并通过设备绑定的方式进一步确保密钥的安全。

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/338b6c1b037a5c49cae5621546d50b88.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/338b6c1b037a5c49cae5621546d50b88.png)

本文为您介绍使用密钥管理系统（Key Management Service，KMS）白盒密钥对 COS 产品 SecretKey 加解密的操作示例，通过白盒密钥对 SecretKey 进行保护和安全使用，详情步骤请参见：

[密钥的管理和分发](https://cloud.tencent.com/document/product/436/90191#.E5.AF.86.E9.92.A5.E7.9A.84.E7.AE.A1.E7.90.86.E5.92.8C.E5.88.86.E5.8F.91)

[通过对象存储 SDK 工具访问 COS](https://cloud.tencent.com/document/product/436/90191#.E9.80.9A.E8.BF.87.E5.AF.B9.E8.B1.A1.E5.AD.98.E5.82.A8-sdk-.E5.B7.A5.E5.85.B7.E8.AE.BF.E9.97.AE-cos)

## 使用 KMS 白盒密钥优势

### **高安全性**

基于高强度混淆加固算法及多重安全防护技术，杜绝 API SecretKey 的明文暴露在源代码中。

### **动态白盒**

支持在白盒库不变的情况下实现灵活的密钥的动态轮换。

### **设备绑定**

绑定设备指纹信息，实现对解密密钥的加固保护。

### **算法支持**

支持国际算法 AES、国密算法 SM4 算法，满足合规要求。

## 密钥的管理和分发

### 步骤1：创建白盒密钥

**注意：**

白盒密钥为 KMS 收费项，详情请参见 [KMS 计费概述](https://cloud.tencent.com/document/product/573/34388#.E7.99.BD.E7.9B.92.E5.AF.86.E9.92.A5) 和 [KMS 购买方式](https://cloud.tencent.com/document/product/573/18809#.E8.B4.AD.E4.B9.B0.E7.99.BD.E7.9B.92.E5.AF.86.E9.92.A5)。

创建白盒密钥对是通过调用白盒服务来实现的，支持控制台方式和 API 方式，本文示例采用控制台方式。

1. 登录 [数据安全保护控制台](https://console.cloud.tencent.com/kms2/whitebox)，在左侧菜单栏选择**密钥管理系统（合规）**>**白盒密钥管理**，根据业务需求切换“地域” ，单击**新建**。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/9c0bc24c25ac1c72db9cb59e4137adc8.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/9c0bc24c25ac1c72db9cb59e4137adc8.png)

2. 在弹出的对话框，填写白盒密钥名称，选择加密算法，描述信息及标签（两者选填），单击**确定**，即可完成白盒密钥的创建。

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/ab2c0f3c0ffe62193481e2683066288a.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/ab2c0f3c0ffe62193481e2683066288a.png)

### 步骤2：控制台获取 API SecretKey

使用主账号登录 [API 密钥管理控制台](https://console.cloud.tencent.com/cam/capi)，可查看您已有的 API 密钥或新建密钥。详情请参见 [主账号访问密钥管理](https://cloud.tencent.com/document/product/598/40488)。

### 步骤3：对 SecretKey 明文进行 base64 编码

将步骤2中获取的 SecretKey 内容进行 base64 编码。 例如，要加密的 SecretKey 明文是：`lY9Ynrabcdj05YH1234LE37xxxx`，使用 openssl 命令生成 base64 编码后的结果为：`bFk5WW5yYWJjZGowNVlIMTIzNExFMzcwSE9Nxxxx`。

echo lY9Ynrabcdj05YH1234LE37xxxx | openssl base64

### 步骤4：使用白盒密钥加密 API SecretKey

1. 进入 [数据安全保护控制台](https://console.cloud.tencent.com/kms2/whitebox)，在白盒密钥列表，单击“白盒密钥ID/名称”或“操作”列的**加密**。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/6c45617a7500758ad00cadf7a1370108.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/6c45617a7500758ad00cadf7a1370108.png)

2. 在弹出的对话框，将 [步骤3](https://cloud.tencent.com/document/product/436/90191#.E6.AD.A5.E9.AA.A43.EF.BC.9A.E5.AF.B9-secretkey-.E6.98.8E.E6.96.87.E8.BF.9B.E8.A1.8C-base64-.E7.BC.96.E7.A0.81) 中获取的编码内容填充至明文（base64）文本框中，单击**白盒加密**。

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/2c869fd8447a15970dc480fb28ceaa19.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/2c869fd8447a15970dc480fb28ceaa19.png)

3. 加密成功后，会返回随机生成的初始化向量（简称 IV）和加密后的密文，单击**下载 IV**和**下载密文**，即可完成内容的下载。

**说明：**

其中初始化向量（简称 IV）和加密后的密文均已进行 base64 编码。

![Image 12](https://qcloudimg.tencent-cloud.cn/image/document/e859383135f960d7ae3cbae68d0de583.png)

![Image 13](https://qcloudimg.tencent-cloud.cn/image/document/e859383135f960d7ae3cbae68d0de583.png)

4. （可选步骤）白盒密钥支持将解密密钥与解密运行的物理环境进行绑定。操作方式为：

在白盒密钥控制台中下载对应环境的指纹采集工具，并在指定的环境中运行指纹采集工具，获得该环境的指纹字符串。

![Image 14](https://qcloudimg.tencent-cloud.cn/image/document/59f218c2cebed03165207cd59394c13f.png)

![Image 15](https://qcloudimg.tencent-cloud.cn/image/document/59f218c2cebed03165207cd59394c13f.png)

在白盒密钥控制台中，选择指定的白盒密钥，单击“新增设备指纹”，输入对应环境的指纹字符串，将该指纹与该密钥进行绑定。

![Image 16](https://qcloudimg.tencent-cloud.cn/image/document/b757fd4bf75359b37f7cfac99fed58d8.png)

![Image 17](https://qcloudimg.tencent-cloud.cn/image/document/b757fd4bf75359b37f7cfac99fed58d8.png)

指纹环境变量被绑定到该密钥后，解密密钥会被更新，后续使用该白盒密钥加密的数据只能使用更新后的解密密钥在已绑定的物理环境中进行解密。

### 步骤5：下载解密密钥

1. 进入 [数据安全保护控制台](https://console.cloud.tencent.com/kms2/whitebox)，在左侧菜单栏选择**白盒密钥管理**页面，单击**白盒密钥ID/名称**，进入密钥基本信息页面。

2. 在密钥基本信息页面，单击**下载解密密钥**，并命名为 decrypt_key_sm4.bin。

![Image 18](https://qcloudimg.tencent-cloud.cn/image/document/e636a41e4ac8bcd81ce0489ed72f3d6f.png)

![Image 19](https://qcloudimg.tencent-cloud.cn/image/document/e636a41e4ac8bcd81ce0489ed72f3d6f.png)

### 步骤6：下载解密 SDK 文件

1. 进入 [数据安全保护控制台](https://console.cloud.tencent.com/kms2/whitebox)，在左侧菜单栏选择**白盒密钥管理**页面，单击右侧的**下载解密SDK文件**。

![Image 20](https://qcloudimg.tencent-cloud.cn/image/document/66eb02f53b1dab8a7d4f16d74337691e.png)

![Image 21](https://qcloudimg.tencent-cloud.cn/image/document/66eb02f53b1dab8a7d4f16d74337691e.png)

2. 在弹出的对话框，根据各业务系统自身的编程语言，选择下载相应编程语言的解密 SDK，并将解密 SDK 集成到业务系统中。

![Image 22](https://qcloudimg.tencent-cloud.cn/image/document/1ca1213c7f6494fea21e05be0bb757f6.png)

![Image 23](https://qcloudimg.tencent-cloud.cn/image/document/1ca1213c7f6494fea21e05be0bb757f6.png)

### 步骤7：白盒解密密钥和 API SecretKey 密文分发

管理员将上述步骤中下载的解密密钥、IV 和密文三个文件，分发给各业务系统的开发或运维人员。其中，解密密钥部署到相应业务系统的文件中，而初始化向量 IV 和密文会作为解密 SDK 的传参。

**注意：**

下载的解密密钥是一个二进制 bin 文件，需要将该文件和可执行文件（已经集成了解密 SDK）放在相同的服务器上，文件路径将作为解密 SDK 的解密参数。

## 通过对象存储 SDK 工具访问 COS

### 步骤1：通过永久密钥初始化身份信息

安装对象存储 SDK 工具后，在客户端代码中引入下载的白盒 SDK，并按照如下步骤获取解密后的 Secret Key：

1. 在代码中引入预先下载的白盒 SDK。

2. 调用白盒密钥解密 SDK 的解密函数对加密后的 Secret Key 进行解密。传入如下参数，从而获得解密后的明文。

decrypt_key_bin_dir：步骤7中解密密钥存放的目录。

decrypt_key_sm4.bin：步骤5中下载的解密密钥，其对应的文件名。

InitializationVector：步骤4中下载的 IV。

CipherText：步骤4中用白盒加密后的 SecretKey 密文。

algorithmType：是生成密钥时使用的算法类型，取值为0或1。0表示 AES_256，1表示 SM4。

3. 使用解密后的 Secret Key 以及 Secret ID（若 Secret ID 也被加密，则同样需要解密）对 COS SDK 进行初始化。后续针对 COS 的服务调用可参考 COS SDK 的相关文档。

白盒密钥解密 SDK 基于 C 语言实现，并提供了基于其他高级语言的适配，例如 Golang、Python、Java 等。具体使用方法可参考指定语言的解密 SDK 中的代码示例。

Golang 示例代码如下（基于 CGO）：

由于白盒解密 SDK 底层功能由 C lib 库实现，因此示例代码采用 CGO 注解的方式将解密 SDK 头文件目录`#cgo CFLAGS: -I${SRCDIR}/include`以及 lib 库文件`#cgo LDFLAGS: -L${SRCDIR}/lib -lydwbcrypto`引入到代码中。头文件目录以及 lib 库通常位于所下载的白盒解密 SDK 的根目录下，应用集成时可根据项目结构自主调整。

假设文件命名为 main.go，且 main.go 所处的包为 main，则首先初始化包：

go mod init main

然后将下面的代码粘贴到 main.go 中：

package main

/*

#cgo CFLAGS: -I${SRCDIR}/include

#cgo LDFLAGS: -L${SRCDIR}/lib -lydwbcrypto

#include <stdio.h>

#include <string.h>

#include <stdlib.h>

#include "wrp.h"

static int clt_load_key(WRP_KEY_CTX *key_ctx, char *decrypt_key_path, const char *file_name,

 uint32_t mode, uint32_t algoType) {

 printf("begin to load key in dir: %s\n", decrypt_key_path);

 printf("begin to load key: %s\n", file_name);

 int err;

 const WRP_KEY* keyalg = WRP_KEY_wbaes();

 if (algoType == 1) { keyalg = WRP_KEY_wbsm4(); }

 err = WRP_KEY_init(key_ctx, keyalg, 0);

 if (err) { printf("Err: orig_byte init\n"); goto end; }

 err = WRP_KEY_ctrl(key_ctx, WRP_KEY_CTRL_WB_SET_PATH, decrypt_key_path, strlen(decrypt_key_path));

 if (err) { printf("Err: set path\n"); goto end; }

 err = WRP_KEY_import(key_ctx, file_name, mode);

 if (err) { printf("Err: WRP_KEY_import error: %d， \n", err); goto end; }

end:

 return err;

}

int clt_cbc_dec(char * file_dir, const char * file_name, uint8_t* ciph, uint32_t ciphlen, char* iv,

 uint32_t algoType, uint8_t* out, uint32_t* outlen) {

 WRP_KEY_CTX *mykey;

 WRP_CIPHER_CTX *myaes = NULL;

 uint32_t bits;

 ERRNO err = ERRNO_OK;

 const WRP_CIPHER* alg = WRP_wbaes_cbc();

 if (algoType == 1) { alg = WRP_wbsm4_cbc(); }

 // IO: load wbkey

 mykey = WRP_KEY_CTX_new();

 err = clt_load_key(mykey, file_dir, file_name, KEYMODE_DECRYPT, algoType);

 if (err) { printf("load whitebox key error: %d\n", err); goto cleanup; }

 printf("load key success\n");

 bits = WRP_KEY_key_len(mykey, KEYLEN_TYPE_BITS);

 printf("key len=%u\n", bits);

 if (bits == 0) { printf("get whitebox key length error\n"); err=-1; goto cleanup; }

 // crypto

 myaes = WRP_CIPHER_CTX_new();

 err = WRP_CIPHER_Decrypt_init(myaes, alg, mykey, (uint8_t *)iv);

 if (err) { printf("Dec: init Err**\n"); goto cleanup; }

 printf("decrypt init success, begin to decrypt cipher\n");

 err = WRP_CIPHER_Decrypt_doCipher(myaes, ciph, ciphlen, out, outlen);

 if (err) { printf("decrypt error: %.8X\n", err); goto cleanup; }

 //printf("decrypt success\n");

 //printf("output: %s\n", deout);

 //printf("\n");

cleanup:

 WRP_KEY_CTX_free(mykey);

 WRP_CIPHER_CTX_free(myaes);

 return err;

}

void set_fingerprint_env_name(char *fingerprint_env_name) {

 WRP_getENV_KEY((uint8_t *)fingerprint_env_name, strlen(fingerprint_env_name));

}

*/

import "C"

import (

 "context"

 "encoding/base64"

 "errors"

 "fmt"

 "io/ioutil"

 "net/http"

 "net/url"

 "os"

 "strconv"

 "time"

 "unsafe"


 "github.com/tencentyun/cos-go-sdk-v5"

)

// Decrypt ...

func Decrypt(input DecryptionInput) ([]byte, error) {

 if input.KeyDir == "" || input.KeyFileName == "" || input.CipherText == "" || input.InitializationVector == "" {

 return nil, errors.New("invalid white-box decryption input")

 }

 cipher, err := base64.StdEncoding.DecodeString(input.CipherText)

 if err != nil {

 return nil, fmt.Errorf("failed to decode cipher text: %w", err)

 }

 iv, err := base64.StdEncoding.DecodeString(input.InitializationVector)

 if err != nil {

 return nil, fmt.Errorf("failed to decode initialization vector: %w", err)

 }

 decryptionKeyDir := C.CString(input.KeyDir)

 defer C.free(unsafe.Pointer(decryptionKeyDir))

 decryptionKeyFileName := C.CString(input.KeyFileName)

 defer C.free(unsafe.Pointer(decryptionKeyFileName))

 // malloc a buffer which size is a little greater than your plaintext

 outLen := len(input.CipherText) + 1024

 outBuf := C.malloc(C.size_t(outLen))

 defer C.free(unsafe.Pointer(outBuf))

 errC := C.clt_cbc_dec(

 decryptionKeyDir, decryptionKeyFileName,

 (*C.uchar)(unsafe.Pointer(&cipher[0])),

 C.uint(len(cipher)),

 (*C.char)(unsafe.Pointer(&iv[0])),

 C.uint(input.AlgorithmType),

 (*C.uchar)(outBuf),

 (*C.uint)(unsafe.Pointer(&outLen)),

 )

 if errC != 0 {

 return nil, fmt.Errorf("whitebox decryption failed with code %d", int(errC))

 }

 plain := C.GoBytes(outBuf, C.int(outLen))

 return plain, nil

}

func main() {

 //将<bucket>和<region>修改为真实的信息

 //bucket的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式

 u, _ := url.Parse("https://<bucket>.cos.<region>.myqcloud.com")

 // 使用环境变量指定白盒密钥相关信息，以及加密后的 secret ID 以及 secret key。

 encryptionAlgorithm, _ := strconv.Atoi(os.Getenv("EncryptionAlgorithm"))

 whiteboxDecryptInput := DecryptionInput{

 KeyDir: os.Getenv("WhiteboxKeyDir"), // e.g.: /usr/local/

 KeyFileName: os.Getenv("WhiteboxKeyFileName"), // e.g.: whitebox_key.bin

 InitializationVector: os.Getenv("WhiteboxDecryptionIV"),

 AlgorithmType: uint(encryptionAlgorithm),

 }

 // 使用白盒 sdk 解密 secret ID

 whiteboxDecryptInput.CipherText = os.Getenv("COS_Encrypted_Secret_ID")

 secretID, err := Decrypt(whiteboxDecryptInput)

 if err != nil {

 panic(err)

 }

 // 使用白盒 sdk 解密 secret key

 whiteboxDecryptInput.CipherText = os.Getenv("COS_Encrypted_Secret_Key")

 secretKey, err := Decrypt(whiteboxDecryptInput)

 if err != nil {

 panic(err)

 }

 b := &cos.BaseURL{BucketURL: u}

 c := cos.NewClient(b, &http.Client{

 //设置超时时间

 Timeout: 100 * time.Second,

 Transport: &cos.AuthorizationTransport{

 //如实填写账号和密钥，也可以设置为环境变量

 SecretID: string(secretID),

 SecretKey: string(secretKey),

 },

 })

 name := "test/hello.txt"

 resp, err := c.Object.Get(context.Background(), name, nil)

 if err != nil {

 panic(err)

 }

 bs, _ := ioutil.ReadAll(resp.Body)

 _ = resp.Body.Close()

 fmt.Printf("%s\n", string(bs))

}

type DecryptionInput struct {

 KeyDir string

 KeyFileName string

 InitializationVector string // Base64 encoded.

 CipherText string // Base64 encoded.

 AlgorithmType uint // 0: AES_256, 1: SM4.

}

如果白盒解密 SDK 所在目录与代码文件在同一级目录，则直接使用相对路径即可：

![Image 24](https://qcloudimg.tencent-cloud.cn/image/document/50a8df53669166f82d866508f57c9b4d.png)

![Image 25](https://qcloudimg.tencent-cloud.cn/image/document/50a8df53669166f82d866508f57c9b4d.png)

代码编译：

go build

代码运行：

# 先设置动态库查找路径

export LD_LIBRARY_PATH=`pwd`/lib/linux:$LD_LIBRARY_PATH

./main

### 步骤2：直接使用 COS SDK 请求 COS 服务

初始化之后，您可以直接使用 COS SDK 工具进行上传、下载等基本操作，而无需像 API 请求一样自行生成签名，因为 SDK 工具代替您通过密钥生成了签名，向 COS 发起请求。
