# Flujo óptimo de potencia DC

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)



![Esquema del modelo](../assets/figuras/modelos/opf_red_dc_ac.svg)

## 1. Intuición del modelo

El OPF-DC optimiza el despacho considerando red de transmisión bajo una aproximación lineal. Permite analizar congestión y redispatch sin modelar potencia reactiva ni pérdidas.

## 2. Elementos de la formulación

| Elemento | Descripción |
|---|---|
| Conjuntos | $N$: barras; $L$: líneas; $G$: generadores. |
| Parámetros | $P^D_n$, $c_g$, $x_\ell$, $\overline{F}_\ell$, $\underline{P}_g$, $\overline{P}_g$. |
| Variables | $P_g$, $\theta_n$, $F_\ell$, $ENS_n$. |

## 3. Formulación matemática

### Objetivo

Minimizar costo y ENS.

$$
\min Z=\sum_{g\in G}c_gP_g+\sum_{n\in N}VOLL\,ENS_n
$$

### Balance nodal

Cada barra equilibra inyección y flujos.

$$
\sum_{g\in G_n}P_g-P^D_n+ENS_n=\sum_{\ell\in L}A_{n,\ell}F_\ell
$$

### Flujo DC

El flujo depende de diferencia angular.

$$
F_\ell=\frac{\theta_i-\theta_j}{x_\ell}
$$

### Límite de línea

Cada línea respeta su capacidad.

$$
-\overline{F}_\ell\leq F_\ell\leq\overline{F}_\ell
$$

### Referencia

Una barra define el ángulo cero.

$$
\theta_{ref}=0
$$

## 4. Interpretación técnica

Debe revisarse qué líneas se saturan, cómo cambia el despacho y si aparece ENS en barras específicas.

## 5. Actividad relacionada

- [Ir a la actividad](../actividades/actividad_03_opf_dc_ac.md)
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)
