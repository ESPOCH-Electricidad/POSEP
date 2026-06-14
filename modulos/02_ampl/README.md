[← Inicio](../../README.md) | [← Módulo anterior](../01_optimizacion/README.md) | [Siguiente módulo →](../03_despacho_economico/README.md)

# Módulo 02 — AMPL para modelos eléctricos

## Objetivo

Traducir formulaciones matemáticas a AMPL mediante archivos `.mod`, `.dat` y `.run`. El módulo no parte de modelos terminados: trabaja con datos y formulaciones para que el estudiante escriba su propia implementación.

![Anatomía AMPL](figuras/01_anatomia_archivos_ampl.svg)

## Sintaxis esencial

Declaración de conjuntos, parámetros y variables:

```ampl
set G;
param Pmax {G};
var Pg {G} >= 0;
```

Suma indexada:

```ampl
sum {g in G} Pg[g]
```

Restricción indexada:

```ampl
subject to Limite {g in G}:
    Pg[g] <= Pmax[g];
```

## Caso 1. Traducción del problema de pinturas

### Datos completos

**Productos**

| producto   |   precio_usd_l |   produccion_l_h |   demanda_max_l |
|:-----------|---------------:|-----------------:|----------------:|
| azul       |             10 |               40 |            1000 |
| negra      |             15 |               30 |             860 |

**Parámetros generales**

| parametro         |   valor | unidad   |
|:------------------|--------:|:---------|
| horas_disponibles |      40 | h/semana |

### Formulación a implementar

$$
\max Z=\sum_{p\in P}r_px_p
$$

$$
\sum_{p\in P}\frac{x_p}{a_p}\leq H
$$

$$
0\leq x_p\leq \bar{x}_p \qquad \forall p\in P
$$

### Actividad

Escriba `pintura.mod`, `pintura.dat` y `pintura.run`. En el `.dat`, declare el conjunto `P` y los parámetros usando las tablas anteriores.

## Caso 2. Escenarios en AMPL

### Enunciado

Prepare un despacho por escenarios. La demanda cambia según el escenario y el archivo `.run` debe resolver cada caso.

### Datos completos

**Generadores**

| gen   |   pmin_mw |   pmax_mw |   costo_usd_mwh |
|:------|----------:|----------:|----------------:|
| G1    |         0 |       120 |              18 |
| G2    |         0 |       100 |              26 |
| G3    |         0 |        80 |              40 |

**Escenarios**

| escenario   |   demanda_mw |
|:------------|-------------:|
| bajo        |          120 |
| base        |          150 |
| alto        |          180 |

### Formulación

$$
\min Z_s=\sum_{g\in G}c_gP_{g,s}
$$

$$
\sum_{g\in G}P_{g,s}=D_s \qquad \forall s\in S
$$

$$
P_g^{min}\leq P_{g,s}\leq P_g^{max} \qquad \forall g\in G,s\in S
$$

### Estructuras a usar

Bucle `for`:

```ampl
for {s in S} {
    let ActiveScenario := s;
    solve;
}
```

Bucle `repeat while`:

```ampl
repeat while k < 5 {
    solve;
    let k := k + 1;
}
```

Condicional:

```ampl
if TotalDemand > TotalCapacity then {
    printf "Caso infactible por falta de capacidad\n";
}
```

### Actividad

Construya un `.run` que resuelva los escenarios bajo, base y alto. Exporte al menos generación por unidad, demanda atendida y costo total.
