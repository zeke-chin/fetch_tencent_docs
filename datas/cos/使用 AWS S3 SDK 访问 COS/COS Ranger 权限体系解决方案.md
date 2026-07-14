<!-- source: https://cloud.tencent.com/document/product/436/51125 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:21:00+08:00 -->

# COS Ranger 权限体系解决方案

最近更新时间：2024-12-19 19:21:52


## 背景

Hadoop Ranger 权限体系是大数据场景下的权限解决方案。用户使用存算分离后，将数据托管在对象存储（Cloud Object Storage，COS）上。COS 使用的是腾讯云访问管理（Cloud Access Management，CAM）权限体系，无论是用户身份，权限策略等，都与本地 Hadoop Ranger 体系不同。为维持客户的使用习惯，我们提供 COS 的 Ranger 接入解决方案。

## 优势

细粒度的权限控制，兼容 Hadoop 权限逻辑，用户统一管理大数据组件与云端托管存储的权限。

插件侧无需在 core-site 中设置密钥，密钥统一在 COS Ranger Service 中设置，避免明文密钥的泄露。

## 解决方案架构

![Image 2](https://qcloudimg.tencent-cloud.cn/image/document/22de4371876dff00618e34961da8421b.png)

![Image 3](https://qcloudimg.tencent-cloud.cn/image/document/22de4371876dff00618e34961da8421b.png)

Hadoop 权限体系中，认证由 Kerberos 提供，授权鉴权由 Ranger 负责。在此基础上，我们提供以下组件，来支持 COS 的 Ranger 权限方案。

1. COS Ranger Plugin：提供 Ranger 服务端的服务定义插件。它们提供了 Ranger 侧的 COS 服务描述，包括权限种类，必要参数定义（例如 COS 的 bucket 参数和 region 参数）。部署了该插件后，用户即可在 Ranger 的控制页面上，填写相应的权限策略。

2. COS Ranger Service：该服务集成了 Ranger 的客户端，周期性从 Ranger 服务端同步权限策略，在收到客户的鉴权请求后，在本地进行权限校验。 同时它提供了 Hadoop 中 DelegationToken 相关的生成、续租等接口，所有的接口都是通过 Hadoop IPC 定义。

3. COS Ranger Client：COSN 插件对其进行动态加载，把权限校验的请求转发给 COS Ranger Service。

## 部署环境

Hadoop 环境。(需要3.2.2版本及以下)

ZooKeeper、Ranger。

Kerberos 服务。

**说明：**

以上服务由于是成熟的开源组件，因此客户可自行安装。组件之间，可能存在版本兼容性问题。这里推荐EMR-V350版本使用的组件版本。

Hadoop-3.2.2

Zookeeper-3.6.3

Ranger-2.3.0

Kerberos-1.15.1

## 部署组件

部署组件请按照 COS Ranger Plugin、COS Ranger Service、COS Ranger Client、COSN 次序进行。

部署 COS Ranger Plugin

部署 COS Ranger Service

部署 COS-Ranger-Client 和 COSN-Ranger-Interface

部署 COSN

COS-Ranger-Plugin 拓展了 Ranger Admin 控制台上的服务种类，用户可在 Ranger 控制台上，设置和 COS 相关的操作权限。

#### 代码地址

可前往 [Github](https://github.com/tencentyun/cos-ranger-service) 的 ranger-plugin 目录下获取。

#### 版本

V1.0 版本及以上。

#### 部署步骤

1. 在 Ranger 的服务定义目录下新建 COS 目录（注意，目录权限需要保证至少有 x 与 r 权限）。 a. 腾讯云的 EMR 环境，路径位于部署了ranger服务的Master节点的 /usr/local/service/ranger/ews/webapp/WEB-INF/classes/ranger-plugins。 b. 自建的 hadoop 环境，可以通过在 ranger 目录下查找 hdfs 等已经接入到 ranger 服务的组件，查找目录位置。

![Image 4](https://qcloudimg.tencent-cloud.cn/image/document/2615e8958eb87afd639c11b5fc7e9e86.png)

![Image 5](https://qcloudimg.tencent-cloud.cn/image/document/2615e8958eb87afd639c11b5fc7e9e86.png)

2. 在 COS 目录下，放入 cos-chdfs-ranger-plugin-xxx.jar。（注意 jar 包至少有 r 权限）。同时需要放入 cos-ranger.json 文件，可前往 [Github](https://github.com/tencentyun/cos-ranger-service/tree/main/ranger-plugin) 获取。

3. 重启 Ranger 服务。

4. 在 Ranger 上注册 COS Service。可参考如下命令：

##生成服务，需传入 Ranger 管理员账号密码，以及 Ranger 服务的地址。

##对于腾讯云 EMR 集群，管理员用户是 root，密码是构建 emr 集群时设置的 root 密码，ranger 服务的 IP 换成 EMR 的 master 节点 IP。

adminUser=root

##构建 EMR 集群时设置的密码，也是 ranger 服务 web 页面的登录密码

adminPasswd=xxxxxx

##如果 ranger 服务有多个 master 节点，任选一个 master 即可

rangerServerAddr=10.0.0.1:6080

##命令行中 -d 指定步骤 2 中的 json 文件

curl -v -u${adminUser}:${adminPasswd} -X POST -H "Accept:application/json" -H "Content-Type:application/json" -d @./cos-ranger.json http://${rangerServerAddr}/service/plugins/definitions

##如果要删除刚定义的服务，则传入刚刚创建服务时，返回的服务 ID

serviceId=102

curl -v -u${adminUser}:${adminPasswd} -X DELETE -H "Accept:application/json" -H "Content-Type:application/json" http://${rangerServerAddr}/service/plugins/definitions/${serviceId}

5. 创建服务成功后，可在 Ranger 控制台看到 COS 服务。如下所示：

![Image 6](https://qcloudimg.tencent-cloud.cn/image/document/a6d5c9ca4a9198b5e1d9aaa5c91f89a2.png)

![Image 7](https://qcloudimg.tencent-cloud.cn/image/document/a6d5c9ca4a9198b5e1d9aaa5c91f89a2.png)

6. 在 COS 服务侧单击**+**，定义新服务实例，服务实例名可自定义，例如`cos`或者`cos_test`，服务的配置如下所示。

![Image 8](https://qcloudimg.tencent-cloud.cn/image/document/620874c9c1615c8826cbc7cbb0b666f1.png)

![Image 9](https://qcloudimg.tencent-cloud.cn/image/document/620874c9c1615c8826cbc7cbb0b666f1.png)

 配置项需添policy.grantrevoke.auth.users和policy.download.auth.users。value设置后续启动 COS Ranger Service 服务的用户名（即允许拉取权限策略的用户）。通常建议设置成 hadoop，后续 COS Ranger Service 可使用此用户名进行启动。

7. 单击新生成的 COS 服务实例。

![Image 10](https://qcloudimg.tencent-cloud.cn/image/document/f3907f158551b27c4782507fbb39836d.png)

![Image 11](https://qcloudimg.tencent-cloud.cn/image/document/f3907f158551b27c4782507fbb39836d.png)

 添加 policy，如下所示：

![Image 12](https://qcloudimg.tencent-cloud.cn/image/document/ca4819bb8985fcd60f82d206144b4880.png)

![Image 13](https://qcloudimg.tencent-cloud.cn/image/document/ca4819bb8985fcd60f82d206144b4880.png)

8. 在跳转界面中，配置以下参数，说明如下：

**bucket**：存储桶名称，例如 examplebucket-1250000000，可登录 [COS 控制台](https://console.cloud.tencent.com/cos5/bucket) 查看。

**path**：COS 对象路径。注意 COS 的对象路径不以/开始。

include：表示设置的权限适用于 path 本身，还是除了 path 以外的其他路径。

recursive：表示权限不仅适用于 path，还适用于 path 路径下的子成员（即递归子成员）。通常用于 path 设置为目录的情况。

**user/group**：用户名和用户组。这里是或的关系，即用户名或者用户组满足其中一个，即可拥有对应的操作权限。

**Permissions**：

Read：读操作。对应于对象存储里面的 GET、HEAD 类操作，包括下载对象、查询对象元数据等。

Write：写操作。对应于对象存储里面的 PUT 类等修改操作，例如上传对象。

Delete：删除操作。 对应于对象存储里删除 Object。对于 Hadoop 的 Rename 操作，需要有对原路径的删除操作权限，对新路径的写入操作权限。

List：遍历权限。对应于对象存储里面的 List Object。

![Image 14](https://qcloudimg.tencent-cloud.cn/image/document/c869e20168a1829db84742c23e72c2f2.png)

![Image 15](https://qcloudimg.tencent-cloud.cn/image/document/c869e20168a1829db84742c23e72c2f2.png)

COS-Ranger-Service 是整个权限体系的核心，负责集成 ranger 的客户端，接收 ranger client 的鉴权请求，token 生成续租请求和临时密钥生成请求。同时也是敏感信息（腾讯云密钥信息）所在的区域，通常部署在堡垒机器上，只允许集群管理员操作，查看配置等。

COS-Ranger-Service 支持多节点的 HA 部署，DelegationToken 状态持久化到 DB上。通过 ZK 互相感知彼此节点的存在。通过客户端配置的任何一个存活的 cos-ranger-server 的地址， 即可知道全量的列表。 客户端通过 round-robin 的方式, 把请求发送给所有 cos-ranger-server 的节点. 因此可以通过平行扩容 cos-ranger-server，来提升整体的鉴权能力。

#### 代码地址

可前往 [Github](https://github.com/tencentyun/cos-ranger-service) 的 cos-ranger-server 目录下获取。

#### 版本

V6.0 版本及以上。

#### 部署步骤

1. 将 COS Ranger Service 服务代码拷贝到集群的几台机器上，生产环境建议至少两台机器。因为涉及到敏感信息，建议是堡垒机或者权限严格管控的机器。

2. 如果是 kerberos 集群, 则需要一个 db 来保存 Delegation Token（有关 kerberos 的 Delegation token 的作用, 搜索相关博文即可）， db 规格推荐16c32g，100g磁盘以上。在负载不高的集群上，可混用 Hive meta store 的 db。 初始化 database 和表的 sql 语句可前往 [Github](https://github.com/tencentyun/cos-ranger-service) 的 cos-ranger-service/sql 目录下获取.

3. 修改 cos-ranger.xml 文件中的相关配置，其中必须修改的配置项如下所示。配置项说明请参见文件中的注释说明（配置文件可前往 [Github](https://github.com/tencentyun/cos-ranger-service) 的 cos-ranger-service/conf 目录下获取）。

qcloud.object.storage.rpc.address

qcloud.object.storage.status.port

qcloud.object.storage.enable.cos.ranger

qcloud.object.storage.zk.address （zk 地址，cos ranger service 启动后注册到 zk 上）

qcloud.object.storage.cos.secret.id

qcloud.object.storage.cos.secret.key

qcloud.object.storage.kerberos.principal (kerberos 集群下的 principal, 非 kerberos 请忽略)

qcloud.object.storage.kerberos.keytab (kerberos 集群下的 keytab 文件, 非 kerberos 请忽略)

sql-dt-secret-manager.connection.url（kerberos 集群, 保存 delegation token 的db, 非 kerberos 请忽略)

sql-dt-secret-manager.connection.username (kerberos 集群, 访问 delegation token 的db的用户名, 非 kerberos 请忽略)

hadoop.security.credential.provider.path (kerberos 集群, 访问 delegation token 的db的用户密码的 jceks 文件路径, 非 kerberos 请忽略)

4. 修改 ranger-cos-security.xml 文件中的相关配置。其中必须修改的配置项有如下所示。配置项说明请参见文件中的注释说明（配置文件可前往 [Github](https://github.com/tencentyun/cos-ranger-service) 的 cos-ranger-service/conf 目录下获取）。

ranger.plugin.cos.policy.cache.dir

ranger.plugin.cos.policy.rest.url

ranger.plugin.cos.service.name

5. 修改 start_rpc_server.sh 中 hadoop_conf_path 和 java.library.path 的配置。这两个配置分别指向 hadoop 配置文件所在的目录（例如 core-site.xml、hdfs-site.xml）以及 hadoop native lib 路径。

6. 执行如下命令启动服务。

chmod +x start_rpc_server.sh

nohup ./start_rpc_server.sh &> nohup.txt &

7. 如果启动失败，查看 log 下 error 日志是否有错误信息。

8. COS Ranger Service 支持展示 HTTP 端口状态（端口名为 qcloud.object.storage.status.port，默认值为9998）。用户可通过以下命令获取状态信息（例如目前全量的cos-ranger-server列表、鉴权数量统计等）。

# 请将下面的10.xx.xx.xxx替换为部署 ranger service 的机器 IP

# port 9998 设置为 qcloud.object.storage.status.port 配置值

curl -v http://10.xx.xx.xxx:9998/status

COS Ranger Client 由 hadoop cosn 插件动态加载，并代理访问 COS Ranger Service 的相关请求。例如获取临时密钥、获取 token、鉴权操作等。

#### 代码地址

可前往 [Github](https://github.com/tencentyun/cos-ranger-service) 的 cos-ranger-client 和 cosn-ranger-interface 目录下获取。

#### 版本

cos-ranger-client 要求V6.0 版本及以上。cosn-ranger-interface 要求 v1.0.5版本及以上。

腾讯云 EMR 环境中默认安装目录在 common/lib 下，例如 /usr/local/service/hadoop/share/hadoop/common/lib 下。请根据自己的环境，放在对应的common/lib 路径下。 对于 ranger-client 的包名，例如 hadoop-ranger-client-for-hadoop-2.8.5-6.0.jar，2.8.5 是 hadoop 版本号，6.0是该包的版本号。for-hadoop 是通常组件使用的版本，其他一些组件，例如 presto， impala 以及高版本的 spark(spark-3.2.0版本及以后) 等，由于对依赖的 hadoop-common做了 shade，因此 ranger-client 也必须做 shade，否则会报类找不到。这些包请下载对应的 for-presto, for-impala, for-spark 版本等。

#### 部署方式

1. 将 cos-ranger-client jar 包和cosn-ranger-interface jar 包拷贝到与 COSN 同一目录下通常在/usr/local/service/hadoop/share/hadoop/common/lib/目录下；请选择拷贝与自身 hadoop 大版本一致的 jar 包，最后确保 jar 包有可读权限。

2. 在 core-site.xml 添加如下配置项：

```

<configuration>

 <!--*****必须配置********-->

 <!-- 上一步部署的 cos ranger server 的地址 -->

 <property>

 <name>qcloud.object.storage.ranger.service.address</name>

 <value>10.0.0.8:9999,10.0.0.10:9999</value>

 </property>

 <!--***可选配置****-->

 <!-- 设置 cos ranger service 端用的 kerberos 凭据，参考 cos ranger service 端的配置，须保持一致，如果没有认证的需求，不需要配置 -->

 <property>

 <name>qcloud.object.storage.kerberos.principal</name>

 <value>hadoop/_HOST@EMR-XXXX</value>

 </property>

</configuration>

```

#### 版本

V8.3.5版本及以上。

#### 部署方式

部署 COSN 插件方法请参考 [Hadoop 工具](https://cloud.tencent.com/document/product/436/6884) 文档，但需注意以下几点：

1. 使用 ranger 后，fs.cosn.userinfo.secretId 和 fs.cosn.userinfo.secretKey 密钥信息不需要配置。COSN 插件后续通过 COSRangerService 获取临时密钥。

2. fs.cosn.credentials.provider 需设置为 org.apache.hadoop.fs.auth.RangerCredentialsProvider 才可通过 Ranger 进行认证鉴权。如下所示：

```

<property>

 <name>fs.cosn.credentials.provider</name>

 <value>org.apache.hadoop.fs.auth.RangerCredentialsProvider</value>

</property>

```

## 验证

1. 使用 hadoop cmd 执行访问 COSN 的相关操作。查看当前用户执行的操作是否符合主账号的权限设置预期，示例如下所示：

#将bucket，路径等替换为主账号的实际信息。

hadoop fs -ls cosn://examplebucket-1250000000/doc

hadoop fs -put ./xxx.txt cosn://examplebucket-1250000000/doc/

hadoop fs -get cosn://examplebucket-1250000000/doc/exampleobject.txt

hadoop fs -rm cosn://examplebucket-1250000000/doc/exampleobject.txt

2. 使用 MR Job 进行验证，验证前需重启相关的服务，例如 Yarn、Hive 等。

## 获取统计信息

可以通过以下 curl 命令手动获取 COS Ranger 的统计信息

curl http://${ranger_ip}:9998/status | jq

# 返回

{

 "allMemberAddress": "10.0.0.7:9999",//集群中所有成员的地址

 "currentNodeIsLeader": true, // 当前节点是否是leader节点

 "leaderAddress": "10.0.0.7:9999", // leader地址(对于客户端v5.x版本有意义，v6.x后是全对等模式，leader信息没有意义

 "authStat": {// 自定义鉴权认证的次数统计信息(对于为实现自定义认证的服务，始终是认证成功)

 "authSuccessStat": { // 认证成功统计信息

 "qps_5m": 0,// 最近 5 分钟的每秒查询数（QPS）

 "total_1m": 0,//最近 1 分钟的总成功认证次数

 "qps_1m": 0,// 最近 1 分钟的每秒查询数

 "total_5m": 0,//最近 5 分钟的总成功认证次数

 "qps": 0//当前的每秒查询数

 },

 "authFailedStat": {// 鉴权认证失败统计信息,字段含义与 authSuccessStat 相同

 "qps_5m": 0,

 "total_1m": 0,

 "qps_1m": 0,

 "total_5m": 0,

 "qps": 0

 }

 },

 "rpcMethodStat": {//包含不同 RPC 方法的调用次数的统计信息

 "checkPermission": {//检查权限的方法统计信息

 "qps_5m": 10,

 "total_1m": 3000,

 "qps_1m": 50,

 "total_5m": 3000,

 "qps": 1000

 },

 "getAvailableService": {//获取可用服务的方法统计信息

 "qps_5m": 0,

 "total_1m": 1,

 "qps_1m": 0.02,

 "total_5m": 1,

 "qps": 0

 }

 },

 "checkPermissionAllowAfterRetryCnt": 0,// 经过重试后允许的权限检查次数

 "checkPermissionAllowCnt": 4000,//允许的权限检查总次数

 "becomeLeaderTime": "2024-12-10T12:56:52.888Z",//当前节点成为leader的时间

 "checkAuthDenyCnt": 0,//被拒绝的认证检查次数

 "serviceStartTime": "2024-12-10T12:56:52.884Z",//服务启动的时间

 "checkPermissionDenyCnt": 0,//被拒绝的权限检查次数

 "accessStat": {//包含不同访问类型的统计信息

 "READ": {//读取操作的统计信息

 "qps_5m": 10,

 "total_1m": 3000,

 "qps_1m": 50,

 "total_5m": 3000,

 "qps": 1000

 }

 },

 "checkCostStat": {//checkPermission(检查权限)耗时的统计信息

 "checkFailStat": {//失败

 "avg_5m": 0,

 "min_1m": 0,

 "avg": 0,

 "min": 0,

 "max": 0,

 "max_1m": 0,

 "avg_1m": 0,

 "max_5m": 0,

 "min_5m": 0

 },

 "checkSuccessStat": {//成功

 "avg_5m": 5,//最近 5 分钟的平均耗时

 "min_1m": 0,//最近1分钟最小耗时

 "avg": 4,//平均耗时

 "min": 0,//最小耗时

 "max": 1263,//最大耗时

 "max_1m": 1263,//最近一分钟最大耗时

 "avg_1m": 5,//最近一分钟平均耗时

 "max_5m": 1263,//最近五分钟最大耗时

 "min_5m": 0//最近五分钟最小耗时

 }

 },

 "authCostStat": {// 权限认证耗时统计

 "authSuccessStat": {

 "avg_5m": 0,

 "min_1m": 0,

 "avg": 0,

 "min": 0,

 "max": 0,

 "max_1m": 0,

 "avg_1m": 0,

 "max_5m": 0,

 "min_5m": 0

 },

 "authFailedStat": {

 "avg_5m": 0,

 "min_1m": 0,

 "avg": 0,

 "min": 0,

 "max": 0,

 "max_1m": 0,

 "avg_1m": 0,

 "max_5m": 0,

 "min_5m": 0

 }

 },

 "rpcMethodCostStat": {//RPC接口耗时统计

 "checkPermission": {

 "avg_5m": 5,

 "min_1m": 0,

 "avg": 4,

 "min": 0,

 "max": 1263,

 "max_1m": 1263,

 "avg_1m": 5,

 "max_5m": 1263,

 "min_5m": 0

 },

 "getAvailableService": {

 "avg_5m": 280,

 "min_1m": 280,

 "avg": 280,

 "min": 280,

 "max": 280,

 "max_1m": 280,

 "avg_1m": 280,

 "max_5m": 280,

 "min_5m": 280

 }

 },

 "statsTimestamp": "2024-12-12T05:28:38.688Z",//统计时间

 "checkStat": {// check policy统计信息

 "checkFailStat": {

 "qps_5m": 0,

 "total_1m": 0,

 "qps_1m": 0,

 "total_5m": 0,

 "qps": 0

 },

 "checkSuccessStat": {

 "qps_5m": 10,

 "total_1m": 3000,

 "qps_1m": 50,

 "total_5m": 3000,

 "qps": 1000

 }

 }

}

接口的出参定义如下：

**一级字段****二级字段****三级字段****字段含义**
serviceStartTime--服务启动时间
currentNodeIsLeader--当前节点是否是leader
becomeLeaderTime--成为leader时间
statsTimestamp--统计时间
leaderAddress--leader地址
allMemberAddress--集群内所有成员地址
checkPermissionAllowCnt--check permission成功数
checkAuthDenyCnt--认证鉴权失败数
checkPermissionDenyCnt--check permission失败数
checkPermissionAllowAfterRetryCnt--重试后check permission成功数
accessStat--操作统计
accessStat LIST-List操作次数
accessStat WRITE-Write操作次数
accessStat READ-Read操作次数
accessStat DELETE-Delete操作次数
authStat--认证统计
authStat authSuccessStat qps、qps_1m、qps_5m、count_1m、count_5m 认证成功统计
authStat authFailedStat qps、qps_1m、qps_5m、count_1m、count_5m 认证失败统计
authCostStat--认证耗时统计
authCostStat authSuccessStat max、min、avg、max_1m、min_1m、avg_1m、max_5m、min_5m、avg_5m 认证成功耗时统计
authCostStat authFailedStat max、min、avg、max_1m、min_1m、avg_1m、max_5m、min_5m、avg_5m 认证失败耗时统计
checkStat--check permission统计
checkStat checkSuccessStat qps、qps_1m、qps_5m、count_1m、count_5m check permission成功统计
checkStat checkFailStat qps、qps_1m、qps_5m、count_1m、count_5m check permission失败统计
checkCostStat--check permission耗时统计
checkCostStat checkSuccessStat max、min、avg、max_1m、min_1m、avg_1m、max_5m、min_5m、avg_5m check permission成功耗时统计
checkCostStat checkFailStat max、min、avg、max_1m、min_1m、avg_1m、max_5m、min_5m、avg_5m check permission失败耗时统计
rpcMethodStat--rpc方法统计
rpcMethodStat getDelegationToken qps、qps_1m、qps_5m、count_1m、count_5m getDelegationToken方法统计
rpcMethodStat renewDelegationToken qps、qps_1m、qps_5m、count_1m、count_5m renewDelegationToken方法统计
rpcMethodStat cancelDelegationToken qps、qps_1m、qps_5m、count_1m、count_5m cancelDelegationToken方法统计
rpcMethodStat verifyDelegationToken qps、qps_1m、qps_5m、count_1m、count_5m verifyDelegationToken方法统计
rpcMethodStat checkPermission qps、qps_1m、qps_5m、count_1m、count_5m checkPermission方法统计
rpcMethodStat getSTS qps、qps_1m、qps_5m、count_1m、count_5m getSTS方法统计
rpcMethodStat getRangerAuthPolicy qps、qps_1m、qps_5m、count_1m、count_5m getRangerAuthPolicy方法统计
rpcMethodStat getAvailableService qps、qps_1m、qps_5m、count_1m、count_5m getAvailableService方法统计
rpcMethodCostStat RPC方法耗时统计
rpcMethodCostStat getDelegationToken max、min、avg、max_1m、min_1m、avg_1m、max_5m、min_5m、avg_5m getDelegationToken方法统计
rpcMethodCostStat renewDelegationToken max、min、avg、max_1m、min_1m、avg_1m、max_5m、min_5m、avg_5m renewDelegationToken方法统计
rpcMethodCostStat cancelDelegationToken max、min、avg、max_1m、min_1m、avg_1m、max_5m、min_5m、avg_5m cancelDelegationToken方法统计
rpcMethodCostStat verifyDelegationToken max、min、avg、max_1m、min_1m、avg_1m、max_5m、min_5m、avg_5m verifyDelegationToken方法统计
rpcMethodCostStat checkPermission max、min、avg、max_1m、min_1m、avg_1m、max_5m、min_5m、avg_5m checkPermission方法统计
rpcMethodCostStat getSTS max、min、avg、max_1m、min_1m、avg_1m、max_5m、min_5m、avg_5m getSTS方法统计
rpcMethodCostStat getRangerAuthPolicy max、min、avg、max_1m、min_1m、avg_1m、max_5m、min_5m、avg_5m getRangerAuthPolicy方法统计
rpcMethodCostStat getAvailableService max、min、avg、max_1m、min_1m、avg_1m、max_5m、min_5m、avg_5m getAvailableService方法统计

## 常见问题

#### 如果开启了 Ranger，但未配置任何 Policy，或者未匹配到任何 Policy，会如何操作？

如果未匹配上任何 policy，会默认拒绝该操作。

#### 配置 COS Ranger Service 侧的密钥可以是子账号？

可以是子账号，但是必须拥有被操作 bucket 的相应权限，才能生成临时密钥给到 COSN 插件，进行相应的操作。通常建议这里设置的密钥拥有对该 bucket 的所有权限。

#### 临时密钥需如何更新，每次访问 COS 前都需要从 COS Ranger Service 侧获取?

临时密钥是 cache 在 COSN 插件侧，并周期性进行异步更新。

#### 在 ranger 页面更改了 Policy 未生效怎么办？

请修改 ranger-cos-security.xml 文件的配置项：ranger.plugin.cos.policy.pollIntervalMs，调小该配置项（单位为毫秒），然后重启 COS Ranger Service 服务。Policy 相关测试结束后，建议修改回原来值（时间间隔太小导致轮询频率高，从而导致 CPU 负载高）。

#### **其他认证和鉴权的问题可**[点击此处](https://cloud.tencent.com/document/product/436/80261)**查看。**
