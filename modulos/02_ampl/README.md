[← Inicio](../../README.md) | [← Módulo anterior](../01_optimizacion/README.md) | [Siguiente módulo →](../03_despacho_economico/README.md)

# Módulo 02 — AMPL para modelos eléctricos

## Objetivo del módulo

El objetivo es aprender a convertir una formulación algebraica en archivos ejecutables de AMPL. El módulo trabaja la separación entre modelo, datos y comandos de ejecución, el uso de conjuntos e índices, la automatización con estructuras de control, la lectura de datos desde archivos externos y la exportación de resultados.

AMPL se usa aquí como herramienta de modelación algebraica. El estudiante no debe memorizar comandos aislados, sino entender cómo cada instrucción representa una parte del modelo matemático.

## Contenidos

1. [Estructura de un proyecto AMPL](#estructura-de-un-proyecto-ampl)
2. [Conjuntos, parámetros, variables y restricciones](#conjuntos-parámetros-variables-y-restricciones)
3. [Archivos `.mod`, `.dat` y `.run`](#archivos-mod-dat-y-run)
4. [Estructuras de control](#estructuras-de-control)
5. [Lectura desde Excel o CSV](#lectura-desde-excel-o-csv)
6. [Exportación y depuración](#exportación-y-depuración)
7. [Archivos incluidos](#archivos-incluidos)
8. [Actividad propuesta](#actividad-propuesta)

## Estructura de un proyecto AMPL

Un modelo reproducible debe separar tres responsabilidades:

- `.mod`: formulación algebraica. Define conjuntos, parámetros, variables, función objetivo y restricciones.
- `.dat`: datos del caso de estudio. Asigna valores a conjuntos y parámetros.
- `.run`: comandos de ejecución. Carga modelo, datos, solver, resuelve, muestra y exporta resultados.

![Anatomía AMPL](figuras/01_anatomia_archivos_ampl.svg)

Esta separación evita mezclar teoría con datos. El mismo modelo puede ejecutarse con distintos casos; el mismo caso puede ser analizado con distintos solvers; y los resultados pueden exportarse sin modificar la formulación.

## Conjuntos, parámetros, variables y restricciones

Un conjunto define el dominio de los índices:

```ampl
set G;     # generadores
set T;     # periodos
```

Un parámetro almacena datos:

```ampl
param demand {T} >= 0;
param Pmax {G} >= 0;
param cvar {G} >= 0;
```

Una variable representa la decisión:

```ampl
var Pg {G,T} >= 0;
```

Una restricción impone una relación técnica:

```ampl
subject to Balance {t in T}:
    sum {g in G} Pg[g,t] = demand[t];
```

La lectura correcta es: para cada periodo $t$, la suma de generación de todos los generadores debe igualar la demanda del periodo. Esta interpretación es más importante que la sintaxis.

## Archivos `.mod`, `.dat` y `.run`

Un archivo `.run` mínimo contiene:

```ampl
reset;
model dispatch.mod;
data dispatch.dat;
option solver highs;
solve;
display Pg, TotalCost;
```

La instrucción `reset` limpia la sesión. `model` carga la formulación. `data` carga el caso. `option solver` selecciona el solver. `solve` resuelve. `display` permite inspeccionar resultados.

Para modelos grandes, se recomienda exportar resultados con `printf`, porque permite generar archivos CSV ordenados:

```ampl
printf "g,t,Pg\n" > "resultados.csv";
printf {g in G, t in T} "%s,%s,%g\n", g, t, Pg[g,t] >> "resultados.csv";
```

## Estructuras de control

AMPL permite automatizar escenarios, sensibilidades y validaciones.

Ejemplo con `for`:

```ampl
for {s in SCEN} {
    let ActiveScenario := s;
    solve;
    printf {g in G, t in T} "%s,%s,%s,%g\n", s, g, t, Pg[g,t]
        >> "dispatch_by_scenario.csv";
}
```

Este patrón sirve para recorrer demanda baja, base y alta; hidrología seca, media y húmeda; precios de combustible; límites de reserva o indisponibilidades.

Ejemplo con `repeat while`:

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

La instrucción `let` modifica valores durante la ejecución. Esto permite hacer sensibilidad sin editar manualmente el archivo `.dat`.

## Lectura desde Excel o CSV

Para usar Excel directamente en AMPL se puede emplear `amplxl`, cuando está disponible en la instalación:

```ampl
load amplxl.dll;

table Productos IN "amplxl" "../datos/pintura_ampl.xlsx" "Productos":
    P <- [producto], beneficio;

read table Productos;
```

En entornos docentes suele ser más robusto usar Python para leer Excel o CSV, validar nombres de columnas y generar archivos `.dat`. Esa ruta reduce errores cuando los laboratorios tienen instalaciones distintas.

Flujo recomendado:

```text
Excel o CSV → Python/pandas → archivo .dat → AMPL → CSV de resultados → Python/gráficos
```

## Exportación y depuración

Errores frecuentes en AMPL:

| Error | Causa probable |
|---|---|
| Índice no definido | Un conjunto no contiene el elemento usado. |
| Parámetro sin valor | Falta un dato en el archivo `.dat`. |
| Modelo infactible | Las restricciones son incompatibles. |
| Modelo no acotado | Falta una restricción que limite una variable. |
| Resultado extraño | Error de unidades o dato mal escalado. |

Comandos útiles:

```ampl
display G, T;
display demand;
expand Balance;
show Pg;
```

`expand` es especialmente útil porque muestra la restricción ya instanciada con sus índices y coeficientes.


## Datos y plantillas de trabajo

Este módulo conserva plantillas AMPL y scripts de apoyo porque su objetivo es enseñar implementación. Aquí sí es importante que el estudiante vea estructuras reales de código: separación `.mod/.dat/.run`, ciclos `for`, sensibilidad con `repeat while`, lectura desde Excel/CSV, exportación de resultados y uso de Python como puente de datos.

| Archivo | Contenido/encabezado |
|---|---|
| `pintura_ampl.xlsx` | archivo de apoyo |

### Archivos AMPL de referencia

| Archivo | Contenido/encabezado |
|---|---|
| `dispatch_excel_read.run` | archivo de apoyo |
| `dispatch_export_csv.run` | archivo de apoyo |
| `exportar_resultados_csv.run` | archivo de apoyo |
| `for_escenarios.run` | archivo de apoyo |
| `if_validacion.run` | archivo de apoyo |
| `pintura.dat` | archivo de apoyo |
| `pintura.mod` | archivo de apoyo |
| `pintura.run` | archivo de apoyo |
| `read_excel_pintura.run` | archivo de apoyo |
| `repeat_while_sensibilidad.run` | archivo de apoyo |
| `transporte.dat` | archivo de apoyo |
| `transporte.mod` | archivo de apoyo |
| `transporte.run` | archivo de apoyo |

### Scripts Python de apoyo

| Archivo | Contenido/encabezado |
|---|---|
| `amplpy_dispatch_workflow.py` | archivo de apoyo |
| `amplpy_pandas_excel.py` | archivo de apoyo |
| `excel_to_dat_dispatch.py` | archivo de apoyo |

## Archivos incluidos

| Archivo | Uso |
|---|---|
| [ampl/pintura.mod](ampl/pintura.mod) | Modelo básico LP. |
| [ampl/transporte.mod](ampl/transporte.mod) | Modelo de transporte. |
| [ampl/for_escenarios.run](ampl/for_escenarios.run) | Automatización con `for`. |
| [ampl/repeat_while_sensibilidad.run](ampl/repeat_while_sensibilidad.run) | Sensibilidad con `repeat while`. |
| [ampl/read_excel_pintura.run](ampl/read_excel_pintura.run) | Lectura directa desde Excel con `amplxl`. |
| [ampl/exportar_resultados_csv.run](ampl/exportar_resultados_csv.run) | Exportación de resultados a CSV. |
| [python/excel_to_dat_dispatch.py](python/excel_to_dat_dispatch.py) | Conversión Excel/CSV a `.dat`. |
| [python/amplpy_dispatch_workflow.py](python/amplpy_dispatch_workflow.py) | Flujo AMPL–Python con `amplpy`. |

## Cómo ejecutar

Desde `modulos/02_ampl/ampl/`:

```bash
ampl pintura.run
ampl transporte.run
ampl for_escenarios.run
ampl repeat_while_sensibilidad.run
```

Para scripts de Python:

```bash
python ../python/excel_to_dat_dispatch.py
```

## Actividad propuesta

Tome un modelo lineal del módulo 01 y sepárelo en tres archivos: `.mod`, `.dat` y `.run`. Luego cree un archivo `.run` adicional que ejecute tres escenarios modificando un parámetro con `let` y exporte los resultados a CSV.
