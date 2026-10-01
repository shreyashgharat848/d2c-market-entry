# Project 1: Market Entry Strategy for a D2C Brand in Tier-2/3 India

> **Disclaimer:** The client ("GlowRoot") is hypothetical. Market inputs in `data/` are illustrative placeholders; replace them with sourced figures and cite them before using any number in a deck or resume.

## Problem statement
GlowRoot is a Bengaluru-based D2C skincare brand (about Rs 60 Cr revenue, ~80% from metros). Metro growth is slowing and customer acquisition cost (CAC) is rising.
**Should GlowRoot enter tier-2/3 cities? Which cities, through which channel, and will it be profitable?**

## Approach
1. **Issue tree:** Is the market attractive? Can we win? Is it profitable?
2. **Market sizing:** top-down funnel (population, age 18-45, online-active, premium skincare buyers, annual spend) with a bottom-up cross-check (pincodes x orders x AOV).
3. **City scorecard:** weighted score on market size (30%), income (25%), internet (20%), logistics (15%), competition (10%).
4. **Competitor benchmark:** 4-5 brands on price per 100 ml, channels, positioning.
5. **Channel options:** e-commerce only vs distributors/chemists vs kirana vs hybrid.
6. **Unit economics and 3-year projection:** contribution per customer, CAC payback, sensitivity to CAC and repeat rate.
7. **Risks and mitigation, then phased recommendation.**

## Folder guide
| Path | Contents |
|---|---|
| `data/city_data_template.csv` | City inputs (fill with sourced data) |
| `analysis/market_sizing.py` | Market size, bottom-up check, city ranking |
| `analysis/unit_economics.py` | Unit economics, 3-year P&L, sensitivity grid |
| `excel/` | Excel model (Assumptions, Market Sizing, Scorecard, Unit Economics, 3-Year P&L, Sensitivity) |
| `deck/` | 12-14 slide deck + one-page summary |

## How to run
```bash
pip install -r ../requirements.txt
python analysis/market_sizing.py
python analysis/unit_economics.py
```

## Data sources to use
Census 2011 (population), NSSO HCES 2022-23 (spend), TRAI / IAMAI-Kantar (internet), IBEF / Redseer / Bain-Flipkart (category), Nykaa/Amazon listings (pricing), Honasa and Nykaa annual reports (margins, CAC).

## Key findings (fill in from YOUR run)
- Serviceable market across 5 cities: Rs ___ Cr (top-down) vs Rs ___ Cr (bottom-up)
- Top cities: ___, ___, ___
- Contribution per customer: Rs ___; CAC payback: ___ months
- Break-even: month ___ (base case); range ___ to ___ under sensitivity

## Recommendation (edit with your results)
Enter 2-3 top-scoring cities in phases. **Phase 1 (0-6 months):** online plus regional-language marketing with an entry-priced starter kit. **Phase 2 (6-18 months):** add chemist distribution in the best-performing city. Investment Rs ___ Cr, break-even in about ___ months.

## Tools
Python (pandas), Excel, PowerPoint
