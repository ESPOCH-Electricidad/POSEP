# Actividad 02 — Operación de corto plazo

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Datos](../datos/) · [Guía AMPL](../../../docs/guia_ampl.md)

## Competencia

Formular, implementar y validar modelos de operación de corto plazo, distinguiendo despacho económico, costos por tramos, compromiso de unidades y operación hidrotérmica.

## Parte A — Despacho económico uninodal

Use `ed_generadores.csv` y `ed_demanda.csv`.

| Generador | $P^{min}$ [MW] | $P^{max}$ [MW] | Costo [USD/MWh] |
|---|---:|---:|---:|
| G1 | 20 | 100 | 15 |
| G2 | 30 | 80 | 22 |
| G3 | 0 | 60 | 35 |

Demanda: 150 MW.

Formule y resuelva:

$$
\min \sum_g c_g P_g
$$

$$
\sum_g P_g=D
$$

$$
P_g^{min}\leq P_g\leq P_g^{max}
$$

Debe reportar generación por unidad, costo total, unidad marginal y verificación de límites.

## Parte B — Despacho por tramos

Use `ed_tramos.csv` y `ed_tramos_demanda.csv`. Modele cada tramo como una variable $p_{g,k}$ limitada por `segmax_mw`.

Tareas:

1. Definir conjuntos de generadores y tramos.
2. Construir el parámetro de costo por generador-tramo.
3. Resolver el despacho con demanda de 170 MW.
4. Comparar el costo total con un despacho de costo promedio por generador.
5. Explicar por qué los tramos baratos se llenan antes que los caros.

## Parte C — Unit commitment

Use `uc_unidades.csv` y `uc_demanda_reserva.csv`. Formule un MILP con variables $u_{g,t}$ de encendido y $P_{g,t}$ de generación.

Incluya:

$$
P_g^{min}u_{g,t}\leq P_{g,t}\leq P_g^{max}u_{g,t}
$$

$$
\sum_g P_{g,t}=D_t
$$

$$
\sum_g(P_g^{max}u_{g,t}-P_{g,t})\geq R_t
$$

$$
P_{g,t}-P_{g,t-1}\leq RU_g
$$

Incluya costo de arranque mediante una variable binaria auxiliar si una unidad pasa de apagada a encendida.

## Parte D — Hidrotérmico simple

Use `hidrotermico_hidro.csv`, `hidrotermico_termicas.csv`, `hidrotermico_demanda_afluencia.csv` y `hidrotermico_voll.csv`.

Formule balance del embalse:

$$
S_{t+1}=S_t+I_t-Q_t-Sp_t
$$

Balance eléctrico:

$$
P_{h,t}+\sum_g P_{g,t}+ENS_t=D_t
$$

Límite hidroeléctrico:

$$
P_{h,t}=\rho Q_t
$$

## Sensibilidades obligatorias

1. Aumente la demanda de todas las horas en 10 %.
2. Duplique el VOLL y observe si cambia la energía no servida.
3. Reduzca el límite de turbinamiento hidroeléctrico en 20 %.

## Validación

- El balance de potencia debe cumplirse en cada hora.
- La reserva debe cumplirse en cada hora del UC.
- El almacenamiento hidroeléctrico debe permanecer entre mínimo y máximo.
- La energía no servida solo debe aparecer cuando sea más costosa o imposible atender demanda con los recursos disponibles.

## Entregables

| Entregable | Contenido |
|---|---|
| Formulación | ED, tramos, UC e hidrotérmico. |
| Archivos | `.mod`, `.dat`, `.run` para al menos ED y UC; modelo hidrotérmico como extensión. |
| Resultados | Generación, encendido, reserva, almacenamiento, costo. |
| Figura | Curva de demanda y generación por tecnología o estado de unidades. |
| Análisis | Comparación de caso base y sensibilidades. |

## Evaluación

| Criterio | Peso |
|---|---:|
| Formulación de balances y límites | 25 % |
| Implementación AMPL reproducible | 25 % |
| Validación técnica | 20 % |
| Sensibilidad e interpretación económica | 20 % |
| Presentación de resultados | 10 % |
