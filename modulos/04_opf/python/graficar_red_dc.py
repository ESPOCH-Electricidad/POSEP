from pathlib import Path
import math
import pandas as pd
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
buses = pd.read_csv(root / 'datos' / 'opf_dc_barras.csv')
lines = pd.read_csv(root / 'datos' / 'opf_dc_lineas.csv')

names = list(buses['bus'])
pos = {b: (math.cos(2*math.pi*i/len(names)), math.sin(2*math.pi*i/len(names))) for i,b in enumerate(names)}

fig, ax = plt.subplots(figsize=(5.5, 5))
for _, r in lines.iterrows():
    x1,y1 = pos[r['from']]; x2,y2 = pos[r['to']]
    ax.plot([x1,x2], [y1,y2], linewidth=1.5)
    ax.text((x1+x2)/2, (y1+y2)/2, f"{r['line']}\n{r['fmax_mw']} MW", ha='center', va='center', fontsize=8)
for _, r in buses.iterrows():
    x,y = pos[r['bus']]
    ax.scatter([x],[y], s=500)
    ax.text(x, y, f"{r['bus']}\nD={r['demand_mw']}", ha='center', va='center', fontsize=9)
ax.set_title('Red DC didáctica')
ax.axis('off')
out = root / 'figuras' / 'red_dc_generada.png'
fig.tight_layout()
fig.savefig(out, dpi=180)
print(f'Figura guardada en: {out}')
