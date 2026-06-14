# Actividad 06 — Expansión de generación

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Datos](../datos/) · [Guía AMPL](../../../docs/guia_ampl.md)

## Competencia

Formular e implementar un modelo de expansión de generación que combine inversión, operación por bloques, capacidad firme, reserva y energía no servida.

## Enunciado

Un sistema debe planificar nueva capacidad de generación para atender demanda futura. Existen tecnologías con diferente CAPEX, costo fijo, costo variable, disponibilidad y crédito firme. La demanda se representa mediante bloques de carga y años de planificación. Se debe decidir cuánta capacidad construir por tecnología minimizando costo total anualizado y penalización por energía no servida.

## Datos principales

Tecnologías (`gep_tecnologias.csv`):

| Tecnología | CAPEX [USD/kW] | FOM [USD/kW-año] | VOM [USD/MWh] | AF | Crédito firme | Existente [MW] | Máximo candidato [MW] |
|---|---:|---:|---:|---:|---:|---:|---:|
| gas | 900 | 20 | 55 | 0.85 | 0.90 | 200 | 500 |
| solar | 650 | 12 | 0 | 0.25 | 0.35 | 50 | 400 |
| eólica | 1200 | 25 | 0 | 0.38 | 0.25 | 30 | 300 |

Bloques (`gep_bloques.csv`):

| Bloque | Demanda [MW] | Duración [h] |
|---|---:|---:|
| base | 500 | 5260 |
| medio | 750 | 3000 |
| pico | 1000 | 500 |

Parámetros (`gep_parametros.csv`): ReserveMargin = 0.15, VOLL = 2000 USD/MWh, CRF = 0.10185.

## Parte A — GEP estático

Formule:

$$
\min Z=\sum_k CRF\,Capex_k\,Build_k + \sum_k FOM_k Cap_k + \sum_{k,b}VOM_k Gen_{k,b}+\sum_b VOLL\,ENS_b
$$

Capacidad:

$$
Cap_k=ExistingCap_k+Build_k
$$

Balance por bloque:

$$
\sum_k Gen_{k,b}+ENS_b=D_bh_b
$$

Límite de generación:

$$
Gen_{k,b}\leq AF_k Cap_k h_b
$$

Reserva firme:

$$
\sum_k FirmCredit_kCap_k\geq(1+RM)D^{peak}
$$

## Parte B — GEP multianual

Use `gep_anios.csv`. Extienda el modelo para años $y\in Y$:

$$
Cap_{k,y}=ExistingCap_k+\sum_{\tau\leq y}Build_{k,\tau}
$$

El costo de inversión debe registrarse en el año de construcción. La operación y la reserva se evalúan en cada año.

## Tareas

1. Construya el `.dat` con tecnologías, bloques, años y parámetros.
2. Implemente el GEP estático para el año base.
3. Reporte capacidad nueva, capacidad total, generación por bloque, ENS, reserva firme y costo.
4. Extienda el modelo a tres años: 2025, 2030 y 2035.
5. Evalúe sensibilidad con tres valores de margen de reserva: 10 %, 15 % y 20 %.
6. Evalúe sensibilidad aumentando el CAPEX solar en 25 %.
7. Evalúe sensibilidad reduciendo el crédito firme solar a 0.15.
8. Explique si el modelo instala capacidad por energía, por costo o por reserva firme.

## Validación

- El balance de energía debe cumplirse en todos los bloques.
- La generación máxima debe respetar capacidad, disponibilidad y horas.
- La capacidad nueva no debe superar el máximo candidato.
- La reserva firme debe cumplir la demanda pico más margen.
- La ENS debe ser cero si existe capacidad suficiente y VOLL es alto.
- En el modelo multianual, la capacidad construida en un año debe permanecer disponible en años posteriores.

## Entregables

| Entregable | Contenido |
|---|---|
| Formulación | GEP estático y extensión multianual. |
| Archivos | `.mod`, `.dat`, `.run` para caso estático y multianual. |
| Resultados | Capacidad, generación, costos, reserva y ENS. |
| Sensibilidad | Reserva, CAPEX solar y crédito firme. |
| Figura | Capacidad instalada por tecnología y año; generación por bloque. |
| Informe | Interpretación del plan de expansión y de las restricciones dominantes. |

## Evaluación

| Criterio | Peso |
|---|---:|
| Formulación de inversión, operación y reserva | 30 % |
| Construcción correcta del archivo de datos | 20 % |
| Implementación AMPL y resultados reproducibles | 20 % |
| Sensibilidad técnica | 15 % |
| Interpretación del plan de expansión | 15 % |
