[← Inicio](../../README.md) | [← Módulo anterior](../02_ampl/README.md) | [Siguiente módulo →](../04_opf/README.md)

# Módulo 03 — Despacho económico y operación de corto plazo

## Objetivo

Asignar generación al menor costo para una demanda dada, incorporando límites técnicos, tramos de costo, pérdidas, compromiso de unidades y operación hidrotérmica.

![Orden de mérito](figuras/02_orden_merito_con_demanda.png)

## Costo variable

Para una unidad térmica:

$$
c_g^{fuel}=HR_g p_g^{fuel}
$$

$$
c_g^{var}=c_g^{fuel}+c_g^{VOM}+EF_g p^{CO_2}
$$

## Caso 1. Despacho económico lineal

### Datos completos

**Generadores**

| gen   |   pmin_mw |   pmax_mw |   costo_usd_mwh |
|:------|----------:|----------:|----------------:|
| G1    |        20 |       100 |              15 |
| G2    |        30 |        80 |              22 |
| G3    |         0 |        60 |              35 |

**Demanda**

| parametro   |   valor | unidad   |
|:------------|--------:|:---------|
| demanda     |     150 | MW       |

### Modelo matemático

Conjunto: $g\in G$. Parámetros: $P_g^{min}$, $P_g^{max}$, $c_g$ y $D$.

Variable:

$$
P_g\geq 0
$$

Función objetivo:

$$
\min Z=\sum_{g\in G}c_gP_g
$$

Restricciones:

$$
\sum_{g\in G}P_g=D
$$

$$
P_g^{min}\leq P_g\leq P_g^{max}\qquad \forall g\in G
$$

### Actividad

Construya el modelo y determine costo total, unidad marginal y orden de mérito.

## Caso 2. Despacho por tramos

### Datos completos

**Bloques de generación**

| gen   | tramo   |   pmax_tramo_mw |   costo_tramo_usd_mwh |
|:------|:--------|----------------:|----------------------:|
| G1    | K1      |              60 |                    14 |
| G1    | K2      |              50 |                    21 |
| G2    | K1      |              70 |                    18 |
| G2    | K2      |              60 |                    28 |

**Demanda**

| parametro   |   valor | unidad   |
|:------------|--------:|:---------|
| demanda     |     170 | MW       |

### Modelo matemático

Conjuntos: $g\in G$, $k\in K_g$.

Variable:

$$
p_{gk}\geq 0
$$

Función objetivo:

$$
\min Z=\sum_{g\in G}\sum_{k\in K_g}c_{gk}p_{gk}
$$

Restricciones:

$$
\sum_{g\in G}\sum_{k\in K_g}p_{gk}=D
$$

$$
0\leq p_{gk}\leq \bar{P}_{gk}\qquad \forall g,k
$$

### Actividad

Construya el `.dat` con índice doble `(g,k)`.

## Caso 3. Despacho con pérdidas

### Datos completos

**Generadores**

| gen   |   pmin_mw |   pmax_mw |   costo_usd_mwh |
|:------|----------:|----------:|----------------:|
| G1    |        20 |       120 |              16 |
| G2    |        20 |       100 |              20 |
| G3    |        10 |        80 |              30 |

**Demanda**

| parametro   |   valor | unidad   |
|:------------|--------:|:---------|
| demanda     |     180 | MW       |

**Coeficientes B**

| g   | h   |   B_1_mw |
|:----|:----|---------:|
| G1  | G1  |  8e-05   |
| G1  | G2  |  2e-05   |
| G1  | G3  |  1e-05   |
| G2  | G1  |  2e-05   |
| G2  | G2  |  0.0001  |
| G2  | G3  |  3e-05   |
| G3  | G1  |  1e-05   |
| G3  | G2  |  3e-05   |
| G3  | G3  |  0.00012 |

### Modelo matemático

$$
P^{loss}=\sum_{g\in G}\sum_{h\in G}P_gB_{gh}P_h
$$

$$
\min Z=\sum_{g\in G}c_gP_g
$$

$$
\sum_{g\in G}P_g=D+P^{loss}
$$

$$
P_g^{min}\leq P_g\leq P_g^{max}\qquad \forall g\in G
$$

### Actividad

Implemente el problema como QP/NLP y compare la generación total con el despacho sin pérdidas.

## Caso 4. Unit commitment

### Datos completos

**Unidades**

| gen   |   pmin_mw |   pmax_mw |   costo_usd_mwh |   arranque_usd |   rampa_subida_mw_h |   rampa_bajada_mw_h |   estado_inicial |
|:------|----------:|----------:|----------------:|---------------:|--------------------:|--------------------:|-----------------:|
| G1    |        30 |       120 |              18 |            500 |                  50 |                  50 |                1 |
| G2    |        20 |        90 |              24 |            350 |                  40 |                  40 |                0 |
| G3    |        10 |        60 |              38 |            120 |                  30 |                  30 |                0 |

**Demanda y reserva**

|   hora |   demanda_mw |   reserva_mw |
|-------:|-------------:|-------------:|
|      1 |          110 |           15 |
|      2 |          130 |           15 |
|      3 |          160 |           20 |
|      4 |          180 |           20 |
|      5 |          150 |           15 |
|      6 |          120 |           15 |

### Modelo matemático

Conjuntos: $g\in G$, $t\in T$.

Variables:

$$
P_{gt}\geq 0,\qquad u_{gt}\in\{0,1\},\qquad v_{gt}\in\{0,1\}
$$

Función objetivo:

$$
\min Z=\sum_{t\in T}\sum_{g\in G}c_gP_{gt}+\sum_{t\in T}\sum_{g\in G}SU_gv_{gt}
$$

Balance:

$$
\sum_{g\in G}P_{gt}=D_t\qquad \forall t
$$

Límites:

$$
P_g^{min}u_{gt}\leq P_{gt}\leq P_g^{max}u_{gt}\qquad \forall g,t
$$

Reserva:

$$
\sum_{g\in G}P_g^{max}u_{gt}\geq D_t+R_t\qquad \forall t
$$

Arranque:

$$
v_{gt}\geq u_{gt}-u_{g,t-1}\qquad \forall g,t
$$

Rampas:

$$
P_{gt}-P_{g,t-1}\leq RU_g,\qquad P_{g,t-1}-P_{gt}\leq RD_g
$$

### Actividad

Construya el MILP y reporte estado de unidades, generación, arranques y costo.

## Caso 5. Despacho hidrotérmico

### Datos completos

**Central hidroeléctrica**

| hidro   |   v0_hm3 |   vmin_hm3 |   vmax_hm3 |   qmax_hm3 |   produccion_mwh_hm3 |
|:--------|---------:|-----------:|-----------:|-----------:|---------------------:|
| H1      |       80 |         20 |        120 |         35 |                    2 |

**Unidades térmicas**

| gen   |   pmax_mw |   costo_usd_mwh |
|:------|----------:|----------------:|
| T1    |       100 |              35 |
| T2    |        80 |              55 |

**Demanda y afluencia**

|   periodo |   demanda_mw |   afluencia_hm3 |
|----------:|-------------:|----------------:|
|         1 |          130 |              20 |
|         2 |          170 |              15 |
|         3 |          150 |              10 |
|         4 |          120 |              25 |

**Penalización**

| parametro   |   valor | unidad   |
|:------------|--------:|:---------|
| VOLL        |    1000 | USD/MWh  |

### Modelo matemático

Variables: $V_t$, $Q_t$, $P^H_t$, $P^T_{gt}$ y $ENS_t$.

Función objetivo:

$$
\min Z=\sum_{t\in T}\sum_{g\in G^T}c_gP^T_{gt}+\sum_{t\in T}VOLL\cdot ENS_t
$$

Balance eléctrico:

$$
P^H_t+\sum_{g\in G^T}P^T_{gt}+ENS_t=D_t\qquad \forall t
$$

Producción hidroeléctrica:

$$
P^H_t=\rho Q_t\qquad \forall t
$$

Balance del embalse:

$$
V_t=V_{t-1}+I_t-Q_t-Sp_t\qquad \forall t
$$

Límites:

$$
V^{min}\leq V_t\leq V^{max},\qquad 0\leq Q_t\leq Q^{max}
$$

### Actividad

Construya el modelo y explique el costo de oportunidad del agua.

## Extensión. Dos embalses en cascada

**Embalses**

| embalse   |   v0_hm3 |   vmin_hm3 |   vmax_hm3 |   qmax_hm3 |   produccion_mwh_hm3 |
|:----------|---------:|-----------:|-----------:|-----------:|---------------------:|
| R1        |       70 |         20 |        110 |         30 |                  2.2 |
| R2        |       60 |         15 |        100 |         35 |                  1.8 |

**Afluencias**

| embalse   |   t1 |   t2 |   t3 |   t4 |
|:----------|-----:|-----:|-----:|-----:|
| R1        |   15 |   10 |   12 |   18 |
| R2        |    8 |    7 |    9 |   10 |

**Relación hidráulica**

| embalse   | aguas_arriba   |
|:----------|:---------------|
| R1        |                |
| R2        | R1             |

Agregue al embalse aguas abajo los caudales turbinados y vertidos del embalse aguas arriba.
