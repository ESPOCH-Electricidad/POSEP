# TNEP: modelo híbrido

> Nota: esta página describe la formulación matemática con fines didácticos. La implementación computacional puede variar según el solver, el lenguaje de modelado y las simplificaciones adoptadas en clase.


## Idea del modelo

El modelo híbrido combina una representación eléctrica más estricta para la red existente con una representación relajada para candidatos, reduciendo complejidad sin perder toda la información física.

## Conjuntos e índices


- $\mathcal{C}^E$: corredores existentes.
- $\mathcal{C}^K$: corredores candidatos.
- $n \in \mathcal{N}$: barras.


## Parámetros


- $B_c$: susceptancia.
- $F_c^{\max}$: capacidad.
- $IC_c$: costo de inversión de candidatos.
- $D_n$: demanda.


## Variables de decisión


- $f_c$: flujo.
- $\theta_n$: ángulo.
- $x_c$: circuitos candidatos construidos.
- $P_g$: generación.


## Función objetivo


$$
\min \sum_{c\in\mathcal{C}^K}IC_cx_c + \sum_g c_gP_g
$$


## Restricciones principales


Para corredores existentes:

$$
f_c = B_c n_c^0(\theta_i-\theta_j) \qquad \forall c\in\mathcal{C}^E
$$

Para corredores candidatos puede mantenerse una restricción de capacidad tipo transporte:

$$
-F_c^{\max}x_c\leq f_c\leq F_c^{\max}x_c \qquad \forall c\in\mathcal{C}^K
$$

Se mantiene balance nodal y límites de generación.


## Interpretación de resultados


Sirve para discutir compromisos entre realismo físico, complejidad computacional y calidad de la solución.


## Actividad sugerida

Comparar el tiempo de solución y el plan de expansión frente al modelo DC completo.
