"""
Bingo Downloader Web - Main Entry Point
FastAPI application for video download web interface
"""
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn

from .config import (
    HOST, PORT, RELOAD, CORS_ORIGINS,
    BASE_DIR, DOWNLOAD_DIR,
)
from .api import download_router, history_router, stats_router, formats_router
from .models import ApiResponse

# Create FastAPI app
app = FastAPI(
    title="Bingo Downloader Web",
    description="Web interface for video downloader supporting 1000+ websites",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files and templates
static_dir = BASE_DIR / "web" / "frontend" / "static"
templates_dir = BASE_DIR / "web" / "frontend" / "templates"

app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
templates = Jinja2Templates(directory=str(templates_dir))

# Include API routers
app.include_router(download_router)
app.include_router(history_router)
app.include_router(stats_router)
app.include_router(formats_router)


# Root route
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Render main page"""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Bingo Downloader",
            "supported_platforms": [
                {"name": "YouTube", "icon": "youtube", "url": "youtube.com"},
                {"name": "Bilibili", "icon": "bilibili", "url": "bilibili.com"},
                {"name": "Twitter/X", "icon": "x", "url": "twitter.com"},
                {"name": "TikTok", "icon": "tiktok", "url": "tiktok.com"},
                {"name": "Vimeo", "icon": "vimeo", "url": "vimeo.com"},
            ]
        }
    )


# Health check
@app.get("/health", response_model=ApiResponse)
async def health_check():
    """Health check endpoint"""
    return ApiResponse(
        success=True,
        message="Bingo Downloader Web is running",
        data={
            "download_dir": str(DOWNLOAD_DIR),
            "version": "1.0.0"
        }
    )


# Run server
def run():
    """Run the development server"""
    uvicorn.run(
        "web.backend.main:app",
        host=HOST,
        port=PORT,
        reload=RELOAD
    )


if __name__ == "__main__":
    run()
