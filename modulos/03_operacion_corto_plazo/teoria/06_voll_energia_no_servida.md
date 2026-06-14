# 6. VOLL y energía no servida

## Motivación

Un modelo de operación puede volverse infactible si la demanda supera la capacidad disponible. Para mantener factibilidad y cuantificar el costo social del déficit, se introduce energía no servida.

## Balance con déficit

\[
\sum_g P_{g,t} + LS_t = D_t
\]

\(LS_t\) representa carga no servida.

## Penalización con VOLL

\[
\min C + \sum_t VOLL \cdot LS_t
\]

El VOLL debe ser suficientemente alto para que el modelo use déficit solo cuando no existan alternativas razonables.

## Lectura técnica

- Si \(LS_t>0\), revisar si es por falta real de capacidad, límites de rampa, mínimo técnico, restricciones de red o datos mal ingresados.
- Un VOLL demasiado bajo puede hacer que el modelo prefiera racionar en lugar de despachar generación costosa.
- Un VOLL demasiado alto puede crear problemas numéricos si se mezcla con costos muy pequeños.
