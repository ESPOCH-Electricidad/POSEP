from pathlib import Path
import pandas as pd

base = Path(__file__).resolve().parents[1]
corredores = pd.read_csv(base / "datos" / "tnep_corredores.csv")
print("Corredores existentes y candidatos:")
print(corredores)

if {"from", "to", "tipo", "invcost_musd"}.issubset(corredores.columns):
    print("\nResumen de inversión candidata:")
    cand = corredores[corredores["tipo"].astype(str).str.lower().str.contains("candidato")]
    print(cand[["from", "to", "fmax_mw", "invcost_musd", "maxnew"]])
elif {"i", "j", "existing", "invcost"}.issubset(corredores.columns):
    print("\nResumen de inversión candidata:")
    print(corredores[["i", "j", "existing", "invcost"]])
