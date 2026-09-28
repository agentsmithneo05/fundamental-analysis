#!/usr/bin/env python3
"""
Institutional Financial Newspaper HTML Publisher
Converts equity research markdown dossiers into standalone, minimalist HTML reports
styled with traditional financial newspaper typography and aesthetics.
"""

import sys
import re
import os
import markdown

def convert_md_to_newspaper_html(md_path: str, html_path: str = None):
    if not os.path.exists(md_path):
        print(f"Error: {md_path} does not exist.")
        return False
        
    if html_path is None:
        html_path = os.path.splitext(md_path)[0] + ".html"
        
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Extract Title and Metadata from the first few lines
    lines = md_text.splitlines()
    title = "Institutional Equity Research Report"
    ticker = ""
    date_str = ""
    for line in lines[:10]:
        if line.startswith("# "):
            title = line.replace("# ", "").strip()
        elif "Target Ticker" in line or "Ticker" in line:
            ticker = line.strip().replace("**", "")
        elif "Research Date" in line:
            date_str = line.strip().replace("**", "")

    # Convert Markdown to HTML
    body_html = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "nl2br", "toc"]
    )

    # Enhance blockquotes and alerts
    body_html = re.sub(
        r"<blockquote>\s*<p>\s*<strong>Key Forensic Insight</strong>:",
        r'<blockquote class="forensic-insight"><p><span class="insight-badge">FORENSIC AUDIT INSIGHT</span>',
        body_html
    )

    newspaper_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --paper-bg: #fdfcf7;
            --paper-surface: #f7f5ed;
            --paper-border: #ded9cc;
            --paper-border-dark: #222222;
            --ink-black: #141414;
            --ink-charcoal: #2a2a2a;
            --ink-muted: #59554d;
            --ink-faint: #807a70;
            --accent-crimson: #8b1d1d;
            --accent-green: #1a6b35;
            --accent-navy: #13294b;
            --font-serif-headline: "Newsreader", "Georgia", "Times New Roman", serif;
            --font-serif-body: "Newsreader", "Georgia", serif;
            --font-display-title: "Cinzel", "Newsreader", "Times New Roman", serif;
            --font-mono: "JetBrains Mono", "SF Mono", Consolas, monospace;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: #ede9df;
            color: var(--ink-charcoal);
            font-family: var(--font-serif-body);
            font-size: 17px;
            line-height: 1.65;
            padding: 24px 12px;
            -webkit-font-smoothing: antialiased;
        }}

        .sheet {{
            max-width: 1040px;
            margin: 0 auto;
            background-color: var(--paper-bg);
            border: 1px solid #d4cebe;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08), 0 1px 3px rgba(0, 0, 0, 0.04);
            padding: 48px 56px;
        }}

        /* Newspaper Masthead */
        .masthead {{
            text-align: center;
            border-bottom: 3px double var(--paper-border-dark);
            padding-bottom: 16px;
            margin-bottom: 24px;
        }}

        .masthead-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: var(--font-mono);
            font-size: 11px;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            color: var(--ink-muted);
            border-bottom: 1px solid var(--paper-border);
            padding-bottom: 6px;
            margin-bottom: 12px;
        }}

        .masthead-banner {{
            font-family: var(--font-display-title);
            font-size: 34px;
            letter-spacing: 3px;
            font-weight: 900;
            color: var(--ink-black);
            text-transform: uppercase;
            margin: 8px 0 4px 0;
            line-height: 1.1;
        }}

        .masthead-tagline {{
            font-style: italic;
            font-size: 14px;
            color: var(--ink-muted);
            margin-bottom: 10px;
        }}

        .masthead-meta {{
            display: flex;
            justify-content: space-between;
            border-top: 1px solid var(--paper-border-dark);
            border-bottom: 1px solid var(--paper-border-dark);
            padding: 6px 4px;
            font-family: var(--font-mono);
            font-size: 11.5px;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--ink-charcoal);
        }}

        /* Article Typography */
        h1 {{
            font-family: var(--font-serif-headline);
            font-size: 28px;
            font-weight: 700;
            color: var(--ink-black);
            line-height: 1.25;
            margin: 20px 0 16px 0;
            letter-spacing: -0.2px;
        }}

        h2 {{
            font-family: var(--font-serif-headline);
            font-size: 22px;
            font-weight: 700;
            color: var(--ink-black);
            border-top: 2px solid var(--paper-border-dark);
            border-bottom: 1px solid var(--paper-border);
            padding: 10px 0 6px 0;
            margin: 36px 0 16px 0;
            letter-spacing: 0.2px;
            text-transform: uppercase;
        }}

        h3 {{
            font-family: var(--font-serif-headline);
            font-size: 18px;
            font-weight: 600;
            color: var(--accent-navy);
            margin: 22px 0 10px 0;
            border-bottom: 1px dashed var(--paper-border);
            padding-bottom: 4px;
        }}

        p {{
            margin-bottom: 14px;
            text-align: justify;
            text-justify: inter-word;
        }}

        strong {{
            color: var(--ink-black);
            font-weight: 600;
        }}

        em {{
            font-style: italic;
        }}

        hr {{
            border: none;
            border-top: 1px solid var(--paper-border);
            margin: 28px 0;
        }}

        /* Financial Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            font-family: var(--font-mono);
            font-size: 13px;
            line-height: 1.45;
            margin: 22px 0;
            background: var(--paper-surface);
            border-top: 2px solid var(--paper-border-dark);
            border-bottom: 2px solid var(--paper-border-dark);
        }}

        th {{
            background-color: #ede9df;
            color: var(--ink-black);
            font-weight: 600;
            text-align: left;
            padding: 8px 10px;
            border-bottom: 1px solid var(--paper-border-dark);
            text-transform: uppercase;
            font-size: 11.5px;
            letter-spacing: 0.5px;
        }}

        td {{
            padding: 7px 10px;
            border-bottom: 1px solid #e3decb;
            color: var(--ink-charcoal);
        }}

        tr:nth-child(even) td {{
            background-color: rgba(0, 0, 0, 0.015);
        }}

        tr:hover td {{
            background-color: rgba(139, 29, 29, 0.04);
        }}

        /* Code Blocks & Terminal Outputs */
        pre {{
            background-color: var(--paper-surface);
            border: 1px solid var(--paper-border);
            border-left: 3px solid var(--accent-navy);
            font-family: var(--font-mono);
            font-size: 12.5px;
            line-height: 1.5;
            padding: 14px 18px;
            margin: 18px 0;
            overflow-x: auto;
            color: var(--ink-charcoal);
        }}

        code {{
            font-family: var(--font-mono);
            font-size: 13px;
            background-color: #efece3;
            padding: 1px 4px;
            border-radius: 2px;
        }}

        /* Editorial Callout & Blockquotes */
        blockquote {{
            background-color: var(--paper-surface);
            border-left: 3px solid var(--accent-crimson);
            padding: 14px 20px;
            margin: 20px 0;
            font-style: italic;
            color: var(--ink-charcoal);
        }}

        .insight-badge {{
            display: inline-block;
            background-color: var(--accent-crimson);
            color: #ffffff;
            font-family: var(--font-mono);
            font-size: 10px;
            font-weight: 600;
            letter-spacing: 1px;
            padding: 2px 6px;
            text-transform: uppercase;
            font-style: normal;
            margin-right: 8px;
            vertical-align: middle;
        }}

        /* Lists */
        ul, ol {{
            margin: 14px 0 18px 26px;
        }}

        li {{
            margin-bottom: 6px;
        }}

        /* Print Styling */
        @media print {{
            body {{
                background: #ffffff;
                color: #000000;
                padding: 0;
            }}
            .sheet {{
                box-shadow: none;
                border: none;
                padding: 0;
                max-width: 100%;
            }}
            a {{
                color: #000000;
                text-decoration: none;
            }}
        }}

        /* Mobile Responsiveness */
        @media (max-width: 768px) {{
            body {{
                padding: 8px 4px;
                font-size: 15.5px;
            }}
            .sheet {{
                padding: 24px 16px;
            }}
            .masthead-banner {{
                font-size: 24px;
            }}
            .masthead-top, .masthead-meta {{
                flex-direction: column;
                gap: 4px;
                text-align: center;
            }}
            table {{
                display: block;
                overflow-x: auto;
                font-size: 11.5px;
            }}
        }}
    </style>
</head>
<body>
    <article class="sheet">
        <header class="masthead">
            <div class="masthead-top">
                <span>The Institutional Financial Chronicle</span>
                <span>Forensic Due Diligence & Valuation Dispatch</span>
                <span>Confidential Research</span>
            </div>
            <div class="masthead-banner">Financial Research Dispatch</div>
            <div class="masthead-tagline">“In the short run the market is a voting machine, but in the long run it is a weighing machine.” — Benjamin Graham</div>
            <div class="masthead-meta">
                <span>{ticker}</span>
                <span>Broadsheet Edition</span>
                <span>{date_str}</span>
            </div>
        </header>

        <main class="article-content">
            {body_html}
        </main>

        <footer style="margin-top: 48px; padding-top: 16px; border-top: 2px solid var(--paper-border-dark); text-align: center; font-family: var(--font-mono); font-size: 11px; color: var(--ink-muted); text-transform: uppercase; letter-spacing: 1px;">
            Published via Institutional Equity Research Knowledge Base • Antigravity Autonomous Agentic Suite
        </footer>
    </article>
</body>
</html>
"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(newspaper_template)

    print(f"Successfully generated financial newspaper HTML: {html_path}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 md_to_newspaper_html.py <path_to_markdown_file> [<output_html_path>]")
        sys.exit(1)
        
    md_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else None
    convert_md_to_newspaper_html(md_file, out_file)
