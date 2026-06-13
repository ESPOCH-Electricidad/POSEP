# Despacho económico con costos por tramos

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)



![Esquema del modelo](../assets/figuras/modelos/despacho_economico.svg)

## 1. Intuición del modelo

Representa costos crecientes mediante segmentos lineales. Es útil cuando la curva real de costo no es estrictamente lineal.

## 2. Elementos de la formulación

| Elemento | Descripción |
|---|---|
| Conjuntos | $G$: generadores; $K$: tramos; $T$: periodos. |
| Parámetros | $c_{g,k}$, $\overline{P}_{g,k}$, $D_t$. |
| Variables | $P_{g,k,t}$: generación del tramo. |

## 3. Formulación matemática

### Objetivo

Minimizar costo por segmentos.

$$
\min Z=\sum_{t}\sum_{g}\sum_{k} c_{g,k}P_{g,k,t}
$$

### Balance

La suma de todos los tramos cubre demanda.

$$
\sum_g\sum_k P_{g,k,t}=D_t \quad \forall t
$$

### Límite por tramo

Cada tramo tiene capacidad máxima.

$$
0\leq P_{g,k,t}\leq \overline{P}_{g,k}
$$

## 4. Interpretación técnica

El orden de uso de tramos revela cómo el sistema utiliza primero segmentos de menor costo.

## 5. Actividad relacionada

- [Ir a la actividad](../actividades/actividad_02_operacion_corto_plazo.md)
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)
