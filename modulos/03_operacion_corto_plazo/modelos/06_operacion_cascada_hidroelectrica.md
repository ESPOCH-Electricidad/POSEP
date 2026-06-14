# Modelo 06 — Operación de cascada hidroeléctrica

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

Una cascada hidroeléctrica acopla embalses aguas arriba y aguas abajo. El caudal turbinado por una central puede ingresar como aporte a otra central.

## 2. Enunciado

Para dos embalses en cascada y cuatro periodos, determine turbinamiento, volumen y generación hidroeléctrica maximizando producción hidro o minimizando vertimientos, respetando balances de agua.



## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| R | embalses/centrales |
| T | periodos |
| UP[r] | embalses aguas arriba de r |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| V0[r] | hm3 | volumen inicial |
| Vmin[r] | hm3 | volumen mínimo |
| Vmax[r] | hm3 | volumen máximo |
| Inflow[r,t] | hm3 | aporte lateral |
| Qmax[r] | hm3 | turbinamiento máximo |
| Prod[r] | MWh/hm3 | coeficiente de producción |

## 5. Datos completos para construir el archivo de datos

### Embalses

| embalse | v0_hm3 | vmin_hm3 | vmax_hm3 | qmax_hm3 | prod_mwh_hm3 |
| --- | --- | --- | --- | --- | --- |
| R1 | 70 | 20 | 110 | 30 | 2.2 |
| R2 | 60 | 15 | 100 | 35 | 1.8 |

### Aportes laterales

| embalse | t1 | t2 | t3 | t4 |
| --- | --- | --- | --- | --- |
| R1 | 15 | 10 | 12 | 18 |
| R2 | 8 | 7 | 9 | 10 |

### Relación aguas arriba

| embalse | upstream |
| --- | --- |
| R1 |  |
| R2 | R1 |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| V[r,t] | hm3 | volumen |
| Q[r,t] | hm3 | turbinamiento |
| S[r,t] | hm3 | vertimiento |
| HGen[r,t] | MWh | energía hidro generada |

## 7. Función objetivo

$$
\max Z=\sum_{r\in R}\sum_{t\in T}HGen_{r,t}
$$

**Explicación de la función objetivo.** Maximiza generación hidro total de la cascada durante el horizonte de análisis.

## 8. Restricciones del modelo

### Generación hidro

$$
HGen_{r,t}=Prod_rQ_{r,t}\quad \forall r,t
$$

**Explicación.** Convierte caudal turbinado en energía producida.

### Balance de embalse

$$
V_{r,t}=V_{r,t-1}+Inflow_{r,t}+\sum_{u\in UP_r}Q_{u,t}-Q_{r,t}-S_{r,t}
$$

**Explicación.** Incluye aporte lateral, caudal recibido desde aguas arriba, turbinamiento propio y vertimiento.

### Límites de almacenamiento y caudal

$$
Vmin_r\leq V_{r,t}\leq Vmax_r,\quad 0\leq Q_{r,t}\leq Qmax_r,\quad S_{r,t}\geq 0
$$

**Explicación.** Asegura operación física factible de embalses y caudales.

## 9. Plantilla `.dat` sugerida

```ampl
set R := R1 R2;
set T := 1 2 3 4;

set UP[R1] := ;
set UP[R2] := R1;

param V0 :=
R1 70
R2 60
;

param Vmin :=
R1 20
R2 15
;

param Vmax :=
R1 110
R2 100
;

param Qmax :=
R1 30
R2 35
;

param Prod :=
R1 2.2
R2 1.8
;

param Inflow:
      1  2  3  4 :=
R1   15 10 12 18
R2    8  7  9 10
;
```

## 10. Resultados esperados

Reportar turbinamiento, generación, volumen por embalse y vertimientos.

## 11. Actividad asociada

[Actividad 02](../actividades/README.md)


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
