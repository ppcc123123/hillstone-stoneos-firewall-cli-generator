#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
通用 PDF 配置手册提取脚本
============================
将厂商配置手册 PDF 按 map.json 定义的主题分组，提取为 references/*.md 文件。

用法:
    python3 extract_pdf.py <pdf_path> --map map.json --output <references_dir>

特性:
    - 基于 PDF 书签(TOC) 计算章节页码范围
    - 按主题聚合多个章节到一个文件
    - 自动清洗文本(合并断行、去除页码页眉噪声)
    - reference 内容以 PDF 为唯一真相，修正必须重跑本脚本
"""

import argparse
import json
import os
import re
import sys

import fitz  # PyMuPDF


def load_toc(doc):
    """返回 L1 章节列表: [(number, title, start_page, end_page), ...]"""
    toc = doc.get_toc()
    l1 = []
    for item in toc:
        level, title, page = item[0], item[1], item[2]
        if level == 1:
            # 解析 "N 标题" 中的编号
            m = re.match(r'^\s*(\d+)\s*(.*)$', title)
            num = int(m.group(1)) if m else len(l1) + 1
            name = m.group(2).strip() if m else title.strip()
            l1.append({"num": num, "name": name, "title": title, "page": page})
    # 计算每章结束页 = 下一章起始页 - 1
    for i, ch in enumerate(l1):
        if i + 1 < len(l1):
            ch["end"] = l1[i + 1]["page"] - 1
        else:
            ch["end"] = doc.page_count
    return l1


def clean_text(text):
    """清洗提取出的文本: 修复单词断行、去除孤立页码。"""
    # 合并被换行切断的英文单词 (如 config-\nuration -> configuration)
    text = re.sub(r'([a-zA-Z])-\n([a-zA-Z])', r'\1\2', text)
    # 合并被换行切断的中文词组 (无空格断行) - 谨慎处理
    # 去除行尾孤立的页码标记如 "- 395 -"
    text = re.sub(r'^\s*-\s*\d+\s*-\s*$', '', text, flags=re.MULTILINE)
    # 合并多余空行
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def extract_chapter(doc, chapter, verbose=True):
    """提取单个章节所有页文本。"""
    pages = []
    start = max(0, chapter["page"] - 1)
    end = min(doc.page_count - 1, chapter["end"] - 1)
    for pn in range(start, end + 1):
        page = doc[pn]
        txt = page.get_text()
        if txt.strip():
            pages.append(f"\n<!-- 来源页 {pn + 1} -->\n" + clean_text(txt))
    if verbose:
        print(f"    章节 [{chapter['title']}] p{chapter['page']}-{chapter['end']} -> {len(pages)} 页文本")
    return "\n".join(pages)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", help="源 PDF 路径")
    ap.add_argument("--map", default="map.json", help="主题映射 JSON")
    ap.add_argument("--output", default="references", help="输出目录")
    args = ap.parse_args()

    if not os.path.exists(args.map):
        print(f"[ERROR] map 文件不存在: {args.map}", file=sys.stderr)
        sys.exit(1)

    with open(args.map, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    os.makedirs(args.output, exist_ok=True)
    doc = fitz.open(args.pdf)
    print(f"PDF: {args.pdf}  总页数={doc.page_count}")

    chapters = load_toc(doc)
    print(f"识别 L1 章节: {len(chapters)} 个")

    # 建立 num -> chapter 索引
    ch_by_num = {ch["num"]: ch for ch in chapters}

    index_entries = []
    for theme in cfg["themes"]:
        key = theme["key"]
        title = theme["title"]
        out_path = os.path.join(args.output, f"{key}.md")
        print(f"\n[提取] {key} - {title}")

        collected = []
        chapter_names = []
        for cnum in theme.get("chapters", []):
            if cnum in ch_by_num:
                ch = ch_by_num[cnum]
                collected.append(extract_chapter(doc, ch))
                chapter_names.append(ch["title"])
            else:
                print(f"    [WARN] 章节号 {cnum} 未在 TOC 中找到，跳过")

        if not collected:
            print(f"    [SKIP] 无内容")
            continue

        body = "\n\n---\n\n".join(collected)
        header = (
            f"# {title}\n\n"
            f"> 来源: {cfg.get('source_pdf', '官方配置手册')}\n"
            f"> 覆盖章节: {', '.join(chapter_names)}\n"
            f"> 本文件由 extract_pdf.py 从官方 PDF 自动提取，请勿手动编辑；"
            f"如需修正请修改 map.json 后重跑脚本。\n\n---\n\n"
        )
        content = header + body + "\n"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        size = len(content)
        print(f"    已保存 {out_path} ({size} 字符)")
        index_entries.append((key, title, theme.get("desc", ""), size))

    doc.close()

    # 生成 index.md
    idx_path = os.path.join(args.output, "index.md")
    lines = ["# 配置参考索引\n", "> 本索引由 extract_pdf.py 自动生成。\n", "| 文件 | 主题 | 内容 | 大小 |\n", "|---|---|---|---|\n"]
    for key, title, desc, size in index_entries:
        lines.append(f"| `{key}.md` | {title} | {desc} | {size} |\n")
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write("".join(lines))
    print(f"\n[完成] 索引已生成: {idx_path}")
    print(f"[完成] 共提取 {len(index_entries)} 个主题文件")


if __name__ == "__main__":
    main()
