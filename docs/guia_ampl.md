# Guía AMPL para las actividades

[Menú principal](../README.md)

AMPL se utilizará como lenguaje algebraico para convertir una formulación matemática en un modelo computacional. En las actividades se construyen tres archivos coherentes:

```text
modelo.mod   estructura algebraica: conjuntos, parámetros, variables, objetivo y restricciones
caso.dat     datos del caso: conjuntos, tablas, escalares y parámetros indexados
ejecutar.run comandos de ejecución: cargar, resolver y reportar
```

## Del modelo matemático al archivo `.mod`

Un archivo `.mod` debe declarar primero los conjuntos, después los parámetros, luego las variables y finalmente la función objetivo y restricciones. La estructura mínima es:

```ampl
set G;
set T;

param demand {T} >= 0;
param pmax {G} >= 0;
param cost {G} >= 0;

var Pg {G,T} >= 0;

minimize TotalCost:
    sum {g in G, t in T} cost[g] * Pg[g,t];

subject to Balance {t in T}:
    sum {g in G} Pg[g,t] = demand[t];
```

La sintaxis AMPL debe conservar la lógica de la formulación. Si una restricción se escribe para todo generador y todo periodo, en AMPL debe indexarse como `{g in G, t in T}`. Si un parámetro tiene dos dimensiones, el archivo `.dat` debe proveer datos compatibles con esas dos dimensiones.

## Construcción del archivo `.dat`

Los datos del caso se deben tomar de las tablas del módulo. Un parámetro escalar se escribe como:

```ampl
param ReserveMargin := 0.15;
```

Un parámetro indexado se escribe como:

```ampl
set G := G1 G2 G3;

param pmax :=
G1 100
G2 80
G3 60
;
```

Una tabla bidimensional puede escribirse con pares de índices:

```ampl
param cost :=
F1 C1 5
F1 C2 7
F2 C1 6
F2 C2 4
;
```

## Archivo `.run`

El archivo `.run` debe permitir reproducir la solución:

```ampl
reset;
model modelo.mod;
data caso.dat;
option solver highs;
solve;
display TotalCost;
```

Cuando el modelo incluya varias salidas, use `display` para exploración y `printf` para reportes ordenados.

## Automatización de escenarios

Para estudiar sensibilidad, se puede recorrer un conjunto de escenarios:

```ampl
set S;
param demand_scenario {S};

for {s in S} {
    let Demand := demand_scenario[s];
    solve;
    printf "%s %.4f\n", s, TotalCost >> "resultados.csv";
}
```

Para variar un parámetro de forma incremental:

```ampl
param rm default 0.10;
param k integer default 0;

repeat while k < 5 {
    solve;
    printf "%g %.4f\n", rm, TotalCost >> "sensibilidad_reserva.csv";
    let rm := rm + 0.025;
    let k := k + 1;
}
```

## Revisión antes de entregar

Antes de reportar resultados, verifique que los nombres de conjuntos coincidan entre `.mod` y `.dat`, que los parámetros tengan las unidades correctas, que no existan restricciones sin índice y que las salidas permitan comprobar balance y límites.
