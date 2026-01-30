# download_video 工具

下载视频到本地。

## 参数

| 参数 | 类型 | 必需 | 默认值 | 描述 |
|------|------|--------|----------|--------|
| `url` | string | 是 | - | 视频 URL |
| `quality` | string | 否 | "best" | 视频质量 |
| `cookies_browser` | string | 否 | "chrome" | 浏览器 cookies |
| `download_path` | string | 否 | ~/Downloads/yt-dlp | 下载路径 |

## 质量（quality）选项

| 值 | 描述 |
|-----|--------|
| `best` | 最佳可用质量 |
| `1080` | 最高 1080p |
| `720` | 最高 720p |
| `480` | 最高 480p |
| `360` | 最高 360p |

## Cookies 浏览器选项

| 值 | 描述 |
|-----|--------|
| `chrome` | Google Chrome |
| `firefox` | Mozilla Firefox |
| `safari` | Safari (macOS) |
| `edge` | Microsoft Edge |
| `brave` | Brave Browser |
| `opera` | Opera |

## 返回值

成功时：
```text
✓ Download completed!

File: ~/Downloads/yt-dlp/Video Title.mp4
Size: 150.00MiB
Platform: YouTube
```

失败时：
```text
✗ Download failed: HTTP Error 403: Forbidden
```

## 示例

### 基础下载

```bash
download_video(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
```

### 指定质量

```bash
download_video(
  url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  quality="1080"
)
```

### 使用 Firefox Cookies

```bash
download_video(
  url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  cookies_browser="firefox"
)
```

### 自定义下载路径

```bash
download_video(
  url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  download_path="~/Videos/youtube"
)
```

### 完整示例

```bash
download_video(
  url="https://www.bilibili.com/video/BV1xx411c7mD",
  quality="720",
  cookies_browser="chrome",
  download_path="~/Videos/bilibili"
)
```

## 使用场景

### 下载 YouTube 视频

```bash
download_video(
  url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  quality="best"
)
```

### 下载 Bilibili 视频

```bash
download_video(
  url="https://www.bilibili.com/video/BV1xx411c7mD",
  quality="1080"
)
```

### 下载 Twitter 视频

```bash
download_video(
  url="https://twitter.com/user/status/123456789",
  quality="best"
)
```

## 注意事项

1. **YouTube 403 错误**
   - 如果遇到 403 错误，使用 cookies_browser 参数
   - 推荐使用 cookies_browser="chrome"

2. **下载路径**
   - 确保目标目录存在
   - 确保有写入权限

3. **磁盘空间**
   - 确保有足够的磁盘空间
   - 1080p 视频通常 100MB - 1GB

4. **网络连接**
   - 大文件下载可能需要较长时间
   - MCP Server 支持断点续传

## 错误处理

### yt-dlp 未安装

```text
✗ Download failed: yt-dlp is not installed. 
Install with: pip install yt-dlp
```

**解决方案**: 安装 yt-dlp
```bash
pip install yt-dlp
```

### 无效的 URL

```text
✗ Download failed: Unsupported URL
```

**解决方案**: 检查 URL 格式是否正确

### 权限错误

```text
✗ Download failed: Permission denied
```

**解决方案**: 检查下载路径权限或更改路径

## 相关工具

- [extract_audio](audio.md) - 提取音频
- [download_with_subs](subtitles.md) - 下载带字幕
- [list_formats](#) - 列出可用格式