# Session 10: Ratios & Portfolio Risk Metrics (Beta, Alpha, Sharpe, Treynor & Sortino)

> **Mutual Fund Analysis & Portfolio Architecture Series**  
> *Curated directly from the lecture discussions of Parth Verma (The Valuation School) with institutional context, operational mechanics, and detailed Indian mutual fund examples.*

---

## 📌 Video Metadata & Quick Reference
- **Title**: `Mutual Fund Risk - 2 | Full Course | Mutual Fund for Beginners in Hindi`
- **YouTube Link**: [Watch Video on YouTube](https://www.youtube.com/watch?v=TxGpiHQWnkA)
- **Playlist Reference**: [Mutual Fund Analysis - Full Course 2024-25](https://www.youtube.com/playlist?list=PL3uUjzLk6Puky6IlCLShDJK4nSFYII5Xx)
- **Session Number**: `10 of 16`
- **Video ID**: `TxGpiHQWnkA`

---

## 1. Core Lecture Discussion & Concepts

In this session, Parth Verma systematically deconstructs the foundational and operational mechanics of **Ratios & Portfolio Risk Metrics (Beta, Alpha, Sharpe, Treynor & Sortino)**. 

### Primary Themes Addressed by the Instructor:
- **Beta ($\beta$)**: Sensitivity to broader market movements. A fund with $\beta = 1.0$ moves in lockstep with its benchmark. If $\beta = 1.2$, a 10% market rise yields a 12% fund gain, but a 10% market decline causes a 12% loss.
- **Alpha (Jensen's $\alpha$)**: The true value added by the fund manager above the expected return predicted by the Capital Asset Pricing Model (CAPM). Positive alpha proves stock-picking skill; negative alpha indicates fees destroying value relative to an index.
- **Sharpe Ratio**: Excess return over risk-free rate divided by total risk (Standard Deviation)
- **Treynor Ratio**: Excess return divided by systematic market risk
- **Sortino Ratio**: Replacing total volatility with **Downside Deviation**. It does not penalize a fund for sharp upward volatility; it only measures risk of negative returns.
- **Maximum Drawdown**: Peak-to-trough percentage decline during historical market crashes.

---

## 2. Real-World Context & Detailed Scenarios

To translate the lecture discussion into actionable investor understanding, consider the following practical scenarios and industry mechanics:

- Sharpe Ratio Calculation Scenario: Assume Risk-Free Rate ($R_f$ on 91-day T-Bills) = 6.5%.
- - Fund A: Return = 16%, $\sigma = 12\%$. $\text{Sharpe} = (16 - 6.5) / 12 = 0.79$.
- - Fund B: Return = 18%, $\sigma = 20\%$. $\text{Sharpe} = (18 - 6.5) / 20 = 0.575$.
- Even though Fund B generated 2% higher absolute return, Fund A is superior on a risk-adjusted basis.
- Sortino Advantage in High-Growth Funds: A technology or small-cap fund that surges +40% in bull months has a high Standard Deviation, which depresses its Sharpe Ratio. Sortino ignores upward spikes and isolates negative drawdowns, revealing whether downside risk is controlled.

---

## 3. Practical Investor Takeaways

1. Alpha measures manager skill beyond market beta; Sharpe and Sortino measure excess return per unit of risk.
2. Always examine Sortino Ratio alongside Sharpe Ratio to avoid penalizing asymmetric upside volatility.
