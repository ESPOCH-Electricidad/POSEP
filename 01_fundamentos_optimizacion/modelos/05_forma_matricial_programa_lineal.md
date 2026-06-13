# Forma matricial de un programa lineal

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)



![Esquema del modelo](../assets/figuras/modelos/modelo_forma_matricial.svg)

## 1. Intuición del modelo

La forma matricial resume un problema lineal usando vectores y matrices. Es útil para entender cómo los solvers organizan la información y por qué es importante mantener consistencia dimensional.

## 2. Elementos de la formulación

| Elemento | Descripción |
|---|---|
| Conjuntos | $I$: restricciones; $J$: variables. |
| Índices | $i \in I$, $j \in J$. |
| Parámetros | $c_j$: costo; $A_{i,j}$: coeficiente; $b_i$: lado derecho. |
| Variable | $x_j$: decisión. |

## 3. Formulación matemática

### Objetivo

Minimizar costo lineal.

$$
\min Z = \sum_{j \in J} c_j x_j
$$

### Restricciones

Cada fila de la matriz representa una restricción.

$$
\sum_{j \in J} A_{i,j}x_j \geq b_i \quad \forall i \in I
$$

### Dominio

Variables continuas no negativas.

$$
x_j \geq 0 \quad \forall j \in J
$$

## 4. Interpretación técnica

Esta formulación permite reconocer que modelos eléctricos grandes son extensiones estructuradas de matrices de balance, límites y costos.

## 5. Actividad relacionada

- [Ir a la actividad](../actividades/actividad_01_fundamentos_optimizacion.md)
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)
