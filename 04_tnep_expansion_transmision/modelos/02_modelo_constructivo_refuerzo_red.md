# Modelo constructivo de refuerzo de red

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)



![Esquema del modelo](../assets/figuras/modelos/tnep_garver_inversion.svg)

## 1. Intuición del modelo

El enfoque constructivo identifica refuerzos de manera iterativa a partir de congestión o infactibilidad, y ayuda a interpretar la lógica de expansión.

## 2. Elementos de la formulación

| Elemento | Descripción |
|---|---|
| Conjuntos | $N$: barras; $L$: corredores; $T$: periodos si aplica. |
| Parámetros | $D_n$, $G^{max}_n$, $c_\ell$, $\overline{F}_\ell$, $x_\ell$, $n^0_\ell$, $\overline{n}_\ell$. |
| Variables | $n_\ell$, $F_\ell$, $\theta_n$, $P_n$, $ENS_n$. |

## 3. Formulación matemática

### Objetivo

Minimizar inversión y penalización por ENS.

$$
\min Z=\sum_{\ell\in L}c_\ell n_\ell+\sum_{n\in N}VOLL\,ENS_n
$$

### Balance nodal

Generación, demanda, ENS y flujos se equilibran.

$$
P_n-D_n+ENS_n=\sum_{\ell\in L}A_{n,\ell}F_\ell
$$

### Capacidad de corredor

La capacidad depende de circuitos existentes y construidos.

$$
-\overline{F}_\ell(n^0_\ell+n_\ell)\leq F_\ell\leq \overline{F}_\ell(n^0_\ell+n_\ell)
$$

### Límite de construcción

No se construye más que el máximo permitido.

$$
0\leq n_\ell\leq\overline{n}_\ell
$$

### Relación DC si aplica

En formulaciones DC, el flujo depende de ángulos.

$$
F_\ell=\frac{(n^0_\ell+n_\ell)(\theta_i-\theta_j)}{x_\ell}
$$

## 4. Interpretación técnica

La solución debe analizar corredores seleccionados, costo de inversión, ENS, congestión y diferencias entre formulaciones.

## 5. Actividad relacionada

- [Ir a la actividad](../actividades/actividad_04_tnep_garver.md)
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)
