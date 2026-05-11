/* ===== 应用主逻辑 ===== */

const app = {
  currentDay: 1,
  totalSections: 0,

  init() {
    this.calculateDay();
    this.renderLesson();
    this.setupNavigation();
  },

  calculateDay() {
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    const start = new Date(START_DATE);
    start.setHours(0, 0, 0, 0);
    const diffDays = Math.floor((today - start) / (1000 * 60 * 60 * 24));
    this.currentDay = Math.max(1, diffDays + 1);
  },

  getLesson(day) {
    // If lesson exists in our data, use it
    if (lessons[day]) return lessons[day];

    // Otherwise generate a placeholder for future days
    return {
      title: `第 ${day} 天的课程准备中...`,
      icon: '🌅',
      subtitle: '每日早7点自动更新，敬请期待',
      sections: [
        {
          icon: '⏰',
          title: '每日更新',
          type: 'tip',
          tipType: 'gold',
          label: '提醒',
          content: [
            '新一天的课程内容将在早上7点自动更新。',
            '坚持每天学习，21天养成高效表达的习惯！',
            '你可以回顾之前学过的课程内容。'
          ]
        }
      ]
    };
  },

  renderLesson() {
    const lesson = this.getLesson(this.currentDay);

    // Update hero
    document.getElementById('heroIcon').textContent = lesson.icon;
    document.getElementById('lessonTitle').textContent = lesson.title;

    const date = new Date(START_DATE);
    date.setDate(date.getDate() + this.currentDay - 1);
    const dateStr = `${date.getFullYear()}年${date.getMonth() + 1}月${date.getDate()}日`;
    document.getElementById('lessonDate').textContent = `第 ${this.currentDay} 天 · ${dateStr}`;
    document.getElementById('lessonSubtitle').textContent = lesson.subtitle;

    // Update day badge
    document.getElementById('dayCounter').textContent = `第 ${this.currentDay} 天`;

    // Render sections
    const container = document.getElementById('contentSections');
    container.innerHTML = '';

    this.totalSections = lesson.sections.length;

    lesson.sections.forEach((section, index) => {
      const sectionEl = document.createElement('div');
      sectionEl.className = 'section';
      sectionEl.id = `section-${index}`;

      let bodyHtml = '';

      switch (section.type) {
        case 'text':
          bodyHtml = section.content.map(p => `<p>${p}</p>`).join('');
          break;

        case 'tip':
          bodyHtml = `
            <div class="tip-box ${section.tipType ? section.tipType : ''}">
              ${section.label ? `<div class="tip-label">${section.label}</div>` : ''}
              ${section.content.map(p => `<p>${p}</p>`).join('')}
            </div>
          `;
          break;

        case 'comparison':
          bodyHtml = `<div class="comparison">${section.rows.map(row => `
            <div class="comp-row">
              <div class="comp-before">${row.before}</div>
              <div class="comp-after">${row.after}</div>
            </div>
          `).join('')}</div>`;
          break;

        case 'case':
          bodyHtml = section.cases.map(c => `
            <div class="case-card ${c.type}">
              <div class="case-label">${c.label}</div>
              <div class="case-content"><p>${c.text}</p></div>
            </div>
          `).join('');
          break;

        case 'practice':
          bodyHtml = `
            <div class="practice-box">
              <div class="tip-label">✏️ 动手练习</div>
              ${section.content.map(p => `<p>${p}</p>`).join('')}
            </div>
          `;
          break;

        case 'quote':
          bodyHtml = `
            <div class="quote-block">
              <p class="quote-text">${section.quote}</p>
              <p class="quote-author">${section.author}</p>
            </div>
          `;
          break;

        default:
          bodyHtml = '';
      }

      sectionEl.innerHTML = `
        <div class="section-header">
          <div class="section-icon">${section.icon}</div>
          <div class="section-title">${section.title}</div>
        </div>
        <div class="section-body">${bodyHtml}</div>
      `;

      container.appendChild(sectionEl);

      // Staggered entrance animation
      setTimeout(() => {
        sectionEl.classList.add('visible');
        this.updateProgress(index + 1);
      }, 100 + index * 200);
    });

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
  },

  updateProgress(sectionsDone) {
    const pct = Math.min(100, Math.round((sectionsDone / this.totalSections) * 100));
    document.getElementById('progressText').textContent = `${pct}%`;
    document.getElementById('progressFill').style.width = `${pct}%`;
  },

  setupNavigation() {
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    prevBtn.addEventListener('click', () => {
      if (this.currentDay > 1) {
        this.currentDay--;
        this.renderLesson();
      }
    });

    nextBtn.addEventListener('click', () => {
      this.currentDay++;
      this.renderLesson();
    });

    // Update button states after render
    const observer = new MutationObserver(() => {
      prevBtn.disabled = this.currentDay <= 1;
      // Check if next day has no content (future)
      const nextLesson = this.getLesson(this.currentDay + 1);
      const hasNext = nextLesson && nextLesson.title && !nextLesson.title.includes('准备中');
      // Allow navigation either way, just show what's there
    });

    observer.observe(document.getElementById('lessonTitle'), { childList: true, subtree: true });
  }
};

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => app.init());
