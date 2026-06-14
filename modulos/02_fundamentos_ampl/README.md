# Módulo 02 — AMPL aplicado a modelos de optimización

Este módulo convierte las formulaciones del Módulo 01 en archivos ejecutables. El objetivo no es solo conocer sintaxis, sino construir flujos reproducibles: modelo, datos, ejecución, escenarios, exportación y depuración.

## Resultado de aprendizaje

El estudiante será capaz de:

- escribir modelos algebraicos en archivos `.mod`;
- separar datos en `.dat`, `.csv` o Excel;
- automatizar corridas con `.run` usando `for`, `repeat while`, `if`, `let`, `printf` y `table`;
- exportar resultados para análisis posterior;
- conectar AMPL con Python mediante `amplpy` cuando se requiera un flujo más robusto.

## Secuencia sugerida

1. `guias/01_estructura_archivos_ampl.md`
2. `guias/02_sets_parametros_variables.md`
3. `guias/03_modelo_datos_run.md`
4. `guias/04_control_flujo_for_repeat_if.md`
5. `guias/05_importacion_excel_csv.md`
6. `guias/06_exportacion_resultados.md`
7. `guias/07_depuracion_modelos.md`
8. `plantillas/`

## Archivos AMPL clave

- `plantillas/pintura/`: LP básico.
- `plantillas/transporte/`: modelo de transporte.
- `plantillas/control_flujo/`: automatización con escenarios y sensibilidad.
- `plantillas/excel_read/`: lectura desde Excel con `table`.
- `plantillas/excel_export/`: exportación de resultados.
