# Guía 06 — Errores frecuentes y depuración

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Guías](README.md)

| Error | Causa probable | Corrección |
|---|---|---|
| índice no definido | se usa un elemento fuera del conjunto | revisar `set` en `.dat` |
| parámetro sin valor | falta dato para algún índice | completar tabla |
| dimensión incorrecta | matriz declarada con índices distintos | revisar filas/columnas |
| modelo infactible | restricciones incompatibles | revisar demanda, límites y balances |
| modelo no acotado | falta límite o restricción | agregar cotas o balance |

Comandos útiles:

```ampl
display G;
display Demand;
expand Balance;
solve;
display solve_result;
```
