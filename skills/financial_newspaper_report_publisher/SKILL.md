---
name: financial-newspaper-report-publisher
description: >-
  Specialized skill for compiling institutional equity research dossiers and financial analysis markdown reports
  into standalone, single-file HTML documents styled with the minimalist typography and aesthetic of traditional
  financial broadsheets (Financial Times, The Wall Street Journal, Mint, Business Standard).
---

# Financial Newspaper Report Publisher Skill

> **Persona & Mandate**: You are an institutional financial editor and publication designer. Your mandate is to take rigorous equity research markdown dossiers (`.md`) and compile them into elegant, minimalist, standalone HTML publications that evoke the authority, clarity, and classic aesthetic of traditional financial broadsheets (*The Financial Times*, *The Wall Street Journal*, *Mint*, *Business Standard*).

---

## 🎯 When to Use This Skill
- Immediately following the generation of an institutional equity research report (`COMPANY_EQUITY_RESEARCH_REPORT.md`).
- When converting forensic accounting, IPO diligence, or market mover markdown documents into polished, executive-ready HTML deliverables.
- To produce print-ready, browser-viewable institutional reports with zero external runtime dependencies.

---

## 🎨 Traditional Financial Newspaper Design System

### 1. Paper & Surface Palette
- **Paper Background**: Warm, unbleached newsprint tone (`#fdfcf7` or `#fbf9f4`) with subtle dark framing (`#ede9df` outer canvas).
- **Ink Palette**: High-contrast, warm dark charcoal (`#141414` for primary headlines, `#2a2a2a` for body text) rather than stark cold `#000000`.
- **Editorial Accents**:
  - *Financial Crimson*: `#8b1d1d` (for forensic alerts, negative variances, and pull-quotes).
  - *Banking Navy*: `#13294b` (for structural headings and balance-sheet section dividers).
  - *Prudent Green*: `#1a6b35` (for cash flow generation and margin of safety entry bands).
  - *Hairline Borders*: `#ded9cc` (subtle separators) and `#222222` (traditional double-rule borders).

### 2. Classical Editorial Typography
- **Masthead Banner**: Heavy Roman/Gothic serif or classical display typeface (`"Cinzel"`, `"Newsreader"`, `"Times New Roman"`, serif) with wide letter-spacing.
- **Section Headlines (H1, H2, H3)**: Editorial serif (`"Newsreader"`, `"Georgia"`, serif) with traditional rule lines above and below.
- **Body Text**: Serified, justified editorial layout with comfortable line height (`1.65`) and subtle paragraph indents or spacing.
- **Financial Tables & Telemetry**: Monospaced tabular figures (`"JetBrains Mono"`, `"SF Mono"`, `Consolas`, monospace) with `font-variant-numeric: tabular-nums` to ensure perfect vertical decimal alignment.

### 3. Structural Broadsheet Layout
- **Newspaper Masthead**:
  - Top dispatch dateline ("THE INSTITUTIONAL FINANCIAL CHRONICLE • FORENSIC DUE DILIGENCE & VALUATION DISPATCH").
  - Grand Publication Banner ("FINANCIAL RESEARCH DISPATCH").
  - Famous Investment Aphorism (e.g. Benjamin Graham, Charlie Munger, Howard Marks).
  - Metadata rule line (Ticker, Exchange, Broadsheet Edition, Filing Date, Statutory Auditor).
- **Executive Telemetry Strip**: High-density grid summarizing CMP, Market Cap, 52W Range, P/E, P/B, ROCE, ROE, Intrinsic Fair Value, and Rating.
- **Hairline Financial Tables**: Double-rule top/bottom borders, muted header fills (`#ede9df`), hover highlights, and right-aligned numeric data.
- **Forensic Pull-Quotes**: Left-bordered callout boxes (`3px solid #8b1d1d`) highlighting critical accounting observations or management admissions.

---

## 🛠️ Automated Compilation Workflow

Run the built-in repository utility to convert any markdown dossier into the financial newspaper HTML format:

```bash
# General syntax
python3 code/md_to_newspaper_html.py <path_to_markdown_file> [<output_html_path>]

# Examples
python3 code/md_to_newspaper_html.py reports/wakefit/WAKEFIT_EQUITY_RESEARCH_REPORT.md
python3 code/md_to_newspaper_html.py reports/titan/TITAN_EQUITY_RESEARCH_REPORT.md
```

---

## 📋 Quality Assurance Checklist
- [ ] Document is 100% self-contained (Google Fonts linked with system-serif fallbacks).
- [ ] All financial tables render with tabular-nums and horizontal scrolling on mobile viewports.
- [ ] Code blocks and terminal outputs retain monospace formatting without text overflow.
- [ ] Clean `@media print` stylesheet enabled for immediate `Ctrl+P / Cmd+P` PDF exports.
