[← Inicio](../../README.md) | [← Módulo anterior](../06_tnep/README.md)

# Módulo 07 — Expansión de generación

## Propósito

El módulo estudia decisiones de inversión en capacidad de generación. La formulación combina demanda futura, bloques de carga, costos anualizados, disponibilidad y requerimientos de reserva.

## Competencia

Formular modelos de expansión de generación, calcular costos anualizados e interpretar planes de inversión bajo criterios de costo, energía y capacidad firme.

![Curva de duración y bloques](figuras/02_curva_duracion_y_bloques.png)

## Costo anual equivalente

Para comparar tecnologías de inversión se usa el factor de recuperación de capital:

$$
CRF=\frac{r(1+r)^T}{(1+r)^T-1}
$$

El costo fijo anualizado de una tecnología puede aproximarse como:

$$
C_i^{fix}=CRF\cdot CAPEX_i+FOM_i
$$

## Caso 1. GEP estático con bloques de carga

### Enunciado

Un sistema debe decidir nueva capacidad de generación para atender bloques de carga anuales y cumplir un margen de reserva. Cada tecnología tiene CAPEX, O&M fijo, costo variable, disponibilidad y crédito firme.

### Datos del caso

**Tecnologías**

| tecnologia   |   capex_usd_kw |   fom_usd_kw_anio |   vom_usd_mwh |   factor_disponibilidad |   credito_firme |   cap_existente_mw |   cap_candidata_max_mw |
|:-------------|---------------:|------------------:|--------------:|------------------------:|----------------:|-------------------:|-----------------------:|
| gas          |            900 |                20 |            55 |                    0.85 |            0.9  |                200 |                    500 |
| solar        |            650 |                12 |             0 |                    0.25 |            0.35 |                 50 |                    400 |
| eolica       |           1200 |                25 |             0 |                    0.38 |            0.25 |                 30 |                    300 |

**Bloques de carga**

| bloque   |   demanda [MW] |   horas |
|:---------|---------------:|--------:|
| base     |            500 |    5260 |
| medio    |            750 |    3000 |
| pico     |           1000 |     500 |

**Parámetros generales**

| parametro      |      valor | unidad   |
|:---------------|-----------:|:---------|
| margen_reserva |    0.15    | p.u.     |
| VOLL           | 2000       | USD/MWh  |
| tasa_descuento |    0.08    | p.u.     |
| CRF            |    0.10185 | p.u.     |

### Formulación matemática

**Conjuntos e índices:** $i\in I$, $b\in B$.

**Parámetros:** $K_i^0$, $K_i^{max}$, $CAPEX_i$, $FOM_i$, $VOM_i$, $AF_i$, $FC_i$, $D_b$, $h_b$, $RM$ y $CRF$.

**Variables:** nueva capacidad $x_i\geq0$ y generación $p_{ib}\geq0$.

**Función objetivo**

$$
\min Z=\sum_{i\in I}(CRF\cdot CAPEX_i+FOM_i)x_i+\sum_{b\in B}\sum_{i\in I}VOM_i p_{ib}h_b
$$

**Restricciones**

Balance por bloque:

$$
\sum_{i\in I}p_{ib}=D_b\qquad \forall b\in B
$$

Límite de generación por disponibilidad:

$$
p_{ib}\leq AF_i(K_i^0+x_i)\qquad \forall i,b
$$

Límite de inversión:

$$
0\leq x_i\leq K_i^{max}\qquad \forall i
$$

Reserva firme:

$$
\sum_{i\in I}FC_i(K_i^0+x_i)\geq (1+RM)D^{peak}
$$

### Actividad

Construya el GEP estático. Reporte capacidad nueva por tecnología, generación por bloque, costo anual y margen de reserva. Explique si la decisión está dominada por CAPEX, costo variable, disponibilidad o crédito firme.

## Caso 2. Expansión multianual

### Enunciado

La demanda crece entre 2025 y 2035. La capacidad construida permanece disponible en años posteriores. Se debe determinar cuándo invertir y en qué tecnología.

### Datos del caso

**Años de planificación**

|   anio |   pico_mw |   energia_gwh |
|-------:|----------:|--------------:|
|   2025 |      1000 |          6200 |
|   2030 |      1150 |          7100 |
|   2035 |      1350 |          8350 |

### Formulación matemática

**Conjuntos e índices:** $i\in I$, $b\in B$, $y\in Y$.

**Variable de inversión anual:** $x_{iy}\geq0$.

**Capacidad acumulada:**

$$
K_{iy}=K_i^0+\sum_{\tau\in Y:\tau\leq y}x_{i\tau}
$$

**Balance por bloque y año:**

$$
\sum_{i\in I}p_{iby}=D_{by}\qquad \forall b,y
$$

**Disponibilidad:**

$$
p_{iby}\leq AF_i K_{iy}\qquad \forall i,b,y
$$

**Reserva:**

$$
\sum_{i\in I}FC_iK_{iy}\geq (1+RM)D_y^{peak}\qquad \forall y
$$

### Actividad

Formule el GEP multianual. Entregue una tabla de capacidad instalada por tecnología y año, inversiones anuales y costo total. Discuta si la expansión se adelanta por reserva o por crecimiento de energía.

## Caso 3. Screening curve

### Enunciado

Antes de resolver el GEP, se puede comparar tecnologías mediante curvas de costo anual en función de horas de operación. Esta herramienta no reemplaza el modelo, pero ayuda a interpretar los resultados.

### Formulación de trabajo

Costo anual por kW:

$$
C_i(h)=C_i^{fix}+VOM_i\cdot h
$$

donde $h$ representa horas equivalentes de operación al año.

### Actividad

Calcule y grafique $C_i(h)$ para cada tecnología. Determine en qué rango de horas conviene cada alternativa y compare esa lectura con el resultado del GEP. Explique por qué una tecnología barata en energía puede no ser suficiente para cubrir reserva.

## Evaluación

| Criterio | Ponderación |
|---|---:|
| Anualización de costos y unidades | 20 % |
| Balance por bloques y disponibilidad | 25 % |
| Reserva firme e inversión acumulada | 25 % |
| Interpretación del plan de expansión | 20 % |
| Tablas y gráficos de resultados | 10 % |


## Archivos de datos

| Archivo | Uso |
|---|---|
| `gep_anios.csv` | Tabla editable del caso |
| `gep_bloques.csv` | Tabla editable del caso |
| `gep_parametros.csv` | Tabla editable del caso |
| `gep_tecnologias.csv` | Tabla editable del caso |
