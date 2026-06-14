# 3. Costos cuadráticos y aproximación por tramos

## Costos cuadráticos

En despacho económico clásico, el costo de una unidad puede aproximarse como:

\[
C_g(P_g)=a_g+b_gP_g+c_gP_g^2
\]

El costo incremental es:

\[
MC_g(P_g)=\frac{dC_g}{dP_g}=b_g+2c_gP_g
\]

## Condición económica sin pérdidas

Si ninguna unidad está en límite, el óptimo cumple:

\[
MC_1(P_1)=MC_2(P_2)=\cdots=MC_g(P_g)=\lambda
\]

## Aproximación por tramos

Para resolver con LP/MILP, un costo no lineal puede aproximarse mediante bloques:

\[
P_g = P_g^{min}u_g + \sum_{k \in K_g} p_{g,k}
\]

\[
0 \leq p_{g,k} \leq \overline{p}_{g,k}
\]

\[
C_g \approx C_g^{min}u_g + \sum_{k \in K_g} c_{g,k}p_{g,k}
\]

## Lectura técnica

La aproximación por tramos permite representar curvas convexas con un modelo lineal. Es útil para introducir costos crecientes sin pasar a QP/NLP.
