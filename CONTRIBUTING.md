# 贡献指南

感谢你愿意为 Design Inspiration Gallery 贡献代码和创意！

## 如何贡献

### 新增设计风格

1. 在 `styles/` 目录下创建新的 HTML 文件
2. 文件名使用英文小写，用连字符分隔，如 `my-style.html`
3. 页面需包含：
   - 共享导航占位符 `<div id="shared-nav" ...>` 和 `<div id="shared-footer" ...>`（参见现有页面）
   - 风格名称、设计理念说明
   - 色彩方案展示
   - 适用场景和技术特点
   - 在 `</body>` 前引入 `<script src="../shared/components.js"></script>`
4. 同步创建 `zh/styles/` 下的英文版本（注意 base-path 为 `../../`）
5. 在 `index.html` 和 `zh/index.html` 中添加风格卡片
6. 在 `shared/update-components.py` 和 `shared/sync-build.py` 的 STYLES 字典中注册新风格

### 改进现有页面

- 视觉效果优化：直接修改对应 HTML 文件即可
- 性能优化：注意保持无外部依赖
- 无障碍改进：确保色彩对比度、语义化 HTML

### 提交流程

1. Fork 本仓库
2. 创建功能分支：`git checkout -b feature/my-feature`
3. 提交更改：`git commit -m '描述你的改动'`
4. 推送到分支：`git push origin feature/my-feature`
5. 提交 Pull Request

### 代码规范

- 使用 4 空格缩进
- CSS 变量统一放在 `:root` 中
- 动画使用 `@keyframes`，避免 JS 动画
- 中英文版本保持结构和样式一致
- 确保在移动端（375px）正常显示

### 语言

- 中文版页面：`styles/` 目录
- 英文版页面：`zh/styles/` 目录
- 两个版本样式代码完全一致，仅文本内容不同