# Flujo óptimo de potencia AC (AC-OPF)

> Nota: esta página describe la formulación matemática con fines didácticos. La implementación computacional puede variar según el solver, el lenguaje de modelado y las simplificaciones adoptadas en clase.


## Idea del modelo

El AC-OPF minimiza costos operativos respetando las ecuaciones no lineales de flujo de potencia, límites de tensión, generación activa/reactiva y capacidad de ramas.

## Conjuntos e índices


- $n,m \in \mathcal{N}$: barras.
- $\ell=(n,m) \in \mathcal{L}$: líneas.
- $g \in \mathcal{G}_n$: generadores ubicados en barra $n$.


## Parámetros


- $P_n^D, Q_n^D$: demanda activa y reactiva.
- $G_{nm}, B_{nm}$: elementos de la matriz de admitancia.
- $V_n^{\min}, V_n^{\max}$: límites de magnitud de tensión.
- $P_g^{\min}, P_g^{\max}, Q_g^{\min}, Q_g^{\max}$: límites de generación.
- $S_\ell^{\max}$: límite aparente de línea.


## Variables de decisión


- $P_g, Q_g$: generación activa y reactiva.
- $V_n$: magnitud de tensión.
- $\theta_n$: ángulo de tensión.


## Función objetivo


$$
\min \sum_g C_g(P_g)
$$


## Restricciones principales


Balance activo:

$$
\sum_{g\in\mathcal{G}_n}P_g-P_n^D = V_n\sum_{m\in\mathcal{N}}V_m\left(G_{nm}\cos\theta_{nm}+B_{nm}\sin\theta_{nm}\right)
$$

Balance reactivo:

$$
\sum_{g\in\mathcal{G}_n}Q_g-Q_n^D = V_n\sum_{m\in\mathcal{N}}V_m\left(G_{nm}\sin\theta_{nm}-B_{nm}\cos\theta_{nm}\right)
$$

Límites:

$$
V_n^{\min}\leq V_n\leq V_n^{\max}
$$

$$
P_g^{\min}\leq P_g\leq P_g^{\max}, \qquad Q_g^{\min}\leq Q_g\leq Q_g^{\max}
$$

$$
|S_\ell|\leq S_\ell^{\max}
$$


## Interpretación de resultados


El AC-OPF es no lineal y no convexo. Es más realista que el DC-OPF, pero más difícil de resolver. Permite analizar tensiones, reactivos y límites aparentes.


## Errores frecuentes

- Tratar el AC-OPF como lineal.
- Comparar directamente resultados AC y DC sin revisar supuestos.
- Ignorar límites reactivos.
