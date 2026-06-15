# Modelo 02 — GEP estático con bloques de carga

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Clasificación del modelo

Este modelo es **estático**. Decide una capacidad final para un año objetivo y evalúa su operación mediante bloques de carga. No contiene años de construcción ni acumulación temporal de inversiones.

| Aspecto | Descripción |
|---|---|
| Horizonte | Un año objetivo |
| Tipo temporal | Estático |
| Variable de inversión | `Build[i]` |
| Capacidad disponible | `Cap[i]` |
| Operación | `P[i,b]` por bloque |
| ENS | `ENS[b]` |
| Archivo AMPL | `gep_static_garver.mod` |

## 2. Enunciado

Determinar la nueva capacidad por tecnología y el despacho por bloque de carga para atender demanda, reserva y límites de capacidad al menor costo anual equivalente.

## 3. Conjuntos e índices

| Símbolo | Nombre AMPL | Descripción |
|---|---|---|
| G | `TECH` | Tecnologías existentes y candidatas. |
| B | `BLOCK` | Bloques de carga representativos. |
| g | `i in TECH` | Índice de tecnología. |
| b | `b in BLOCK` | Índice de bloque de carga. |

## 4. Parámetros

| Parámetro | Unidad | Descripción |
|---|---|---|
| `hours[b]` | h/año | Duración del bloque b. |
| `demand[b]` | MW | Demanda del bloque b. |
| `cap0[i]` | MW | Capacidad inicial de la tecnología i. |
| `capmax[i]` | MW | Capacidad máxima permitida. |
| `inv[i]` | MUSD/MW | Costo de inversión por MW. |
| `fom[i]` | MUSD/MW-año | Costo fijo anual de O&M. |
| `vom[i]` | USD/MWh | Costo variable de generación. |
| `af[i,b]` | p.u. | Factor de disponibilidad por bloque. |
| `firm[i]` | p.u. | Crédito firme de capacidad. |
| `reserve_margin` | p.u. | Margen de reserva. |
| `voll` | USD/MWh | Valor de energía no suministrada. |
| `peak_demand` | MW | Máxima demanda entre bloques. |

## 5. Variables

| Variable | Dominio | Descripción |
|---|---|---|
| `Build[i]` | continua >= 0 | Nueva capacidad instalada. |
| `Cap[i]` | continua >= 0 | Capacidad total disponible. |
| `P[i,b]` | continua >= 0 | Potencia generada en el bloque b. |
| `ENS[b]` | continua >= 0 | Demanda no atendida en el bloque b. |

`P[i,b]` está en MW. La energía se obtiene con `P[i,b]*hours[b]`.

## 6. Función objetivo

$$
\min Z =
\sum_{i\in TECH} inv_i Build_i
+\sum_{i\in TECH} fom_i Cap_i
+\sum_{i\in TECH}\sum_{b\in BLOCK}\frac{vom_i P_{i,b}hours_b}{10^6}
+\sum_{b\in BLOCK}\frac{voll\,ENS_b hours_b}{10^6}
$$

El modelo minimiza inversión, costo fijo, costo variable y ENS. Los costos variables y ENS se convierten de USD a MUSD dividiendo para $10^6$.

## 7. Restricciones

### Capacidad total

$$
Cap_i=cap0_i+Build_i
\qquad \forall i\in TECH
$$

### Balance de demanda por bloque

$$
\sum_{i\in TECH}P_{i,b}+ENS_b=demand_b
\qquad \forall b\in BLOCK
$$

### Límite de producción

$$
P_{i,b}\le af_{i,b}Cap_i
\qquad \forall i\in TECH,\ b\in BLOCK
$$

### Reserva firme

$$
\sum_{i\in TECH} firm_i Cap_i\ge (1+reserve\_margin)peak\_demand
$$

### Capacidad máxima

$$
Cap_i\le capmax_i
\qquad \forall i\in TECH
$$

## 8. Plantilla `.dat` orientativa

```ampl
set TECH := G1_GAS_EXIST G3_HYD_EXIST G6_THERM_EXIST PV5_NEW WIND2_NEW CCGT6_NEW HYD3_NEW;
set BLOCK := noche valle dia punta;
```

## 9. Resultados esperados

Reportar `Build`, `Cap`, `P`, `ENS`, costo total, componentes de costo y margen de reserva.

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
