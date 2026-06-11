# Despacho económico con pérdidas

> Nota: esta página describe la formulación matemática con fines didácticos. La implementación computacional puede variar según el solver, el lenguaje de modelado y las simplificaciones adoptadas en clase.


## Idea del modelo

Extiende el ED incorporando pérdidas de transmisión. El balance exige que la generación cubra demanda más pérdidas.

## Conjuntos e índices


- $g \in \mathcal{G}$: generadores.


## Parámetros


- $D$: demanda total.
- $B_{gh}, B_{0g}, B_{00}$: coeficientes de pérdidas.
- $P_g^{\min}, P_g^{\max}$: límites de generación.
- $C_g(P_g)$: función de costo.


## Variables de decisión


- $P_g$: potencia generada.
- $P_L$: pérdidas totales del sistema, calculadas a partir de la generación.


## Función objetivo


$$
\min \sum_{g \in \mathcal{G}} C_g(P_g)
$$


## Restricciones principales


Pérdidas aproximadas:

$$
P_L = \sum_{g \in \mathcal{G}}\sum_{h \in \mathcal{G}} P_g B_{gh}P_h + \sum_{g \in \mathcal{G}} B_{0g}P_g + B_{00}
$$

Balance:

$$
\sum_{g \in \mathcal{G}} P_g = D + P_L
$$

Límites:

$$
P_g^{\min} \leq P_g \leq P_g^{\max}
$$


## Interpretación de resultados


El despacho cambia porque no todos los generadores afectan de la misma forma las pérdidas. El costo incremental debe corregirse mediante factores de penalización o sensibilidad de pérdidas.


## Errores frecuentes

- Suponer que el generador más barato siempre aumenta producción.
- Olvidar que las pérdidas dependen del punto de operación.
- Comparar con ED sin pérdidas sin revisar el balance.
