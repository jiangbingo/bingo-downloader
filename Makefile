# Bingo Downloader - Makefile
# A powerful video downloader with MCP Server and Skills

.PHONY: help
help:
	@echo "Bingo Downloader - Video Downloader with MCP Server, Skills & Web UI"
	@echo ""
	@echo "Installation:"
	@echo "  make install          - Install MCP, Skills & Web"
	@echo "  make install-mcp      - Install MCP Server only"
	@echo "  make install-skill    - Install Skills only"
	@echo "  make install-web      - Install Web UI dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make build             - Build MCP Server"
	@echo "  make dev               - Run MCP Server in dev mode"
	@echo "  make run-web           - Run Web UI server"
	@echo "  make dev-web           - Run Web UI in dev mode (hot reload)"
	@echo "  make test              - Run all tests"
	@echo "  make test-web          - Run Web UI tests"
	@echo "  make test-download     - Download test videos"
	@echo "  make test-download-url - Test with custom URL"
	@echo ""
	@echo "Documentation:"
	@echo "  make docs-serve        - Serve documentation locally"
	@echo "  make docs-build        - Build documentation"
	@echo ""
	@echo "Release:"
	@echo "  make version           - Bump version"
	@echo "  make publish           - Publish MCP to npm"
	@echo "  make release           - Create release tag"

# Install everything
.PHONY: install
install: install-mcp install-skill install-web
	@echo ""
	@echo "✓ Installation complete!"
	@echo ""
	@echo "To use MCP Server, add this to your claude_desktop_config.json:"
	@echo '{"mcpServers": {"bingo-downloader": {"command": "node", "args": ["$(PWD)/mcp/dist/index.js"]}}}'
	@echo ""
	@echo "To use Web UI, run: make run-web"
	@echo ""

# Install MCP Server
.PHONY: install-mcp
install-mcp:
	@echo "Installing MCP Server..."
	@cd mcp && npm install
	@cd mcp && npm run build
	@echo "✓ MCP Server installed"
	@echo ""
	@echo "Add this to your claude_desktop_config.json:"
	@echo '{"mcpServers": {"bingo-downloader": {"command": "node", "args": ["$(PWD)/mcp/dist/index.js"]}}}'
	@echo ""

# Install Skills
.PHONY: install-skill
install-skill:
	@echo "Installing Skills to all supported AI IDEs..."
	@echo ""
	@# Cursor
	@mkdir -p ~/.cursor/skills/bingo-downloader
	@cp skill/SKILL.md ~/.cursor/skills/bingo-downloader/
	@echo "✓ Cursor: ~/.cursor/skills/bingo-downloader/"
	@# Windsurf (Codeium)
	@mkdir -p ~/.windsurf/skills/bingo-downloader 2>/dev/null || true
	@cp skill/SKILL.md ~/.windsurf/skills/bingo-downloader/ 2>/dev/null || true
	@echo "✓ Windsurf: ~/.windsurf/skills/bingo-downloader/"
	@# Continue (VS Code extension)
	@mkdir -p ~/.continue/skills/bingo-downloader 2>/dev/null || true
	@cp skill/SKILL.md ~/.continue/skills/bingo-downloader/ 2>/dev/null || true
	@echo "✓ Continue: ~/.continue/skills/bingo-downloader/"
	@# Cline (VS Code extension)
	@mkdir -p ~/.cline/skills/bingo-downloader 2>/dev/null || true
	@cp skill/SKILL.md ~/.cline/skills/bingo-downloader/ 2>/dev/null || true
	@echo "✓ Cline: ~/.cline/skills/bingo-downloader/"
	@# Roo Code (VS Code extension)
	@mkdir -p ~/.roocode/skills/bingo-downloader 2>/dev/null || true
	@cp skill/SKILL.md ~/.roocode/skills/bingo-downloader/ 2>/dev/null || true
	@echo "✓ Roo Code: ~/.roocode/skills/bingo-downloader/"
	@echo ""
	@echo "✅ Skills installed to all supported AI IDEs!"
	@echo ""
	@echo "Note: Restart your AI IDE for changes to take effect."
	@echo ""

# Install Web UI
.PHONY: install-web
install-web:
	@echo "Installing Web UI dependencies with uv..."
	@which uv || (echo "✗ uv not found. Install with: curl -LsSf https://astral.sh/uv/install.sh | sh" && exit 1)
	@echo "Creating virtual environment in web/backend/.venv..."
	@cd web/backend && uv venv .venv
	@echo "✓ Virtual environment created: web/backend/.venv/"
	@echo "Installing dependencies..."
	@cd web/backend && uv pip install -r requirements.txt
	@echo "✓ Web UI dependencies installed to web/backend/.venv/"
	@echo ""
	@echo "════════════════════════════════════════════════════════════════"
	@echo "  Next Steps:"
	@echo "════════════════════════════════════════════════════════════════"
	@echo "  From project root:  make run-web"
	@echo "  From web/backend/:   make run   (or use ./run.sh)"
	@echo "════════════════════════════════════════════════════════════════"
	@echo ""

# Build
.PHONY: build
build:
	@echo "Building MCP Server..."
	@cd mcp && npm run build
	@echo "✓ Build complete"

# Dev mode
.PHONY: dev
dev:
	@cd mcp && npm run dev

# Run Web UI
.PHONY: run-web
run-web:
	@echo "Starting Web UI server..."
	@cd web && PYTHONPATH=$(PWD) backend/.venv/bin/python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000

# Run Web UI in dev mode
.PHONY: dev-web
dev-web:
	@echo "Starting Web UI in dev mode..."
	@cd web && PYTHONPATH=$(PWD) backend/.venv/bin/python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

# Test
.PHONY: test
test: test-mcp test-web
	@echo ""
	@echo "✓ All tests complete"

# Test MCP Server
.PHONY: test-mcp
test-mcp:
	@echo "Running MCP Server tests..."
	@cd mcp && npm test

# Test MCP Server with coverage
.PHONY: test-mcp-coverage
test-mcp-coverage:
	@echo "Running MCP Server tests with coverage..."
	@cd mcp && npm run test:coverage

# Test MCP Server with UI
.PHONY: test-mcp-ui
test-mcp-ui:
	@echo "Running MCP Server tests with UI..."
	@cd mcp && npm run test:ui

# Test MCP Server in watch mode
.PHONY: test-mcp-watch
test-mcp-watch:
	@echo "Running MCP Server tests in watch mode..."
	@cd mcp && npm run test:watch

# Test Web UI
.PHONY: test-web
test-web:
	@echo "Running Web UI tests..."
	@cd web/backend && .venv/bin/pytest tests/ -v

# Test Web UI with coverage
.PHONY: test-web-coverage
test-web-coverage:
	@echo "Running Web UI tests with coverage..."
	@cd web/backend && .venv/bin/pytest tests/ -v --cov=. --cov-report=html --cov-report=term

# Test coverage for all
.PHONY: test-coverage
test-coverage: test-mcp-coverage test-web-coverage
	@echo ""
	@echo "✓ Coverage reports generated"
	@echo "MCP coverage: mcp/coverage/"
	@echo "Web coverage: web/backend/htmlcov/"

# Check dependencies
.PHONY: check
check:
	@echo "Checking dependencies..."
	@which yt-dlp || (echo "✗ yt-dlp not found. Install with: pip install yt-dlp" && exit 1)
	@which ffmpeg || (echo "✗ ffmpeg not found. Install with: brew install ffmpeg" && exit 1)
	@which node || (echo "✗ Node.js not found" && exit 1)
	@echo "✓ All dependencies OK"

# Test download - Download sample videos for testing
.PHONY: test-download
test-download:
	@echo "Downloading test videos..."
	@mkdir -p tests/samples
	@echo "Downloading YouTube test video..."
	@(cd tests/samples && yt-dlp --newline --no-color -f "b" --max-filesize 10M -o "youtube_test.%(ext)s" "https://www.youtube.com/watch?v=jNQXAC9IVRw" && ls -lh) || echo "  ✗ YouTube download failed (may need VPN or cookies)"
	@echo ""
	@echo "✓ Test download complete!"
	@echo "Samples saved to: tests/samples/"
	@ls -lh tests/samples/ 2>/dev/null | tail -n +2 || echo "  (No samples directory)"
	@echo ""
	@echo "Tip: Use with your own URL:"
	@echo "  yt-dlp -f b \"YOUR_URL\" -o downloads/video.%(ext)s"
	@echo ""

# Test download with custom URL
.PHONY: test-download-url
test-download-url:
	@read -p "Enter video URL: " url; \
	mkdir -p tests/samples; \
	echo ""; \
	echo "Downloading from: $$url"; \
	(cd tests/samples && yt-dlp --newline -f "b" -o "custom_test.%(ext)s" "$$url" && ls -lh) || echo "  ✗ Download failed"

# Clean test samples
.PHONY: clean-test
clean-test:
	@echo "Cleaning test samples..."
	@rm -rf tests/samples
	@echo "✓ Test samples cleaned"

# Version update
.PHONY: version
version:
	@read -p "New version: " version; \
	npm version $$version; \
	cd mcp && npm version $$version; \
	echo "✓ Version updated to $$version"

# Publish
.PHONY: publish
publish:
	@echo "Publishing MCP Server..."
	@cd mcp && npm publish
	@echo "✓ Published to npm"
	@echo ""
	@echo "Skills are available in repository"
	@echo "Users can install with: make install-skill"

# Release
.PHONY: release
release: version publish
	@echo "✓ Release complete"

# Documentation
.PHONY: docs-serve
docs-serve:
	@echo "Serving documentation..."
	@cd docs && mkdocs serve

.PHONY: docs-build
docs-build:
	@echo "Building documentation..."
	@cd docs && mkdocs build
	@echo "✓ Documentation built to docs/site/"

# Clean
.PHONY: clean
clean: clean-test
	@echo "Cleaning MCP Server..."
	@cd mcp && rm -rf dist
	@echo "Cleaning Web UI..."
	@rm -rf web/backend/.venv
	@rm -rf web/backend/__pycache__
	@rm -rf web/backend/api/__pycache__
	@rm -rf web/backend/core/__pycache__
	@rm -rf web/backend/models/__pycache__
	@find web -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Clean complete"

# Uninstall
.PHONY: uninstall
uninstall:
	@echo "Uninstalling Skills from all AI IDEs..."
	@rm -rf ~/.cursor/skills/bingo-downloader
	@echo "✓ Cursor: removed"
	@rm -rf ~/.windsurf/skills/bingo-downloader 2>/dev/null || true
	@echo "✓ Windsurf: removed"
	@rm -rf ~/.continue/skills/bingo-downloader 2>/dev/null || true
	@echo "✓ Continue: removed"
	@rm -rf ~/.cline/skills/bingo-downloader 2>/dev/null || true
	@echo "✓ Cline: removed"
	@rm -rf ~/.roocode/skills/bingo-downloader 2>/dev/null || true
	@echo "✓ Roo Code: removed"
	@echo ""
	@echo "✅ Skills uninstalled from all AI IDEs"
	@echo ""
	@echo "Note: To uninstall MCP Server, remove it from your claude_desktop_config.json"