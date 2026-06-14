# 1. De una decisión técnica a un modelo matemático

## Idea central

Un modelo de optimización no empieza con una ecuación. Empieza con una decisión. En ingeniería eléctrica, una decisión puede ser cuánto generar, qué unidad encender, dónde construir una línea, qué tecnología instalar o qué demanda no servida penalizar.

La forma general de un problema de optimización es:

\[
\min_x f(x)
\]

sujeto a:

\[
g_i(x) \leq 0 \quad \forall i
\]

\[
h_j(x) = 0 \quad \forall j
\]

\[
x \in X
\]

## Lectura técnica

- \(x\): variables de decisión. Representan lo que el modelo puede elegir.
- \(f(x)\): función objetivo. Representa el criterio que se desea minimizar o maximizar.
- \(g_i(x)\): restricciones de desigualdad. Representan límites máximos, mínimos, capacidades, presupuestos o disponibilidad.
- \(h_j(x)\): restricciones de igualdad. Representan balances, conservación de flujo o ecuaciones físicas.
- \(X\): dominio. Define si las variables son continuas, enteras, binarias, no negativas o acotadas.

## Preguntas para formular correctamente

1. ¿Qué se decide?
2. ¿Qué criterio se optimiza?
3. ¿Qué datos son parámetros y no deben ser variables?
4. ¿Qué restricciones no pueden violarse?
5. ¿La solución debe ser continua, entera o binaria?
6. ¿Cómo se revisará si la solución tiene sentido?

## Ejemplo abstracto

Si se decide producir dos bienes \(x_1\) y \(x_2\), con utilidad \(p_1,p_2\), consumo de recursos \(a_{r1},a_{r2}\) y disponibilidad \(b_r\), el modelo puede escribirse como:

\[
\max \; p_1x_1+p_2x_2
\]

\[
a_{r1}x_1+a_{r2}x_2 \leq b_r \quad \forall r
\]

\[
x_1,x_2 \geq 0
\]

La misma estructura aparece luego en despacho de generación, transporte de energía, expansión de red y selección de tecnologías.
