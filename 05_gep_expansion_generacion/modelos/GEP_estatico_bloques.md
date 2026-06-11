# GEP estático con bloques de carga

> Nota: esta página describe la formulación matemática con fines didácticos. La implementación computacional puede variar según el solver, el lenguaje de modelado y las simplificaciones adoptadas en clase.


## Idea del modelo

Representa la demanda mediante bloques de carga para capturar diferencias entre demanda punta, media y baja dentro de un periodo de planificación.

## Conjuntos e índices


- $g\in\mathcal{G}$: tecnologías.
- $b\in\mathcal{B}$: bloques de carga.
- $c\in\mathcal{CAND}$: tecnologías candidatas.


## Parámetros


- $D_b$: demanda del bloque $b$.
- $h_b$: duración del bloque.
- $C_g$: costo variable.
- $IC_g$: costo de inversión.
- $firm_g$: crédito de capacidad.


## Variables de decisión


- $P_{g,b}$: despacho de tecnología $g$ en bloque $b$.
- $I_g$: capacidad nueva instalada.
- $Cap_g$: capacidad total.
- $ENS_b$: energía no servida por bloque.


## Función objetivo


$$
\min \sum_{b\in\mathcal{B}}h_b\sum_g C_gP_{g,b}+\sum_{c\in\mathcal{CAND}}IC_c I_c+\sum_b h_b C^{ENS}ENS_b
$$


## Restricciones principales


Balance por bloque:

$$
\sum_g P_{g,b}+ENS_b=D_b
$$

Despacho limitado por capacidad:

$$
P_{g,b}\leq Cap_g
$$

Capacidad:

$$
Cap_g=P_g^0+I_g
$$

Reserva en punta:

$$
\sum_g firm_g Cap_g\geq (1+RM)D_{peak}
$$


## Interpretación de resultados


Permite observar cómo tecnologías de bajo costo operativo pueden despacharse muchas horas, mientras que otras tecnologías pueden justificarse por punta, reserva o costo de inversión.


## Actividad sugerida

Comparar el plan con un único bloque versus tres bloques de carga.
