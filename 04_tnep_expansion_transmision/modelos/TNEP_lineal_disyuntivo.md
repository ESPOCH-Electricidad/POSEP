# TNEP: modelo lineal disyuntivo

> Nota: esta página describe la formulación matemática con fines didácticos. La implementación computacional puede variar según el solver, el lenguaje de modelado y las simplificaciones adoptadas en clase.


## Idea del modelo

El modelo lineal disyuntivo usa variables binarias y restricciones Big-M para activar la relación DC solo cuando el circuito candidato se construye.

## Conjuntos e índices


- $c\in\mathcal{C}^K$: candidatos.
- $n\in\mathcal{N}$: barras.


## Parámetros


- $B_c$: susceptancia.
- $F_c^{\max}$: límite de flujo.
- $IC_c$: costo de inversión.
- $M_c$: constante Big-M.


## Variables de decisión


- $y_c\in\{0,1\}$: 1 si se construye el candidato.
- $f_c$: flujo por candidato.
- $\theta_n$: ángulo.


## Función objetivo


$$
\min \sum_{c\in\mathcal{C}^K}IC_c y_c + \sum_g c_gP_g
$$


## Restricciones principales


Activación de flujo DC:

$$
-M_c(1-y_c) \leq f_c - B_c(\theta_i-\theta_j) \leq M_c(1-y_c)
$$

Capacidad condicionada:

$$
-F_c^{\max}y_c \leq f_c \leq F_c^{\max}y_c
$$

Variable binaria:

$$
y_c\in\{0,1\}
$$


## Interpretación de resultados


Si $y_c=0$, el flujo del candidato queda forzado a cero. Si $y_c=1$, se activa la relación DC. La calidad del modelo depende de una elección adecuada de $M_c$.


## Errores frecuentes

- Usar un Big-M demasiado grande, generando relajaciones débiles.
- Usar un Big-M demasiado pequeño, eliminando soluciones factibles.
- No verificar físicamente la solución.
