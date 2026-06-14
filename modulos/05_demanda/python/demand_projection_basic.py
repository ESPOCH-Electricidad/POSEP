from pathlib import Path
import pandas as pd
import numpy as np

base = Path(__file__).resolve().parents[1]
data_path = base / "datos" / "demanda_historica_completa.csv"
df = pd.read_csv(data_path)

# Espera columnas: anio, energia_gwh, pico_mw
last = df.iloc[-1]
years = list(range(int(last["anio"]) + 1, int(last["anio"]) + 11))
scenarios = {"bajo": 0.02, "base": 0.035, "alto": 0.05}
rows = []
for s, g in scenarios.items():
    for k, y in enumerate(years, start=1):
        rows.append({
            "escenario": s,
            "anio": y,
            "energia_gwh": last["energia_gwh"] * (1 + g) ** k,
            "pico_mw": last["pico_mw"] * (1 + g) ** k,
        })
out = pd.DataFrame(rows)
out.to_csv(base / "datos" / "demanda_proyectada_v16.csv", index=False)
print(out.head())
