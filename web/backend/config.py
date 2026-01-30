"""
Bingo Downloader Web - Configuration
"""
from pathlib import Path
from typing import Optional
import os

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SKILL_SCRIPTS_DIR = BASE_DIR / "skill" / "scripts"
DOWNLOAD_DIR = Path.home() / "Downloads" / "yt-dlp"

# Database
DATABASE_PATH = Path.home() / ".yt-dlp-history.db"

# Server config
HOST: str = os.getenv("HOST", "0.0.0.0")
PORT: int = int(os.getenv("PORT", "8000"))
RELOAD: bool = os.getenv("RELOAD", "true").lower() == "true"

# CORS
CORS_ORIGINS: list[str] = os.getenv(
    "CORS_ORIGINS",
    "http://localhost:8000,http://localhost:3000,http://127.0.0.1:8000"
).split(",")

# Download settings
DEFAULT_QUALITY: str = os.getenv("DEFAULT_QUALITY", "1080")
DEFAULT_COOKIES_BROWSER: str = os.getenv("DEFAULT_COOKIES_BROWSER", "chrome")
MAX_FILE_SIZE_WARNING: int = int(os.getenv("MAX_FILE_SIZE_WARNING", "2147483648"))  # 2GB

# Retry settings
MAX_RETRY_ATTEMPTS: int = int(os.getenv("MAX_RETRY_ATTEMPTS", "3"))
INITIAL_RETRY_DELAY: int = int(os.getenv("INITIAL_RETRY_DELAY", "5"))
RETRY_BACKOFF_MULTIPLIER: int = int(os.getenv("RETRY_BACKOFF_MULTIPLIER", "2"))

# Ensure directories exist
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

# Platform detection patterns
PLATFORM_PATTERNS = {
    "YouTube": ["youtube.com", "youtu.be"],
    "Bilibili": ["bilibili.com"],
    "Twitter/X": ["twitter.com", "x.com"],
    "TikTok": ["tiktok.com", "douyin.com"],
    "Vimeo": ["vimeo.com"],
    "Twitch": ["twitch.tv"],
}


def detect_platform(url: str) -> Optional[str]:
    """Detect platform from URL"""
    for platform, patterns in PLATFORM_PATTERNS.items():
        if any(pattern in url.lower() for pattern in patterns):
            return platform
    return "Unknown"
