# Actividad 04 — Proyección de demanda eléctrica

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Datos](../datos/)

## Competencia

Construir una proyección de demanda eléctrica diferenciando energía anual, demanda pico, variables explicativas, validación histórica y escenarios de planificación.

## Enunciado

A partir de datos históricos de energía, demanda pico, población y PIB, construya una proyección para los años 2025, 2030 y 2035. La salida debe alimentar modelos de expansión de transmisión y generación.

## Datos

Use:

- `demanda_historica_completa.csv` para exploración y regresión.
- `demanda_series_tiempo.csv` para tendencia.
- `variables_socioeconomicas.csv` para variables explicativas.
- `plantilla_demanda_proyectada.csv` como formato de salida.

## Tareas

1. Grafique energía anual y demanda pico 2018-2024.
2. Calcule factor de carga anual:

$$
LF_y=\frac{E_y}{P_y^{peak}8760}
$$

3. Ajuste una proyección de energía y pico usando al menos dos enfoques:
   - crecimiento compuesto;
   - regresión con población y PIB o tendencia temporal.
4. Evalúe el ajuste histórico con MAE, RMSE y MAPE.
5. Construya tres escenarios: bajo, medio y alto.
6. Exporte dos archivos:
   - `demanda_tnep.csv`: año, escenario, pico MW;
   - `demanda_gep.csv`: año, escenario, energía GWh, pico MW.
7. Explique qué escenario usaría para una planificación conservadora y por qué.

## Validación

- La energía proyectada debe ser coherente con la trayectoria histórica.
- El pico debe crecer de forma compatible con energía y factor de carga.
- Los escenarios no deben cruzarse: bajo ≤ medio ≤ alto.
- Las unidades deben permanecer en GWh y MW según corresponda.

## Producto esperado

| Producto | Contenido |
|---|---|
| Script o libro de cálculo | Procesamiento, proyección, métricas y exportación. |
| Tablas | Histórico, métricas, escenarios. |
| Figuras | Energía/pico histórico, proyección por escenario, factor de carga. |
| Archivos de salida | `demanda_tnep.csv` y `demanda_gep.csv`. |
| Informe | Supuestos, método, validación y lectura para planificación. |

## Evaluación

| Criterio | Peso |
|---|---:|
| Tratamiento correcto de energía y pico | 25 % |
| Construcción de escenarios | 25 % |
| Validación con métricas | 20 % |
| Exportación útil para TNEP/GEP | 20 % |
| Claridad de interpretación | 10 % |
