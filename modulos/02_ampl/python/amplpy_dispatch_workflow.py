from pathlib import Path
import pandas as pd
from amplpy import AMPL

# Ejemplo de flujo AMPL-Python. Requiere amplpy y un solver instalado.
repo = Path(__file__).resolve().parents[3]
model_path = repo / "modulos" / "03_despacho_economico" / "ampl" / "dispatch.mod"
data_path = repo / "modulos" / "03_despacho_economico" / "ampl" / "dispatch.dat"
out_file = Path("dispatch_results_from_amplpy.csv")

ampl = AMPL()
ampl.read(str(model_path))
ampl.read_data(str(data_path))
ampl.set_option("solver", "highs")
ampl.solve()

pg = ampl.get_variable("Pg").get_values().to_pandas()
pg.to_csv(out_file)

print(f"Resultados exportados a {out_file}")
