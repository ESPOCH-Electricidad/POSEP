from pathlib import Path
import pandas as pd
from amplpy import AMPL

base = Path(__file__).resolve().parents[3]
model_path = base / "03_operacion_corto_plazo" / "ampl" / "01_despacho_economico" / "dispatch.mod"
data_path = base / "03_operacion_corto_plazo" / "ampl" / "01_despacho_economico" / "dispatch.dat"

ampl = AMPL()
ampl.read(str(model_path))
ampl.read_data(str(data_path))
ampl.set_option("solver", "highs")
ampl.solve()

pg = ampl.get_variable("Pg").get_values().to_pandas()
pg.to_csv("dispatch_results_from_amplpy.csv")

print("Resultados exportados a dispatch_results_from_amplpy.csv")
