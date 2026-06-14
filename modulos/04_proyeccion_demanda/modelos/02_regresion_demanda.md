# Flujo 02 — Regresión de demanda

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

La regresión permite estimar demanda a partir de variables explicativas como población, PIB o número de clientes.

## 2. Enunciado

Ajuste un modelo de regresión para energía anual usando población y PIB como variables explicativas. Compare valores observados y estimados.



> Este flujo se resuelve en Python. No se entrega `.dat` de AMPL; se entrega CSV de proyección para alimentar modelos de expansión.


## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| T | periodos históricos |
| Y | años de proyección |
| S | escenarios |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| Energy[t] | GWh | energía histórica |
| Peak[t] | MW | demanda máxima histórica |
| GDP[t] | índice | variable explicativa |
| Population[t] | millones | variable explicativa |

## 5. Datos completos para construir el archivo de datos

### Datos de regresión

| anio | energia_gwh | pico_mw | poblacion_millones | pib_indice |
| --- | --- | --- | --- | --- |
| 2018 | 25000 | 4200 | 16.9 | 100 |
| 2019 | 25800 | 4350 | 17.1 | 101 |
| 2020 | 25200 | 4280 | 17.3 | 96 |
| 2021 | 26800 | 4480 | 17.5 | 100 |
| 2022 | 27900 | 4650 | 17.7 | 104 |
| 2023 | 29100 | 4820 | 17.9 | 107 |
| 2024 | 30300 | 4990 | 18.1 | 110 |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| ŷ[t] | GWh o MW | valor estimado/proyectado |
| error[t] | GWh o MW | diferencia observada-estimada |

## 7. Función objetivo

$$
\min_{\beta}\sum_{t\in T}(Energy_t-\beta_0-\beta_1Population_t-\beta_2GDP_t)^2
$$

**Explicación de la función objetivo.** Minimiza la suma de errores cuadráticos entre energía observada y energía estimada por el modelo lineal.

## 8. Restricciones del modelo

### Ecuación estimada

$$
\widehat{Energy}_t=\beta_0+\beta_1Population_t+\beta_2GDP_t
$$

**Explicación.** Relaciona demanda con variables socioeconómicas.

### Validación

$$
error_t=Energy_t-\widehat{Energy}_t
$$

**Explicación.** Permite calcular MAE, RMSE y MAPE.

## 9. Guía para construir el archivo `.dat`

Este flujo no requiere archivo `.dat` de AMPL. La salida esperada es un archivo CSV que luego alimenta modelos de optimización.

## 10. Resultados esperados

Coeficientes estimados, errores, gráfico observado-estimado y proyección preliminar.

## 11. Actividad asociada

[Actividad 04](../actividades/README.md)

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
