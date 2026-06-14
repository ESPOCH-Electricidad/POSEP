# 1. Modelo transporte para TNEP

## Idea central

El modelo transporte ignora ángulos y leyes eléctricas, pero sirve como primera aproximación para asignar generación a cargas mediante corredores con capacidad.

## Decisión de inversión

\[
y_l \in \{0,1\}
\]

\(y_l=1\) si se construye el corredor candidato.

## Límite de flujo activado

\[
-F_l^{max}(n_l^0+y_l) \leq f_l \leq F_l^{max}(n_l^0+y_l)
\]

## Costo

\[
\min \sum_l C_l y_l + \sum_g c_g P_g + VOLL \sum_n LS_n
\]

## Lectura técnica

El modelo transporte puede subestimar necesidades reales de red porque no impone relaciones angulares. Su valor docente es introducir decisiones binarias de expansión y balance nodal antes del DC-TNEP.
