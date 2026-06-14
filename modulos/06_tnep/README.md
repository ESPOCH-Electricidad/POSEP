[← Inicio](../../README.md) | [← Módulo anterior](../05_demanda/README.md) | [Siguiente módulo →](../07_gep/README.md)

# Módulo 06 — Expansión de transmisión

## Objetivo

Formular problemas de expansión de transmisión con red existente, corredores candidatos, límites de flujo, generación disponible, demanda y costos de inversión.

![Red existente y candidatos](figuras/01_red_existente_candidatos.svg)

## Caso 1. Modelo de transporte

### Datos completos

**Barras**

| bus   |   demanda_mw |   genmax_mw |
|:------|-------------:|------------:|
| B1    |            0 |         150 |
| B2    |           80 |           0 |
| B3    |          120 |           0 |
| B4    |           50 |         100 |

**Corredores**

| linea   | desde   | hasta   | tipo      |   x_pu |   fmax_mw |   costo_inv_musd |   max_nuevas |
|:--------|:--------|:--------|:----------|-------:|----------:|-----------------:|-------------:|
| L12     | B1      | B2      | existente |   0.1  |       100 |                0 |            0 |
| L23     | B2      | B3      | existente |   0.08 |        80 |                0 |            0 |
| L34     | B3      | B4      | existente |   0.11 |        70 |                0 |            0 |
| C13     | B1      | B3      | candidato |   0.12 |        90 |               40 |            1 |
| C24     | B2      | B4      | candidato |   0.1  |        80 |               35 |            1 |
| C14     | B1      | B4      | candidato |   0.15 |       100 |               55 |            1 |

**Parámetros**

| parametro   | valor   | unidad   |
|:------------|:--------|:---------|
| slack       | B1      | -        |
| VOLL        | 1000    | USD/MWh  |

### Modelo matemático

Conjuntos: $n\in N$, $l\in L$, $l\in L^C$.

Variables:

$$
f_l,\qquad y_l\in\{0,1\},\qquad P_n^G\geq 0,\qquad ENS_n\geq 0
$$

Función objetivo:

$$
\min Z=\sum_{l\in L^C}IC_ly_l+\sum_{n\in N}VOLL\cdot ENS_n
$$

Balance nodal:

$$
P_n^G+ENS_n-d_n=\sum_{l:from(l)=n}f_l-\sum_{l:to(l)=n}f_l\qquad \forall n
$$

Límites existentes:

$$
-F_l^{max}\leq f_l\leq F_l^{max}
$$

Límites candidatos:

$$
-F_l^{max}y_l\leq f_l\leq F_l^{max}y_l
$$

Generación:

$$
0\leq P_n^G\leq G_n^{max}
$$

### Actividad

Construya el modelo de transporte y determine qué corredores se construyen.

## Caso 2. DC-TNEP

Agregue ángulos $\theta_n$ y reactancias $x_l$.

Línea existente:

$$
f_l=\frac{\theta_i-\theta_j}{x_l}
$$

Corredor candidato:

$$
f_l-\frac{\theta_i-\theta_j}{x_l}\leq M(1-y_l)
$$

$$
f_l-\frac{\theta_i-\theta_j}{x_l}\geq -M(1-y_l)
$$

$$
\theta_{slack}=0
$$

### Actividad

Compare la solución del modelo de transporte y del DC-TNEP.

## Caso 3. Expansión multietapa

### Datos completos

|   anio |   factor_demanda |
|-------:|-----------------:|
|   2025 |             1    |
|   2030 |             1.15 |
|   2035 |             1.35 |

Variable:

$$
y_{l,y}\in\{0,1\}
$$

Restricción de permanencia:

$$
y_{l,y}\geq y_{l,y-1}\qquad \forall l,y
$$

### Actividad

Use los factores de demanda para resolver los años 2025, 2030 y 2035.
