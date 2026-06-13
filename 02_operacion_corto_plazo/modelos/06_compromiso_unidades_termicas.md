# Compromiso de unidades térmicas

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)



![Esquema del modelo](../assets/figuras/modelos/unit_commitment.svg)

## 1. Intuición del modelo

Decide qué unidades se encienden, cuándo arrancan y cuánto generan. Es un MILP por sus variables binarias.

## 2. Elementos de la formulación

| Elemento | Descripción |
|---|---|
| Conjuntos | $G$: unidades; $T$: horas. |
| Parámetros | $c_g$, $SU_g$, $\underline{P}_g$, $\overline{P}_g$, $RU_g$, $RD_g$, $D_t$. |
| Variables | $P_{g,t}$, $u_{g,t}$, $v_{g,t}$, $ENS_t$. |

## 3. Formulación matemática

### Objetivo

Minimizar generación, arranques y ENS.

$$
\min Z=\sum_{g,t}c_gP_{g,t}+\sum_{g,t}SU_gv_{g,t}+\sum_t VOLL\,ENS_t
$$

### Límites con estado

La generación depende de si la unidad está encendida.

$$
\underline{P}_g u_{g,t}\leq P_{g,t}\leq \overline{P}_g u_{g,t}
$$

### Arranque

La variable de arranque captura transición de apagado a encendido.

$$
v_{g,t}\geq u_{g,t}-u_{g,t-1}
$$

### Rampa

La generación no cambia más que la rampa permitida.

$$
P_{g,t}-P_{g,t-1}\leq RU_g
$$

## 4. Interpretación técnica

El resultado debe analizar estados, arranques, rampas activas, reserva y costo operativo.

## 5. Actividad relacionada

- [Ir a la actividad](../actividades/actividad_02_operacion_corto_plazo.md)
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)
