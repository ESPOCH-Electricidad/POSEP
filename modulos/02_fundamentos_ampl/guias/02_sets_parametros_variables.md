# Guía 02 — Conjuntos, parámetros y variables

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Guías](README.md)

## Conjuntos

```ampl
set G;      # generadores
set T;      # periodos
set L;      # líneas
```

## Parámetros

```ampl
param Demand{T};
param Pmax{G};
param Cost{G};
```

## Variables

```ampl
var P{G,T} >= 0;
var u{G,T} binary;
```

Cada parámetro debe tener nombre, índice, unidad, significado y tabla de valores.
