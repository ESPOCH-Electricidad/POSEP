# Planificación y Operación de Sistemas Eléctricos de Potencia

Paquete académico v16 reorganizado con la siguiente lógica docente:

1. **Presentación principal del curso**: mapa general, horizonte temporal, relación operación–planificación y flujo de herramientas.
2. **Módulo 01 — Optimización matemática aplicada**: formulación, LP, MILP, QP/NLP, dualidad, KKT, solvers y validación.
3. **Módulo 02 — AMPL aplicado**: implementación computacional, `.mod/.dat/.run`, control de flujo, conexión con Excel/CSV, Python y exportación.
4. **Módulo 03 — Operación de corto plazo**: despacho económico, costo marginal, compromiso de unidades, rampas, reservas, hidrotérmico y VOLL.
5. **Módulo 04 — Flujo óptimo de potencia**: OPF DC/AC, balance nodal, congestión, límites térmicos y precios sombra.
6. **Módulo 05 — Proyección de demanda**: energía, pico, perfiles, regresión, series de tiempo, escenarios y exportación a modelos.
7. **Módulo 06 — Expansión de transmisión**: modelo transporte, DC-TNEP, big-M, candidatos y expansión multietapa.
8. **Módulo 07 — Expansión de generación**: GEP estático, bloques de carga, multianual, reserva, CRF, LCOE y screening curves.

## Criterio de rediseño

El módulo 01 queda dedicado a optimización. La economía de la energía no se ubica como bloque inicial, sino en los módulos donde se usa: despacho económico, expansión de generación y evaluación de inversiones. El horizonte temporal se ubica en la presentación principal porque funciona como mapa conceptual del curso.

## Estructura general

```text
presentacion_principal/
modulos/
  01_fundamentos_optimizacion/
  02_fundamentos_ampl/
  03_operacion_corto_plazo/
  04_opf_flujo_optimo_potencia/
  05_proyeccion_demanda/
  06_tnep_expansion_transmision/
  07_gep_expansion_generacion/
codigo_comun/
casos_integradores/
docs/
referencias/
```

## Uso recomendado

- Iniciar con `presentacion_principal/00_presentacion_general_curso.md`.
- En cada módulo, revisar primero `teoria/`, luego `modelos/`, después `ampl/` o `python/`, y finalmente `actividades/`.
- Las plantillas AMPL están separadas para que el estudiante observe la relación entre formulación algebraica, datos y ejecución.
- Los scripts Python complementan lectura de datos, generación de `.dat`, análisis de resultados y gráficos.

## Archivos clave añadidos en v16

- Teoría completa para cada módulo, separada en secciones.
- Plantillas AMPL reales para despacho económico, UC, OPF DC, TNEP y GEP.
- Scripts de automatización AMPL con `for`, `repeat while`, lectura desde Excel/CSV y exportación.
- Presentación principal en Markdown y Beamer (`.tex`).
- Auditoría v16 con verificación de cobertura del paquete.
