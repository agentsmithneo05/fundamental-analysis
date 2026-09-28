# Session 22: Altman Z-Score Modeling for Financial Distress & Solvency

> **Financial Modeling & Valuation Series**  
> *Curated directly from the lecture discussions of Parth Verma (The Valuation School) with institutional modeling architecture, Excel formulas, financial mechanics, and practical corporate finance scenarios.*

---

## 📌 Video Metadata & Quick Reference
- **Title**: `Altman's Z Score Modelling | Learn Financial Modeling | Step by Step | Session 20`
- **YouTube Link**: [Watch Video on YouTube](https://www.youtube.com/watch?v=13YAACEFamQ)
- **Playlist Reference**: [Learn Financial Modelling - Step by Step](https://www.youtube.com/playlist?list=PL3uUjzLk6PulhRop_ffNeHyK0kprzO4cT)
- **Session Number**: `22 of 34`
- **Video ID**: `13YAACEFamQ`
- **Duration**: `43m 39s`

---

## 1. Core Lecture Discussion & Concepts

In this session, Parth Verma systematically deconstructs the foundational, mathematical, and modeling mechanics of **Session 22: Altman Z-Score Modeling for Financial Distress & Solvency**. 

### Primary Themes Addressed by the Instructor:
- **Background of the Altman Z-Score: Empirical formula developed by Edward Altman to predict corporate bankruptcy risk within 2 years**
- **The 5 Financial Ratios of the Original Z-Score (Manufacturing & Public Entities)**
- **Z-Score interpretation zones: Safe Zone (Z > 2.99), Grey Zone (1.81 <= Z <= 2.99), Distress Zone (Z < 1.81)**
- **The Modified Z'-Score for Private Companies and Non-Manufacturing/Service Firms**
- **Building an automated Altman Z-Score monitoring template in Excel**

---

## 2. Key Formulas, Mechanics & Excel Architecture

The quantitative framework and spreadsheet implementations taught in this session include:

- `Altman Z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 0.999*X5`
- `X1 = Working Capital / Total Assets (Liquidity measure)`
- `X2 = Retained Earnings / Total Assets (Cumulative profitability & age measure)`
- `X3 = EBIT / Total Assets (Operating productivity / asset earning power)`
- `X4 = Market Value of Equity / Total Liabilities (Financial leverage measure)`
- `X5 = Sales / Total Assets (Asset turnover measure)`

---

## 3. Real-World Context & Detailed Modeling Scenarios

To translate the lecture discussion into actionable institutional understanding, consider the following practical scenarios and modeling practices:

- Forensic analysis of a distressed Indian infrastructure firm: Over 4 years, X1 turned negative due to short-term loan reliance; X3 dropped as stalled projects produced no EBIT; Z-Score plunged from 2.45 (Grey) to 0.82 (Distress) 18 months before loan default.
- Service sector adjustment: Using the 4-variable Z'' score (omitting X5 sales/assets) for IT and consulting firms to avoid penalizing them for low asset bases.

---

## 4. Practical Practitioner Takeaways

1. The Altman Z-Score is an invaluable early warning system; companies in the distress zone frequently suffer severe equity dilution or debt restructuring.
2. X3 (EBIT / Total Assets) has the highest coefficient (3.3), reflecting that operating earning power is the ultimate defense against bankruptcy.

