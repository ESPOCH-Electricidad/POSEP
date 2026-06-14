from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = [
    "presentacion_principal/00_presentacion_general_curso.md",
    "modulos/01_fundamentos_optimizacion/teoria/01_de_decision_a_modelo.md",
    "modulos/02_fundamentos_ampl/guias/04_control_flujo_for_repeat_if.md",
    "modulos/03_operacion_corto_plazo/ampl/01_despacho_economico/dispatch.mod",
    "modulos/04_opf_flujo_optimo_potencia/ampl/01_opf_dc/opf_dc.mod",
    "modulos/06_tnep_expansion_transmision/ampl/02_tnep_dc/tnep_dc.mod",
    "modulos/07_gep_expansion_generacion/ampl/02_gep_multianual/gep_multiyear.mod",
]
missing = [p for p in required if not (root / p).exists()]
print(f"Archivos totales: {sum(1 for _ in root.rglob('*') if _.is_file())}")
if missing:
    print("Faltantes:")
    for p in missing:
        print(" -", p)
    raise SystemExit(1)
print("Verificación básica completada: paquete v16 consistente.")
