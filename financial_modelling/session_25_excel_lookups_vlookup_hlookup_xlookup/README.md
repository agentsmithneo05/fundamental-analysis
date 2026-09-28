# Session 25: Master Excel Lookups - VLOOKUP, HLOOKUP, XLOOKUP & INDEX-MATCH

> **Financial Modeling & Valuation Series**  
> *Curated directly from the lecture discussions of Parth Verma (The Valuation School) with institutional modeling architecture, Excel formulas, financial mechanics, and practical corporate finance scenarios.*

---

## 📌 Video Metadata & Quick Reference
- **Title**: `Learn Lookup in Excel | Vlookup | Hlookup | Xlookup`
- **YouTube Link**: [Watch Video on YouTube](https://www.youtube.com/watch?v=tUxaY5o_hyY)
- **Playlist Reference**: [Learn Financial Modelling - Step by Step](https://www.youtube.com/playlist?list=PL3uUjzLk6PulhRop_ffNeHyK0kprzO4cT)
- **Session Number**: `25 of 34`
- **Video ID**: `tUxaY5o_hyY`
- **Duration**: `16m 16s`

---

## 1. Core Lecture Discussion & Concepts

In this session, Parth Verma systematically deconstructs the foundational, mathematical, and modeling mechanics of **Session 25: Master Excel Lookups - VLOOKUP, HLOOKUP, XLOOKUP & INDEX-MATCH**. 

### Primary Themes Addressed by the Instructor:
- **Understanding the evolution of lookup functions in Microsoft Excel**
- **VLOOKUP: Syntax, mechanics, exact match (0/FALSE) vs approximate match (1/TRUE), and the fatal left-lookup limitation**
- **HLOOKUP: Horizontal data extraction across row headers and why it is used in timeline models**
- **INDEX-MATCH: The classic investment banking standard; 2-way dynamic lookups that never break when columns are inserted**
- **XLOOKUP: Modern Excel's unified lookup function; handling default values, reverse searches, and exact-or-next match options**

---

## 2. Key Formulas, Mechanics & Excel Architecture

The quantitative framework and spreadsheet implementations taught in this session include:

- `VLOOKUP: =VLOOKUP(Lookup_Value, Table_Array, Col_Index_Num, FALSE)`
- `HLOOKUP: =HLOOKUP(Lookup_Value, Table_Array, Row_Index_Num, FALSE)`
- `INDEX-MATCH: =INDEX(Return_Range, MATCH(Lookup_Val, Lookup_Array, 0))`
- `2-Way INDEX-MATCH: =INDEX(Matrix_Range, MATCH(Row_Val, Row_Array, 0), MATCH(Col_Val, Col_Array, 0))`
- `XLOOKUP: =XLOOKUP(Lookup_Value, Lookup_Array, Return_Array, 'Not Found', 0)`

---

## 3. Real-World Context & Detailed Modeling Scenarios

To translate the lecture discussion into actionable institutional understanding, consider the following practical scenarios and modeling practices:

- Column insertion break test: A financial model uses =VLOOKUP('Revenue', A1:G20, 5, FALSE). When an analyst inserts a new column for FY23 Actuals, the formula silently pulls the wrong data; using INDEX-MATCH or XLOOKUP dynamically adjusts without breaking.
- Financial statement mapping: Using XLOOKUP to map raw ERP/trial balance account line items into standardized institutional financial statement categories.

---

## 4. Practical Practitioner Takeaways

1. Stop using hardcoded column index numbers in VLOOKUP; transition to XLOOKUP or INDEX-MATCH for robust financial models.
2. Mastering 2-way lookups allows seamless extraction of any financial metric across any historical or forecast fiscal year.

