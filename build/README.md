# Design Inspiration Gallery — 安装指南

30 种 UI 设计风格灵感画廊 | 支持 Windows / Android / iOS

**所有版本均为离线可用，无需网络连接。**

---

## Windows 安装

### 自动安装程序（推荐）
1. 解压 ZIP 文件
2. 右键 `setup.ps1` →「使用 PowerShell 运行」
3. 弹出窗口中选择安装目录
4. 自动复制文件 + 创建桌面/开始菜单快捷方式
5. 双击桌面「Design Inspiration Gallery」使用

> 如提示安全策略，先运行：`Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass`
> 或双击 `setup.bat` 通过批处理安装

### 便携版（免安装）
直接打开 `app/index.html` 在浏览器中使用，无需安装

### 卸载
运行安装目录下的 `uninstall.bat`，或直接删除安装目录

---

## Android 安装

### 方式一：编译 APK（完全离线）
1. 用 Android Studio 打开 `android/` 文件夹
2. 等待 Gradle 同步完成
3. Build → Build Bundle(s) / APK(s) → Build APK(s)
4. APK 文件在 `app/build/outputs/apk/debug/`
5. 传输到手机安装 → 打开即可使用，完全离线

### 方式二：文件管理器直接打开
1. 将 `app/` 文件夹复制到手机存储
2. 用文件管理器打开 `app/index.html`
3. 选择 Chrome 浏览器打开

---

## iOS 安装

### 添加到主屏幕
1. 将 `app/` 文件夹通过 AirDrop/文件传到 iPhone
2. 用 Safari 打开「文件」App 中的 `index.html`
3. 点击底部「分享」→「添加到主屏幕」

---

## 文件说明
```
app/              # 网站源文件（HTML/CSS/JS/图标，离线可用）
setup.ps1         # Windows PowerShell 安装程序（可选安装位置）
setup.bat         # Windows 批处理安装程序
android/          # Android Studio 项目（编译离线 APK）
README.md         # 本文件
```