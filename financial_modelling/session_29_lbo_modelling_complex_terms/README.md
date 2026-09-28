# Session 29: LBO Modeling - Complex Deal Terms, Debt Tranches & Covenants

> **Financial Modeling & Valuation Series**  
> *Curated directly from the lecture discussions of Parth Verma (The Valuation School) with institutional modeling architecture, Excel formulas, financial mechanics, and practical corporate finance scenarios.*

---

## 📌 Video Metadata & Quick Reference
- **Title**: `Learn LBO MODELLING in Excel | Complex Terms | Session 2 | Full Course`
- **YouTube Link**: [Watch Video on YouTube](https://www.youtube.com/watch?v=rFtt9GAqxTM)
- **Playlist Reference**: [Learn Financial Modelling - Step by Step](https://www.youtube.com/playlist?list=PL3uUjzLk6PulhRop_ffNeHyK0kprzO4cT)
- **Session Number**: `29 of 34`
- **Video ID**: `rFtt9GAqxTM`
- **Duration**: `20m 27s`

---

## 1. Core Lecture Discussion & Concepts

In this session, Parth Verma systematically deconstructs the foundational, mathematical, and modeling mechanics of **Session 29: LBO Modeling - Complex Deal Terms, Debt Tranches & Covenants**. 

### Primary Themes Addressed by the Instructor:
- **Deconstructing the Capital Structure Debt Tranches: Revolver, Senior Secured Term Loan A (amortizing), Term Loan B (institutional, bullet repayment), Subordinated/Mezzanine Debt**
- **Payment-in-Kind (PIK) interest mechanics: Interest accrued to debt principal rather than paid in cash**
- **Debt covenants: Maintenance Covenants (Max Leverage Ratio, Min Interest Coverage) vs Incurrence Covenants (Restrictions on capex, acquisitions, dividends)**
- **Cash Sweep mechanics: Mandatory prepayment of debt using excess cash generated (e.g. 50% or 75% cash sweep)**
- **Management equity rollover, options pool, and sweet equity dilution**

---

## 2. Key Formulas, Mechanics & Excel Architecture

The quantitative framework and spreadsheet implementations taught in this session include:

- `PIK Interest = Beginning Debt Principal * PIK Interest Rate (added to Ending Principal)`
- `Cash Sweep Amount = Min(Cash Available after scheduled amortization, Excess Cash * Sweep %)`
- `Leverage Covenant Ratio = Total Debt / LTM EBITDA <= Maximum Allowable Multiple`
- `Interest Coverage Covenant = EBITDA / Total Cash Interest >= Minimum Required Ratio`

---

## 3. Real-World Context & Detailed Modeling Scenarios

To translate the lecture discussion into actionable institutional understanding, consider the following practical scenarios and modeling practices:

- Modeling PIK Mezzanine Debt: ₹100 Cr Mezzanine facility with 8% cash interest + 4% PIK interest. In year 1, cash interest paid = ₹8 Cr; PIK interest of ₹4 Cr is added to principal, making year 2 opening debt ₹104 Cr.
- Cash sweep preventing cash hoarding: Company generates ₹50 Cr excess cash; an 80% sweep forces a ₹40 Cr prepayment on Term Loan B, accelerating deleveraging and boosting sponsor IRR.

---

## 4. Practical Practitioner Takeaways

1. Senior debt is cheaper but carries restrictive maintenance covenants; mezzanine debt is expensive and dilutive but provides cash flexibility through PIK options.
2. Covenant headroom analysis must be stress-tested against cyclical revenue drops to avoid premature default.

