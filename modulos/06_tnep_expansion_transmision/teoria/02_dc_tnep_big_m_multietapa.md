# 2. DC-TNEP, big-M y expansión multietapa

## Flujo DC en expansión

Para una línea existente:

\[
f_l = B_l(\theta_i-\theta_j)
\]

Para una línea candidata, la ecuación se activa solo si se construye:

\[
-M(1-y_l) \leq f_l-B_l(\theta_i-\theta_j) \leq M(1-y_l)
\]

## Límite térmico

\[
-F_l^{max}y_l \leq f_l \leq F_l^{max}y_l
\]

## Multietapa

En expansión multietapa, la inversión queda acumulada:

\[
y_{l,y} \geq y_{l,y-1}
\]

Una línea construida en un año permanece disponible en años posteriores.

## Lectura técnica

El big-M debe definirse de forma coherente con los límites físicos. Un M excesivo puede deteriorar el rendimiento del solver.
