# Ejemplo 03 — Transporte de energía

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

El problema de transporte asigna flujos desde fuentes hacia cargas. No representa leyes eléctricas de corriente alterna, pero introduce balances, costos y restricciones de oferta/demanda.

## 2. Enunciado

Existen tres fuentes de energía y tres centros de carga. Cada fuente tiene oferta máxima, cada carga tiene demanda mínima y cada ruta tiene un costo unitario de transporte. Se debe determinar la energía enviada por cada ruta minimizando el costo total.



## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| I | fuentes de energía |
| J | centros de carga |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| supply[i] | MWh | oferta máxima de la fuente i |
| demand[j] | MWh | demanda mínima de la carga j |
| cost[i,j] | USD/MWh | costo de transporte de i a j |

## 5. Datos completos para construir el archivo de datos

### Fuentes

| fuente | supply_mwh |
| --- | --- |
| F1 | 120 |
| F2 | 100 |
| F3 | 90 |

### Cargas

| carga | demand_mwh |
| --- | --- |
| C1 | 80 |
| C2 | 110 |
| C3 | 90 |

### Costos de transporte

| fuente | carga | cost_usd_mwh |
| --- | --- | --- |
| F1 | C1 | 5 |
| F1 | C2 | 7 |
| F1 | C3 | 9 |
| F2 | C1 | 6 |
| F2 | C2 | 4 |
| F2 | C3 | 8 |
| F3 | C1 | 9 |
| F3 | C2 | 6 |
| F3 | C3 | 3 |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| f[i,j] | MWh, continua no negativa | flujo enviado desde fuente i hacia carga j |

## 7. Función objetivo

$$
\min Z=\sum_{i\in I}\sum_{j\in J} cost_{i,j} f_{i,j}
$$

**Explicación de la función objetivo.** Minimiza el costo total de transporte de energía considerando todas las rutas posibles entre fuentes y cargas.

## 8. Restricciones del modelo

### Oferta máxima

$$
\sum_{j\in J} f_{i,j}\leq supply_i\quad \forall i\in I
$$

**Explicación.** Cada fuente no puede enviar más energía que su disponibilidad.

### Demanda mínima

$$
\sum_{i\in I} f_{i,j}\geq demand_j\quad \forall j\in J
$$

**Explicación.** Cada carga debe recibir al menos la demanda requerida.

### No negatividad de flujos

$$
f_{i,j}\geq 0\quad \forall i,j
$$

**Explicación.** No se permiten flujos negativos.

## 9. Plantilla `.dat` sugerida

```ampl
set I := F1 F2 F3;
set J := C1 C2 C3;

param supply :=
F1 120
F2 100
F3 90
;

param demand :=
C1 80
C2 110
C3 90
;

param cost:
        C1  C2  C3 :=
F1      5   7   9
F2      6   4   8
F3      9   6   3
;
```

## 10. Resultados esperados

El estudiante debe reportar flujos por ruta, costo total, fuentes saturadas y cargas cubiertas.

## 11. Actividad asociada

[Actividad 01B](../actividades/actividad_01_transporte_energia.md)

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
