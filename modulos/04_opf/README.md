[← Inicio](../../README.md) | [← Módulo anterior](../03_despacho_economico/README.md) | [Siguiente módulo →](../05_demanda/README.md)

# Módulo 04 — Flujo óptimo de potencia

## Objetivo

Incorporar restricciones de red al despacho mediante balance nodal, ángulos de barra, flujos y límites térmicos.

![Red de barras y líneas](figuras/01_red_barras_lineas.svg)

## Caso 1. OPF DC de tres barras

### Datos completos

**Barras**

| bus   |   demanda_mw |
|:------|-------------:|
| B1    |            0 |
| B2    |           90 |
| B3    |           80 |

**Generadores**

| gen   | bus   |   pmin_mw |   pmax_mw |   costo_usd_mwh |
|:------|:------|----------:|----------:|----------------:|
| G1    | B1    |         0 |       160 |              18 |
| G2    | B3    |         0 |       100 |              32 |

**Líneas**

| linea   | desde   | hasta   |   x_pu |   fmax_mw |
|:--------|:--------|:--------|-------:|----------:|
| L12     | B1      | B2      |   0.1  |       100 |
| L23     | B2      | B3      |   0.08 |        80 |
| L13     | B1      | B3      |   0.12 |        60 |

**Parámetros**

| parametro   | valor   | unidad   |
|:------------|:--------|:---------|
| slack       | B1      | -        |
| VOLL        | 1000    | USD/MWh  |

### Modelo matemático

Conjuntos: $n\in N$, $l\in L$, $g\in G$.

Variables:

$$
P_g\geq 0,\qquad \theta_n,\qquad f_l,\qquad ENS_n\geq 0
$$

Función objetivo:

$$
\min Z=\sum_{g\in G}c_gP_g+\sum_{n\in N}VOLL\cdot ENS_n
$$

Flujo DC para una línea $l$ entre $i$ y $j$:

$$
f_l=\frac{\theta_i-\theta_j}{x_l}
$$

Balance nodal:

$$
\sum_{g:b(g)=n}P_g+ENS_n-d_n=\sum_{l:from(l)=n}f_l-\sum_{l:to(l)=n}f_l\qquad \forall n
$$

Límites:

$$
P_g^{min}\leq P_g\leq P_g^{max},\qquad -F_l^{max}\leq f_l\leq F_l^{max}
$$

Referencia angular:

$$
\theta_{slack}=0
$$

### Actividad

Construya el OPF DC y reporte generación, ángulos, flujos y líneas congestionadas.

## Caso 2. Congestión

Reduzca el límite de `L13` de 60 MW a 40 MW. Compare costo, generación y flujos frente al caso base.

## Caso 3. Estructura de OPF AC

### Datos completos

**Barras**

| bus   |   pdem_mw |   qdem_mvar |   vmin_pu |   vmax_pu |
|:------|----------:|------------:|----------:|----------:|
| B1    |         0 |           0 |      0.95 |      1.05 |
| B2    |        80 |          30 |      0.95 |      1.05 |
| B3    |        60 |          25 |      0.95 |      1.05 |

**Generadores**

| gen   | bus   |   pmin_mw |   pmax_mw |   qmin_mvar |   qmax_mvar |   costo_usd_mwh |
|:------|:------|----------:|----------:|------------:|------------:|----------------:|
| G1    | B1    |         0 |       180 |         -80 |         120 |              20 |
| G2    | B3    |         0 |       100 |         -50 |          80 |              35 |

**Líneas**

| linea   | desde   | hasta   |   r_pu |   x_pu |   bsh_pu |   smax_mva |
|:--------|:--------|:--------|-------:|-------:|---------:|-----------:|
| L12     | B1      | B2      |  0.02  |   0.1  |    0.02  |        120 |
| L23     | B2      | B3      |  0.015 |   0.08 |    0.015 |        100 |
| L13     | B1      | B3      |  0.025 |   0.12 |    0.025 |         90 |

**Parámetros**

| parametro   | valor   | unidad   |
|:------------|:--------|:---------|
| slack       | B1      | -        |
| BaseMVA     | 100     | MVA      |

### Modelo matemático

Variables: $V_n$, $\theta_n$, $P_g$, $Q_g$, $P_{ij}$ y $Q_{ij}$.

Balances:

$$
\sum_{g:b(g)=n}P_g-P_n^D=\sum_{j\in\Omega_n}P_{nj}\qquad \forall n
$$

$$
\sum_{g:b(g)=n}Q_g-Q_n^D=\sum_{j\in\Omega_n}Q_{nj}\qquad \forall n
$$

Límites:

$$
V_n^{min}\leq V_n\leq V_n^{max}
$$

$$
P_g^{min}\leq P_g\leq P_g^{max},\qquad Q_g^{min}\leq Q_g\leq Q_g^{max}
$$

$$
P_{ij}^2+Q_{ij}^2\leq (S_{ij}^{max})^2
$$

### Actividad

Identifique qué ecuaciones convierten al OPF AC en un problema no lineal.
