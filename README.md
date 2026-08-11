# Design Inspiration Gallery

🎨 31 种前端 UI 设计风格的灵感画廊，每种风格都有独立、完整的视觉展示页面。

## 预览

在线访问：[https://hihihg-lang.github.io/design-inspiration-gallery/](https://hihihg-lang.github.io/design-inspiration-gallery/)

## 设计风格列表

| # | 风格 | 说明 |
|---|------|------|
| 1 | 极简主义 Minimalism | 留白、克制、功能至上 |
| 2 | 新拟态 Neumorphism | 柔和阴影、凸起/凹陷效果 |
| 3 | 玻璃态 Glassmorphism | 毛玻璃、半透明层次 |
| 4 | 野兽派 Brutalism | 原始、粗暴、直接 |
| 5 | 扁平设计 Flat Design | 简洁、无阴影、纯色块 |
| 6 | 赛博朋克 Cyberpunk | 霓虹灯、暗黑、未来感 |
| 7 | 蒸汽波 Vaporwave | 粉紫渐变、复古合成器波 |
| 8 | 瑞士现代主义 Swiss Modernism | 网格系统、无衬线、清晰 |
| 9 | 孟菲斯 Memphis | 几何图形、大胆配色 |
| 10 | 粘土态 Claymorphism | 3D 柔和、粘土质感 |
| 11 | 暗黑模式 OLED | 纯黑背景、省电、扫描线 |
| 12 | 复古未来主义 Retro-Futurism | 80年代科幻、几何图形 |
| 13 | 电子墨水 E-Ink | 类纸质感、护眼 |
| 14 | 极光 UI Aurora UI | 渐变光晕、北极光效果 |
| 15 | 液体玻璃 Liquid Glass | 动态模糊、流体感 |
| 16 | HUD 科幻 HUD Sci-Fi | 线框、全息投影 |
| 17 | 像素艺术 Pixel Art | 8-bit、复古游戏 |
| 18 | 拟物主义 Skeuomorphism | 真实材质、质感 |
| 19 | 动态驱动 Motion-Driven | 动画优先、活力 |
| 20 | Bento 网格 Bento Grid | 卡片式、模块化 |
| 21 | 零界面 Zero UI | 语音、手势优先 |
| 22 | 英雄中心 Hero-Centric | 大标题、视觉冲击 |
| 23 | 有机仿生 Organic Biomimicry | 自然曲线、流体 |
| 24 | 软 UI Soft UI | 柔和圆角、温暖 |
| 25 | Z世代混乱 Gen-Z Chaos | 拼贴、随机、大胆 |
| 26 | 新粗野主义 Neubrutalism | 硬阴影、粗边框 |
| 27 | AI 原生 AI-Native | 生成式、自适应 |
| 28 | 包容性设计 Inclusive Design | 无障碍、高对比度 |
| 29 | 空间 UI Spatial UI | 3D 深度、视差 |
| 30 | Y2K 复兴 Y2K Revival | 千禧年、金属质感 |
| 31 | 古老魔法书 Ancient Spellbook | 羊皮纸、符文、水晶球 |

## 项目结构

```
├── index.html                  # 首页画廊（中文）
├── styles/                     # 31种风格页面（中文）
│   ├── minimalism.html
│   ├── ancient-spellbook.html
│   └── ...
├── zh/                         # 英文版本
│   ├── index.html
│   └── styles/
├── standalone/                 # 独立版（零外部依赖，可离线使用）
├── build/                      # 安装包构建文件
├── color-mixer.html            # 配色工具
├── palette.html                # 配色库
├── reference.html              # 参考资源
└── philosophy.html             # 设计理念
```

## 技术栈

- 纯 HTML/CSS，无需构建工具
- [Tailwind CSS](https://tailwindcss.com/)（CDN 引入）
- CSS 自定义动画（`@keyframes`、`@property`）
- 部分页面使用 SVG 滤镜实现纹理效果

## 本地运行

```bash
# 任意静态服务器即可
python3 -m http.server 8080
# 访问 http://localhost:8080
```

## 贡献指南

欢迎提交 Pull Request！请查看 [CONTRIBUTING.md](./CONTRIBUTING.md)。

贡献方向：
- 新增设计风格
- 改进现有页面的视觉效果
- 修复 Bug
- 补充文档

## 许可证

MIT License — 详见 [LICENSE](./LICENSE)