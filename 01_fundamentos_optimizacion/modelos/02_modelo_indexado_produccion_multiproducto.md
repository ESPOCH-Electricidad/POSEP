# Modelo indexado de producción multiproducto

> [Menú principal](../../README.md) · [Volver a Fundamentos](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)

## 1. Contexto del problema

El modelo muestra cómo escalar una formulación usando conjuntos e índices, evitando escribir manualmente ecuaciones repetidas.

## 2. Enunciado guía

Formular una producción multiproducto con varios recursos y demanda mínima.

## 3. Figura conceptual del modelo

![Figura conceptual](../assets/figuras/01_mapa_modelo_optimizacion.svg)

## 4. Datos que debe reconocer el estudiante

| Elemento | Descripción |
|---|---|
| Conjuntos | $P$: productos, $R$: recursos. |
| Índices | $p\in P$, $r\in R$. |
| Parámetros | $a_{r,p}$, $B_r$, $c_p$, $D$. |
| Variables | $x_p$. |

## 5. Formulación matemática

### Función objetivo

$$
\min Z=\sum_{p\in P}c_px_p
$$

### Demanda

$$
\sum_{p\in P}x_p\geq D
$$

La producción agregada cumple un requerimiento.

### Recursos

$$
\sum_{p\in P}a_{r,p}x_p\leq B_r\quad \forall r\in R
$$

Cada recurso tiene disponibilidad limitada.

## 6. Interpretación técnica

La solución no debe interpretarse solo como un valor objetivo. El estudiante debe explicar qué decisiones se activan, qué restricciones quedan vinculantes y qué implicación física o económica tiene el resultado.

## 7. Qué resultado debe graficarse

Uso de recursos por tipo y producción óptima por producto.

## 8. Errores frecuentes

- Omitir índices.
- No declarar toda la matriz de parámetros.
- Duplicar ecuaciones manualmente.

## 9. Actividad relacionada

[Ir a la actividad](../actividades/actividad_01A_produccion_lineal.md)

---

> [Menú principal](../../README.md) · [Volver a Fundamentos](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)
