# Guía AMPL para las actividades

[Menú principal](../README.md)

AMPL se utiliza para escribir la formulación algebraica de los modelos. En este curso no basta con ejecutar un archivo: el estudiante debe pasar del enunciado a los conjuntos, parámetros, variables, función objetivo y restricciones.

## Estructura de trabajo

Para cada actividad de optimización se recomienda preparar tres archivos:

```text
nombre_modelo.mod   formulación algebraica
nombre_modelo.dat   datos del caso
nombre_modelo.run   comandos de ejecución
```

El archivo `.mod` no debe contener datos numéricos del caso; esos datos deben estar en el `.dat` o ser leídos desde tablas externas. Esta separación permite reutilizar el mismo modelo con otros escenarios.

## Elementos básicos

```ampl
set G;
param Pmax {G} >= 0;
param cvar {G} >= 0;
var Pg {G} >= 0;
```

`set` declara conjuntos, `param` declara datos conocidos y `var` declara decisiones. Una restricción indexada se escribe una vez y AMPL la expande para todos los elementos del conjunto.

```ampl
subject to LimiteGeneracion {g in G}:
    Pg[g] <= Pmax[g];
```

## Archivo de ejecución mínimo

```ampl
reset;
model actividad.mod;
data actividad.dat;
option solver highs;
solve;
display Pg;
```

El archivo `.run` debe mostrar las variables necesarias para validar el resultado. Para problemas con red, conviene mostrar también flujos, ángulos y restricciones activas. Para problemas de expansión, conviene mostrar inversión, capacidad acumulada, energía no servida y costo total.

## Bucles para escenarios

Cuando una actividad pide comparar demanda base, alta y baja, se puede resolver el mismo modelo varias veces cambiando un parámetro.

```ampl
set S := bajo base alto;
param mult_demanda {S};
param escenario symbolic;

for {s in S} {
    let escenario := s;
    solve;
    printf "%s,%f\n", s, TotalCost >> "resultados_escenarios.csv";
}
```

La salida debe revisarse con una tabla que permita comparar costo, inversión, energía no servida y variables relevantes.

## Sensibilidad con `repeat while`

```ampl
param rm default 0.10;
param k integer default 0;

repeat while k < 5 {
    solve;
    printf "%f,%f\n", rm, TotalCost >> "sensibilidad_reserva.csv";
    let rm := rm + 0.02;
    let k := k + 1;
}
```

Este patrón es útil para margen de reserva, VOLL, tasa de descuento, demanda, costo de combustible o capacidad máxima de candidatos.

## Lectura desde hojas de cálculo

Cuando el entorno tenga habilitado el manejador de hojas de cálculo, AMPL puede leer datos desde archivos `.xlsx`. En laboratorios donde esa opción no esté disponible, se recomienda convertir las tablas a `.dat` o `.csv` con Python.

```ampl
load amplxl.dll;

table Generadores IN "amplxl" "datos.xlsx" "Generadores":
    G <- [GEN], Pmax, cvar;

read table Generadores;
```

## Conversión desde Python

Python puede usarse para validar tablas y escribir un archivo `.dat` con nombres consistentes.

```python
from pathlib import Path
import pandas as pd

gen = pd.read_csv("datos/ed_generadores.csv")

with Path("actividad.dat").open("w", encoding="utf-8") as f:
    f.write("set G := " + " ".join(gen["generador"]) + ";\n")
    f.write("param Pmax :=\n")
    for _, row in gen.iterrows():
        f.write(f"{row['generador']} {row['pmax_mw']}\n")
    f.write(";\n")
```

Antes de resolver, verifique que los nombres de columnas, conjuntos e índices coincidan con los usados en el `.mod`.
