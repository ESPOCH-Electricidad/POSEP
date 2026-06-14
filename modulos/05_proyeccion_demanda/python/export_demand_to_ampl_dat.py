from pathlib import Path
import pandas as pd

base = Path(__file__).resolve().parents[1]
df = pd.read_csv(base / "datos" / "demanda_proyectada_v16.csv")
scenario = "base"
sub = df[df["escenario"] == scenario]

out = base / "datos" / "demanda_gep_v16.dat"
with out.open("w", encoding="utf-8") as f:
    f.write("set Y := " + " ".join(sub["anio"].astype(str)) + ";\n\n")
    f.write("param PeakDemand :=\n")
    for _, r in sub.iterrows():
        f.write(f"{int(r['anio'])} {r['pico_mw']:.3f}\n")
    f.write(";\n\n")
    f.write("param EnergyDemand :=\n")
    for _, r in sub.iterrows():
        f.write(f"{int(r['anio'])} {r['energia_gwh']:.3f}\n")
    f.write(";\n")
print(f"Archivo AMPL generado: {out}")
