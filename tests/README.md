# 测试框架文档

## 概述

本项目为 Bingo Video Downloader 提供了完整的测试框架，涵盖 MCP Server (TypeScript) 和 Web API (Python)。

## 测试框架结构

### TypeScript 测试 (MCP Server)
- **测试框架**: Vitest
- **覆盖率工具**: @vitest/coverage-v8
- **测试文件**: `/mcp/src/downloader.test.ts`

### Python 测试 (Web API)
- **测试框架**: pytest
- **异步测试**: pytest-asyncio
- **HTTP 客户端**: httpx (FastAPI TestClient)
- **覆盖率工具**: pytest-cov
- **测试文件**:
  - `/web/backend/tests/conftest.py` - 测试配置和 fixtures
  - `/web/backend/tests/test_api.py` - API 端点测试

### Python 测试 (Skill)
- **测试框架**: pytest
- **测试文件**: `/skill/tests/test_download.py`

## 运行测试

### 使用 Makefile (推荐)

```bash
# 运行所有测试
make test

# 仅运行 MCP Server 测试
make test-mcp

# 仅运行 Web API 测试
make test-web

# 运行所有测试并生成覆盖率报告
make test-coverage

# MCP Server 测试覆盖率
make test-mcp-coverage

# Web API 测试覆盖率
make test-web-coverage
```

### 直接使用命令

#### MCP Server (TypeScript)

```bash
cd mcp

# 运行测试
npm test

# 监听模式（文件变化自动重新运行）
npm run test:watch

# 生成覆盖率报告
npm run test:coverage

# 启动测试 UI
npm run test:ui
```

#### Web API (Python)

```bash
cd web/backend

# 激活虚拟环境
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate  # Windows

# 运行测试
pytest tests/ -v

# 运行测试并生成覆盖率报告
pytest tests/ -v --cov=. --cov-report=html --cov-report=term

# 查看覆盖率报告
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

## 测试覆盖

### MCP Server 测试 (51 个测试用例)

- ✅ **平台检测** (6 个测试)
  - YouTube URL 检测
  - Bilibili URL 检测
  - Twitter/X URL 检测
  - TikTok/Douyin URL 检测
  - Vimeo URL 检测
  - 未知平台检测

- ✅ **URL 验证** (4 个测试)
  - 空 URL 拒绝
  - 危险字符检测
  - 非 HTTP 协议拒绝
  - 有效 URL 接受

- ✅ **路径验证** (2 个测试)
  - 默认下载路径
  - 自定义下载路径

- ✅ **质量选择** (2 个测试)
  - 1080p 格式
  - 720p 格式

- ✅ **音频提取** (2 个测试)
  - 正确的音频格式
  - 不同音频格式

- ✅ **字幕下载** (2 个测试)
  - 启用字幕下载
  - 自定义字幕语言

- ✅ **格式列表** (1 个测试)
  - 列出可用格式

- ✅ **Cookie 处理** (2 个测试)
  - 默认 Chrome cookies
  - 不同浏览器 cookies

### Web API 测试

#### 健康检查端点
- ✅ `/health` 端点状态
- ✅ `/` 根端点 HTML 返回

#### 下载 API
- ✅ 成功启动下载
- ✅ 无效 URL 处理
- ✅ 获取下载进度
- ✅ 不存在的任务处理
- ✅ 取消下载
- ✅ 列出所有任务
- ✅ Cookie 授权
- ✅ Cookie 状态查询

#### 历史 API
- ✅ 获取下载历史
- ✅ 带限制的历史查询
- ✅ 按平台过滤
- ✅ 清除历史
- ✅ 删除单条记录

#### 统计 API
- ✅ 获取下载统计
- ✅ 按平台分组统计

#### 格式 API
- ✅ 列出可用格式
- ✅ 缺少 URL 参数验证

#### 输入验证
- ✅ 下载请求验证
- ✅ 质量参数验证
- ✅ 历史限制验证

#### 错误处理
- ✅ yt-dlp 未安装处理
- ✅ 下载失败处理

#### 并发测试
- ✅ 多个同时下载

### Skill 测试

- ✅ 平台检测
- ✅ 播放列表检测
- ✅ 智能格式选择
- ✅ 下载历史管理
- ✅ BingoDownloader 类

## Mock 策略

### TypeScript
- 使用 `vi.mock()` mock `child_process` 模块
- 避免 actual `yt-dlp` 调用
- 模拟成功和失败场景

### Python
- 使用 `unittest.mock.patch` mock 外部依赖
- Mock `BingoDownloader` 类
- Mock `DownloadHistory` 类
- Mock `subprocess` 调用

## 覆盖率报告

### MCP Server
- 报告位置: `/mcp/coverage/`
- 查看方式: 在浏览器中打开 `mcp/coverage/index.html`

### Web API
- 报告位置: `/web/backend/htmlcov/`
- 查看方式: 在浏览器中打开 `web/backend/htmlcov/index.html`

## 测试独立性

所有测试都设计为独立运行，不依赖外部服务：
- ✅ Mock 所有 yt-dlp 调用
- ✅ Mock 数据库操作
- ✅ 使用临时目录进行文件操作
- ✅ 独立的测试隔离

## 持续集成

测试可以通过以下方式集成到 CI/CD 流程：

```yaml
# .github/workflows/test.yml 示例
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '20'
      - name: Install MCP dependencies
        run: cd mcp && npm install
      - name: Run MCP tests
        run: make test-mcp
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Install Web dependencies
        run: make install-web
      - name: Run Web tests
        run: make test-web
```

## 开发指南

### 添加新测试

#### TypeScript
```typescript
import { describe, it, expect, vi } from 'vitest';

describe('New Feature', () => {
  it('should do something', () => {
    // Arrange
    const input = 'test';

    // Act
    const result = functionUnderTest(input);

    // Assert
    expect(result).toBe('expected');
  });
});
```

#### Python
```python
def test_new_feature(client):
    """Test new feature"""
    response = client.get("/api/new-endpoint")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
```

## 故障排除

### MCP 测试失败
```bash
# 清理并重新安装依赖
cd mcp
rm -rf node_modules package-lock.json
npm install
npm test
```

### Web 测试失败
```bash
# 重新创建虚拟环境
cd web/backend
rm -rf .venv
uv venv .venv
uv pip install -r requirements.txt
pytest tests/ -v
```

## 测试最佳实践

1. **独立性**: 每个测试应该独立运行
2. **清晰性**: 测试名称应该清楚描述测试内容
3. **快速性**: 使用 mock 避免慢速操作
4. **可维护性**: 在 `conftest.py` 中共享 fixtures
5. **覆盖率**: 目标是 >80% 的代码覆盖率

## 贡献指南

提交代码前请确保：
1. 所有测试通过: `make test`
2. 代码覆盖率不降低: `make test-coverage`
3. 新功能包含测试
4. 测试清晰且易于理解

## 资源

- [Vitest 文档](https://vitest.dev/)
- [pytest 文档](https://docs.pytest.org/)
- [FastAPI 测试文档](https://fastapi.tiangolo.com/tutorial/testing/)
