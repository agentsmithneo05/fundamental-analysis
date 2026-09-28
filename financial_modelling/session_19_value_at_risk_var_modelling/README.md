# Session 19: Value at Risk (VaR) Modeling in Excel

> **Financial Modeling & Valuation Series**  
> *Curated directly from the lecture discussions of Parth Verma (The Valuation School) with institutional modeling architecture, Excel formulas, financial mechanics, and practical corporate finance scenarios.*

---

## 📌 Video Metadata & Quick Reference
- **Title**: `VAR calculation in EXCEL | Learn Financial Modeling | Step by Step | Session 18`
- **YouTube Link**: [Watch Video on YouTube](https://www.youtube.com/watch?v=MlIijqGBml0)
- **Playlist Reference**: [Learn Financial Modelling - Step by Step](https://www.youtube.com/playlist?list=PL3uUjzLk6PulhRop_ffNeHyK0kprzO4cT)
- **Session Number**: `19 of 34`
- **Video ID**: `MlIijqGBml0`
- **Duration**: `39m 10s`

---

## 1. Core Lecture Discussion & Concepts

In this session, Parth Verma systematically deconstructs the foundational, mathematical, and modeling mechanics of **Session 19: Value at Risk (VaR) Modeling in Excel**. 

### Primary Themes Addressed by the Instructor:
- **What is Value at Risk (VaR)? Quantifying maximum expected loss over a specific time horizon at a given confidence level (e.g. 95% or 99%)**
- **Three main approaches to VaR: Historical Method, Parametric (Variance-Covariance) Method, and Monte Carlo Simulation**
- **Parametric VaR calculation using normal distribution: Mean return, standard deviation, and Z-score (NORMSINV)**
- **Historical VaR using PERCENTILE.INC in Excel on historical daily returns**
- **Limitations of VaR: Fat-tail risk, black swan events, and why Expected Shortfall (CVaR) is used by institutional risk desks**

---

## 2. Key Formulas, Mechanics & Excel Architecture

The quantitative framework and spreadsheet implementations taught in this session include:

- `Parametric 1-Day VaR (95%) = -(Mean_Return - Z * Volatility) * Portfolio_Value (where Z = 1.645 for 95%, 2.326 for 99%)`
- `Historical VaR in Excel = -PERCENTILE.INC(Daily_Returns_Array, 1 - Confidence_Level) * Portfolio_Value`
- `Multi-day VaR = 1-Day VaR * SQRT(Time_Horizon_Days)`
- `Excel Z-score: =NORM.S.INV(Confidence_Level)`

---

## 3. Real-World Context & Detailed Modeling Scenarios

To translate the lecture discussion into actionable institutional understanding, consider the following practical scenarios and modeling practices:

- Calculating VaR for a ₹10 Crore equity portfolio: Daily standard deviation is 1.8%; 1-day 99% VaR = 2.326 * 1.8% * ₹10 Cr = ₹41.87 Lakhs. Interpretation: On 99 out of 100 trading days, the daily loss will not exceed ₹41.87 Lakhs.
- Historical vs Parametric divergence during market crashes: In March 2020, parametric VaR severely understated downside because market returns exhibited extreme kurtosis (fat tails), causing 6-sigma moves.

---

## 4. Practical Practitioner Takeaways

1. VaR does not tell you what happens in the worst 1% of cases; it only tells you the threshold loss that separates normal days from bad days.
2. Always supplement VaR with stress testing and scenario analysis.

