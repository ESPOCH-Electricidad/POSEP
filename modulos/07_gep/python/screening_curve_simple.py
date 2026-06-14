from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
tech = pd.read_csv(root / 'datos' / 'gep_tecnologias.csv')
params = pd.read_csv(root / 'datos' / 'gep_parametros.csv')
r = float(params.loc[params['parametro'].eq('discount_rate'), 'valor'].iloc[0]) if 'parametro' in params.columns and params['parametro'].eq('discount_rate').any() else 0.1
life = int(params.loc[params['parametro'].eq('life_years'), 'valor'].iloc[0]) if 'parametro' in params.columns and params['parametro'].eq('life_years').any() else 25
crf = r*(1+r)**life/((1+r)**life-1)
hours = np.linspace(0, 8760, 100)

fig, ax = plt.subplots(figsize=(8,4.8))
for _, row in tech.iterrows():
    fixed = (row['capex_usd_kw']*crf + row['fom_usd_kw_anio']) * 1000  # USD/MW-year
    cost = fixed + row['vom_usd_mwh'] * hours
    ax.plot(hours, cost/1000, label=row['tecnologia'])
ax.set_xlabel('Horas de utilización [h/año]')
ax.set_ylabel('Costo anual aproximado [kUSD/MW-año]')
ax.set_title('Screening curve simplificada')
ax.grid(True, alpha=0.3)
ax.legend()
out = root / 'figuras' / 'screening_curve_generada.png'
fig.tight_layout()
fig.savefig(out, dpi=180)
print(f'Figura guardada en: {out}')
