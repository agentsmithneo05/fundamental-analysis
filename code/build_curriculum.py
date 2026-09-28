#!/usr/bin/env python3
"""
Curriculum Builder for Fundamental Analysis & Equity Research
Fetches transcripts, structures playlists into chapters, writes senior analyst
deep-dive analyses with literature references, and generates data for the web UI.
"""

import os
import json
import re
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi

BASE_DIR = Path("/home/neo/codebase/fundamental_analysis")
PLAYLIST_DIR = BASE_DIR / "playlists" / "basics_of_equity_research"
REPORT_DIR = BASE_DIR / "report"
WEB_DIR = BASE_DIR / "web"

PLAYLIST_DIR.mkdir(parents=True, exist_ok=True)
WEB_DIR.mkdir(parents=True, exist_ok=True)

# Curated metadata with modules, thematic categorization, and references
MODULES_CONFIG = [
    {
        "module_id": "mod_01",
        "title": "Module 1: Orientation & Foundations of Equity Research",
        "description": "Deconstructing the analyst's mandate, information asymmetry, and structural dynamics between Buy-Side and Sell-Side.",
        "canonical_books": [
            {"title": "Security Analysis (6th Ed.)", "author": "Benjamin Graham & David Dodd", "topic": "Intrinsic Value & The Analyst's Charter"},
            {"title": "Expectations Investing", "author": "Michael J. Mauboussin & Alfred Rappaport", "topic": "Reading Market Expectations vs Fundamentals"},
            {"title": "The Intelligent Investor", "author": "Benjamin Graham", "topic": "Mr. Market & Margin of Safety"}
        ]
    },
    {
        "module_id": "mod_02",
        "title": "Module 2: Business Model Analysis & Economic Moats",
        "description": "Dissecting value chains, unit economics, pricing power, Porter's 5 Forces, and sustainable competitive advantages.",
        "canonical_books": [
            {"title": "Competitive Strategy", "author": "Michael E. Porter", "topic": "Industry Structure & Five Forces Framework"},
            {"title": "The Little Book That Builds Wealth", "author": "Pat Dorsey", "topic": "The 4 Sources of Economic Moats (Network, Intangibles, Cost, Switching)"},
            {"title": "Common Stocks and Uncommon Profits", "author": "Philip A. Fisher", "topic": "The 15-Point Scuttlebutt Method"}
        ]
    },
    {
        "module_id": "mod_03",
        "title": "Module 3: Corporate Governance & Management Due Diligence",
        "description": "Promoter integrity, board oversight, related-party transactions, capital allocation, and minority shareholder rights.",
        "canonical_books": [
            {"title": "Poor Charlie's Almanack", "author": "Charles T. Munger", "topic": "Incentives, Agency Costs & Cognitive Biases"},
            {"title": "The Joys of Compounding", "author": "Gautam Baid", "topic": "Management Quality & Capital Allocation Discipline"},
            {"title": "Outsiders: Eight Unconventional CEOs", "author": "William N. Thorndike Jr.", "topic": "Capital Allocation Frameworks"}
        ]
    },
    {
        "module_id": "mod_04",
        "title": "Module 4: Financial Statement Mastery & Accounting Forensics",
        "description": "Rigorous decompression of the Balance Sheet, Income Statement, Cash Flow Statement, EBITDA reconciliations, and forensic red flags.",
        "canonical_books": [
            {"title": "Financial Shenanigans (4th Ed.)", "author": "Howard M. Schilit & Jeremy Perler", "topic": "Detecting Revenue & Cash Flow Manipulations"},
            {"title": "Quality of Earnings", "author": "Thornton L. O'glove", "topic": "Divergence between GAAP Net Income and Operating Cash Flow"},
            {"title": "Financial Statement Analysis and Security Valuation", "author": "Stephen H. Penman", "topic": "Reformulating Statements & Clean Surplus Accounting"}
        ]
    },
    {
        "module_id": "mod_05",
        "title": "Module 5: Financial Ratio Analysis & DuPont Decomposition",
        "description": "Deconstructing return on invested capital (ROIC), return on equity (ROE), asset turns, cash conversion cycles, and solvency stress tests.",
        "canonical_books": [
            {"title": "Valuation: Measuring and Managing the Value of Companies", "author": "McKinsey & Company", "topic": "ROIC vs WACC Spreads & Value Drivers"},
            {"title": "More Than You Know: Finding Financial Wisdom", "author": "Michael J. Mauboussin", "topic": "Base Rates, Mean Reversion in ROE/ROIC"}
        ]
    },
    {
        "module_id": "mod_06",
        "title": "Module 6: Primary Research, Concalls & The Analyst's Toolkit",
        "description": "Annual report deep dives, earnings concall interrogation, credit rating surveillance, channel checks, and screeners.",
        "canonical_books": [
            {"title": "One Up On Wall Street", "author": "Peter Lynch", "topic": "Street-level Scuttlebutt & Operational Channel Checks"},
            {"title": "Margin of Safety", "author": "Seth A. Klarman", "topic": "Risk Management, Sifting Noise vs Signal in Filings"}
        ]
    },
    {
        "module_id": "mod_07",
        "title": "Module 7: Valuation, Cost of Capital & Market Cycles",
        "description": "WACC deconstruction, cost of equity, capital asset pricing model limits, market cycles, and macroeconomic transmission mechanisms.",
        "canonical_books": [
            {"title": "Damodaran on Valuation", "author": "Aswath Damodaran", "topic": "Discount Rates, Terminal Value, Risk-Free Rate Fallacies"},
            {"title": "Mastering the Market Cycle", "author": "Howard Marks", "topic": "Pendulum Swings in Psychology & Credit Availability"}
        ]
    },
    {
        "module_id": "mod_08",
        "title": "Module 8: The Senior Analyst Practicum & Mindset",
        "description": "Cognitive psychology, consensus arbitrage, variant perception, thesis writing, and professional research ethics.",
        "canonical_books": [
            {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "topic": "Cognitive Biases, Overconfidence, Anchoring in Valuations"},
            {"title": "Superforecasting: The Art and Science of Prediction", "author": "Philip E. Tetlock", "topic": "Probabilistic Calibration & Updating Beliefs"}
        ]
    }
]

def load_playlist_videos():
    path = REPORT_DIR / "playlist_videos.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def sanitize_slug(text):
    text = re.sub(r'[^a-zA-Z0-9\s_-]', '', text.lower())
    text = re.sub(r'[\s-]+', '_', text.strip())
    return text[:45]

print("Loaded builder module")
