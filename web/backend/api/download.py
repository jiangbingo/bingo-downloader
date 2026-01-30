"""
Bingo Downloader Web - Download API Endpoints
"""
import asyncio
import uuid
from typing import Dict
from fastapi import APIRouter, HTTPException, BackgroundTasks
from ..models import DownloadRequest, DownloadProgress, ApiResponse

router = APIRouter(prefix="/api/download", tags=["download"])

# In-memory task storage (in production, use Redis or similar)
active_tasks: Dict[str, DownloadProgress] = {}
task_locks: Dict[str, asyncio.Lock] = {}


async def run_download(task_id: str, request: DownloadRequest):
    """Run download in background"""
    try:
        from ..core import VideoDownloader, CORE_AVAILABLE

        if not CORE_AVAILABLE:
            active_tasks[task_id].status = "failed"
            active_tasks[task_id].error = "Core modules not available"
            return

        # Update status to downloading
        active_tasks[task_id].status = "downloading"
        active_tasks[task_id].progress = 0.0

        # Create downloader instance
        downloader = VideoDownloader()

        # Run download (this will be updated to support progress tracking)
        result = await asyncio.to_thread(
            downloader.download,
            request.url,
            quality=request.quality,
            audio_only=(request.format_type == "audio"),
            audio_format=request.audio_format if request.format_type == "audio" else None,
            subtitles=request.subtitles,
            sub_langs=request.sub_langs,
            cookies_browser=request.cookies_browser,
            download_path=request.download_path
        )

        if result.get("success"):
            active_tasks[task_id].status = "completed"
            active_tasks[task_id].progress = 100.0
            active_tasks[task_id].filename = result.get("filename")
        else:
            active_tasks[task_id].status = "failed"
            active_tasks[task_id].error = result.get("error", "Unknown error")

    except Exception as e:
        active_tasks[task_id].status = "failed"
        active_tasks[task_id].error = str(e)


@router.post("/start", response_model=ApiResponse)
async def start_download(request: DownloadRequest, background_tasks: BackgroundTasks):
    """Start a new download task"""
    task_id = str(uuid.uuid4())

    # Initialize task
    active_tasks[task_id] = DownloadProgress(
        task_id=task_id,
        status="pending",
        progress=0.0
    )

    # Start download in background
    background_tasks.add_task(run_download, task_id, request)

    return ApiResponse(
        success=True,
        message="Download started",
        data={"task_id": task_id}
    )


@router.get("/progress/{task_id}", response_model=DownloadProgress)
async def get_progress(task_id: str):
    """Get download progress"""
    if task_id not in active_tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return active_tasks[task_id]


@router.post("/cancel/{task_id}", response_model=ApiResponse)
async def cancel_download(task_id: str):
    """Cancel a download task"""
    if task_id not in active_tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    # Mark as cancelled (actual cancellation will be implemented)
    active_tasks[task_id].status = "failed"
    active_tasks[task_id].error = "Cancelled by user"

    return ApiResponse(
        success=True,
        message="Download cancelled"
    )


@router.get("/tasks", response_model=Dict[str, DownloadProgress])
async def list_tasks():
    """List all active tasks"""
    return active_tasks
