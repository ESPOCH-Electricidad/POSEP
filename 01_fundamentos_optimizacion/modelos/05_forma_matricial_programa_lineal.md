# Forma matricial de un programa lineal

> [Menú principal](../../README.md) · [Volver a Fundamentos](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)

## 1. Contexto del problema

Los solvers organizan el modelo como matrices, vectores y dominios. Esta vista permite entender escala, estructura y sensibilidad.

## 2. Enunciado guía

Representar un PL en forma compacta con matriz de restricciones y vector de costos.

## 3. Figura conceptual del modelo

![Figura conceptual](../assets/figuras/05_dualidad_sensibilidad.svg)

## 4. Datos que debe reconocer el estudiante

| Elemento | Descripción |
|---|---|
| Conjuntos | $I$: restricciones, $J$: variables. |
| Índices | $i\in I$, $j\in J$. |
| Parámetros | $A_{i,j}$, $b_i$, $c_j$. |
| Variables | $x_j$. |

## 5. Formulación matemática

### Función objetivo

$$
\min Z=\sum_{j\in J}c_jx_j
$$

### Restricciones

$$
\sum_{j\in J}A_{i,j}x_j\geq b_i\quad \forall i
$$

Cada fila representa una restricción.

### Dominio

$$
x_j\geq 0\quad \forall j
$$

Variables continuas no negativas.

## 6. Interpretación técnica

La solución no debe interpretarse solo como un valor objetivo. El estudiante debe explicar qué decisiones se activan, qué restricciones quedan vinculantes y qué implicación física o económica tiene el resultado.

## 7. Qué resultado debe graficarse

Diagrama de matriz, variables activas, holguras y duales.

## 8. Errores frecuentes

- No controlar sentido de restricciones.
- Perder unidades.
- No relacionar matriz con interpretación física.

## 9. Actividad relacionada

[Ir a la actividad](../actividades/actividad_01A_produccion_lineal.md)

---

> [Menú principal](../../README.md) · [Volver a Fundamentos](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)
