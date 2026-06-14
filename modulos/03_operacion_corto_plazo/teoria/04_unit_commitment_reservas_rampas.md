# 4. Unit commitment, reservas y rampas

## Decisión adicional

En despacho económico simple se decide cuánto genera cada unidad. En unit commitment se decide además si la unidad está encendida o apagada:

\[
u_{g,t} \in \{0,1\}
\]

## Límites con variable binaria

\[
P_g^{min}u_{g,t} \leq P_{g,t} \leq P_g^{max}u_{g,t}
\]

Si \(u_{g,t}=0\), la potencia debe ser cero. Si \(u_{g,t}=1\), la unidad opera entre mínimo técnico y máximo.

## Arranque

Una variable de arranque \(v_{g,t}\) puede definirse como:

\[
v_{g,t} \geq u_{g,t}-u_{g,t-1}
\]

El costo de arranque entra en el objetivo:

\[
\sum_{g,t} C^{start}_g v_{g,t}
\]

## Reserva operativa

\[
\sum_g (P_g^{max}u_{g,t}-P_{g,t}) \geq R_t
\]

La reserva asegura capacidad disponible ante contingencias o errores de pronóstico.

## Rampas

\[
P_{g,t}-P_{g,t-1} \leq RU_g
\]

\[
P_{g,t-1}-P_{g,t} \leq RD_g
\]

## Lectura técnica

El UC puede encender unidades más caras antes de necesitarlas si se requiere reserva, se aproxima una rampa fuerte o se evita un arranque posterior costoso.
