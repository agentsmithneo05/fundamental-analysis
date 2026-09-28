import json, os, subprocess

# Load metadata
with open('fm_metadata_raw.json') as f:
    raw_meta = json.load(f)

# Master curated sessions details for the 34 sessions
sessions_data = [
    {
        "id": "session_01_introduction_and_setup",
        "yt_id": "QhBLvRu2XSI",
        "num": 1,
        "title": "Session 1: Introduction to Financial Modeling & Excel Foundation",
        "topics": [
            "What is Financial Modeling and why it is the core operating system of Investment Banking, Equity Research, Corporate Finance, and PE",
            "Financial Modeling vs Accounting: Modeling as a forward-looking decision-support tool rather than historical bookkeeping",
            "Golden Rules of Financial Modeling Architecture: Strict separation of inputs, calculations, and output summaries",
            "Formatting Standards: Blue font for hardcoded inputs, Black font for formulas/calculations, Green for external sheet references",
            "Standard model architecture: Cover Page, Executive Summary, Historical Financials, Assumptions/Drivers, Forecast Financial Statements, Debt & Depreciation Schedules, Valuation (DCF & Relative), Sensitivity Tables"
        ],
        "formulas": [
            "Rule 1: Never hardcode numbers inside a formula (e.g. use =C10*(1+$B$4) instead of =C10*1.10)",
            "Dynamic Date Headers: =EDATE(StartDate, 12) or =DATE(YEAR(C4)+1, MONTH(C4), DAY(C4))",
            "Dynamic Forecast Flags: =IF(Year>=ForecastStart, 1, 0)"
        ],
        "practical_examples": [
            "Model auditing nightmare: An analyst hardcoded tax rate as 25% directly inside Net Income formulas across 5 sheets; when corporate tax changed to 22%, the model produced silent errors and took 14 hours to debug.",
            "Best Practice Setup: Dedicated Assumptions Block at the top or in a separate tab where tax rate, inflation, GDP growth, and margin assumptions reside."
        ],
        "takeaways": [
            "Financial models are living corporate simulations; readability and auditability are as critical as mathematical logic.",
            "Consistency in cell formatting, color coding, and sign conventions (+ for inflows, - for outflows) separates amateur models from institutional models."
        ]
    },
    {
        "id": "session_02_historical_data_entry",
        "yt_id": "9vAqWaRnfsU",
        "num": 2,
        "title": "Session 2: Historical Financial Statements & Data Extraction",
        "topics": [
            "Extracting 5-10 years of historical financial data from Annual Reports, BSE/NSE filings, and Screener.in",
            "Structuring the Historical Income Statement (Revenue from Operations, COGS, Gross Profit, Operating Expenses, EBITDA, Depreciation, EBIT, Interest, EBT, Tax, PAT)",
            "Structuring the Historical Balance Sheet (Equity Share Capital, Reserves & Surplus, Borrowings, Other Liabilities vs PPE, CWIP, Investments, Current Assets)",
            "Cash Flow Statement verification (Operating, Investing, Financing activities) and cash reconciliation",
            "Normalizing non-recurring and extraordinary items (asset sales, one-time litigation losses, impairment write-downs)"
        ],
        "formulas": [
            "EBITDA = EBIT + Depreciation & Amortization",
            "Gross Margin = (Revenue - COGS) / Revenue",
            "EBITDA Margin = EBITDA / Revenue",
            "Operating Working Capital = (Trade Receivables + Inventory + Other Current Assets) - (Trade Payables + Other Current Liabilities)"
        ],
        "practical_examples": [
            "Tata Motors / FMCG case study: Extracting Screener.in consolidated financials vs standalone financials.",
            "Accounting classification differences: Ensuring exceptional items are isolated before calculating normalized EBITDA; otherwise, margin trends will be distorted."
        ],
        "takeaways": [
            "Always reconcile Historical Balance Sheet Net Assets with Total Equity + Debt before forecasting.",
            "Use consolidated financials for holding companies with operating subsidiaries to capture the full economic picture."
        ]
    },
    {
        "id": "session_03_excel_functions_and_tools",
        "yt_id": "OMQe-JF76rg",
        "num": 3,
        "title": "Session 3: Excel Functions, Shortcuts, Dynamic Modeling & Protection",
        "topics": [
            "Essential Excel functions for financial modeling: INDEX, MATCH, XLOOKUP, OFFSET, CHOOSE, SUMIFS",
            "Auditing tools: Trace Precedents (Ctrl + [), Trace Dependents (Ctrl + ]), Evaluate Formula (Alt + M + V)",
            "Dynamic scenario modeling using CHOOSE and INDEX for Base, Bull, and Bear cases",
            "Name Manager and Data Validation dropdowns for dynamic scenario switching",
            "Model governance: Cell locking, hidden formula protection, and worksheet protection (Alt + T + P + P)"
        ],
        "formulas": [
            "Dynamic Case Switcher: =CHOOSE(Scenario_Index, Base_Revenue, Bull_Revenue, Bear_Revenue)",
            "INDEX-MATCH lookup: =INDEX(Data_Range, MATCH(Lookup_Val, Row_Header_Range, 0), MATCH(Year_Val, Col_Header_Range, 0))",
            "Safe Error Handling: =IFERROR(Formula, 0)"
        ],
        "practical_examples": [
            "Creating an executive scenario switcher: In cell C2, a Data Validation dropdown allows selecting 1 (Base), 2 (Optimistic), 3 (Conservative); all sales, margin, and capex schedules automatically update instantly.",
            "Protecting client deliverables: Unlocking only driver input cells (F4:F20) while locking and hiding all proprietary formula cells so users cannot break the financial engine."
        ],
        "takeaways": [
            "Dynamic modeling eliminates the need to build three separate models for bull, base, and bear scenarios.",
            "Keyboard navigation and shortcut mastery (Alt hotkeys) increase financial modeling speed by 3x."
        ]
    },
    {
        "id": "session_04_three_statement_model",
        "yt_id": "-VIqSzEFvjM",
        "num": 4,
        "title": "Session 4: Integrated 3-Statement Financial Modeling",
        "topics": [
            "The core mechanics of the 3-Statement Integrated Model (Income Statement, Balance Sheet, Cash Flow Statement)",
            "The Circularity and Linking Mechanism: Net Income flows from Income Statement to Retained Earnings on Balance Sheet and top of Cash Flow Statement",
            "Depreciation schedule linking: Non-cash expense added back in Cash Flow from Operations and reducing Net PPE on Balance Sheet",
            "Capex schedule linking: Subtracted in Cash Flow from Investing and increasing Gross PPE on Balance Sheet",
            "The Balance Sheet Balancing Equation: Total Assets = Total Equity + Total Debt + Other Liabilities, using Cash as the final balancing plug"
        ],
        "formulas": [
            "Retained Earnings_t = Retained Earnings_{t-1} + Net Income_t - Dividends_t",
            "Ending Cash_t = Beginning Cash_t + CFO_t + CFI_t + CFF_t",
            "Balance Sheet Check = Total Assets - (Total Equity + Total Liabilities); Must equal EXACTLY 0.00"
        ],
        "practical_examples": [
            "Tracing a ₹100 Crores Capex funded 60% by Debt and 40% by Cash: Cash outflow of ₹100 Cr in CFI; Debt increases by ₹60 Cr in CFF; Net cash decreases by ₹40 Cr; Balance Sheet: PPE increases by ₹100 Cr, Cash decreases by ₹40 Cr (Net Assets +₹60 Cr), Debt increases by ₹60 Cr (Net Liabilities +₹60 Cr). Perfectly balanced.",
            "Resolving circular reference warnings: When interest income depends on cash balance and cash balance depends on interest income."
        ],
        "takeaways": [
            "If your Balance Sheet check does not equal zero, do not plug an arbitrary dummy number; systematically trace Cash Flow line items.",
            "The Cash Flow Statement is the mathematical bridge that keeps the Balance Sheet in equilibrium."
        ]
    },
    {
        "id": "session_05_ratio_analysis_modelling",
        "yt_id": "t93qZunzHd8",
        "num": 5,
        "title": "Session 5: Financial Ratio Analysis & Performance Diagnostics",
        "topics": [
            "Categorization of financial ratios: Liquidity, Solvency, Turnover/Efficiency, and Profitability",
            "Liquidity Ratios: Current Ratio, Quick Ratio, and Cash Ratio",
            "Turnover / Working Capital Efficiency Ratios: Days Sales Outstanding (DSO), Days Inventory Outstanding (DIO), Days Payable Outstanding (DPO), and Cash Conversion Cycle (CCC)",
            "Profitability & Return Ratios: Return on Equity (ROE), Return on Capital Employed (ROCE), Return on Invested Capital (ROIC)",
            "Solvency & Leverage Ratios: Debt-to-Equity, Net Debt-to-EBITDA, and Interest Coverage Ratio"
        ],
        "formulas": [
            "Cash Conversion Cycle (CCC) = DIO + DSO - DPO",
            "ROCE = EBIT / (Total Assets - Current Liabilities)",
            "ROIC = NOPAT / Invested Capital = (EBIT * (1 - Tax Rate)) / (Total Equity + Net Debt)",
            "Interest Coverage Ratio = EBIT / Finance Costs"
        ],
        "practical_examples": [
            "Retail vs Heavy Industrial CCC: DMart / Avenue Supermarts operates with negative or near-zero working capital due to high inventory turn and rapid cash collections; an EPC contractor like L&T often has CCC of 90-120 days.",
            "Detecting balance sheet stress: A company with Net Debt / EBITDA exceeding 3.5x and Interest Coverage below 2.0x faces severe refinancing vulnerabilities during an interest rate hiking cycle."
        ],
        "takeaways": [
            "High revenue growth without ROIC exceeding WACC destroys economic value.",
            "The Cash Conversion Cycle reveals whether working capital expansion is absorbing or releasing operational cash flow."
        ]
    },
    {
        "id": "session_06_forecasting_methodologies",
        "yt_id": "Ccv8eAqBSSQ",
        "num": 6,
        "title": "Session 6: Forecasting Methodologies & Revenue/Cost Schedules",
        "topics": [
            "Forecasting philosophies: Top-Down (Market Size -> Penetration -> Pricing) vs Bottom-Up (Store Count -> Volume -> ARPU)",
            "Cost structure forecasting: Fixed costs vs Variable costs as a % of Revenue",
            "Working Capital schedules: Forecasting Receivables, Inventory, and Payables using historical DSO, DIO, DPO days",
            "Depreciation waterfall schedules: Straight-Line Method (SLM) based on asset useful life and capex additions",
            "Debt & Interest waterfall schedules: Opening debt, new borrowings, scheduled repayments, and ending debt with average interest calculations"
        ],
        "formulas": [
            "Forecast Receivables = (Forecast DSO / 365) * Forecast Revenue",
            "Forecast Inventory = (Forecast DIO / 365) * Forecast COGS",
            "Forecast Payables = (Forecast DPO / 365) * Forecast Raw Material / Purchases",
            "Interest Expense = Average(Beginning Debt, Ending Debt) * Interest Rate"
        ],
        "practical_examples": [
            "Auto OEM forecasting: Number of vehicles sold * Average Realization per Vehicle + Aftermarket Spares / Services.",
            "Building a circular-safe debt schedule: Using Beginning Debt rather than Average Debt to prevent Excel iterative calculation errors in automated models."
        ],
        "takeaways": [
            "Forecast drivers must be rooted in observable industry metrics (capacity, store rollouts, utilization, pricing power) rather than arbitrary growth percentages.",
            "Working capital days should be kept stable or trend conservatively toward long-term historical medians."
        ]
    },
    {
        "id": "session_07_dcf_excel_modelling",
        "yt_id": "pdveRcJucX4",
        "num": 7,
        "title": "Session 7: Discounted Cash Flow (DCF) Valuation Modeling",
        "topics": [
            "Theoretical foundation of DCF: The value of an operating business equals the present value of its future unlevered free cash flows discounted at the firm's WACC",
            "Unlevered Free Cash Flow (FCFF) calculation: EBIT * (1 - Tax Rate) + D&A - Capex - Change in Non-Cash Working Capital",
            "Explicit Forecast Period (typically 5 to 10 years) based on company maturity and competitive visibility",
            "Terminal Value calculation methods: Gordon Growth Model (Perpetuity Growth) vs Exit Multiple Method (EV/EBITDA)",
            "Reconciling Enterprise Value (EV) to Equity Value: EV - Net Debt - Minority Interest - Preferred Stock + Non-Operating Assets = Equity Value"
        ],
        "formulas": [
            "FCFF = EBIT * (1 - t) + Depreciation - Capex - ΔNWC",
            "Terminal Value (Gordon Growth) = (FCFF_{n+1}) / (WACC - g) = FCFF_n * (1 + g) / (WACC - g)",
            "Discount Factor_t = 1 / (1 + WACC)^t (or mid-year convention: 1 / (1 + WACC)^(t - 0.5))",
            "Implied Share Price = Equity Value / Diluted Shares Outstanding"
        ],
        "practical_examples": [
            "Valuing an Indian IT firm: Modeling 5-year explicit FCFF of ₹2,500 Cr to ₹4,000 Cr; Terminal growth rate pegged at 5.0% (aligned with long-term nominal Indian GDP minus 1-2%); WACC computed at 11.5%.",
            "Reconciliation of Bridge: Showing how ₹50,000 Cr Enterprise Value translates to ₹55,000 Cr Equity Value after adding ₹7,000 Cr net cash and subtracting ₹2,000 Cr minority interest."
        ],
        "takeaways": [
            "Terminal value typically represents 60% to 80% of total enterprise value in a DCF; small changes in terminal growth rate or WACC cause massive swings.",
            "Always check that the perpetual growth rate does not exceed the long-term risk-free rate or GDP growth of the operating economy."
        ]
    },
    {
        "id": "session_08_wacc_modelling_part_1",
        "yt_id": "Pp_qhxHUziQ",
        "num": 8,
        "title": "Session 8: Weighted Average Cost of Capital (WACC) Modeling - Part 1",
        "topics": [
            "Understanding WACC as the blended hurdle rate required by all capital providers (equity and debt)",
            "Capital Asset Pricing Model (CAPM) for Cost of Equity: Ke = Rf + Beta * (Rm - Rf)",
            "Risk-Free Rate (Rf) selection: Using the 10-year Government of India (G-Sec) bond yield for Indian assets",
            "Equity Risk Premium (ERP): Historical market return minus risk-free rate (typically 5.5% to 7.0% for Indian markets)",
            "Capital structure weightings: Market value of equity vs Book/Market value of debt"
        ],
        "formulas": [
            "WACC = (We * Ke) + (Wd * Kd * (1 - t))",
            "Cost of Equity (Ke) = Rf + Beta * ERP",
            "We = Market Cap / (Market Cap + Total Debt)",
            "Wd = Total Debt / (Market Cap + Total Debt)"
        ],
        "practical_examples": [
            "Indian manufacturing firm WACC calculation: Rf = 7.10% (10-Yr G-Sec), ERP = 6.0%, Beta = 1.15 -> Ke = 7.10% + 1.15*(6.0%) = 14.0%. Kd = 9.0%, Tax rate = 25.17% -> After-tax Kd = 6.73%. Weights: 75% Equity, 25% Debt -> WACC = (0.75 * 14.0%) + (0.25 * 6.73%) = 10.5% + 1.68% = 12.18%.",
            "The market value fallacy: Why novice modelers mistakenly use book value of equity (Net Worth) instead of market capitalization, artificially distorting debt weight and understating WACC."
        ],
        "takeaways": [
            "Always use market values for capital weights; book equity represents historical retained capital, not current economic opportunity cost.",
            "WACC reflects the risk of the cash flows being generated, not the funding structure of a specific project."
        ]
    },
    {
        "id": "session_09_wacc_modelling_beta_analysis",
        "yt_id": "qRri_spNhHo",
        "num": 9,
        "title": "Session 9: What is Beta? Regression, Levering & Unlevering Beta",
        "topics": [
            "Theoretical definition of Beta: Systematic, non-diversifiable market risk relative to the market benchmark",
            "Raw Historical Beta vs Adjusted (Bloomberg / Blume) Beta: Formula = (2/3) * Raw Beta + (1/3) * 1.0",
            "Calculating Beta in Excel: SLOPE function using 3 to 5 years of weekly or monthly percentage stock returns vs Nifty 50 / S&P BSE 500",
            "Unlevering Beta: Stripping out financial risk (debt leverage) to determine Pure Business / Asset Risk",
            "Re-levering Beta: Applying target or company-specific capital structure to find the appropriate operational Beta"
        ],
        "formulas": [
            "Excel Beta Formula: =SLOPE(Stock_Returns_Array, Market_Returns_Array)",
            "Unlevered Beta (Asset Beta) = Levered Beta / (1 + (1 - Tax_Rate) * (Debt / Equity))",
            "Re-levered Beta = Unlevered Beta * (1 + (1 - Tax_Rate) * (Target_Debt / Target_Equity))"
        ],
        "practical_examples": [
            "Unlevering peer betas for an unlisted company: Analyzing listed peers (e.g. Titan, Kalyan, Senco); extracting their levered betas, unlevering them based on their respective D/E ratios to find median industry Asset Beta, then re-levering at the target firm's capital structure.",
            "Impact of high financial leverage: Two companies in the same industry with identical business risk; Company A has D/E of 0.2x (Beta 1.1), while Company B has D/E of 1.5x (Beta 2.1). Company B's high beta is driven by financial risk, not operational difference."
        ],
        "takeaways": [
            "Historical regression beta is backward-looking and heavily influenced by the chosen benchmark and time window; institutional analysts unlever peer betas to find pure industry risk.",
            "Adjusted beta accounts for the empirical tendency of betas to regress toward the market mean of 1.0 over long horizons."
        ]
    },
    {
        "id": "session_10_wacc_modelling_part_3",
        "yt_id": "N0VG4nbeoBI",
        "num": 10,
        "title": "Session 10: WACC Modeling Part 3 - Cost of Debt, Terminal WACC & Hurdles",
        "topics": [
            "Estimating the Cost of Debt (Kd): Effective interest rate vs Yield-to-Maturity (YTM) on corporate bonds vs Synthetic Rating approach",
            "Tax shield mechanics: Why interest deductibility lowers the effective cost of debt (Kd * (1 - t))",
            "Terminal WACC: Adjusting capital structure and risk profile as a company transitions from high-growth to stable, mature state",
            "Country Risk Premium (CRP) and size premium additions for mid-cap and emerging market entities",
            "Sanity checking WACC against Return on Capital Employed (ROCE) and industry peer hurdle rates"
        ],
        "formulas": [
            "Effective Kd = Total Finance Costs / Average Borrowings",
            "Synthetic Rating Kd = Risk-Free Rate + Default Spread (based on Interest Coverage Ratio)",
            "After-tax Cost of Debt = Kd * (1 - Marginal Tax Rate)"
        ],
        "practical_examples": [
            "Synthetic rating for an unrated firm: Interest coverage ratio of 4.2x corresponds to a synthetic BBB rating, implying a default spread of 2.25% over the 10-Yr G-Sec (7.10%), yielding a pre-tax Kd of 9.35%.",
            "The terminal WACC adjustment: In year 10, a startup's debt capacity increases from 5% to 30%, and beta drops from 1.6 to 1.0, reducing terminal WACC from 15.5% to 11.2%."
        ],
        "takeaways": [
            "Do not rely solely on historical interest expense / debt; for distressed or fast-growing firms, look at current marginal borrowing yields.",
            "Ensure the marginal tax rate used for the tax shield matches current statutory rates (e.g. 25.17% in India under Section 115BAA)."
        ]
    },
    {
        "id": "session_11_common_size_statements",
        "yt_id": "csv-QJTubG8",
        "num": 11,
        "title": "Session 11: Common-Size Statement Modeling & Structural Trend Analysis",
        "topics": [
            "Vertical Analysis vs Horizontal Analysis across financial statements",
            "Vertical Income Statement: Expressing every line item as a percentage of Total Net Revenue",
            "Vertical Balance Sheet: Expressing every asset line as a percentage of Total Assets, and liabilities as a percentage of Total Liabilities & Equity",
            "Identifying operating leverage: Fixed cost dilution as revenue scales up",
            "Benchmarking against peer averages to spot accounting anomalies, cost inefficiencies, and margin outliers"
        ],
        "formulas": [
            "Income Statement Common-Size Line = Line Item / Total Revenue * 100",
            "Balance Sheet Common-Size Line = Line Item / Total Assets * 100",
            "Operating Leverage Degree = % Change in EBIT / % Change in Revenue"
        ],
        "practical_examples": [
            "FMCG vs Tech Common-Size: FMCG company spends 45% on Raw Materials, 12% on Advertising, 8% on Employee expenses; SaaS/IT firm spends 5% on COGS, 60% on Employee expenses, 20% on S&M.",
            "Catching margin erosion: Common-size analysis reveals Freight & Logistics rising from 4.2% of sales to 7.8% over 3 years, highlighting an unhedged operational cost inflation before management discussed it in concalls."
        ],
        "takeaways": [
            "Common-size statements normalize company scale, allowing direct comparison between a ₹500 Cr small-cap and a ₹50,000 Cr industry leader.",
            "Stable or expanding gross margins coupled with shrinking operating expense percentages is the signature of true economic scale."
        ]
    },
    {
        "id": "session_12_growth_rate_mechanics",
        "yt_id": "0N3zIEhaq1c",
        "num": 12,
        "title": "Session 12: Sales Forecasting & Long-Term Growth Rate Mechanics",
        "topics": [
            "Mechanics of organic vs inorganic growth modeling",
            "Sustainable Growth Rate (SGR) formula: Growth achievable without external equity financing",
            "Fundamental growth drivers: Reinvestment Rate * Return on Invested Capital (ROIC)",
            "CAGR (Compound Annual Growth Rate) vs Moving Averages vs Linear Regression for historical trend estimation",
            "Setting the terminal growth rate (g): Why terminal growth can never mathematically exceed long-term GDP growth"
        ],
        "formulas": [
            "Sustainable Growth Rate (SGR) = ROE * Retention Ratio = ROE * (1 - Dividend Payout Ratio)",
            "Fundamental Growth in Operating Income = Reinvestment Rate * ROCE (or ROIC)",
            "Reinvestment Rate = (Net Capex + Change in NWC) / (EBIT * (1 - t))",
            "CAGR = (Ending Value / Beginning Value)^(1 / n) - 1"
        ],
        "practical_examples": [
            "The capital allocation paradox: Company A earns 25% ROCE and reinvests 60% of earnings -> Expected fundamental growth = 25% * 60% = 15%. Company B earns 8% ROCE and reinvests 100% of earnings -> Expected fundamental growth = 8% * 100% = 8%, but destroys economic value because 8% < WACC (11%).",
            "Terminal growth limit: Modeling terminal growth of 8% in India when nominal GDP growth is projected at 6-7% implies the company will eventually become larger than the entire Indian economy—a fatal modeling flaw."
        ],
        "takeaways": [
            "Growth only creates value when Return on Capital exceeds Cost of Capital (ROIC > WACC); growth below cost of capital destroys value.",
            "Set terminal growth conservatively at 3% to 5% for Indian companies, aligned with long-term inflation and real GDP potential."
        ]
    },
    {
        "id": "session_13_dcf_fcff_fcfe_modelling",
        "yt_id": "h-rO3pNHHuw",
        "num": 13,
        "title": "Session 13: Free Cash Flow to Firm (FCFF) vs FCFE Valuation Modeling",
        "topics": [
            "FCFF (Free Cash Flow to Firm) vs FCFE (Free Cash Flow to Equity): Conceptual differences and when to use which model",
            "FCFF approach (Entity approach): Discounts unlevered cash flows available to all providers of capital at WACC to get Enterprise Value",
            "FCFE approach (Equity approach): Discounts levered cash flows available to equity shareholders at Cost of Equity (Ke) to get Equity Value directly",
            "Treating Net Borrowings: Why new debt issuances are added and debt repayments subtracted in FCFE, but omitted from FCFF",
            "Modeling financial institutions (Banks & NBFCs): Why DCF/FCFF fails for banks and why Dividend Discount Model (DDM) or FCFE is mandatory"
        ],
        "formulas": [
            "FCFF = EBIT*(1 - t) + D&A - Capex - ΔNWC",
            "FCFE = Net Income + D&A - Capex - ΔNWC + New Debt Issued - Debt Repayments",
            "Alternative FCFE = FCFF - Interest Expense*(1 - t) + Net Borrowings",
            "Equity Value (from FCFE) = Sum(PV of FCFE discounted at Ke) + PV(Terminal FCFE)"
        ],
        "practical_examples": [
            "Why FCFF is preferred for industrial companies: Capital structure changes over the forecast period do not distort operating cash flow forecasts.",
            "Bank valuation failure: A student tries to compute FCFF for HDFC Bank; Capex and Working Capital cannot be separated from loans and deposits, and debt is raw material, not financing. Solution: Use Gordon DDM or Residual Income Model."
        ],
        "takeaways": [
            "If leverage is stable, FCFF discounted at WACC and FCFE discounted at Ke yield mathematically identical Equity Values.",
            "Use FCFF when debt is volatile or when valuing cyclical/turnaround companies; use DDM/FCFE for financial services firms."
        ]
    },
    {
        "id": "session_14_relative_valuation_peer_multiples",
        "yt_id": "1aAh_CbnOj0",
        "num": 14,
        "title": "Session 14: Relative Valuation Modeling & Peer Comps Architecture",
        "topics": [
            "Philosophy of Relative Valuation: Valuing an asset based on how the market prices comparable assets",
            "Enterprise Value Multiples vs Equity Value Multiples: The Matching Principle (Enterprise metrics divided by firm earnings, Equity metrics divided by equity earnings)",
            "Common multiples: EV/EBITDA, EV/Sales, EV/EBIT, P/E (Price-to-Earnings), P/B (Price-to-Book), and PEG ratio",
            "Selecting truly comparable peers: Industry classification, geographic exposure, growth profile, margins, and capital structure",
            "Trailing Twelve Months (TTM) vs Next Twelve Months (NTM / Forward) multiples"
        ],
        "formulas": [
            "Enterprise Value = Market Cap + Total Debt + Minority Interest + Preferred Stock - Cash & Cash Equivalents",
            "EV/EBITDA Multiple = Enterprise Value / EBITDA",
            "P/E Multiple = Market Price per Share / Diluted EPS",
            "PEG Ratio = (P/E Multiple) / Expected EPS Growth Rate"
        ],
        "practical_examples": [
            "The Cardinal Matching Sin: Dividing Enterprise Value by Net Income (EV/PAT) or Market Cap by EBITDA (P/EBITDA); mixing firm and equity claims leads to nonsensical comparisons.",
            "Capital intensity adjustment: Why EV/EBITDA is preferred over P/E for telecom or steel companies with different depreciation policies and debt loads."
        ],
        "takeaways": [
            "Relative valuation reflects market sentiment and current pricing, whereas DCF reflects intrinsic cash flow power; institutional analysts always use both.",
            "Never compare a 25% ROIC market leader directly to a 9% ROIC marginal player without applying a quality discount."
        ]
    },
    {
        "id": "session_15_relative_valuation_practical_case",
        "yt_id": "DpKdORBG224",
        "num": 15,
        "title": "Session 15: Relative Valuation Practical Modeling & Multiples Analysis",
        "topics": [
            "Building a dynamic Peer Comps Table in Excel step-by-step",
            "Extracting peer data: Market Cap, Total Debt, Cash, EBITDA, Sales, and Net Profit from screener or annual reports",
            "Computing Min, 25th Percentile, Median, Mean, 75th Percentile, and Max benchmark multiples",
            "Applying peer multiples to target company metrics to derive implied Enterprise Value and Equity Value ranges",
            "Handling outlier distortions: Why median is preferred over mean in comps tables"
        ],
        "formulas": [
            "Median Multiple in Excel = MEDIAN(Multiple_Range)",
            "Implied EV = Target_Company_EBITDA * Peer_Median_EV_EBITDA",
            "Implied Share Price = (Implied EV - Net Debt) / Shares_Outstanding"
        ],
        "practical_examples": [
            "Valuing an unlisted specialty chemical player: Assembling 8 listed peers (Aarti Ind, Deepak Nitrite, Clean Science, Naveen Fluorine); calculating median EV/EBITDA of 18.5x; multiplying target's ₹120 Cr EBITDA yields ₹2,220 Cr EV; subtracting ₹220 Cr Net Debt gives ₹2,000 Cr Equity Value.",
            "Outlier impact: One peer undergoing an acquisition has an EV/EBITDA of 95x due to temporarily depressed earnings; using Average inflates the target valuation by 40%, whereas Median remains robust."
        ],
        "takeaways": [
            "Always use the Median multiple rather than the Mean to protect your valuation from skewed peer outliers.",
            "Triangulate implied valuation across multiple metrics: EV/EBITDA, P/E, and EV/Sales."
        ]
    },
    {
        "id": "session_16_sensitivity_analysis_modelling",
        "yt_id": "cdPqgPmZQjM",
        "num": 16,
        "title": "Session 16: Sensitivity & Scenario Analysis Using 2-Way Data Tables",
        "topics": [
            "Why point estimates in financial modeling are dangerous and incomplete",
            "Setting up 2-Way Data Tables in Excel (Data -> What-If Analysis -> Data Table)",
            "Sensitizing Target Share Price against WACC (Row Input) and Terminal Growth Rate (Column Input)",
            "Sensitizing EBITDA Margin vs Revenue Growth for operating forecasts",
            "Formatting Data Tables: Handling the top-left formula cell linkage and applying conditional formatting heat maps"
        ],
        "formulas": [
            "Data Table Row Input: Reference cell for WACC (e.g. C15)",
            "Data Table Column Input: Reference cell for Terminal Growth Rate (e.g. C16)",
            "Top-left corner link: =Target_Share_Price_Cell"
        ],
        "practical_examples": [
            "DCF sensitivity matrix: WACC varied from 10.5% to 13.5% (in 0.5% steps); Terminal growth varied from 4.0% to 6.0% (in 0.5% steps). The table reveals the stock is worth ₹450 in the worst case and ₹820 in the best case, framing the investment debate around probability rather than a single ₹610 target.",
            "Conditional Formatting Heat Map: Color-coding the valuation matrix from Dark Red (undervalued/downside) to Dark Green (strong upside) to present to the Investment Committee."
        ],
        "takeaways": [
            "A financial model without sensitivity analysis is unfinished; decision-makers need to know which variables create the most vulnerability.",
            "Ensure Excel calculation options are set to 'Automatic except for data tables' if large data tables slow down spreadsheet performance."
        ]
    },
    {
        "id": "session_17_football_field_valuation",
        "yt_id": "O-SzKtazG-g",
        "num": 17,
        "title": "Session 17: Football Field Valuation Chart & Range Synthesis",
        "topics": [
            "The purpose of a Football Field Chart in Investment Banking pitchbooks and fairness opinions",
            "Synthesizing valuation ranges across multiple methodologies: 52-Week High/Low, Historical P/E Comps, Peer EV/EBITDA Comps, DCF Base Case, DCF Sensitivity Range, and Precedent Transactions",
            "Structuring the Excel table: Method, Min Value, Max Value, Spread",
            "Building the Floating Bar Chart using Stacked Bar charts in Excel",
            "Highlighting Current Market Price (CMP) as a vertical reference line to identify mispricing"
        ],
        "formulas": [
            "Spread = Max_Valuation - Min_Valuation",
            "Base Floating Offset = Min_Valuation",
            "Implied Target Range = [Min(Method_Mins), Max(Method_Maxes)]"
        ],
        "practical_examples": [
            "M&A fairness presentation: Pitching an acquisition of an auto component maker. DCF yields ₹320-₹410; Comps yield ₹280-₹350; 52-week trading range is ₹250-₹310; Precedent transactions show ₹340-₹430. CMP is ₹290. The football field clearly illustrates that a takeover bid at ₹360 is fair to both seller and acquirer.",
            "Formatting trick: Setting the 'Min Value' series fill to 'No Fill' and border to 'No Border' so only the spread floating bar is visible."
        ],
        "takeaways": [
            "The Football Field chart is the ultimate executive summary of valuation work; it replaces confusing numbers with clear, visual ranges.",
            "Never rely on a single valuation methodology; convergence across distinct models builds conviction."
        ]
    },
    {
        "id": "session_18_financial_modeling_interview_case",
        "yt_id": "damvzw7xNpk",
        "num": 18,
        "title": "Session 18: Investment Banking Financial Modeling Interview Case Study",
        "topics": [
            "Deconstructing typical Investment Banking and Private Equity modeling tests (timed 60 to 180 minute tests)",
            "Common interview prompts: 'Here is a 3-year historical P&L and Balance Sheet; build a 5-year forecast and DCF model in 90 minutes'",
            "Speed vs Precision trade-offs: How to balance dynamic linking with error-free balance sheet balancing",
            "Quick sanity checks interviewers look for: Working capital turns, Capex-to-D&A ratio, ROCE trend, and terminal value reasonableness",
            "Structuring clean presentation tabs for interview graders"
        ],
        "formulas": [
            "Quick D&A Forecast = D&A as % of Gross PPE or % of Revenue",
            "Quick Capex Forecast = Capex as % of Sales or Capex = D&A * 1.2 (for growing firm)",
            "Balance Check Formula = IF(ROUND(Assets - Liabilities, 2) = 0, 'OK', 'ERROR')"
        ],
        "practical_examples": [
            "Navigating a modeling test trap: The prompt gives a high revenue growth assumption (30%) but forgets to specify capex; an amateur keeps capex flat, leading to asset turnover rising to unrealistic levels (15x); a smart candidate dynamically links capex to revenue capacity, demonstrating business acumen.",
            "Time management strategy: Allocate 20 mins to historical setup, 35 mins to forecast schedules, 20 mins to DCF/WACC, 15 mins to sensitivity tables and formatting."
        ],
        "takeaways": [
            "In modeling tests, a balanced model with sensible assumptions beats an overly complex model that does not balance or has circular errors.",
            "Interviewers care as much about your formatting discipline and keyboard shortcut speed as your theoretical valuation formulas."
        ]
    },
    {
        "id": "session_19_value_at_risk_var_modelling",
        "yt_id": "MlIijqGBml0",
        "num": 19,
        "title": "Session 19: Value at Risk (VaR) Modeling in Excel",
        "topics": [
            "What is Value at Risk (VaR)? Quantifying maximum expected loss over a specific time horizon at a given confidence level (e.g. 95% or 99%)",
            "Three main approaches to VaR: Historical Method, Parametric (Variance-Covariance) Method, and Monte Carlo Simulation",
            "Parametric VaR calculation using normal distribution: Mean return, standard deviation, and Z-score (NORMSINV)",
            "Historical VaR using PERCENTILE.INC in Excel on historical daily returns",
            "Limitations of VaR: Fat-tail risk, black swan events, and why Expected Shortfall (CVaR) is used by institutional risk desks"
        ],
        "formulas": [
            "Parametric 1-Day VaR (95%) = -(Mean_Return - Z * Volatility) * Portfolio_Value (where Z = 1.645 for 95%, 2.326 for 99%)",
            "Historical VaR in Excel = -PERCENTILE.INC(Daily_Returns_Array, 1 - Confidence_Level) * Portfolio_Value",
            "Multi-day VaR = 1-Day VaR * SQRT(Time_Horizon_Days)",
            "Excel Z-score: =NORM.S.INV(Confidence_Level)"
        ],
        "practical_examples": [
            "Calculating VaR for a ₹10 Crore equity portfolio: Daily standard deviation is 1.8%; 1-day 99% VaR = 2.326 * 1.8% * ₹10 Cr = ₹41.87 Lakhs. Interpretation: On 99 out of 100 trading days, the daily loss will not exceed ₹41.87 Lakhs.",
            "Historical vs Parametric divergence during market crashes: In March 2020, parametric VaR severely understated downside because market returns exhibited extreme kurtosis (fat tails), causing 6-sigma moves."
        ],
        "takeaways": [
            "VaR does not tell you what happens in the worst 1% of cases; it only tells you the threshold loss that separates normal days from bad days.",
            "Always supplement VaR with stress testing and scenario analysis."
        ]
    },
    {
        "id": "session_20_dupont_analysis_modelling_part_1",
        "yt_id": "LIHqS2aQYtY",
        "num": 20,
        "title": "Session 20: DuPont Analysis Modeling - 3-Stage & 5-Stage Deconstruction (Part 1)",
        "topics": [
            "The purpose of DuPont Analysis: Breaking down Return on Equity (ROE) into operational and financial drivers",
            "The 3-Stage DuPont Model: Net Profit Margin (Profitability) * Asset Turnover (Efficiency) * Financial Leverage (Leverage)",
            "The 5-Stage DuPont Model: Tax Burden * Interest Burden * Operating Margin (EBIT Margin) * Asset Turnover * Financial Leverage",
            "Dissecting whether ROE expansion is driven by operational excellence or dangerous debt loading",
            "Setting up the DuPont tracking model in Excel across 5 years of historical financial data"
        ],
        "formulas": [
            "3-Stage ROE = (Net Income / Revenue) * (Revenue / Assets) * (Assets / Equity)",
            "5-Stage ROE = (Net Income / EBT) * (EBT / EBIT) * (EBIT / Revenue) * (Revenue / Assets) * (Assets / Equity)",
            "Tax Burden = Net Income / EBT",
            "Interest Burden = EBT / EBIT",
            "Operating Margin = EBIT / Revenue",
            "Asset Turnover = Revenue / Average Total Assets",
            "Equity Multiplier = Average Total Assets / Average Total Equity"
        ],
        "practical_examples": [
            "Comparing two companies with identical 20% ROE: Company X has Net Margin of 15%, Asset Turnover of 1.1x, and Leverage of 1.2x (high quality, asset-light moat); Company Y has Net Margin of 3%, Asset Turnover of 0.8x, and Leverage of 8.3x (fragile, highly levered balance sheet).",
            "Interest burden decay: A company's operating margin improves from 12% to 15%, but its interest burden drops from 0.90 to 0.55 due to excessive debt, completely wiping out operating gains."
        ],
        "takeaways": [
            "Never look at ROE in isolation; high ROE driven purely by the Equity Multiplier represents elevated financial risk rather than business quality.",
            "5-stage DuPont separates tax and financing decisions from pure operating margin performance."
        ]
    },
    {
        "id": "session_21_dupont_analysis_modelling_part_2",
        "yt_id": "DcLvXfXPLKo",
        "num": 21,
        "title": "Session 21: DuPont Analysis Modeling - Practical Case Breakdown (Part 2)",
        "topics": [
            "Deep-dive practical case study modeling DuPont across Indian listed companies",
            "Automating DuPont calculations directly from historical financial statement sheets in Excel",
            "Analyzing trend shifts: Plotting 5-stage components over a 10-year economic cycle",
            "Diagnosing margin vs turnover trade-offs (e.g. Luxury retail vs Discount hypermarket)",
            "Connecting DuPont insights to valuation multiples (Why high-margin, low-leverage ROE commands higher P/B multiples)"
        ],
        "formulas": [
            "Justified P/B Multiple = (ROE - g) / (Ke - g)",
            "DuPont Check: Product of all 5 stages MUST equal Net Income / Equity"
        ],
        "practical_examples": [
            "Titan Company vs Trent vs DMart: Deconstructing how Trent's asset turnover and working capital discipline drive superior ROE despite lower gross margins than traditional jewelry retailing.",
            "Cement industry case study: Showing how cyclic downturns crash asset turnover and operating margin simultaneously, crushing ROE from 18% to 4%."
        ],
        "takeaways": [
            "Companies with sustainable high ROE driven by high asset turnover and operating margins consistently outperform companies reliant on debt multipliers.",
            "Incorporate a DuPont dashboard into every institutional equity research model to benchmark quality of earnings."
        ]
    },
    {
        "id": "session_22_altman_z_score_distress_modelling",
        "yt_id": "13YAACEFamQ",
        "num": 22,
        "title": "Session 22: Altman Z-Score Modeling for Financial Distress & Solvency",
        "topics": [
            "Background of the Altman Z-Score: Empirical formula developed by Edward Altman to predict corporate bankruptcy risk within 2 years",
            "The 5 Financial Ratios of the Original Z-Score (Manufacturing & Public Entities)",
            "Z-Score interpretation zones: Safe Zone (Z > 2.99), Grey Zone (1.81 <= Z <= 2.99), Distress Zone (Z < 1.81)",
            "The Modified Z'-Score for Private Companies and Non-Manufacturing/Service Firms",
            "Building an automated Altman Z-Score monitoring template in Excel"
        ],
        "formulas": [
            "Altman Z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 0.999*X5",
            "X1 = Working Capital / Total Assets (Liquidity measure)",
            "X2 = Retained Earnings / Total Assets (Cumulative profitability & age measure)",
            "X3 = EBIT / Total Assets (Operating productivity / asset earning power)",
            "X4 = Market Value of Equity / Total Liabilities (Financial leverage measure)",
            "X5 = Sales / Total Assets (Asset turnover measure)"
        ],
        "practical_examples": [
            "Forensic analysis of a distressed Indian infrastructure firm: Over 4 years, X1 turned negative due to short-term loan reliance; X3 dropped as stalled projects produced no EBIT; Z-Score plunged from 2.45 (Grey) to 0.82 (Distress) 18 months before loan default.",
            "Service sector adjustment: Using the 4-variable Z'' score (omitting X5 sales/assets) for IT and consulting firms to avoid penalizing them for low asset bases."
        ],
        "takeaways": [
            "The Altman Z-Score is an invaluable early warning system; companies in the distress zone frequently suffer severe equity dilution or debt restructuring.",
            "X3 (EBIT / Total Assets) has the highest coefficient (3.3), reflecting that operating earning power is the ultimate defense against bankruptcy."
        ]
    },
    {
        "id": "session_23_one_page_company_profile_part_1",
        "yt_id": "LMtOMPxPOaM",
        "num": 23,
        "title": "Session 23: One-Page Institutional Company Profile Modeling (Part 1)",
        "topics": [
            "The purpose of a One-Page Company Profile / Executive Tear Sheet in Investment Banking and PE",
            "Grid layout and visual hierarchy: Header, Business Overview, Key Investment Highlights, Financial Summary Table, Key Metrics & Valuation",
            "Formatting conventions: Standard font families (Calibri/Arial), unified row heights, consistent number formatting (₹ Cr, $ M, % with 1 decimal)",
            "Automating data linkage: Pulling summary metrics directly from the underlying financial model via dynamic lookups",
            "Designing clean mini-charts (Sparklines) for 5-year revenue, EBITDA margin, and stock price trends"
        ],
        "formulas": [
            "Dynamic Header: =Company_Name & ' (' & Ticker & ') - Institutional Factsheet'",
            "Sparkline data range: Historical 5-year revenue or EBITDA array",
            "Dynamic CMP & Valuation metrics: Pulled from current price and shares outstanding cells"
        ],
        "practical_examples": [
            "Building a Tear Sheet for an IPO pitch: Creating a single printable page that summarizes business segments, 5-year CAGR, ROCE profile, and peer multiples so partners can digest the thesis in 60 seconds.",
            "Print setup discipline: Setting Print Area, Page Setup to 'Fit to 1 page wide by 1 page tall', suppressing gridlines, and removing Excel errors before PDF export."
        ],
        "takeaways": [
            "A cluttered tear sheet destroys credibility; white space, structured alignment, and clean visual grouping are essential.",
            "Every single figure on the one-page profile must dynamically trace back to the master model without manual typing."
        ]
    },
    {
        "id": "session_24_one_page_company_profile_part_2",
        "yt_id": "O2WuKBxp5Jo",
        "num": 24,
        "title": "Session 24: One-Page Institutional Company Profile Modeling (Part 2)",
        "topics": [
            "Advanced formatting and data visualization on the One-Page Company Profile",
            "Integrating Shareholding Pattern charts (Promoter, FII, DII, Public) using Donut/Pie charts",
            "Segmental Revenue & EBIT contribution breakdown: Modeling business division performance",
            "Credit rating and debt maturity profile summary",
            "Polishing the final deliverable: Final PDF export checks, color theme harmonization, and executive readiness"
        ],
        "formulas": [
            "Segment Contribution % = Segment Revenue / Total Consolidated Revenue",
            "Free Float Calculation = Total Shares * (1 - Promoter Holding %)",
            "Market Cap = CMP * Diluted Shares Outstanding"
        ],
        "practical_examples": [
            "Diversified conglomerate tear sheet: Showing Reliance Industries' revenue and EBITDA contribution broken down across Oil-to-Chemicals (O2C), Jio Platforms, and Reliance Retail.",
            "Institutional client deliverable: Adding a clean corporate logo, subtle corporate brand palette (e.g. Navy Blue #002060 and Slate Grey), and structured footers with source citations."
        ],
        "takeaways": [
            "A great financial tear sheet tells the entire strategic and quantitative story of a business in one glance.",
            "Visual excellence and aesthetic rigor reflect professional competence in front of institutional clients and investors."
        ]
    },
    {
        "id": "session_25_excel_lookups_vlookup_hlookup_xlookup",
        "yt_id": "tUxaY5o_hyY",
        "num": 25,
        "title": "Session 25: Master Excel Lookups - VLOOKUP, HLOOKUP, XLOOKUP & INDEX-MATCH",
        "topics": [
            "Understanding the evolution of lookup functions in Microsoft Excel",
            "VLOOKUP: Syntax, mechanics, exact match (0/FALSE) vs approximate match (1/TRUE), and the fatal left-lookup limitation",
            "HLOOKUP: Horizontal data extraction across row headers and why it is used in timeline models",
            "INDEX-MATCH: The classic investment banking standard; 2-way dynamic lookups that never break when columns are inserted",
            "XLOOKUP: Modern Excel's unified lookup function; handling default values, reverse searches, and exact-or-next match options"
        ],
        "formulas": [
            "VLOOKUP: =VLOOKUP(Lookup_Value, Table_Array, Col_Index_Num, FALSE)",
            "HLOOKUP: =HLOOKUP(Lookup_Value, Table_Array, Row_Index_Num, FALSE)",
            "INDEX-MATCH: =INDEX(Return_Range, MATCH(Lookup_Val, Lookup_Array, 0))",
            "2-Way INDEX-MATCH: =INDEX(Matrix_Range, MATCH(Row_Val, Row_Array, 0), MATCH(Col_Val, Col_Array, 0))",
            "XLOOKUP: =XLOOKUP(Lookup_Value, Lookup_Array, Return_Array, 'Not Found', 0)"
        ],
        "practical_examples": [
            "Column insertion break test: A financial model uses =VLOOKUP('Revenue', A1:G20, 5, FALSE). When an analyst inserts a new column for FY23 Actuals, the formula silently pulls the wrong data; using INDEX-MATCH or XLOOKUP dynamically adjusts without breaking.",
            "Financial statement mapping: Using XLOOKUP to map raw ERP/trial balance account line items into standardized institutional financial statement categories."
        ],
        "takeaways": [
            "Stop using hardcoded column index numbers in VLOOKUP; transition to XLOOKUP or INDEX-MATCH for robust financial models.",
            "Mastering 2-way lookups allows seamless extraction of any financial metric across any historical or forecast fiscal year."
        ]
    },
    {
        "id": "session_26_cohort_preview_equity_research",
        "yt_id": "bh6miDtLr4I",
        "num": 26,
        "title": "Session 26: Equity Research & Valuation Cohort Roadmap",
        "topics": [
            "Overview of professional career paths in Equity Research, Investment Banking, Private Equity, and Credit Rating",
            "The complete workflow of an institutional research analyst: Industry study -> Management concalls -> Financial modeling -> Valuation -> Initiating Coverage Report",
            "Core technical competencies required by top global investment banks and domestic brokerage houses",
            "Portfolio of live company models: Why building models on live listed companies beats textbook theory",
            "Interview preparation roadmap: Cracking technical rounds, stock pitches, and case study assessments"
        ],
        "formulas": [
            "Stock Pitch Structure: Recommendation (Buy/Sell) + Target Price + CMP + Horizon + 3 Core Catalysts + 2 Key Risks + Valuation Basis",
            "Target Price = Implied DCF / Comps Value",
            "Expected Return = (Target Price - CMP + Expected Dividend) / CMP"
        ],
        "practical_examples": [
            "Drafting an institutional stock pitch: Selecting a mid-cap manufacturing leader, identifying an unpriced industry tailwind (China+1 capex cycle), demonstrating 25% EPS CAGR over 3 years, and presenting a compelling risk-reward skew of 3:1.",
            "Common interview mistake: Knowing DCF formulas by heart but having zero knowledge of industry capacity utilization, raw material trends, or competitor pricing moves."
        ],
        "takeaways": [
            "Financial modeling is not an end in itself; it is the quantitative foundation that validates your qualitative investment thesis.",
            "A live stock pitch supported by an audit-ready financial model is the single most powerful asset for cracking high-finance roles."
        ]
    },
    {
        "id": "session_27_lbo_modelling_introduction",
        "yt_id": "iuTejjY0t1Y",
        "num": 27,
        "title": "Session 27: Introduction to Leveraged Buyout (LBO) Mechanics & PE Returns",
        "topics": [
            "What is a Leveraged Buyout (LBO)? The acquisition of a company using a significant amount of borrowed money (debt) to fund the purchase price",
            "Why Private Equity firms use leverage: Amplifying equity returns (IRR) on invested capital",
            "The Mortgage Analogy: Buying a house with 20% down payment and 80% mortgage; property appreciation and rental income paying down debt generates extraordinary equity gains",
            "Ideal LBO Candidate Characteristics: Predictable cash flows, low existing debt, strong asset base, low ongoing capex, and operational turnaround/margin expansion potential",
            "Key return metrics: Internal Rate of Return (IRR) and Multiple on Invested Capital (MoIC / CoC)"
        ],
        "formulas": [
            "MoIC (Multiple on Invested Capital) = Total Cash Returned to Sponsor / Initial Equity Invested",
            "IRR = (MoIC)^(1 / Holding_Period_Years) - 1 (approximate rule: 2.0x in 5 years ~ 15% IRR; 2.5x in 5 years ~ 20% IRR; 3.0x in 5 years ~ 25% IRR)",
            "LBO Equity Value at Exit = Exit Enterprise Value - Ending Net Debt"
        ],
        "practical_examples": [
            "All-Equity vs LBO comparison: PE firm buys Company for ₹1,000 Cr. Case A (All Equity): Invests ₹1,000 Cr equity. In 5 years, company sells for ₹1,500 Cr. Gain = ₹500 Cr (1.5x MoIC, 8.4% IRR). Case B (LBO): Invests ₹300 Cr equity + ₹700 Cr debt. Cash flows pay down debt to ₹200 Cr. In 5 years, sells for ₹1,500 Cr. Equity proceeds = ₹1,500 Cr - ₹200 Cr = ₹1,300 Cr. Gain = ₹1,000 Cr on ₹300 Cr equity (4.33x MoIC, 34.1% IRR).",
            "The double-edged sword: If cash flows collapse, debt service obligations can trigger covenant breaches and bankruptcy, wiping out equity completely."
        ],
        "takeaways": [
            "LBO value creation comes from three distinct levers: Debt Paydown (deleveraging), Operational Improvement (EBITDA growth), and Multiple Expansion.",
            "Cash flow predictability and downside protection are far more important in an LBO than high top-line growth."
        ]
    },
    {
        "id": "session_28_lbo_modelling_excel_from_scratch",
        "yt_id": "saQWSw6F6T8",
        "num": 28,
        "title": "Session 28: LBO Modeling in Excel from Scratch - Core Architecture",
        "topics": [
            "Setting up the LBO model tabs and structure: Transaction Assumptions, Sources & Uses of Funds, Forecast Financials, Debt Schedule & Waterfall, and Returns Summary",
            "Transaction Assumptions: Entry Multiple (EV/EBITDA), Purchase Price, Transaction Fees, and Financing Structure (% Senior Debt, % Subordinated Debt, % Sponsor Equity)",
            "Building the Sources & Uses Table: Sources (Debt tranches, Rollover Equity, Sponsor Equity) must EXACTLY equal Uses (Purchase Enterprise Value, Refinancing Existing Debt, Transaction & Financing Fees)",
            "The core logic of the balance sheet adjustments on Day 1 of the buyout (Goodwill creation, debt refinancing, equity wipeout)",
            "Basic debt paydown modeling using Free Cash Flow"
        ],
        "formulas": [
            "Total Enterprise Value = LTM EBITDA * Entry EV/EBITDA Multiple",
            "Sponsor Equity (Plug) = Total Uses - Total Debt Sources - Rollover Equity",
            "Sources & Uses Check: Total Sources - Total Uses MUST equal 0.00",
            "Free Cash Flow Available for Debt Service (CFADS) = CFO - Capex - Minimum Cash Balance Requirement"
        ],
        "practical_examples": [
            "Sources & Uses setup: Target EBITDA = ₹100 Cr; Entry multiple = 10.0x -> Purchase EV = ₹1,000 Cr. Existing debt to refinance = ₹150 Cr. Fees = ₹30 Cr. Total Uses = ₹1,180 Cr. Sources: Senior Term Loan (4.0x EBITDA) = ₹400 Cr; Mezzanine Debt (2.0x EBITDA) = ₹200 Cr; Sponsor Equity = ₹580 Cr (balancing plug).",
            "Transaction fee capitalization vs expensing: Modeling advisory fees expensed through retained earnings vs financing fees capitalized and amortized over the debt tenure."
        ],
        "takeaways": [
            "The Sources & Uses table is the mathematical anchor of every LBO; a single unlinked fee throws off the opening balance sheet.",
            "Sponsor equity is always the residual balancing figure after all debt financing capacity is exhausted."
        ]
    },
    {
        "id": "session_29_lbo_modelling_complex_terms",
        "yt_id": "rFtt9GAqxTM",
        "num": 29,
        "title": "Session 29: LBO Modeling - Complex Deal Terms, Debt Tranches & Covenants",
        "topics": [
            "Deconstructing the Capital Structure Debt Tranches: Revolver, Senior Secured Term Loan A (amortizing), Term Loan B (institutional, bullet repayment), Subordinated/Mezzanine Debt",
            "Payment-in-Kind (PIK) interest mechanics: Interest accrued to debt principal rather than paid in cash",
            "Debt covenants: Maintenance Covenants (Max Leverage Ratio, Min Interest Coverage) vs Incurrence Covenants (Restrictions on capex, acquisitions, dividends)",
            "Cash Sweep mechanics: Mandatory prepayment of debt using excess cash generated (e.g. 50% or 75% cash sweep)",
            "Management equity rollover, options pool, and sweet equity dilution"
        ],
        "formulas": [
            "PIK Interest = Beginning Debt Principal * PIK Interest Rate (added to Ending Principal)",
            "Cash Sweep Amount = Min(Cash Available after scheduled amortization, Excess Cash * Sweep %)",
            "Leverage Covenant Ratio = Total Debt / LTM EBITDA <= Maximum Allowable Multiple",
            "Interest Coverage Covenant = EBITDA / Total Cash Interest >= Minimum Required Ratio"
        ],
        "practical_examples": [
            "Modeling PIK Mezzanine Debt: ₹100 Cr Mezzanine facility with 8% cash interest + 4% PIK interest. In year 1, cash interest paid = ₹8 Cr; PIK interest of ₹4 Cr is added to principal, making year 2 opening debt ₹104 Cr.",
            "Cash sweep preventing cash hoarding: Company generates ₹50 Cr excess cash; an 80% sweep forces a ₹40 Cr prepayment on Term Loan B, accelerating deleveraging and boosting sponsor IRR."
        ],
        "takeaways": [
            "Senior debt is cheaper but carries restrictive maintenance covenants; mezzanine debt is expensive and dilutive but provides cash flexibility through PIK options.",
            "Covenant headroom analysis must be stress-tested against cyclical revenue drops to avoid premature default."
        ]
    },
    {
        "id": "session_30_lbo_modelling_concept_and_schedules",
        "yt_id": "oJMmKtKPrYg",
        "num": 30,
        "title": "Session 30: LBO Modeling - Concept Modeling, Debt Paydown & Interest Waterfall",
        "topics": [
            "Building the full Debt Schedule and Cash Flow Waterfall in Excel",
            "Order of priority in the waterfall: Operating expenses -> Maintenance capex -> Taxes -> Revolver interest -> Term Loan interest -> Scheduled Term Loan principal amortization -> Cash Sweep -> Discretionary cash",
            "Modeling the Revolver facility (Revolving Credit Facility): Drawing when cash dips below minimum operating cash, repaying when surplus cash exists",
            "Dynamic interest expense calculation across multiple debt tranches",
            "Exit valuation modeling: Exit year EBITDA * Exit EV/EBITDA multiple - Ending Net Debt = Exit Equity Value",
            "Calculating Sponsor Returns: XIRR and MoIC"
        ],
        "formulas": [
            "Ending Debt = Beginning Debt + New Borrowings - Scheduled Amortization - Cash Sweep Prepayment",
            "Revolver Draw = MAX(0, Min_Cash_Required - Ending_Cash_Before_Revolver)",
            "Exit Enterprise Value = Exit_Year_EBITDA * Exit_Multiple",
            "Exit Equity Proceeds = Exit EV - Total Ending Debt + Ending Cash",
            "MoIC = Exit Equity Proceeds / Initial Sponsor Equity",
            "IRR = (Exit Equity Proceeds / Initial Sponsor Equity)^(1 / Years) - 1"
        ],
        "practical_examples": [
            "The 5-Year LBO Returns Summary: Initial Sponsor investment = ₹300 Cr in 2024. In 2029 (Year 5), EBITDA has grown from ₹80 Cr to ₹140 Cr. Exit multiple assumed flat at 9.0x -> Exit EV = ₹1,260 Cr. Debt reduced from ₹500 Cr to ₹120 Cr; cash = ₹40 Cr -> Net Debt = ₹80 Cr. Exit Equity = ₹1,260 Cr - ₹80 Cr = ₹1,180 Cr. MoIC = ₹1,180 / ₹300 = 3.93x. IRR = (3.93)^(1/5) - 1 = 31.5%.",
            "Returns Deconstruction Table: Splitting the ₹880 Cr equity profit into: (1) EBITDA Growth, (2) Debt Paydown, and (3) Multiple Change."
        ],
        "takeaways": [
            "The cash flow waterfall ensures that cash is rigorously allocated according to debt seniority before equity holders receive any distribution.",
            "A disciplined LBO thesis does not rely on multiple expansion; underwriting target returns based on flat or contracting exit multiples ensures safety."
        ]
    },
    {
        "id": "session_31_lbo_modelling_deal_sourcing_funnel",
        "yt_id": "eBzWdfXtlOg",
        "num": 31,
        "title": "Session 31: LBO Modeling - PE Deal Sourcing Funnel & Screening",
        "topics": [
            "The Private Equity Deal Sourcing Architecture: Inbound vs Outbound sourcing, Proprietary vs Auction processes",
            "The Deal Funnel: Reviewing 100+ teasers -> 20 Confidential Information Memorandums (CIM) -> 5 Non-Binding Indications of Interest (IOI) -> 2 Letter of Intent (LOI) / Confirmatory Due Diligence -> 1 Completed Transaction",
            "Quick Paper LBO / Mental LBO math for rapid screening without Excel",
            "Key operational filters: Free cash flow conversion (% of EBITDA converting to FCF), pricing power, customer concentration, and regulatory stability",
            "Investment Committee (IC) Paper structure: Executive summary, market dynamics, historical financial track record, thesis, value creation plan, and downside risks"
        ],
        "formulas": [
            "Paper LBO Shortcut: If a firm generates 60% FCF conversion on EBITDA, 4x leverage can be paid down by ~2.4x EBITDA over 5 years without growth.",
            "FCF Conversion = (EBITDA - Capex - Change in NWC - Cash Taxes) / EBITDA"
        ],
        "practical_examples": [
            "Screening a contract manufacturer: Revenue is growing 25%, but FCF conversion is only 15% due to massive working capital lockup and continuous capex; rejected at teaser stage because it cannot service LBO debt.",
            "Mental LBO interview question: 'Target has ₹50 Cr EBITDA, bought at 8x with 4x debt; in 5 years, EBITDA grows to ₹75 Cr, bought at 8x, debt paid down by 50%. What is the MoIC?' Fast mental math: Entry EV ₹400 Cr, Debt ₹200 Cr, Equity ₹200 Cr. Exit EV = 75*8 = ₹600 Cr. Ending Debt = ₹100 Cr. Exit Equity = ₹500 Cr. MoIC = 500 / 200 = 2.5x (~20% IRR)."
        ],
        "takeaways": [
            "PE associates spend 80% of their time screening and saying 'no' to deals; rapid elimination of unviable targets protects firm bandwidth.",
            "Mastering mental LBO math is essential for senior PE interviews and partner-level decision making."
        ]
    },
    {
        "id": "session_32_lbo_modelling_due_diligence",
        "-V5LvZY5wpo": "-V5LvZY5wpo",
        "yt_id": "-V5LvZY5wpo",
        "num": 32,
        "title": "Session 32: LBO Due Diligence & Buy-Side Fundamental Quality Audit",
        "topics": [
            "The Due Diligence Workstreams: Financial & Accounting (Quality of Earnings - QoE), Commercial (Market & Competition), Legal, Tax, Operational & IT, ESG/Regulatory",
            "Quality of Earnings (QoE) report deconstruction: Normalizing EBITDA for pro-forma acquisitions, owner personal expenses, non-arm's length related-party transactions, and deferred maintenance capex",
            "Customer Concentration & Churn analysis: Cohort retention curves, revenue concentration of top 5/10 customers",
            "Management depth and post-acquisition incentive alignment (Sweet Equity, Management Incentive Plan - MIP)",
            "Drafting the Confirmatory Due Diligence findings and setting purchase price adjustments / escrow indemnity reserves"
        ],
        "formulas": [
            "Reported EBITDA +/- Quality of Earnings Adjustments = Adjusted / Normalized EBITDA",
            "Customer Churn Rate = Customers Lost during Period / Beginning Customers",
            "Revenue Retention Rate = Ending ARR from Existing Cohort / Beginning ARR from Cohort"
        ],
        "practical_examples": [
            "Uncovering aggressive revenue recognition: In due diligence, the audit team discovers ₹25 Cr of shipments in the last week of March with liberal 180-day return rights (channel stuffing); normalizing EBITDA reduces purchase price by ₹150 Cr.",
            "Capex misclassification: Management treated ₹15 Cr of routine equipment repairs as capitalized assets rather than operating expenses, artificially inflating reported EBITDA by 18%."
        ],
        "takeaways": [
            "Due diligence is where transactions are won or lost; audited financial statements only verify historical books, while due diligence audits economic reality.",
            "Never accept management's adjusted EBITDA without independently auditing the Quality of Earnings."
        ]
    },
    {
        "id": "session_33_ipo_analysis_masterclass_lenskart",
        "yt_id": "wcw2DemxmFw",
        "num": 33,
        "title": "Session 33: IPO Analysis Masterclass - Decoding DRHP, Valuation & Lenskart Case Study",
        "topics": [
            "The IPO lifecycle and regulatory roadmap in India (SEBI guidelines, Draft Red Herring Prospectus - DRHP, Red Herring Prospectus - RHP, Anchor Allocation, Price Band)",
            "Decoding the DRHP: How to navigate a 600-page regulatory filing (Business Overview, Risk Factors, Objects of the Offer, Financial Statements, MD&A, Shareholding)",
            "Fresh Issue vs Offer for Sale (OFS): Why fresh issue expands corporate growth capital while OFS allows existing promoters/PE investors to cash out",
            "Comprehensive Case Study: Analyzing Lenskart's business model, omnichannel retail economics, store-level unit economics, and supply chain vertical integration",
            "Valuing high-growth consumer/tech IPOs: Unit economics, store payback periods, adjusted EBITDA vs reported net losses, and post-listing market expectations"
        ],
        "formulas": [
            "Store Payback Period = Initial Store Setup Capex / Annual Store Operating Free Cash Flow",
            "Post-Issue Market Cap = Total Post-Issue Shares Outstanding * Upper Price Band",
            "Implied P/S or EV/Sales = Market Cap (or EV) / LTM Revenue",
            "Fresh Capital Inflow = Fresh Issue Shares * Issue Price"
        ],
        "practical_examples": [
            "Analyzing Lenskart's unit economics: Setting up a store costs ₹35-40 Lakhs; generating ₹1.2 Cr revenue at 60% gross margin with 18% store-level EBITDA produces ₹20+ Lakhs cash flow per store, yielding a rapid ~2-year payback period.",
            "Evaluating Offer for Sale (OFS) red flags: When promoters and early venture investors offload 90% of the total IPO size with minimal fresh capital entering the business, it signals an exit liquidity event rather than growth expansion."
        ],
        "takeaways": [
            "Always read the 'Objects of the Offer' first to verify if proceeds fund high-ROI capex/debt retirement or merely provide venture capital exits.",
            "High growth without a proven path to store-level or customer-level unit economic profitability creates severe post-listing valuation derating."
        ]
    },
    {
        "id": "session_34_advanced_valuation_cohort_roadmap",
        "yt_id": "eT0TnGmPI4o",
        "num": 34,
        "title": "Session 34: Advanced Valuation & Financial Modeling Career Roadmap",
        "topics": [
            "Synthesizing the complete Financial Modeling & Valuation Masterclass",
            "The transition from technical modeler to strategic deal advisor and capital allocator",
            "Building an institutional finance portfolio: Creating dynamic 3-statement models, DCFs, LBOs, and teardowns on GitHub and LinkedIn",
            "Mastering concall interrogation, annual report forensic auditing, and competitive strategy analysis",
            "Lifelong learning principles: Navigating market cycles, maintaining intellectual honesty, and continuous financial modeling mastery"
        ],
        "formulas": [
            "The Master Valuation Synthesis: Intrinsic Value (DCF) vs Market Value (Peer Comps) vs Transaction Value (Precedents / LBO)",
            "Margin of Safety % = (Intrinsic Value - CMP) / Intrinsic Value * 100"
        ],
        "practical_examples": [
            "Career breakthrough case study: An aspiring analyst publishes an open-source, beautifully formatted 3-statement financial model and DCF of an unrated mid-cap specialty chemical company; a boutique investment bank reaches out directly for an off-market interview.",
            "The discipline of continuous updating: Financial models must be updated every quarter following concalls and earnings releases to track variance against thesis drivers."
        ],
        "takeaways": [
            "Technical financial modeling skills get you through the interview door; qualitative judgment, forensic curiosity, and intellectual integrity make you a world-class analyst.",
            "Your models should always prioritize clarity, auditability, and robust business logic over unnecessary mathematical complexity."
        ]
    }
]

print(f"Total defined sessions: {len(sessions_data)}")

# Create financial_modelling directory
base_dir = "financial_modelling"
os.makedirs(base_dir, exist_ok=True)

# Generate each session folder, metadata.json, and README.md
for s in sessions_data:
    folder_path = os.path.join(base_dir, s['id'])
    os.makedirs(folder_path, exist_ok=True)
    
    # Metadata
    raw_info = raw_meta.get(s['yt_id'], {})
    duration = raw_info.get('duration', 0)
    meta = {
        "session_number": s['num'],
        "folder_name": s['id'],
        "title": s['title'],
        "youtube_id": s['yt_id'],
        "youtube_url": f"https://www.youtube.com/watch?v={s['yt_id']}",
        "playlist_url": "https://www.youtube.com/playlist?list=PL3uUjzLk6PulhRop_ffNeHyK0kprzO4cT",
        "duration_seconds": duration,
        "duration_formatted": f"{duration // 60}m {duration % 60}s" if duration else "N/A",
        "upload_date": raw_info.get('upload_date'),
        "view_count": raw_info.get('view_count')
    }
    with open(os.path.join(folder_path, "metadata.json"), "w") as f:
        json.dump(meta, f, indent=2)
        
    # README.md
    readme_content = f"""# {s['title']}

> **Financial Modeling & Valuation Series**  
> *Curated directly from the lecture discussions of Parth Verma (The Valuation School) with institutional modeling architecture, Excel formulas, financial mechanics, and practical corporate finance scenarios.*

---

## 📌 Video Metadata & Quick Reference
- **Title**: `{raw_info.get('title', s['title'])}`
- **YouTube Link**: [Watch Video on YouTube](https://www.youtube.com/watch?v={s['yt_id']})
- **Playlist Reference**: [Learn Financial Modelling - Step by Step](https://www.youtube.com/playlist?list=PL3uUjzLk6PulhRop_ffNeHyK0kprzO4cT)
- **Session Number**: `{s['num']:02d} of {len(sessions_data)}`
- **Video ID**: `{s['yt_id']}`
- **Duration**: `{duration // 60}m {duration % 60}s`

---

## 1. Core Lecture Discussion & Concepts

In this session, Parth Verma systematically deconstructs the foundational, mathematical, and modeling mechanics of **{s['title']}**. 

### Primary Themes Addressed by the Instructor:
"""
    for t in s['topics']:
        readme_content += f"- **{t}**\n"
        
    readme_content += f"""
---

## 2. Key Formulas, Mechanics & Excel Architecture

The quantitative framework and spreadsheet implementations taught in this session include:

"""
    for f_item in s['formulas']:
        readme_content += f"- `{f_item}`\n"

    readme_content += f"""
---

## 3. Real-World Context & Detailed Modeling Scenarios

To translate the lecture discussion into actionable institutional understanding, consider the following practical scenarios and modeling practices:

"""
    for p in s['practical_examples']:
        readme_content += f"- {p}\n"

    readme_content += f"""
---

## 4. Practical Practitioner Takeaways

"""
    for idx_t, tk in enumerate(s['takeaways'], 1):
        readme_content += f"{idx_t}. {tk}\n"

    readme_content += "\n"

    with open(os.path.join(folder_path, "README.md"), "w") as f:
        f.write(readme_content)

print("Generated all session folders, metadata, and READMEs.")
