# Actividad 03 — Flujo óptimo de potencia DC

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Datos](../datos/) · [Guía AMPL](../../../docs/guia_ampl.md)

## Competencia

Formular un OPF DC con balance nodal, flujo por diferencias angulares y límites térmicos, interpretando congestión y costo marginal por ubicación.

## Enunciado

Se dispone de una red de tres barras, tres líneas y dos generadores. Se debe determinar el despacho de mínimo costo que atiende la demanda respetando los límites de la red.

## Datos principales

Barras (`opf_dc_barras.csv`):

| Barra | Demanda [MW] |
|---|---:|
| B1 | 0 |
| B2 | 90 |
| B3 | 80 |

Generadores (`opf_dc_generadores.csv`):

| Generador | Barra | $P^{min}$ [MW] | $P^{max}$ [MW] | Costo [USD/MWh] |
|---|---|---:|---:|---:|
| G1 | B1 | 0 | 160 | 18 |
| G2 | B3 | 0 | 100 | 32 |

Líneas (`opf_dc_lineas.csv`):

| Línea | Desde | Hasta | x [p.u.] | Fmax [MW] |
|---|---|---|---:|---:|
| L12 | B1 | B2 | 0.10 | 100 |
| L23 | B2 | B3 | 0.08 | 80 |
| L13 | B1 | B3 | 0.12 | 60 |

## Formulación mínima

Variables: generación $P_g$, ángulo $\theta_i$, flujo $F_l$ y opcionalmente energía no servida $ENS_i$.

Objetivo:

$$
\min \sum_g c_gP_g + VOLL\sum_i ENS_i
$$

Balance nodal:

$$
\sum_{g\in G_i}P_g + ENS_i - D_i = \sum_{l\in L_i^{out}}F_l-\sum_{l\in L_i^{in}}F_l
$$

Flujo DC:

$$
F_l=\frac{\theta_{from(l)}-\theta_{to(l)}}{x_l}
$$

Límites:

$$
-F_l^{max}\leq F_l\leq F_l^{max}
$$

Referencia:

$$
\theta_{B1}=0
$$

## Tareas

1. Construya el `.dat` con conjuntos `BUS`, `GEN` y `LINE`.
2. Implemente el OPF DC en AMPL.
3. Reporte generación, ángulos, flujos y costo total.
4. Identifique líneas congestionadas.
5. Compare con un despacho uninodal sin límites de red.
6. Reduzca el límite de L13 a 40 MW y compare.
7. Aumente el costo de G2 a 45 USD/MWh y analice si cambia el despacho.

## Validación

- El balance debe cumplirse en cada barra.
- El flujo calculado debe coincidir con la diferencia angular dividida para la reactancia.
- Ninguna línea debe superar su límite.
- El signo del flujo debe interpretarse con la dirección definida en los datos.

## Entregables

- Formulación completa del OPF DC.
- Archivos `.mod`, `.dat` y `.run`.
- Tabla de generación, flujos y ángulos.
- Gráfico de red con flujos o tabla clara por línea.
- Comparación caso base, límite reducido y costo modificado.
- Conclusión sobre congestión.

## Evaluación

| Criterio | Peso |
|---|---:|
| Balance nodal y flujo DC correctamente formulados | 35 % |
| Implementación y datos | 25 % |
| Identificación de congestión | 15 % |
| Sensibilidad y comparación con despacho uninodal | 15 % |
| Presentación técnica | 10 % |
