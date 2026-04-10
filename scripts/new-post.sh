#!/bin/bash

# Script to create a new blog post

set -e

# Get current date
DATE=$(date +%Y-%m-%d)

# Get title from command line or prompt
if [ -z "$1" ]; then
    echo "Enter post title:"
    read TITLE
else
    TITLE="$1"
fi

# Convert title to filename
FILENAME=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd '[:alnum:]-')
FILENAME="$DATE-$FILENAME.md"
FILEPATH="_posts/$FILENAME"

# Get categories
echo "Enter categories (comma-separated, e.g., ai,open-source):"
read CATEGORIES

# Create categories array
if [ -n "$CATEGORIES" ]; then
    CATEGORIES_ARRAY="[$(echo "$CATEGORIES" | sed "s/,/\", \"/g" | sed "s/^/\"/" | sed "s/$/\"/")]"
else
    CATEGORIES_ARRAY="[]"
fi

# Create post file
cat > "$FILEPATH" << EOF
---
layout: post
title: "$TITLE"
date: $DATE
categories: $CATEGORIES_ARRAY
author: Yuancheng Yao
---

# $TITLE

<!-- Start writing your post here -->

## Introduction

Start with an engaging introduction...

## Main Content

Add your main content here...

## Conclusion

Wrap up your thoughts...

---

*"Quote relevant to your post" - Author*
EOF

echo "✅ Created new post: $FILEPATH"
echo "📝 Open it in your editor to start writing!"