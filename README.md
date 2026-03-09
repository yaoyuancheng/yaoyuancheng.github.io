# GitHub Pages 发布指南

## 你的个人主页文件已准备好！

位置：`/root/.openclaw/workspace/yaoyuancheng.github.io/index.html`

## 发布步骤

### 方法 1：使用 GitHub CLI（推荐）

```bash
# 1. 安装 gh CLI（如果没有）
# Ubuntu/Debian:
sudo apt update && sudo apt install gh -y

# 2. 登录 GitHub
gh auth login

# 3. 创建仓库并推送
cd /root/.openclaw/workspace/yaoyuancheng.github.io
gh repo create yaoyuancheng/yaoyuancheng.github.io --public --source=. --remote=origin --push
```

### 方法 2：手动创建仓库

1. 访问 https://github.com/new
2. 仓库名：`yaoyuancheng.github.io`
3. 设为公开仓库
4. 创建后，在终端执行：

```bash
cd /root/.openclaw/workspace/yaoyuancheng.github.io
git remote add origin https://github.com/yaoyuancheng/yaoyuancheng.github.io.git
git branch -M main
git push -u origin main
```

## 发布成功后

访问：`https://yaoyuancheng.github.io` 即可看到你的主页！

## 后续更新

修改 `index.html` 后，执行：
```bash
cd /root/.openclaw/workspace/yaoyuancheng.github.io
git add .
git commit -m "Update page"
git push
```
