from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

base = Path(__file__).resolve().parents[1]
tech = pd.read_csv(base / "datos" / "gep_tecnologias.csv")

name_col = "technology" if "technology" in tech.columns else "tecnologia"
fixed_col = "fixed_cost" if "fixed_cost" in tech.columns else "fom_usd_kw_anio"
var_col = "variable_cost" if "variable_cost" in tech.columns else "vom_usd_mwh"
capex_col = "capex_usd_kw" if "capex_usd_kw" in tech.columns else None

hours = np.linspace(0, 8760, 100)
r = 0.10
life = 25
crf = r * (1 + r) ** life / ((1 + r) ** life - 1)

plt.figure(figsize=(8, 4.5))
for _, row in tech.iterrows():
    fixed = float(row[fixed_col])
    if capex_col:
        fixed += float(row[capex_col]) * crf
    y = fixed + float(row[var_col]) * hours / 1000.0
    plt.plot(hours, y, label=str(row[name_col]))

plt.xlabel("Horas equivalentes de operación [h/año]")
plt.ylabel("Costo anual equivalente aproximado [USD/kW-año]")
plt.title("Screening curve simplificada")
plt.legend()
plt.tight_layout()
out = base / "figuras" / "screening_curve_generada.png"
plt.savefig(out, dpi=200)
print(f"Figura guardada en {out}")
