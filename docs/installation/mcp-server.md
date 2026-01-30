# MCP Server 安装指南

MCP Server 提供标准化的工具接口，可以与所有支持 MCP 协议的 AI IDE 集成。

## 安装步骤

### 方法 1：使用 Makefile（推荐）

```bash
# 进入项目目录
cd bingo-downloader

# 安装 MCP Server
make install-mcp
```

这会自动：
1. 安装 npm 依赖
2. 编译 TypeScript 代码
3. 生成可执行的 JavaScript 文件

### 方法 2：手动安装

```bash
# 进入 MCP 目录
cd mcp

# 安装依赖
npm install

# 构建
npm run build
```

## 配置 MCP Server

### 在 Claude Desktop 中配置

1. **打开配置文件**

**macOS/Linux**:
```bash
open ~/.claude/claude_desktop_config.json
# 或使用编辑器
code ~/.claude/claude_desktop_config.json
```

**Windows**:
```powershell
notepad %APPDATA%\Claude\claude_desktop_config.json
```

2. **添加 Bingo Downloader 配置**

```json
{
  "mcpServers": {
    "bingo-downloader": {
      "command": "node",
      "args": ["/absolute/path/to/bingo-downloader/mcp/dist/index.js"],
      "env": {
        "PATH": "/usr/local/bin:/usr/bin:/bin"
      }
    }
  }
}
```

**重要**：
- 将 `/absolute/path/to/bingo-downloader/mcp/dist/index.js` 替换为你的实际路径
- Windows 示例：`C:\\Users\\YourName\\Documents\\bingo-downloader\\mcp\\dist\\index.js`

3. **保存并重启 Claude Desktop**

### 在其他 AI IDE 中配置

**Cursor**:
```bash
# MCP Server 会自动被检测
# 确保文件在正确位置即可
```

**Windsurf**:
- 在设置中添加 MCP Server
- 路径：`/path/to/bingo-downloader/mcp/dist/index.js`

**其他 IDE**:
查阅 IDE 的 MCP 配置文档，通常在设置 → MCP 或插件配置中。

## 验证安装

### 测试 MCP Server

1. **启动 Claude Desktop**
2. **打开新对话**
3. **测试工具**：

```
你: 列出这个视频的格式 https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

如果看到格式列表，说明 MCP Server 工作正常！

### 检查日志

如果遇到问题，查看 Claude Desktop 日志：

**macOS/Linux**:
```bash
# 日志位置
~/Library/Application Support/Claude/claude-desktop.log
# 或
~/.config/Claude/claude-desktop.log
```

**Windows**:
```powershell
%APPDATA%\Claude\claude-desktop.log
```

## 开发模式

如果你想修改 MCP Server 代码：

```bash
# 开发模式（自动重新编译）
cd mcp
npm run dev
```

然后在配置文件中使用源文件路径：
```json
{
  "mcpServers": {
    "bingo-downloader": {
      "command": "npx",
      "args": ["tsx", "/path/to/bingo-downloader/mcp/src/index.ts"]
    }
  }
}
```

## 全局安装

如果你想在任何地方使用 MCP Server：

```bash
# 全局安装
cd mcp
npm install -g .

# 然后在配置中使用
{
  "mcpServers": {
    "bingo-downloader": {
      "command": "bingo-downloader-mcp"
    }
  }
}
```

## 可用的 MCP 工具

安装后，以下工具将可用：

| 工具名 | 描述 | 参数 |
|--------|------|------|
| `download_video` | 下载视频 | url, quality, cookies_browser, download_path |
| `extract_audio` | 提取音频 | url, format, quality, cookies_browser |
| `download_with_subs` | 下载带字幕的视频 | url, quality, sub_langs, cookies_browser |
| `list_formats` | 列出可用格式 | url, cookies_browser |
| `get_history` | 查看下载历史 | limit, platform |
| `get_stats` | 查看统计信息 | platform |

详细参数说明，请查看 [API 参考](../api/index.md)。

## 故障排除

### 问题：MCP Server 无法启动

**可能原因**：
1. Node.js 版本太低（需要 18+）
2. 编译失败
3. 路径不正确

**解决方案**：
```bash
# 检查 Node.js 版本
node --version

# 重新构建
cd mcp
npm install
npm run build

# 检查编译产物
ls -la dist/
```

### 问题：工具调用失败

**可能原因**：
1. yt-dlp 未安装
2. ffmpeg 未安装（音频提取）
3. 权限问题

**解决方案**：
```bash
# 检查依赖
which yt-dlp
which ffmpeg

# 测试 yt-dlp
yt-dlp --version

# 测试下载
yt-dlp https://www.youtube.com/watch?v=dQw4w9WgXcQ -f best
```

### 问题：找不到配置文件

**解决方案**：
```bash
# macOS/Linux
ls -la ~/.claude/

# Windows
dir %APPDATA%\Claude

# 手动创建目录
mkdir -p ~/.claude
touch ~/.claude/claude_desktop_config.json
```

## 卸载

```bash
# 从配置文件中移除配置
# 编辑 ~/.claude/claude_desktop_config.json
# 删除 "bingo-downloader" 条目

# 可选：删除源代码
cd ..
rm -rf bingo-downloader
```

## 下一步

- [快速开始](../guide/quick-start.md)
- [API 参考](../api/index.md)
- [使用指南](../usage/index.md)