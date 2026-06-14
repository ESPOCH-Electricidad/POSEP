from pathlib import Path
import pandas as pd

# Lee el archivo Excel del módulo y genera un .dat de AMPL.
# El nombre de hojas/columnas puede ajustarse según la plantilla usada en clase.
base = Path(__file__).resolve().parents[1]
excel_path = base / "datos" / "pintura_ampl.xlsx"
out_file = base / "ampl" / "pintura_generado.dat"

products = pd.read_excel(excel_path, sheet_name="products")
params = pd.read_excel(excel_path, sheet_name="parameters")

with out_file.open("w", encoding="utf-8") as f:
    f.write("set P := " + " ".join(products["PRODUCT"].astype(str)) + ";\n\n")

    for col in ["price", "rate", "market"]:
        f.write(f"param {col} :=\n")
        for _, row in products.iterrows():
            f.write(f"{row['PRODUCT']} {row[col]}\n")
        f.write(";\n\n")

    hours = params.loc[params["parameter"].eq("Hours"), "value"].iloc[0]
    f.write(f"param Hours := {hours};\n")

print(f"Archivo generado: {out_file}")
