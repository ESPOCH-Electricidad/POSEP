# Modelo 03 — GEP multianual con selección tecnológica

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Clasificación del modelo

Este modelo es un **GEP multietapa completo**. Decide qué tecnologías se habilitan, en qué año se construyen, cuánta capacidad se instala y cómo opera el sistema por año y bloque de carga.

| Aspecto | Descripción |
|---|---|
| Horizonte | Varios años ordenados |
| Tipo temporal | Multietapa / multianual |
| Variable de selección | `Select[c]` |
| Variable binaria anual | `BuildOn[c,y]` |
| Variable de inversión | `Build[c,y]` |
| Capacidad acumulada | `Cap[i,y]` con lead time |
| Operación | `P[i,y,b]` |
| Archivo AMPL | `gep_multiyear_garver.mod` |

## 2. Enunciado

Determinar selección tecnológica, cronograma de construcción, capacidad instalada disponible, despacho por bloques, ENS, emisiones y cumplimiento de metas renovables durante varios años, minimizando el costo presente del plan.

## 3. Conjuntos e índices

| Símbolo | Nombre AMPL | Descripción |
|---|---|---|
| Y | `YEAR ordered` | Años del horizonte. |
| B | `BLOCK` | Bloques de carga. |
| G | `TECH` | Tecnologías existentes y candidatas. |
| Gcand | `CAND within TECH` | Tecnologías candidatas. |
| Gren | `REN within TECH` | Tecnologías renovables. |
| Gtherm | `THERM within TECH` | Tecnologías térmicas. |
| Ghyd | `HYDRO within TECH` | Tecnologías hidroeléctricas. |
| Gvre | `VAR_REN within TECH` | Renovables variables. |
| g | `i in TECH`, `c in CAND` | Índice de tecnología. |
| y | `y in YEAR` | Índice de año. |
| b | `b in BLOCK` | Índice de bloque. |
| tau | `tau in YEAR` | Año auxiliar para acumulación de capacidad. |

## 4. Parámetros

### Demanda y economía

| Parámetro | Unidad | Descripción |
|---|---|---|
| `hours[b]` | h/año | Duración del bloque. |
| `demand[y,b]` | MW | Demanda por año y bloque. |
| `annual_demand[y]` | MWh | Demanda anual, calculada como sumatoria por bloques. |
| `peak[y]` | MW | Demanda máxima anual. |
| `discount` | p.u. | Tasa de descuento. |
| `df[y]` | p.u. | Factor de descuento. |
| `voll` | USD/MWh | Penalización de ENS. |

### Capacidad, operación y política

| Parámetro | Unidad | Descripción |
|---|---|---|
| `cap0[i]` | MW | Capacidad inicial. |
| `retire[i,y]` | MW | Retiro acumulado. |
| `capmax[i]` | MW | Capacidad máxima total. |
| `af[i,b]` | p.u. | Disponibilidad por bloque. |
| `firm[i]` | p.u. | Crédito firme. |
| `ef[i]` | tCO2/MWh | Factor de emisión. |
| `hydro_cf[y]` | p.u. | Disponibilidad hidroenergética anual. |
| `fuelmax[th,y]` | MWh/año | Límite anual de energía térmica. |
| `ren_min[y]` | p.u. | Participación renovable mínima. |
| `emcap[y]` | tCO2/año | Límite anual de emisiones. |
| `budget[y]` | MUSD/año | Presupuesto anual de inversión. |

### Inversión

| Parámetro | Unidad | Descripción |
|---|---|---|
| `invfix[c]` | MUSD | Costo fijo por seleccionar tecnología. |
| `capex[c]` | MUSD/MW | Costo de inversión por MW. |
| `pot[c]` | MW | Potencial máximo acumulado. |
| `buildmin[c]` | MW/año | Construcción mínima si se activa. |
| `buildmax[c]` | MW/año | Construcción máxima anual. |
| `lead[c]` | periodos | Tiempo de construcción. |

## 5. Variables

| Variable | Dominio | Descripción |
|---|---|---|
| `Select[c]` | binaria | 1 si la candidata c se habilita en el plan. |
| `BuildOn[c,y]` | binaria | 1 si se activa construcción de c en y. |
| `Build[c,y]` | continua >= 0 | Capacidad nueva construida. |
| `Cap[i,y]` | continua >= 0 | Capacidad disponible acumulada. |
| `P[i,y,b]` | continua >= 0 | Potencia generada por año y bloque. |
| `ENS[y,b]` | continua >= 0 | Déficit por año y bloque. |
| `Curt[v,y,b]` | continua >= 0 | Vertimiento de renovables variables. |
| `Emis[y]` | continua >= 0 | Emisiones anuales. |

## 6. Función objetivo

$$
\min Z = \sum_{c\in CAND} invfix_c Select_c
+\sum_{y\in YEAR}df_y\left(
\sum_{c\in CAND}capex_cBuild_{c,y}
+\sum_{i\in TECH}fom_iCap_{i,y}
+\sum_{i\in TECH}\sum_{b\in BLOCK}\frac{vom_iP_{i,y,b}hours_b}{10^6}
+\sum_{b\in BLOCK}\frac{voll\,ENS_{y,b}hours_b}{10^6}
\right)
$$

Incluye selección, inversión, O&M fijo, operación y ENS, todo expresado en valor presente.

## 7. Restricciones

### Capacidad de candidatas

$$
Cap_{i,y}=cap0_i-retire_{i,y}+\sum_{\tau\in YEAR: ord(\tau)+lead_i\le ord(y)}Build_{i,\tau}
\qquad \forall i\in CAND,\ y\in YEAR
$$

### Capacidad de existentes

$$
Cap_{i,y}=cap0_i-retire_{i,y}
\qquad \forall i\in TECH\setminus CAND,\ y\in YEAR
$$

### Enlaces de construcción

$$
Build_{c,y}\le buildmax_cBuildOn_{c,y}
\qquad \forall c\in CAND,\ y\in YEAR
$$

$$
Build_{c,y}\ge buildmin_cBuildOn_{c,y}
\qquad \forall c\in CAND,\ y\in YEAR
$$

$$
BuildOn_{c,y}\le Select_c
\qquad \forall c\in CAND,\ y\in YEAR
$$

### Potencial máximo acumulado

$$
\sum_{y\in YEAR}Build_{c,y}\le pot_cSelect_c
\qquad \forall c\in CAND
$$

### Capacidad máxima

$$
Cap_{i,y}\le capmax_i
\qquad \forall i\in TECH,\ y\in YEAR
$$

### Balance de demanda

$$
\sum_{i\in TECH}P_{i,y,b}+ENS_{y,b}=demand_{y,b}
\qquad \forall y\in YEAR,\ b\in BLOCK
$$

### Límite de producción

$$
P_{i,y,b}\le af_{i,b}Cap_{i,y}
\qquad \forall i\in TECH,\ y\in YEAR,\ b\in BLOCK
$$

### Vertimiento renovable variable

$$
P_{v,y,b}+Curt_{v,y,b}=af_{v,b}Cap_{v,y}
\qquad \forall v\in VAR\_REN,\ y\in YEAR,\ b\in BLOCK
$$

### Energía hidroeléctrica anual

$$
\sum_{b\in BLOCK}P_{h,y,b}hours_b\le hydro\_cf_yCap_{h,y}8760
\qquad \forall h\in HYDRO,\ y\in YEAR
$$

### Límite térmico anual

$$
\sum_{b\in BLOCK}P_{th,y,b}hours_b\le fuelmax_{th,y}
\qquad \forall th\in THERM,\ y\in YEAR
$$

### Reserva de potencia

$$
\sum_{i\in TECH}firm_iCap_{i,y}\ge (1+reserve\_margin)peak_y
\qquad \forall y\in YEAR
$$

### Suficiencia energética anual

$$
\sum_{i\in TECH}\sum_{b\in BLOCK}af_{i,b}Cap_{i,y}hours_b
\ge (1+energy\_margin)annual\_demand_y
\qquad \forall y\in YEAR
$$

### Participación renovable mínima

$$
\sum_{r\in REN}\sum_{b\in BLOCK}P_{r,y,b}hours_b
\ge ren\_min_y annual\_demand_y
\qquad \forall y\in YEAR
$$

### Cálculo de emisiones

$$
Emis_y=\sum_{i\in TECH}\sum_{b\in BLOCK}ef_iP_{i,y,b}hours_b
\qquad \forall y\in YEAR
$$

### Límite anual de emisiones

$$
Emis_y\le emcap_y
\qquad \forall y\in YEAR
$$

### Límite anual de ENS

$$
\sum_{b\in BLOCK}ENS_{y,b}hours_b\le ens\_max\_share\ annual\_demand_y
\qquad \forall y\in YEAR
$$

### Presupuesto anual

$$
\sum_{c\in CAND}capex_cBuild_{c,y}\le budget_y
\qquad \forall y\in YEAR
$$

## 8. Resultados esperados

Reportar valor objetivo, `Select`, `BuildOn`, `Build`, `Cap`, `P`, `ENS`, `Curt`, `Emis`, cumplimiento renovable, cumplimiento de reserva, uso de presupuesto y efectos de los lead times.

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
