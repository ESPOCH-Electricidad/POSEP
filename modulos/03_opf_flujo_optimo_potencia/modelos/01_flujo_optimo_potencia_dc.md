# Modelo 01 — Flujo óptimo de potencia DC

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

El OPF-DC incorpora red de transmisión mediante balance nodal, ángulos de barra, reactancias y límites de flujo activo.

## 2. Enunciado

Para una red de 3 barras, 3 líneas, 2 generadores y demanda por barra, determine el despacho de mínimo costo respetando límites de transmisión.



## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| N | barras |
| L | líneas |
| G | generadores |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| From[l] | - | barra de origen de la línea l |
| To[l] | - | barra de destino de la línea l |
| X[l] | p.u. | reactancia de la línea |
| Fmax[l] | MW | límite de flujo |
| Demand[n] | MW | demanda activa |
| GenBus[g] | - | barra donde se ubica el generador |
| Pmin[g] | MW | generación mínima |
| Pmax[g] | MW | generación máxima |
| Cost[g] | USD/MWh | costo variable |
| Slack | - | barra de referencia |

## 5. Datos completos para construir el archivo de datos

### Barras

| bus | demand_mw |
| --- | --- |
| B1 | 0 |
| B2 | 90 |
| B3 | 80 |

### Generadores

| gen | bus | pmin_mw | pmax_mw | cost_usd_mwh |
| --- | --- | --- | --- | --- |
| G1 | B1 | 0 | 160 | 18 |
| G2 | B3 | 0 | 100 | 32 |

### Líneas

| line | from | to | x_pu | fmax_mw |
| --- | --- | --- | --- | --- |
| L12 | B1 | B2 | 0.1 | 100 |
| L23 | B2 | B3 | 0.08 | 80 |
| L13 | B1 | B3 | 0.12 | 60 |

### Parámetros

| parametro | valor | unidad |
| --- | --- | --- |
| Slack | B1 | - |
| VOLL | 1000 | USD/MWh |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| Pg[g] | MW | generación activa |
| theta[n] | rad | ángulo de barra |
| F[l] | MW | flujo activo |
| ENS[n] | MW | demanda no servida |

## 7. Función objetivo

$$
\min Z=\sum_{g\in G}Cost_gPg_g+\sum_{n\in N}VOLL\,ENS_n
$$

**Explicación de la función objetivo.** Minimiza costo de generación y penaliza demanda no servida. La penalización evita soluciones que desconecten carga sin costo.

## 8. Restricciones del modelo

### Balance nodal

$$
\sum_{g:GenBus_g=n}Pg_g-Demand_n+ENS_n=\sum_{\ell\in L}A_{n,\ell}F_\ell\quad \forall n
$$

**Explicación.** Cada barra equilibra generación, demanda, ENS y flujos incidentes.

### Flujo DC

$$
F_\ell=\frac{\theta_{From_\ell}-\theta_{To_\ell}}{X_\ell}\quad \forall \ell
$$

**Explicación.** El flujo activo depende de la diferencia angular y de la reactancia.

### Límite de línea

$$
-Fmax_\ell\leq F_\ell\leq Fmax_\ell\quad \forall \ell
$$

**Explicación.** Cada línea respeta su capacidad térmica.

### Límites de generación

$$
Pmin_g\leq Pg_g\leq Pmax_g\quad \forall g
$$

**Explicación.** Cada generador opera dentro de su rango técnico.

### Barra slack

$$
\theta_{Slack}=0
$$

**Explicación.** Fija la referencia angular del sistema.

## 9. Plantilla `.dat` sugerida

```ampl
set N := B1 B2 B3;
set L := L12 L23 L13;
set G := G1 G2;

param From :=
L12 B1
L23 B2
L13 B1
;

param To :=
L12 B2
L23 B3
L13 B3
;

param X :=
L12 0.10
L23 0.08
L13 0.12
;

param Fmax :=
L12 100
L23 80
L13 60
;

param Demand :=
B1 0
B2 90
B3 80
;

param GenBus :=
G1 B1
G2 B3
;

param Pmin :=
G1 0
G2 0
;

param Pmax :=
G1 160
G2 100
;

param Cost :=
G1 18
G2 32
;

param Slack symbolic := B1;
param VOLL := 1000;
```

## 10. Resultados esperados

Reportar generación, flujos, ángulos, congestión, ENS y costo total.

## 11. Actividad asociada

[Actividad 03](../actividades/README.md)

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
