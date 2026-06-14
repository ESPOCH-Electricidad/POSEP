[← Inicio](../../README.md) | [← Módulo anterior](../06_tnep/README.md)

# Módulo 07 — Expansión de generación

## Objetivo

Formular problemas de expansión de generación con tecnologías existentes y candidatas, bloques de carga, costos anualizados, disponibilidad y reserva firme.

![Curva de duración y bloques](figuras/02_curva_duracion_y_bloques.png)

## Costo anual equivalente

$$
CRF=\frac{r(1+r)^T}{(1+r)^T-1}
$$

## Caso 1. GEP estático

### Datos completos

**Tecnologías**

| tecnologia   |   capex_usd_kw |   fom_usd_kw_anio |   vom_usd_mwh |   factor_disponibilidad |   credito_firme |   cap_existente_mw |   cap_candidata_max_mw |
|:-------------|---------------:|------------------:|--------------:|------------------------:|----------------:|-------------------:|-----------------------:|
| gas          |            900 |                20 |            55 |                    0.85 |            0.9  |                200 |                    500 |
| solar        |            650 |                12 |             0 |                    0.25 |            0.35 |                 50 |                    400 |
| eolica       |           1200 |                25 |             0 |                    0.38 |            0.25 |                 30 |                    300 |

**Bloques de carga**

| bloque   |   demanda_mw |   horas |
|:---------|-------------:|--------:|
| base     |          500 |    5260 |
| medio    |          750 |    3000 |
| pico     |         1000 |     500 |

**Parámetros**

| parametro      |      valor | unidad   |
|:---------------|-----------:|:---------|
| margen_reserva |    0.15    | p.u.     |
| VOLL           | 2000       | USD/MWh  |
| tasa_descuento |    0.08    | p.u.     |
| CRF            |    0.10185 | p.u.     |

### Modelo matemático

Conjuntos: $g\in G$, $b\in B$.

Variables:

$$
K_g^{new}\geq 0,\qquad P_{gb}\geq 0,\qquad ENS_b\geq 0
$$

Función objetivo:

$$
\min Z=\sum_{g\in G}(CRF\cdot CAPEX_g\cdot1000+FOM_g\cdot1000)K_g^{new}
+\sum_{g\in G}\sum_{b\in B}VOM_gP_{gb}H_b
+\sum_{b\in B}VOLL\cdot ENS_bH_b
$$

Balance:

$$
\sum_{g\in G}P_{gb}+ENS_b=D_b\qquad \forall b
$$

Disponibilidad:

$$
P_{gb}\leq AF_g(K_g^0+K_g^{new})\qquad \forall g,b
$$

Límite de expansión:

$$
0\leq K_g^{new}\leq \bar{K}_g\qquad \forall g
$$

Reserva firme:

$$
\sum_{g\in G}FC_g(K_g^0+K_g^{new})\geq (1+RM)D^{peak}
$$

### Actividad

Construya el GEP estático y reporte capacidad nueva, generación por bloque y costo total.

## Caso 2. Expansión multianual

### Datos completos

|   anio |   pico_mw |   energia_gwh |
|-------:|----------:|--------------:|
|   2025 |      1000 |          6200 |
|   2030 |      1150 |          7100 |
|   2035 |      1350 |          8350 |

Variables:

$$
K_{g,y}^{new}\geq 0
$$

$$
K_{g,y}^{avail}=K_g^0+\sum_{\tau\leq y}K_{g,\tau}^{new}
$$

Restricción de acumulación:

$$
K_{g,y}^{avail}=K_{g,y-1}^{avail}+K_{g,y}^{new}\qquad \forall g,y
$$

### Actividad

Extienda el modelo a 2025, 2030 y 2035.

## Caso 3. Screening curve

![Screening curve](figuras/03_screening_curve.png)

Relación de costo por horas de operación:

$$
C_g(h)=F_g+c_gh
$$

### Actividad

Construya las rectas de costo para gas, solar y eólica. Explique por qué esta comparación no reemplaza al GEP con reserva, bloques y disponibilidad.
