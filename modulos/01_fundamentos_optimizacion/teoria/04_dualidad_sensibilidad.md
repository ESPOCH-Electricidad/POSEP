# 4. Dualidad y sensibilidad

## Idea central

La dualidad permite interpretar el valor marginal de una restricción. En sistemas eléctricos, este concepto será esencial para entender costo marginal, precio sombra, congestión y valor de capacidad.

## Problema primal

\[
\min c^Tx
\]

\[
Ax \geq b
\]

\[
x \geq 0
\]

## Problema dual asociado

\[
\max b^T\lambda
\]

\[
A^T\lambda \leq c
\]

\[
\lambda \geq 0
\]

## Interpretación del multiplicador

El multiplicador dual \(\lambda_i\) mide cuánto cambia el valor óptimo si se relaja marginalmente el lado derecho de la restricción \(i\). De forma aproximada:

\[
\Delta z^* \approx \lambda_i \Delta b_i
\]

## Lectura técnica

- Si una restricción no está activa, normalmente su multiplicador es cero.
- Si una restricción está activa, su multiplicador puede indicar escasez.
- Un multiplicador alto no significa error; puede indicar que un recurso limitante tiene alto valor marginal.

## Ejemplo conceptual

Si una restricción de capacidad limita generación barata, su precio sombra indica cuánto disminuiría el costo total si se incrementa esa capacidad en una unidad. Esta idea se usará después en OPF y expansión.

## Precaución

La sensibilidad local es válida alrededor del punto óptimo y dentro del rango en que no cambia la base óptima ni la estructura discreta del problema. En MILP, la interpretación dual es más delicada porque las variables binarias introducen discontinuidades.
