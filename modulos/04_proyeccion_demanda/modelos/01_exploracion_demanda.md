# Flujo 01 — Exploración de demanda

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

Antes de proyectar, se deben revisar consistencia, tendencia, valores atípicos y relación entre energía y demanda pico.

## 2. Enunciado

Usando la serie histórica 2018–2024, construya gráficos de energía y pico, calcule tasas de crecimiento y verifique consistencia de datos.



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

### Datos históricos

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
\text{Diagnóstico}=\{tendencia,\ estacionalidad,\ atípicos,\ consistencia\}
$$

**Explicación de la función objetivo.** El objetivo no es optimizar, sino diagnosticar la calidad de datos y preparar la serie para modelos predictivos.

## 8. Restricciones del modelo

### Consistencia temporal

$$
T=\{2018,\ldots,2024\}
$$

**Explicación.** La serie debe tener periodos consecutivos sin duplicados.

### No negatividad

$$
Energy_t>0,\quad Peak_t>0
$$

**Explicación.** La energía y la demanda máxima deben ser positivas.

## 9. Guía para construir el archivo `.dat`

Este flujo no requiere archivo `.dat` de AMPL. La salida esperada es un archivo CSV que luego alimenta modelos de optimización.

## 10. Resultados esperados

Reporte de gráficos históricos, tasas de crecimiento y observaciones de calidad de datos.

## 11. Actividad asociada

[Actividad 04](../actividades/README.md)

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
