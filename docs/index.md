# Welcome to Bingo Downloader

<div align="center">

**A powerful video downloader with MCP Server and Skills**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![yt-dlp](https://img.shields.io/badge/Powered%20by-yt--lp-red.svg)](https://github.com/yt-dlp/yt-dlp)
[![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-blue.svg)](https://modelcontextprotocol.io/)

**Supporting: YouTube, Bilibili, Twitter/X, TikTok and 1000+ other sites**

[Quick Start](quick-start.md) • [Installation](installation/index.md) • [Documentation](usage/index.md)

</div>

---

## Features

### 🚀 Dual Mode

- **MCP Server**: Direct tool integration with AI IDEs
- **Skills**: Natural language interface for easy usage

### 🎬 Video Downloading

- **1000+ Sites Supported**: YouTube, Bilibili, Twitter, TikTok, and more
- **Quality Selection**: Choose from 360p, 480p, 720p, 1080p, or best available
- **Smart Cookie Handling**: Auto-handle YouTube 403 errors with browser cookies
- **Resume Support**: Auto-resume interrupted downloads

### 🎵 Audio Extraction

- Extract audio from any video
- Support for MP3, WAV, M4A, FLAC, AAC formats
- High-quality audio conversion

### 📝 Subtitles

- Download and embed subtitles
- Multi-language support
- Auto-detect available languages

### 📊 History & Statistics

- Track all your downloads
- View download statistics
- Platform breakdown
- Success rate tracking

---

## Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/jiangbingo/bingo-downloader.git
cd bingo-downloader
```

### 2. Install

```bash
# Install both MCP Server and Skills
make install

# Or install separately
make install-mcp      # MCP Server only
make install-skill    # Skills only
```

### 3. Configure MCP Server

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

### 4. Start Using

- **With MCP**: Direct tool calls from your AI IDE
- **With Skills**: Natural language requests

Example:

```
You: "下载这个 YouTube 视频 https://www.youtube.com/watch?v=xxx"

Claude: [Uses MCP tool to download]
✓ Download completed!
```

---

## Architecture

Bingo Downloader uses a dual-mode architecture:

```
┌─────────────────────────────────────────────────┐
│         User (You or AI IDE)               │
└────────────┬────────────────────────────────┘
             │
    ┌────────┴────────┐
    │                 │
    ↓                 ↓
┌─────────┐   ┌──────────┐
│  MCP    │   │  Skills  │
│ Server  │   │  (Docs)  │
└────┬────┘   └────┬─────┘
     │              │
     └──────┬───────┘
            ↓
     ┌──────────────────┐
     │    yt-dlp      │
     │  (Engine)      │
     └──────────────────┘
```

### MCP Server

- Runs as a local process
- Communicates via stdin/stdout
- Provides tools for video downloading
- Manages download history

### Skills

- Natural language interface
- Easy to use
- Works with multiple AI IDEs
- Automatic tool invocation

---

## Supported Platforms

| Platform | Status | Notes |
|----------|--------|-------|
| YouTube | ✅ Perfect | Use cookies for best results |
| Bilibili | ✅ Perfect | Works directly |
| Twitter/X | ✅ Perfect | Works directly |
| TikTok/Douyin | ✅ Perfect | Works directly |
| Vimeo | ✅ Perfect | Works directly |
| Twitch | ✅ Perfect | Works directly |
| Facebook | ✅ Good | May require cookies |
| Instagram | ✅ Good | May require cookies |

[View full list of 1000+ supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

---

## AI IDE Support

Bingo Downloader works with popular AI-powered development environments:

| AI IDE | Status |
|---------|--------|
| **Cursor** | ✅ Fully Supported |
| **Claude Code** | ✅ Fully Supported |
| **Windsurf** | ✅ Fully Supported |
| **OpenAI CodeSandbox** | ✅ Compatible |
| **Gemini Code** | ✅ Experimental |
| **Trae** | ✅ Experimental |

---

## Documentation

- [Quick Start](quick-start.md) - Get started in 5 minutes
- [Installation Guide](installation/index.md) - Detailed installation instructions
- [Usage Guide](usage/index.md) - How to use all features
- [API Reference](api/index.md) - Complete API documentation
- [Examples](examples/index.md) - Real-world examples
- [Troubleshooting](troubleshooting/index.md) - Common issues and solutions

---

## Requirements

- **Node.js**: >= 18.0.0
- **yt-dlp**: Latest version
- **ffmpeg**: Required for audio extraction
- **Python**: 3.8+ (for yt-dlp)

[See detailed requirements](installation/dependencies.md)

---

## Contributing

Contributions are welcome! Please read our [Contributing Guide](contributing/index.md).

---

## License

MIT License - see [LICENSE](https://github.com/jiangbingo/bingo-downloader/blob/main/LICENSE) for details

---

<div align="center">

Made with ❤️ by [jiangbingo](https://github.com/jiangbingo)

[⭐ Star on GitHub](https://github.com/jiangbingo/bingo-downloader) • 
[🐛 Report Issues](https://github.com/jiangbingo/bingo-downloader/issues)

</div>