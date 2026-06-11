# TNEP: modelo DC

> Nota: esta página describe la formulación matemática con fines didácticos. La implementación computacional puede variar según el solver, el lenguaje de modelado y las simplificaciones adoptadas en clase.


## Idea del modelo

El modelo DC de expansión de transmisión incorpora flujos dependientes de diferencias angulares y susceptancias, representando una aproximación eléctrica lineal.

## Conjuntos e índices


- $n \in \mathcal{N}$: barras.
- $c=(i,j) \in \mathcal{C}$: corredores.


## Parámetros


- $B_c$: susceptancia del corredor.
- $F_c^{\max}$: límite por circuito.
- $IC_c$: costo de inversión.
- $n_c^0$: circuitos existentes.
- $\bar n_c$: máximo de candidatos.
- $M_c$: constante grande para formulaciones disyuntivas.


## Variables de decisión


- $x_c$: número de circuitos construidos.
- $f_c$: flujo activo.
- $\theta_n$: ángulo nodal.
- $P_g$: generación.


## Función objetivo


$$
\min \sum_c IC_c x_c + \sum_g c_gP_g
$$


## Restricciones principales


Balance nodal:

$$
\sum_{g\in\mathcal{G}_n}P_g-D_n=\sum_{c\in\delta^+(n)}f_c-\sum_{c\in\delta^-(n)}f_c
$$

Relación DC en corredores existentes:

$$
f_c=B_c n_c^0(\theta_i-\theta_j)
$$

Para candidatos, se puede usar una formulación disyuntiva o linealizada con Big-M:

$$
-M_c(1-y_c) \leq f_c - B_c(\theta_i-\theta_j) \leq M_c(1-y_c)
$$

Capacidad:

$$
-F_c^{\max}(n_c^0+x_c)\leq f_c\leq F_c^{\max}(n_c^0+x_c)
$$


## Interpretación de resultados


El resultado debe compararse con transporte para evidenciar cómo las leyes eléctricas cambian la expansión óptima.


## Actividad sugerida

Resolver o analizar el caso Garver con transporte y DC; identificar corredores que cambian entre formulaciones.
