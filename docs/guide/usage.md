# 使用指南

本指南详细介绍 Bingo Downloader 的各种使用场景和最佳实践。

## 基础使用

### 下载视频

最简单的用法，使用默认设置下载视频：

```
你: 下载这个视频 https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

这会下载最佳可用质量到默认路径 `~/Downloads/yt-dlp/`。

### 指定质量

```
你: 用 720p 下载这个视频 https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

支持的质量选项：
- `best` - 最佳可用质量
- `1080` - 最高 1080p
- `720` - 最高 720p
- `480` - 最高 480p
- `360` - 最高 360p

### 自定义下载路径

```
你: 下载到 ~/Videos/music 这个文件夹 https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

## 高级功能

### 提取音频

将视频转换为音频文件：

```
你: 提取这个视频的音频，保存为 mp3 https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

支持的音频格式：
- `mp3` - MP3 格式（默认）
- `wav` - WAV 无损格式
- `m4a` - M4A 格式
- `flac` - FLAC 无损格式
- `aac` - AAC 格式

示例：
```
你: 提取 FLAC 音质 https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### 下载字幕

下载视频并嵌入字幕：

```
你: 下载这个视频带字幕 https://www.bilibili.com/video/BV1xx411c7mD
```

指定字幕语言：
```
你: 下载中英文字幕 https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### 查看可用格式

在下载前查看所有可用格式：

```
你: 列出这个视频的所有格式 https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

这会显示：
- 视频质量选项
- 音频格式选项
- 文件大小
- 编解码器信息

### 查看下载历史

查看最近的下载记录：

```
你: 查看我的下载历史
```

限制显示数量：
```
你: 显示最近 5 条下载记录
```

按平台筛选：
```
你: 查看 YouTube 的下载历史
```

### 查看统计信息

```
你: 显示下载统计
```

显示：
- 总下载次数
- 成功率
- 总下载大小
- 各平台分布

## 平台特定使用

### YouTube

#### 基本

```
你: 下载这个 YouTube 视频 https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

#### 处理 403 错误

如果遇到 403 错误，使用浏览器 cookies：

```
你: 用 Chrome cookies 下载这个 YouTube 视频
```

系统会自动使用 `cookies_browser="chrome"` 参数。

#### 短链接

```
你: 下载这个 YouTube 视频 youtu.be/dQw4w9WgXcQ
```

#### YouTube Shorts

```
你: 下载这个 YouTube Shorts youtube.com/shorts/xxx
```

### Bilibili

```
你: 下载这个 B 站视频 https://www.bilibili.com/video/BV1xx411c7mD
```

Bilibili 支持的功能：
- 高清下载（最高 1080p+）
- 弹幕下载
- CC 字幕

### Twitter/X

```
你: 下载这个 Twitter 视频 twitter.com/user/status/123456
```

### TikTok

```
你: 下载这个 TikTok 视频 tiktok.com/@user/video/123456
```

### 其他平台

支持 1000+ 网站，包括：
- Instagram
- Facebook
- Vimeo
- Dailymotion
- 等等...

直接粘贴 URL 即可下载。

## 最佳实践

### 1. 选择合适的质量

- **日常观看**: 720p 足够
- **高清收藏**: 1080p
- **专业用途**: best（最高质量）
- **节省空间**: 360p

### 2. 音频质量

- **日常听歌**: MP3 (默认)
- **音乐收藏**: FLAC 或 WAV
- **兼容性**: M4A 或 AAC

### 3. 使用 Cookies

对于 YouTube 和某些平台，使用 cookies 可以：
- 避免 403 错误
- 解锁会员内容
- 提高下载速度

### 4. 管理下载路径

按类型分类：

```
~/Downloads/
├── yt-dlp/
│   ├── youtube/
│   ├── bilibili/
│   ├── music/
│   └── podcasts/
```

## 工作流示例

### 音乐下载工作流

```
你: 提取这个视频的音频保存为 mp3 https://www.youtube.com/watch?v=xxx

[下载中...]

你: 下载到 ~/Music/playlist

[下载完成]

你: 查看下载历史
```

### 视频学习工作流

```
你: 下载这个教程视频 1080p https://www.youtube.com/watch?v=xxx

[下载中...]

你: 下载带字幕，我要中英文字幕

[下载完成]

你: 提取音频，我也要听版本

[音频提取完成]
```

### 内容整理工作流

```
你: 下载这个视频 https://www.bilibili.com/video/BV1xx411c7mD

你: 下载这个视频 https://www.bilibili.com/video/BV1yy411c7mD

你: 下载这个视频 https://www.bilibili.com/video/BV1zz411c7mD

你: 查看下载历史

你: 显示统计信息
```

## 常见使用场景

### 场景 1：离线观看

```
你: 下载这个 YouTube 播放列表的所有视频，用 720p
```

### 场景 2：音乐收藏

```
你: 提取这个音乐视频的 FLAC 音质 https://www.youtube.com/watch?v=xxx
```

### 场景 3：学习资料

```
你: 下载这个教程视频带字幕 https://www.youtube.com/watch?v=xxx
```

### 场景 4：内容备份

```
你: 下载我发布的所有 Twitter 视频
```

### 场景 5：播客下载

```
你: 提取这个播客的音频 https://www.youtube.com/watch?v=xxx
```

## 提示和技巧

### 1. 快速下载

使用自然语言，越简单越好：

- ✅ "下载这个视频 [URL]"
- ✅ "下载 [URL]"
- ❌ "请帮我执行下载操作，URL 是..."

### 2. 批量操作

虽然当前版本不支持直接批量下载，但你可以：

```
你: 下载这个视频 [URL1]

[完成]

你: 下载这个视频 [URL2]

[完成]

...
```

### 3. 质量选择

如果不确定，使用：

```
你: 列出这个视频的格式 [URL]

[查看格式]

你: 用第二个格式下载
```

### 4. 错误处理

遇到错误时：

1. 检查 URL 是否正确
2. 尝试使用 cookies
3. 查看错误信息
4. 尝试降低质量

## 错误排除

### 下载失败

```
✗ Download failed: HTTP Error 403: Forbidden
```

**解决方案**：
```
你: 用 Chrome cookies 下载 [URL]
```

### 音频提取失败

```
✗ Audio extraction failed: ffmpeg not found
```

**解决方案**：
安装 ffmpeg：
```bash
brew install ffmpeg  # macOS
```

### URL 不支持

```
✗ Unsupported URL
```

**解决方案**：
1. 检查 URL 格式
2. 确认网站是否支持
3. 尝试完整 URL 而非短链接

## 相关文档

- [快速开始](quick-start.md)
- [API 参考](../api/index.md)
- [故障排除](../troubleshooting/)
- [示例](../examples/)