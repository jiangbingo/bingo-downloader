# Contributing to Bingo Downloader

Thank you for your interest in contributing to Bingo Downloader! This document provides guidelines and instructions for contributing.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**: What happened and what you expected to happen
- **Steps to reproduce**: Minimal reproduction steps
- **Environment info**:
  - Operating system and version
  - Node.js version (`node --version`)
  - yt-dlp version (`yt-dlp --version`)
  - AI IDE / CLI being used
  - MCP Server or Skills
- **Error messages**: Full error output with stack traces
- **Screenshots**: If applicable

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:

- **Use case**: What problem would this solve?
- **Proposed solution**: How should it work?
- **Alternatives considered**: What other approaches did you consider?
- **Impact**: Who would benefit and how?

## Development Setup

### Prerequisites

```bash
# Install Node.js (18+)
node --version || brew install node

# Install yt-dlp
pip install yt-dlp

# Install ffmpeg (required for audio extraction)
brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Linux

# Install development dependencies
cd mcp
npm install
```

### Project Structure

```
bingo-downloader/
├── mcp/              # MCP Server implementation
│   ├── src/
│   │   ├── index.ts      # MCP Server entry point
│   │   ├── downloader.ts # Download logic
│   │   └── history.ts    # History management
│   ├── package.json
│   └── tsconfig.json
├── skill/            # Skills implementation
│   ├── SKILL.md
│   ├── Makefile
│   └── scripts/
├── docs/              # Documentation
│   ├── mkdocs.yml
│   └── *.md
├── .github/           # CI/CD workflows
├── Makefile          # Unified commands
└── README.md
```

### Making Changes

1. **Fork repository** and create your branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following code style guidelines

3. **Test your changes**:
   ```bash
   # Build MCP Server
   cd mcp
   npm run build
   
   # Type check
   npx tsc --noEmit
   
   # Run in dev mode
   npm run dev
   ```

4. **Commit your changes** with clear messages:
   ```bash
   git commit -m "feat: add batch download support"
   ```

5. **Push and create pull request**

## Code Style Guidelines

### TypeScript (mcp/src/)

- Follow ESLint configuration
- Use strict TypeScript mode
- Add JSDoc comments for public APIs
- Keep functions focused and under 100 lines when possible
- Use async/await for asynchronous operations
- Handle errors properly with try-catch

### MCP Tool Guidelines

When adding new MCP tools:

1. Define tool schema in `ListToolsRequestSchema` handler
2. Implement tool logic in `CallToolRequestSchema` handler
3. Add proper error handling with helpful messages
4. Update API documentation in `docs/api/`
5. Add usage examples in `docs/examples/`

Example:
```typescript
case 'new_tool': {
  const result = await newTool(
    args.url as string,
    args.optionalParam as string
  );
  return {
    content: [{
      type: 'text',
      text: result.success 
        ? `✓ Success: ${result.message}` 
        : `✗ Error: ${result.error}`
    }],
    isError: !result.success
  };
}
```

### Skills Guidelines

When updating Skills:

1. Update `skill/SKILL.md` with new trigger keywords
2. Document new features in SKILL.md content
3. Add usage examples
4. Update `docs/guide/` if needed

## Adding New Features

### 1. MCP Tools

When adding new MCP tools:

1. Implement tool logic in appropriate file:
   - `downloader.ts` for download-related tools
   - `history.ts` for history/statistics tools
2. Register tool in `index.ts`
3. Add to `docs/api/` directory
4. Test with AI IDE

### 2. Format Support

To add support for a new video format:

1. Test with yt-dlp directly
2. Add format option to relevant tools
3. Document in API reference
4. Add examples

### 3. Platform-Specific Features

To add platform-specific handling:

1. Update platform detection in `downloader.ts`
2. Add necessary parameters
3. Test with sample URLs
4. Document platform-specific notes

## Documentation

### API Documentation

When adding or modifying MCP tools:

1. Create/update file in `docs/api/`
2. Include:
   - Tool description
   - Parameters table
   - Return values
   - Examples
   - Error handling
3. Update `docs/mkdocs.yml` navigation

### Documentation Updates

Keep documentation in sync:
- Update `README.md` (English)
- Update `docs/guide/` sections
- Update `docs/api/` reference
- Update `CHANGELOG.md` for releases

## Testing

### Manual Testing Checklist

- [ ] Tool compiles without errors
- [ ] Type checking passes
- [ ] Basic download works
- [ ] Audio extraction works
- [ ] Subtitle download works
- [ ] Quality selection works
- [ ] Format listing works
- [ ] History tracking works
- [ ] Statistics calculation correct
- [ ] Error messages are helpful

### Platform Testing

Test with MCP-compatible AI IDEs:
- [ ] Claude Desktop
- [ ] Cursor
- [ ] Windsurf

Test with Skills:
- [ ] Cursor
- [ ] Claude Code
- [ ] Windsurf
- [ ] Gemini Code

## Pull Request Process

1. **Update CHANGELOG.md**: Add entry under "Unreleased" section
2. **Ensure tests pass**: All type checks and builds
3. **Update documentation**: Keep README and docs in sync
4. **Squash commits**: Clean up commit history if needed
5. **Link issues**: Reference related issue numbers

### PR Title Convention

Use semantic prefix:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (no functional change)
- `refactor:` Code refactoring
- `test:` Test additions or changes
- `chore:` Build process or auxiliary tool changes

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Manual testing completed
- [ ] Documentation updated
- [ ] CHANGELOG.md updated

## Related Issues
Closes #123
```

## Release Process

1. Update version numbers:
   - `mcp/package.json`
   - Run `make version`
2. Update `CHANGELOG.md`
3. Create Git tag
4. Create GitHub release with notes
5. MCP Server automatically published to npm (if configured)

## CI/CD

The project uses GitHub Actions for:

- **CI**: Testing on multiple OS and Node versions
- **Documentation**: Automatic deployment to GitHub Pages
- **Quality**: Type checking and linting

View workflows in `.github/workflows/`

## Community Guidelines

- Be respectful and constructive
- Welcome newcomers and help them learn
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Help

- Check existing documentation first
- Search existing issues and discussions
- Ask questions in GitHub Discussions
- Join community chat (if available)

## License

By contributing, you agree that your contributions will be licensed under MIT License.

## Acknowledgments

Thank you to all contributors who have helped make Bingo Downloader better!

Special thanks to:
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) team for the powerful download engine
- [MCP Team](https://modelcontextprotocol.io/) for the protocol specification
- All contributors and users who provide feedback