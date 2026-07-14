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

在项目根目录配置密钥：

```bash
cp .env.example .env
# 编辑 .env，填入真实 key
```

```env
jina_key=jina_xxxxxxxx          # 可选；无 key 时走 Jina 免费额度
tavily_key=tvly-xxxxxxxx        # 使用 --backend tavily 时需要
```

也支持 `JINA_API_KEY` / `TAVILY_API_KEY`。

## 导出 urls.json（浏览器脚本）

在腾讯云文档页用 Console 展开侧栏并导出链接列表：

1. 打开产品文档，例如 <https://cloud.tencent.com/document/product/1814>
2. F12 → Console，粘贴 [`scripts/export_tencent_docs_urls.js`](scripts/export_tencent_docs_urls.js) 全文并回车
3. JSON 会复制到剪贴板，保存为 `datas/<product>/urls.json`

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
# 默认 jina + 4 并发 + tqdm；抓完自动写 AGENTS.md
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

# 索引相关（默认会生成 AGENTS.md）
uv run main.py datas/sandbox/urls.json --index-style tree
uv run main.py datas/sandbox/urls.json --claude          # 额外 CLAUDE.md -> AGENTS.md
uv run main.py datas/sandbox/urls.json --no-index        # 不写 AGENTS.md
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
<!-- fetched_at: 2026-07-13T16:30:00+08:00 -->

# 页面正文 ...
```

`fetched_at` 为抓取时刻，时区固定为东八区（`Asia/Shanghai`）。

## 项目结构

```
fetch_tencent_docs/
├── main.py                 # CLI / 并发 / 落盘
├── clean_md.py             # 清洗导航/页脚噪音
├── gen_index.py            # 生成 AGENTS.md（Agent 目录索引）
├── scripts/
│   └── export_tencent_docs_urls.js  # 浏览器 Console：导出 urls.json
├── fetchers/
│   ├── __init__.py         # create_fetcher()
│   ├── base.py             # Fetcher 抽象
│   ├── jina.py             # Jina Reader (httpx)
│   └── tavily.py           # Tavily Extract (tavily-python SDK)
├── pyproject.toml
├── .env.example            # 环境变量模板（可提交）
├── .env                    # API Key（勿提交，从 .env.example 复制）
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

## 生成 Agent 索引（gen_index.py）

给 Agent 用的文件索引，默认写到 `datas/<product>/AGENTS.md`（符合常见 Agent 约定）。

```bash
# 推荐：嵌套分组，不重复父路径前缀（默认）
uv run gen_index.py datas/sandbox

# 额外创建相对软链 CLAUDE.md -> AGENTS.md（默认不创建）
uv run gen_index.py datas/sandbox --claude

# 纯路径列表（grep 友好）
uv run gen_index.py datas/sandbox --style paths

# ASCII 树（人类好看，符号更费 token）
uv run gen_index.py datas/sandbox --style tree
```

| style | 特点 | 适用 |
| --- | --- | --- |
| `grouped`（默认） | `## 顶层` + 嵌套列表，目录名只写一次（如 `- Go SDK 常见问题/ (99)`） | Agent 导航 |
| `paths` | 一行一个完整相对路径 | 极简 / 脚本 |
| `tree` | `├──` 树形 | 给人看 |

`grouped` 路径还原规则：

- `## 准备工作` + `- 简介.md` → `准备工作/简介.md`
- `## 准备工作` + `- Go SDK 常见问题/ (99)` + `  - 上传对象.md` → `准备工作/Go SDK 常见问题/上传对象.md`
- 更深层：`- 人像抠图/ (3)` 下的 `  - 创建任务.md` → `.../人像抠图/创建任务.md`（忽略 `(n)` 计数）

建议流水线：

```bash
# main 默认已生成 AGENTS.md；clean 后可再刷一次索引
uv run main.py datas/sandbox/urls.json -b jina -c 2
uv run clean_md.py datas/sandbox
uv run gen_index.py datas/sandbox   # 可选：清洗后刷新 AGENTS.md
```

## 说明

- 默认后端是 **jina**；`jina_key` 可选，有 key 会带 `Authorization: Bearer`。
- **tavily** 使用官方 SDK，必须配置 `tavily_key`。
- 失败条目会汇总打印；有失败时退出码为 1。
- 请妥善保管 API Key，不要把 `.env` 提交到 Git。
