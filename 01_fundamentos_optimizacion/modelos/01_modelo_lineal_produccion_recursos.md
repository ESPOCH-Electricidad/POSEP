# Modelo lineal de producción con recursos limitados

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)



![Esquema del modelo](../assets/figuras/modelos/modelo_produccion_lineal.svg)

## 1. Intuición del modelo

Este modelo permite introducir la programación lineal mediante una decisión de asignación de recursos. Cada alternativa consume capacidad y aporta beneficio o costo. El objetivo es encontrar la combinación factible que optimiza el criterio económico.

## 2. Elementos de la formulación

| Elemento | Descripción |
|---|---|
| Conjunto | $P$: productos o alternativas. |
| Índice | $p \in P$. |
| Parámetros | $c_p$: beneficio; $a_p$: consumo de recurso; $R$: recurso disponible; $\overline{x}_p$: producción máxima. |
| Variable | $x_p$: cantidad producida del producto $p$. |

## 3. Formulación matemática

### Función objetivo

Maximizar beneficio total.

$$
\max Z = \sum_{p \in P} c_p x_p
$$

### Recurso disponible

El consumo total no puede superar el recurso disponible.

$$
\sum_{p \in P} a_p x_p \leq R
$$

### Límite de producción

Cada alternativa respeta su capacidad máxima.

$$
0 \leq x_p \leq \overline{x}_p \quad \forall p \in P
$$

## 4. Interpretación técnica

La solución muestra qué alternativas son económicamente atractivas y qué restricción limita el sistema. Si la restricción de recurso está activa, aumentar $R$ podría mejorar el objetivo.

## 5. Actividad relacionada

- [Ir a la actividad](../actividades/actividad_01_fundamentos_optimizacion.md)
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)
