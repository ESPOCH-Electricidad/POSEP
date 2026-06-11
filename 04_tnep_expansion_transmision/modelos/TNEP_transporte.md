# TNEP: modelo de transporte

> Nota: esta página describe la formulación matemática con fines didácticos. La implementación computacional puede variar según el solver, el lenguaje de modelado y las simplificaciones adoptadas en clase.


## Idea del modelo

El modelo de transporte decide nuevos circuitos de transmisión usando balance nodal y límites de capacidad, pero sin imponer leyes de Kirchhoff sobre ángulos de fase.

## Conjuntos e índices


- $n \in \mathcal{N}$: barras.
- $c=(i,j) \in \mathcal{C}$: corredores existentes o candidatos.
- $g \in \mathcal{G}_n$: generadores en barra $n$.


## Parámetros


- $D_n$: demanda.
- $P_g^{\max}$: capacidad de generación.
- $F_c^{\max}$: capacidad por circuito.
- $n_c^0$: circuitos existentes.
- $\bar n_c$: máximo de nuevos circuitos.
- $IC_c$: costo de inversión por circuito.


## Variables de decisión


- $P_g$: generación.
- $f_c$: flujo por corredor.
- $x_c \in \mathbb{Z}_+$: número de circuitos nuevos.


## Función objetivo


$$
\min \sum_{c\in\mathcal{C}} IC_c x_c + \sum_g c_g P_g
$$


## Restricciones principales


Balance nodal:

$$
\sum_{g\in\mathcal{G}_n}P_g - D_n = \sum_{c\in\delta^+(n)}f_c - \sum_{c\in\delta^-(n)}f_c
$$

Capacidad del corredor:

$$
-F_c^{\max}(n_c^0+x_c)\leq f_c\leq F_c^{\max}(n_c^0+x_c)
$$

Límites de construcción:

$$
0\leq x_c\leq \bar n_c, \qquad x_c\in\mathbb{Z}_+
$$


## Interpretación de resultados


Es útil como primera aproximación porque puede identificar corredores necesarios, pero puede producir soluciones no factibles bajo leyes eléctricas DC/AC.


## Errores frecuentes

- Interpretar factibilidad de transporte como factibilidad eléctrica completa.
- Ignorar que no se imponen ángulos.
- Usar sus resultados finales sin validación DC o AC.
