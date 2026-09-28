# Session 1: Introduction to Financial Modeling & Excel Foundation

> **Financial Modeling & Valuation Series**  
> *Curated directly from the lecture discussions of Parth Verma (The Valuation School) with institutional modeling architecture, Excel formulas, financial mechanics, and practical corporate finance scenarios.*

---

## 📌 Video Metadata & Quick Reference
- **Title**: `Learn Financial Modelling - Step by Step`
- **YouTube Link**: [Watch Video on YouTube](https://www.youtube.com/watch?v=QhBLvRu2XSI)
- **Playlist Reference**: [Learn Financial Modelling - Step by Step](https://www.youtube.com/playlist?list=PL3uUjzLk6PulhRop_ffNeHyK0kprzO4cT)
- **Session Number**: `01 of 34`
- **Video ID**: `QhBLvRu2XSI`
- **Duration**: `41m 11s`

---

## 1. Core Lecture Discussion & Concepts

In this session, Parth Verma systematically deconstructs the foundational, mathematical, and modeling mechanics of **Session 1: Introduction to Financial Modeling & Excel Foundation**. 

### Primary Themes Addressed by the Instructor:
- **What is Financial Modeling and why it is the core operating system of Investment Banking, Equity Research, Corporate Finance, and PE**
- **Financial Modeling vs Accounting: Modeling as a forward-looking decision-support tool rather than historical bookkeeping**
- **Golden Rules of Financial Modeling Architecture: Strict separation of inputs, calculations, and output summaries**
- **Formatting Standards: Blue font for hardcoded inputs, Black font for formulas/calculations, Green for external sheet references**
- **Standard model architecture: Cover Page, Executive Summary, Historical Financials, Assumptions/Drivers, Forecast Financial Statements, Debt & Depreciation Schedules, Valuation (DCF & Relative), Sensitivity Tables**

---

## 2. Key Formulas, Mechanics & Excel Architecture

The quantitative framework and spreadsheet implementations taught in this session include:

- `Rule 1: Never hardcode numbers inside a formula (e.g. use =C10*(1+$B$4) instead of =C10*1.10)`
- `Dynamic Date Headers: =EDATE(StartDate, 12) or =DATE(YEAR(C4)+1, MONTH(C4), DAY(C4))`
- `Dynamic Forecast Flags: =IF(Year>=ForecastStart, 1, 0)`

---

## 3. Real-World Context & Detailed Modeling Scenarios

To translate the lecture discussion into actionable institutional understanding, consider the following practical scenarios and modeling practices:

- Model auditing nightmare: An analyst hardcoded tax rate as 25% directly inside Net Income formulas across 5 sheets; when corporate tax changed to 22%, the model produced silent errors and took 14 hours to debug.
- Best Practice Setup: Dedicated Assumptions Block at the top or in a separate tab where tax rate, inflation, GDP growth, and margin assumptions reside.

---

## 4. Practical Practitioner Takeaways

1. Financial models are living corporate simulations; readability and auditability are as critical as mathematical logic.
2. Consistency in cell formatting, color coding, and sign conventions (+ for inflows, - for outflows) separates amateur models from institutional models.

