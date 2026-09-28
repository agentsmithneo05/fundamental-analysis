import os
import json
import time
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi

BASE_DIR = Path("/home/neo/codebase/fundamental_analysis")
PLAYLIST_DIR = BASE_DIR / "playlists" / "basics_of_equity_research"
REPORT_DIR = BASE_DIR / "report"
WEB_DIR = BASE_DIR / "web"

PLAYLIST_DIR.mkdir(parents=True, exist_ok=True)
WEB_DIR.mkdir(parents=True, exist_ok=True)

with open(REPORT_DIR / "playlist_videos.json") as f:
    videos = json.load(f)

print(f"Total videos to process: {len(videos)}")
api = YouTubeTranscriptApi()

success_count = 0
for idx, vid in enumerate(videos, 1):
    vid_id = vid["id"]
    try:
        tl = api.list(vid_id)
        # try hi or en
        t = tl.find_transcript(['hi', 'en'])
        data = t.fetch()
        vid["transcript_status"] = "available"
        vid["snippet_count"] = len(data)
        success_count += 1
    except Exception as e:
        vid["transcript_status"] = "unavailable"
        vid["snippet_count"] = 0

print(f"Transcript availability check complete: {success_count}/{len(videos)} available")
