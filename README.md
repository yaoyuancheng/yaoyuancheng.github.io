# yaoyuancheng.github.io

Personal blog and portfolio site for Yuancheng Yao.

## 🚀 Live Site

Visit: [https://yaoyuancheng.github.io](https://yaoyuancheng.github.io)

## 📖 About

This is my personal website built with Jekyll and hosted on GitHub Pages. It serves as:

- A **blog** for sharing thoughts on AI, open source, and technology
- A **portfolio** showcasing my projects and work
- A **personal brand** space to connect with the community

## 🛠️ Tech Stack

- **Static Site Generator:** Jekyll
- **Theme:** Minima (customized)
- **Hosting:** GitHub Pages
- **CSS:** Sass with custom styles
- **Deployment:** Automatic via GitHub Pages

## 📁 Project Structure

```
.
├── _config.yml          # Jekyll configuration
├── _posts/              # Blog posts
├── _layouts/            # Layout templates
├── _includes/           # Reusable components
├── assets/
│   └── css/            # Custom styles
├── index.md            # Home page
├── about.md            # About page
├── blog.md             # Blog index
└── README.md           # This file
```

## 🚦 Local Development

To run the site locally:

1. **Install Ruby and Jekyll:**
   ```bash
   gem install bundler jekyll
   ```

2. **Clone the repository:**
   ```bash
   git clone https://github.com/yaoyuancheng/yaoyuancheng.github.io
   cd yaoyuancheng.github.io
   ```

3. **Install dependencies:**
   ```bash
   bundle install
   ```

4. **Run the development server:**
   ```bash
   bundle exec jekyll serve
   ```

5. **Open in browser:** [http://localhost:4000](http://localhost:4000)

## 📝 Writing Blog Posts

To create a new blog post:

1. Create a new file in `_posts/` with the naming convention:
   ```
   YYYY-MM-DD-title-of-post.md
   ```

2. Add front matter:
   ```yaml
   ---
   layout: post
   title: "Your Post Title"
   date: YYYY-MM-DD
   categories: [category1, category2]
   author: Yuancheng Yao
   ---
   ```

3. Write your content in Markdown

## 🎨 Customization

### Styles
Custom styles are in `assets/css/style.scss`. The site uses:
- **Primary color:** `#2c3e50` (dark blue)
- **Secondary color:** `#3498db` (blue)
- **Accent color:** `#e74c3c` (red)

### Layouts
The site uses Jekyll's default layouts with customizations in:
- `_layouts/default.html` - Base layout
- `_layouts/home.html` - Home page layout
- `_layouts/post.html` - Blog post layout

## 🔧 Deployment

The site is automatically deployed by GitHub Pages when changes are pushed to the `main` branch.

To manually trigger a rebuild:
1. Push changes to GitHub
2. GitHub Pages will automatically rebuild (takes 1-2 minutes)

## 📊 Analytics

Google Analytics can be added by:
1. Getting a tracking ID from Google Analytics
2. Adding it to `_config.yml`:
   ```yaml
   google_analytics: UA-XXXXXXXXX-X
   ```

## 🤝 Contributing

While this is a personal site, suggestions and improvements are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

Content is licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

Code is licensed under [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with [Jekyll](https://jekyllrb.com/)
- Hosted by [GitHub Pages](https://pages.github.com/)
- Theme based on [Minima](https://github.com/jekyll/minima)
- Icons from [Font Awesome](https://fontawesome.com/)

---

*Last updated: April 2026*