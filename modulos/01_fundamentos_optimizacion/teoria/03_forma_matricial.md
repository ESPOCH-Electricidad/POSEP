# 3. Forma matricial

## Motivación

Un modelo algebraico con muchos índices se convierte internamente en una matriz que el solver procesa. Entender la forma matricial ayuda a depurar modelos AMPL y a reconocer problemas de dimensión, signos y unidades.

## Forma general

\[
\min c^Tx
\]

\[
Ax=b
\]

\[
l \leq x \leq u
\]

donde:

- \(A\) contiene coeficientes tecnológicos.
- \(x\) contiene todas las variables del modelo.
- \(b\) contiene términos independientes.
- \(l,u\) contienen límites inferiores y superiores.

## Ejemplo de balance

Considere tres generadores y una demanda total:

\[
P_1+P_2+P_3=D
\]

En forma matricial:

\[
\begin{bmatrix}1 & 1 & 1\end{bmatrix}
\begin{bmatrix}P_1\\P_2\\P_3\end{bmatrix}=D
\]

Si además existen límites:

\[
0 \leq P_g \leq \overline{P}_g
\]

el solver no ve una frase eléctrica; ve una matriz, vectores y cotas.

## Relación con AMPL

La restricción:

```ampl
subject to Balance {t in T}:
    sum {g in G} Pg[g,t] = demand[t];
```

crea una fila de matriz por cada periodo \(t\). Cada variable \(Pg[g,t]\) asociada a ese periodo entra con coeficiente 1.
