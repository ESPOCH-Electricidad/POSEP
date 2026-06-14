# Modelo 03 — Despacho económico con pérdidas

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

El despacho con pérdidas muestra que la demanda no es lo único que debe cubrirse: parte de la generación se pierde en la red. Se usa una aproximación cuadrática simple mediante coeficientes B.

## 2. Enunciado

Con tres generadores, demanda de 180 MW y una matriz B de pérdidas, determine el despacho que minimiza el costo operativo sujeto a balance con pérdidas.



## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| G | generadores |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| Demand | MW | demanda total |
| Pmin[g] | MW | límite mínimo |
| Pmax[g] | MW | límite máximo |
| Cost[g] | USD/MWh | costo variable |
| B[g,h] | 1/MW | coeficiente de pérdidas cuadráticas |

## 5. Datos completos para construir el archivo de datos

### Generadores

| gen | pmin_mw | pmax_mw | cost_usd_mwh |
| --- | --- | --- | --- |
| G1 | 20 | 120 | 16 |
| G2 | 20 | 100 | 20 |
| G3 | 10 | 80 | 30 |

### Matriz B

| g | h | B_1_mw |
| --- | --- | --- |
| G1 | G1 | 8e-05 |
| G1 | G2 | 2e-05 |
| G1 | G3 | 1e-05 |
| G2 | G1 | 2e-05 |
| G2 | G2 | 0.0001 |
| G2 | G3 | 3e-05 |
| G3 | G1 | 1e-05 |
| G3 | G2 | 3e-05 |
| G3 | G3 | 0.00012 |

### Demanda

| parametro | valor | unidad |
| --- | --- | --- |
| Demand | 180 | MW |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| P[g] | MW, continua | potencia generada por g |

## 7. Función objetivo

$$
\min Z=\sum_{g\in G}Cost_gP_g
$$

**Explicación de la función objetivo.** Minimiza costo de generación. Las pérdidas aparecen en la restricción de balance, por lo que el sistema debe generar más que la demanda.

## 8. Restricciones del modelo

### Balance con pérdidas

$$
\sum_{g\in G}P_g = Demand+\sum_{g\in G}\sum_{h\in G}B_{g,h}P_gP_h
$$

**Explicación.** La generación total cubre demanda más pérdidas activas estimadas por una expresión cuadrática.

### Límites de generación

$$
Pmin_g\leq P_g\leq Pmax_g\quad \forall g\in G
$$

**Explicación.** Cada generador mantiene su operación dentro de límites.

## 9. Plantilla `.dat` sugerida

```ampl
set G := G1 G2 G3;

param Demand := 180;

param Pmin :=
G1 20
G2 20
G3 10
;

param Pmax :=
G1 120
G2 100
G3 80
;

param Cost :=
G1 16
G2 20
G3 30
;

param B:
       G1       G2       G3 :=
G1     0.00008  0.00002  0.00001
G2     0.00002  0.00010  0.00003
G3     0.00001  0.00003  0.00012
;
```

## 10. Resultados esperados

Reportar generación, pérdidas totales, generación total y costo operativo.

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
