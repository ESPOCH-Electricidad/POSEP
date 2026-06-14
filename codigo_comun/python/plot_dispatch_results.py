from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

file = Path("dispatch_pg.csv")
df = pd.read_csv(file)
pivot = df.pivot(index="period", columns="generator", values="power")
ax = pivot.plot(kind="bar", stacked=True)
ax.set_xlabel("Periodo")
ax.set_ylabel("Potencia [MW]")
ax.set_title("Despacho por generador")
plt.tight_layout()
plt.savefig("dispatch_stack.png", dpi=200)
print("Figura generada: dispatch_stack.png")
