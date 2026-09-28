import json
from pathlib import Path

BASE_DIR = Path("/home/neo/codebase/fundamental_analysis")
CATALOG_PATH = BASE_DIR / "web" / "catalog.json"
OUTPUT_HTML = BASE_DIR / "web" / "index.html"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog_data = json.load(f)

# Embed catalog data directly as a JS constant so it works seamlessly on file:// protocol
catalog_json_str = json.dumps(catalog_data, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Institutional Equity Research & Fundamental Analysis | 32-Yr Senior Analyst Masterclass</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-dark: #090D16;
      --bg-card: #111726;
      --bg-card-hover: #162035;
      --bg-card-subtle: #19243C;
      --border-color: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(16, 185, 129, 0.3);
      --text-main: #F3F4F6;
      --text-muted: #9CA3AF;
      --text-dim: #6B7280;
      --accent-emerald: #10B981;
      --accent-emerald-glow: rgba(16, 185, 129, 0.2);
      --accent-amber: #F59E0B;
      --accent-amber-glow: rgba(245, 158, 11, 0.2);
      --accent-cyan: #06B6D4;
      --accent-indigo: #6366F1;
      --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.6;
      height: 100vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
    }}

    /* Scrollbars */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: rgba(0, 0, 0, 0.2);
    }}
    ::-webkit-scrollbar-thumb {{
      background: rgba(255, 255, 255, 0.15);
      border-radius: 3px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: rgba(255, 255, 255, 0.3);
    }}

    /* Top Navigation Bar */
    header.top-bar {{
      height: 70px;
      background: rgba(17, 23, 38, 0.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      z-index: 50;
      flex-shrink: 0;
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .brand-icon {{
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, var(--accent-emerald), var(--accent-cyan));
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #000;
      font-weight: 800;
      font-size: 20px;
      box-shadow: 0 0 16px var(--accent-emerald-glow);
    }}

    .brand-title h1 {{
      font-size: 17px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #FFF;
    }}

    .brand-title p {{
      font-size: 11.5px;
      color: var(--accent-emerald);
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }}

    .header-center {{
      flex: 1;
      max-width: 480px;
      margin: 0 24px;
      position: relative;
    }}

    .search-input {{
      width: 100%;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 9px 14px 9px 38px;
      color: #FFF;
      font-size: 13px;
      font-family: var(--font-sans);
      outline: none;
      transition: all 0.2s;
    }}

    .search-input:focus {{
      border-color: var(--accent-emerald);
      background: rgba(255, 255, 255, 0.08);
      box-shadow: 0 0 12px var(--accent-emerald-glow);
    }}

    .search-icon {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      pointer-events: none;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 7px 14px;
      border-radius: 7px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      transition: all 0.2s;
      text-decoration: none;
    }}

    .btn-secondary {{
      background: rgba(255, 255, 255, 0.06);
      color: var(--text-main);
      border-color: var(--border-color);
    }}
    .btn-secondary:hover {{
      background: rgba(255, 255, 255, 0.12);
      border-color: rgba(255, 255, 255, 0.2);
    }}

    .btn-primary {{
      background: var(--accent-emerald);
      color: #06281E;
      font-weight: 700;
    }}
    .btn-primary:hover {{
      background: #0ea372;
      box-shadow: 0 0 14px var(--accent-emerald-glow);
    }}

    /* Main Container Layout */
    .app-container {{
      display: flex;
      flex: 1;
      height: calc(100vh - 70px);
      overflow: hidden;
    }}

    /* Sidebar Navigation */
    aside.sidebar {{
      width: 360px;
      background: var(--bg-card);
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      flex-shrink: 0;
    }}

    .sidebar-header {{
      padding: 16px;
      border-bottom: 1px solid var(--border-color);
      background: rgba(0, 0, 0, 0.15);
    }}

    .sidebar-header h2 {{
      font-size: 13.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--text-muted);
      margin-bottom: 8px;
    }}

    .filter-pills {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 4px;
    }}

    .pill {{
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 11px;
      font-weight: 600;
      white-space: nowrap;
      cursor: pointer;
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-muted);
      border: 1px solid var(--border-color);
      transition: all 0.2s;
    }}
    .pill.active, .pill:hover {{
      background: var(--accent-emerald);
      color: #000;
      border-color: var(--accent-emerald);
    }}

    .chapters-list {{
      flex: 1;
      overflow-y: auto;
      padding: 10px;
    }}

    .module-group {{
      margin-bottom: 16px;
    }}

    .module-title {{
      font-size: 11px;
      font-weight: 700;
      color: var(--accent-amber);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 6px 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .chapter-card {{
      padding: 11px 12px;
      border-radius: 8px;
      margin-bottom: 5px;
      cursor: pointer;
      border: 1px solid transparent;
      background: rgba(255, 255, 255, 0.02);
      transition: all 0.2s;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .chapter-card:hover {{
      background: var(--bg-card-hover);
      border-color: var(--border-color);
      transform: translateX(2px);
    }}

    .chapter-card.active {{
      background: rgba(16, 185, 129, 0.08);
      border-color: var(--accent-emerald);
      box-shadow: inset 3px 0 0 var(--accent-emerald);
    }}

    .chapter-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }}

    .chapter-number {{
      font-family: var(--font-mono);
      font-size: 10.5px;
      font-weight: 600;
      color: var(--accent-cyan);
      background: rgba(6, 182, 212, 0.1);
      padding: 1px 6px;
      border-radius: 4px;
    }}

    .chapter-badge {{
      font-size: 10px;
      font-weight: 600;
      padding: 1px 6px;
      border-radius: 4px;
    }}
    .badge-transcript {{
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-emerald);
    }}

    .chapter-name {{
      font-size: 12.5px;
      font-weight: 600;
      color: var(--text-main);
      line-height: 1.35;
    }}

    .chapter-topic {{
      font-size: 11px;
      color: var(--text-dim);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    /* Main Content Area */
    main.content-view {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      background: radial-gradient(circle at top right, rgba(16, 185, 129, 0.03), transparent 40%),
                  radial-gradient(circle at bottom left, rgba(6, 182, 212, 0.03), transparent 40%),
                  var(--bg-dark);
      padding: 24px 32px;
      gap: 20px;
    }}

    /* Chapter Header Banner */
    .chapter-banner {{
      background: linear-gradient(135deg, rgba(25, 36, 60, 0.7), rgba(17, 23, 38, 0.9));
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 20px 24px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
    }}

    .banner-tags {{
      display: flex;
      gap: 8px;
      align-items: center;
      flex-wrap: wrap;
    }}

    .tag {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      padding: 3px 10px;
      border-radius: 6px;
    }}
    .tag-module {{
      background: rgba(245, 158, 11, 0.15);
      color: var(--accent-amber);
      border: 1px solid rgba(245, 158, 11, 0.3);
    }}
    .tag-session {{
      background: rgba(6, 182, 212, 0.15);
      color: var(--accent-cyan);
      border: 1px solid rgba(6, 182, 212, 0.3);
    }}

    .banner-title {{
      font-size: 22px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #FFF;
      line-height: 1.3;
    }}

    .banner-meta {{
      display: flex;
      align-items: center;
      gap: 20px;
      font-size: 12.5px;
      color: var(--text-muted);
      flex-wrap: wrap;
    }}

    .banner-meta a {{
      color: var(--accent-emerald);
      text-decoration: none;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }}
    .banner-meta a:hover {{
      text-decoration: underline;
    }}

    /* Video Player Card */
    .video-container {{
      width: 100%;
      background: #000;
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid var(--border-color);
      position: relative;
      padding-top: 48%; /* 16:9 approx */
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4);
    }}

    .video-container iframe {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: none;
    }}

    /* Tabs Bar */
    .tabs-bar {{
      display: flex;
      gap: 8px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 4px;
      overflow-x: auto;
    }}

    .tab-btn {{
      padding: 9px 16px;
      border-radius: 8px 8px 0 0;
      font-size: 13px;
      font-weight: 700;
      color: var(--text-muted);
      background: transparent;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 7px;
      transition: all 0.2s;
      border-bottom: 2px solid transparent;
      white-space: nowrap;
    }}

    .tab-btn:hover {{
      color: #FFF;
      background: rgba(255, 255, 255, 0.03);
    }}

    .tab-btn.active {{
      color: var(--accent-emerald);
      border-bottom-color: var(--accent-emerald);
      background: rgba(16, 185, 129, 0.06);
    }}

    /* Tab Panels */
    .tab-panel {{
      display: none;
      animation: fadeIn 0.2s ease-in;
    }}
    .tab-panel.active {{
      display: block;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Senior Analyst Crucible Box */
    .crucible-callout {{
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.08), rgba(17, 23, 38, 0.9));
      border: 1px solid rgba(245, 158, 11, 0.25);
      border-left: 4px solid var(--accent-amber);
      border-radius: 10px;
      padding: 18px 22px;
      margin-bottom: 20px;
    }}

    .crucible-callout h3 {{
      color: var(--accent-amber);
      font-size: 15px;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
      letter-spacing: -0.01em;
    }}

    .crucible-callout p {{
      font-size: 13.5px;
      color: #E5E7EB;
      line-height: 1.6;
      font-style: italic;
    }}

    /* Content Cards Grid */
    .grid-2 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 16px;
      margin-top: 16px;
    }}

    .card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 20px;
      transition: all 0.2s;
    }}

    .card:hover {{
      border-color: rgba(255, 255, 255, 0.15);
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
    }}

    .card-title {{
      font-size: 15px;
      font-weight: 700;
      color: #FFF;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .card-content {{
      font-size: 13.5px;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    .card-content ul {{
      padding-left: 18px;
      margin-top: 8px;
    }}

    .card-content li {{
      margin-bottom: 6px;
    }}

    /* Book Cards */
    .book-card {{
      background: var(--bg-card-subtle);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 18px;
      margin-bottom: 14px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      border-left: 3px solid var(--accent-cyan);
    }}

    .book-title {{
      font-size: 15px;
      font-weight: 700;
      color: #FFF;
    }}

    .book-author {{
      font-size: 12px;
      color: var(--accent-cyan);
      font-weight: 600;
    }}

    .book-thesis {{
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.55;
    }}

    .book-app {{
      font-size: 12.5px;
      color: #E2E8F0;
      background: rgba(255, 255, 255, 0.04);
      padding: 8px 12px;
      border-radius: 6px;
      border-left: 2px solid var(--accent-emerald);
    }}

    /* Transcript Viewer */
    .transcript-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      max-height: 600px;
    }}

    .transcript-toolbar {{
      padding: 12px 18px;
      background: rgba(0, 0, 0, 0.2);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}

    .transcript-search {{
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 6px 12px;
      font-size: 12px;
      color: #FFF;
      outline: none;
      width: 260px;
    }}

    .transcript-search:focus {{
      border-color: var(--accent-emerald);
    }}

    .transcript-entries {{
      padding: 14px 18px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .transcript-line {{
      display: flex;
      gap: 14px;
      padding: 6px 10px;
      border-radius: 6px;
      cursor: pointer;
      transition: background 0.15s;
    }}

    .transcript-line:hover {{
      background: rgba(255, 255, 255, 0.05);
    }}

    .transcript-time {{
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--accent-cyan);
      font-weight: 600;
      min-width: 55px;
      user-select: none;
    }}

    .transcript-text {{
      font-size: 13px;
      color: #D1D5DB;
      line-height: 1.5;
    }}

    /* Bookshelf Modal */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(8px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }}
    .modal-overlay.active {{
      display: flex;
    }}

    .modal-dialog {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      width: 100%;
      max-width: 900px;
      max-height: 85vh;
      overflow-y: auto;
      padding: 28px;
      position: relative;
      box-shadow: 0 24px 64px rgba(0, 0, 0, 0.6);
    }}

    .modal-close {{
      position: absolute;
      top: 20px;
      right: 20px;
      background: rgba(255, 255, 255, 0.08);
      border: none;
      color: #FFF;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .library-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
      gap: 16px;
      margin-top: 20px;
    }}

    @media (max-width: 1024px) {{
      aside.sidebar {{
        width: 300px;
      }}
      main.content-view {{
        padding: 16px;
      }}
    }}

    @media (max-width: 768px) {{
      .app-container {{
        flex-direction: column;
      }}
      aside.sidebar {{
        width: 100%;
        height: 240px;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Navigation Header -->
  <header class="top-bar">
    <div class="brand-group">
      <div class="brand-icon">α</div>
      <div class="brand-title">
        <h1>Alpha Vantage & Equity Research</h1>
        <p>32-Yr Senior Analyst Masterclass & Curriculum Portal</p>
      </div>
    </div>

    <div class="header-center">
      <span class="search-icon">🔍</span>
      <input type="text" id="globalSearch" class="search-input" placeholder="Search 49 sessions, books, forensic methods, or transcript keywords...">
    </div>

    <div class="header-actions">
      <button class="btn btn-secondary" onclick="openLibraryModal()">
        📚 Canonical Bookshelf (<span id="bookCount">19</span>)
      </button>
      <a href="https://github.com/agentsmithneo05/fundamental-analysis" target="_blank" class="btn btn-secondary">
        ⭐ GitHub Repo
      </a>
    </div>
  </header>

  <!-- App Body Layout -->
  <div class="app-container">
    <!-- Sidebar: Course Chapters -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <h2>Course Syllabus (49 Sessions)</h2>
        <div class="filter-pills" id="moduleFilterPills">
          <div class="pill active" onclick="filterByModule('all')">All Modules</div>
          <div class="pill" onclick="filterByModule('module_1')">Mod 1: Foundations</div>
          <div class="pill" onclick="filterByModule('module_2')">Mod 2: Moats</div>
          <div class="pill" onclick="filterByModule('module_3')">Mod 3: Governance</div>
          <div class="pill" onclick="filterByModule('module_4')">Mod 4: Statements</div>
          <div class="pill" onclick="filterByModule('module_5')">Mod 5: Ratios</div>
          <div class="pill" onclick="filterByModule('module_6')">Mod 6: Tooling</div>
          <div class="pill" onclick="filterByModule('module_7')">Mod 7: WACC & Macro</div>
          <div class="pill" onclick="filterByModule('module_8')">Mod 8: Mindset</div>
        </div>
      </div>

      <div class="chapters-list" id="chaptersList">
        <!-- Rendered via JS -->
      </div>
    </aside>

    <!-- Main Content Canvas -->
    <main class="content-view" id="mainCanvas">
      <!-- Chapter Banner -->
      <div class="chapter-banner">
        <div class="banner-tags">
          <span class="tag tag-module" id="bannerModule">Module 1: Orientation</span>
          <span class="tag tag-session" id="bannerSession">Session 01</span>
          <span class="tag" style="background:rgba(255,255,255,0.08);" id="bannerVideoId">ID: 588JO2LGQPI</span>
        </div>
        <h2 class="banner-title" id="bannerTitle">Basics of Equity Research | Full Course | Session 1 : Introduction</h2>
        <div class="banner-meta">
          <span>Instructor: <strong>Parth Verma (The Valuation School)</strong></span>
          <span>•</span>
          <a id="bannerYtLink" href="https://www.youtube.com/watch?v=588JO2LGQPI" target="_blank">
            ▶ Open on YouTube
          </a>
          <span>•</span>
          <a id="bannerPlaylistLink" href="https://www.youtube.com/playlist?list=PL3uUjzLk6Pum8iq_fpwzb8hwFaRGZQP4k" target="_blank">
            📋 Full Playlist
          </a>
          <span>•</span>
          <span id="bannerTranscriptCount">341 Transcript Snippets</span>
        </div>
      </div>

      <!-- YouTube Embed Card -->
      <div class="video-container">
        <iframe id="videoIframe" src="https://www.youtube.com/embed/588JO2LGQPI?enablejsapi=1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>

      <!-- Tab Navigation -->
      <div class="tabs-bar">
        <button class="tab-btn active" onclick="switchTab('summary')">📋 Executive Brief</button>
        <button class="tab-btn" onclick="switchTab('crucible')">🧠 Senior Analyst Crucible</button>
        <button class="tab-btn" onclick="switchTab('literature')">📖 Canonical Literature</button>
        <button class="tab-btn" onclick="switchTab('practices')">🔍 Diligence Protocols</button>
        <button class="tab-btn" onclick="switchTab('transcript')">📜 Interactive Transcript</button>
      </div>

      <!-- Tab Panels -->
      <!-- 1. Executive Brief -->
      <div class="tab-panel active" id="tab-summary">
        <div class="card">
          <div class="card-title">🎯 Curriculum Placement & Core Mission</div>
          <div class="card-content" id="summaryContent">
            <!-- Injected -->
          </div>
        </div>
      </div>

      <!-- 2. Senior Analyst Crucible -->
      <div class="tab-panel" id="tab-crucible">
        <div class="crucible-callout">
          <h3>⚖️ The 32-Year Senior Analyst's Institutional Crucible</h3>
          <p id="crucibleQuote">
            "In over three decades of interrogating financial statements and grilling management teams across market cycles, I have learned that the greatest risk to an analyst is not mathematical complexity, but intellectual complacency."
          </p>
        </div>

        <div class="grid-2">
          <div class="card">
            <div class="card-title">🎭 The Incentive Asymmetry (Principal-Agent Dilemma)</div>
            <div class="card-content">
              Beginner courses assume corporate disclosures and sell-side research notes represent unvarnished truth. In the institutional arena:
              <ul>
                <li><strong>Sell-side pressure</strong>: Bound by investment banking syndicate fees, trading volume commissions, and corporate access restrictions. Over 85% of sell-side ratings are "Buy" or "Hold".</li>
                <li><strong>Management incentives</strong>: Heavy stock-option packages encourage EBITDA inflation, aggressive revenue recognition, and vendor financing schemes.</li>
                <li><strong>Senior Rule</strong>: Always ask <em>"What incentive is driving this management disclosure?"</em></li>
              </ul>
            </div>
          </div>

          <div class="card">
            <div class="card-title">🔮 The Illusion of Precision vs Directional Accuracy</div>
            <div class="card-content">
              Novices build 50-tab financial models forecasting revenue out to 2038 with 12.34% WACCs:
              <ul>
                <li>As <strong>Benjamin Graham & David Dodd</strong> established in <em>Security Analysis</em>, intrinsic value is never a single precise point; it is a probability range.</li>
                <li>A slight 0.5% tweak in terminal growth or discount rate swings intrinsic equity value by 30-40%.</li>
                <li>Anchor your investment thesis on <strong>structural competitive moats</strong> and <strong>normalized return on invested capital (ROIC)</strong>, not spreadsheet precision.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- 3. Canonical Literature -->
      <div class="tab-panel" id="tab-literature">
        <div id="literatureCards">
          <!-- Injected -->
        </div>
      </div>

      <!-- 4. Institutional Practices -->
      <div class="tab-panel" id="tab-practices">
        <div class="card">
          <div class="card-title">🛡️ Institutional Due Diligence & Forensic Protocols</div>
          <div class="card-content" id="practicesList">
            <!-- Injected -->
          </div>
        </div>
      </div>

      <!-- 5. Interactive Transcript -->
      <div class="tab-panel" id="tab-transcript">
        <div class="transcript-box">
          <div class="transcript-toolbar">
            <input type="text" id="transcriptSearchInput" class="transcript-search" placeholder="Filter transcript in real-time...">
            <span style="font-size:12px; color:var(--text-dim);" id="transcriptMatchCount">Showing entries</span>
          </div>
          <div class="transcript-entries" id="transcriptContainer">
            <!-- Injected -->
          </div>
        </div>
      </div>

    </main>
  </div>

  <!-- Bookshelf Modal -->
  <div class="modal-overlay" id="libraryModal" onclick="closeLibraryModal(event)">
    <div class="modal-dialog" onclick="event.stopPropagation()">
      <button class="modal-close" onclick="closeLibraryModal()">✕</button>
      <h2 style="font-size: 22px; font-weight:800; color:#FFF;">📚 The Senior Analyst's Canonical Library</h2>
      <p style="font-size:13px; color:var(--text-muted); margin-top:4px;">
        Curated across 32 years of institutional investing. The 19 foundational works every serious equity research analyst must master.
      </p>
      <div class="library-grid" id="libraryGridContainer">
        <!-- Injected -->
      </div>
    </div>
  </div>

  <!-- Embed Master Catalog Data -->
  <script>
    const CATALOG = {catalog_json_str};
    let currentChapter = CATALOG.chapters[0];
    let activeModuleFilter = 'all';

    function init() {{
      renderChaptersList();
      selectChapter(CATALOG.chapters[0].chapter_index);
      renderLibraryModal();
    }}

    function filterByModule(moduleId) {{
      activeModuleFilter = moduleId;
      document.querySelectorAll('#moduleFilterPills .pill').forEach(p => p.classList.remove('active'));
      event.target.classList.add('active');
      renderChaptersList();
    }}

    function renderChaptersList() {{
      const container = document.getElementById('chaptersList');
      container.innerHTML = '';
      
      const filtered = activeModuleFilter === 'all' 
        ? CATALOG.chapters 
        : CATALOG.chapters.filter(c => c.module_id === activeModuleFilter);

      // Group by module
      const groups = {{}};
      filtered.forEach(ch => {{
        if (!groups[ch.module_id]) groups[ch.module_id] = [];
        groups[ch.module_id].push(ch);
      }});

      for (const [modId, chs] of Object.entries(groups)) {{
        const modObj = CATALOG.modules.find(m => m.id === modId);
        const groupEl = document.createElement('div');
        groupEl.className = 'module-group';
        groupEl.innerHTML = `<div class="module-title">${{modObj ? modObj.title : modId}}</div>`;

        chs.forEach(ch => {{
          const card = document.createElement('div');
          card.className = `chapter-card ${{currentChapter && currentChapter.chapter_index === ch.chapter_index ? 'active' : ''}}`;
          card.onclick = () => selectChapter(ch.chapter_index);
          card.innerHTML = `
            <div class="chapter-top">
              <span class="chapter-number">CH ${{String(ch.chapter_index).padStart(2, '0')}}</span>
              ${{ch.snippet_count > 0 ? '<span class="chapter-badge badge-transcript">Transcript ✓</span>' : '<span class="chapter-badge" style="color:var(--text-dim);">Dossier</span>'}}
            </div>
            <div class="chapter-name">${{ch.title}}</div>
            <div class="chapter-topic">${{ch.topic}}</div>
          `;
          groupEl.appendChild(card);
        }});
        container.appendChild(groupEl);
      }}
    }}

    function selectChapter(chIdx) {{
      const ch = CATALOG.chapters.find(c => c.chapter_index === chIdx);
      if (!ch) return;
      currentChapter = ch;

      // Update active in sidebar
      renderChaptersList();

      // Update Banner
      const modObj = CATALOG.modules.find(m => m.id === ch.module_id);
      document.getElementById('bannerModule').innerText = modObj ? modObj.title.split(':')[0] : ch.module_id;
      document.getElementById('bannerSession').innerText = `Session ${{String(ch.chapter_index).padStart(2, '0')}}`;
      document.getElementById('bannerVideoId').innerText = `ID: ${{ch.video_id}}`;
      document.getElementById('bannerTitle').innerText = ch.title;
      document.getElementById('bannerYtLink').href = ch.video_url;
      document.getElementById('bannerTranscriptCount').innerText = `${{ch.snippet_count || 0}} Transcript Snippets`;

      // Update Video Player
      document.getElementById('videoIframe').src = `https://www.youtube.com/embed/${{ch.video_id}}?enablejsapi=1`;

      // Update Summary Tab
      document.getElementById('summaryContent').innerHTML = `
        <p style="font-size:14.5px; color:#F3F4F6; margin-bottom:12px;"><strong>Session Focus:</strong> ${{ch.topic}}</p>
        <p style="margin-bottom:12px;">${{ch.analysis_preview}}</p>
        <p style="margin-top:14px;"><strong>Referenced Canonical Frameworks:</strong> ${{ch.books.map(b => b.title).join(', ')}}</p>
      `;

      // Update Literature Tab
      const litContainer = document.getElementById('literatureCards');
      litContainer.innerHTML = '';
      ch.books.forEach(b => {{
        const bEl = document.createElement('div');
        bEl.className = 'book-card';
        bEl.innerHTML = `
          <div class="book-title">📖 ${{b.title}} (${{b.year}})</div>
          <div class="book-author">Author: ${{b.authors}} | Category: <code>${{b.category}}</code></div>
          <div class="book-thesis">${{b.thesis}}</div>
          <div class="book-app">🎯 <strong>Direct Application:</strong> Critical reading for mastering ${{ch.topic}}. Provides base rates and structural frameworks to evaluate management narratives without falling into consensus groupthink.</div>
        `;
        litContainer.appendChild(bEl);
      }});

      // Update Practices Tab
      const pracContainer = document.getElementById('practicesList');
      pracContainer.innerHTML = '<ul>' + ch.practices.map(p => `
        <li style="margin-bottom:12px;">
          <strong style="color:var(--accent-emerald); font-size:14px;">${{p}}</strong>
          <p style="margin-top:4px; color:var(--text-muted); font-size:13px;">Deployed by Tier-1 institutions to discover non-consensus variance and stress-test whether reported margins and cash flows are real or cosmetic.</p>
        </li>
      `).join('') + '</ul>';

      // Update Transcript Tab
      renderTranscript(ch.snippets || []);
    }}

    function renderTranscript(snippets) {{
      const container = document.getElementById('transcriptContainer');
      const countEl = document.getElementById('transcriptMatchCount');
      container.innerHTML = '';

      if (!snippets || snippets.length === 0) {{
        container.innerHTML = '<div style="padding:20px; color:var(--text-dim); text-align:center;">Transcript snippets available in the raw dossier file. Direct YouTube closed captions can also be activated on the video player above.</div>';
        countEl.innerText = '0 snippets';
        return;
      }}

      countEl.innerText = `${{snippets.length}} entries`;
      snippets.forEach(s => {{
        const row = document.createElement('div');
        row.className = 'transcript-line';
        const mins = Math.floor(s.start / 60);
        const secs = Math.floor(s.start % 60);
        const timeStr = `${{String(mins).padStart(2, '0')}}:${{String(secs).padStart(2, '0')}}`;

        row.onclick = () => seekVideo(Math.floor(s.start));
        row.innerHTML = `
          <span class="transcript-time">${{timeStr}}</span>
          <span class="transcript-text">${{s.text}}</span>
        `;
        container.appendChild(row);
      }});
    }}

    function seekVideo(seconds) {{
      const iframe = document.getElementById('videoIframe');
      iframe.src = `https://www.youtube.com/embed/${{currentChapter.video_id}}?start=${{seconds}}&autoplay=1`;
    }}

    function switchTab(tabId) {{
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
      event.target.classList.add('active');
      document.getElementById(`tab-${{tabId}}`).classList.add('active');
    }}

    // Filter Transcript
    document.getElementById('transcriptSearchInput')?.addEventListener('input', (e) => {{
      const query = e.target.value.toLowerCase();
      const lines = document.querySelectorAll('.transcript-line');
      let matches = 0;
      lines.forEach(l => {{
        const text = l.querySelector('.transcript-text').innerText.toLowerCase();
        if (text.includes(query)) {{
          l.style.display = 'flex';
          matches++;
        }} else {{
          l.style.display = 'none';
        }}
      }});
      document.getElementById('transcriptMatchCount').innerText = `${{matches}} matching entries`;
    }});

    // Global Search
    document.getElementById('globalSearch')?.addEventListener('input', (e) => {{
      const q = e.target.value.toLowerCase().trim();
      if (!q) {{
        renderChaptersList();
        return;
      }}
      const matching = CATALOG.chapters.filter(c => 
        c.title.toLowerCase().includes(q) || 
        c.topic.toLowerCase().includes(q) ||
        c.practices.some(p => p.toLowerCase().includes(q)) ||
        c.books.some(b => b.title.toLowerCase().includes(q) || b.authors.toLowerCase().includes(q))
      );
      
      const container = document.getElementById('chaptersList');
      container.innerHTML = `<div class="module-title">Search Results (${{matching.length}})</div>`;
      matching.forEach(ch => {{
        const card = document.createElement('div');
        card.className = `chapter-card ${{currentChapter && currentChapter.chapter_index === ch.chapter_index ? 'active' : ''}}`;
        card.onclick = () => selectChapter(ch.chapter_index);
        card.innerHTML = `
          <div class="chapter-top">
            <span class="chapter-number">CH ${{String(ch.chapter_index).padStart(2, '0')}}</span>
            <span class="chapter-badge badge-transcript">${{ch.module_id}}</span>
          </div>
          <div class="chapter-name">${{ch.title}}</div>
          <div class="chapter-topic">${{ch.topic}}</div>
        `;
        container.appendChild(card);
      }});
    }});

    function openLibraryModal() {{
      document.getElementById('libraryModal').classList.add('active');
    }}

    function closeLibraryModal(e) {{
      if (!e || e.target === document.getElementById('libraryModal') || e.target.classList.contains('modal-close')) {{
        document.getElementById('libraryModal').classList.remove('active');
      }}
    }}

    function renderLibraryModal() {{
      const grid = document.getElementById('libraryGridContainer');
      grid.innerHTML = '';
      Object.values(CATALOG.library).forEach(b => {{
        const el = document.createElement('div');
        el.className = 'book-card';
        el.innerHTML = `
          <div class="book-title">📖 ${{b.title}} (${{b.year}})</div>
          <div class="book-author">Author: ${{b.authors}} | Category: <code>${{b.category}}</code></div>
          <div class="book-thesis">${{b.thesis}}</div>
        `;
        grid.appendChild(el);
      }});
      document.getElementById('bookCount').innerText = Object.keys(CATALOG.library).length;
    }}

    window.onload = init;
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Web application successfully generated at {OUTPUT_HTML} (Size: {len(html_content):,} bytes)")
