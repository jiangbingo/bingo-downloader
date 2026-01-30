# 🚀 GitHub 发布指南

## 📋 发布前检查清单

### ✅ 已完成的项目

- [x] **LICENSE** - MIT License
- [x] **CHANGELOG.md** - 完整的版本历史记录
- [x] **CONTRIBUTING.md** - 贡献指南
- [x] **SECURITY.md** - 安全策略
- [x] **.gitignore** - 完善的忽略规则
- [x] **GitHub Issue 模板** - Bug 报告、功能请求、文档问题
- [x] **PR 模板** - Pull Request 模板
- [x] **README.md / README_CN.md** - 中英文文档
- [x] **SKILL.md** - AI 助手技能定义

### 🔍 发布前验证

```bash
# 1. 语法检查
python3 -m py_compile scripts/download.py
bash -n scripts/download.sh

# 2. 测试安装（在另一个目录）
cd /tmp && git clone <your-repo-url> test-skill && cd test-skill
make install-all

# 3. 功能测试
make download URL="https://www.youtube.com/watch?v=dQw4w9WgXcQ" Q=720
make smart-download URL="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
make history
make stats
make presets
```

---

## 📦 GitHub 仓库设置

### 1. Repository Settings

**建议设置：**

| 设置项 | 值 | 说明 |
|--------|-----|------|
| Repository name | `bingo-downloader-skill` | 简洁明了 |
| Description | AI-powered video downloader skill for AI IDEs | GitHub 关于部分 |
| Visibility | Public | 开源项目 |
| Topics | `video-downloader`, `yt-dlp`, `ai-ide`, `cursor`, `claude-code`, `bilibili`, `youtube`, `tiktok` | 帮助发现 |
| License | MIT License | 选择 LICENSE 文件 |
| Branch protection | Enable on `main` branch | 要求 PR review |
| Issues | Enabled | 允许报告问题 |
| Projects | Disabled | 或根据需要 |
| Wikis | Optional | 文档已在 README |
| Discussions | Enabled | 社区交流 |

### 2. Topics 标签（重要！）

在 GitHub 仓库页面添加以下 Topics：

```
video-downloader
yt-dlp
ai-ide
cursor-ide
claude-code
windsurf
bilibili
youtube
tiktok
douyin
video-download
smart-download
batch-download
playlist-downloader
python
bash
makefile
automation
productivity
developer-tools
cli
terminal
```

### 3. Repository Description

**Short Description (≤150 chars):**
```
AI-powered video downloader skill for AI IDEs - Download from 1000+ sites including YouTube, Bilibili, TikTok with smart format selection, auto-retry, playlist support.
```

**About Section:**
```
🎬 Bingo Downloader Skill - The ultimate video downloader for AI-powered IDEs.

Features:
🤖 AI-Powered Smart Format Selection
🔄 Smart Retry with Exponential Backoff
📋 Playlist Auto-Detection
🖼️ Thumbnail Extraction
📊 Download History & Statistics
⚙️ Configuration Presets
📦 Batch Download

Supports 1000+ sites: YouTube, Bilibili, Twitter, TikTok, Douyin, and more!

Works with: Cursor, Claude Code, Windsurf, Gemini, Trae, OpenAI CodeSandbox
```

---

## 🏷️ Git Tags 和 Releases

### 1. 创建标签

```bash
# 创建 v2.0.0 标签
git tag -a v2.0.0 -m "Release v2.0.0 - Smart Features Release

🚀 Major Release with 7 AI-Powered Features:
- AI-Powered Smart Format Selection
- Smart Retry with Exponential Backoff
- Batch Download with Progress Tracking
- Playlist Auto-Detection
- Thumbnail Extraction
- Download History & Statistics
- Configuration Presets

Supported on: Cursor, Claude Code, Windsurf, Gemini, Trae"

# 推送标签到远程
git push origin v2.0.0
```

### 2. GitHub Release

在 GitHub 创建 Release 时使用以下内容：

**Title:**
```
🚀 v2.0.0 - Smart Features Release
```

**Description:**
```markdown
## 🎉 Major Release - AI-Powered Smart Features

We're excited to announce version 2.0.0 of Bingo Downloader Skill! This release introduces **7 major smart features** powered by AI and automation.

### ✨ What's New

#### 🤖 1. AI-Powered Smart Format Selection
Automatically selects the best video format based on:
- User preference history
- Network conditions
- File size optimization
- Codec compatibility (H.264/H.265 priority)
- Frame rate preference (60fps > 30fps)
- HDR detection

```bash
make smart-download URL="VIDEO_URL"
```

#### 🔄 2. Smart Retry with Exponential Backoff
Network failures automatically retry with:
- Up to 3 attempts
- Exponential backoff: 5s → 10s → 20s
- Clear progress indication

#### 📦 3. Batch Download
Download multiple videos from a text file:
```bash
make batch-download FILE=url_list.txt
```

#### 📋 4. Playlist Auto-Detection
Automatic playlist detection with interactive options:
```bash
make playlist URL="PLAYLIST_URL"
```

#### 🖼️ 5. Thumbnail Extraction
Download video thumbnails automatically:
```bash
make thumbnail URL="VIDEO_URL"
```

#### 📊 6. Download History & Statistics
Track your downloads with SQLite database:
```bash
make history  # View last 20 downloads
make stats    # View statistics
```

#### ⚙️ 7. Configuration Presets
One-click setups for common scenarios:
```bash
make presets  # List all presets
make download URL="VIDEO_URL" PRESET=high-quality
```

### 🌐 Platform Support

✅ Cursor IDE
✅ Claude Code
✅ Windsurf IDE
✅ Gemini Code
✅ Trae IDE
✅ OpenAI CodeSandbox

### 📚 Documentation

- [Full Documentation](https://github.com/jiangbingo/bingo-downloader-skill/blob/main/README.md)
- [中文文档](https://github.com/jiangbingo/bingo-downloader-skill/blob/main/README_CN.md)
- [Contributing Guide](https://github.com/jiangbingo/bingo-downloader-skill/blob/main/CONTRIBUTING.md)
- [Changelog](https://github.com/jiangbingo/bingo-downloader-skill/blob/main/CHANGELOG.md)

### 🚀 Quick Start

```bash
# Clone and install
git clone https://github.com/jiangbingo/bingo-downloader-skill.git
cd bingo-downloader-skill
make install-all

# Download a video
make download URL="https://www.youtube.com/watch?v=xxx"
```

### 🐛 Bug Fixes

- Fixed cookie handling for YouTube downloads
- Improved error messages and suggestions
- Enhanced playlist download reliability

### 📖 Full Changelog

[View all changes](https://github.com/jiangbingo/bingo-downloader-skill/blob/main/CHANGELOG.md#200---2025-01-30)

### 🙏 Acknowledgments

Thanks to all contributors and the yt-dlp team for making this project possible!

---

**[Download v2.0.0](https://github.com/jiangbingo/bingo-downloader-skill/archive/refs/tags/v2.0.0.zip)**
```

---

## 📢 发布推广

### 1. 发布到相关社区

**中文社区:**
- [ ] V2EX: https://www.v2ex.com/go/python
- [ ] 掘金: 发布技术文章
- [ ] 知乎: AI 工具分享
- [ ] Bilibili: 视频教程
- [ ] GitHub 中文社区

**国际社区:**
- [ ] Reddit: r/Python, r/curiveditor, r/LocalLLaMA
- [ ] Hacker News: Show HN
- [ ] Product Hunt
- [ ] Twitter/X

### 2. 相关项目留言

在以下项目留言介绍：
- yt-dlp (GitHub Issues/Discussions)
- Cursor (Discord)
- Claude Code (Discord)

### 3. 社交媒体模板

**Twitter/X:**
```
🎬 Just released v2.0.0 of my Bingo Downloader Skill!

AI-powered video downloader that works with Cursor, Claude Code, and more AI IDEs. Supports 1000+ sites including YouTube, Bilibili, TikTok.

✨ Smart features:
- AI format selection
- Auto-retry
- Playlist detection
- Download history

https://github.com/jiangbingo/bingo-downloader-skill

#AI #VideoDownloader #OpenSource #Cursor #ClaudeCode
```

**V2EX/掘金/知乎:**
```
【开源】Bingo Downloader Skill v2.0.0 发布 - 为 AI IDE 打造的智能视频下载工具

分享一个我开发的视频下载技能工具，专为 AI IDE（Cursor、Claude Code 等）设计。

主要特性：
✅ 支持 1000+ 网站（YouTube、B站、抖音等）
✅ AI 智能格式选择
✅ 自动重试机制
✅ 播放列表自动检测
✅ 下载历史统计

GitHub: https://github.com/jiangbingo/bingo-downloader-skill

欢迎 Star 和反馈！
```

---

## 🔧 Git 操作命令

### 首次推送

```bash
# 1. 添加远程仓库（如果还没有）
git remote add origin https://github.com/jiangbingo/bingo-downloader-skill.git

# 2. 推送所有代码和标签
git push -u origin master --tags

# 3. 设置默认分支为 main（可选）
git branch -M main
git push -u origin main
```

### 后续维护

```bash
# 创建新版本
git tag -a v2.0.1 -m "Release v2.0.1 - Bug fixes"
git push origin v2.0.1

# 创建发布分支
git checkout -b release/v2.0.1
```

---

## 📊 发布后监控

### 1. 查看数据

在 GitHub Insights 查看：
- Traffic（流量来源）
- Clones（克隆次数）
- Stars/Forks 增长
- Issues 和 PR 活动

### 2. 回应反馈

- 及时回复 Issues
- 感谢 Stars
- 合并 PR
- 发布新版本

### 3. 持续改进

根据用户反馈：
- 收集功能请求
- 修复 Bug
- 优化性能
- 更新文档

---

## 🎯 成功指标

发布成功的标志：
- [ ] 获得 10+ Stars（首周）
- [ ] 收到有价值的 Issues
- [ ] 有用户 Fork 并贡献
- [ ] 在社区被讨论/分享
- [ ] 稳定运行无重大 Bug

---

## 📝 常见问题

### Q: 是否应该设置 Sponsor 按钮？
A: 是的，在 GitHub 仓库设置中启用 Sponsor 按钮，可以链接到:
- GitHub Sponsors
- PayPal
- 微信/支付宝二维码

### Q: 是否需要 Code Owners？
A: 建议创建 `.github/CODEOWNERS` 文件：
```
# All changes
* @jiangbingo

# Documentation only
*.md @jiangbingo
```

### Q: 是否需要 CI/CD？
A: 可以添加基本的 GitHub Actions：
- 语法检查
- 测试运行
- 自动发布

---

## 🎉 预祝发布成功！

如有任何问题，欢迎随时联系。
