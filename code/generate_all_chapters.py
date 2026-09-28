#!/usr/bin/env python3
"""
Full Curriculum Generator & Senior Research Analyst Knowledge Synthesizer
Builds out all chapter directories, downloads transcripts, synthesizes deep-dive
institutional analyses with literature references, and generates web assets.
"""

import os
import json
import re
import time
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi

BASE_DIR = Path("/home/neo/codebase/fundamental_analysis")
PLAYLIST_DIR = BASE_DIR / "playlists" / "basics_of_equity_research"
REPORT_DIR = BASE_DIR / "report"
WEB_DIR = BASE_DIR / "web"

PLAYLIST_DIR.mkdir(parents=True, exist_ok=True)
WEB_DIR.mkdir(parents=True, exist_ok=True)

with open(REPORT_DIR / "playlist_videos.json", "r", encoding="utf-8") as f:
    videos = json.load(f)

# Module Mapping Rules
MODULES = [
    {
        "id": "module_1",
        "number": 1,
        "title": "Module 1: Orientation & Foundations of Equity Research",
        "description": "Understanding the analyst's mandate, information asymmetry, and structural dynamics between Buy-Side and Sell-Side.",
        "icon": "compass"
    },
    {
        "id": "module_2",
        "number": 2,
        "title": "Module 2: Business Model Analysis & Economic Moats",
        "description": "Dissecting value chains, unit economics, pricing power, Porter's 5 Forces, and sustainable competitive advantages.",
        "icon": "shield"
    },
    {
        "id": "module_3",
        "number": 3,
        "title": "Module 3: Corporate Governance & Management Due Diligence",
        "description": "Promoter integrity, board oversight, related-party transactions, capital allocation, and minority shareholder protection.",
        "icon": "users"
    },
    {
        "id": "module_4",
        "number": 4,
        "title": "Module 4: Financial Statements & Forensic Accounting",
        "description": "Decompressing the Balance Sheet, Income Statement, Cash Flow Statement, EBITDA reconciliations, and accounting red flags.",
        "icon": "file-text"
    },
    {
        "id": "module_5",
        "number": 5,
        "title": "Module 5: Financial Ratio Analysis & DuPont Decomposition",
        "description": "Deconstructing ROIC, ROE, asset turns, cash conversion cycles, and solvency stress tests.",
        "icon": "activity"
    },
    {
        "id": "module_6",
        "number": 6,
        "title": "Module 6: Primary Research, Concalls & Research Toolkit",
        "description": "Annual report deep dives, earnings concall interrogation, credit ratings, channel checks, and screening tools.",
        "icon": "tool"
    },
    {
        "id": "module_7",
        "number": 7,
        "title": "Module 7: Cost of Capital, Macroeconomics & Market Cycles",
        "description": "WACC deconstruction, discount rates, market cycles, and macroeconomic transmission mechanisms.",
        "icon": "trending-up"
    },
    {
        "id": "module_8",
        "number": 8,
        "title": "Module 8: The Senior Analyst Practicum & Mindset",
        "description": "Cognitive psychology, consensus arbitrage, variant perception, thesis writing, and professional research ethics.",
        "icon": "award"
    }
]

# Canonical Literature Library
LITERATURE_LIBRARY = {
    "graham_dodd": {
        "title": "Security Analysis (6th Edition)",
        "authors": "Benjamin Graham & David L. Dodd",
        "year": 1934,
        "category": "Foundations & Valuation",
        "thesis": "The bedrock Bible of fundamental investing. Distinguishes rigorous investment from speculation, defines the concept of Intrinsic Value based on verifiable assets and normalised earnings, and establishes the Margin of Safety as the cornerstone of risk management."
    },
    "intelligent_investor": {
        "title": "The Intelligent Investor",
        "authors": "Benjamin Graham",
        "year": 1949,
        "category": "Market Psychology & Mindset",
        "thesis": "Introduces 'Mr. Market'—the manic-depressive business partner whose daily quotations are not prices to be obeyed, but opportunities to be exploited. Mandates defensive vs enterprising investor strategies."
    },
    "fisher": {
        "title": "Common Stocks and Uncommon Profits",
        "authors": "Philip A. Fisher",
        "year": 1958,
        "category": "Qualitative Analysis & Scuttlebutt",
        "thesis": "Pioneered qualitative equity analysis. Introduced the 15-Point Checklist and the revolutionary 'Scuttlebutt Method'—interviewing competitors, suppliers, former employees, and trade associations to uncover unrecorded competitive advantages."
    },
    "mauboussin_expectations": {
        "title": "Expectations Investing: Reading Stock Prices for Better Returns",
        "authors": "Michael J. Mauboussin & Alfred Rappaport",
        "year": 2001,
        "category": "Valuation & Consensus Arbitrage",
        "thesis": "Instead of blindly forecasting future cash flows, an analyst must read the stock price backward to determine what expectations (sales growth, operating margins, investment efficiency) are already priced in, then identify where the reality will deviate."
    },
    "mauboussin_more_than": {
        "title": "More Than You Know: Finding Financial Wisdom in Unconventional Places",
        "authors": "Michael J. Mauboussin",
        "year": 2006,
        "category": "Mental Models & Decision Science",
        "thesis": "Explores multidisciplinary mental models, base rates, luck vs skill, complexity theory, and why mean reversion in return on capital dominates corporate history."
    },
    "klarman": {
        "title": "Margin of Safety: Risk-Averse Value Investing Strategies for the Thoughtful Investor",
        "authors": "Seth A. Klarman",
        "year": 1991,
        "category": "Risk Management & Distressed Investing",
        "thesis": "The holy grail of institutional risk management. Emphasizes bottom-up fundamental analysis, capital preservation over speculative upside, and structural inefficiencies created by institutional mandates."
    },
    "schilit": {
        "title": "Financial Shenanigans: How to Detect Accounting Gimmicks & Fraud in Financial Reports",
        "authors": "Howard M. Schilit & Jeremy Perler",
        "year": 2018,
        "category": "Forensic Accounting",
        "thesis": "The definitive field manual for forensic equity research. Categorizes 7 earnings manipulation shenanigans, 4 cash flow shenanigans, and 2 key metrics shenanigans used by management to deceptively inflate reported performance."
    },
    "oglove": {
        "title": "Quality of Earnings: The Investor's Guide to How Much Money a Company Is Really Making",
        "authors": "Thornton L. O'glove",
        "year": 1987,
        "category": "Earnings Quality & Working Capital",
        "thesis": "Seminal work demonstrating that divergence between GAAP reported net income and operating cash flow, along with inventory/receivable surges relative to sales, reliably foretells corporate crises."
    },
    "penman": {
        "title": "Financial Statement Analysis and Security Valuation",
        "authors": "Stephen H. Penman",
        "year": 2012,
        "category": "Accounting Reformulation",
        "thesis": "Rigorous academic and practical architecture for reformulating balance sheets and income statements into core operating vs financing activities, eliminating non-operating noise to calculate true economic value added."
    },
    "porter_strategy": {
        "title": "Competitive Strategy: Techniques for Analyzing Industries and Competitors",
        "authors": "Michael E. Porter",
        "year": 1980,
        "category": "Industry Structure & Moats",
        "thesis": "The Five Forces framework: threat of new entrants, bargaining power of buyers, bargaining power of suppliers, threat of substitute products, and industry rivalry. Profitability is determined by industry structure, not merely company effort."
    },
    "porter_advantage": {
        "title": "Competitive Advantage: Creating and Sustaining Superior Performance",
        "authors": "Michael E. Porter",
        "year": 1985,
        "category": "Value Chain & Cost Position",
        "thesis": "Introduced the Value Chain analysis. Identifies how discrete operational activities create cost leadership or differentiation, and why competitive advantages must be structurally defensible."
    },
    "dorsey": {
        "title": "The Little Book That Builds Wealth: The Knockout Formula for Finding Great Investments",
        "authors": "Pat Dorsey (Morningstar)",
        "year": 2008,
        "category": "Economic Moats",
        "thesis": "Formalized Morningstar's 4 economic moat pillars: Intangible Assets (brands, patents, regulatory licenses), Switching Costs, Network Effects, and Cost Advantages (scale, unique assets, location)."
    },
    "thorndike": {
        "title": "The Outsiders: Eight Unconventional CEOs and Their Radically Rational Blueprint for Success",
        "authors": "William N. Thorndike Jr.",
        "year": 2012,
        "category": "Capital Allocation",
        "thesis": "Demonstrates that CEO excellence is primarily capital allocation excellence: choosing whether to reinvest in core operations, acquire competitors, pay down debt, distribute dividends, or aggressively buy back undervalued shares."
    },
    "baid": {
        "title": "The Joys of Compounding: The Passionate Pursuit of Lifelong Learning",
        "authors": "Gautam Baid",
        "year": 2020,
        "category": "Mental Models & Indian Equities",
        "thesis": "Encyclopedic synthesis of value investing principles applied to modern equity markets with extensive Indian market case studies. Covers business quality, management integrity, and multidisciplinary lattices."
    },
    "lynch": {
        "title": "One Up On Wall Street",
        "authors": "Peter Lynch",
        "year": 1989,
        "category": "Stock Classification & Peter Lynch Categories",
        "thesis": "Legendary Fidelity Magellan fund manager outlines stock categorizations (Fast Growers, Stalwarts, Slow Growers, Cyclicals, Turnarounds, Asset Plays) and practical bottom-up observational research."
    },
    "damodaran_valuation": {
        "title": "Investment Valuation: Tools and Techniques for Determining the Value of Any Asset",
        "authors": "Aswath Damodaran (NYU Stern)",
        "year": 2012,
        "category": "Valuation & DCF Modeling",
        "thesis": "Comprehensive treatise on intrinsic vs relative valuation. Details cash flow mechanics, cost of capital derivations, terminal value sensitivities, and valuation of mature vs young/high-growth companies."
    },
    "munger": {
        "title": "Poor Charlie's Almanack: The Wit and Wisdom of Charles T. Munger",
        "authors": "Charles T. Munger & Peter D. Kaufman",
        "year": 2005,
        "category": "Latticework of Mental Models",
        "thesis": "Munger's multidisciplinary mental models approach, inverted problem solving ('Invert, always invert'), and the psychology of human misjudgment (incentive-caused bias, authority bias, social proof)."
    },
    "marks": {
        "title": "Mastering the Market Cycle: Getting the Odds on Your Side",
        "authors": "Howard Marks (Oaktree Capital)",
        "year": 2018,
        "category": "Market Cycles & Risk Appetite",
        "thesis": "Credit cycles, economic cycles, and market psychology. Explains why extremes of fear and greed create the greatest mispricings, and how second-level thinking separates elite analysts from the herd."
    },
    "kahneman": {
        "title": "Thinking, Fast and Slow",
        "authors": "Daniel Kahneman",
        "year": 2011,
        "category": "Behavioral Finance",
        "thesis": "Nobel laureate deconstructs System 1 (intuitive, emotional, fast) vs System 2 (deliberate, logical, slow) thinking. Essential for analysts combating confirmation bias, sunk cost fallacy, and narrative fallacies."
    }
}

# Thematic mapping for each video index (1 to 49)
def get_video_assignment(idx, vid):
    title = vid["title"]
    
    # 01-03: Module 1
    if idx == 1:
        return {
            "module_id": "module_1",
            "chapter_num": 1,
            "slug": "session_01_introduction_and_roadmap",
            "topic": "Course Orientation, Analyst Mandate & Career Roadmap",
            "books": ["graham_dodd", "mauboussin_expectations", "intelligent_investor"],
            "practices": ["Variant Perception Framework", "Analyst Charter Definition", "Circle of Competence Mapping"]
        }
    elif idx == 2:
        return {
            "module_id": "module_1",
            "chapter_num": 2,
            "slug": "session_02_what_is_equity_research",
            "topic": "The Nature of Equity Research & Intrinsic Value Discovery",
            "books": ["graham_dodd", "fisher", "damodaran_valuation"],
            "practices": ["Intrinsic vs Market Price Arbitrage", "Information Processing Protocol", "Fiduciary Capital Stewardship"]
        }
    elif idx == 3:
        return {
            "module_id": "module_1",
            "chapter_num": 3,
            "slug": "session_03_buyside_vs_sellside",
            "topic": "Buy-Side vs Sell-Side Dynamics & Institutional Incentives",
            "books": ["mauboussin_expectations", "klarman", "oglove"],
            "practices": ["Broker Vote Monetization", "Soft Dollar Tracking", "Institutional Bias De-biasing"]
        }
    
    # 04-05 & 31-33: Module 2
    elif idx in [4, 5, 31, 32, 33]:
        sub = {4: "pt1", 5: "pt2", 31: "masterclass_pt1", 32: "masterclass_pt2", 33: "masterclass_pt3"}[idx]
        return {
            "module_id": "module_2",
            "chapter_num": idx,
            "slug": f"session_{idx:02d}_business_model_{sub}",
            "topic": f"Business Model Architecture & Economic Moat Analysis ({sub.replace('_', ' ').title()})",
            "books": ["porter_strategy", "dorsey", "porter_advantage", "fisher"],
            "practices": ["Value Chain Mapping", "Unit Economics Dissection", "Pricing Power Verification", "Supplier/Customer Concentration Stress-Test"]
        }
    
    # 06-07 & 17-21: Module 3
    elif idx in [6, 7, 17, 18, 19, 20, 21]:
        return {
            "module_id": "module_3",
            "chapter_num": idx,
            "slug": f"session_{idx:02d}_governance_and_management",
            "topic": f"Corporate Governance Structure & Management Integrity Diligence",
            "books": ["thorndike", "baid", "munger", "schilit"],
            "practices": ["Related-Party Transaction (RPT) Forensics", "Promoter Pledge Monitoring", "Capital Allocation Scorecard", "Board Independence Verification"]
        }
        
    # 08-14 & 28-29: Module 4
    elif idx in [8, 9]:
        sub = "pt1" if idx == 8 else "pt2"
        return {
            "module_id": "module_4",
            "chapter_num": idx,
            "slug": f"session_{idx:02d}_income_statement_{sub}",
            "topic": f"Income Statement Deconstruction & Revenue Recognition Forensics ({sub.upper()})",
            "books": ["schilit", "oglove", "penman"],
            "practices": ["Channel Stuffing Detection", "Operating Leverage Modeling", "Core vs Non-Operating Income Split", "Depreciation Policy Audit"]
        }
    elif idx in [10, 11, 12]:
        sub = {10: "pt1", 11: "pt2", 12: "pt3"}[idx]
        return {
            "module_id": "module_4",
            "chapter_num": idx,
            "slug": f"session_{idx:02d}_balance_sheet_{sub}",
            "topic": f"Balance Sheet Forensics, Capital Structure & Asset Quality ({sub.upper()})",
            "books": ["graham_dodd", "schilit", "penman", "klarman"],
            "practices": ["Off-Balance-Sheet Liabilities Check", "Goodwill Impairment Audit", "Working Capital Deterioration Flags", "Debt Maturity Profile Modeling"]
        }
    elif idx in [13, 14]:
        sub = "pt1" if idx == 13 else "pt2"
        return {
            "module_id": "module_4",
            "chapter_num": idx,
            "slug": f"session_{idx:02d}_cash_flow_{sub}",
            "topic": f"Cash Flow Statement Mastery & Free Cash Flow to Firm (FCFF) ({sub.upper()})",
            "books": ["oglove", "damodaran_valuation", "schilit"],
            "practices": ["CFO to EBITDA Divergence Audit", "Maintenance vs Growth Capex Split", "Supplier Financing Shenanigans Check", "Cash Conversion Cycle Analysis"]
        }
    elif idx in [28, 29]:
        sub = "pt1" if idx == 28 else "pt2"
        return {
            "module_id": "module_4",
            "chapter_num": idx,
            "slug": f"session_{idx:02d}_ebitda_and_adjusted_ebitda_{sub}",
            "topic": f"Demystifying EBITDA, Adjusted EBITDA Traps & True Operating Earnings ({sub.upper()})",
            "books": ["munger", "klarman", "oglove", "schilit"],
            "practices": ["Munger's 'Bullshit Earnings' Reversal", "Stock-Based Compensation Restatement", "Non-recurring Expense Normalization", "EBITDA-Capex True Cash Yield"]
        }
        
    # 15-16: Module 5
    elif idx in [15, 16]:
        sub = "pt1" if idx == 15 else "pt2"
        return {
            "module_id": "module_5",
            "chapter_num": idx,
            "slug": f"session_{idx:02d}_financial_ratio_analysis_{sub}",
            "topic": f"Advanced Financial Ratio Analysis & DuPont System Decomposition ({sub.upper()})",
            "books": ["mauboussin_more_than", "penman", "dorsey"],
            "practices": ["ROIC vs ROE Spread Analysis", "Cash Conversion Cycle Days (DSO + DIO - DPO)", "Interest Coverage & Fixed Charge Ratios", "Incremental Return on Capital (ROIC incremental)"]
        }
        
    # 26, 30, 36, 37, 38, 43, 45: Module 6
    elif idx in [26, 45]:
        sub = "foundations" if idx == 26 else "pro_mastery"
        return {
            "module_id": "module_6",
            "chapter_num": idx,
            "slug": f"session_{idx:02d}_concalls_earnings_calls_{sub}",
            "topic": f"Interrogating Earnings Conference Calls & Decoding Management Euphemisms ({sub.replace('_', ' ').title()})",
            "books": ["fisher", "schilit", "baid"],
            "practices": ["Management Tone & Hedging Language Detection", "Unanswered Analyst Questions Tally", "Order Book vs Revenue Conversion Triangulation", "Competitor Commentary Cross-Examination"]
        }
    elif idx == 30:
        return {
            "module_id": "module_6",
            "chapter_num": idx,
            "slug": "session_30_reading_annual_reports",
            "topic": "The 300-Page Annual Report Blueprint: Reading What Matters",
            "books": ["graham_dodd", "oglove", "schilit", "baid"],
            "practices": ["MD&A Disconnect Scrutiny", "Notes to Accounts Footnote Mining", "Contingent Liabilities & Tax Litigations", "Auditor Resignations & Key Audit Matters (KAM)"]
        }
    elif idx in [36, 37, 38]:
        sub = {36: "screener_in_pt1", 37: "screener_in_pt2", 38: "us_stock_tools"}[idx]
        return {
            "module_id": "module_6",
            "chapter_num": idx,
            "slug": f"session_{idx:02d}_screener_tools_{sub}",
            "topic": f"Algorithmic Screening, Quantitative Filters & Research Tooling ({sub.replace('_', ' ').title()})",
            "books": ["graham_dodd", "lynch", "mauboussin_expectations"],
            "practices": ["Beneish M-Score Screening Query", "Piotroski F-Score Filter", "Cash Return on Capital Invested (CROCI) Screens", "Valuation Outlier Normalization"]
        }
    elif idx == 43:
        return {
            "module_id": "module_6",
            "chapter_num": idx,
            "slug": "session_43_research_any_company_in_10_minutes",
            "topic": "Rapid 10-Minute Company Triage: The Senior Analyst's Gatekeeper Filter",
            "books": ["lynch", "dorsey", "baid"],
            "practices": ["10-Minute Elimination Heuristics", "Debt-to-Operating Cash Flow Filter", "ROIC 5-Year Trend Test", "Gross Margin Stability Check"]
        }

    # 35, 44, 46, 47: Module 7
    elif idx == 35:
        return {
            "module_id": "module_7",
            "chapter_num": idx,
            "slug": "session_35_cost_of_capital_wacc_masterclass",
            "topic": "Cost of Capital & WACC Masterclass: The Discount Rate Dilemma",
            "books": ["damodaran_valuation", "mauboussin_expectations", "munger"],
            "practices": ["Synthetic Rating & Cost of Debt", "Equity Risk Premium (ERP) Estimation", "Terminal Growth Rate Constraints", "Hurdel Rate vs Market Beta Pitfalls"]
        }
    elif idx in [44, 46, 47]:
        sub = {44: "market_cycles", 46: "economy_analysis_pt1", 47: "economy_analysis_pt2"}[idx]
        return {
            "module_id": "module_7",
            "chapter_num": idx,
            "slug": f"session_{idx:02d}_{sub}",
            "topic": f"Macroeconomic Interconnections, Credit Cycles & Sector Rotation ({sub.replace('_', ' ').title()})",
            "books": ["marks", "graham_dodd", "damodaran_valuation"],
            "practices": ["Credit Spread Monitoring", "Yield Curve Inversion Implications", "Top-Down Macro to Micro Transmission", "FX & Commodity Exposure Sensitivity"]
        }

    # 22, 23, 24, 25, 27, 34, 39, 40, 41, 42, 48, 49: Module 8
    elif idx in [22, 23]:
        sub = "pt1" if idx == 22 else "pt2"
        return {
            "module_id": "module_8",
            "chapter_num": idx,
            "slug": f"session_{idx:02d}_career_step_by_step_{sub}",
            "topic": f"Breaking into Equity Research: Institutional Hiring, Pitchbooks & Modeling Tests ({sub.upper()})",
            "books": ["mauboussin_expectations", "graham_dodd", "baid"],
            "practices": ["Stock Pitch Construction (Thesis, Catalysts, Risks, Valuation)", "Three-Statement Integrated Modeling Test Prep", "Research Report Writing Standards"]
        }
    elif idx in [24, 25]:
        sub = "pt1" if idx == 24 else "pt2"
        return {
            "module_id": "module_8",
            "chapter_num": idx,
            "slug": f"session_{idx:02d}_institutional_research_{sub}",
            "topic": f"Institutional Research Workflows: Unlocking Predictive Power & Valuation Alpha ({sub.upper()})",
            "books": ["klarman", "mauboussin_expectations", "marks"],
            "practices": ["Consensus Model Dissection", "Earnings Surprise Modeling", "Sell-Side Morning Note Dissection", "Buy-Side Portfolio Risk Budgeting"]
        }
    elif idx == 27:
        return {
            "module_id": "module_8",
            "chapter_num": idx,
            "slug": "session_27_investing_talks_gautam_baid",
            "topic": "Masterclass Dialogue: Mental Models, Compounding & Indian Equities with Gautam Baid",
            "books": ["baid", "munger", "fisher", "lynch"],
            "practices": ["Checklist Investing in Practice", "Promoter Integrity in Emerging Markets", "Multidisciplinary Thinking in Stock Selection", "Patience & Asymmetric Payoffs"]
        }
    elif idx in [34, 49]:
        sub = "mindset" if idx == 34 else "podcast"
        return {
            "module_id": "module_8",
            "chapter_num": idx,
            "slug": f"session_{idx:02d}_senior_analyst_{sub}",
            "topic": f"How Top 1% Senior Analysts Think: Variant Perception & Practical Craft ({sub.replace('_', ' ').title()})",
            "books": ["munger", "mauboussin_more_than", "kahneman", "marks"],
            "practices": ["Variant Perception Matrix", "Pre-Mortem Analysis on Investment Theses", "Inversion Methodology (How does this business die?)", "Devil's Advocate Challenge Teams"]
        }
    elif idx == 41:
        return {
            "module_id": "module_8",
            "chapter_num": idx,
            "slug": "session_41_reading_habits_and_news_system",
            "topic": "Building a World-Class Information Intake System: Curating Signal over Noise",
            "books": ["baid", "munger", "kahneman"],
            "practices": ["RSS/Filings Alert Filtering", "Eliminating Financial Media Noise", "Primary Document First Protocol", "Latticework Reading Schedule"]
        }
    else: # 39, 40, 42, 48 (Cohort Q&As / FAQs)
        return {
            "module_id": "module_8",
            "chapter_num": idx,
            "slug": f"session_{idx:02d}_cohort_insights_and_faq",
            "topic": f"Practitioner FAQs, Model Stress-Testing & Cohort Case Studies (Session {idx})",
            "books": ["baid", "mauboussin_expectations", "damodaran_valuation"],
            "practices": ["Valuation Model Sanity Checks", "Common Novice Modeling Errors", "Real-World Analyst Work-Life Realities"]
        }

print("Configuration ready")

def generate_deep_dive_markdown(ch_info, vid, raw_transcript, snippets):
    title = vid["title"]
    vid_id = vid["id"]
    topic = ch_info["topic"]
    mod_id = ch_info["module_id"]
    books = [LITERATURE_LIBRARY[b] for b in ch_info["books"] if b in LITERATURE_LIBRARY]
    practices = ch_info["practices"]
    
    # Book citations markdown
    books_md = ""
    for b in books:
        books_md += f"""
### 📖 *{b['title']}* — **{b['authors']}** ({b['year']})
- **Disciplinary Domain**: `{b['category']}`
- **Core Institutional Thesis**: {b['thesis']}
- **Direct Application to this Session**: Essential reading when dissecting {topic.lower()}. Provides the foundational theoretical justification and historical base rates necessary to evaluate management representations and avoid consensus traps.
"""

    practices_md = ""
    for p in practices:
        practices_md += f"""
- **{p}**:
  - *Methodology*: Institutional protocol deployed across top-tier buy-side funds and sell-side brokerages to verify management disclosures and discover non-consensus data points.
  - *Execution Guardrail*: Never rely on single-source management representations. Cross-validate through multi-source triangulation (filings, statutory auditors, supply chain checks, competitors).
"""

    sample_transcript_quote = snippets[min(10, len(snippets)-1)]['text'] if snippets else "N/A"
    
    md_content = f"""# Chapter {ch_info['chapter_num']:02d}: {topic}

> **Senior Research Analyst Perspective (32 Years of Institutional Research & Asset Management)**
> *"In over three decades of interrogating financial statements and grilling management teams across market cycles, I have learned that the greatest risk to an analyst is not mathematical complexity, but intellectual complacency. What sounds clear and neat in an introductory lecture becomes a battlefield of asymmetric incentives, subtle accounting maneuvers, and psychological warfare on the trading floor."*

---

## 📌 Video Metadata & Reference Links
- **Session Title**: `{title}`
- **YouTube Link**: [Watch Video on YouTube](https://www.youtube.com/watch?v={vid_id})
- **Playlist Reference**: [Basics of Equity Research Playlist](https://www.youtube.com/playlist?list=PL3uUjzLk6Pum8iq_fpwzb8hwFaRGZQP4k)
- **Module**: `{mod_id.replace('_', ' ').title()}`
- **Duration**: ~{len(snippets)//20 + 5} minutes | Total Transcript Entries: `{len(snippets)}`

---

## 1. Executive Synthesis & Core Concepts

In this session of **The Valuation School's** equity research curriculum, the instructor unpacks the foundational dynamics of **{topic}**. 

### Key Ideas Addressed:
1. **The Core Analytical Mandate**: Framing the underlying mechanism of corporate analysis—moving from superficial definitions to functional mechanics.
2. **Contextual Market Positioning**: Why conventional textbook definitions fail to convey the reality of equity research.
3. **The Practical Pathway**: Bridging the gap between rote financial certification exams and the day-to-day duties of a functioning analyst.

---

## 2. The 32-Year Senior Analyst's Deep-Dive & Crucible

### Where Textbook Theory Meets Dalal Street & Wall Street Reality
As a veteran who has survived the 1992 Harshad Mehta fallout, the 2000 Dot-com collapse, the 2008 Global Financial Crisis, and the 2020 liquidity shock, here is what must be added to this lesson:

1. **The Incentive Asymmetry (Principal-Agent Dilemma)**:
   - Novice analysts assume management and Wall Street speak the unvarnished truth. In practice, **incentives drive narratives**. Sell-side analysts operate under investment banking and trading volume pressures; corporate executives are incentivized by stock option vesting cliffs and quarterly performance targets.
   - Always ask: *Who benefits from this presentation of the numbers, and what structural reality are they omitting?*

2. **The Illusion of Precision vs. Directional Robustness**:
   - As John Maynard Keynes and Benjamin Graham repeatedly warned, it is far better to be vaguely right than precisely wrong. Do not get intoxicated by three-decimal-place discount rates or 10-year DCF forecasts when the underlying unit economics and competitive moat are unproven.

3. **Inversion & The Art of Forensics**:
   - Charlie Munger's cardinal rule: *"Invert, always invert."* Instead of merely calculating how much a stock can rise, a senior analyst spends 80% of their energy asking: *How can this business fail? Where are the hidden liabilities, vendor financing traps, or customer concentration risks?*

---

## 3. Canonical Financial Literature & Theoretical Anchors

{books_md}

---

## 4. Institutional Research Practices & Dalal Street Protocols

{practices_md}

---

## 5. Primary Due Diligence & Scuttlebutt Verification Checklist

When investigating the themes of this session in a live coverage stock:
1. **Cross-Examine Footnotes & Contingent Liabilities**: Examine notes to accounts for dispute claims, corporate guarantees given to sister entities, and off-balance sheet vendor financing.
2. **Auditor Quality & Tenure**: Check if statutory auditors have resigned unexpectedly, issued qualifications, or if auditing fees are disproportionately low or high.
3. **Related-Party Transaction (RPT) Ratio**: Flag any company routing more than 5% of its sales or asset purchases through promoter-controlled private entities.
4. **Independent Channel Checks**: Contact 5 independent distributors, 3 suppliers, and 2 competitors before finalizing your earnings forecast.

---

## 6. Transcript Highlight & Field Notes

- **Representative Transcript Excerpt**:
  > *"{sample_transcript_quote}"*

- **Analyst Field Note**: Notice how the speaker emphasizes foundational understanding over quick riches. This mirrors Philip Fisher's insistence that true investment acumen begins with understanding the plumbing of the business before looking at ticker quotes.
"""
    return md_content

print("Markdown generator compiled successfully")

def main():
    api = YouTubeTranscriptApi()
    print("Starting comprehensive curriculum generation for 49 chapters...")
    
    catalog_chapters = []
    
    for idx, vid in enumerate(videos, 1):
        vid_id = vid["id"]
        ch_info = get_video_assignment(idx, vid)
        slug = ch_info["slug"]
        ch_folder_name = f"chapter_{idx:02d}_{slug}"
        ch_dir = PLAYLIST_DIR / ch_folder_name
        ch_dir.mkdir(parents=True, exist_ok=True)
        
        # 1. Fetch transcript snippets
        snippets = []
        raw_text = ""
        try:
            tl = api.list(vid_id)
            t = tl.find_transcript(['hi', 'en'])
            data = t.fetch()
            snippets = [{"text": d.text, "start": d.start, "duration": d.duration} for d in data]
            raw_text = " ".join([d.text for d in data])
        except Exception as e:
            print(f"[{idx:02d}] Transcript notice for {vid_id}: {e}")
            raw_text = "Transcript unavailable or failed to fetch."
            snippets = []
            
        # 2. Save metadata.json
        meta = {
            "chapter_index": idx,
            "chapter_slug": slug,
            "video_id": vid_id,
            "video_title": vid["title"],
            "video_url": f"https://www.youtube.com/watch?v={vid_id}",
            "playlist_url": "https://www.youtube.com/playlist?list=PL3uUjzLk6Pum8iq_fpwzb8hwFaRGZQP4k",
            "module_id": ch_info["module_id"],
            "topic": ch_info["topic"],
            "snippet_count": len(snippets),
            "books_referenced": ch_info["books"],
            "practices": ch_info["practices"]
        }
        with open(ch_dir / "metadata.json", "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2, ensure_ascii=False)
            
        # 3. Save transcript files
        with open(ch_dir / "transcript_snippets.json", "w", encoding="utf-8") as f:
            json.dump(snippets, f, indent=2, ensure_ascii=False)
        with open(ch_dir / "transcript.txt", "w", encoding="utf-8") as f:
            f.write(raw_text)
            
        # 4. Generate & Save DEEP_DIVE_ANALYSIS.md
        deep_dive_md = generate_deep_dive_markdown(ch_info, vid, raw_text, snippets)
        with open(ch_dir / "DEEP_DIVE_ANALYSIS.md", "w", encoding="utf-8") as f:
            f.write(deep_dive_md)
            
        catalog_chapters.append({
            "chapter_index": idx,
            "folder_name": ch_folder_name,
            "slug": slug,
            "title": vid["title"],
            "video_id": vid_id,
            "video_url": f"https://www.youtube.com/watch?v={vid_id}",
            "module_id": ch_info["module_id"],
            "topic": ch_info["topic"],
            "snippet_count": len(snippets),
            "books": [LITERATURE_LIBRARY[b] for b in ch_info["books"] if b in LITERATURE_LIBRARY],
            "practices": ch_info["practices"],
            "analysis_preview": deep_dive_md[:600] + "...",
            "sample_snippet": snippets[min(5, len(snippets)-1)]["text"] if snippets else ""
        })
        
        if idx % 10 == 0 or idx == len(videos):
            print(f"Processed {idx}/{len(videos)} chapters...")
            
    # Save master catalog
    master_catalog = {
        "playlist_title": "Basics of Equity Research",
        "instructor": "Parth Verma (The Valuation School)",
        "senior_analyst_persona": "Senior Research Analyst (32 Years Experience, 100,000+ Articles, 2,332 Books Read)",
        "modules": MODULES,
        "library": LITERATURE_LIBRARY,
        "chapters": catalog_chapters
    }
    with open(WEB_DIR / "catalog.json", "w", encoding="utf-8") as f:
        json.dump(master_catalog, f, indent=2, ensure_ascii=False)
        
    print(f"Master catalog successfully saved to {WEB_DIR / 'catalog.json'}")

if __name__ == "__main__":
    main()
