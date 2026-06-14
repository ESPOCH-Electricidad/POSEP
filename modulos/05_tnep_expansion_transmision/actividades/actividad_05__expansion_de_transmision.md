# Actividad 05 — Expansión de transmisión

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Datos](../datos/) · [Guía AMPL](../../../docs/guia_ampl.md)

## Competencia

Formular un problema de expansión de transmisión con red existente, corredores candidatos, inversión binaria, balance nodal y límites de transferencia.

## Enunciado

Una red de cuatro barras debe atender demanda futura. Existen líneas en operación y corredores candidatos que pueden construirse una sola vez. Se debe decidir qué líneas candidatas instalar para minimizar inversión y energía no servida, respetando límites de generación y transmisión.

## Datos principales

Barras (`tnep_barras.csv`):

| Barra | Demanda [MW] | Generación máxima [MW] |
|---|---:|---:|
| B1 | 0 | 150 |
| B2 | 80 | 0 |
| B3 | 120 | 0 |
| B4 | 50 | 100 |

Corredores (`tnep_corredores.csv`): incluyen líneas existentes y candidatas, reactancia, límite, costo de inversión y máximo número de construcciones.

## Parte A — Modelo de transporte

Formule un modelo sin ángulos:

$$
\min \sum_{l\in C}IC_l y_l + VOLL\sum_i ENS_i
$$

$$
g_i+ENS_i-D_i=\sum_{l\in out(i)}f_l-\sum_{l\in in(i)}f_l
$$

$$
-F_l^{max}(existing_l+y_l)\leq f_l\leq F_l^{max}(existing_l+y_l)
$$

## Parte B — Modelo DC-TNEP

Agregue ángulos y relación DC para líneas existentes. Para candidatas, use una formulación con $M$:

$$
-M(1-y_l)\leq f_l-\frac{\theta_{from(l)}-\theta_{to(l)}}{x_l}\leq M(1-y_l)
$$

## Parte C — Escenarios de demanda

Use `tnep_anios.csv` para escalar la demanda por año. Resuelva 2025, 2030 y 2035. Compare si el plan de expansión cambia con el crecimiento.

## Tareas

1. Construya el `.dat` con barras, corredores, parámetros y años.
2. Implemente primero el modelo de transporte.
3. Implemente luego el modelo DC-TNEP.
4. Reporte líneas construidas, flujos, generación, ENS y costo.
5. Compare transporte vs DC y explique diferencias.
6. Aumente el costo de la línea C14 en 50 % y analice si cambia el plan.
7. Reduzca el VOLL a 300 USD/MWh y observe si el modelo prefiere no construir.

## Validación

- El balance debe cumplirse en cada barra.
- Las líneas no construidas no deben transportar flujo.
- Los límites de líneas existentes y candidatas construidas deben respetarse.
- La barra de referencia debe fijarse en el modelo DC.
- La energía no servida debe interpretarse como indicador de insuficiencia, no como solución deseable.

## Entregables

| Entregable | Contenido |
|---|---|
| Formulación | Transporte y DC-TNEP. |
| Archivos | `.mod`, `.dat`, `.run` para ambos modelos. |
| Resultados | Líneas construidas, flujos, generación y ENS. |
| Comparación | Transporte vs DC; base vs sensibilidad. |
| Figura | Red con líneas existentes, candidatas y seleccionadas. |

## Evaluación

| Criterio | Peso |
|---|---:|
| Formulación de inversión y flujo | 30 % |
| Implementación de variables binarias y big-M | 25 % |
| Validación de red y balances | 20 % |
| Sensibilidad e interpretación de plan | 15 % |
| Presentación de resultados | 10 % |
