# Modelo 03 — GEP multianual

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

El GEP multianual decide cuándo construir capacidad considerando crecimiento de demanda futura.

## 2. Enunciado

Para 2025, 2030 y 2035, determine capacidad nueva por tecnología y año, minimizando costo presente.



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
\min Z=\sum_{y\in Y}\alpha_y(C_y^{inv}+C_y^{fix}+C_y^{var}+C_y^{ENS})
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

### Acumulación de capacidad

$$
Cap_{k,y}=Cap_{k,y-1}+Build_{k,y}
$$

**Explicación.** La capacidad construida en un año permanece disponible en años posteriores.

### Demanda anual

$$
PeakDemand_y,\ Demand_{y,b}
$$

**Explicación.** La demanda proviene del módulo de proyección de demanda.

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

Reportar cronograma de expansión, capacidad acumulada, costo presente y margen de reserva.

## 11. Actividad asociada

[Actividad 06](../actividades/README.md)


## 12. Validación mínima

- Verifique que todas las unidades sean consistentes.
- Compruebe que todos los conjuntos usados en la formulación tengan datos.
- Revise que el balance principal cierre.
- Identifique restricciones activas.
- Compare el resultado contra una estimación manual simple.

## 13. Preguntas de análisis

1. ¿Qué restricción limita principalmente la solución?
2. ¿Qué parámetro tendría mayor impacto si cambia?
3. ¿El resultado es técnicamente razonable?
4. ¿Qué dato adicional se necesitaría para aplicar el modelo a un sistema real?

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
