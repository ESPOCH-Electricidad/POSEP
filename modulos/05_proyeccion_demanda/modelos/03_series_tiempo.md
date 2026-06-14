# Flujo 03 — Series temporales

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

Los modelos de series temporales usan la dependencia de la demanda con sus propios valores pasados.

## 2. Enunciado

Construya un pronóstico simple de energía anual y demanda pico usando rezagos temporales. Compare contra una línea base de crecimiento promedio.



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

### Serie temporal

| anio | energia_gwh | pico_mw |
| --- | --- | --- |
| 2018 | 25000 | 4200 |
| 2019 | 25800 | 4350 |
| 2020 | 25200 | 4280 |
| 2021 | 26800 | 4480 |
| 2022 | 27900 | 4650 |
| 2023 | 29100 | 4820 |
| 2024 | 30300 | 4990 |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| ŷ[t] | GWh o MW | valor estimado/proyectado |
| error[t] | GWh o MW | diferencia observada-estimada |

## 7. Función objetivo

$$
\min \sum_{t\in T}(D_t-\widehat{D}_t)^2
$$

**Explicación de la función objetivo.** Minimiza error de predicción sobre la serie temporal disponible.

## 8. Restricciones del modelo

### Modelo autoregresivo simple

$$
\widehat{D}_t=\alpha+\phi D_{t-1}
$$

**Explicación.** La demanda estimada depende del valor observado en el periodo anterior.

### Error

$$
e_t=D_t-\widehat{D}_t
$$

**Explicación.** Base para calcular métricas de validación.

## 9. Plantilla `.dat` sugerida

Este flujo no requiere archivo `.dat` de AMPL. La salida esperada es un archivo CSV que luego alimenta modelos de optimización.

## 10. Resultados esperados

Pronóstico, gráfico histórico-proyectado y métricas de validación.

## 11. Actividad asociada

[Actividad 04](../actividades/README.md)


## 12. Validación mínima

- Verifique que todas las unidades sean consistentes.
- Compruebe que todos los conjuntos usados en la formulación tengan datos.
- Revise que el balance principal cierre.
- Identifique restricciones activas.
- Compare el resultado contra una estimación manual simple.

## 13. Preguntas de análisis

1. ¿Qué restricción limita principalmente la solución?
2. ¿Qué parámetro tendría mayor impacto si cambia?
3. ¿El resultado es técnicamente razonable?
4. ¿Qué dato adicional se necesitaría para aplicar el modelo a un sistema real?

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
