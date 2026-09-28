# Session 8: Weighted Average Cost of Capital (WACC) Modeling - Part 1

> **Financial Modeling & Valuation Series**  
> *Curated directly from the lecture discussions of Parth Verma (The Valuation School) with institutional modeling architecture, Excel formulas, financial mechanics, and practical corporate finance scenarios.*

---

## 📌 Video Metadata & Quick Reference
- **Title**: `Master WACC Modelling | DCF Modelling | Session - 8 | Investment Banking`
- **YouTube Link**: [Watch Video on YouTube](https://www.youtube.com/watch?v=Pp_qhxHUziQ)
- **Playlist Reference**: [Learn Financial Modelling - Step by Step](https://www.youtube.com/playlist?list=PL3uUjzLk6PulhRop_ffNeHyK0kprzO4cT)
- **Session Number**: `08 of 34`
- **Video ID**: `Pp_qhxHUziQ`
- **Duration**: `40m 5s`

---

## 1. Core Lecture Discussion & Concepts

In this session, Parth Verma systematically deconstructs the foundational, mathematical, and modeling mechanics of **Session 8: Weighted Average Cost of Capital (WACC) Modeling - Part 1**. 

### Primary Themes Addressed by the Instructor:
- **Understanding WACC as the blended hurdle rate required by all capital providers (equity and debt)**
- **Capital Asset Pricing Model (CAPM) for Cost of Equity: Ke = Rf + Beta * (Rm - Rf)**
- **Risk-Free Rate (Rf) selection: Using the 10-year Government of India (G-Sec) bond yield for Indian assets**
- **Equity Risk Premium (ERP): Historical market return minus risk-free rate (typically 5.5% to 7.0% for Indian markets)**
- **Capital structure weightings: Market value of equity vs Book/Market value of debt**

---

## 2. Key Formulas, Mechanics & Excel Architecture

The quantitative framework and spreadsheet implementations taught in this session include:

- `WACC = (We * Ke) + (Wd * Kd * (1 - t))`
- `Cost of Equity (Ke) = Rf + Beta * ERP`
- `We = Market Cap / (Market Cap + Total Debt)`
- `Wd = Total Debt / (Market Cap + Total Debt)`

---

## 3. Real-World Context & Detailed Modeling Scenarios

To translate the lecture discussion into actionable institutional understanding, consider the following practical scenarios and modeling practices:

- Indian manufacturing firm WACC calculation: Rf = 7.10% (10-Yr G-Sec), ERP = 6.0%, Beta = 1.15 -> Ke = 7.10% + 1.15*(6.0%) = 14.0%. Kd = 9.0%, Tax rate = 25.17% -> After-tax Kd = 6.73%. Weights: 75% Equity, 25% Debt -> WACC = (0.75 * 14.0%) + (0.25 * 6.73%) = 10.5% + 1.68% = 12.18%.
- The market value fallacy: Why novice modelers mistakenly use book value of equity (Net Worth) instead of market capitalization, artificially distorting debt weight and understating WACC.

---

## 4. Practical Practitioner Takeaways

1. Always use market values for capital weights; book equity represents historical retained capital, not current economic opportunity cost.
2. WACC reflects the risk of the cash flows being generated, not the funding structure of a specific project.

