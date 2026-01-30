# 使用示例

本页提供各种实际使用场景的示例。

## 基础示例

### 示例 1：简单下载

下载一个 YouTube 视频：

```
你: 下载这个视频 https://www.youtube.com/watch?v=dQw4w9WgXcQ

Claude: ✓ Download completed!

File: ~/Downloads/yt-dlp/Rick Astley - Never Gonna Give You Up.mp4
Size: 50.00MiB
Platform: YouTube
```

### 示例 2：指定质量

下载 720p 视频：

```
你: 用 720p 下载 https://www.youtube.com/watch?v=dQw4w9WgXcQ

Claude: ✓ Download completed!

File: ~/Downloads/yt-dlp/Rick Astley - Never Gonna Give You Up [720p].mp4
Size: 25.00MiB
Platform: YouTube
```

### 示例 3：自定义路径

下载到特定文件夹：

```
你: 下载到 ~/Videos/music 这个文件夹 https://www.youtube.com/watch?v=dQw4w9WgXcQ

Claude: ✓ Download completed!

File: ~/Videos/music/Rick Astley - Never Gonna Give You Up.mp4
Size: 50.00MiB
Platform: YouTube
```

## 音频示例

### 示例 4：提取 MP3

提取视频音频为 MP3：

```
你: 提取这个视频的音频，保存为 mp3 https://www.youtube.com/watch?v=dQw4w9WgXcQ

Claude: ✓ Audio extracted!

File: ~/Downloads/yt-dlp/Rick Astley - Never Gonna Give You Up.mp3
Size: 5.00MiB
Format: MP3 (320kbps)
```

### 示例 5：提取 FLAC

提取高质量 FLAC 音频：

```
你: 提取 FLAC 音质 https://www.youtube.com/watch?v=dQw4w9WgXcQ

Claude: ✓ Audio extracted!

File: ~/Downloads/yt-dlp/Rick Astley - Never Gonna Give You Up.flac
Size: 15.00MiB
Format: FLAC (lossless)
```

### 示例 6：音乐收藏

下载多个音乐视频并提取音频：

```
你: 提取这个视频的音频 https://www.youtube.com/watch?v=xxx1

Claude: [完成]

你: 提取这个视频的音频 https://www.youtube.com/watch?v=xxx2

Claude: [完成]

你: 提取这个视频的音频 https://www.youtube.com/watch?v=xxx3

Claude: [完成]

你: 查看下载历史

Claude: ✓ Found 3 downloads

[显示历史记录]
```

## 字幕示例

### 示例 7：下载带字幕

下载视频并嵌入字幕：

```
你: 下载这个视频带字幕 https://www.youtube.com/watch?v=dQw4w9WgXcQ

Claude: ✓ Download completed!

File: ~/Downloads/yt-dlp/Rick Astley - Never Gonna Give You Up [en].mp4
Size: 50.00MiB
Subtitles: English
```

### 示例 8：多语言字幕

下载视频并指定字幕语言：

```
你: 下载中英文字幕 https://www.youtube.com/watch?v=dQw4w9WgXcQ

Claude: ✓ Download completed!

File: ~/Downloads/yt-dlp/Rick Astley - Never Gonna Give You Up [zh,en].mp4
Size: 50.00MiB
Subtitles: Chinese, English
```

### 示例 9：Bilibili 字幕

下载 B 站视频带弹幕：

```
你: 下载这个 B 站视频带字幕 https://www.bilibili.com/video/BV1xx411c7mD

Claude: ✓ Download completed!

File: ~/Downloads/yt-dlp/Video Title [danmaku].mp4
Size: 100.00MiB
Platform: Bilibili
Subtitles: Danmaku
```

## 格式查看示例

### 示例 10：列出所有格式

查看视频的所有可用格式：

```
你: 列出这个视频的格式 https://www.youtube.com/watch?v=dQw4w9WgXcQ

Claude: ✓ Found 12 formats

Video Formats:
  1. 1080p (best) - H.264, 60fps - 50MB
  2. 720p - H.264, 60fps - 25MB
  3. 480p - H.264, 30fps - 15MB
  4. 360p - H.264, 30fps - 8MB

Audio Formats:
  1. MP3 (320kbps) - 5MB
  2. M4A (AAC) - 4MB
```

### 示例 11：选择特定格式

根据格式列表下载：

```
你: 列出这个视频的格式 https://www.youtube.com/watch?v=dQw4w9WgXcQ

Claude: [显示格式列表]

你: 用第二个格式下载

Claude: ✓ Download completed!

File: ~/Downloads/yt-dlp/Video Title [720p].mp4
Size: 25.00MiB
```

## 历史和统计示例

### 示例 12：查看下载历史

查看最近的下载记录：

```
你: 查看下载历史

Claude: ✓ Found 10 downloads

1. Rick Astley - Never Gonna Give You Up
   Platform: YouTube
   Quality: 1080p
   Size: 50.00MiB
   Date: 2025-01-30 15:00:00

2. Video Title
   Platform: Bilibili
   Quality: 720p
   Size: 100.00MiB
   Date: 2025-01-30 14:30:00

... [更多记录]
```

### 示例 13：限制历史数量

只查看最近 5 条记录：

```
你: 显示最近 5 条下载记录

Claude: ✓ Found 5 downloads

[显示 5 条记录]
```

### 示例 14：按平台筛选

查看特定平台的下载记录：

```
你: 查看 YouTube 的下载历史

Claude: ✓ Found 5 YouTube downloads

[显示 YouTube 下载记录]
```

### 示例 15：查看统计信息

查看下载统计数据：

```
你: 显示下载统计

Claude: ✓ Statistics

Total Downloads: 50
Successful: 48 (96%)
Failed: 2 (4%)
Total Size: 2.5GiB

Platform Breakdown:
  YouTube: 30 (60%)
  Bilibili: 15 (30%)
  Twitter: 5 (10%)
```

## 平台特定示例

### 示例 16：YouTube Shorts

下载 YouTube Shorts：

```
你: 下载这个 YouTube Shorts youtube.com/shorts/xxx

Claude: ✓ Download completed!

File: ~/Downloads/yt-dlp/Shorts Title.mp4
Size: 5.00MiB
Platform: YouTube Shorts
```

### 示例 17：Bilibili 高清

下载 B 站高清视频：

```
你: 用 1080p 下载这个 B 站视频 https://www.bilibili.com/video/BV1xx411c7mD

Claude: ✓ Download completed!

File: ~/Downloads/yt-dlp/Video Title [1080p].mp4
Size: 150.00MiB
Platform: Bilibili
```

### 示例 18：Twitter 视频

下载 Twitter 视频：

```
你: 下载这个 Twitter 视频 twitter.com/user/status/123456

Claude: ✓ Download completed!

File: ~/Downloads/yt-dlp/Twitter Video.mp4
Size: 10.00MiB
Platform: Twitter
```

### 示例 19：TikTok 视频

下载 TikTok 视频：

```
你: 下载这个 TikTok 视频 tiktok.com/@user/video/123456

Claude: ✓ Download completed!

File: ~/Downloads/yt-dlp/TikTok Video.mp4
Size: 8.00MiB
Platform: TikTok
```

## 复杂工作流示例

### 示例 20：学习资料下载

下载教程视频并获取多个版本：

```
你: 下载这个教程视频 1080p https://www.youtube.com/watch?v=xxx

Claude: ✓ Download completed!

你: 下载带字幕，我要中英文字幕

Claude: ✓ Download completed!

你: 提取音频，我也要听版本

Claude: ✓ Audio extracted!

File: ~/Downloads/yt-dlp/Tutorial Audio.mp3
Size: 10.00MiB
```

### 示例 21：音乐播放列表

下载多个音乐视频并提取音频：

```
你: 提取这个视频的音频 https://www.youtube.com/watch?v=xxx1
Claude: ✓ Audio extracted!

你: 提取这个视频的音频 https://www.youtube.com/watch?v=xxx2
Claude: ✓ Audio extracted!

你: 提取这个视频的音频 https://www.youtube.com/watch?v=xxx3
Claude: ✓ Audio extracted!

你: 查看下载历史
Claude: ✓ Found 3 downloads

[显示所有音频文件]
```

### 示例 22：内容分类下载

按平台分类下载：

```
你: 下载这个 YouTube 视频 https://www.youtube.com/watch?v=xxx1
Claude: ✓ Download completed!

你: 下载这个 B 站视频 https://www.bilibili.com/video/BV1xx411c7mD
Claude: ✓ Download completed!

你: 查看 YouTube 的下载历史
Claude: ✓ Found 1 YouTube download

[显示 YouTube 记录]
```

### 示例 23：质量控制

先查看格式再下载：

```
你: 列出这个视频的格式 https://www.youtube.com/watch?v=xxx

Claude: [显示格式列表]

你: 用第三个格式下载
Claude: ✓ Download completed!

File: ~/Downloads/yt-dlp/Video Title [480p].mp4
Size: 15.00MiB
```

## 错误处理示例

### 示例 24：处理 403 错误

遇到 403 错误时使用 cookies：

```
你: 下载这个 YouTube 视频 https://www.youtube.com/watch?v=xxx

Claude: ✗ Download failed: HTTP Error 403: Forbidden

你: 用 Chrome cookies 下载
Claude: ✓ Download completed!

File: ~/Downloads/yt-dlp/Video Title.mp4
Size: 50.00MiB
```

### 示例 25：质量降级

高清晰度失败时降级：

```
你: 用 1080p 下载 https://www.youtube.com/watch?v=xxx

Claude: ✗ Download failed: 1080p not available

你: 用 720p 下载
Claude: ✓ Download completed!

File: ~/Downloads/yt-dlp/Video Title [720p].mp4
Size: 25.00MiB
```

## 实际场景示例

### 场景 1：离线观看

```
你: 下载这个播放列表的第一个视频 720p https://www.youtube.com/playlist?list=xxx
Claude: ✓ Download completed!

你: 下载第二个视频 720p
Claude: ✓ Download completed!

[继续下载其他视频...]
```

### 场景 2：音乐收藏

```
你: 提取这个音乐视频的 FLAC 音质 https://www.youtube.com/watch?v=xxx1
Claude: ✓ Audio extracted!

你: 提取这个音乐视频的 FLAC 音质 https://www.youtube.com/watch?v=xxx2
Claude: ✓ Audio extracted!

你: 提取这个音乐视频的 FLAC 音质 https://www.youtube.com/watch?v=xxx3
Claude: ✓ Audio extracted!

你: 查看下载历史
Claude: ✓ Found 3 FLAC downloads
```

### 场景 3：学习资料

```
你: 下载这个教程视频带字幕 https://www.youtube.com/watch?v=xxx1
Claude: ✓ Download completed!

你: 下载这个教程视频带字幕 https://www.youtube.com/watch?v=xxx2
Claude: ✓ Download completed!

你: 查看下载历史
Claude: ✓ Found 2 tutorial downloads
```

### 场景 4：内容备份

```
你: 下载这个 Twitter 视频 https://twitter.com/user/status/xxx1
Claude: ✓ Download completed!

你: 下载这个 Twitter 视频 https://twitter.com/user/status/xxx2
Claude: ✓ Download completed!

你: 查看 Twitter 的下载历史
Claude: ✓ Found 2 Twitter downloads
```

### 场景 5：播客下载

```
你: 提取这个播客的音频 https://www.youtube.com/watch?v=xxx1
Claude: ✓ Audio extracted!

你: 提取这个播客的音频 https://www.youtube.com/watch?v=xxx2
Claude: ✓ Audio extracted!

你: 提取这个播客的音频 https://www.youtube.com/watch?v=xxx3
Claude: ✓ Audio extracted!

你: 查看下载历史
Claude: ✓ Found 3 podcast downloads
```

## 更多示例

查看更多特定平台的示例：

- [YouTube 示例](youtube.md)
- [Bilibili 示例](bilibili.md)
- [Twitter 示例](twitter.md)
- [其他平台示例](other-platforms.md)

## 相关文档

- [快速开始](../guide/quick-start.md)
- [使用指南](../guide/usage.md)
- [API 参考](../api/index.md)
- [故障排除](../troubleshooting/)