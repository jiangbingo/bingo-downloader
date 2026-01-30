# 依赖安装指南

Bingo Downloader 需要以下依赖才能正常工作。

## 系统要求

- **Node.js**: >= 18.0.0
- **Python**: 3.8 或更高版本
- **操作系统**: macOS, Linux, Windows

## 核心依赖

### 1. Node.js

**用途**: 运行 MCP Server

**macOS**:
```bash
# 使用 Homebrew
brew install node

# 或使用 nvm（推荐）
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 20
nvm use 20
```

**Linux (Ubuntu/Debian)**:
```bash
# 使用 apt
sudo apt update
sudo apt install nodejs npm

# 或使用 nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 20
nvm use 20
```

**Windows**:
```powershell
# 使用 Chocolatey
choco install nodejs

# 或从官网下载安装包
# https://nodejs.org/
```

**验证安装**:
```bash
node --version  # 应显示 v18.0.0 或更高
```

### 2. Python

**用途**: 运行 yt-dlp

**macOS**:
```bash
# macOS 通常已预装 Python
python3 --version

# 如果未安装
brew install python3
```

**Linux (Ubuntu/Debian)**:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Windows**:
```powershell
# 从官网下载安装包
# https://www.python.org/downloads/

# 或使用 Chocolatey
choco install python
```

**验证安装**:
```bash
python --version  # 应显示 3.8 或更高
```

### 3. yt-dlp

**用途**: 视频下载引擎

**推荐方法: 使用 uv（最快）**

```bash
# 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 使用 uv 安装 yt-dlp
uv pip install yt-dlp
```

**使用 pip**:

```bash
# macOS/Linux
pip3 install yt-dlp

# Windows
pip install yt-dlp

# 如果需要用户权限
pip3 install --user yt-dlp
```

**使用 Homebrew (macOS)**:

```bash
brew install yt-dlp
```

**更新到最新版本**:

```bash
# 使用 uv
uv pip install --upgrade yt-dlp

# 使用 pip
pip3 install --upgrade yt-dlp

# 使用 brew
brew upgrade yt-dlp
```

**验证安装**:
```bash
yt-dlp --version  # 应显示版本号
```

### 4. ffmpeg

**用途**: 音频提取和视频转换

**macOS**:
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian)**:
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows**:

下载预编译的二进制文件：
```bash
# 1. 下载
# https://www.gyan.dev/ffmpeg/builds/

# 2. 解压到 C:\ffmpeg
# 添加到 PATH
setx PATH "%PATH%;C:\ffmpeg\bin"
```

或使用 Chocolatey:
```powershell
choco install ffmpeg
```

**验证安装**:
```bash
ffmpeg -version  # 应显示版本信息
```

## 可选依赖

### 5. aria2（推荐）

**用途**: 多线程下载，加速大文件下载

**macOS**:
```bash
brew install aria2
```

**Linux (Ubuntu/Debian)**:
```bash
sudo apt install aria2
```

**Windows**:
```powershell
choco install aria2
```

**yt-dlp 配置**:
```bash
# ~/.yt-dlp.conf
--external-downloader aria2c
--external-downloader-args "-x 16 -k 1M"
```

### 6. atomicparsley（可选）

**用途**: 写入视频元数据（标题、艺术家等）

**macOS**:
```bash
brew install atomicparsley
```

**Linux (Ubuntu/Debian)**:
```bash
sudo apt install atomicparsley
```

## 系统特定设置

### macOS

权限问题：
```bash
# 如果遇到权限问题，使用 --user
pip3 install --user yt-dlp
```

### Linux

确保 yt-dlp 可执行：
```bash
# 添加到 PATH（在 ~/.bashrc 或 ~/.zshrc）
export PATH=$PATH:~/.local/bin

# 或创建符号链接
sudo ln -s ~/.local/bin/yt-dlp /usr/local/bin/yt-dlp
```

### Windows

将 Python 和 Node.js 添加到 PATH：
1. 打开"系统属性" → "环境变量"
2. 编辑"Path"变量
3. 添加 Python 和 Node.js 的安装路径
4. 重启终端

## 验证所有依赖

运行以下命令确保所有依赖已正确安装：

```bash
# 检查脚本
#!/bin/bash

echo "检查依赖..."

# Node.js
if command -v node &> /dev/null; then
    echo "✓ Node.js: $(node --version)"
else
    echo "✗ Node.js: 未安装"
fi

# Python
if command -v python3 &> /dev/null; then
    echo "✓ Python: $(python3 --version)"
else
    echo "✗ Python: 未安装"
fi

# yt-dlp
if command -v yt-dlp &> /dev/null; then
    echo "✓ yt-dlp: $(yt-dlp --version | head -n 1)"
else
    echo "✗ yt-dlp: 未安装"
fi

# ffmpeg
if command -v ffmpeg &> /dev/null; then
    echo "✓ ffmpeg: $(ffmpeg -version | grep version | head -n 1)"
else
    echo "✗ ffmpeg: 未安装"
fi
```

保存为 `check-deps.sh` 并运行：
```bash
chmod +x check-deps.sh
./check-deps.sh
```

## 故障排除

### 问题：pip 安装失败

**解决方案**: 尝试其他安装方法
```bash
# 使用 uv（推荐）
curl -LsSf https://astral.sh/uv/install.sh | sh
uv pip install yt-dlp

# 或使用 brew（macOS）
brew install yt-dlp

# 或下载预编译二进制
# https://github.com/yt-dlp/yt-dlp/releases
```

### 问题：ffmpeg 找不到

**解决方案**: 确保在 PATH 中
```bash
# 查找 ffmpeg
which ffmpeg

# 如果未找到，添加到 PATH
export PATH=$PATH:/path/to/ffmpeg/bin

# 永久添加（在 ~/.bashrc 或 ~/.zshrc）
echo 'export PATH=$PATH:/path/to/ffmpeg/bin' >> ~/.zshrc
```

### 问题：yt-dlp 权限被拒绝

**解决方案**: 使用 --user 安装或设置权限
```bash
# 使用 --user
pip3 install --user yt-dlp

# 或设置权限
sudo chmod +x ~/.local/bin/yt-dlp
```

## 下一步

安装完成后，继续阅读：
- [MCP Server 安装](mcp-server.md)
- [Skills 安装](skills.md)
- [快速开始](../guide/quick-start.md)