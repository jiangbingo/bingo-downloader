<div align="center">

  # 🎬 Bingo Downloader

  ### 🔥 A powerful video downloader with MCP Server, Skills & Web UI
  ### Supporting 1000+ websites: YouTube, Bilibili, Twitter, TikTok and more!

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
  [![yt-dlp](https://img.shields.io/badge/Powered%20by-yt--lp-red.svg)](https://github.com/yt-dlp/yt-dlp)
  [![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-blue.svg)](https://modelcontextprotocol.io/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-Web%20UI-green.svg)](https://fastapi.tiangolo.com/)
  [![Node](https://img.shields.io/badge/Node-18%2B-green.svg)](https://nodejs.org/)
  [![Docs](https://img.shields.io/badge/Docs-MkDocs-blue.svg)](https://jiangbingo.github.io/bingo-downloader/)

  [English](./README.md) | [中文文档](./README_CN.md)

</div>

<div align="center">

**⚡ One command, download from 1000+ websites!**

**🤖 Works seamlessly with AI IDEs - just paste a URL and let AI handle the rest!**

**🌐 Beautiful Web UI - for those who prefer a graphical interface!**

**📚 Full Documentation: [bingo-downloader.jiangbingo.com](https://jiangbingo.github.io/bingo-downloader/)**

</div>

---

## ✨ Features

### 🚀 Triple Mode Architecture

- **MCP Server**: Direct tool integration with AI IDEs (Cursor, Claude, etc.)
- **Skills**: Natural language interface for easy usage
- **Web UI**: Modern browser-based interface (NEW!)
- All modes share the same powerful yt-dlp backend

### 🎬 Video Downloading

- 🌐 **1000+ Sites Supported** - YouTube, Bilibili, Twitter/X, TikTok, and more
- 🎯 **Quality Selection** - Choose from 360p, 480p, 720p, 1080p, or best available
- 🍪 **Smart Cookie Handling** - Auto-handle YouTube 403 errors with browser cookies
- ⏸️ **Resume Support** - Auto-resume interrupted downloads
- 🔄 **Smart Retry** - Exponential backoff on network failures

### 🎵 Audio Extraction

- Extract audio from any video
- Support for MP3, WAV, M4A, FLAC, AAC formats
- High-quality audio conversion

### 📝 Subtitles

- Download and embed subtitles
- Multi-language support (all, en, zh, ja, etc.)
- Auto-detect available languages

### 📊 History & Statistics

- Track all your downloads in local database
- View download statistics and success rate
- Platform breakdown and total data downloaded

---

## 🚀 Quick Start

### 1️⃣ Clone Repository

```bash
git clone https://github.com/jiangbingo/bingo-downloader.git
cd bingo-downloader
```

### 2️⃣ Install

```bash
# Install everything (MCP, Skills & Web UI)
make install

# Or install separately
make install-mcp      # MCP Server only
make install-skill    # Skills only
make install-web      # Web UI only
```

### 3️⃣ Configure MCP Server (Optional)

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "bingo-downloader": {
      "command": "node",
      "args": ["/path/to/bingo-downloader/mcp/dist/index.js"]
    }
  }
}
```

### 4️⃣ Start Using!

#### Option A: With AI IDE (MCP/Skills)

Just tell your AI IDE what you want:

> "下载这个视频 https://www.youtube.com/watch?v=xxx"

And watch magic happen! ✨

#### Option B: With Web UI (NEW!)

```bash
# Start the web server
make run-web

# Or in dev mode
make dev-web
```

Then open your browser to **http://localhost:8000**

---

## 📖 Documentation

📚 **Full documentation available at**: [bingo-downloader.jiangbingo.com](https://jiangbingo.github.io/bingo-downloader/)

### Quick Links

- [Quick Start Guide](https://jiangbingo.github.io/bingo-downloader/quick-start/)
- [Installation](https://jiangbingo.github.io/bingo-downloader/installation/)
- [Usage Guide](https://jiangbingo.github.io/bingo-downloader/usage/)
- [API Reference](https://jiangbingo.github.io/bingo-downloader/api/)
- [Examples](https://jiangbingo.github.io/bingo-downloader/examples/)
- [Troubleshooting](https://jiangbingo.github.io/bingo-downloader/troubleshooting/)

---

## 🤖 Supported AI IDEs

| AI IDE | Installation | Status |
|---------|--------------|--------|
| **[Cursor](https://cursor.sh)** | `make install-skill` | ✅ Fully Supported |
| **[Claude Code](https://code.anthropic.com/)** | `make install-skill` | ✅ Fully Supported |
| **[Windsurf](https://windsurf.ai/)** | `make install-skill` | ✅ Fully Supported |
| **[OpenAI CodeSandbox](https://codesandbox.io)** | `make install-skill` | ✅ Compatible |
| **[Gemini Code](https://ai.google.dev/gemini-code)** | `make install-skill` | ✅ Experimental |
| **[Trae](https://trae.ai)** | `make install-skill` | ✅ Experimental |

### Why Use with AI IDEs?

🎯 **Natural Language Interface** - Just paste a URL and tell your AI assistant what you want:
- "Download this YouTube video in 1080p"
- "Extract audio from this Bilibili video"
- "Get subtitles for this Twitter video"

🚀 **Automatic Command Generation** - The AI understands your request and executes the right download command automatically.

🛠️ **Zero Configuration** - Install once and use across all your AI-powered development tools.

---

## 🌐 Supported Platforms

| Platform | Status | Notes |
|----------|--------|-------|
| <img src="https://simpleicons.org/icons/youtube.svg" width="20" height="20"> YouTube | ✅ Perfect | Use cookies for best results |
| <img src="https://simpleicons.org/icons/bilibili.svg" width="20" height="20"> Bilibili | ✅ Perfect | Works directly |
| <img src="https://simpleicons.org/icons/x.svg" width="20" height="20"> Twitter/X | ✅ Perfect | Works directly |
| <img src="https://simpleicons.org/icons/tiktok.svg" width="20" height="20"> TikTok | ✅ Perfect | Works directly |
| <img src="https://simpleicons.org/icons/vimeo.svg" width="20" height="20"> Vimeo | ✅ Perfect | Works directly |
| <img src="https://simpleicons.org/icons/twitch.svg" width="20" height="20"> Twitch | ✅ Perfect | Works directly |
| <img src="https://simpleicons.org/icons/facebook.svg" width="20" height="20"> Facebook | ✅ Good | May require cookies |
| <img src="https://simpleicons.org/icons/instagram.svg" width="20" height="20"> Instagram | ✅ Good | May require cookies |

And 1000+ more sites! [View full list](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

---

## 📁 Project Structure

```
bingo-downloader/
├── mcp/                    # MCP Server implementation
│   ├── src/
│   │   ├── index.ts          # MCP Server entry point
│   │   ├── downloader.ts     # Download logic
│   │   └── history.ts        # History management
│   ├── package.json
│   └── tsconfig.json
│
├── skill/                  # Skills with natural language interface
│   ├── SKILL.md           # Skill definition
│   ├── Makefile           # Installation commands
│   └── scripts/          # Helper scripts
│
├── web/                    # Web UI (NEW!)
│   ├── backend/           # FastAPI backend
│   │   ├── main.py        # Application entry
│   │   ├── api/           # API routes
│   │   ├── models/        # Data models
│   │   └── core/          # Core logic (reuses skill scripts)
│   ├── frontend/          # HTML/CSS/JS templates
│   │   ├── templates/     # Jinja2 templates
│   │   └── static/        # Static assets
│   └── tests/             # Web tests
│
├── docs/                   # MkDocs documentation
│   ├── index.md
│   ├── installation/
│   ├── usage/
│   ├── api/
│   └── examples/
│
└── README.md              # This file
```

---

## 💻 Usage

### Using MCP Server

After installation and configuration, MCP tools are available in your AI IDE:

```bash
# Download video
bingo-downloader → download_video(url="https://youtube.com/...")

# Extract audio
bingo-downloader → extract_audio(url="https://youtube.com/...", format="mp3")

# Download with subtitles
bingo-downloader → download_with_subs(url="https://youtube.com/...")

# List formats
bingo-downloader → list_formats(url="https://youtube.com/...")

# View history
bingo-downloader → get_history(limit=20)

# View statistics
bingo-downloader → get_stats()
```

### Using Skills

Skills provide a natural language interface. Just ask your AI IDE:

> "Download this YouTube video https://www.youtube.com/watch?v=xxx"
> "Extract audio from this Bilibili video"
> "Download in 720p with subtitles"
> "Show me my download history"

The AI will automatically call the appropriate MCP tools.

---

## 🎯 Makefile Commands

### Installation
```bash
make install          # Install both MCP and Skills
make install-mcp      # Install MCP Server only
make install-skill    # Install Skills only
make uninstall        # Uninstall Skills
```

### Development
```bash
make build             # Build MCP Server
make dev              # Run MCP Server in dev mode
make test             # Run tests
make check            # Check dependencies
```

### Documentation
```bash
make docs-serve       # Serve documentation locally
make docs-build       # Build documentation
```

### Release
```bash
make version          # Bump version
make publish          # Publish MCP to npm
make release          # Create release tag
```

---

## ⚙️ Configuration

### System Requirements

- **Node.js**: >= 18.0.0
- **Python**: 3.8+ (for yt-dlp)
- **yt-dlp**: Latest version
- **ffmpeg**: Required for audio extraction

### Installation Commands

```bash
# Install yt-dlp
pip install yt-dlp
# or: uv pip install yt-dlp (recommended)
# or: brew install yt-dlp (macOS)

# Install ffmpeg
brew install ffmpeg  # macOS
# or: sudo apt install ffmpeg  # Linux
```

### Custom Configuration

Create `~/.yt-dlp.conf` for custom defaults:

```bash
# Default download path
DOWNLOAD_PATH="~/Videos"

# Default cookies browser
COOKIES_BROWSER="chrome"

# Default quality
QUALITY="1080"
```

---

## 🐛 Troubleshooting

### HTTP Error 403 (YouTube)

**Problem:** YouTube blocks download with 403 Forbidden error.

**Solution:** Use browser cookies
```bash
# MCP: Set cookies_browser parameter
download_video(url="...", cookies_browser="chrome")

# Skills: AI will automatically use cookies
```

### Command Not Found

**Problem:** `yt-dlp: command not found`

**Solution:**
```bash
pip install yt-dlp
```

### FFmpeg Not Found

**Problem:** `ffmpeg not found` (when extracting audio)

**Solution:**
```bash
brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Linux
```

For more troubleshooting, see the [full documentation](https://jiangbingo.github.io/bingo-downloader/troubleshooting/).

---

## 📝 Example Interactions

### Example 1: Simple Download

> **You:** 下载这个视频 https://www.youtube.com/watch?v=xxx

**AI:** [Calls MCP tool: download_video with cookies_browser="chrome"]
```
✓ Download completed!

File: ~/Downloads/yt-dlp/Rick Astley - Never Gonna Give You Up.mp4
Size: 50.00MiB
Platform: YouTube
```

### Example 2: Audio Extraction

> **You:** I need to extract MP3 audio from this Bilibili video

**AI:** [Calls MCP tool: extract_audio with format="mp3"]
```
✓ Audio extraction completed!

File: ~/Downloads/yt-dlp/Video Title.mp3
Format: mp3
Size: 3.50MiB
```

### Example 3: With Subtitles

> **You:** Download this video with English and Chinese subtitles

**AI:** [Calls MCP tool: download_with_subs with sub_langs="en,zh"]
```
✓ Download with subtitles completed!

File: ~/Downloads/yt-dlp/Video Title.mp4
Subtitles: Embedded (English, Chinese)
Quality: best
```

---

## 🙏 Credits

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The powerful video downloader engine
- [Model Context Protocol](https://modelcontextprotocol.io/) - Standard for AI tool integration
- [MkDocs](https://www.mkdocs.org/) - Documentation framework
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - Documentation theme

---

## 📄 License

MIT License - feel free to use this in your own projects!

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](https://jiangbingo.github.io/bingo-downloader/contributing/).

---

## 📚 Documentation

For comprehensive documentation, visit **[bingo-downloader.jiangbingo.com](https://jiangbingo.github.io/bingo-downloader/)**

<div align="center">

Made with ❤️ by [jiangbingo](https://github.com/jiangbingo)

[⭐ Star this repo](https://github.com/jiangbingo/bingo-downloader) if it helps you!

[📚 Full Documentation](https://jiangbingo.github.io/bingo-downloader/) • 
[🐛 Report Issues](https://github.com/jiangbingo/bingo-downloader/issues)

</div>