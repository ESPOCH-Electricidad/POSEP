# 1. OPF DC y balance nodal

## Supuestos del flujo DC

El flujo DC se basa en tres simplificaciones principales:

1. magnitudes de tensión cercanas a 1 p.u.;
2. diferencias angulares pequeñas;
3. resistencia despreciable frente a reactancia.

## Flujo por línea

Para una línea \((i,j)\):

\[
f_{ij}=B_{ij}(\theta_i-\theta_j)
\]

## Balance nodal

\[
\sum_{g \in G_i} P_{g,t} - D_{i,t} = \sum_{j:(i,j)\in L} f_{ij,t}
\]

La generación neta en el nodo debe igualar el flujo neto que sale por las líneas.

## Referencia angular

Para evitar infinitas soluciones equivalentes, se fija un ángulo de referencia:

\[
\theta_{ref,t}=0
\]

## Límites térmicos

\[
-F_{ij}^{max} \leq f_{ij,t} \leq F_{ij}^{max}
\]

Si una línea alcanza el límite, puede aparecer congestión y el costo marginal puede diferir entre nodos.
