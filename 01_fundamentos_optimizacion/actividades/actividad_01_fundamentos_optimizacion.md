# Actividad 01 — Fundamentos de optimización aplicada a sistemas eléctricos

## 1. Contexto de la actividad

En los modelos de operación y planificación de sistemas eléctricos, la primera habilidad que debe desarrollar el estudiante
es traducir un problema físico o económico a una formulación matemática. Esta actividad evalúa esa competencia a partir de
un sistema de suministro simplificado con cuatro tecnologías de generación.

La actividad se relaciona con los modelos revisados previamente en la sección `modelos/` del bloque de fundamentos:
programación lineal, programación lineal entera mixta y análisis de sensibilidad.

## 2. Objetivo general

Formular, implementar y analizar un modelo de optimización lineal para abastecimiento de demanda eléctrica,
construyendo desde cero los archivos `.dat`, `.mod`, `.run` y `.out` en AMPL.

## 3. Objetivos específicos

Al finalizar la actividad, el estudiante debe ser capaz de:

1. identificar conjuntos, índices, parámetros y variables de decisión;
2. formular una función objetivo de minimización de costo;
3. construir restricciones de balance, límites técnicos y participación mínima;
4. transformar tablas de datos en un archivo `.dat`;
5. implementar el modelo completo en AMPL;
6. analizar sensibilidad frente a cambios de demanda, costos y disponibilidad;
7. presentar resultados en Excel mediante tablas y gráficos.

## 4. Datos del caso de estudio

Se dispone de cuatro tecnologías de generación para cubrir una demanda agregada de un sistema eléctrico simplificado.

### Tabla 1. Tecnologías de generación disponibles

| Tecnología | Descripción              | Costo variable [USD/MWh] | Producción mínima [MW] | Producción máxima [MW] | Emisiones [tCO2/MWh] |
|-----------|---------------------------|---------------------------|-------------------------|-------------------------|----------------------|
| G1        | Térmica eficiente          | 18                        | 20                      | 120                     | 0.55                 |
| G2        | Térmica flexible           | 24                        | 0                       | 90                      | 0.72                 |
| G3        | Hidroeléctrica             | 6                         | 0                       | 80                      | 0.00                 |
| G4        | Solar fotovoltaica         | 0                         | 0                       | 50                      | 0.00                 |

### Tabla 2. Parámetros del sistema

| Parámetro | Valor | Unidad |
|----------|------:|--------|
| Demanda base | 210 | MW |
| Demanda alta | 245 | MW |
| Participación mínima renovable | 25 | % de la demanda |
| Límite máximo de emisiones | 95 | tCO2/h |
| Penalización por energía no servida | 1000 | USD/MWh |

## 5. Trabajo solicitado

### 5.1 Replicación del modelo base

El estudiante debe construir un modelo lineal de despacho simplificado. El modelo debe minimizar el costo total de operación,
considerando la posibilidad de energía no servida penalizada.

El modelo debe incluir, como mínimo:

#### Conjuntos

- conjunto de tecnologías de generación;
- conjunto de escenarios, cuando se realice sensibilidad.

#### Parámetros

- costo variable;
- generación mínima;
- generación máxima;
- factor de emisión;
- demanda;
- penalización por energía no servida;
- límite de emisiones;
- participación mínima renovable.

#### Variables

- potencia generada por tecnología;
- energía no servida;
- emisiones totales;
- costo total.

#### Función objetivo

Minimizar:

```text
costo de generación + penalización por energía no servida
```

#### Restricciones mínimas

1. balance de potencia;
2. límites mínimos y máximos de generación;
3. cálculo de emisiones;
4. límite máximo de emisiones;
5. participación mínima renovable;
6. no negatividad.

## 6. Archivos AMPL que debe entregar el estudiante

El estudiante debe entregar obligatoriamente:

```text
actividad_01.dat
actividad_01.mod
actividad_01.run
actividad_01.out
```

### 6.1 Archivo `.dat`

Debe ser construido desde las tablas anteriores. No se aceptará copiar datos sin estructura. El archivo debe incluir:

```ampl
set G := ... ;

param cost :=
...
;

param pmin :=
...
;

param pmax :=
...
;
```

### 6.2 Archivo `.mod`

Debe contener una formulación limpia y comentada:

```ampl
set G;

param cost{G};
param pmin{G};
param pmax{G};
param demand;

var Pg{g in G} >= 0;
```

Los nombres pueden cambiar, pero deben ser consistentes.

### 6.3 Archivo `.run`

Debe cargar modelo, datos, solver, resolver y exportar resultados. Debe incluir comandos `display` para:

- generación por tecnología;
- energía no servida;
- emisiones;
- costo total;
- restricciones relevantes.

### 6.4 Archivo `.out`

Debe contener la salida completa de AMPL. El estudiante debe señalar en su informe dónde se observan:

- valor objetivo;
- generación por tecnología;
- cumplimiento de demanda;
- energía no servida;
- restricciones activas.

## 7. Experimentos de sensibilidad

El estudiante debe resolver como mínimo los siguientes casos:

| Escenario | Cambio solicitado |
|----------|-------------------|
| Base | Datos originales |
| S1 — Demanda alta | Usar demanda de 245 MW |
| S2 — Menor disponibilidad hidro | Reducir generación máxima de G3 en 40 % |
| S3 — Mayor costo térmico | Incrementar costo de G1 y G2 en 25 % |
| S4 — Política ambiental estricta | Reducir límite de emisiones a 70 tCO2/h |

## 8. Excel de resultados

El estudiante debe entregar un archivo Excel con al menos las siguientes hojas:

### Hoja 1. Datos

Datos originales transcritos desde el enunciado.

### Hoja 2. Resultados por escenario

| Escenario | Pg_G1 | Pg_G2 | Pg_G3 | Pg_G4 | ENS | Costo total | Emisiones |
|----------|------:|------:|------:|------:|----:|------------:|----------:|

### Hoja 3. Gráficos

Debe incluir:

1. gráfico de barras apiladas de generación por tecnología;
2. gráfico de costo total por escenario;
3. gráfico de emisiones por escenario;
4. gráfico de energía no servida, si existe.

## 9. Informe técnico en PDF

El informe debe tener la siguiente estructura:

1. Introducción y descripción del problema.
2. Formulación matemática.
3. Implementación en AMPL.
4. Resultados del caso base.
5. Análisis de sensibilidad.
6. Discusión técnica.
7. Conclusiones.

## 10. Preguntas directrices de razonamiento

Responda de forma argumentada:

1. ¿Qué tecnología domina en el despacho base y por qué?
2. ¿Qué restricción condiciona más la solución: capacidad, emisiones o participación renovable?
3. ¿La energía no servida aparece en algún escenario? ¿Qué significa desde el punto de vista de planificación?
4. ¿Cómo cambia el costo marginal del sistema al aumentar la demanda?
5. ¿Qué escenario muestra mayor vulnerabilidad técnica?
6. ¿El modelo lineal construido es suficiente para representar operación real? Justifique sus limitaciones.

## 11. Criterios de evaluación

La calificación se realizará con la rúbrica incluida en `rubrica_actividad_01.csv`.
