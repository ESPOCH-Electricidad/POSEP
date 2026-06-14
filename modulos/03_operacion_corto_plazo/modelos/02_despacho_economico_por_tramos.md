# Modelo 02 — Despacho económico por tramos

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

Este modelo aproxima curvas de costo crecientes mediante bloques de generación con costos variables diferentes.

## 2. Enunciado

Para dos generadores con dos tramos de generación cada uno y demanda de 170 MW, determine cuánto despachar en cada tramo minimizando costo.



## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| G | generadores |
| K | tramos de generación |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| Demand | MW | demanda total |
| SegMax[g,k] | MW | capacidad máxima del tramo k del generador g |
| SegCost[g,k] | USD/MWh | costo variable del tramo |

## 5. Datos completos para construir el archivo de datos

### Tramos

| gen | tramo | segmax_mw | segcost_usd_mwh |
| --- | --- | --- | --- |
| G1 | K1 | 60 | 14 |
| G1 | K2 | 50 | 21 |
| G2 | K1 | 70 | 18 |
| G2 | K2 | 60 | 28 |

### Demanda

| parametro | valor | unidad |
| --- | --- | --- |
| Demand | 170 | MW |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| Pseg[g,k] | MW, continua no negativa | potencia generada en el tramo k del generador g |

## 7. Función objetivo

$$
\min Z=\sum_{g\in G}\sum_{k\in K} SegCost_{g,k} Pseg_{g,k}
$$

**Explicación de la función objetivo.** Minimiza el costo total sumando la energía producida en cada tramo por su costo marginal.

## 8. Restricciones del modelo

### Balance de potencia

$$
\sum_{g\in G}\sum_{k\in K}Pseg_{g,k}=Demand
$$

**Explicación.** La suma de generación de todos los tramos cubre exactamente la demanda.

### Capacidad de tramo

$$
0\leq Pseg_{g,k}\leq SegMax_{g,k}\quad \forall g,k
$$

**Explicación.** Cada tramo tiene una capacidad máxima; los tramos más caros se usan solo si los baratos se saturan.

## 9. Plantilla `.dat` sugerida

```ampl
set G := G1 G2;
set K := K1 K2;

param Demand := 170;

param SegMax:
       K1  K2 :=
G1     60  50
G2     70  60
;

param SegCost:
       K1  K2 :=
G1     14  21
G2     18  28
;
```

## 10. Resultados esperados

Reportar potencia por tramo, costo total y tramos saturados.

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
