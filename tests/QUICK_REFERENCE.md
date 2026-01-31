# 测试框架快速参考

## 快速开始

### 运行所有测试
```bash
make test
```

### MCP Server 测试 (TypeScript + Vitest)
```bash
# 运行测试
cd mcp && npm test

# 监听模式
cd mcp && npm run test:watch

# 覆盖率报告
cd mcp && npm run test:coverage

# UI 模式
cd mcp && npm run test:ui
```

### Web API 测试 (Python + pytest)
```bash
# 运行测试
cd web/backend && .venv/bin/pytest tests/ -v

# 覆盖率报告
cd web/backend && .venv/bin/pytest tests/ -v --cov=. --cov-report=html
```

## 测试结果

### MCP Server ✅
- **测试文件**: 2 passed
- **测试用例**: 42 passed
- **覆盖率**: ~70%
- **运行时间**: 378ms

### Web API 📝
- 测试框架已就绪
- 需要修复相对导入问题

## 关键文件

| 组件 | 配置文件 | 测试文件 |
|------|---------|---------|
| MCP Server | `/mcp/vitest.config.ts` | `/mcp/src/downloader.test.ts` |
| Web API | `/web/backend/tests/conftest.py` | `/web/backend/tests/test_api.py` |
| Python Skill | - | `/skill/tests/test_download.py` |

## Mock 策略

### TypeScript
```typescript
// Mock child_process
vi.mock('child_process', () => ({
  spawn: (...args: any[]) => mockSpawn(...args),
}));
```

### Python
```python
# Mock dependencies
@patch('api.download.BingoDownloader')
def test_download(mock_downloader):
    # test code
```

## 测试覆盖

### ✅ MCP Server (42 tests)
- 平台检测 (6)
- URL 验证 (4)
- 路径验证 (2)
- 质量选择 (2)
- 音频提取 (2)
- 字幕下载 (2)
- 格式列表 (1)
- Cookie 处理 (2)
- 更多...

### 📝 Web API (规划中)
- 健康检查
- 下载 API
- 历史 API
- 统计 API
- 格式 API
- 输入验证
- 错误处理

## 故障排除

### MCP 测试失败
```bash
cd mcp
rm -rf node_modules package-lock.json
npm install
npm test
```

### Web 测试失败
```bash
cd web/backend
rm -rf .venv
uv venv .venv
uv pip install -r requirements.txt
pytest tests/ -v
```

## 文档
- 详细文档: `/tests/README.md`
- 设置摘要: `/tests/TESTING_SUMMARY.md`
