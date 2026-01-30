# 🚀 Bingo Downloader 发布指南

## 📊 项目状态总结

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 代码质量 | ✅ 完成 | TypeScript + Python 双实现 |
| 隐私检查 | ✅ 通过 | 无敏感信息 |
| .gitignore | ✅ 完善 | 已更新 |
| 文档 | ✅ 完成 | README + SKILL.md + MkDocs |
| MCP Server | ✅ 完成 | 6 个工具已实现 |
| Skills | ✅ 完成 | 支持所有主流 AI IDE |

---

## 🎯 推荐配置

### 1. 仓库名称

**推荐：`bingo-downloader`**

```bash
git remote add origin https://github.com/jiangbingo/bingo-downloader.git
```

### 2. 默认分支

**推荐：`main`**（行业标准）

```bash
git branch -M main
git push -u origin main
```

**为什么选择 `main` 而不是 `master`？**
- GitHub/GitLab 默认分支（2020年起）
- 促进包容性语言
- 现代化标准
- 更广泛的社区接受度

---

## 🧪 测试流程

### 阶段 1：本地测试 MCP Server

```bash
cd /Users/jiangbin/Documents/bingo-downloader-skill/bingo-downloader

# 1. 安装依赖
cd mcp && npm install && cd ..

# 2. 构建
make build

# 3. 运行测试脚本
node test-mcp.js
```

### 阶段 2：AI IDE 集成测试

#### Cursor IDE 测试

1. **配置 MCP Server**：
   ```json
   // ~/.cursor/mcp.json 或 Cursor 设置
   {
     "mcpServers": {
       "bingo-downloader": {
         "command": "node",
         "args": ["/Users/jiangbin/Documents/bingo-downloader-skill/bingo-downloader/mcp/dist/index.js"]
       }
     }
   }
   ```

2. **安装 Skills**：
   ```bash
   make install-skill
   ```

3. **测试对话**：
   - "下载这个视频 https://www.youtube.com/watch?v=dQw4w9WgXcQ"
   - "提取音频"
   - "查看下载历史"

#### Claude Code 测试

1. **配置 MCP Server**：
   ```json
   // ~/Library/Application Support/Claude/claude_desktop_config.json
   {
     "mcpServers": {
       "bingo-downloader": {
         "command": "node",
         "args": ["/path/to/bingo-downloader/mcp/dist/index.js"]
       }
     }
   }
   ```

2. **测试相同对话**

### 阶段 3：功能测试清单

- [ ] 下载 YouTube 视频（需要 cookies）
- [ ] 下载 Bilibili 视频
- [ ] 提取音频（MP3）
- [ ] 下载带字幕的视频
- [ ] 列出可用格式
- [ ] 查看下载历史
- [ ] 查看统计信息
- [ ] 错误处理（403, 无效 URL）
- [ ] 智能重试机制

---

## 📝 Git 提交最佳实践

### 1. 首次提交

```bash
git init
git branch -M main
git add .
git commit -m "Initial commit: Bingo Downloader v1.0.0

🎬 MCP Server + Skills dual-mode architecture

Features:
- MCP Server with 6 tools (download, audio, subs, formats, history, stats)
- Skills for AI IDEs (Cursor, Claude Code, Windsurf, etc.)
- Support 1000+ video sites (YouTube, Bilibili, Twitter, TikTok)
- Audio extraction, subtitles, quality selection
- Download history and statistics
- Smart retry with exponential backoff

Tech Stack:
- TypeScript + MCP SDK
- Python + yt-dlp
- MkDocs documentation"
```

### 2. 提交信息规范

使用 Conventional Commits：

```bash
# 功能添加
git commit -m "feat: add thumbnail extraction support"

# Bug 修复
git commit -m "fix: resolve YouTube 403 error with cookies"

# 文档更新
git commit -m "docs: update MCP installation guide"

# 性能优化
git commit -m "perf: improve download speed with parallel processing"

# 测试
git commit -m "test: add integration tests for MCP tools"
```

### 3. 分支策略

```bash
# 主分支
main           # 生产版本

# 开发分支
develop        # 开发版本

# 功能分支
feature/xxx    # 新功能
bugfix/xxx     # Bug 修复
hotfix/xxx     # 紧急修复
docs/xxx       # 文档更新
```

---

## 🌟 GitHub 仓库优化

### 1. Repository Settings

| 设置项 | 值 | 说明 |
|--------|-----|------|
| Repository name | `bingo-downloader` | 简洁明了 |
| Description | `MCP Server + Skills for AI IDEs - Download videos from 1000+ sites` | 简短描述 |
| Visibility | Public | 开源项目 |
| Topics | 见下方 | 帮助发现 |
| License | MIT | 开源协议 |
| Default branch | `main` | 推荐 |
| Issues | Enabled | 允许反馈 |
| Projects | Disabled | 或根据需要 |
| Wikis | Optional | 已有 MkDocs |

### 2. Topics（添加到仓库）

```
mcp
model-context-protocol
video-downloader
yt-dlp
youtube
bilibili
tiktok
ai-ide
cursor-ide
claude-code
windsurf
typescript
python
skills
automation
developer-tools
```

### 3. README 优化

确保 README.md 包含：
- ✅ 项目徽章（License、MCP、Node、Docs）
- ✅ 快速开始指南
- ✅ 功能列表
- ✅ 安装说明
- ✅ 使用示例
- ✅ 支持的平台
- ✅ 文档链接
- ✅ 贡献指南

### 4. 创建 Release

```bash
# 创建标签
git tag -a v1.0.0 -m "Release v1.0.0

🎬 Initial release of Bingo Downloader

Features:
- MCP Server with 6 tools
- Skills for AI IDEs
- Support 1000+ sites
- Download history & stats"

# 推送标签
git push origin v1.0.0
```

在 GitHub 创建 Release 时添加：

**Title:**
```
🎬 v1.0.0 - Initial Release
```

**Description:**
```markdown
## 🎉 First Release of Bingo Downloader!

Dual-mode architecture with MCP Server and AI IDE Skills.

### ✨ Features

- 🤖 **MCP Server**: Direct tool integration
- 💬 **Skills**: Natural language interface
- 🌐 **1000+ Sites**: YouTube, Bilibili, Twitter, TikTok
- 🎵 **Audio Extraction**: MP3, WAV, M4A support
- 📝 **Subtitles**: Multi-language support
- 📊 **History & Stats**: Track your downloads

### 🚀 Quick Start

```bash
git clone https://github.com/jiangbingo/bingo-downloader.git
cd bingo-downloader
make install
```

### 📚 Documentation

[Full Documentation](https://jiangbingo.github.io/bingo-downloader/)

### 🙏 Credits

Built with [yt-dlp](https://github.com/yt-dlp/yt-dlp) and [Model Context Protocol](https://modelcontextprotocol.io/)
```

---

## 🔐 安全检查清单

发布前确认：

- [ ] 无 API 密钥或密码
- [ ] 无个人邮箱或电话
- [ ] 无内部 URL 或 IP 地址
- [ ] 无临时文件或调试代码
- [ ] .gitignore 配置正确
- [ ] License 文件已添加
- [ ] README 无敏感信息
- [ ] 依赖项已更新到安全版本

---

## 📢 发布后推广

### 中文社区

- **V2EX**: https://www.v2ex.com/go/python
  - 标题：[开源] Bingo Downloader - AI IDE 视频下载工具

- **掘金**:
  - 发布技术文章介绍 MCP + Skills 架构

- **知乎**:
  - AI 工具分享

### 国际社区

- **Reddit**:
  - r/Python
  - r/curiveditor
  - r/LocalLLaMA

- **Hacker News**:
  - Show HN: Bingo Downloader

- **Product Hunt**:
  - 产品发布

### 相关项目

在以下地方留言：
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) Issues
- Cursor Discord
- Claude Code Discord

---

## 📈 成功指标

首月目标：
- [ ] 20+ Stars
- [ ] 5+ Forks
- [ ] 10+ Issues/Discussions
- [ ] 正面反馈
- [ ] 稳定运行

---

## 🎓 学习资源

- [MCP 官方文档](https://modelcontextprotocol.io/)
- [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)
- [Cursor 文档](https://cursor.sh/docs)
- [MkDocs 文档](https://www.mkdocs.org/)

---

## 📞 支持

- GitHub Issues: https://github.com/jiangbingo/bingo-downloader/issues
- Discussions: https://github.com/jiangbingo/bingo-downloader/discussions

---

**祝发布成功！🎉**
