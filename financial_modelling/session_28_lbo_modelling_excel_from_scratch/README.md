# Session 28: LBO Modeling in Excel from Scratch - Core Architecture

> **Financial Modeling & Valuation Series**  
> *Curated directly from the lecture discussions of Parth Verma (The Valuation School) with institutional modeling architecture, Excel formulas, financial mechanics, and practical corporate finance scenarios.*

---

## 📌 Video Metadata & Quick Reference
- **Title**: `Learn LBO MODELLING in Excel from Scratch | Full Course`
- **YouTube Link**: [Watch Video on YouTube](https://www.youtube.com/watch?v=saQWSw6F6T8)
- **Playlist Reference**: [Learn Financial Modelling - Step by Step](https://www.youtube.com/playlist?list=PL3uUjzLk6PulhRop_ffNeHyK0kprzO4cT)
- **Session Number**: `28 of 34`
- **Video ID**: `saQWSw6F6T8`
- **Duration**: `16m 6s`

---

## 1. Core Lecture Discussion & Concepts

In this session, Parth Verma systematically deconstructs the foundational, mathematical, and modeling mechanics of **Session 28: LBO Modeling in Excel from Scratch - Core Architecture**. 

### Primary Themes Addressed by the Instructor:
- **Setting up the LBO model tabs and structure: Transaction Assumptions, Sources & Uses of Funds, Forecast Financials, Debt Schedule & Waterfall, and Returns Summary**
- **Transaction Assumptions: Entry Multiple (EV/EBITDA), Purchase Price, Transaction Fees, and Financing Structure (% Senior Debt, % Subordinated Debt, % Sponsor Equity)**
- **Building the Sources & Uses Table: Sources (Debt tranches, Rollover Equity, Sponsor Equity) must EXACTLY equal Uses (Purchase Enterprise Value, Refinancing Existing Debt, Transaction & Financing Fees)**
- **The core logic of the balance sheet adjustments on Day 1 of the buyout (Goodwill creation, debt refinancing, equity wipeout)**
- **Basic debt paydown modeling using Free Cash Flow**

---

## 2. Key Formulas, Mechanics & Excel Architecture

The quantitative framework and spreadsheet implementations taught in this session include:

- `Total Enterprise Value = LTM EBITDA * Entry EV/EBITDA Multiple`
- `Sponsor Equity (Plug) = Total Uses - Total Debt Sources - Rollover Equity`
- `Sources & Uses Check: Total Sources - Total Uses MUST equal 0.00`
- `Free Cash Flow Available for Debt Service (CFADS) = CFO - Capex - Minimum Cash Balance Requirement`

---

## 3. Real-World Context & Detailed Modeling Scenarios

To translate the lecture discussion into actionable institutional understanding, consider the following practical scenarios and modeling practices:

- Sources & Uses setup: Target EBITDA = ₹100 Cr; Entry multiple = 10.0x -> Purchase EV = ₹1,000 Cr. Existing debt to refinance = ₹150 Cr. Fees = ₹30 Cr. Total Uses = ₹1,180 Cr. Sources: Senior Term Loan (4.0x EBITDA) = ₹400 Cr; Mezzanine Debt (2.0x EBITDA) = ₹200 Cr; Sponsor Equity = ₹580 Cr (balancing plug).
- Transaction fee capitalization vs expensing: Modeling advisory fees expensed through retained earnings vs financing fees capitalized and amortized over the debt tenure.

---

## 4. Practical Practitioner Takeaways

1. The Sources & Uses table is the mathematical anchor of every LBO; a single unlinked fee throws off the opening balance sheet.
2. Sponsor equity is always the residual balancing figure after all debt financing capacity is exhausted.

