# Guía 03 — Modelo, datos y ejecución

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Guías](README.md)

## Ejemplo mínimo `.mod`

```ampl
set G;
param Demand;
param Pmax{G};
param Cost{G};
var P{g in G} >= 0, <= Pmax[g];

minimize TotalCost:
    sum {g in G} Cost[g] * P[g];

subject to Balance:
    sum {g in G} P[g] = Demand;
```

## Ejemplo mínimo `.dat`

```ampl
set G := G1 G2 G3;
param Demand := 150;
param Pmax := G1 100 G2 80 G3 60;
param Cost := G1 15 G2 22 G3 35;
```

## Ejemplo `.run`

```ampl
reset;
model despacho.mod;
data despacho.dat;
option solver highs;
solve;
display P, TotalCost;
```
