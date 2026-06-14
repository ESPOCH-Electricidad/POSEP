from pathlib import Path
import pandas as pd

csv_file = Path("input.csv")
out_file = Path("output.dat")
set_name = "I"
param_name = "value"

# El CSV debe tener columnas: id,value
df = pd.read_csv(csv_file)
if not {"id", "value"}.issubset(df.columns):
    raise ValueError("El CSV debe contener columnas id,value")

with out_file.open("w", encoding="utf-8") as f:
    f.write(f"set {set_name} := " + " ".join(df["id"].astype(str)) + ";\n\n")
    f.write(f"param {param_name} :=\n")
    for _, row in df.iterrows():
        f.write(f"{row['id']} {row['value']}\n")
    f.write(";\n")

print(f"Archivo generado: {out_file}")
