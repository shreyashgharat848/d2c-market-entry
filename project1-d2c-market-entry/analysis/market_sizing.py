"""Top-down market sizing + city scorecard. Replace template values with SOURCED numbers."""
import os, pandas as pd
here = os.path.dirname(os.path.abspath(__file__))
d = pd.read_csv(os.path.join(here, "..", "data", "city_data_template.csv"))
YEARS_SINCE_2011 = 15

d["Population_now"] = d.Population_2011 * (1 + d.Growth_pct_pa/100) ** YEARS_SINCE_2011
d["Target_pop"]  = d.Population_now * d.Pct_18_45/100
d["Online_pop"]  = d.Target_pop * d.Pct_online_active/100
d["Buyers"]      = d.Online_pop * d.Pct_premium_skincare/100
d["Market_Rs_Cr"] = d.Buyers * d.Annual_spend_per_buyer_Rs / 1e7

# Weighted scorecard (score 1-5). Market size scored by quintile rank.
d["Size_score"] = pd.qcut(d.Market_Rs_Cr.rank(method="first"), 5, labels=[1,2,3,4,5]).astype(int)
w = {"Size_score":.30, "Income_score":.25, "Internet_score":.20, "Logistics_score":.15, "Competition_score":.10}
d["Weighted_score"] = sum(d[k]*v for k, v in w.items())
d = d.sort_values("Weighted_score", ascending=False)
print(d[["City","Buyers","Market_Rs_Cr","Weighted_score"]].round(2).to_string(index=False))
print(f"\nTotal serviceable market (5 cities): Rs {d.Market_Rs_Cr.sum():.1f} Cr")
d.to_csv(os.path.join(here, "..", "data", "city_scorecard_output.csv"), index=False)

# Bottom-up cross-check: pincodes x orders per pincode per month x AOV (EDIT these)
pincodes, orders_pm, aov = 120, 650, 550
bottom_up = pincodes * orders_pm * 12 * aov / 1e7
print(f"Bottom-up estimate: Rs {bottom_up:.1f} Cr/yr  (compare with top-down; aim within 20-30%)")
