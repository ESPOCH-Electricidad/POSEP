# Modelo 02 — Flujo óptimo de potencia AC

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

El OPF-AC representa potencia activa y reactiva, magnitudes de tensión, ángulos, pérdidas y límites eléctricos. Es un modelo no lineal.

## 2. Enunciado

Para una red de 3 barras con cargas activas/reactivas, líneas con R/X/B y dos generadores, determine la operación de mínimo costo respetando límites de tensión y potencia reactiva.



## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| N | barras |
| L | líneas |
| G | generadores |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| R[l] | p.u. | resistencia |
| X[l] | p.u. | reactancia |
| Bsh[l] | p.u. | susceptancia de línea |
| Pload[n] | MW | demanda activa |
| Qload[n] | MVAr | demanda reactiva |
| Vmin[n] | p.u. | tensión mínima |
| Vmax[n] | p.u. | tensión máxima |
| Pmin/Pmax[g] | MW | límites activos |
| Qmin/Qmax[g] | MVAr | límites reactivos |
| GenBus[g] | - | barra del generador |
| Cost[g] | USD/MWh | costo activo |

## 5. Datos completos para construir el archivo de datos

### Barras

| bus | pload_mw | qload_mvar | vmin_pu | vmax_pu |
| --- | --- | --- | --- | --- |
| B1 | 0 | 0 | 0.95 | 1.05 |
| B2 | 80 | 30 | 0.95 | 1.05 |
| B3 | 60 | 25 | 0.95 | 1.05 |

### Generadores

| gen | bus | pmin_mw | pmax_mw | qmin_mvar | qmax_mvar | cost_usd_mwh |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | B1 | 0 | 180 | -80 | 120 | 20 |
| G2 | B3 | 0 | 100 | -50 | 80 | 35 |

### Líneas

| line | from | to | r_pu | x_pu | bsh_pu | smax_mva |
| --- | --- | --- | --- | --- | --- | --- |
| L12 | B1 | B2 | 0.02 | 0.1 | 0.02 | 120 |
| L23 | B2 | B3 | 0.015 | 0.08 | 0.015 | 100 |
| L13 | B1 | B3 | 0.025 | 0.12 | 0.025 | 90 |

### Parámetros

| parametro | valor | unidad |
| --- | --- | --- |
| Slack | B1 | - |
| BaseMVA | 100 | MVA |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| Pg[g] | MW | generación activa |
| Qg[g] | MVAr | generación reactiva |
| V[n] | p.u. | magnitud de tensión |
| theta[n] | rad | ángulo |

## 7. Función objetivo

$$
\min Z=\sum_{g\in G}Cost_gPg_g
$$

**Explicación de la función objetivo.** Minimiza costo de generación activa. Las variables de tensión y reactivos aparecen para garantizar factibilidad eléctrica.

## 8. Restricciones del modelo

### Balance activo AC

$$
P^G_i-P^D_i=V_i\sum_jV_j(G_{ij}\cos\theta_{ij}+B_{ij}\sin\theta_{ij})
$$

**Explicación.** La inyección activa en cada barra debe coincidir con los flujos activos calculados por la red.

### Balance reactivo AC

$$
Q^G_i-Q^D_i=V_i\sum_jV_j(G_{ij}\sin\theta_{ij}-B_{ij}\cos\theta_{ij})
$$

**Explicación.** La inyección reactiva sostiene el perfil de tensión y cumple la demanda Q.

### Límites de tensión

$$
Vmin_i\leq V_i\leq Vmax_i\quad \forall i
$$

**Explicación.** Cada barra debe operar dentro del rango admisible de tensión.

### Límites de generación

$$
Pmin_g\leq Pg_g\leq Pmax_g,\quad Qmin_g\leq Qg_g\leq Qmax_g
$$

**Explicación.** Cada generador respeta límites de potencia activa y reactiva.

## 9. Guía para construir el archivo `.dat`

A partir de las tablas anteriores, prepare el archivo de datos respetando los nombres de conjuntos, parámetros y unidades del modelo. La siguiente estructura muestra cómo debe organizarse la información.

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

param R :=
L12 0.02
L23 0.015
L13 0.025
;

param X :=
L12 0.10
L23 0.08
L13 0.12
;

param Bsh :=
L12 0.02
L23 0.015
L13 0.025
;

param Pload :=
B1 0
B2 80
B3 60
;

param Qload :=
B1 0
B2 30
B3 25
;

param Vmin :=
B1 0.95
B2 0.95
B3 0.95
;

param Vmax :=
B1 1.05
B2 1.05
B3 1.05
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
G1 180
G2 100
;

param Qmin :=
G1 -80
G2 -50
;

param Qmax :=
G1 120
G2 80
;

param Cost :=
G1 20
G2 35
;

param Slack symbolic := B1;
param BaseMVA := 100;
```

## 10. Resultados esperados

Reportar generación P/Q, perfil de tensión, ángulos, flujos aparentes y pérdidas.

## 11. Actividad asociada

[Actividad 03](../actividades/README.md)

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
