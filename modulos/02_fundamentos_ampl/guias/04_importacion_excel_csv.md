# Guía 04 — Importación desde Excel y CSV

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Guías](README.md)

## Recomendación docente

El flujo más robusto para clase es:

```text
Excel/CSV → Python/pandas → archivo .dat → AMPL
```

También se puede leer Excel directamente con manejadores de tablas cuando la instalación lo permite.

```ampl
load amplxl.dll;

table Products IN "amplxl" "pintura_ampl.xlsx" "products":
    P <- [PRODUCT], price, rate, market;

read table Products;
```

La sintaxis exacta puede depender del manejador disponible y de la instalación local.
