# Modelo 03 — DC de expansión de transmisión

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

El modelo DC incorpora ángulos y reactancias para aproximar flujos físicos.

## 2. Enunciado

Decida expansión de transmisión minimizando inversión y ENS con balance nodal DC.



## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| N | barras |
| L | corredores |
| L_EXIST | corredores existentes |
| L_CAND | corredores candidatos |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| From[l]/To[l] | - | barras terminales |
| X[l] | p.u. | reactancia |
| Fmax[l] | MW | capacidad por circuito |
| n0[l] | circuitos | existentes |
| InvCost[l] | MUSD | costo de inversión |
| MaxNew[l] | circuitos | máximo de nuevos |
| Demand[n] | MW | demanda por barra |
| GenMax[n] | MW | capacidad de generación por barra |
| VOLL | USD/MWh | penalización ENS |

## 5. Datos completos para construir el archivo de datos

### Barras

| bus | demand_mw | genmax_mw |
| --- | --- | --- |
| B1 | 0 | 150 |
| B2 | 80 | 0 |
| B3 | 120 | 0 |
| B4 | 50 | 100 |

### Corredores

| line | from | to | tipo | x_pu | fmax_mw | invcost_musd | maxnew |
| --- | --- | --- | --- | --- | --- | --- | --- |
| L12 | B1 | B2 | existente | 0.1 | 100 | 0 | 0 |
| L23 | B2 | B3 | existente | 0.08 | 80 | 0 | 0 |
| L34 | B3 | B4 | existente | 0.11 | 70 | 0 | 0 |
| C13 | B1 | B3 | candidato | 0.12 | 90 | 40 | 1 |
| C24 | B2 | B4 | candidato | 0.1 | 80 | 35 | 1 |
| C14 | B1 | B4 | candidato | 0.15 | 100 | 55 | 1 |

### Años

| anio | factor_demanda |
| --- | --- |
| 2025 | 1.0 |
| 2030 | 1.15 |
| 2035 | 1.35 |

### Parámetros

| parametro | valor | unidad |
| --- | --- | --- |
| VOLL | 1000 | USD/MWh |
| Slack | B1 | - |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| F[l] | MW | flujo por corredor |
| n[l] | entera | circuitos nuevos |
| Gen[n] | MW | generación por barra |
| ENS[n] | MW | demanda no servida |
| theta[n] | rad | ángulo, si aplica |

## 7. Función objetivo

$$
\min Z=\sum_{\ell\in L_{cand}}InvCost_\ell n_\ell+\sum_nVOLL\,ENS_n
$$

**Explicación de la función objetivo.** Minimiza inversión y penalización por energía no servida; algunos modelos agregan costo operativo o descuento temporal.

## 8. Restricciones del modelo

### Balance nodal

$$
Gen_n-Demand_n+ENS_n=\sum_{\ell}A_{n,\ell}F_\ell\quad \forall n
$$

**Explicación.** Cada barra equilibra generación, demanda, ENS y flujos.

### Capacidad de corredor

$$
-Fmax_\ell(n^0_\ell+n_\ell)\leq F_\ell\leq Fmax_\ell(n^0_\ell+n_\ell)
$$

**Explicación.** La capacidad depende de circuitos existentes y nuevos.

### Límite de inversión

$$
0\leq n_\ell\leq MaxNew_\ell\quad \forall \ell\in L_{cand}
$$

**Explicación.** Cada corredor candidato tiene un número máximo de circuitos nuevos.

### Flujo DC

$$
F_\ell=(\theta_{From_\ell}-\theta_{To_\ell})/X_\ell
$$

**Explicación.** Vincula flujo con diferencia angular.

### Slack

$$
\theta_{Slack}=0
$$

**Explicación.** Define referencia angular.

## 9. Guía para construir el archivo `.dat`

A partir de las tablas anteriores, prepare el archivo de datos respetando los nombres de conjuntos, parámetros y unidades del modelo. La siguiente estructura muestra cómo debe organizarse la información.

```ampl
set N := B1 B2 B3 B4;
set L := L12 L23 L34 C13 C24 C14;
set L_EXIST := L12 L23 L34;
set L_CAND := C13 C24 C14;

param From :=
L12 B1
L23 B2
L34 B3
C13 B1
C24 B2
C14 B1
;

param To :=
L12 B2
L23 B3
L34 B4
C13 B3
C24 B4
C14 B4
;

param X :=
L12 0.10
L23 0.08
L34 0.11
C13 0.12
C24 0.10
C14 0.15
;

param Fmax :=
L12 100
L23 80
L34 70
C13 90
C24 80
C14 100
;

param n0 :=
L12 1
L23 1
L34 1
C13 0
C24 0
C14 0
;

param InvCost :=
C13 40
C24 35
C14 55
;

param MaxNew :=
C13 1
C24 1
C14 1
;

param Demand :=
B1 0
B2 80
B3 120
B4 50
;

param GenMax :=
B1 150
B2 0
B3 0
B4 100
;

param VOLL := 1000;
param Slack symbolic := B1;
```

## 10. Resultados esperados

Reportar inversión, ángulos, flujos y congestión.

## 11. Actividad asociada

[Actividad 05](../actividades/README.md)

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
