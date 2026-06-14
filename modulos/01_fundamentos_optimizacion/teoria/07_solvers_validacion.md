# 7. Solvers, estados de solución y validación

## Modelador vs solver

AMPL, GAMS o Pyomo son modeladores. CPLEX, Gurobi, HiGHS, IPOPT o KNITRO son solvers. El modelador traduce ecuaciones algebraicas a una estructura que el solver puede resolver.

## Tipos de problemas y solvers típicos

| Tipo | Estructura | Solvers frecuentes |
|---|---|---|
| LP | lineal continuo | HiGHS, CPLEX, Gurobi |
| MILP | lineal con enteras/binarias | CPLEX, Gurobi, CBC, HiGHS |
| QP | objetivo cuadrático | CPLEX, Gurobi, Mosek |
| NLP | restricciones u objetivo no lineal | IPOPT, KNITRO |
| MINLP | no lineal con enteras | Bonmin, Couenne, SCIP, Knitro |

## Estados de solución

- `optimal`: se encontró solución óptima bajo tolerancias.
- `infeasible`: no existe solución que cumpla todas las restricciones.
- `unbounded`: el objetivo puede mejorar sin límite.
- `locally optimal`: óptimo local en problemas no lineales.
- `time limit`: se alcanzó límite de tiempo; revisar gap y factibilidad.

## Validación mínima

Después de resolver, siempre revisar:

1. Balance de igualdad.
2. Límites de variables.
3. Restricciones activas.
4. Unidades de los resultados.
5. Valor de la función objetivo.
6. Variables binarias con valores 0/1.
7. Sensibilidad ante cambios razonables de datos.

## Regla de ingeniería

Un resultado óptimo no necesariamente es un resultado correcto. La formulación, los datos y la interpretación deben validarse técnicamente.
