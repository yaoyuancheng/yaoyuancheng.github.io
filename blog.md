---
layout: page
title: "Blog"
permalink: /blog/
---

# Blog Posts

Welcome to my blog! Here you'll find articles about AI, open source, development, and occasional thoughts about giraffes 🦒.

{% for post in site.posts %}
## [{{ post.title }}]({{ post.url | relative_url }})
*{{ post.date | date: "%Y-%m-%d" }}* • {{ post.categories | join: ", " }}

{{ post.excerpt | strip_html | truncatewords: 50 }}

[Read more →]({{ post.url | relative_url }})

---
{% endfor %}

## Categories

{% assign categories = site.posts | map: 'categories' | flatten | uniq | sort %}
{% for category in categories %}
- [{{ category }}](/category/{{ category | slugify }}/)
{% endfor %}

## Subscribe

Want to stay updated? You can:
- **RSS Feed:** [Subscribe via RSS](/feed.xml)
- **GitHub:** Follow [@yaoyuancheng](https://github.com/yaoyuancheng) for project updates
- **Check back regularly:** New posts every 1-2 weeks

---

*"Writing is thinking. To write well is to think clearly." - David McCullough*