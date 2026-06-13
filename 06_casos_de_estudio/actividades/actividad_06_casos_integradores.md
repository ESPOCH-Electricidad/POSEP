# Actividad 06 — Casos integradores de operación y planificación

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)


## 0. Revisión previa obligatoria

Antes de desarrollar esta actividad, el estudiante debe revisar los documentos de la carpeta `../modelos/` del bloque correspondiente. La actividad no consiste en copiar el modelo revisado en clase: primero debe replicar su lógica y luego construir una variante, escenario o extensión propia.

## 1. Contexto

La última evaluación integra los bloques de la asignatura. El estudiante debe seleccionar un caso de estudio, identificar qué
modelo corresponde al problema planteado, construir los archivos AMPL desde cero y comparar resultados entre modelos o escenarios.

Esta actividad no busca repetir un modelo aislado, sino demostrar criterio de ingeniería para elegir, adaptar y defender una
formulación.

## 2. Objetivo general

Desarrollar un estudio integrador de operación y planificación de sistemas eléctricos, seleccionando un caso de estudio y
formulando el modelo AMPL apropiado para resolverlo.

## 3. Casos disponibles

### Tabla 1. Catálogo de casos

| Caso | Barras | Líneas/corredores | Generadores | Uso recomendado |
|------|-------:|------------------:|------------:|-----------------|
| Caso A — Sistema didáctico 3 barras | 3 | 3 | 2 | ED, OPF-DC básico |
| Caso B — Sistema didáctico 5 barras | 5 | 7 | 4 | OPF-DC, OPF-AC |
| Caso C — Garver 6 barras | 6 | 11 corredores | 3 zonas de generación | TNEP, GEP simplificado |
| Caso D — IEEE 14 adaptado | 14 | según datos del repositorio | según datos del repositorio | OPF-DC/AC |
| Caso E — IEEE 24 RTS adaptado | 24 | según datos del repositorio | según datos del repositorio | UC, OPF, confiabilidad |

### Tabla 2. Matriz de selección de modelo

| Pregunta técnica | Modelo sugerido |
|------------------|-----------------|
| ¿Cuánto genera cada unidad en una hora? | ED |
| ¿Qué unidades se encienden durante un horizonte horario? | UC |
| ¿La red limita el despacho? | OPF-DC / OPF-AC |
| ¿Qué líneas deben construirse? | TNEP |
| ¿Qué generación debe instalarse en el largo plazo? | GEP |
| ¿Cómo cambia el sistema ante varios escenarios? | Modelo base + sensibilidad |

## 4. Trabajo solicitado

Cada grupo o estudiante debe elegir un caso y desarrollar un estudio que incluya al menos dos niveles:

### Nivel 1. Modelo principal

Debe seleccionar uno de los siguientes:

- ED;
- UC;
- OPF-DC;
- OPF-AC;
- TNEP;
- GEP.

### Nivel 2. Extensión o comparación

Debe seleccionar una extensión:

- sensibilidad de demanda;
- sensibilidad de costos;
- salida de línea o generador;
- restricción ambiental;
- comparación ED vs OPF;
- comparación transporte vs DC;
- comparación GEP base vs GEP con emisiones.

## 5. Datos mínimos que debe construir el estudiante

El estudiante debe construir sus archivos `.dat` desde las tablas del caso seleccionado. Si utiliza datos del repositorio,
debe transformarlos a la estructura de su propio modelo.

Debe entregar:

```text
actividad_06_caso.dat
actividad_06_modelo_principal.mod
actividad_06_extension.mod      # si corresponde
actividad_06.run
actividad_06.out
resultados_actividad_06.xlsx
informe_actividad_06.pdf
```

## 6. Contenido mínimo del informe

1. Justificación del caso seleccionado.
2. Selección del modelo y justificación.
3. Formulación matemática completa.
4. Construcción de datos.
5. Implementación AMPL.
6. Resultados base.
7. Extensión o escenario.
8. Comparación de resultados.
9. Discusión de limitaciones.
10. Conclusiones.

## 7. Excel de resultados

El Excel debe contener:

### Hoja 1. Datos del caso

Datos transcritos y depurados.

### Hoja 2. Resultados base

Resultados principales del modelo seleccionado.

### Hoja 3. Escenario o extensión

Resultados del caso modificado.

### Hoja 4. Comparación

| Indicador | Caso base | Caso modificado | Cambio absoluto | Cambio porcentual | Interpretación |
|----------|----------:|----------------:|----------------:|------------------:|----------------|

### Hoja 5. Gráficos

Al menos tres gráficos, seleccionados según el modelo:

- generación por unidad;
- flujos por línea;
- líneas construidas;
- capacidad instalada;
- costo total;
- ENS;
- emisiones.

## 8. Preguntas directrices

1. ¿Por qué seleccionó ese modelo y no otro?
2. ¿Qué simplificaciones introduce su formulación?
3. ¿Qué restricciones condicionan más la solución?
4. ¿Qué variables representan decisiones físicas y cuáles decisiones económicas?
5. ¿Qué cambia al modificar el parámetro seleccionado?
6. ¿El resultado sería útil para tomar una decisión real? ¿Qué validaciones adicionales harían falta?
7. ¿Qué aprendizaje del curso fue más importante para resolver el caso?

## 9. Criterios de evaluación

Consultar `rubrica_actividad_06.csv`.
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)
