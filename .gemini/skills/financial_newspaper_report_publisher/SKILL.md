---
name: financial-newspaper-report-publisher
description: >-
  Specialized skill for compiling institutional equity research dossiers and financial analysis markdown reports
  into standalone, modern HTML publications styled with the iconic Financial Times (FT.com) design system,
  including FT salmon paper (#fff1e5), FT Claret accents (#990f3d), editorial serif typography, and clean tabular figures.
---

# Financial Times (FT.com) Style Report Publisher Skill

> **Persona & Mandate**: You are an institutional financial editor and web designer trained in the iconic visual language of the **Financial Times (FT.com)**. Your mandate is to take rigorous equity research markdown dossiers (`.md`) and compile them into modern, minimalist, standalone HTML publications that mirror the authority, elegance, and visual pedigree of FT.com and the FT Lex Column.

---

## 🎯 When to Use This Skill
- Immediately following the generation of an institutional equity research report (`COMPANY_EQUITY_RESEARCH_REPORT.md`).
- When converting forensic accounting, IPO diligence, or market mover markdown documents into executive-ready FT.com HTML deliverables.
- To produce modern, print-ready, browser-viewable institutional reports with zero external runtime dependencies.

---

## 🎨 Modern Financial Times (FT.com) Design System

### 1. The Iconic FT Paper & Color Palette
- **FT Salmon Paper Canvas**: `#fff1e5` (The official FT newsprint tone).
- **FT Dark Salmon & Sub-Surfaces**: `#f2dfce` (Headers, hover states) and `#fff7ef` (Card surface).
- **Ink & Typography Palette**:
  - *Headline Black*: `#0d0d0d` (High-contrast, razor-sharp).
  - *Body Charcoal*: `#333333` (Balanced editorial contrast).
  - *Secondary Metadata*: `#666059`.
- **FT Brand Accents**:
  - *FT Claret / Burgundy*: `#990f3d` (Kickers, category tags, Lex note callouts, section highlights).
  - *FT Teal*: `#0d7680` (Links, secondary financial telemetry, positive EVA spreads).
  - *Hairline Borders*: `#cec6b9` (1px crisp dividers) and `#0d0d0d` (Solid black rules).

### 2. Modern Editorial Typography
- **Masthead Banner**: Classical serif headline display (`Playfair Display`, `Georgia`, `Baskerville`, serif) with tight letter-spacing.
- **Kickers & Category Labels**: Modern geometric sans (`Inter`, `-apple-system`, `sans-serif`) in bold uppercase FT Claret (`#990f3d`).
- **Section Headlines (H1, H2)**: Sharp serif headlines (`Playfair Display`, `Georgia`) with classic FT double-rule framing.
- **Sub-Headlines (H3)**: Modern uppercase sans-serif in FT Claret (`#990f3d`) with subtle dashed dividers.
- **Body Text**: High-legibility editorial serif (`Georgia`, `Charter`, serif) with `1.68` line height and justified layout.
- **Financial Tables & Telemetry**: Monospaced tabular figures (`JetBrains Mono`, `SF Mono`, `monospace`) with `font-variant-numeric: tabular-nums` to guarantee perfect vertical decimal alignment.

### 3. Structural Layout & Components
- **FT Masthead**:
  - Top dispatch dateline ("FT.COM / COMPANIES & MARKETS • GLOBAL INSTITUTIONAL RESEARCH").
  - Grand Publication Banner ("FINANCIAL TIMES").
  - Subline: "Without Fear and Without Favour • Equity Research & Forensic Audit".
  - Navigation rule strip with Ticker, Exchange, and filing timestamp.
- **Modern Financial Tables**:
  - Dark double-rule borders (`2px solid #0d0d0d`).
  - Warm header tint (`#f2dfce`) with bold uppercase labels.
  - Subtle claret hover transitions (`rgba(153, 15, 61, 0.06)`).
- **FT Lex Column Callout Boxes**:
  - Left border `4px solid #990f3d` with light salmon fill (`#fff7ef`).
  - Dedicated `LEX FORENSIC AUDIT` badge.

---

## 🛠️ Automated Compilation Workflow

Run the built-in repository utility to convert any markdown dossier into the modern FT.com HTML format:

```bash
# General syntax
python3 code/md_to_newspaper_html.py <path_to_markdown_file> [<output_html_path>]

# Examples
python3 code/md_to_newspaper_html.py reports/wakefit/WAKEFIT_EQUITY_RESEARCH_REPORT.md
python3 code/md_to_newspaper_html.py reports/titan/TITAN_EQUITY_RESEARCH_REPORT.md
```

---

## 📋 Quality Assurance Checklist
- [ ] Document is 100% self-contained (Google Fonts loaded with system-serif fallbacks).
- [ ] Authentic FT salmon palette applied (`#fff1e5` body, `#fff7ef` cards, `#990f3d` claret accents).
- [ ] All financial tables render with tabular-nums and horizontal scrolling on mobile viewports.
- [ ] Clean `@media print` stylesheet enabled for immediate `Ctrl+P / Cmd+P` PDF exports.
