from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
gen = pd.read_csv(root / 'datos' / 'ed_generadores.csv').sort_values('cost_usd_mwh')
demand = float(pd.read_csv(root / 'datos' / 'ed_demanda.csv').loc[0, 'valor'])

gen['width'] = gen['pmax_mw']
gen['left'] = gen['width'].cumsum() - gen['width']

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.bar(gen['left'], gen['cost_usd_mwh'], width=gen['width'], align='edge', edgecolor='black')
ax.axvline(demand, linestyle='--', linewidth=1.5)
ax.set_xlabel('Potencia acumulada [MW]')
ax.set_ylabel('Costo variable [USD/MWh]')
ax.set_title('Orden de mérito y demanda')
ax.grid(True, axis='y', alpha=0.3)
out = root / 'figuras' / 'orden_merito_generado.png'
out.parent.mkdir(exist_ok=True)
fig.tight_layout()
fig.savefig(out, dpi=180)
print(f'Figura guardada en: {out}')
