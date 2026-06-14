# Modelo 04 — Compromiso de unidades térmicas

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

El compromiso de unidades decide qué generadores encender y cuánto generar en cada hora. Es un problema MILP porque combina variables continuas de generación y binarias de estado.

## 2. Enunciado

Para tres unidades térmicas y seis horas de demanda, determine el encendido, arranque y despacho que minimiza costo de operación y arranque, manteniendo reserva y rampas.



## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| G | unidades térmicas |
| T | horas |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| Demand[t] | MW | demanda horaria |
| Reserve[t] | MW | reserva requerida |
| Pmin[g] | MW | mínimo técnico |
| Pmax[g] | MW | máximo técnico |
| Cost[g] | USD/MWh | costo variable |
| Startup[g] | USD | costo de arranque |
| RU[g] | MW/h | rampa de subida |
| RD[g] | MW/h | rampa de bajada |
| InitialStatus[g] | 0/1 | estado inicial |

## 5. Datos completos para construir el archivo de datos

### Unidades

| gen | pmin_mw | pmax_mw | cost_usd_mwh | startup_usd | ru_mw_h | rd_mw_h | initial_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G1 | 30 | 120 | 18 | 500 | 50 | 50 | 1 |
| G2 | 20 | 90 | 24 | 350 | 40 | 40 | 0 |
| G3 | 10 | 60 | 38 | 120 | 30 | 30 | 0 |

### Demanda y reserva

| hora | demand_mw | reserve_mw |
| --- | --- | --- |
| 1 | 110 | 15 |
| 2 | 130 | 15 |
| 3 | 160 | 20 |
| 4 | 180 | 20 |
| 5 | 150 | 15 |
| 6 | 120 | 15 |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| P[g,t] | MW, continua | generación de unidad g en hora t |
| u[g,t] | binaria | 1 si la unidad g está encendida en t |
| v[g,t] | binaria | 1 si la unidad g arranca en t |

## 7. Función objetivo

$$
\min Z=\sum_{t\in T}\sum_{g\in G}Cost_gP_{g,t}+\sum_{t\in T}\sum_{g\in G}Startup_gv_{g,t}
$$

**Explicación de la función objetivo.** Minimiza el costo de producción y el costo de arranque. El modelo penaliza encendidos innecesarios y generación costosa.

## 8. Restricciones del modelo

### Balance horario

$$
\sum_{g\in G}P_{g,t}=Demand_t\quad \forall t
$$

**Explicación.** En cada hora, la generación total cubre la demanda.

### Reserva

$$
\sum_{g\in G}Pmax_g u_{g,t}\geq Demand_t+Reserve_t\quad \forall t
$$

**Explicación.** La capacidad en línea debe cubrir demanda más reserva.

### Límites condicionados al estado

$$
Pmin_g u_{g,t}\leq P_{g,t}\leq Pmax_g u_{g,t}\quad \forall g,t
$$

**Explicación.** Una unidad apagada no genera; una encendida respeta mínimo y máximo.

### Arranque

$$
v_{g,t}\geq u_{g,t}-u_{g,t-1}\quad \forall g,t
$$

**Explicación.** Detecta transición de apagado a encendido.

### Rampa

$$
P_{g,t}-P_{g,t-1}\leq RU_g,\quad P_{g,t-1}-P_{g,t}\leq RD_g
$$

**Explicación.** Limita cambios de generación entre horas consecutivas.

## 9. Plantilla `.dat` sugerida

```ampl
set G := G1 G2 G3;
set T := 1 2 3 4 5 6;

param Demand :=
1 110
2 130
3 160
4 180
5 150
6 120
;

param Reserve :=
1 15
2 15
3 20
4 20
5 15
6 15
;

param Pmin :=
G1 30
G2 20
G3 10
;

param Pmax :=
G1 120
G2 90
G3 60
;

param Cost :=
G1 18
G2 24
G3 38
;

param Startup :=
G1 500
G2 350
G3 120
;

param RU :=
G1 50
G2 40
G3 30
;

param RD :=
G1 50
G2 40
G3 30
;

param InitialStatus :=
G1 1
G2 0
G3 0
;
```

## 10. Resultados esperados

Reportar cronograma de encendido, arranques, despacho horario, reserva disponible y costo total.

## 11. Actividad asociada

[Actividad 02](../actividades/README.md)

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
