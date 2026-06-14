# Modelo 01 — Despacho económico uninodal

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

El despacho económico uninodal determina la generación de menor costo para cubrir una demanda agregada sin representar la red de transmisión.

## 2. Enunciado

Con tres generadores térmicos disponibles y una demanda de 150 MW, determine la potencia generada por cada unidad minimizando el costo operativo.



## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| G | generadores |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| Demand | MW | demanda total del sistema |
| Pmin[g] | MW | generación mínima |
| Pmax[g] | MW | generación máxima |
| Cost[g] | USD/MWh | costo variable |

## 5. Datos completos para construir el archivo de datos

### Generadores

| gen | pmin_mw | pmax_mw | cost_usd_mwh |
| --- | --- | --- | --- |
| G1 | 20 | 100 | 15 |
| G2 | 30 | 80 | 22 |
| G3 | 0 | 60 | 35 |

### Demanda

| parametro | valor | unidad |
| --- | --- | --- |
| Demand | 150 | MW |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| P[g] | MW, continua | potencia generada por g |

## 7. Función objetivo

$$
\min Z=\sum_{g\in G} Cost_g P_g
$$

**Explicación de la función objetivo.** Minimiza el costo variable total de generación para una hora representativa.

## 8. Restricciones del modelo

### Balance de potencia

$$
\sum_{g\in G}P_g = Demand
$$

**Explicación.** La generación total debe igualar la demanda agregada del sistema.

### Límites de generación

$$
Pmin_g\leq P_g\leq Pmax_g\quad \forall g\in G
$$

**Explicación.** Cada unidad opera dentro de su rango técnico permitido.

## 9. Plantilla `.dat` sugerida

```ampl
set G := G1 G2 G3;

param Demand := 150;

param Pmin :=
G1 20
G2 30
G3 0
;

param Pmax :=
G1 100
G2 80
G3 60
;

param Cost :=
G1 15
G2 22
G3 35
;
```

## 10. Resultados esperados

Reportar generación por unidad, costo total, unidad marginal y límites activos.

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
