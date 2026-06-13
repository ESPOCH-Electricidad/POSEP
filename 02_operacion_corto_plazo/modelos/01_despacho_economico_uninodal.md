# Despacho económico uninodal

> [Menú principal](../../README.md) · [Volver a Operación](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)

## 1. Contexto del problema

El operador cubre demanda con generadores de distinto costo ignorando la red.

## 2. Enunciado guía

Determinar generación por unidad para minimizar costo.

## 3. Figura conceptual del modelo

![Figura conceptual](../assets/figuras/02_orden_merito_despacho.svg)

## 4. Datos que debe reconocer el estudiante

| Elemento | Descripción |
|---|---|
| Conjuntos e índices | $G$: generadores; $T$: periodos |
| Parámetros | demanda, costos, límites técnicos, disponibilidad |
| Variables | $P_{g,t}$, $ENS_t$ |

## 5. Formulación matemática

### Función objetivo

$$
\min Z=\sum_{t,g}c_gP_{g,t}+\sum_tVOLL\,ENS_t
$$

### Balance

$$
\sum_gP_{g,t}+ENS_t=D_t
$$

Demanda cubierta en cada periodo.

### Límites

$$
\underline{P}_g\leq P_{g,t}\leq \overline{P}_g
$$

Rangos técnicos de operación.

## 6. Interpretación técnica

La solución no debe interpretarse solo como un valor objetivo. El estudiante debe explicar qué decisiones se activan, qué restricciones quedan vinculantes y qué implicación física o económica tiene el resultado.

## 7. Qué resultado debe graficarse

Gráfico de generación por unidad, costo horario y ENS.

## 8. Errores frecuentes

- No revisar límites.
- No interpretar ENS.
- No graficar resultados horarios.

## 9. Actividad relacionada

[Ir a la actividad](../actividades/actividad_02_operacion_corto_plazo.md)

---

> [Menú principal](../../README.md) · [Volver a Operación](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)
