# fetch_tencent_docs

从腾讯云文档 URL 列表抓取页面，保存为 Markdown。

支持两种后端：

| 后端 | 实现 | 说明 | 默认 |
| --- | --- | --- | --- |
| **jina** | `httpx` 复用连接 | [Jina Reader](https://jina.ai/reader/) `https://r.jina.ai/<url>` | ✅ |
| **tavily** | 官方 [tavily-python](https://github.com/tavily-ai/tavily-python) SDK | [Tavily Extract](https://docs.tavily.com/) | |

并发由线程池调度；Jina 侧用 httpx keepalive，Tavily 走 SDK。

## 环境要求

- Python >= 3.12
- [uv](https://github.com/astral-sh/uv)

## 安装

```bash
uv sync
```

在项目根目录配置 `.env`：

```env
jina_key=jina_xxxxxxxx          # 可选；无 key 时走 Jina 免费额度
tavily_key=tvly-xxxxxxxx        # 使用 --backend tavily 时需要
```

也支持 `JINA_API_KEY` / `TAVILY_API_KEY`。

## 输入：urls.json

JSON 对象，key 为文档标题路径，value 为 URL：

```json
{
  "产品动态": "https://cloud.tencent.com/document/product/1814/123809",
  "产品简介>Agent Runtime 概述": "https://cloud.tencent.com/document/product/1814/129423",
  "产品简介>Agent 沙箱>Agent 沙箱概述": "https://cloud.tencent.com/document/product/1814/123811"
}
```

规则：`>` 会被转成目录层级。

| key | 输出路径 |
| --- | --- |
| `产品动态` | `产品动态.md` |
| `产品简介>Agent Runtime 概述` | `产品简介/Agent Runtime 概述.md` |
| `产品简介>Agent 沙箱>Agent 沙箱概述` | `产品简介/Agent 沙箱/Agent 沙箱概述.md` |

输出目录 = `urls.json` 所在目录。

## 用法

```bash
# 默认 jina + 4 并发 + tqdm 进度条
uv run main.py datas/sandbox/urls.json

# 指定后端
uv run main.py datas/sandbox/urls.json -b jina
uv run main.py datas/sandbox/urls.json --backend tavily

# 指定并发
uv run main.py datas/sandbox/urls.json -c 8

# 断点续跑
uv run main.py datas/sandbox/urls.json --skip-existing

# Tavily 抽取深度（仅 tavily 生效）
uv run main.py datas/sandbox/urls.json -b tavily --depth basic

# 每个 worker 请求后额外 sleep（限速）
uv run main.py datas/sandbox/urls.json --delay 0.5
```

完整路径示例：

```bash
uv run main.py /Users/zeke/workspace/wm_work/fetch_tencent_docs/datas/sandbox/urls.json -c 6
```

会在 `datas/sandbox/` 下生成对应的 `.md` 文件。

## 输出说明

```markdown
<!-- source: https://cloud.tencent.com/document/product/1814/123809 -->
<!-- fetcher: jina -->

# 页面正文 ...
```

## 项目结构

```
fetch_tencent_docs/
├── main.py                 # CLI / 并发 / 落盘
├── fetchers/
│   ├── __init__.py         # create_fetcher()
│   ├── base.py             # Fetcher 抽象
│   ├── jina.py             # Jina Reader (httpx)
│   └── tavily.py           # Tavily Extract (tavily-python SDK)
├── pyproject.toml
├── .env                    # API Key（勿提交）
├── datas/
│   └── sandbox/
│       ├── urls.json
│       └── *.md
└── README.md
```

## 清洗噪音（clean_md.py）

Jina 抓下来的 Markdown 会夹带腾讯云整站导航/页脚。抓完后建议跑：

```bash
# 预览体积变化
uv run clean_md.py datas/sandbox --dry-run

# 就地清洗（删除导航/热词/本页目录/页脚等）
uv run clean_md.py datas/sandbox

# 保留「本页目录」
uv run clean_md.py datas/sandbox --keep-toc
```

清洗规则大致是：

1. **起点**：正文 `# 标题` + `最近更新时间`
2. **去掉**：顶部导航、近期搜索热词、产品 mega-menu、侧栏目录、分享按钮
3. **去掉**：`## 本页目录`（可用 `--keep-toc` 保留）
4. **终点**：`上一篇/下一篇`、相关文档列表、Copyright、AI 助手 chrome

实测 sandbox 全量约 **~84%** 体积是可删噪音。

## 说明

- 默认后端是 **jina**；`jina_key` 可选，有 key 会带 `Authorization: Bearer`。
- **tavily** 使用官方 SDK，必须配置 `tavily_key`。
- 失败条目会汇总打印；有失败时退出码为 1。
- 请妥善保管 API Key，不要把 `.env` 提交到 Git。
