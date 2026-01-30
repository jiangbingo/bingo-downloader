# 故障排除

本页面提供常见问题的解决方案。

## 安装问题

### 问题：MCP Server 无法启动

**症状**：
```
Error: Cannot find module './dist/index.js'
```

**解决方案**：
```bash
# 进入 MCP 目录
cd bingo-downloader/mcp

# 安装依赖
npm install

# 构建
npm run build

# 验证构建产物
ls -la dist/
```

### 问题：Node.js 版本太低

**症状**：
```
Error: Node.js version is too old. Please use Node.js 18 or higher.
```

**解决方案**：
```bash
# 使用 nvm 安装 Node.js 20
nvm install 20
nvm use 20

# 验证版本
node --version
```

### 问题：Skills 没有生效

**症状**：
AI IDE 无法识别 Skills

**解决方案**：
```bash
# 确认 SKILL.md 在正确位置
ls -la ~/.cursor/skills/bingo-downloader/SKILL.md

# 如果不存在，重新安装
cd bingo-downloader
make install-skill

# 重启 AI IDE
```

## 下载问题

### 问题：YouTube 403 错误

**症状**：
```
✗ Download failed: HTTP Error 403: Forbidden
```

**原因**：YouTube 的反爬虫机制

**解决方案**：
```
使用浏览器 cookies 下载：
你: 用 Chrome cookies 下载 [URL]
```

或手动指定：
```bash
download_video(
  url="https://www.youtube.com/watch?v=xxx",
  cookies_browser="chrome"
)
```

### 问题：音频提取失败

**症状**：
```
✗ Audio extraction failed: ffmpeg not found
```

**原因**：ffmpeg 未安装

**解决方案**：
```bash
# macOS
brew install ffmpeg

# Linux (Ubuntu/Debian)
sudo apt update
sudo apt install ffmpeg

# 验证安装
ffmpeg -version
```

### 问题：下载速度慢

**症状**：下载速度非常慢

**解决方案**：

1. **使用 aria2 加速**：
```bash
# 安装 aria2
brew install aria2  # macOS
sudo apt install aria2  # Linux

# 配置 yt-dlp
echo '--external-downloader aria2c' >> ~/.yt-dlp.conf
echo '--external-downloader-args "-x 16 -k 1M"' >> ~/.yt-dlp.conf
```

2. **使用 cookies**：
```
用 Chrome cookies 下载 [URL]
```

3. **降低质量**：
```
用 720p 下载 [URL]
```

### 问题：下载中断

**症状**：下载到一半停止

**解决方案**：

1. **检查网络连接**
2. **使用 cookies**：避免被限速
3. **降低质量**：减少文件大小
4. **检查磁盘空间**：
```bash
df -h
```

### 问题：文件名乱码

**症状**：下载的文件名包含乱码

**解决方案**：

```bash
# 配置文件名编码
echo '--restrict-filenames' >> ~/.yt-dlp.conf
```

## 配置问题

### 问题：找不到配置文件

**症状**：
```
Error: Configuration file not found
```

**解决方案**：

```bash
# macOS/Linux: 查找配置文件
ls -la ~/.yt-dlp.conf

# 如果不存在，创建
touch ~/.yt-dlp.conf

# 添加配置
echo '-o ~/Downloads/yt-dlp/%(title)s.%(ext)s' >> ~/.yt-dlp.conf
```

### 问题：下载路径不正确

**症状**：文件下载到错误的位置

**解决方案**：

1. **检查默认路径**：
```bash
cat ~/.yt-dlp.conf | grep -oP '(?<=-o ).*' || echo "~/Downloads/yt-dlp"
```

2. **自定义路径**：
```
下载到 ~/Videos/music 这个文件夹 [URL]
```

3. **修改配置**：
```bash
echo '-o ~/Videos/%(title)s.%(ext)s' >> ~/.yt-dlp.conf
```

## 平台特定问题

### YouTube

#### 问题：视频不可用

**症状**：
```
✗ Video unavailable
```

**解决方案**：
1. 检查视频是否被删除
2. 使用 cookies 登录
3. 检查地区限制
4. 尝试使用 VPN

#### 问题：会员内容无法下载

**症状**：
```
✗ Sign in to confirm you're not a bot
```

**解决方案**：
```
用 Chrome cookies 下载 [URL]
```

确保浏览器已登录 YouTube Premium。

### Bilibili

#### 问题：需要登录

**症状**：
```
✗ Login required
```

**解决方案**：

```bash
# 使用 cookies
yt-dlp --cookies-from-browser chrome [URL]
```

或在 AI IDE 中：
```
用 Chrome cookies 下载 [URL]
```

#### 问题：高清不可用

**症状**：无法下载 1080p+

**解决方案**：
- 需要登录
- 某些视频限制了最高清晰度
- 尝试使用 cookies

### Twitter/X

#### 问题：视频无法下载

**症状**：
```
✗ Could not extract video data
```

**解决方案**：
1. 确保是公开推文
2. 使用 cookies 登录
3. 检查 URL 是否正确

### TikTok

#### 问题：需要登录

**症状**：
```
✗ Login required
```

**解决方案**：
```
用 Chrome cookies 下载 [URL]
```

## 性能问题

### 问题：内存占用高

**症状**：下载时内存占用过高

**解决方案**：

```bash
# 限制缓存大小
echo '--cache-dir /tmp/yt-dlp' >> ~/.yt-dlp.conf
echo '--no-cache-dir' >> ~/.yt-dlp.conf
```

### 问题：CPU 占用高

**症状**：下载时 CPU 占用过高

**解决方案**：

1. **降低下载速度**：
```bash
echo '--limit-rate 1M' >> ~/.yt-dlp.conf
```

2. **使用硬件加速**：
```bash
# 配置 ffmpeg 使用硬件编码
echo '--postprocessor-args "ffmpeg:-threads 1"' >> ~/.yt-dlp.conf
```

## 历史和统计问题

### 问题：历史记录丢失

**症状**：下载历史为空

**解决方案**：

```bash
# 检查历史文件
ls -la ~/.yt-dlp-history.json

# 如果不存在，会自动创建
# 尝试下载一个新视频来初始化
```

### 问题：统计不准确

**症状**：统计数据与实际不符

**解决方案**：

```bash
# 删除历史文件重新开始
rm ~/.yt-dlp-history.json

# 或手动编辑历史文件
vim ~/.yt-dlp-history.json
```

## AI IDE 问题

### Claude Desktop

#### 问题：MCP Server 不响应

**症状**：工具调用无响应

**解决方案**：

1. **检查配置文件**：
```bash
cat ~/.claude/claude_desktop_config.json
```

2. **检查路径**：
```bash
# 确保路径是绝对路径
ls -la /path/to/bingo-downloader/mcp/dist/index.js
```

3. **重启 Claude Desktop**

4. **查看日志**：
```bash
cat ~/Library/Application\ Support/Claude/claude-desktop.log
```

### Cursor

#### 问题：Skills 不生效

**症状**：无法触发 Skills

**解决方案**：

1. **检查 SKILL.md 位置**：
```bash
ls -la ~/.cursor/skills/bingo-downloader/SKILL.md
```

2. **重新安装**：
```bash
cd bingo-downloader
make install-skill
```

3. **重启 Cursor**

### Windsurf

#### 问题：MCP 工具不可用

**症状**：工具列表中没有 Bingo Downloader

**解决方案**：

1. **检查 MCP 配置**
2. **确保 MCP Server 已构建**：
```bash
cd bingo-downloader/mcp
npm run build
```
3. **重启 Windsurf**

## 网络问题

### 问题：连接超时

**症状**：
```
✗ Connection timeout
```

**解决方案**：

1. **检查网络连接**
2. **增加超时时间**：
```bash
echo '--socket-timeout 60' >> ~/.yt-dlp.conf
```
3. **使用代理**（如果需要）：
```bash
echo '--proxy socks5://127.0.0.1:1080' >> ~/.yt-dlp.conf
```

### 问题：DNS 解析失败

**症状**：
```
✗ DNS lookup failed
```

**解决方案**：

1. **更换 DNS 服务器**
2. **使用 VPN**
3. **检查 hosts 文件**

## 调试技巧

### 启用详细日志

```bash
# 临时启用详细日志
export YTDL_PREFER_LEGACY=1
yt-dlp -v [URL]
```

### 测试 yt-dlp

```bash
# 直接测试 yt-dlp
yt-dlp [URL]

# 列出格式
yt-dlp -F [URL]

# 测试下载
yt-dlp -f best [URL]
```

### 检查依赖

```bash
# 检查所有依赖
node --version
python --version
yt-dlp --version
ffmpeg -version
```

### 查看配置

```bash
# 查看 yt-dlp 配置
cat ~/.yt-dlp.conf

# 查看 MCP 配置
cat ~/.claude/claude_desktop_config.json

# 查看 Skills 配置
cat ~/.cursor/skills/bingo-downloader/SKILL.md
```

## 获取帮助

如果以上解决方案都无法解决问题：

1. **查看日志**：
   - MCP Server 日志
   - AI IDE 日志
   - yt-dlp 输出

2. **检查 GitHub Issues**：
   - [已知问题](https://github.com/jiangbingo/bingo-downloader/issues)
   - 搜索类似问题

3. **创建新 Issue**：
   - 提供详细错误信息
   - 包含环境信息
   - 附上日志文件

4. **社区支持**：
   - [GitHub Discussions](https://github.com/jiangbingo/bingo-downloader/discussions)

## 相关文档

- [快速开始](../guide/quick-start.md)
- [使用指南](../guide/usage.md)
- [API 参考](../api/index.md)
- [安装指南](../installation/)