import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

interface DownloadResult {
  success: boolean;
  filePath?: string;
  fileSize?: string;
  duration?: string;
  platform?: string;
  error?: string;
  format?: string;
  quality?: string;
  subtitles?: string;
  formats?: string;
}

// Detect platform from URL
function detectPlatform(url: string): string {
  if (url.includes('youtube.com') || url.includes('youtu.be')) return 'YouTube';
  if (url.includes('bilibili.com')) return 'Bilibili';
  if (url.includes('twitter.com') || url.includes('x.com')) return 'Twitter/X';
  if (url.includes('tiktok.com') || url.includes('douyin.com')) return 'TikTok/Douyin';
  if (url.includes('vimeo.com')) return 'Vimeo';
  if (url.includes('twitch.tv')) return 'Twitch';
  if (url.includes('facebook.com')) return 'Facebook';
  if (url.includes('instagram.com')) return 'Instagram';
  return 'Unknown';
}

// Get quality format string
function getQualityFormat(quality: string): string {
  switch (quality) {
    case '1080':
      return 'bestvideo[height<=1080]+bestaudio/best[height<=1080]';
    case '720':
      return 'bestvideo[height<=720]+bestaudio/best[height<=720]';
    case '480':
      return 'bestvideo[height<=480]+bestaudio/best[height<=480]';
    case '360':
      return 'bestvideo[height<=360]+bestaudio/best[height<=360]';
    default:
      return 'bestvideo+bestaudio/best';
  }
}

// Build yt-dlp command with common options
function buildCommand(options: {
  url: string;
  format?: string;
  audio?: boolean;
  audioFormat?: string;
  audioQuality?: string;
  subs?: boolean;
  subLangs?: string;
  cookiesBrowser?: string;
  downloadPath?: string;
}): string {
  const {
    url,
    format,
    audio = false,
    audioFormat = 'mp3',
    audioQuality = 'best',
    subs = false,
    subLangs = 'all',
    cookiesBrowser = 'chrome',
    downloadPath = '~/Downloads/yt-dlp',
  } = options;

  let cmd = `yt-dlp -P "${downloadPath}"`;

  // Add format
  if (audio) {
    cmd += ' -x';
    if (audioFormat) {
      cmd += ` --audio-format ${audioFormat}`;
    }
    if (audioQuality && audioQuality !== 'best') {
      cmd += ` --audio-quality ${audioQuality}`;
    }
  } else if (format) {
    cmd += ` -f "${format}"`;
  }

  // Add subtitles
  if (subs) {
    cmd += ` --write-subs --sub-langs ${subLangs} --embed-subs`;
  }

  // Add cookies
  if (cookiesBrowser) {
    cmd += ` --cookies-from-browser ${cookiesBrowser}`;
  }

  // Add URL
  cmd += ` "${url}"`;

  return cmd;
}

// Download video
export async function downloadVideo(
  url: string,
  quality: string = 'best',
  cookiesBrowser: string = 'chrome',
  downloadPath?: string
): Promise<DownloadResult> {
  const platform = detectPlatform(url);
  const qualityFormat = getQualityFormat(quality);

  const command = buildCommand({
    url,
    format: qualityFormat,
    cookiesBrowser,
    downloadPath,
  });

  try {
    const { stdout, stderr } = await execAsync(command, {
      maxBuffer: 10 * 1024 * 1024, // 10MB buffer
    });

    // Parse output to extract file info
    const filePathMatch = stdout.match(/\[download\] Destination: (.+)/);
    const sizeMatch = stdout.match(/\[download\] (\d+\.?\d*% of \d+\.?\d*[A-Z]+)/);

    return {
      success: true,
      filePath: filePathMatch ? filePathMatch[1] : 'Download completed',
      fileSize: sizeMatch ? sizeMatch[1] : 'Unknown',
      platform,
    };
  } catch (error: any) {
    const errorMsg = error.stderr || error.message || 'Unknown error';
    
    // Check if yt-dlp is installed
    if (errorMsg.includes('command not found') || errorMsg.includes('not recognized')) {
      return {
        success: false,
        error: 'yt-dlp is not installed. Install with: pip install yt-dlp',
      };
    }

    return {
      success: false,
      error: errorMsg,
    };
  }
}

// Extract audio
export async function extractAudio(
  url: string,
  format: string = 'mp3',
  quality: string = 'best',
  cookiesBrowser: string = 'chrome'
): Promise<DownloadResult> {
  const platform = detectPlatform(url);

  const command = buildCommand({
    url,
    audio: true,
    audioFormat: format,
    audioQuality: quality,
    cookiesBrowser,
  });

  try {
    const { stdout, stderr } = await execAsync(command, {
      maxBuffer: 10 * 1024 * 1024,
    });

    const filePathMatch = stdout.match(/\[download\] Destination: (.+)/);
    const sizeMatch = stdout.match(/\[download\] (\d+\.?\d*% of \d+\.?\d*[A-Z]+)/);

    return {
      success: true,
      filePath: filePathMatch ? filePathMatch[1] : 'Extraction completed',
      fileSize: sizeMatch ? sizeMatch[1] : 'Unknown',
      format,
      platform,
    };
  } catch (error: any) {
    const errorMsg = error.stderr || error.message || 'Unknown error';
    
    // Check for ffmpeg
    if (errorMsg.includes('ffmpeg') || errorMsg.includes('FFmpeg')) {
      return {
        success: false,
        error: 'ffmpeg is not installed. Install with: brew install ffmpeg (macOS) or sudo apt install ffmpeg (Linux)',
      };
    }

    return {
      success: false,
      error: errorMsg,
    };
  }
}

// Download with subtitles
export async function downloadWithSubs(
  url: string,
  quality: string = 'best',
  subLangs: string = 'all',
  cookiesBrowser: string = 'chrome'
): Promise<DownloadResult & { subtitles?: string }> {
  const platform = detectPlatform(url);
  const qualityFormat = getQualityFormat(quality);

  const command = buildCommand({
    url,
    format: qualityFormat,
    subs: true,
    subLangs,
    cookiesBrowser,
  });

  try {
    const { stdout, stderr } = await execAsync(command, {
      maxBuffer: 10 * 1024 * 1024,
    });

    const filePathMatch = stdout.match(/\[download\] Destination: (.+)/);
    const subsMatch = stdout.match(/\[download\] Downloading video subtitles (.+)/);

    return {
      success: true,
      filePath: filePathMatch ? filePathMatch[1] : 'Download completed',
      subtitles: subsMatch ? subsMatch[1] : 'Embedded subtitles',
      quality,
      platform,
    };
  } catch (error: any) {
    return {
      success: false,
      error: error.stderr || error.message || 'Unknown error',
    };
  }
}

// List formats
export async function listFormats(
  url: string,
  cookiesBrowser: string = 'chrome'
): Promise<DownloadResult & { formats?: string }> {
  const command = buildCommand({
    url,
    cookiesBrowser,
  }).replace(/-f .+?\s/, '-F '); // Replace format with -F to list

  try {
    const { stdout } = await execAsync(command, {
      maxBuffer: 10 * 1024 * 1024,
    });

    // Parse and format the output
    const lines = stdout.split('\n');
    let formattedFormats = '';
    
    lines.forEach((line: string) => {
      if (line.match(/^\s*\d+/)) {
        formattedFormats += line + '\n';
      }
    });

    return {
      success: true,
      formats: formattedFormats || stdout,
    };
  } catch (error: any) {
    return {
      success: false,
      error: error.stderr || error.message || 'Unknown error',
    };
  }
}