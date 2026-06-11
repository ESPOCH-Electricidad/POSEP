# GEP multianual

> Nota: esta página describe la formulación matemática con fines didácticos. La implementación computacional puede variar según el solver, el lenguaje de modelado y las simplificaciones adoptadas en clase.


## Idea del modelo

Extiende el GEP a un horizonte de planificación con varios años, permitiendo cronogramas de inversión y crecimiento de demanda.

## Conjuntos e índices


- $g\in\mathcal{G}$: tecnologías.
- $c\in\mathcal{CAND}$: tecnologías candidatas.
- $t\in\mathcal{T}$: años.
- $b\in\mathcal{B}$: bloques de carga, si aplica.


## Parámetros


- $D_{t,b}$: demanda por año y bloque.
- $df_t$: factor de descuento.
- $IC_{c,t}$: costo de inversión por tecnología y año.
- $Life_c$: vida útil o disponibilidad de inversión.
- $IC_{c,t}^{max}$: límite de construcción por año.


## Variables de decisión


- $I_{c,t}$: inversión nueva en tecnología $c$ en año $t$.
- $Cap_{g,t}$: capacidad acumulada disponible.
- $P_{g,t,b}$: despacho.
- $ENS_{t,b}$: energía no servida.


## Función objetivo


$$
\min \sum_{t}df_t\left[\sum_{c}IC_{c,t}I_{c,t}+\sum_b h_b\sum_gC_gP_{g,t,b}+\sum_bh_bC^{ENS}ENS_{t,b}\right]
$$


## Restricciones principales


Evolución de capacidad:

$$
Cap_{g,t}=P_g^0+\sum_{\tau\leq t}I_{g,\tau}
$$

Balance por año y bloque:

$$
\sum_gP_{g,t,b}+ENS_{t,b}=D_{t,b}
$$

Límites de despacho:

$$
P_{g,t,b}\leq Cap_{g,t}
$$

Reserva por año:

$$
\sum_g firm_gCap_{g,t}\geq(1+RM)D_{t,peak}
$$

Límites anuales de construcción:

$$
0\leq I_{c,t}\leq IC_{c,t}^{max}
$$


## Interpretación de resultados


El resultado debe leerse como cronograma: qué se construye, cuándo se construye, cuánto cuesta y qué restricciones justifican la decisión.


## Errores frecuentes

- Evaluar solo el último año e ignorar el cronograma.
- Confundir inversión anual con capacidad acumulada.
- No aplicar descuento cuando corresponde.
