# Flujo óptimo de potencia AC

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)



![Esquema del modelo](../assets/figuras/modelos/opf_red_dc_ac.svg)

## 1. Intuición del modelo

El OPF-AC representa potencia activa, potencia reactiva, tensiones y pérdidas. Es más fiel al sistema eléctrico, pero resulta no lineal y puede ser más difícil de resolver.

## 2. Elementos de la formulación

| Elemento | Descripción |
|---|---|
| Conjuntos | $N$: barras; $G$: generadores. |
| Parámetros | $P^D_i$, $Q^D_i$, $G_{ij}$, $B_{ij}$, límites de tensión y generación. |
| Variables | $P_g$, $Q_g$, $V_i$, $\theta_i$. |

## 3. Formulación matemática

### Objetivo

Minimizar costo de generación.

$$
\min Z=\sum_{g\in G}c_gP_g
$$

### Balance activo

Balance no lineal de potencia activa.

$$
P_i^G-P_i^D=V_i\sum_{j\in N}V_j\left(G_{ij}\cos\theta_{ij}+B_{ij}\sin\theta_{ij}\right)
$$

### Balance reactivo

Balance no lineal de potencia reactiva.

$$
Q_i^G-Q_i^D=V_i\sum_{j\in N}V_j\left(G_{ij}\sin\theta_{ij}-B_{ij}\cos\theta_{ij}\right)
$$

### Tensión

La tensión debe mantenerse en rango.

$$
\underline{V}_i\leq V_i\leq\overline{V}_i
$$

### Generación reactiva

Los generadores tienen límites de reactivos.

$$
\underline{Q}_g\leq Q_g\leq\overline{Q}_g
$$

## 4. Interpretación técnica

El resultado debe interpretar tensiones, reactivos, pérdidas, límites activos y diferencias frente a OPF-DC.

## 5. Actividad relacionada

- [Ir a la actividad](../actividades/actividad_03_opf_dc_ac.md)
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)
