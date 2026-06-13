# Modelo de transporte de energía

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)



![Esquema del modelo](../assets/figuras/modelos/modelo_transporte_energia.svg)

## 1. Intuición del modelo

El modelo de transporte asigna flujos desde fuentes de oferta hacia nodos de demanda. Es una formulación previa a los modelos de red, porque considera capacidad y demanda, pero no representa leyes eléctricas como ángulos o reactancias.

## 2. Elementos de la formulación

| Elemento | Descripción |
|---|---|
| Conjuntos | $I$: fuentes; $J$: demandas. |
| Índices | $i \in I$, $j \in J$. |
| Parámetros | $S_i$: oferta; $D_j$: demanda; $c_{i,j}$: costo de transporte. |
| Variable | $f_{i,j}$: flujo enviado desde $i$ hacia $j$. |

## 3. Formulación matemática

### Objetivo

Minimizar costo total de transporte.

$$
\min Z = \sum_{i \in I}\sum_{j \in J} c_{i,j} f_{i,j}
$$

### Oferta

Cada fuente no puede enviar más que su capacidad.

$$
\sum_{j \in J} f_{i,j} \leq S_i \quad \forall i \in I
$$

### Demanda

Cada destino debe recibir su demanda.

$$
\sum_{i \in I} f_{i,j} \geq D_j \quad \forall j \in J
$$

### No negatividad

Los flujos no pueden ser negativos.

$$
f_{i,j} \geq 0 \quad \forall i,j
$$

## 4. Interpretación técnica

El resultado identifica rutas de transporte utilizadas y fuentes marginales. Es útil para comprender después el modelo de transporte en expansión de transmisión.

## 5. Actividad relacionada

- [Ir a la actividad](../actividades/actividad_01_fundamentos_optimizacion.md)
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)
