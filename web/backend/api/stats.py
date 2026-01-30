"""
Bingo Downloader Web - Statistics API Endpoints
"""
from fastapi import APIRouter
from ..models import StatsResponse, ApiResponse

router = APIRouter(prefix="/api/stats", tags=["stats"])


@router.get("/", response_model=StatsResponse)
async def get_stats():
    """Get download statistics"""
    from ..core import DownloadHistory, CORE_AVAILABLE

    if not CORE_AVAILABLE:
        return StatsResponse(
            total_downloads=0,
            successful_downloads=0,
            failed_downloads=0,
            success_rate=0.0,
            total_bytes=0,
            total_size_human="0 B",
            by_platform={}
        )

    history_db = DownloadHistory()
    stats = history_db.get_statistics()

    return StatsResponse(**stats)


@router.get("/by-platform", response_model=dict)
async def get_stats_by_platform():
    """Get statistics grouped by platform"""
    from ..core import DownloadHistory, CORE_AVAILABLE

    if not CORE_AVAILABLE:
        return {}

    history_db = DownloadHistory()
    stats = history_db.get_statistics()

    return stats.get("by_platform", {})
