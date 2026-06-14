# Modelo 01 — GEP estático de capacidad

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

El GEP estático decide capacidad nueva para un año objetivo usando demanda pico, reserva y operación representativa.

## 2. Enunciado

Determine cuánta capacidad instalar por tecnología para cubrir demanda, reserva y operación por bloques en un año objetivo.



## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| K | tecnologías |
| B | bloques de carga |
| Y | años, si aplica |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| Capex[k] | USD/kW | costo de inversión |
| FOM[k] | USD/kW-año | costo fijo |
| VOM[k] | USD/MWh | costo variable |
| AF[k] | p.u. | factor de disponibilidad |
| FirmCredit[k] | p.u. | crédito firme |
| ExistingCap[k] | MW | capacidad existente |
| CandidateMax[k] | MW | máximo construible |
| Demand[b] | MW | demanda por bloque |
| Hours[b] | h | duración del bloque |
| PeakDemand | MW | demanda máxima |
| ReserveMargin | p.u. | margen de reserva |

## 5. Datos completos para construir el archivo de datos

### Tecnologías

| tecnologia | capex_usd_kw | fom_usd_kw_anio | vom_usd_mwh | af | firm_credit | existingcap_mw | candidatemax_mw |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gas | 900 | 20 | 55 | 0.85 | 0.9 | 200 | 500 |
| solar | 650 | 12 | 0 | 0.25 | 0.35 | 50 | 400 |
| eolica | 1200 | 25 | 0 | 0.38 | 0.25 | 30 | 300 |

### Bloques de carga

| bloque | demand_mw | hours |
| --- | --- | --- |
| base | 500 | 5260 |
| medio | 750 | 3000 |
| pico | 1000 | 500 |

### Años

| anio | peak_mw | energy_gwh |
| --- | --- | --- |
| 2025 | 1000 | 6200 |
| 2030 | 1150 | 7100 |
| 2035 | 1350 | 8350 |

### Parámetros

| parametro | valor | unidad |
| --- | --- | --- |
| ReserveMargin | 0.15 | p.u. |
| VOLL | 2000 | USD/MWh |
| DiscountRate | 0.08 | p.u. |
| CRF | 0.10185 | p.u. |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| Build[k] | MW | capacidad nueva |
| Cap[k] | MW | capacidad total |
| Gen[k,b] | MWh | generación por tecnología y bloque |
| ENS[b] | MWh | energía no servida |

## 7. Función objetivo

$$
\min Z=\sum_k CRF\,Capex_k\,Build_k+\sum_kFOM_kCap_k+\sum_{k,b}VOM_kGen_{k,b}+\sum_bVOLL\,ENS_b
$$

**Explicación de la función objetivo.** Minimiza inversión anualizada, costo fijo, costo variable y penalización por energía no servida.

## 8. Restricciones del modelo

### Balance de energía por bloque

$$
\sum_{k\in K}Gen_{k,b}+ENS_b=Demand_b
$$

**Explicación.** La generación de tecnologías cubre la demanda del bloque o se penaliza ENS.

### Límite de generación

$$
Gen_{k,b}\leq AF_k Cap_k h_b
$$

**Explicación.** La energía producida depende de capacidad, disponibilidad y duración del bloque.

### Capacidad total

$$
Cap_k=ExistingCap_k+Build_k
$$

**Explicación.** La capacidad disponible suma parque existente y nueva inversión.

### Reserva firme

$$
\sum_k FirmCredit_kCap_k\geq (1+ReserveMargin)PeakDemand
$$

**Explicación.** La capacidad firme debe cubrir demanda pico más margen de reserva.

## 9. Plantilla `.dat` sugerida

```ampl
set K := gas solar eolica;
set B := base medio pico;

param Capex :=
gas 900
solar 650
eolica 1200
;

param FOM :=
gas 20
solar 12
eolica 25
;

param VOM :=
gas 55
solar 0
eolica 0
;

param AF :=
gas 0.85
solar 0.25
eolica 0.38
;

param FirmCredit :=
gas 0.90
solar 0.35
eolica 0.25
;

param ExistingCap :=
gas 200
solar 50
eolica 30
;

param CandidateMax :=
gas 500
solar 400
eolica 300
;

param Demand :=
base 500
medio 750
pico 1000
;

param Hours :=
base 5260
medio 3000
pico 500
;

param PeakDemand := 1000;
param ReserveMargin := 0.15;
param VOLL := 2000;
param CRF := 0.10185;
```

## 10. Resultados esperados

Reportar capacidad nueva, capacidad total, generación por tecnología, reserva firme y costo total.

## 11. Actividad asociada

[Actividad 06](../actividades/README.md)

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
