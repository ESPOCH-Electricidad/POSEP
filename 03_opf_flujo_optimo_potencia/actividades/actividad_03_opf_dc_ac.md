# Actividad 03 — Flujo óptimo de potencia: OPF-DC y OPF-AC

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/ruta_aprendizaje.md) · [Modelos](../../docs/mapa_modelos.md) · [Casos](../../docs/mapa_casos.md) · [Evaluación](../../docs/evaluacion.md)


## 0. Revisión previa obligatoria

Antes de desarrollar esta actividad, el estudiante debe revisar los documentos de la carpeta `../modelos/` del bloque correspondiente. La actividad no consiste en copiar el modelo revisado en clase: primero debe replicar su lógica y luego construir una variante, escenario o extensión propia.

## 1. Contexto

El flujo óptimo de potencia permite determinar el despacho de generación considerando restricciones de red.
A diferencia del despacho económico, el OPF reconoce que la energía debe transportarse por líneas con límites físicos.
Esta actividad evalúa la capacidad del estudiante para formular un OPF-DC y ampliar la discusión hacia OPF-AC.

## 2. Objetivo general

Construir un modelo OPF-DC desde datos tabulados, ejecutar escenarios de congestión y comparar la interpretación con los
requerimientos adicionales de un OPF-AC.

## 3. Datos del sistema de prueba

El sistema posee cinco barras, cuatro generadores y siete líneas de transmisión.

### Tabla 1. Barras y demanda

| Barra | Tipo | Demanda activa Pd [MW] | Demanda reactiva Qd [MVAr] |
|------:|------|------------------------:|----------------------------:|
| 1 | Slack | 0  | 0  |
| 2 | PV    | 70 | 25 |
| 3 | PQ    | 90 | 35 |
| 4 | PQ    | 60 | 20 |
| 5 | PQ    | 80 | 30 |

### Tabla 2. Generadores

| Gen | Barra | Costo variable [USD/MWh] | Pmin [MW] | Pmax [MW] | Qmin [MVAr] | Qmax [MVAr] |
|----|------:|---------------------------:|----------:|----------:|------------:|------------:|
| G1 | 1 | 20 | 30 | 220 | -80 | 120 |
| G2 | 2 | 28 | 20 | 160 | -60 | 90  |
| G3 | 3 | 45 | 0  | 100 | -40 | 70  |
| G4 | 5 | 55 | 0  | 90  | -30 | 60  |

### Tabla 3. Líneas de transmisión

| Línea | Desde | Hasta | r [p.u.] | x [p.u.] | b [p.u.] | Límite [MW] |
|------|------:|------:|---------:|---------:|---------:|------------:|
| L12 | 1 | 2 | 0.020 | 0.060 | 0.030 | 120 |
| L13 | 1 | 3 | 0.080 | 0.240 | 0.025 | 100 |
| L23 | 2 | 3 | 0.060 | 0.180 | 0.020 | 90  |
| L24 | 2 | 4 | 0.060 | 0.180 | 0.020 | 80  |
| L34 | 3 | 4 | 0.010 | 0.030 | 0.015 | 70  |
| L35 | 3 | 5 | 0.080 | 0.240 | 0.025 | 75  |
| L45 | 4 | 5 | 0.030 | 0.090 | 0.020 | 85  |

### Tabla 4. Parámetros generales

| Parámetro | Valor |
|----------|------:|
| Base MVA | 100 |
| Límite inferior tensión AC | 0.95 p.u. |
| Límite superior tensión AC | 1.05 p.u. |
| Barra de referencia | 1 |
| Penalización por carga no servida | 3000 USD/MWh |

## 4. Trabajo solicitado

### Parte A. OPF-DC

Construya un modelo OPF-DC con:

- balance nodal activo;
- ángulo de referencia;
- flujo lineal por línea;
- límites térmicos;
- límites de generación activa;
- energía no servida por barra, penalizada.

### Parte B. Análisis de congestión

Identifique líneas saturadas, generación marginal y cambios de despacho respecto al despacho económico sin red.

### Parte C. Extensión OPF-AC

No basta con copiar la formulación AC. El estudiante debe explicar qué datos adicionales usa el OPF-AC y cómo cambia la interpretación:

- magnitudes de tensión;
- potencia reactiva;
- pérdidas;
- límites de Q;
- ecuaciones no lineales.

Si el docente lo solicita, el estudiante debe implementar una versión AC simplificada.

## 5. Archivos requeridos

```text
actividad_03_opf.dat
actividad_03_opf_dc.mod
actividad_03_opf_ac.mod   # si se implementa
actividad_03.run
actividad_03.out
resultados_actividad_03.xlsx
informe_actividad_03.pdf
```

## 6. Escenarios obligatorios

| Escenario | Modificación |
|----------|--------------|
| Base | Datos originales |
| S1 — Demanda alta | Aumentar Pd en barras 3, 4 y 5 en 15 % |
| S2 — Corredor limitado | Reducir límite de L24 y L34 en 30 % |
| S3 — Salida de línea | Retirar L35 |
| S4 — Generación local restringida | Reducir Pmax de G3 a 40 MW |
| S5 — Refuerzo operativo | Aumentar límite de L24 a 120 MW |

## 7. Excel de resultados

Debe incluir:

### Hoja 1. Datos de red

Barras, generadores y líneas.

### Hoja 2. Resultados OPF-DC

| Escenario | Barra | Generación [MW] | Demanda [MW] | ENS [MW] | Ángulo [rad] |
|----------|------:|----------------:|-------------:|---------:|-------------:|

### Hoja 3. Flujos por línea

| Escenario | Línea | Desde | Hasta | Flujo [MW] | Límite [MW] | Carga [%] | Congestionada |
|----------|-------|------:|------:|-----------:|------------:|----------:|---------------|

### Hoja 4. Gráficos

1. barras de generación por escenario;
2. carga porcentual de líneas;
3. mapa simple de congestión;
4. costo total por escenario.

## 8. Preguntas directrices

1. ¿Qué líneas se congestionan en el caso base?
2. ¿Qué generador aumenta su despacho cuando se limita un corredor?
3. ¿Existe energía no servida? ¿Dónde aparece y por qué?
4. ¿Cómo se diferencia el resultado OPF-DC de un despacho económico sin red?
5. ¿Qué restricciones adicionales hacen que el OPF-AC sea más exigente?
6. ¿Qué escenario muestra mayor fragilidad de la red?
7. ¿Qué refuerzo operativo reduce más el costo del sistema?

## 9. Evaluación

Consultar `rubrica_actividad_03.csv`.
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/ruta_aprendizaje.md) · [Modelos](../../docs/mapa_modelos.md) · [Casos](../../docs/mapa_casos.md) · [Evaluación](../../docs/evaluacion.md)
