from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

base = Path(__file__).resolve().parents[1]
gen = pd.read_csv(base / "datos" / "ed_generadores.csv")

name_col = "gen" if "gen" in gen.columns else gen.columns[0]
pmax_col = "Pmax" if "Pmax" in gen.columns else "pmax_mw"
cost_col = "cvar" if "cvar" in gen.columns else "cost_usd_mwh"

missing = [c for c in [pmax_col, cost_col] if c not in gen.columns]
if missing:
    raise ValueError(f"Faltan columnas requeridas: {missing}")

gen = gen.sort_values(cost_col).reset_index(drop=True)

plt.figure(figsize=(8, 4.5))
left = 0.0
for _, row in gen.iterrows():
    width = float(row[pmax_col])
    plt.bar(left, float(row[cost_col]), width=width, align="edge", edgecolor="black")
    plt.text(left + width/2, float(row[cost_col]) + 1, str(row[name_col]), ha="center", fontsize=8)
    left += width

plt.xlabel("Potencia acumulada [MW]")
plt.ylabel("Costo variable [USD/MWh]")
plt.title("Curva de oferta por orden de mérito")
plt.tight_layout()
out = base / "figuras" / "orden_merito_generado.png"
plt.savefig(out, dpi=200)
print(f"Figura guardada en {out}")
