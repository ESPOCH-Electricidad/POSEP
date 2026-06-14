# Guía AMPL para los modelos del curso

[Menú principal](../README.md) · [Ruta de aprendizaje](ruta_aprendizaje.md) · [Evaluación](evaluacion.md)

Esta guía acompaña los ejemplos, modelos y actividades de los módulos. Su finalidad es que el estudiante pueda pasar de una formulación matemática a tres archivos de trabajo: `.mod`, `.dat` y `.run`.

## 1. Relación entre formulación y AMPL

Cada modelo del curso se presenta con enunciado, datos, conjuntos, parámetros, variables, función objetivo y restricciones. En AMPL esa estructura se traduce de forma directa:

| Elemento de la formulación | Elemento en AMPL | Ejemplo de declaración |
|---|---|---|
| Conjunto | `set` | `set G;` |
| Parámetro escalar | `param` | `param Demand >= 0;` |
| Parámetro indexado | `param` con índice | `param Pmax {G} >= 0;` |
| Variable continua | `var` | `var P {G} >= 0;` |
| Variable binaria | `var` con dominio | `var u {G,T} binary;` |
| Objetivo | `minimize` o `maximize` | `minimize TotalCost: ...;` |
| Restricción | `subject to` | `subject to Balance: ...;` |

El archivo `.mod` debe contener la estructura algebraica del problema. El archivo `.dat` debe contener los datos del caso. El archivo `.run` debe indicar cómo cargar, resolver y reportar el modelo.

## 2. Estructura mínima de un archivo `.mod`

La construcción recomendada es escribir primero los conjuntos, luego los parámetros, después las variables, la función objetivo y finalmente las restricciones.

```ampl
# Conjuntos
set G;
set T;

# Parámetros
param Demand {T} >= 0;
param Pmin {G} >= 0;
param Pmax {G} >= 0;
param Cost {G} >= 0;

# Variables
var P {G,T} >= 0;

# Función objetivo
minimize TotalCost:
    sum {g in G, t in T} Cost[g] * P[g,t];

# Restricciones
subject to Balance {t in T}:
    sum {g in G} P[g,t] = Demand[t];

subject to Limits {g in G, t in T}:
    Pmin[g] <= P[g,t] <= Pmax[g];
```

Antes de escribir el modelo, revise que cada símbolo usado en una ecuación tenga una declaración previa en AMPL. Un error común es usar un índice o parámetro que no fue declarado.

## 3. Construcción del archivo `.dat`

Los datos de cada caso están en las tablas del enunciado y en archivos CSV dentro de `datos/`. El archivo `.dat` debe respetar los nombres usados en el `.mod`.

### Parámetro escalar

```ampl
param Demand := 150;
```

### Conjunto simple

```ampl
set G := G1 G2 G3;
```

### Parámetro indexado por un conjunto

```ampl
param Pmax :=
G1 100
G2  80
G3  60
;
```

### Parámetro bidimensional

```ampl
param CostTransport:
        L1   L2   L3 :=
S1      4    6    9
S2      5    4    7
;
```

### Conjunto de pares

```ampl
set LINES :=
(B1,B2)
(B1,B3)
(B2,B3)
;
```

En modelos de red conviene declarar líneas como pares ordenados, por ejemplo `set L within {BUS,BUS};`, para evitar confusión entre barras, líneas y corredores.

## 4. Archivo `.run`

Un archivo `.run` básico permite limpiar la sesión, cargar modelo y datos, seleccionar solver, resolver y mostrar resultados.

```ampl
reset;
model actividad.mod;
data actividad.dat;

option solver highs;
solve;

display TotalCost;
display P;
```

En problemas MILP puede utilizarse un solver compatible con variables binarias o enteras. En problemas NLP u OPF AC se requiere un solver no lineal.

## 5. Uso de índices y sumatorias

AMPL permite escribir restricciones para todos los elementos de un conjunto. Esta es una de sus ventajas principales frente a escribir ecuaciones una por una.

```ampl
subject to Balance {t in T}:
    sum {g in G} P[g,t] = Demand[t];
```

La expresión anterior crea una restricción de balance para cada periodo `t`.

Cuando se necesita filtrar un conjunto, puede usarse una condición dentro del índice:

```ampl
sum {(i,j) in LINES: i = b} Flow[i,j]
```

Este tipo de expresión es útil en balance nodal, expansión de transmisión y modelos con redes.

## 6. Variables binarias y restricciones de activación

En modelos de compromiso de unidades, localización y expansión se utilizan variables binarias.

```ampl
var u {G,T} binary;
var P {G,T} >= 0;
```

Una restricción típica vincula una variable continua con una decisión binaria:

```ampl
subject to GenerationUpper {g in G, t in T}:
    P[g,t] <= Pmax[g] * u[g,t];
```

Si `u[g,t] = 0`, la unidad queda apagada y la generación debe ser cero. Si `u[g,t] = 1`, la generación puede tomar valores hasta su capacidad máxima.

## 7. Automatización con `for`

El comando `for` permite resolver varios escenarios o casos sin modificar manualmente los archivos.

```ampl
set SCEN;
param factor {SCEN};
param ActiveFactor;

for {s in SCEN} {
    let ActiveFactor := factor[s];
    solve;
    printf "%s,%g\n", s, TotalCost >> "resultados_escenarios.csv";
}
```

Esta estructura es útil para demanda baja, base y alta; hidrología seca, media y húmeda; precios de combustible; límites de inversión o criterios de reserva.

## 8. Sensibilidad con `repeat while`

`repeat while` permite repetir una corrida hasta cumplir una condición. Es apropiado para analizar una tasa, una penalización o un límite que cambia por pasos.

```ampl
param r default 0.06;
param k integer default 0;

repeat while k < 6 {
    solve;
    printf "%g,%g\n", r, TotalCost >> "sensibilidad.csv";
    let r := r + 0.01;
    let k := k + 1;
}
```

En expansión de generación, `r` puede representar tasa de descuento. En operación, el parámetro variable puede ser demanda, reserva, VOLL o precio de combustible.

## 9. Exportación de resultados

Para reportar resultados conviene escribir archivos CSV desde AMPL.

```ampl
printf "gen,periodo,p_mw\n" > "generacion.csv";
printf {g in G, t in T} "%s,%s,%g\n", g, t, P[g,t] >> "generacion.csv";
```

La primera línea crea el encabezado. La segunda escribe los resultados por índice.

## 10. Lectura directa desde Excel

Cuando la instalación de AMPL dispone del manejador para Excel, se puede leer una hoja `.xlsx` con `table`. El nombre de las columnas debe coincidir con los campos declarados o debe mapearse explícitamente.

```ampl
reset;
load amplxl.dll;
model actividad.mod;

table Generadores IN "amplxl" "datos_actividad.xlsx" "Generadores":
    G <- [gen], Pmin, Pmax, Cost;

read table Generadores;
solve;
```

En aulas o laboratorios donde la lectura directa de Excel no esté configurada, una ruta estable es exportar las hojas a CSV o construir el `.dat` desde Python.

## 11. Construcción de `.dat` desde Excel con Python

El siguiente patrón permite leer una hoja de cálculo y escribir un archivo `.dat`. Debe adaptarse a los nombres de columnas de cada caso.

```python
from pathlib import Path
import pandas as pd

archivo = Path("datos_actividad.xlsx")
gen = pd.read_excel(archivo, sheet_name="Generadores")

with open("actividad.dat", "w", encoding="utf-8") as f:
    f.write("set G := " + " ".join(gen["gen"].astype(str)) + ";\n\n")

    f.write("param Pmax :=\n")
    for _, row in gen.iterrows():
        f.write(f"{row['gen']} {row['pmax_mw']}\n")
    f.write(";\n\n")

    f.write("param Cost :=\n")
    for _, row in gen.iterrows():
        f.write(f"{row['gen']} {row['cost_usd_mwh']}\n")
    f.write(";\n")
```

Esta ruta es conveniente cuando los datos se entregan en tablas extensas, como demanda, corredores de transmisión, tecnologías de generación o bloques de carga.

## 12. Revisión del modelo antes de resolver

Antes de ejecutar `solve`, se recomienda verificar dimensiones y datos.

```ampl
display G;
display T;
display Demand;
display Pmax;
```

Para revisar cómo AMPL expandió una restricción:

```ampl
expand Balance;
```

Si el modelo resulta infactible, revise primero balance, límites mínimos, límites máximos, demanda, reserva y unidades.

## 13. Entregables AMPL por actividad

Para las actividades de optimización, operación, OPF, TNEP y GEP, el estudiante debe entregar:

| Archivo | Contenido esperado |
|---|---|
| `.mod` | Formulación algebraica implementada en AMPL |
| `.dat` | Datos del caso construidos desde las tablas del enunciado |
| `.run` | Secuencia de ejecución, solver y reportes |
| `.csv` de salida | Resultados exportados desde AMPL, cuando aplique |
| informe breve | Interpretación técnica de resultados, validación y sensibilidad |

El archivo `.mod` debe derivarse de las ecuaciones del modelo, no de una plantilla cerrada. El archivo `.dat` debe construirse a partir de los datos del caso.

---

[Menú principal](../README.md) · [Ruta de aprendizaje](ruta_aprendizaje.md) · [Evaluación](evaluacion.md)
