# 日志系统配置文档

Bingo Downloader 使用统一的日志系统，为 TypeScript (MCP Server) 和 Python (Web Backend & CLI) 提供结构化日志记录。

## 概述

日志系统提供以下功能：

- **结构化日志**：JSON 格式的结构化输出，便于解析和分析
- **日志级别**：支持 DEBUG, INFO, WARN, ERROR 等多个级别
- **文件轮转**：按日期自动轮转日志文件
- **环境适配**：开发环境彩色输出，生产环境 JSON 格式
- **性能优化**：TypeScript 使用高性能的 Pino 库

---

## TypeScript (MCP Server) 日志配置

### 日志文件位置

- **开发环境**：仅控制台输出（彩色格式化）
- **生产环境**：
  - 普通日志：`{LOG_FILE}` （默认未设置，可通过环境变量配置）
  - 错误日志：`{LOG_FILE}-error.log`

### 环境变量

| 变量名 | 说明 | 默认值 | 可选值 |
|--------|------|--------|--------|
| `NODE_ENV` | 运行环境 | `development` | `development`, `production` |
| `LOG_LEVEL` | 日志级别 | `DEBUG` (开发), `INFO` (生产) | `debug`, `info`, `warn`, `error`, `silent` |
| `LOG_FILE` | 日志文件路径 | 未设置 | 任意文件路径（如：`/var/log/bingo-downloader.log`） |

### 使用示例

```typescript
import { logger, createLogger, logDownloadStart } from './logger.js';

// 使用默认 logger
logger.info('Server started');
logger.error({ error: err }, 'Database connection failed');

// 创建带上下文的子 logger
const dbLogger = createLogger('database');
dbLogger.debug('Query executed', { query: 'SELECT * FROM users' });

// 使用便捷函数
logDownloadStart(url, { platform: 'YouTube', quality: '1080p' });
```

### 日志级别说明

- **DEBUG**：详细的调试信息（仅开发环境）
- **INFO**：一般信息（下载开始/完成、服务器启动等）
- **WARN**：警告信息（可重试的失败、降级功能等）
- **ERROR**：错误信息（下载失败、连接错误等）
- **SILENT**：完全静默（不推荐）

---

## Python 日志配置

### 日志文件位置

默认日志目录：`~/.bingo-downloader/logs/`

| 文件 | 说明 |
|------|------|
| `{name}.log` | 普通日志（INFO 及以上级别） |
| `{name}-error.log` | 错误日志（仅 ERROR 级别） |
| `download.log` | CLI 下载脚本日志 |
| `web.log` | Web 后端日志 |

### 日志轮转

- **轮转周期**：每天午夜
- **保留天数**：30 天
- **编码格式**：UTF-8

### 环境变量

| 变量名 | 说明 | 默认值 | 可选值 |
|--------|------|--------|--------|
| `LOG_LEVEL` | 日志级别 | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |
| `LOG_DIR` | 日志目录 | `~/.bingo-downloader/logs/` | 任意目录路径 |

### 使用示例

```python
from utils.logger import BingoLogger, log_download_start, log_download_success, log_download_error

# 获取 logger 实例
logger = BingoLogger.get_logger(__name__, log_file='my_module')

# 记录日志
logger.info('Processing started')
logger.debug('Debug information', extra_key='value')
logger.warning('Warning message')
logger.error('Error occurred', exc_info=True)

# 使用便捷函数
log_download_start(logger, url, platform, quality='1080p')
log_download_success(logger, url, file_path='/path/to/file.mp4', duration=45.2)
log_download_error(logger, url, error, duration=10.5)
```

---

## 日志格式

### TypeScript 开发环境（彩色格式化）

```
[2026-01-31 16:30:45] [INFO] (index) - Bingo Downloader MCP Server running on stdio
[2026-01-31 16:30:46] [DEBUG] (downloader) - Download started | URL: https://youtube.com/watch?v=xxx | Platform: YouTube
```

### TypeScript 生产环境（JSON 格式）

```json
{
  "level": "info",
  "time": "2026-01-31T16:30:45.123Z",
  "context": "index",
  "msg": "Bingo Downloader MCP Server running on stdio"
}
```

### Python 控制台输出（彩色）

```
2026-01-31 16:30:45 [INFO] bingo_downloader - Download started | URL: https://youtube.com/watch?v=xxx | Platform: YouTube
```

### Python 文件输出（详细格式）

```
2026-01-31 16:30:45 [INFO] bingo_downloader [download.py:887] - Download started | URL: https://youtube.com/watch?v=xxx | Platform: YouTube
```

---

## 开发环境配置

### MCP Server (TypeScript)

```bash
# 开发环境（默认）
export NODE_ENV=development
export LOG_LEVEL=debug

# 启动开发服务器
npm run dev
```

### Web 后端 (Python)

```bash
# 设置日志级别为 DEBUG
export LOG_LEVEL=DEBUG

# 启动开发服务器
python -m web.backend.main
```

---

## 生产环境配置

### MCP Server (TypeScript)

```bash
# 生产环境
export NODE_ENV=production
export LOG_LEVEL=info
export LOG_FILE=/var/log/bingo-downloader/mcp.log

# 启动服务
npm start
```

### Web 后端 (Python)

```bash
# 生产环境
export LOG_LEVEL=INFO

# 使用 systemd/supervisor 启动
python -m web.backend.main
```

---

## 日志分析

### 使用 jq 分析 JSON 日志

```bash
# 统计错误数量
cat /var/log/bingo-downloader/mcp.log | jq 'select(.level == "error")' | wc -l

# 查找特定 URL 的下载记录
cat /var/log/bingo-downloader/mcp.log | jq 'select(.url == "https://youtube.com/watch?v=xxx")'

# 统计各平台的下载次数
cat /var/log/bingo-downloader/mcp.log | jq -r '.platform' | sort | uniq -c
```

### 查看 Python 日志

```bash
# 查看最近错误
tail -f ~/.bingo-downloader/logs/download-error.log

# 搜索特定关键词
grep "youtube.com" ~/.bingo-downloader/logs/download.log

# 查看最近 100 行日志
tail -n 100 ~/.bingo-downloader/logs/download.log
```

---

## 性能考虑

### TypeScript (Pino)

- **性能优化**：Pino 是最快的 Node.js 日志库之一
- **异步写入**：生产环境使用异步文件写入，不阻塞主线程
- **低开销**：结构化日志开销最小，适合高并发场景

### Python (logging)

- **文件轮转**：使用 TimedRotatingFileHandler，自动管理日志文件
- **多进程安全**：每个进程独立写入，避免锁竞争
- **内存控制**：日志缓冲区限制大小，避免内存占用过高

---

## 故障排查

### 日志未生成

1. 检查日志目录权限
2. 检查环境变量是否正确设置
3. 查看控制台错误信息

### 日志级别不生效

1. 确认环境变量拼写正确
2. 重启服务以应用新配置
3. 检查是否有其他配置覆盖

### 磁盘空间不足

1. 日志自动轮转，保留 30 天
2. 手动清理旧日志：`rm ~/.bingo-downloader/logs/*.log.*`
3. 调整保留天数（修改 `backupCount` 参数）

---

## 最佳实践

### 1. 选择合适的日志级别

- **DEBUG**：开发调试，不包含敏感信息
- **INFO**：重要操作、状态变化
- **WARN**：可恢复的异常、降级功能
- **ERROR**：需要关注的错误

### 2. 使用结构化数据

```typescript
// 推荐
logger.info({ userId: '123', action: 'login' }, 'User logged in');

// 不推荐
logger.info('User 123 logged in');
```

### 3. 记录关键操作的开始和结束

```typescript
const startTime = Date.now();
try {
  logger.info({ type: 'operation_start' }, 'Starting operation');
  // ... 执行操作
  const duration = Date.now() - startTime;
  logger.info({ type: 'operation_success', duration }, 'Operation completed');
} catch (error) {
  const duration = Date.now() - startTime;
  logger.error({ type: 'operation_error', error, duration }, 'Operation failed');
}
```

### 4. 避免记录敏感信息

- 不要记录密码、令牌、密钥
- 对 URL 中的敏感参数进行脱敏
- 限制 PII（个人身份信息）的记录

---

## 相关文件

- **TypeScript**：
  - `/mcp/src/logger.ts` - 日志配置
  - `/mcp/src/index.ts` - MCP Server 主入口
  - `/mcp/src/downloader.ts` - 下载器实现
  - `/mcp/src/history.ts` - 历史记录管理

- **Python**：
  - `/web/backend/utils/logger.py` - 日志配置
  - `/web/backend/main.py` - Web 后端主入口
  - `/skill/scripts/download.py` - CLI 下载脚本

---

## 版本历史

- **v1.0.0** (2026-01-31)：初始实现
  - TypeScript 使用 Pino
  - Python 使用标准 logging 模块
  - 支持环境变量配置
  - 自动日志轮转
