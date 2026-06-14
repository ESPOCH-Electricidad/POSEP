# Guía 01 — Estructura de archivos AMPL

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Guías](README.md)

## Idea central

AMPL separa el modelo algebraico de los datos. Esta separación permite resolver el mismo problema con distintos casos.

```text
caso/
├── modelo.mod
├── datos.dat
└── ejecutar.run
```

## Flujo típico

```ampl
reset;
model modelo.mod;
data datos.dat;
option solver highs;
solve;
display variable_principal;
```

Un proyecto AMPL está bien organizado si el modelo puede cambiar de caso sustituyendo solo el archivo `.dat`.
