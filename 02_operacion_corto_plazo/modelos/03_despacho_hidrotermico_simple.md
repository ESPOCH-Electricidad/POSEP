# Despacho hidrotérmico simple

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)



![Esquema del modelo](../assets/figuras/modelos/hidrotermico.svg)

## 1. Intuición del modelo

Coordina generación hidroeléctrica limitada por energía disponible y generación térmica con costo variable.

## 2. Elementos de la formulación

| Elemento | Descripción |
|---|---|
| Conjuntos | $G$: térmicas; $H$: hidroeléctricas; $T$: periodos. |
| Parámetros | $c_g$, $D_t$, $\overline{P}_h$, $E_h$. |
| Variables | $P_{g,t}$, $H_{h,t}$, $ENS_t$. |

## 3. Formulación matemática

### Objetivo

Minimizar costo térmico y ENS.

$$
\min Z=\sum_t\sum_g c_gP_{g,t}+\sum_t VOLL\,ENS_t
$$

### Balance

Térmica, hidro y ENS cubren demanda.

$$
\sum_gP_{g,t}+\sum_hH_{h,t}+ENS_t=D_t
$$

### Energía hidro

El uso hidro total no supera disponibilidad.

$$
\sum_t H_{h,t}\leq E_h \quad \forall h
$$

## 4. Interpretación técnica

La solución muestra en qué horas conviene usar agua y en qué horas opera generación térmica.

## 5. Actividad relacionada

- [Ir a la actividad](../actividades/actividad_02_operacion_corto_plazo.md)
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)
