<!-- source: https://cloud.tencent.com/document/product/436/56423 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:24:06+08:00 -->

# 获取 GooseFS 监控指标

最近更新时间：2024-08-21 16:32:52


## 获取监控指标

以下介绍三种基础的获取监控指标的途径：

### 1. 通过 JSON 格式拉取监控指标

GooseFS 默认的获取监控指标的方式是通过 JSON 格式拉取，对应着 MetricsServlet 这一配置项。可以在命令行中向 GooseFS 的 Leading Master 节点发起一个 HTTP 请求，拉取所需的监控指标，其中 master 的 metrics 端口为9201，worker 的 metrics 端口为 9204。请求指令格式如下：

$ curl <LEADING_MASTER_HOSTNAME>:<MASTER_WEB_PORT>/metrics/json

如上示例中，<LEADING_MASTER_HOSTNAME> 需要是合法的 MASTER 节点的 IP，<MASTER_WEB_PORT> 需要为已经启用的端口。

如果需要获取某个 WORKER 节点的监控指标，可以通过如下方式获取：

$ curl <WORKER_HOSTNAME>:<WORKER_WEB_PORT>/metrics/json

### 2. 通过 CSV 文件获取监控指标

GooseFS 支持将数据导出为 CSV 格式文件，通过该能力获取监控指标，首先需要准备一个存储监控指标的目录：

$ mkdir /tmp/goosefs-metrics

准备好存储路径后，修改配置文件 conf/metrics.properties ，启用 CsvSink 能力：

sink.csv.class=goosefs.metrics.sink.CsvSink # 启用CsvSink能力

sink.csv.period=1 # 设置监控指标导出周期

sink.csv.unit=seconds # 设置监控指标导出周期的单位

sink.csv.directory=/tmp/goosefs-metrics # 设置监控指标导出路径

配置好后需要重启节点以便配置生效。配置生效后，监控指标将周期性地导出成 CSV 格式并存储在指定路径下。

**注意：**

GooseFS 准备了监控配置模板，可以参考 conf/metrics.properties.template文件。

如果 GooseFS 是集群化部署，需要保证指定的指标存储路径能被所有节点读取。

### 3. 拉取 Prometheus 监控指标

GooseFS master 和 worker 的 Prometheus 的监控指标可用如下的命令查看，其中 master 的 metrics 端口为9201，worker 的 metrics 端口为 9204：

curl <LEADING_MASTER_HOSTNAME>:<MASTER_WEB_PORT>/metrics/prometheus/

# HELP Master_CreateFileOps Generated from Dropwizard metric import (metric=Master.CreateFileOps, type=com.codahale.metrics.Counter)

...

curl <WORKER_IP>:<WOKER_PORT>/metrics/prometheus/

# HELP pools_Code_Cache_max Generated from Dropwizard metric import (metric=pools.Code-Cache.max, type=com.codahale.metrics.jvm.MemoryUsageGaugeSet$$Lambda$51/137460818)

...
