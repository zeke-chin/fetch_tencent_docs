/**
 * 腾讯云文档侧栏目录导出脚本（浏览器 Console 执行）
 *
 * 用途：
 *   在腾讯云产品文档页打开 DevTools Console，粘贴并运行本脚本，
 *   会展开全部目录并导出 { "父级>子级": "url" } JSON，用于生成
 *   datas/<product>/urls.json，供 `uv run main.py ...` 抓取。
 *
 * 用法：
 *   1. 打开目标产品文档，例如：
 *      https://cloud.tencent.com/document/product/1814
 *   2. F12 → Console，粘贴本文件全部内容后回车
 *   3. JSON 会打印并复制到剪贴板
 *   4. 保存为 datas/<name>/urls.json
 *
 * 路径约定：
 *   key 使用 `>` 分隔层级（无空格），与 main.py 的目录落盘规则一致。
 *   例：产品简介>Agent 沙箱>Agent 沙箱概述
 */
(async () => {
  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  const expandable =
    '.J-expandable:not(.active):not(.on) > a.J-navLayer[href="javascript:void 0;"]';

  // 先递归展开全部目录
  for (let idle = 0; idle < 4; ) {
    const nodes = [...document.querySelectorAll(expandable)].filter(
      (node) => node.offsetParent !== null,
    );

    if (!nodes.length) {
      idle++;
      await sleep(300);
      continue;
    }

    idle = 0;
    nodes.forEach((node) => node.click());
    await sleep(250);
  }

  // 读取目录链接，并构建“父级>子级”路径
  const result = {};
  const stack = [];

  const links = [
    ...document.querySelectorAll("a.J-navLayer[data-node][data-level]"),
  ].filter((a) => /^https?:/.test(a.href));

  for (const a of links) {
    const level = Number(a.dataset.level);
    const name = (a.title || a.textContent).trim();
    if (!level || !name) continue;

    stack.length = level - 1;
    stack[level - 1] = name;

    // 与 datas/*/urls.json、main.py title_to_path 一致：用 > 分隔、无空格
    result[stack.filter(Boolean).join(">")] = a.href;
  }

  // 补充没有 data-level 的一级页面（如“词汇表”）
  for (const a of document.querySelectorAll(
    '.rno-column-aside-menu-wrap > a[href]:not([href^="javascript"])',
  )) {
    const name = (a.title || a.textContent).trim();
    if (name && /^https?:/.test(a.href)) result[name] ||= a.href;
  }

  const json = JSON.stringify(result, null, 2);
  console.log(json);

  if (typeof copy === "function") copy(json);
  else await navigator.clipboard.writeText(json);

  console.info(
    `已导出 ${Object.keys(result).length} 个页面，JSON 已复制到剪贴板。`,
  );
})();
