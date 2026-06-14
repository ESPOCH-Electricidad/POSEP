# 7. Depuración de modelos AMPL

## Errores frecuentes

| Error | Causa común | Revisión sugerida |
|---|---|---|
| índice inexistente | set incompleto o nombre mal escrito | `display SET;` |
| parámetro sin valor | dato faltante en `.dat` | `display param;` |
| dimensión incorrecta | parámetro 2D leído como 1D | revisar declaración `{i,j}` |
| infactibilidad | demanda/capacidad incompatible | revisar balance y límites |
| no acotado | variable sin límite o costo mal firmado | revisar dominio y objetivo |
| resultado extraño | unidades inconsistentes | MW, MWh, USD/MWh, horas |

## Comandos útiles

```ampl
display G, T;
display demand, Pmax;
expand Balance;
show Pg;
display solve_result, solve_message;
```

## Validación posterior

Después de `solve`, exportar resultados y revisar:

- suma de generación vs demanda;
- límites de potencia;
- variables binarias;
- costo total;
- periodos con déficit o energía no servida.
