# Actividades — Fundamentos de optimización

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Datos](../datos/) · [Guía AMPL](../../../docs/guia_ampl.md)

Las actividades de este módulo buscan que el estudiante pase de un enunciado verbal a una formulación algebraica y luego a una implementación reproducible. Cada actividad debe entregarse con formulación, archivo `.dat`, archivo `.mod`, archivo `.run`, resultados y análisis.

| Actividad | Competencia principal | Enlace |
|---|---|---|
| 01A | Formular un LP de producción y analizar restricciones activas | [Programación lineal](actividad_01_programacion_lineal.md) |
| 01B | Formular un problema de transporte con oferta, demanda y costos | [Transporte de energía](actividad_01_transporte_energia.md) |
| 01C | Formular un MILP de selección binaria con cobertura mínima | [Localización de antenas](actividad_01_localizacion_antenas.md) |

## Entrega común

Cada estudiante debe presentar una carpeta con:

```text
actividad_01X/
  modelo.mod
  caso.dat
  ejecutar.run
  resultados.csv
  informe.pdf o informe.md
```

El informe debe explicar qué restricciones se activan, cómo se validó la solución y qué cambia ante una variación de datos.
