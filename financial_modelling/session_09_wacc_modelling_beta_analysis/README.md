# Session 9: What is Beta? Regression, Levering & Unlevering Beta

> **Financial Modeling & Valuation Series**  
> *Curated directly from the lecture discussions of Parth Verma (The Valuation School) with institutional modeling architecture, Excel formulas, financial mechanics, and practical corporate finance scenarios.*

---

## 📌 Video Metadata & Quick Reference
- **Title**: `What is Beta? Master WACC Modelling -2 | DCF Modelling | Session 9 | Investment Banking`
- **YouTube Link**: [Watch Video on YouTube](https://www.youtube.com/watch?v=qRri_spNhHo)
- **Playlist Reference**: [Learn Financial Modelling - Step by Step](https://www.youtube.com/playlist?list=PL3uUjzLk6PulhRop_ffNeHyK0kprzO4cT)
- **Session Number**: `09 of 34`
- **Video ID**: `qRri_spNhHo`
- **Duration**: `50m 2s`

---

## 1. Core Lecture Discussion & Concepts

In this session, Parth Verma systematically deconstructs the foundational, mathematical, and modeling mechanics of **Session 9: What is Beta? Regression, Levering & Unlevering Beta**. 

### Primary Themes Addressed by the Instructor:
- **Theoretical definition of Beta: Systematic, non-diversifiable market risk relative to the market benchmark**
- **Raw Historical Beta vs Adjusted (Bloomberg / Blume) Beta: Formula = (2/3) * Raw Beta + (1/3) * 1.0**
- **Calculating Beta in Excel: SLOPE function using 3 to 5 years of weekly or monthly percentage stock returns vs Nifty 50 / S&P BSE 500**
- **Unlevering Beta: Stripping out financial risk (debt leverage) to determine Pure Business / Asset Risk**
- **Re-levering Beta: Applying target or company-specific capital structure to find the appropriate operational Beta**

---

## 2. Key Formulas, Mechanics & Excel Architecture

The quantitative framework and spreadsheet implementations taught in this session include:

- `Excel Beta Formula: =SLOPE(Stock_Returns_Array, Market_Returns_Array)`
- `Unlevered Beta (Asset Beta) = Levered Beta / (1 + (1 - Tax_Rate) * (Debt / Equity))`
- `Re-levered Beta = Unlevered Beta * (1 + (1 - Tax_Rate) * (Target_Debt / Target_Equity))`

---

## 3. Real-World Context & Detailed Modeling Scenarios

To translate the lecture discussion into actionable institutional understanding, consider the following practical scenarios and modeling practices:

- Unlevering peer betas for an unlisted company: Analyzing listed peers (e.g. Titan, Kalyan, Senco); extracting their levered betas, unlevering them based on their respective D/E ratios to find median industry Asset Beta, then re-levering at the target firm's capital structure.
- Impact of high financial leverage: Two companies in the same industry with identical business risk; Company A has D/E of 0.2x (Beta 1.1), while Company B has D/E of 1.5x (Beta 2.1). Company B's high beta is driven by financial risk, not operational difference.

---

## 4. Practical Practitioner Takeaways

1. Historical regression beta is backward-looking and heavily influenced by the chosen benchmark and time window; institutional analysts unlever peer betas to find pure industry risk.
2. Adjusted beta accounts for the empirical tendency of betas to regress toward the market mean of 1.0 over long horizons.

