# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-01-30

### 🚀 Major Release - MCP Server & Monorepo Architecture

This release transforms the project from a Skills-only implementation to a full-featured monorepo with both MCP Server and Skills support.

### Added

#### 1. MCP Server Implementation
- **Full TypeScript MCP Server** with stdio transport
- 6 MCP tools available:
  - `download_video`: Download videos with quality selection
  - `extract_audio`: Extract audio in multiple formats (MP3, WAV, M4A, FLAC, AAC)
  - `download_with_subs`: Download videos with embedded subtitles
  - `list_formats`: List all available video/audio formats
  - `get_history`: View download history from local database
  - `get_stats`: View download statistics and success rate
- Platform auto-detection (YouTube, Bilibili, Twitter, TikTok, etc.)
- Smart cookie handling for YouTube 403 errors
- Download history management with JSON-based storage
- Comprehensive error handling with helpful messages

#### 2. Monorepo Architecture
- Unified repository structure for MCP Server and Skills
- Shared Makefile for easy installation and management
- Coordinated version management across all components
- Improved code organization and maintainability

#### 3. Documentation System
- **MkDocs-based documentation** with Material theme
- Multi-language support (English and Chinese)
- Dark/light mode toggle
- GitHub Pages integration with automatic deployment
- Comprehensive documentation structure:
  - Quick start guide
  - Installation instructions
  - API reference
  - Usage examples
  - Troubleshooting guide
  - Contributing guidelines

#### 4. GitHub Actions CI/CD
- Automated CI testing across multiple OS and Node versions
- Automatic documentation deployment to GitHub Pages
- Build verification and type checking
- Streamlined release process

### Changed

#### Project Structure
```
bingo-downloader/
├── mcp/              # New: MCP Server implementation
│   ├── src/
│   │   ├── index.ts
│   │   ├── downloader.ts
│   │   └── history.ts
│   ├── package.json
│   └── tsconfig.json
├── skill/            # Retained: Skills implementation
│   ├── SKILL.md
│   ├── Makefile
│   └── scripts/
├── docs/              # New: MkDocs documentation
│   ├── mkdocs.yml
│   └── index.md
├── .github/           # New: CI/CD workflows
│   └── workflows/
├── Makefile          # Updated: Unified commands
└── README.md         # Updated: Comprehensive guide
```

### Enhanced

#### Makefile Commands
- `make install` - Install both MCP and Skills
- `make install-mcp` - Install MCP Server only
- `make install-skill` - Install Skills only
- `make build` - Build MCP Server
- `make dev` - Run MCP Server in development mode
- `make docs-serve` - Serve documentation locally
- `make docs-build` - Build documentation
- `make version` - Bump version across all components
- `make publish` - Publish MCP Server to npm
- `make check` - Verify dependencies

#### Skills
- Now work as natural language interface to MCP tools
- Enhanced trigger keywords for AI assistants
- Better integration with AI IDEs (Cursor, Claude, Windsurf, etc.)

### Documentation

- Complete API reference for all MCP tools
- Installation guides for MCP Server and Skills
- Quick start guide for new users
- Troubleshooting section with common issues
- Configuration guides (cookies, presets, etc.)
- Example usage for different platforms

### Platform Support

**MCP Server Compatible with:**
- Claude Desktop
- Cursor
- Windsurf
- Any MCP-compliant AI IDE

**Skills Compatible with:**
- Cursor
- Claude Code
- Windsurf
- Gemini Code
- Trae
- OpenAI CodeSandbox

### Performance

- Optimized MCP Server with efficient TypeScript compilation
- Fast history queries with JSON-based storage
- Minimal resource footprint
- Quick tool execution with proper error handling

### Migration

**From bingo-downloader-skill 1.x:**
1. Clone new repository: `git clone https://github.com/jiangbingo/bingo-downloader.git`
2. Run: `make install`
3. Configure MCP Server in your AI IDE (optional)
4. Skills continue to work seamlessly

No data migration needed - history is stored per-component.

## [1.0.0] - 2025-01-27

### Initial Release (bingo-downloader-skill)

#### Features
- Basic video download support
- Audio extraction (MP3)
- Subtitle download
- Quality selection (720p, 1080p, etc.)
- Playlist download support
- Format listing capability
- Multi-platform support (YouTube, Bilibili, Twitter, TikTok, 1000+ sites)
- Makefile automation
- Bash and Python script implementations
- Installation scripts for AI IDEs

#### Documentation
- Comprehensive README in English and Chinese
- SKILL.md for AI assistant integration
- Quick reference guide

---

## Release Notes

### Version 2.0.0 Highlights

**For Users:**
- 🚀 **Dual Mode**: Choose between MCP Server or Skills based on your needs
- 📦 **Easy Installation**: Single `make install` command for everything
- 📚 **Great Documentation**: Comprehensive MkDocs site with examples
- 🤖 **AI-Ready**: Works seamlessly with all major AI IDEs

**For Developers:**
- 🧩 **TypeScript**: Full type safety and modern tooling
- 🔌 **MCP Protocol**: Standardized tool interface
- 📦 **NPM Package**: Easy to distribute and install
- 🔄 **CI/CD**: Automated testing and deployment

### Upgrade from 1.0.0

This is a new project structure. Follow these steps:

```bash
# 1. Clone new repository
git clone https://github.com/jiangbingo/bingo-downloader.git
cd bingo-downloader

# 2. Install
make install

# 3. Configure MCP Server (optional)
# Add to your claude_desktop_config.json
```

All your skills from 1.0.0 will continue to work!

---

## [Unreleased]

### Planned
- [ ] Batch download through MCP tools
- [ ] Download queue management
- [ ] Real-time download progress in MCP
- [ ] Format presets configuration
- [ ] Integration tests for all AI IDEs