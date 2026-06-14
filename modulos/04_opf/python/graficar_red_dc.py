from pathlib import Path
import pandas as pd

base = Path(__file__).resolve().parents[1]
buses = pd.read_csv(base / "datos" / "opf_dc_barras.csv")
lines = pd.read_csv(base / "datos" / "opf_dc_lineas.csv")
print("Barras del caso DC:")
print(buses)
print("\nLíneas del caso DC:")
print(lines)
