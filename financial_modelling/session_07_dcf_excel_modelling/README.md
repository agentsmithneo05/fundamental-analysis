# Session 7: Discounted Cash Flow (DCF) Valuation Modeling

> **Financial Modeling & Valuation Series**  
> *Curated directly from the lecture discussions of Parth Verma (The Valuation School) with institutional modeling architecture, Excel formulas, financial mechanics, and practical corporate finance scenarios.*

---

## 📌 Video Metadata & Quick Reference
- **Title**: `DCF Excel Modelling | Step by Step - Session 7  | Investment Banking`
- **YouTube Link**: [Watch Video on YouTube](https://www.youtube.com/watch?v=pdveRcJucX4)
- **Playlist Reference**: [Learn Financial Modelling - Step by Step](https://www.youtube.com/playlist?list=PL3uUjzLk6PulhRop_ffNeHyK0kprzO4cT)
- **Session Number**: `07 of 34`
- **Video ID**: `pdveRcJucX4`
- **Duration**: `49m 2s`

---

## 1. Core Lecture Discussion & Concepts

In this session, Parth Verma systematically deconstructs the foundational, mathematical, and modeling mechanics of **Session 7: Discounted Cash Flow (DCF) Valuation Modeling**. 

### Primary Themes Addressed by the Instructor:
- **Theoretical foundation of DCF: The value of an operating business equals the present value of its future unlevered free cash flows discounted at the firm's WACC**
- **Unlevered Free Cash Flow (FCFF) calculation: EBIT * (1 - Tax Rate) + D&A - Capex - Change in Non-Cash Working Capital**
- **Explicit Forecast Period (typically 5 to 10 years) based on company maturity and competitive visibility**
- **Terminal Value calculation methods: Gordon Growth Model (Perpetuity Growth) vs Exit Multiple Method (EV/EBITDA)**
- **Reconciling Enterprise Value (EV) to Equity Value: EV - Net Debt - Minority Interest - Preferred Stock + Non-Operating Assets = Equity Value**

---

## 2. Key Formulas, Mechanics & Excel Architecture

The quantitative framework and spreadsheet implementations taught in this session include:

- `FCFF = EBIT * (1 - t) + Depreciation - Capex - ΔNWC`
- `Terminal Value (Gordon Growth) = (FCFF_{n+1}) / (WACC - g) = FCFF_n * (1 + g) / (WACC - g)`
- `Discount Factor_t = 1 / (1 + WACC)^t (or mid-year convention: 1 / (1 + WACC)^(t - 0.5))`
- `Implied Share Price = Equity Value / Diluted Shares Outstanding`

---

## 3. Real-World Context & Detailed Modeling Scenarios

To translate the lecture discussion into actionable institutional understanding, consider the following practical scenarios and modeling practices:

- Valuing an Indian IT firm: Modeling 5-year explicit FCFF of ₹2,500 Cr to ₹4,000 Cr; Terminal growth rate pegged at 5.0% (aligned with long-term nominal Indian GDP minus 1-2%); WACC computed at 11.5%.
- Reconciliation of Bridge: Showing how ₹50,000 Cr Enterprise Value translates to ₹55,000 Cr Equity Value after adding ₹7,000 Cr net cash and subtracting ₹2,000 Cr minority interest.

---

## 4. Practical Practitioner Takeaways

1. Terminal value typically represents 60% to 80% of total enterprise value in a DCF; small changes in terminal growth rate or WACC cause massive swings.
2. Always check that the perpetual growth rate does not exceed the long-term risk-free rate or GDP growth of the operating economy.

