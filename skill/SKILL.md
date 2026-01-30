---
name: bingo-downloader
description: Download videos from YouTube, Bilibili, Twitter, TikTok and 1000+ other sites using yt-dlp. Use when user provides video URL and wants to download, extract audio (MP3), download subtitles, or select video quality. Features: AI-powered smart format selection, auto-retry with exponential backoff, playlist auto-detection, thumbnail extraction, download history & statistics, configuration presets, batch download. Triggers on: "下载视频", "download video", "yt-dlp", "YouTube", "B站", "Bilibili", "抖音", "Douyin", "提取音频", "extract audio", "视频下载", "video downloader", "playlist", "播放列表", "智能下载", "smart download", "缩略图", "thumbnail", "批量下载", "batch download".
---

# Bingo Video Downloader

A powerful video downloader skill powered by [yt-dlp](https://github.com/yt-dlp/yt-dlp), supporting 1000+ websites including YouTube, Bilibili, Twitter/X, TikTok, and more.

## Quick Reference

| Platform | Special Handling |
|----------|------------------|
| YouTube | Always use `--cookies-from-browser chrome` to avoid 403 errors |
| Bilibili | Works directly, may need cookies for some content |
| Twitter/X | Works directly |
| TikTok/Douyin | Works directly |

## Prerequisites

Always verify dependencies before downloading:

```bash
# Check yt-dlp
which yt-dlp || pip install yt-dlp

# Check ffmpeg (required for audio extraction)
which ffmpeg || brew install ffmpeg  # macOS
# or: sudo apt install ffmpeg  # Linux
```

## Installation Methods

### Method 1: Makefile (Recommended)

```bash
# Clone and install
git clone https://github.com/jiangbingo/bingo-downloader-skill.git
cd bingo-downloader-skill
make install
```

### Method 2: Manual Install

```bash
mkdir -p ~/.cursor/skills/bingo-downloader/scripts
cp SKILL.md ~/.cursor/skills/bingo-downloader/
cp scripts/download.sh ~/.cursor/skills/bingo-downloader/scripts/
```

## Download Commands

### 1. Basic Video Download (Best Quality)

```bash
# Using Makefile
make download URL="https://www.youtube.com/watch?v=xxx"

# Using script directly
scripts/download.sh "https://www.youtube.com/watch?v=xxx"

# Using yt-dlp directly
yt-dlp -P "~/Downloads/yt-dlp" "VIDEO_URL"
```

### 2. YouTube Download (with Cookies)

**IMPORTANT:** YouTube requires cookies to avoid 403 Forbidden errors.

```bash
# Using Makefile (auto-applies cookies)
make download URL="https://www.youtube.com/watch?v=xxx"

# Explicit cookies command
make cookie-download URL="https://www.youtube.com/watch?v=xxx"

# Using script with specific browser
scripts/download.sh -c chrome "https://www.youtube.com/watch?v=xxx"
```

Supported browsers: `chrome`, `firefox`, `safari`, `edge`, `brave`, `opera`

### 3. Extract Audio Only (MP3)

```bash
# Using Makefile
make audio URL="https://www.youtube.com/watch?v=xxx"

# Using script
scripts/download.sh -a "VIDEO_URL"

# Direct yt-dlp
yt-dlp -P "~/Downloads/yt-dlp" -x --audio-format mp3 "VIDEO_URL"
```

### 4. Download with Subtitles

```bash
# Using Makefile
make subs URL="https://www.youtube.com/watch?v=xxx"

# Using script
scripts/download.sh -s "VIDEO_URL"

# Direct yt-dlp
yt-dlp -P "~/Downloads/yt-dlp" --write-subs --sub-langs all --embed-subs "VIDEO_URL"
```

### 5. Specific Quality

```bash
# 720p using Makefile
make quality URL="https://www.youtube.com/watch?v=xxx" Q=720

# 1080p using Makefile
make quality URL="https://www.youtube.com/watch?v=xxx" Q=1080

# Using script
scripts/download.sh -q 720 "VIDEO_URL"

# Direct yt-dlp
yt-dlp -P "~/Downloads/yt-dlp" -f "bestvideo[height<=720]+bestaudio/best[height<=720]" "VIDEO_URL"
```

### 6. List Available Formats

```bash
# Using Makefile
make list URL="https://www.youtube.com/watch?v=xxx"

# Using script
scripts/download.sh -l "VIDEO_URL"

# Direct yt-dlp
yt-dlp -F "VIDEO_URL"
```

Then download specific format by ID:
```bash
yt-dlp -P "~/Downloads/yt-dlp" -f FORMAT_ID "VIDEO_URL"
```

### 7. Download Playlist

```bash
# Download entire playlist
yt-dlp -P "~/Downloads/yt-dlp" -o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" "PLAYLIST_URL"

# Download specific range (e.g., items 1-5)
yt-dlp -P "~/Downloads/yt-dlp" -I 1:5 "PLAYLIST_URL"
```

### 8. Download with Thumbnail

```bash
yt-dlp -P "~/Downloads/yt-dlp" --write-thumbnail "VIDEO_URL"
```

## 🚀 Smart Features (New!)

### 9. AI-Powered Smart Format Selection

Automatically selects the best video format based on:
- User preference history
- Network conditions
- File size optimization
- Codec compatibility (H.264/H.265 priority)
- Frame rate preference (60fps > 30fps)

```bash
make smart-download USE_PYTHON=true URL="VIDEO_URL"
python3 scripts/download.py --smart "VIDEO_URL"
```

### 10. Playlist Auto-Detection

Automatically detects playlist URLs and offers interactive options:
- Download all videos
- Specify range (e.g., 1-5, 8, 10-15)
- Cancel

```bash
make playlist URL="PLAYLIST_URL"
make playlist-range URL="PLAYLIST_URL" RANGE="1-5,8-10"
python3 scripts/download.py --playlist-items "1-5" "PLAYLIST_URL"
```

### 11. Download History & Statistics

All downloads are tracked in SQLite database (`~/.yt-dlp-history.db`):

```bash
make history
make stats
python3 scripts/download.py --history
python3 scripts/download.py --stats
```

Statistics include:
- Total downloads, success/failure counts
- Success rate percentage
- Total file size downloaded
- Breakdown by platform

### 12. Configuration Presets

Built-in presets for common use cases:

```bash
make presets
make download URL="VIDEO_URL" PRESET=high-quality
make download URL="VIDEO_URL" PRESET=fast
make download URL="VIDEO_URL" PRESET=audio-only
make download URL="VIDEO_URL" PRESET=best

# Or save custom preset
python3 scripts/download.py --save-preset my-preset --audio --subs
python3 scripts/download.py --preset my-preset "VIDEO_URL"
```

Default presets:
- **high-quality**: 1080p with subtitles and thumbnail
- **fast**: 720p quick download
- **audio-only**: High-quality MP3 extraction
- **best**: Best quality available (no limit)

### 13. Batch Download

Download multiple videos from a text file:

```bash
make batch-download FILE=url_list.txt

# URL list format (one URL per line, # for comments)
# My download list
https://www.youtube.com/watch?v=xxx1
https://www.youtube.com/watch?v=xxx2
https://www.bilibili.com/video/BV1xx
```

Shows progress with success/failure summary.

### 14. Smart Retry with Exponential Backoff

Network failures automatically retry with:
- Up to 3 attempts (configurable)
- Exponential backoff: 5s → 10s → 20s
- Distinguishes retryable errors (429, 503, 502, timeout)
- Clear progress indication

## Makefile Commands

```bash
# Show all available commands
make help

# Check dependencies
make check

# Install to Cursor
make install

# Uninstall
make uninstall

# Update yt-dlp
make update

# Run tests
make test

# Clean temporary files
make clean
```

## Workflow

When user provides a video URL:

1. **Identify the platform** from the URL
2. **Ask what they want** (if not specified):
   - Just download the video?
   - Extract audio only?
   - Need subtitles?
   - Specific quality?
3. **Apply platform-specific handling**:
   - YouTube → Always use cookies
   - Other sites → Try without cookies first
4. **Construct and execute the command**
5. **Handle errors gracefully**:
   - 403 Forbidden → Retry with cookies
   - Connection issues → Inform about auto-resume
   - Format unavailable → List formats first

## Error Handling

### HTTP 403 Forbidden (YouTube)

**Symptom:** `HTTP Error 403: Forbidden`

**Solution:** Always use cookies for YouTube
```bash
make cookie-download URL="YOUTUBE_URL"
```

### Video Unavailable

**Symptom:** `Video unavailable` or geo-restricted

**Solutions:**
```bash
# Try with cookies
make cookie-download URL="VIDEO_URL"

# List formats and select specific one
make list URL="VIDEO_URL"
```

### Download Interrupted

**Symptom:** Network timeout or interruption

**Solution:** Just retry - yt-dlp auto-resumes downloads

### Format Not Available

**Symptom:** `Requested format not available`

**Solution:**
```bash
# List available formats first
make list URL="VIDEO_URL"

# Download with format ID
scripts/download.sh -f FORMAT_ID "VIDEO_URL"
```

## Configuration

Create `~/.yt-dlp.conf` for default settings:

```bash
# Default download path
DOWNLOAD_PATH="~/Videos"

# Default cookies browser
COOKIES_BROWSER="chrome"

# Default quality
QUALITY="1080"
```

## Example Interactions

### Example 1: Basic Download

**User:** 下载这个视频 https://www.youtube.com/watch?v=dQw4w9WgXcQ

**Response:**
```bash
# YouTube detected - using cookies automatically
make cookie-download URL="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### Example 2: Audio Extraction

**User:** Extract audio from this Bilibili video https://www.bilibili.com/video/BV1xx411c7mD

**Response:**
```bash
# Bilibili - extracting audio as MP3
make audio URL="https://www.bilibili.com/video/BV1xx411c7mD"
```

### Example 3: Quality Selection

**User:** Download in 720p: https://twitter.com/username/status/1234567890

**Response:**
```bash
# Twitter - downloading at 720p
make quality URL="https://twitter.com/username/status/1234567890" Q=720
```

### Example 4: With Subtitles

**User:** 下载带字幕的视频 https://www.youtube.com/watch?v=xxx

**Response:**
```bash
# YouTube - downloading with embedded subtitles
make cookie-download URL="https://www.youtube.com/watch?v=xxx" SUBS=true
# Or using the script directly:
scripts/download.sh -c chrome -s "https://www.youtube.com/watch?v=xxx"
```

## Supported Sites

yt-dlp supports 1000+ sites including:

| Category | Sites |
|----------|-------|
| Video Platforms | YouTube, YouTube Music, Vimeo, Dailymotion, Twitch |
| Chinese Platforms | Bilibili (B站), Douyin (抖音), Youku, iQIYI |
| Social Media | Twitter/X, TikTok, Facebook, Instagram, Reddit |
| Live Streaming | Twitch, YouTube Live |

[Full list](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

## Tips & Best Practices

1. **YouTube downloads:** Always use `--cookies-from-browser chrome` (Makefile does this automatically)
2. **Large files:** yt-dlp supports auto-resume, just retry if interrupted
3. **Keep updated:** Run `make update` or `pip install -U yt-dlp` regularly
4. **Check formats first:** Use `make list` before downloading if unsure about available formats
5. **Batch downloads:** Create a text file with URLs (one per line) and use batch commands
6. **Custom output path:** Use `DOWNLOAD_PATH` variable with make commands

## Troubleshooting Quick Reference

| Error | Quick Fix |
|-------|-----------|
| `command not found: yt-dlp` | `pip install yt-dlp` |
| `ffmpeg not found` | `brew install ffmpeg` |
| `HTTP Error 403` | Use `make cookie-download` |
| `Video unavailable` | Try cookies or check URL |
| `Format not available` | Use `make list` to see formats |
| Download slow | Update yt-dlp: `make update` |
