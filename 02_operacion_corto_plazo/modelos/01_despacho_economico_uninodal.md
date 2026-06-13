# Despacho económico uninodal

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)



![Esquema del modelo](../assets/figuras/modelos/despacho_economico.svg)

## 1. Intuición del modelo

El despacho económico asigna generación para cubrir demanda al menor costo sin representar la red. Es el modelo operativo más básico.

## 2. Elementos de la formulación

| Elemento | Descripción |
|---|---|
| Conjuntos | $G$: generadores; $T$: periodos. |
| Parámetros | $c_g$, $\underline{P}_g$, $\overline{P}_g$, $D_t$, $VOLL$. |
| Variables | $P_{g,t}$, $ENS_t$. |

## 3. Formulación matemática

### Objetivo

Minimizar costo operativo y ENS.

$$
\min Z=\sum_{t\in T}\sum_{g\in G} c_g P_{g,t}+\sum_{t\in T}VOLL\,ENS_t
$$

### Balance

Generación y ENS cubren demanda.

$$
\sum_{g\in G}P_{g,t}+ENS_t=D_t \quad \forall t
$$

### Límites

Cada unidad respeta límites técnicos.

$$
\underline{P}_g \leq P_{g,t}\leq \overline{P}_g \quad \forall g,t
$$

## 4. Interpretación técnica

El resultado permite identificar la unidad marginal, el costo horario y la necesidad de ENS si no hay capacidad suficiente.

## 5. Actividad relacionada

- [Ir a la actividad](../actividades/actividad_02_operacion_corto_plazo.md)
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)
