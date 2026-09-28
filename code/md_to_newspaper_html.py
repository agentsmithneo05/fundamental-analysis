#!/usr/bin/env python3
"""
Modern Financial Times (FT.com) Style HTML Publisher
Converts equity research markdown dossiers into standalone, modern HTML reports
styled with the iconic Financial Times (FT.com) design system, typography, and palette.
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
    date_str = "September 29, 2026"
    for line in lines[:12]:
        if line.startswith("# "):
            title = line.replace("# ", "").strip()
        elif "Target Ticker" in line or "Ticker" in line:
            ticker = line.strip().replace("**", "").replace("Target Ticker: ", "")
        elif "Research Date" in line:
            date_str = line.strip().replace("**", "").replace("Research Date: ", "")

    # Convert Markdown to HTML
    body_html = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "nl2br", "toc"]
    )

    # Enhance blockquotes and alerts with FT Lex / Forensic badges
    body_html = re.sub(
        r"<blockquote>\s*<p>\s*<strong>Key Forensic Insight</strong>:",
        r'<blockquote class="ft-lex-note"><p><span class="ft-kicker-badge">LEX FORENSIC AUDIT</span>',
        body_html
    )

    ft_html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Financial Times Research</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,400;1,600&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            /* FT.com Official Origami Design Palette */
            --ft-paper: #fff1e5;            /* Iconic FT Pink / Salmon paper */
            --ft-paper-dark: #f2dfce;       /* Darker salmon for headers & hover */
            --ft-paper-card: #fff7ef;       /* Card surface */
            --ft-border: #cec6b9;           /* Hairline card & divider border */
            --ft-border-dark: #0d0d0d;      /* Solid black rule */
            --ft-claret: #990f3d;           /* Iconic FT Claret / Burgundy */
            --ft-teal: #0d7680;             /* FT Teal for secondary data & links */
            --ft-slate: #262a33;            /* Dark Slate */
            --ft-ink: #0d0d0d;              /* Primary text black */
            --ft-body: #333333;             /* High-legibility body dark grey */
            --ft-muted: #666059;            /* Secondary metadata grey */
            --ft-green: #00703c;            /* Positive financial metric */
            --ft-red: #cc0000;              /* Negative variance / warning */
            
            /* Typography */
            --font-headline: "Playfair Display", "Georgia", "Times New Roman", serif;
            --font-body: "Georgia", "Charter", serif;
            --font-sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --font-mono: "JetBrains Mono", "SF Mono", Consolas, monospace;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: #f7e6d7;
            color: var(--ft-body);
            font-family: var(--font-body);
            font-size: 17.5px;
            line-height: 1.68;
            padding: 24px 12px;
            -webkit-font-smoothing: antialiased;
        }}

        /* Broadsheet Container */
        .ft-container {{
            max-width: 1060px;
            margin: 0 auto;
            background-color: var(--ft-paper);
            border: 1px solid var(--ft-border);
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08), 0 1px 4px rgba(0, 0, 0, 0.04);
            padding: 40px 60px;
        }}

        /* Modern FT Header & Masthead */
        .ft-header {{
            border-bottom: 2px solid var(--ft-border-dark);
            padding-bottom: 18px;
            margin-bottom: 28px;
        }}

        .ft-top-ticker {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: var(--font-sans);
            font-size: 11.5px;
            font-weight: 600;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: var(--ft-claret);
            border-bottom: 1px solid var(--ft-border);
            padding-bottom: 8px;
            margin-bottom: 16px;
        }}

        .ft-masthead-title {{
            font-family: var(--font-headline);
            font-size: 42px;
            font-weight: 900;
            letter-spacing: 1px;
            color: var(--ft-ink);
            text-align: center;
            margin: 4px 0 6px 0;
            line-height: 1.05;
        }}

        .ft-masthead-subline {{
            text-align: center;
            font-family: var(--font-sans);
            font-size: 12px;
            font-weight: 500;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: var(--ft-muted);
            margin-bottom: 14px;
        }}

        .ft-nav-strip {{
            display: flex;
            justify-content: space-between;
            border-top: 1px solid var(--ft-border-dark);
            border-bottom: 1px solid var(--ft-border-dark);
            padding: 8px 6px;
            font-family: var(--font-sans);
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            color: var(--ft-ink);
            background-color: rgba(242, 223, 206, 0.4);
        }}

        /* Kicker & Editorial Headings */
        .ft-kicker {{
            display: inline-block;
            font-family: var(--font-sans);
            font-size: 13px;
            font-weight: 700;
            color: var(--ft-claret);
            text-transform: uppercase;
            letter-spacing: 1.2px;
            margin-bottom: 6px;
        }}

        h1 {{
            font-family: var(--font-headline);
            font-size: 32px;
            font-weight: 800;
            color: var(--ft-ink);
            line-height: 1.2;
            margin: 24px 0 16px 0;
            letter-spacing: -0.4px;
        }}

        h2 {{
            font-family: var(--font-headline);
            font-size: 24px;
            font-weight: 700;
            color: var(--ft-ink);
            border-top: 2px solid var(--ft-border-dark);
            border-bottom: 1px solid var(--ft-border);
            padding: 12px 0 8px 0;
            margin: 40px 0 18px 0;
            letter-spacing: -0.2px;
        }}

        h3 {{
            font-family: var(--font-sans);
            font-size: 17px;
            font-weight: 700;
            color: var(--ft-claret);
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin: 26px 0 10px 0;
            border-bottom: 1px dashed var(--ft-border);
            padding-bottom: 4px;
        }}

        p {{
            margin-bottom: 16px;
            text-align: justify;
            text-justify: inter-word;
        }}

        strong {{
            color: var(--ft-ink);
            font-weight: 700;
        }}

        em {{
            font-style: italic;
        }}

        hr {{
            border: none;
            border-top: 1px solid var(--ft-border);
            margin: 32px 0;
        }}

        /* FT Modern Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            font-family: var(--font-mono);
            font-size: 13px;
            line-height: 1.45;
            margin: 24px 0;
            background-color: var(--ft-paper-card);
            border-top: 2px solid var(--ft-border-dark);
            border-bottom: 2px solid var(--ft-border-dark);
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
        }}

        th {{
            background-color: var(--ft-paper-dark);
            color: var(--ft-ink);
            font-family: var(--font-sans);
            font-weight: 700;
            text-align: left;
            padding: 10px 12px;
            border-bottom: 1px solid var(--ft-border-dark);
            text-transform: uppercase;
            font-size: 11px;
            letter-spacing: 0.8px;
        }}

        td {{
            padding: 8px 12px;
            border-bottom: 1px solid var(--ft-border);
            color: var(--ft-ink);
            font-variant-numeric: tabular-nums;
        }}

        tr:nth-child(even) td {{
            background-color: rgba(242, 223, 206, 0.25);
        }}

        tr:hover td {{
            background-color: rgba(153, 15, 61, 0.06);
        }}

        /* Code Blocks & Terminal Snippets */
        pre {{
            background-color: #f7e6d7;
            border: 1px solid var(--ft-border);
            border-left: 4px solid var(--ft-claret);
            font-family: var(--font-mono);
            font-size: 12.5px;
            line-height: 1.5;
            padding: 16px 20px;
            margin: 22px 0;
            overflow-x: auto;
            color: var(--ft-ink);
            box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.04);
        }}

        code {{
            font-family: var(--font-mono);
            font-size: 13px;
            background-color: rgba(242, 223, 206, 0.8);
            padding: 2px 5px;
            border-radius: 2px;
            color: var(--ft-ink);
        }}

        /* FT Lex Callout / Pull Quotes */
        blockquote, .ft-lex-note {{
            background-color: var(--ft-paper-card);
            border-left: 4px solid var(--ft-claret);
            border-top: 1px solid var(--ft-border);
            border-right: 1px solid var(--ft-border);
            border-bottom: 1px solid var(--ft-border);
            padding: 16px 22px;
            margin: 24px 0;
            font-style: italic;
            color: var(--ft-ink);
        }}

        .ft-kicker-badge {{
            display: inline-block;
            background-color: var(--ft-claret);
            color: #ffffff;
            font-family: var(--font-sans);
            font-size: 10.5px;
            font-weight: 700;
            letter-spacing: 1.2px;
            padding: 3px 8px;
            text-transform: uppercase;
            font-style: normal;
            margin-right: 10px;
            vertical-align: middle;
            border-radius: 1px;
        }}

        /* Lists */
        ul, ol {{
            margin: 16px 0 20px 28px;
        }}

        li {{
            margin-bottom: 8px;
        }}

        /* Links */
        a {{
            color: var(--ft-teal);
            text-decoration: underline;
            text-decoration-thickness: 1px;
            text-underline-offset: 2px;
            transition: color 0.15s ease;
        }}

        a:hover {{
            color: var(--ft-claret);
        }}

        /* Print Styling */
        @media print {{
            body {{
                background: #ffffff;
                color: #000000;
                padding: 0;
            }}
            .ft-container {{
                box-shadow: none;
                border: none;
                padding: 0;
                max-width: 100%;
                background: #ffffff;
            }}
            table {{
                background: #ffffff;
            }}
            th {{
                background: #f0f0f0;
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
                font-size: 16px;
            }}
            .ft-container {{
                padding: 24px 16px;
            }}
            .ft-masthead-title {{
                font-size: 28px;
            }}
            .ft-top-ticker, .ft-nav-strip {{
                flex-direction: column;
                gap: 6px;
                text-align: center;
            }}
            table {{
                display: block;
                overflow-x: auto;
                font-size: 12px;
            }}
        }}
    </style>
</head>
<body>
    <article class="ft-container">
        <header class="ft-header">
            <div class="ft-top-ticker">
                <span>FT.COM / COMPANIES & MARKETS</span>
                <span>GLOBAL INSTITUTIONAL RESEARCH</span>
                <span>SPECIAL FORENSIC DISPATCH</span>
            </div>
            <div class="ft-masthead-title">FINANCIAL TIMES</div>
            <div class="ft-masthead-subline">Without Fear and Without Favour • Equity Research & Forensic Audit</div>
            <div class="ft-nav-strip">
                <span>{ticker}</span>
                <span>INTRINSIC VALUATION & DILIGENCE</span>
                <span>{date_str}</span>
            </div>
        </header>

        <main class="ft-article-content">
            {body_html}
        </main>

        <footer style="margin-top: 48px; padding-top: 18px; border-top: 2px solid var(--ft-border-dark); text-align: center; font-family: var(--font-sans); font-size: 11px; font-weight: 600; color: var(--ft-muted); text-transform: uppercase; letter-spacing: 1.5px;">
            Published via Financial Times Design Framework • Institutional Equity Research Suite • Antigravity Autonomous Systems
        </footer>
    </article>
</body>
</html>
"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(ft_html_template)

    print(f"Successfully generated modern FT.com style HTML: {html_path}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 md_to_newspaper_html.py <path_to_markdown_file> [<output_html_path>]")
        sys.exit(1)
        
    md_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else None
    convert_md_to_newspaper_html(md_file, out_file)
