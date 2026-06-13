# Modelo GEP estático de capacidad

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)



![Esquema del modelo](../assets/figuras/modelos/gep_horizonte_inversion.svg)

## 1. Intuición del modelo

Decide capacidad nueva para cubrir demanda y margen de reserva en un periodo representativo.

## 2. Elementos de la formulación

| Elemento | Descripción |
|---|---|
| Conjuntos | $Y$: años; $B$: bloques; $K$: tecnologías candidatas; $E$: existentes. |
| Parámetros | $D_{y,b}$, $h_b$, $CAPEX_k$, $FOM_k$, $c_k$, $AF_k$, $FC_k$, $VOLL$, $RM$. |
| Variables | $Build_{k,y}$, $Cap_{k,y}$, $Gen_{k,y,b}$, $ENS_{y,b}$. |

## 3. Formulación matemática

### Objetivo

Minimizar inversión, costos fijos, operación y ENS.

$$
\min Z=\sum_{k,y}CAPEX_k Build_{k,y}+\sum_{k,y}FOM_k Cap_{k,y}+\sum_{k,y,b}c_k Gen_{k,y,b}+\sum_{y,b}VOLL\,ENS_{y,b}
$$

### Balance por bloque

Generación y ENS cubren demanda.

$$
\sum_k Gen_{k,y,b}+\sum_e Gen_{e,y,b}+ENS_{y,b}=D_{y,b}
$$

### Capacidad acumulada

La capacidad crece con inversiones previas.

$$
Cap_{k,y}=Cap_{k,y-1}+Build_{k,y}
$$

### Límite de generación

La generación queda limitada por capacidad y disponibilidad.

$$
Gen_{k,y,b}\leq AF_k Cap_{k,y}h_b
$$

### Reserva firme

La capacidad firme cubre demanda pico y margen.

$$
\sum_k FC_k Cap_{k,y}+\sum_e FC_e Cap^0_e\geq(1+RM)D^{peak}_y
$$

## 4. Interpretación técnica

El análisis debe diferenciar capacidad nueva, capacidad acumulada, energía generada, reserva, ENS y costo total.

## 5. Actividad relacionada

- [Ir a la actividad](../actividades/actividad_05_gep_multianual.md)
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)
