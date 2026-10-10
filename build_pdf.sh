#!/bin/bash
# 一键生成《每日表达力课程全集》PDF（轻量压缩版，适合 QQ 等平台发送）
# 用法: ./build_pdf.sh [输出路径]
set -e
cd "$(dirname "$0")"

CHROME=/root/.cache/ms-playwright/chromium-1228/chrome-linux64/chrome
OUT="${1:-/root/claude/每日表达力课程全集.pdf}"

echo "1/4 提取课程数据 (content.js → /tmp/lessons.json)..."
node extract.js

echo "2/4 生成轻量 HTML (去圆角/渐变)..."
LIGHT=1 python3 build_course_pdf.py

echo "3/4 Chromium 打印 PDF (746 页约需 1-2 分钟)..."
"$CHROME" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --virtual-time-budget=180000 --print-to-pdf=/tmp/course_print.pdf \
  file:///tmp/course_light.html 2>&1 | grep -i "bytes written" || true

echo "4/4 pikepdf 对象流压缩..."
python3 - <<'EOF'
import pikepdf
pdf = pikepdf.open('/tmp/course_print.pdf')
pdf.save('/tmp/course_final.pdf', compress_streams=True,
         object_stream_mode=pikepdf.ObjectStreamMode.generate, recompress_flate=True)
print('  压缩完成')
EOF

cp /tmp/course_final.pdf "$OUT"
echo "✅ 完成：$OUT ($(du -h "$OUT" | cut -f1))"
