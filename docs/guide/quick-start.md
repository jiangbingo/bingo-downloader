# 快速开始

本指南将帮助你在 5 分钟内快速上手 Bingo Downloader。

## 前置要求

在开始之前，请确保你的系统已安装以下依赖：

```bash
# 检查 Node.js（需要 18+）
node --version

# 检查 Python（需要 3.8+）
python --version

# 检查 yt-dlp
yt-dlp --version

# 检查 ffmpeg
ffmpeg -version
```

如果缺少依赖，请查看[依赖安装指南](../installation/dependencies.md)。

## 安装

### 步骤 1：克隆仓库

```bash
git clone https://github.com/jiangbingo/bingo-downloader.git
cd bingo-downloader
```

### 步骤 2：安装

```bash
# 安装 MCP Server 和 Skills（推荐）
make install

# 或单独安装
make install-mcp      # 仅 MCP Server
make install-skill    # 仅 Skills
```

### 步骤 3：配置 MCP Server（可选）

如果你想在 AI IDE 中使用 MCP 工具，需要配置 `claude_desktop_config.json`：

**macOS/Linux:**
```bash
# 打开配置文件
open ~/.claude/claude_desktop_config.json
# 或编辑
code ~/.claude/claude_desktop_config.json
```

**Windows:**
```bash
# 配置文件位置
%APPDATA%\Claude\claude_desktop_config.json
```

添加以下配置：

```json
{
  "mcpServers": {
    "bingo-downloader": {
      "command": "node",
      "args": ["$(pwd)/mcp/dist/index.js"]
    }
  }
}
```

**注意**：将 `$(pwd)` 替换为实际的完整路径，例如 `/Users/jiangbin/Documents/bingo-downloader/mcp/dist/index.js`。

## 快速使用

### 使用 Skills（推荐新手）

Skills 提供自然语言接口，只需描述你想要什么：

```
你: "下载这个 YouTube 视频 https://www.youtube.com/watch?v=dQw4w9WgXcQ"

Claude: [自动调用 MCP 工具]

✓ Download completed!

File: ~/Downloads/yt-dlp/Rick Astley - Never Gonna Give You Up.mp4
Size: 50.00MiB
Platform: YouTube
```

更多示例：
- "提取这个 Bilibili 视频的音频"
- "下载这个 Twitter 视频带字幕"
- "用 720p 下载这个视频"

### 使用 MCP 工具

如果你想直接使用 MCP 工具，可以在 AI IDE 中调用：

```bash
# 下载视频
download_video(url="https://youtube.com/...", quality="1080")

# 提取音频
extract_audio(url="https://youtube.com/...", format="mp3")

# 下载带字幕
download_with_subs(url="https://youtube.com/...", sub_langs="en,zh")

# 列出格式
list_formats(url="https://youtube.com/...")

# 查看历史
get_history(limit=10)

# 查看统计
get_stats()
```

## 下一步

- 📖 [完整使用指南](index.md)
- 🔧 [配置选项](../configuration/)
- 📚 [API 参考](../api/)
- 💡 [示例](../examples/)

## 常见问题

### Q: MCP Server 无法启动？

**A**: 检查以下几点：
1. Node.js 版本 >= 18.0.0
2. 已运行 `make build` 构建 MCP Server
3. 配置文件中的路径是绝对路径

### Q: 下载失败，显示 403 错误？

**A**: 这是 YouTube 的反爬虫机制。使用浏览器 cookies：

```
你: "使用 Chrome cookies 下载这个视频"

Claude: [自动设置 cookies_browser="chrome"]
```

或在调用工具时指定：
```bash
download_video(url="...", cookies_browser="chrome")
```

### Q: 音频提取失败？

**A**: 检查 ffmpeg 是否安装：

```bash
ffmpeg -version

# 如果未安装
brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Linux
```

### Q: Skills 没有生效？

**A**: 确保：
1. 已运行 `make install-skill`
2. SKILL.md 文件在正确位置：`~/.cursor/skills/bingo-downloader/SKILL.md`
3. 重启 AI IDE

## 需要帮助？

- 📚 [完整文档](https://jiangbingo.github.io/bingo-downloader/)
- 🐛 [报告问题](https://github.com/jiangbingo/bingo-downloader/issues)
- 💬 [讨论区](https://github.com/jiangbingo/bingo-downloader/discussions)