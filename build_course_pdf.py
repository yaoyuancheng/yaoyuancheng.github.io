#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 lessons.json 生成《每日表达力课程全集》HTML，供 Chromium 打印为 PDF"""
import json, html, datetime

L = json.load(open('/tmp/lessons.json', encoding='utf-8'))
START = datetime.date(2026, 5, 11)


def esc(s):
    return html.escape(str(s or ''))


def raw(s):
    """含 HTML 标签的字段：仅做最小转义，保留标签"""
    return str(s or '')


def li(items):
    return ''.join(f'<li>{raw(x)}</li>' for x in items)


def sec_text(s):
    return '<div class="sec sec-text">' + ''.join(
        f'<p>{raw(c)}</p>' for c in s.get('content', [])) + '</div>'


def sec_tip(s):
    label = f'<span class="tip-label">{esc(s.get("label"))}</span>' if s.get('label') else ''
    return ('<div class="sec sec-tip">'
            f'<div class="sec-head"><span class="sec-icon">{raw(s.get("icon"))}</span>'
            f'<span class="sec-title">{esc(s.get("title"))}</span>{label}</div>'
            + ''.join(f'<p>{raw(c)}</p>' for c in s.get('content', []))
            + '</div>')


def sec_comparison(s):
    rows = ''
    for r in s.get('rows', []):
        rows += ('<div class="cmp-row">'
                 f'<div class="cmp-cell cmp-before"><span class="cmp-tag">✗</span><div>{raw(r.get("before"))}</div></div>'
                 f'<div class="cmp-cell cmp-after"><span class="cmp-tag">✓</span><div>{raw(r.get("after"))}</div></div>'
                 '</div>')
    return ('<div class="sec sec-cmp">'
            f'<div class="sec-head"><span class="sec-icon">{raw(s.get("icon"))}</span>'
            f'<span class="sec-title">{esc(s.get("title"))}</span></div>'
            '<div class="cmp-legend"><span>✗ 常见说法</span><span>✓ 优化说法</span></div>'
            f'{rows}</div>')


def sec_case(s):
    blocks = ''
    for c in s.get('cases', []):
        t = c.get('type', '')
        cls = {'negative': 'case-bad', 'positive': 'case-good'}.get(t, 'case-neutral')
        blocks += (f'<div class="case-block {cls}">'
                   f'<div class="case-label">{raw(c.get("label"))}</div>'
                   f'<div class="case-body">{raw(c.get("text"))}</div></div>')
    return ('<div class="sec sec-case">'
            f'<div class="sec-head"><span class="sec-icon">{raw(s.get("icon"))}</span>'
            f'<span class="sec-title">{esc(s.get("title"))}</span></div>'
            f'{blocks}</div>')


def sec_practice(s):
    return ('<div class="sec sec-practice">'
            f'<div class="sec-head"><span class="sec-icon">{raw(s.get("icon"))}</span>'
            f'<span class="sec-title">{esc(s.get("title"))}</span></div>'
            + ''.join(f'<p>{raw(c)}</p>' for c in s.get('content', []))
            + '</div>')


def sec_quote(s):
    return ('<div class="sec sec-quote">'
            f'<div class="sec-head"><span class="sec-icon">{raw(s.get("icon"))}</span>'
            f'<span class="sec-title">{esc(s.get("title"))}</span></div>'
            f'<blockquote>{raw(s.get("quote"))}</blockquote>'
            f'<div class="quote-author">{raw(s.get("author"))}</div></div>')


RENDER = {'text': sec_text, 'tip': sec_tip, 'comparison': sec_comparison,
          'case': sec_case, 'practice': sec_practice, 'quote': sec_quote}

# ---- 封面 ----
days = len(L)
first_id, last_id = L[0]['id'], L[-1]['id']
toc_items = ''.join(
    f'<li><span class="toc-id">{l["id"]}</span>'
    f'<span class="toc-ic">{raw(l.get("icon"))}</span>'
    f'<span class="toc-t">{esc(l.get("title"))}</span></li>' for l in L)

cover = f'''<section class="cover">
  <div class="cover-badge">表达力修炼手账</div>
  <h1 class="cover-title">每日表达力课程<span class="cover-sub">全集</span></h1>
  <div class="cover-line"></div>
  <p class="cover-desc">从金字塔原理到提问的艺术<br>一场关于「说清楚、听明白、问到位」的长期修炼</p>
  <div class="cover-stats">
    <div class="stat"><b>{days}</b><span>节课程</span></div>
    <div class="stat"><b>{last_id - first_id + 1}</b><span>天跨度</span></div>
    <div class="stat"><b>58</b><span>万字</span></div>
  </div>
  <div class="cover-foot">2026.05.11 起 &nbsp;·&nbsp; 课程编号 {first_id}–{last_id}</div>
</section>
<section class="toc">
  <h2 class="toc-h">目 录</h2>
  <ol class="toc-list">{toc_items}</ol>
</section>'''

# ---- 正文 ----
body = ''
for l in L:
    secs = ''.join(RENDER.get(s['type'], sec_text)(s) for s in l.get('sections', []))
    body += f'''<section class="lesson">
  <div class="lesson-head">
    <div class="lesson-icon">{raw(l.get("icon"))}</div>
    <div class="lesson-meta">
      <h2 class="lesson-title"><span class="lesson-no">第 {l["id"]} 课&nbsp;</span>{esc(l.get("title"))}</h2>
      <div class="lesson-sub">{raw(l.get("subtitle"))}</div>
    </div>
  </div>
  {secs}
</section>'''

CSS = '''
@page { size: A4; margin: 16mm 14mm 16mm 14mm; }
@page cover { margin: 0; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: "Noto Sans CJK SC", "Noto Color Emoji", sans-serif;
  font-size: 10.5pt; line-height: 1.75; color: #24262e; margin: 0;
}
p { margin: 0 0 8px; }
strong { color: #1b3b6f; font-weight: 700; }
em { color: #7a5c2e; font-style: normal; background: #fff8e6; padding: 0 3px; border-radius: 3px; }

/* ---- 封面 ---- */
.cover { page: cover; height: 297mm; display: flex; flex-direction: column; justify-content: center;
  align-items: center; text-align: center; break-after: page;
  background: linear-gradient(160deg, #1e2a52 0%, #2f4a8f 45%, #4a6fc4 100%);
  color: #fff; margin: 0; padding: 0 18mm; }
.cover-badge { font-size: 12pt; letter-spacing: 6px; color: #b9c9f0; border: 1px solid #6d86c8;
  padding: 6px 20px; border-radius: 30px; margin-bottom: 30px; }
.cover-title { font-size: 42pt; font-weight: 800; margin: 0 0 10px; letter-spacing: 3px; line-height: 1.25; }
.cover-title .cover-sub { display: block; font-size: 30pt; color: #cddaf7; font-weight: 500; letter-spacing: 10px; }
.cover-line { width: 90px; height: 4px; background: #ffd166; margin: 22px 0 26px; border-radius: 2px; }
.cover-desc { font-size: 13pt; color: #d5def5; line-height: 2; margin: 0 0 46px; }
.cover-stats { display: flex; gap: 16px; margin-bottom: 50px; }
.stat { background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.25);
  border-radius: 14px; padding: 16px 26px; min-width: 100px; }
.stat b { display: block; font-size: 26pt; color: #ffd166; line-height: 1.2; }
.stat span { font-size: 10pt; color: #cfdaf3; letter-spacing: 2px; }
.cover-foot { font-size: 10.5pt; color: #9fb2dd; letter-spacing: 2px; }

/* ---- 目录 ---- */
.toc { break-after: page; }
.toc-h { text-align: center; font-size: 20pt; letter-spacing: 8px; color: #1e2a52;
  margin: 0 0 18px; padding-bottom: 10px; border-bottom: 3px double #b9c9f0; }
.toc-list { list-style: none; padding: 0; margin: 0; columns: 2; column-gap: 10mm; }
.toc-list li { break-inside: avoid; font-size: 9pt; padding: 2.2px 0; display: flex;
  align-items: baseline; border-bottom: 1px dotted #dfe4f0; }
.toc-id { color: #7b8bb5; min-width: 24px; font-size: 8pt; }
.toc-ic { min-width: 17px; }
.toc-t { flex: 1; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; }

/* ---- 课程 ---- */
.lesson { break-before: page; }
.lesson-head { display: flex; gap: 14px; align-items: flex-start; border-left: 6px solid #2f4a8f;
  background: linear-gradient(90deg, #eef2fc 0%, #f8fafd 70%, #fff 100%);
  padding: 14px 18px; border-radius: 0 12px 12px 0; margin-bottom: 16px; }
.lesson-icon { font-size: 26pt; line-height: 1; }
.lesson-no { display: block; font-size: 8.5pt; color: #6b7ba8; letter-spacing: 3px;
  font-weight: 400; margin-bottom: 2px; }
.lesson-title { font-size: 17pt; margin: 2px 0 4px; color: #16224a; line-height: 1.4; font-weight: 700; }
.lesson-sub { font-size: 9.5pt; color: #5c6784; line-height: 1.6; }

.sec { margin: 0 0 13px; padding: 12px 15px; border-radius: 10px; }
.lesson-head { break-after: avoid; }
.sec p { margin: 0 0 7px; }
.sec p:last-child { margin-bottom: 0; }
.sec-head { display: flex; align-items: center; gap: 8px; margin-bottom: 9px;
  padding-bottom: 7px; border-bottom: 1px solid rgba(0,0,0,.07); }
.sec-icon { font-size: 13pt; line-height: 1; }
.sec-title { font-size: 11.5pt; font-weight: 700; }

.sec-text { background: #f6f8fc; border-left: 4px solid #7d9be0; }
.sec-text .sec-title { color: #2f4a8f; }

.sec-tip { background: #fffbf0; border: 1px solid #f0dca6; border-left: 4px solid #e0a800; }
.sec-tip .sec-title { color: #8a6100; }
.tip-label { font-size: 8pt; background: #e0a800; color: #fff; padding: 2px 10px;
  border-radius: 20px; margin-left: auto; letter-spacing: 1px; }

.sec-cmp { background: #fbfcfe; border: 1px solid #e2e8f5; }
.sec-cmp .sec-title { color: #2f4a8f; }
.cmp-legend { display: flex; gap: 10px; font-size: 8pt; color: #8b96b3; margin-bottom: 7px; }
.cmp-legend span { flex: 1; }
.cmp-row { display: flex; gap: 9px; margin-bottom: 8px; break-inside: avoid; }
.cmp-row:last-child { margin-bottom: 0; }
.cmp-cell { flex: 1; padding: 9px 11px; border-radius: 8px; font-size: 9.5pt; line-height: 1.65; position: relative; }
.cmp-before { background: #fdf1f1; border: 1px solid #f3cfcf; }
.cmp-after { background: #eefaf1; border: 1px solid #c8ead4; }
.cmp-tag { position: absolute; top: -7px; left: 9px; font-size: 8pt; width: 16px; height: 16px;
  line-height: 16px; text-align: center; border-radius: 50%; color: #fff; }
.cmp-before .cmp-tag { background: #d9534f; }
.cmp-after .cmp-tag { background: #3d9e5f; }

.sec-case { background: #fafbfd; border: 1px solid #e4e9f3; }
.sec-case .sec-title { color: #2f4a8f; }
.case-block { padding: 10px 13px; border-radius: 9px; margin-bottom: 9px; break-inside: avoid; }
.case-block:last-child { margin-bottom: 0; }
.case-bad { background: #fdf3f3; border-left: 4px solid #d9534f; }
.case-good { background: #f0faf3; border-left: 4px solid #3d9e5f; }
.case-neutral { background: #f4f6fb; border-left: 4px solid #8fa4d4; }
.case-label { font-weight: 700; font-size: 10pt; margin-bottom: 6px; }
.case-bad .case-label { color: #a8342f; }
.case-good .case-label { color: #2b7a48; }
.case-neutral .case-label { color: #3c5185; }
.case-body { font-size: 9.5pt; line-height: 1.7; }

.sec-practice { background: #f2fbf6; border: 1px dashed #7fc79b; }
.sec-practice .sec-title { color: #24754a; }

.sec-quote { background: linear-gradient(135deg, #f3f0fb 0%, #faf8ff 100%);
  border: 1px solid #ded3f2; text-align: center; padding: 18px 22px; break-inside: avoid; }
.sec-quote .sec-title { color: #5b3fa8; }
.sec-quote .sec-head { justify-content: center; border-bottom: none; margin-bottom: 6px; }
.sec-quote blockquote { font-size: 13pt; line-height: 1.95; color: #3c2a6b; margin: 6px 0 10px;
  font-weight: 500; position: relative; }
.sec-quote blockquote::before { content: "“"; font-size: 34pt; color: #c3b3e8;
  position: absolute; left: -6px; top: -16px; }
.quote-author { font-size: 9.5pt; color: #7b6ba8; }
'''

# ---- 轻量模式（LIGHT=1）：去掉 border-radius 与渐变，PDF 体积约降 60% ----
# 圆角会被 Chromium 渲染成大量贝塞尔曲线指令（单页可达 600+ 条），是体积大头
import os, re as _re
if os.environ.get('LIGHT'):
    CSS = _re.sub(r'border-radius:\s*[^;]+;', '', CSS)
    CSS = (CSS
            .replace('background: linear-gradient(135deg, #f3f0fb 0%, #faf8ff 100%);', 'background: #f7f4fe;')
            .replace('background: linear-gradient(160deg, #1e2a52 0%, #2f4a8f 45%, #4a6fc4 100%);', 'background: #2b4180;')
            .replace('linear-gradient(90deg, #eef2fc 0%, #f8fafd 70%, #fff 100%)', '#f4f7fd'))
    out_html = '/tmp/course_light.html'
else:
    out_html = '/tmp/course_full.html'

doc = f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>每日表达力课程全集</title>
<style>{CSS}</style></head>
<body>{cover}{body}</body></html>'''

open(out_html, 'w', encoding='utf-8').write(doc)
print(f'✅ HTML 生成完成：{out_html}，{len(doc)/1024/1024:.2f} MB，{days} 节课')
