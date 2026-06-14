from pathlib import Path
import pandas as pd

input_file = Path("input_dispatch.xlsx")
out_file = Path("dispatch_generated.dat")

gen = pd.read_excel(input_file, sheet_name="Generators")
dem = pd.read_excel(input_file, sheet_name="Demand")

required_gen = {"GEN", "Pmin", "Pmax", "cvar"}
required_dem = {"PERIOD", "demand"}
if not required_gen.issubset(gen.columns):
    raise ValueError(f"Missing generator columns: {required_gen - set(gen.columns)}")
if not required_dem.issubset(dem.columns):
    raise ValueError(f"Missing demand columns: {required_dem - set(dem.columns)}")

with out_file.open("w", encoding="utf-8") as f:
    f.write("set G := " + " ".join(gen["GEN"].astype(str)) + ";\n")
    f.write("set T := " + " ".join(dem["PERIOD"].astype(str)) + ";\n\n")

    for col in ["Pmin", "Pmax", "cvar"]:
        f.write(f"param {col} :=\n")
        for _, row in gen.iterrows():
            f.write(f"{row['GEN']} {row[col]}\n")
        f.write(";\n\n")

    f.write("param demand :=\n")
    for _, row in dem.iterrows():
        f.write(f"{row['PERIOD']} {row['demand']}\n")
    f.write(";\n")

print(f"Archivo generado: {out_file}")
