# 2. Programación lineal

## Definición

La programación lineal estudia problemas donde la función objetivo y todas las restricciones son lineales. En forma compacta:

\[
\min c^T x
\]

sujeto a:

\[
Ax \leq b
\]

\[
x \geq 0
\]

## Interpretación de los términos

- \(c\): vector de costos, utilidades o penalizaciones.
- \(A\): matriz tecnológica. Cada fila representa una restricción y cada columna una variable.
- \(b\): recursos disponibles, demandas, capacidades o límites.
- \(x\): decisiones continuas.

## Región factible

La región factible es el conjunto de puntos que cumplen simultáneamente todas las restricciones. Si la región está vacía, el problema es infactible. Si la función objetivo puede mejorar indefinidamente, el problema es no acotado.

En programación lineal, si existe una solución óptima finita, al menos un óptimo se encuentra en un vértice de la región factible. Este resultado justifica el método simplex y también explica por qué restricciones activas determinan la solución.

## Restricción activa

Una restricción está activa cuando se cumple con igualdad en la solución óptima:

\[
a_i^Tx^* = b_i
\]

Una restricción no activa tiene holgura:

\[
a_i^Tx^* < b_i
\]

## Ejemplo mínimo

\[
\max 40x_1+30x_2
\]

\[
2x_1+x_2 \leq 100
\]

\[
x_1+x_2 \leq 80
\]

\[
x_1,x_2 \geq 0
\]

La lectura técnica es que \(x_1\) y \(x_2\) son decisiones, las restricciones limitan recursos y la función objetivo mide beneficio. No se debe resolver mecánicamente sin interpretar unidades.

## Errores frecuentes

- Mezclar parámetros y variables.
- Usar restricciones sin unidad consistente.
- Formular una igualdad cuando corresponde una desigualdad.
- No acotar variables que físicamente tienen límite.
- Maximizar beneficios cuando en realidad se quiere minimizar costos, sin cambiar signos correctamente.
