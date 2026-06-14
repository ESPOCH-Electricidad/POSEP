# 6. QP, NLP y condiciones KKT

## Programación cuadrática

Un problema QP tiene función objetivo cuadrática y restricciones lineales:

\[
\min \frac{1}{2}x^TQx+c^Tx
\]

\[
Ax \leq b
\]

Si \(Q\) es semidefinida positiva, el problema es convexo y cualquier óptimo local es global.

## Programación no lineal

Un problema NLP admite funciones no lineales en objetivo o restricciones:

\[
\min f(x)
\]

\[
g_i(x) \leq 0
\]

\[
h_j(x)=0
\]

En sistemas eléctricos, el OPF AC es un ejemplo típico por las ecuaciones no lineales de potencia activa y reactiva.

## Óptimo local y global

- Óptimo local: no existe un punto cercano con mejor valor objetivo.
- Óptimo global: no existe ningún punto factible con mejor valor objetivo.

En problemas no convexos, un solver puede entregar un óptimo local sin garantizar globalidad.

## Condiciones KKT

Para un problema diferenciable con restricciones:

\[
\mathcal{L}(x,\lambda,\mu)=f(x)+\sum_i \lambda_i g_i(x)+\sum_j \mu_j h_j(x)
\]

Las condiciones KKT incluyen:

1. Factibilidad primal.
2. Factibilidad dual: \(\lambda_i \geq 0\).
3. Complementariedad: \(\lambda_i g_i(x)=0\).
4. Estacionariedad: \(\nabla_x \mathcal{L}=0\).

## Conexión futura

- Despacho económico cuadrático: QP.
- OPF AC: NLP no lineal y potencialmente no convexo.
- Costos marginales: multiplicadores de balance.
- Límites activos: complementariedad y precios sombra.
