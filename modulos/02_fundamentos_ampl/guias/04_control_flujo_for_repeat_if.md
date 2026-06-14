# 4. Control de flujo en AMPL: `for`, `repeat while`, `if` y `let`

## Idea central

En estudios de operación y planificación no se resuelve un único caso. Se resuelven escenarios de demanda, precios de combustible, hidrología, tasas de descuento o criterios de reserva. Por eso AMPL debe usarse también como lenguaje de ejecución.

## Bucle `for`

```ampl
for {s in SCEN} {
    let ActiveScenario := s;
    solve;
    printf "%s,%g\n", s, TotalCost >> "resultados.csv";
}
```

Uso típico:

- demanda baja/base/alta;
- hidrología seca/media/húmeda;
- sensibilidades de combustible;
- comparación de candidatos de expansión.

## Bucle `repeat while`

```ampl
param k integer default 0;
param r default 0.06;

repeat while k < 6 {
    solve;
    printf "%g,%g\n", r, TotalCost >> "sensibilidad.csv";
    let r := r + 0.01;
    let k := k + 1;
}
```

Uso típico:

- sensibilidad de tasa de descuento;
- sensibilidad de VOLL;
- incremento progresivo de demanda;
- búsqueda de umbrales de factibilidad.

## Condicional `if`

```ampl
if solve_result != "solved" then {
    display solve_result;
    break;
}
```

Uso típico:

- detener corridas infactibles;
- separar casos con y sin solución;
- exportar logs de validación.

## Cambio de datos con `let`

```ampl
let demand[t] := demand[t] * 1.05;
```

`let` modifica parámetros o variables iniciales durante la ejecución. Debe usarse con cuidado para evitar perder trazabilidad de datos.
