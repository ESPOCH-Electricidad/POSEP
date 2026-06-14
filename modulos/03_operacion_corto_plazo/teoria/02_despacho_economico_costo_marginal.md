# 2. Despacho económico y costo marginal

## Problema básico

Dada una demanda \(D_t\), se decide la potencia \(P_{g,t}\) de cada generador para minimizar el costo operativo:

\[
\min \sum_{t \in T}\sum_{g \in G} c^{var}_g P_{g,t}
\]

sujeto a:

\[
\sum_{g \in G} P_{g,t}=D_t \quad \forall t
\]

\[
P_g^{min} \leq P_{g,t} \leq P_g^{max} \quad \forall g,t
\]

## Orden de mérito

Si no hay red, rampas ni mínimos técnicos, las unidades se ordenan por \(c^{var}_g\). La demanda se cubre primero con las unidades más baratas. La unidad parcialmente cargada en el margen determina el costo marginal del sistema.

## Costo marginal

El costo marginal corresponde al costo de abastecer un MWh adicional en el periodo considerado. En un modelo lineal sin congestión y sin pérdidas, coincide con el costo variable de la unidad marginal.

## Interpretación del multiplicador de balance

Si \(\lambda_t\) es el multiplicador dual del balance:

\[
\sum_g P_{g,t}=D_t
\]

entonces \(\lambda_t\) representa la variación del costo total óptimo ante un incremento marginal de demanda en \(t\).

## Validación

Después de resolver:

- comprobar que la suma de generación iguala la demanda;
- revisar que ninguna unidad exceda \(P^{max}\);
- identificar unidad marginal;
- comparar costo total con cálculo manual por orden de mérito.
