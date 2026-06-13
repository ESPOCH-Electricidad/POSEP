# 04 — Planificación de expansión de transmisión

> [Menú principal](../README.md) · [Índice del sitio](../docs/index.md) · [Ruta de aprendizaje](../docs/learning_path.md) · [Modelos](../docs/modelos.md) · [Casos](../docs/casos_de_estudio.md) · [Evaluación](../docs/evaluacion.md)



![Mapa visual del bloque](../docs/assets/img/bloques/04_tnep.svg)

## 1. Propósito del bloque

La planificación de expansión de transmisión decide qué líneas o circuitos deben construirse para permitir que la generación abastezca la demanda de forma segura y económica. El problema combina decisiones de inversión y operación de red.

![Formulaciones TNEP](assets/figuras/teoria/tnep_formulaciones.svg)

## 2. Formulación conceptual

La decisión de inversión se representa mediante variables como:

$$
n_\ell \in \mathbb{Z}_+
$$

donde $n_\ell$ es el número de circuitos nuevos en el corredor $\ell$. El costo de inversión es:

$$
C^{inv} = \sum_{\ell \in L} c_\ell n_\ell
$$

y el flujo queda limitado por la capacidad total existente y construida:

$$
-\overline{F}_\ell (n^0_\ell+n_\ell)
\leq F_\ell \leq
\overline{F}_\ell (n^0_\ell+n_\ell)
$$

## 3. Modelos del bloque

| Modelo | Acceso |
|---|---|
| Transporte | [Abrir](modelos/01_modelo_transporte_expansion_transmision.md) |
| Constructivo | [Abrir](modelos/02_modelo_constructivo_refuerzo_red.md) |
| DC | [Abrir](modelos/03_modelo_dc_expansion_transmision.md) |
| Híbrido | [Abrir](modelos/04_modelo_hibrido_expansion_transmision.md) |
| Lineal disyuntivo | [Abrir](modelos/05_modelo_lineal_disyuntivo_expansion_transmision.md) |
| Multietapa | [Abrir](modelos/06_modelo_multietapa_expansion_transmision.md) |
---

> [Menú principal](../README.md) · [Índice del sitio](../docs/index.md) · [Ruta de aprendizaje](../docs/learning_path.md) · [Modelos](../docs/modelos.md) · [Casos](../docs/casos_de_estudio.md) · [Evaluación](../docs/evaluacion.md)
