# 项目重组说明

## 📋 概述

本项目已从单一的 Skills 项目重组为 Monorepo 架构，同时支持 MCP Server 和 Skills 两种模式。

## 🏗️ 新项目结构

```
bingo-downloader/
├── mcp/                    # MCP Server 实现
│   ├── src/
│   │   ├── index.ts          # MCP Server 入口
│   │   ├── downloader.ts     # 下载逻辑（封装 yt-dlp）
│   │   └── history.ts        # 历史记录管理
│   ├── package.json          # npm 包配置
│   └── tsconfig.json        # TypeScript 配置
│
├── skill/                  # Skills 实现
│   ├── SKILL.md           # Skill 定义（AI IDE 使用）
│   ├── Makefile           # Skills 安装脚本
│   └── scripts/          # 辅助脚本（从原项目迁移）
│       ├── download.sh
│       └── download.py
│
├── docs/                   # MkDocs 文档
│   ├── mkdocs.yml         # 文档配置
│   ├── index.md           # 文档首页
│   ├── installation/      # 安装指南（待创建）
│   ├── usage/            # 使用指南（待创建）
│   ├── api/              # API 参考（待创建）
│   ├── examples/         # 示例（待创建）
│   └── configuration/    # 配置说明（待创建）
│
├── shared/                 # 共享代码（可选）
│
├── .gitignore             # Git 忽略文件
├── Makefile              # 统一的 Makefile
├── README.md             # 项目说明
├── LICENSE               # 许可证（需从原项目复制）
├── CHANGELOG.md          # 变更日志（需从原项目复制）
└── CONTRIBUTING.md       # 贡献指南（需从原项目复制）
```

## 🔄 主要变更

### 1. MCP Server 实现

**新增文件**：
- `mcp/src/index.ts` - MCP Server 主入口
  - 注册 6 个工具：download_video, extract_audio, download_with_subs, list_formats, get_history, get_stats
  - 使用 JSON-RPC 协议通过 stdin/stdout 通信
  - 自动错误处理和格式化

- `mcp/src/downloader.ts` - 下载逻辑
  - 封装 yt-dlp 命令
  - 自动检测平台（YouTube, Bilibili, Twitter 等）
  - 支持质量选择、音频提取、字幕下载
  - 智能错误处理（检查 yt-dlp 和 ffmpeg 安装）

- `mcp/src/history.ts` - 历史记录管理
  - 使用 JSON 文件存储下载历史
  - 支持查询、统计、筛选
  - 平台分解和成功率计算

- `mcp/package.json` - npm 包配置
  - 包名：@bingo/downloader-mcp
  - 依赖：@modelcontextprotocol/sdk
  - 支持全局安装

- `mcp/tsconfig.json` - TypeScript 配置
  - 目标：ES2022
  - 严格模式启用
  - 声明文件和源码映射

### 2. Skills 实现

**保留文件**：
- `skill/SKILL.md` - Skill 定义（从原项目复制）
- `skill/Makefile` - 安装脚本（从原项目复制）
- `skill/scripts/` - 辅助脚本（从原项目复制）

**说明**：Skills 现在作为 MCP Server 的自然语言接口层。

### 3. 统一 Makefile

**新增命令**：
```bash
# 安装
make install          # 安装 MCP 和 Skills
make install-mcp      # 仅安装 MCP Server
make install-skill    # 仅安装 Skills
make uninstall        # 卸载 Skills

# 开发
make build             # 构建 MCP Server
make dev              # 开发模式运行 MCP Server
make test             # 运行测试
make check            # 检查依赖

# 文档
make docs-serve       # 本地服务文档
make docs-build       # 构建文档

# 发布
make version          # 更新版本号
make publish          # 发布 MCP 到 npm
make release          # 创建发布标签
```

### 4. 文档系统

**使用 MkDocs**：
- 主题：Material for MkDocs
- 支持暗色/亮色模式切换
- 支持中英文搜索
- GitHub Pages 集成
- 版本管理

**文档结构**：
- 首页和快速开始
- 安装指南（MCP、Skills、依赖）
- 使用指南（MCP 工具、Skills 示例）
- API 参考（所有工具的详细说明）
- 示例（YouTube、Bilibili、批量下载）
- 配置说明（Cookies、预设）
- 故障排除（常见错误、解决方案）
- 贡献指南

### 5. 项目名称变更

- **原名称**：bingo-downloader-skill
- **新名称**：bingo-downloader

**原因**：
- 反映双模式架构（MCP + Skills）
- 更简洁和通用
- 便于未来扩展

## 🎯 双模式工作流程

```
用户请求
    ↓
┌─────────┴─────────┐
│                 │
Skills (SKILL.md)  直接 MCP 调用
    │                 │
    ↓                 ↓
理解用户意图       执行工具
    │                 │
    └─────┬─────────┘
          ↓
    MCP Server
          ↓
    yt-dlp 命令
          ↓
    下载文件
```

**Skills 模式**：
- 用户自然语言请求
- Skills 理解意图
- 调用 MCP 工具
- 返回结果给用户

**MCP 模式**：
- 直接工具调用
- 开发者/高级用户使用
- 更灵活的控制

## 📚️ 文档链接

**MkDocs 文档**：https://jiangbingo.github.io/bingo-downloader/

**GitHub 仓库**：https://github.com/jiangbingo/bingo-downloader

## ✅ 下一步行动

1. **创建剩余文档页面**：
   - installation/mcp-server.md
   - installation/skills.md
   - installation/dependencies.md
   - usage/mcp-tools.md
   - usage/skills-examples.md
   - api/download.md
   - api/audio.md
   - api/subtitles.md
   - api/history.md
   - examples/youtube.md
   - examples/bilibili.md
   - troubleshooting/common-errors.md
   - 等等...

2. **复制许可证和贡献文件**：
   - 从原项目复制 LICENSE
   - 从原项目复制 CHANGELOG.md
   - 从原项目复制 CONTRIBUTING.md

3. **创建 GitHub Actions**：
   - CI/CD 流程
   - 自动发布文档到 GitHub Pages
   - 自动测试 MCP Server

4. **测试 MCP Server**：
   - 本地测试所有工具
   - 测试与 Cursor/Claude 集成
   - 测试错误处理

5. **发布到 npm**：
   - 首次发布 @bingo/downloader-mcp
   - 更新文档链接

## 🎓 学习资源

### MCP 协议
- [MCP 官方文档](https://modelcontextprotocol.io/)
- [MCP SDK](https://github.com/modelcontextprotocol/typescript-sdk)

### MkDocs
- [MkDocs 官方文档](https://www.mkdocs.org/)
- [Material 主题](https://squidfunk.github.io/mkdocs-material/)

### yt-dlp
- [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)
- [支持的网站列表](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

## 📝 维护建议

1. **版本同步**：
   - MCP Server 和 Skills 应该使用相同版本号
   - 使用 `make version` 统一更新

2. **文档更新**：
   - MCP 工具变更时同步更新 API 文档
   - 添加新功能时更新使用示例

3. **测试**：
   - 每次发布前测试 MCP Server
   - 测试与主流 AI IDE 的兼容性

4. **依赖更新**：
   - 定期更新 @modelcontextprotocol/sdk
   - 定期更新 yt-dlp
   - 测试新版本兼容性

## 🎉 总结

项目重组完成！新的架构提供了：

- ✅ MCP Server：强大的工具集成
- ✅ Skills：友好的自然语言接口
- ✅ 统一的 Makefile：简化安装和管理
- ✅ MkDocs 文档：专业和易用的文档系统
- ✅ Monorepo：统一维护和版本管理

用户现在可以选择最适合他们的使用方式，同时享受相同的核心功能。