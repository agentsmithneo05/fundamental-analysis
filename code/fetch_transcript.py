#!/usr/bin/env python3
"""
Simple utility to fetch and save YouTube video transcripts.
Usage:
    uv run --with youtube-transcript-api python3 fetch_transcript.py <VIDEO_ID> <OUTPUT_DIR>
"""

import sys
import json
import re
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url_or_id):
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url_or_id)
    return match.group(1) if match else url_or_id

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fetch_transcript.py <VIDEO_ID_OR_URL> [OUTPUT_DIR]")
        sys.exit(1)
        
    raw_input = sys.argv[1]
    video_id = extract_video_id(raw_input)
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(".")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Fetching transcript for Video ID: {video_id}...")
    api = YouTubeTranscriptApi()
    
    try:
        tl = api.list(video_id)
        # Prefer Hindi or English
        t = tl.find_transcript(['hi', 'en'])
        data = t.fetch()
        
        snippets = [{"text": d.text, "start": d.start, "duration": d.duration} for d in data]
        full_text = " ".join([d.text for d in data])
        
        with open(out_dir / "transcript_snippets.json", "w", encoding="utf-8") as f:
            json.dump(snippets, f, indent=2, ensure_ascii=False)
            
        with open(out_dir / "transcript.txt", "w", encoding="utf-8") as f:
            f.write(full_text)
            
        print(f"Success! Saved {len(snippets)} snippets to {out_dir}")
    except Exception as e:
        print(f"Failed to fetch transcript: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
