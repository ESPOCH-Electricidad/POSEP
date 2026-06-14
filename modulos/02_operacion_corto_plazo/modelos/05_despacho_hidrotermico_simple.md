# Modelo 05 — Despacho hidrotérmico simple

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

El despacho hidrotérmico coordina generación térmica y generación hidroeléctrica. El agua es un recurso limitado que debe distribuirse en el tiempo.

## 2. Enunciado

Para dos térmicas y una central hidroeléctrica con embalse durante cuatro periodos, determine la generación que minimiza costo térmico y penalización por energía no servida.



## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| G | generadores térmicos |
| H | centrales hidroeléctricas |
| T | periodos |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| Demand[t] | MW | demanda por periodo |
| Cost[g] | USD/MWh | costo térmico |
| Pmax[g] | MW | máximo térmico |
| V0[h] | hm3 | volumen inicial |
| Vmin[h] | hm3 | volumen mínimo |
| Vmax[h] | hm3 | volumen máximo |
| Inflow[h,t] | hm3 | afluencia |
| Qmax[h] | hm3 | turbinamiento máximo |
| Prod[h] | MW/hm3 | coeficiente de producción |
| VOLL | USD/MWh | penalización ENS |

## 5. Datos completos para construir el archivo de datos

### Térmicas

| gen | pmax_mw | cost_usd_mwh |
| --- | --- | --- |
| T1 | 100 | 35 |
| T2 | 80 | 55 |

### Hidro

| hidro | v0_hm3 | vmin_hm3 | vmax_hm3 | qmax_hm3 | prod_mw_hm3 |
| --- | --- | --- | --- | --- | --- |
| H1 | 80 | 20 | 120 | 35 | 2.0 |

### Demanda y afluencia

| periodo | demand_mw | inflow_hm3 |
| --- | --- | --- |
| 1 | 130 | 20 |
| 2 | 170 | 15 |
| 3 | 150 | 10 |
| 4 | 120 | 25 |

### Penalización

| parametro | valor | unidad |
| --- | --- | --- |
| VOLL | 1000 | USD/MWh |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| Pg[g,t] | MW | generación térmica |
| Q[h,t] | hm3 | turbinamiento |
| V[h,t] | hm3 | volumen de embalse |
| Ph[h,t] | MW | generación hidro |
| ENS[t] | MW | energía no servida |

## 7. Función objetivo

$$
\min Z=\sum_{t\in T}\sum_{g\in G}Cost_gPg_{g,t}+\sum_{t\in T}VOLL\,ENS_t
$$

**Explicación de la función objetivo.** Minimiza costo térmico y penaliza demanda no atendida. La hidro no tiene costo variable explícito, pero está limitada por agua.

## 8. Restricciones del modelo

### Balance eléctrico

$$
\sum_gPg_{g,t}+\sum_hPh_{h,t}+ENS_t=Demand_t\quad \forall t
$$

**Explicación.** La demanda se cubre con generación térmica, hidro o ENS.

### Producción hidro

$$
Ph_{h,t}=Prod_hQ_{h,t}\quad \forall h,t
$$

**Explicación.** Convierte turbinamiento en potencia hidroeléctrica.

### Balance de embalse

$$
V_{h,t}=V_{h,t-1}+Inflow_{h,t}-Q_{h,t}\quad \forall h,t
$$

**Explicación.** El volumen actual depende del volumen previo, afluencia y turbinamiento.

### Límites térmicos e hidráulicos

$$
0\leq Pg_{g,t}\leq Pmax_g,\quad 0\leq Q_{h,t}\leq Qmax_h,\quad Vmin_h\leq V_{h,t}\leq Vmax_h
$$

**Explicación.** Restringe operación de térmicas, turbinamiento y almacenamiento.

## 9. Guía para construir el archivo `.dat`

A partir de las tablas anteriores, prepare el archivo de datos respetando los nombres de conjuntos, parámetros y unidades del modelo. La siguiente estructura muestra cómo debe organizarse la información.

```ampl
set G := T1 T2;
set H := H1;
set T := 1 2 3 4;

param Demand :=
1 130
2 170
3 150
4 120
;

param Cost :=
T1 35
T2 55
;

param Pmax :=
T1 100
T2 80
;

param V0 :=
H1 80
;

param Vmin :=
H1 20
;

param Vmax :=
H1 120
;

param Qmax :=
H1 35
;

param Prod :=
H1 2.0
;

param Inflow:
      1  2  3  4 :=
H1   20 15 10 25
;

param VOLL := 1000;
```

## 10. Resultados esperados

Reportar generación térmica, generación hidro, volumen final, uso de agua y ENS.

## 11. Actividad asociada

[Actividad 02](../actividades/README.md)

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
