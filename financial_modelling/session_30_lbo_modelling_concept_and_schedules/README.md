# Session 30: LBO Modeling - Concept Modeling, Debt Paydown & Interest Waterfall

> **Financial Modeling & Valuation Series**  
> *Curated directly from the lecture discussions of Parth Verma (The Valuation School) with institutional modeling architecture, Excel formulas, financial mechanics, and practical corporate finance scenarios.*

---

## 📌 Video Metadata & Quick Reference
- **Title**: `Learn LBO MODELLING in Excel | Concept Modelling | Session 3 | Full Course`
- **YouTube Link**: [Watch Video on YouTube](https://www.youtube.com/watch?v=oJMmKtKPrYg)
- **Playlist Reference**: [Learn Financial Modelling - Step by Step](https://www.youtube.com/playlist?list=PL3uUjzLk6PulhRop_ffNeHyK0kprzO4cT)
- **Session Number**: `30 of 34`
- **Video ID**: `oJMmKtKPrYg`
- **Duration**: `33m 9s`

---

## 1. Core Lecture Discussion & Concepts

In this session, Parth Verma systematically deconstructs the foundational, mathematical, and modeling mechanics of **Session 30: LBO Modeling - Concept Modeling, Debt Paydown & Interest Waterfall**. 

### Primary Themes Addressed by the Instructor:
- **Building the full Debt Schedule and Cash Flow Waterfall in Excel**
- **Order of priority in the waterfall: Operating expenses -> Maintenance capex -> Taxes -> Revolver interest -> Term Loan interest -> Scheduled Term Loan principal amortization -> Cash Sweep -> Discretionary cash**
- **Modeling the Revolver facility (Revolving Credit Facility): Drawing when cash dips below minimum operating cash, repaying when surplus cash exists**
- **Dynamic interest expense calculation across multiple debt tranches**
- **Exit valuation modeling: Exit year EBITDA * Exit EV/EBITDA multiple - Ending Net Debt = Exit Equity Value**
- **Calculating Sponsor Returns: XIRR and MoIC**

---

## 2. Key Formulas, Mechanics & Excel Architecture

The quantitative framework and spreadsheet implementations taught in this session include:

- `Ending Debt = Beginning Debt + New Borrowings - Scheduled Amortization - Cash Sweep Prepayment`
- `Revolver Draw = MAX(0, Min_Cash_Required - Ending_Cash_Before_Revolver)`
- `Exit Enterprise Value = Exit_Year_EBITDA * Exit_Multiple`
- `Exit Equity Proceeds = Exit EV - Total Ending Debt + Ending Cash`
- `MoIC = Exit Equity Proceeds / Initial Sponsor Equity`
- `IRR = (Exit Equity Proceeds / Initial Sponsor Equity)^(1 / Years) - 1`

---

## 3. Real-World Context & Detailed Modeling Scenarios

To translate the lecture discussion into actionable institutional understanding, consider the following practical scenarios and modeling practices:

- The 5-Year LBO Returns Summary: Initial Sponsor investment = ₹300 Cr in 2024. In 2029 (Year 5), EBITDA has grown from ₹80 Cr to ₹140 Cr. Exit multiple assumed flat at 9.0x -> Exit EV = ₹1,260 Cr. Debt reduced from ₹500 Cr to ₹120 Cr; cash = ₹40 Cr -> Net Debt = ₹80 Cr. Exit Equity = ₹1,260 Cr - ₹80 Cr = ₹1,180 Cr. MoIC = ₹1,180 / ₹300 = 3.93x. IRR = (3.93)^(1/5) - 1 = 31.5%.
- Returns Deconstruction Table: Splitting the ₹880 Cr equity profit into: (1) EBITDA Growth, (2) Debt Paydown, and (3) Multiple Change.

---

## 4. Practical Practitioner Takeaways

1. The cash flow waterfall ensures that cash is rigorously allocated according to debt seniority before equity holders receive any distribution.
2. A disciplined LBO thesis does not rely on multiple expansion; underwriting target returns based on flat or contracting exit multiples ensures safety.

