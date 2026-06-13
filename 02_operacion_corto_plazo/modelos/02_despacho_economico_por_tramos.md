# Despacho económico con costos por tramos

> [Menú principal](../../README.md) · [Volver a Operación](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)

## 1. Contexto del problema

Las curvas de costo se aproximan mediante segmentos lineales.

## 2. Enunciado guía

Despachar segmentos de generación minimizando costo.

## 3. Figura conceptual del modelo

![Figura conceptual](../assets/figuras/03_costos_por_tramos.svg)

## 4. Datos que debe reconocer el estudiante

| Elemento | Descripción |
|---|---|
| Conjuntos e índices | $G$: generadores; $K$: tramos; $T$: periodos |
| Parámetros | demanda, costos, límites técnicos, disponibilidad |
| Variables | $P_{g,k,t}$ |

## 5. Formulación matemática

### Función objetivo

$$
\min Z=\sum_{t,g,k}c_{g,k}P_{g,k,t}
$$

### Balance

$$
\sum_g\sum_kP_{g,k,t}=D_t
$$

La suma de tramos cubre demanda.

### Tramo

$$
0\leq P_{g,k,t}\leq \overline{P}_{g,k}
$$

Cada tramo tiene capacidad.

## 6. Interpretación técnica

La solución no debe interpretarse solo como un valor objetivo. El estudiante debe explicar qué decisiones se activan, qué restricciones quedan vinculantes y qué implicación física o económica tiene el resultado.

## 7. Qué resultado debe graficarse

Barras apiladas por tramo y costo total.

## 8. Errores frecuentes

- No revisar límites.
- No interpretar ENS.
- No graficar resultados horarios.

## 9. Actividad relacionada

[Ir a la actividad](../actividades/actividad_02_operacion_corto_plazo.md)

---

> [Menú principal](../../README.md) · [Volver a Operación](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)
