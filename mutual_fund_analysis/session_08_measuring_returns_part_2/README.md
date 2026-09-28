# Session 08: SIP Returns (XIRR) & Rolling Returns Consistency Analysis

> **Mutual Fund Analysis & Portfolio Architecture Series**  
> *Curated directly from the lecture discussions of Parth Verma (The Valuation School) with institutional context, operational mechanics, and detailed Indian mutual fund examples.*

---

## 📌 Video Metadata & Quick Reference
- **Title**: `Measuring Mutual Fund Returns - 2 | Full Course | Mutual Fund for Beginners in Hindi`
- **YouTube Link**: [Watch Video on YouTube](https://www.youtube.com/watch?v=2ajlNnHwAm8)
- **Playlist Reference**: [Mutual Fund Analysis - Full Course 2024-25](https://www.youtube.com/playlist?list=PL3uUjzLk6Puky6IlCLShDJK4nSFYII5Xx)
- **Session Number**: `08 of 16`
- **Video ID**: `2ajlNnHwAm8`

---

## 1. Core Lecture Discussion & Concepts

In this session, Parth Verma systematically deconstructs the foundational and operational mechanics of **SIP Returns (XIRR) & Rolling Returns Consistency Analysis**. 

### Primary Themes Addressed by the Instructor:
- **Why CAGR Fails for SIPs**: In a Systematic Investment Plan (SIP), capital enters the fund at different dates and varying NAVs. The first installment compounds for 60 months; the last installment compounds for only 30 days. Applying CAGR produces erroneous results.
- **Extended Internal Rate of Return (XIRR)**: The exact discount rate at which the Net Present Value (NPV) of all staggered cash outflows (SIP installments) equals the current portfolio redemption value.
- **Rolling Returns — The Ultimate Consistency Test**: Taking daily or weekly rolling windows over 3-year, 5-year, or 10-year horizons to eliminate start-date and end-date market timing bias.

---

## 2. Real-World Context & Detailed Scenarios

To translate the lecture discussion into actionable investor understanding, consider the following practical scenarios and industry mechanics:

- XIRR vs CAGR Scenario: An investor runs a ₹10,000 monthly SIP for 5 years (60 installments = ₹6,00,000 invested). Portfolio value reaches ₹9,50,000. Applying CAGR on total cost yields ~9.6%, but the true XIRR is ~18.2%, reflecting the fact that later installments had shorter compounding periods.
- Rolling Returns Analysis of Top Indian Funds: Comparing Fund A vs Fund B over a 7-year period. Fund A shows higher 5-year point-to-point trailing returns because of a recent cyclical surge. However, 5-year rolling return analysis over 1,500 trading days reveals Fund B delivered returns >12% in 88% of all instances, while Fund A delivered negative returns in 14% of instances. Fund B is the superior, consistent allocator.

---

## 3. Practical Investor Takeaways

1. Always use XIRR to evaluate the true annual compounding performance of SIPs, SWPs, and partial redemptions.
2. Rolling returns are the gold standard for separating lucky market timing from consistent fund manager alpha.
