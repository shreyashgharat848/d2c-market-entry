"""Unit economics, 3-year projection, and sensitivity. All inputs are ILLUSTRATIVE: edit them."""
import numpy as np, pandas as pd

A = dict(aov=550, orders_per_year=2.2, gross_margin=0.60, fulfil_per_order=90,
         cac=300, repeat_rate=0.35, fixed_cost_per_year=[1.5e7, 1.2e7, 1.2e7],  # Rs
         new_customers=[40000, 60000, 80000])

def contribution_per_customer(a):
    rev = a["aov"] * a["orders_per_year"]
    return rev * a["gross_margin"] - a["fulfil_per_order"] * a["orders_per_year"]

def projection(a):
    base = 0; rows = []; cum = 0
    for yr in range(3):
        new = a["new_customers"][yr]
        active = new + base * a["repeat_rate"]
        # new customers pay CAC; repeat customers earn contribution with no CAC
        contrib = contribution_per_customer(a) * active
        acq = new * a["cac"]
        profit = contrib - acq - a["fixed_cost_per_year"][yr]
        cum += profit; base = active
        rows.append([f"Year {yr+1}", new, round(active), contrib/1e7, acq/1e7,
                     a["fixed_cost_per_year"][yr]/1e7, profit/1e7, cum/1e7])
    return pd.DataFrame(rows, columns=["Year","New","Active","Contribution_Cr","CAC_spend_Cr",
                                       "Fixed_Cr","Profit_Cr","Cumulative_Cr"])

print(f"Contribution per customer/yr: Rs {contribution_per_customer(A):.0f}")
print(f"CAC payback (months): {A['cac']/contribution_per_customer(A)*12:.1f}\n")
print(projection(A).round(2).to_string(index=False))

# Sensitivity: 3-year cumulative profit vs CAC and repeat rate
cacs = [A["cac"]*f for f in (0.8, 1.0, 1.2)]; reps = [A["repeat_rate"]+d for d in (-0.10, 0, 0.10)]
grid = pd.DataFrame([[projection({**A, "cac": c, "repeat_rate": r}).Cumulative_Cr.iloc[-1]
                      for r in reps] for c in cacs],
                    index=[f"CAC Rs {c:.0f}" for c in cacs], columns=[f"Repeat {r:.0%}" for r in reps])
print("\n3-year cumulative profit (Rs Cr):\n", grid.round(2))
