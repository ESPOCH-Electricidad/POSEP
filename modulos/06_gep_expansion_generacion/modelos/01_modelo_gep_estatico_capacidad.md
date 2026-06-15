# Modelo 01 — GEP base por periodos

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Clasificación del modelo

Este modelo es un **GEP multietapa simplificado**. Tiene periodos de planificación, inversión por periodo y capacidad acumulada. Su objetivo es introducir la relación entre construcción de nueva capacidad, demanda futura y reserva firme.

| Aspecto | Descripción |
|---|---|
| Horizonte | 2025, 2030 y 2035 |
| Tipo temporal | Multietapa simplificado |
| Variable de inversión | `IC[g,t]` |
| Capacidad acumulada | `Cap[g,t]` |
| Operación | Despacho equivalente `P[g,t]` |
| ENS | `ENS[t]` |
| Archivo AMPL | `GEP_base_Garver.mod` |

El modelo se considera multietapa porque la inversión tiene índice temporal y la capacidad construida en un periodo permanece disponible en los periodos posteriores. Es simplificado porque no usa bloques horarios, lead time, descuento ni selección tecnológica binaria.

## 2. Enunciado

Determinar la capacidad nueva que debe incorporarse en 2025, 2030 y 2035 para cubrir la demanda pico de cada periodo, cumplir reserva firme, respetar límites de construcción, controlar emisiones y evitar ENS.

## 3. Conjuntos e índices

| Símbolo | Nombre AMPL | Descripción |
|---|---|---|
| G | `G` | Tecnologías o unidades existentes y candidatas. |
| T | `T ordered` | Periodos de planificación. |
| CAND | `CAND within G` | Subconjunto de tecnologías candidatas. |
| g | `g in G` | Índice de tecnología o unidad. |
| t | `t in T` | Índice de periodo. |
| tau | `tau in T` | Índice auxiliar para acumulación de capacidad. |

## 4. Parámetros

| Parámetro | Unidad | Descripción |
|---|---|---|
| `Pmax0[g]` | MW | Capacidad inicial de la tecnología g. |
| `Pmin[g]` | MW | Potencia mínima de despacho equivalente. |
| `Pdem[t]` | MW | Demanda pico del periodo t. |
| `IC_cost[g]` | MUSD/MW | Costo de inversión por MW construido. |
| `IC_min[g,t]` | MW | Construcción mínima permitida. |
| `IC_max[g,t]` | MW | Construcción máxima permitida. |
| `Cg[g]` | MUSD/MW | Costo operativo equivalente. |
| `firm[g]` | p.u. | Crédito firme de capacidad. |
| `ef[g]` | tCO2/MWh eq. | Factor de emisiones equivalente. |
| `Emi_max[t]` | tCO2 eq. | Límite agregado de emisiones. |
| `ENS_Cost` | MUSD/MW | Penalización por déficit. |
| `ENS_max[t]` | MW | ENS máxima admisible. |
| `reserve_margin` | p.u. | Margen de reserva de potencia. |

## 5. Variables

| Variable | Dominio | Descripción |
|---|---|---|
| `IC[g,t]` | entera >= 0 | Nueva capacidad instalada de g en t. |
| `Cap[g,t]` | continua >= 0 | Capacidad acumulada disponible. |
| `P[g,t]` | continua >= 0 | Generación o despacho equivalente. |
| `ENS[t]` | continua >= 0 | Demanda no atendida del periodo. |

## 6. Función objetivo

$$
\min Z=
\sum_{g\in G}\sum_{t\in T} IC\_cost_g IC_{g,t}
+\sum_{g\in G}\sum_{t\in T} Cg_g P_{g,t}
+\sum_{t\in T} ENS\_Cost\,ENS_t
$$

La función objetivo suma inversión, operación equivalente y penalización por ENS.

## 7. Restricciones

### Capacidad acumulada

$$
Cap_{g,t}=Pmax0_g+\sum_{\tau\in T: ord(\tau)\le ord(t)} IC_{g,\tau}
\qquad \forall g\in G,\ t\in T
$$

La capacidad disponible en cada periodo incluye capacidad inicial y todas las inversiones realizadas hasta ese periodo.

### Balance de demanda

$$
\sum_{g\in G}P_{g,t}+ENS_t=Pdem_t
\qquad \forall t\in T
$$

La demanda pico se atiende con generación o ENS.

### Límite de despacho

$$
P_{g,t}\le Cap_{g,t}
\qquad \forall g\in G,\ t\in T
$$

El despacho equivalente no puede superar la capacidad disponible.

### Mínimo de despacho

$$
P_{g,t}\ge Pmin_g
\qquad \forall g\in G,\ t\in T
$$

Representa mínimos técnicos o compromisos operativos simplificados.

### Límites de construcción

$$
IC\_min_{g,t}\le IC_{g,t}\le IC\_max_{g,t}
\qquad \forall g\in G,\ t\in T
$$

Controla el rango de nueva capacidad que puede entrar en cada periodo.

### Reserva firme

$$
\sum_{g\in G} firm_g Cap_{g,t}\ge (1+reserve\_margin)Pdem_t
\qquad \forall t\in T
$$

La capacidad firme debe cubrir la demanda pico más el margen de reserva.

### Emisiones

$$
\sum_{g\in G} ef_g P_{g,t}\le Emi\_max_t
\qquad \forall t\in T
$$

Limita emisiones agregadas por periodo.

### ENS máxima

$$
ENS_t\le ENS\_max_t
\qquad \forall t\in T
$$

Controla el déficit máximo admisible.

## 8. Plantilla `.dat` orientativa

```ampl
set T := 2025 2030 2035;
set G := G1_GAS_EXIST G3_HYD_EXIST G6_THERM_EXIST PV5_NEW WIND2_NEW CCGT6_NEW HYD3_NEW;
set CAND := PV5_NEW WIND2_NEW CCGT6_NEW HYD3_NEW;
```

La palabra `ordered` se declara en el `.mod`, no en el `.dat`.

## 9. Resultados esperados

Reportar `IC`, `Cap`, `P`, `ENS`, valor objetivo, cumplimiento de reserva, límite de emisiones y tecnologías que reciben inversión.

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
