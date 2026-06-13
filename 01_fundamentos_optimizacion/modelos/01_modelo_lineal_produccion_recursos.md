# Modelo lineal de producción con recursos limitados

> [Menú principal](../../README.md) · [Volver a Fundamentos](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)

## 1. Contexto del problema

Una organización debe decidir cómo usar recursos escasos entre alternativas. El ejemplo es pequeño, pero reproduce la estructura de despacho, asignación de capacidad e inversión.

## 2. Enunciado guía

Determinar la cantidad óptima de cada producto maximizando beneficio o minimizando costo bajo límites de recursos.

## 3. Figura conceptual del modelo

![Figura conceptual](../assets/figuras/02_region_factible.svg)

## 4. Datos que debe reconocer el estudiante

| Elemento | Descripción |
|---|---|
| Conjuntos | $P$: productos. |
| Índices | $p\in P$. |
| Parámetros | $c_p$, $a_p$, $R$, $\overline{x}_p$. |
| Variables | $x_p$: producción. |

## 5. Formulación matemática

### Función objetivo

$$
\max Z=\sum_{p\in P}c_px_p
$$

### Recurso

$$
\sum_{p\in P}a_px_p\leq R
$$

El consumo total no supera la disponibilidad.

### Límite

$$
0\leq x_p\leq \overline{x}_p
$$

Cada producto tiene cota técnica.

## 6. Interpretación técnica

La solución no debe interpretarse solo como un valor objetivo. El estudiante debe explicar qué decisiones se activan, qué restricciones quedan vinculantes y qué implicación física o económica tiene el resultado.

## 7. Qué resultado debe graficarse

Gráfico de región factible, producción por alternativa y holgura de recursos.

## 8. Errores frecuentes

- No revisar unidades.
- Confundir parámetro con variable.
- No analizar restricciones activas.

## 9. Actividad relacionada

[Ir a la actividad](../actividades/actividad_01A_produccion_lineal.md)

---

> [Menú principal](../../README.md) · [Volver a Fundamentos](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)
