# Flujo 04 — Escenarios y exportación

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

La planificación requiere escenarios de demanda futura. Este flujo genera archivos de salida para TNEP y GEP.

## 2. Enunciado

Construya escenarios bajo, medio y alto para 2025, 2030 y 2035. Exporte un archivo compatible con modelos de expansión.



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

### Demanda proyectada

| anio | escenario | energia_gwh | pico_mw |
| --- | --- | --- | --- |
| 2025 | bajo | 30900 | 5070 |
| 2025 | medio | 31200 | 5120 |
| 2025 | alto | 31600 | 5200 |
| 2030 | bajo | 34000 | 5600 |
| 2030 | medio | 35600 | 5850 |
| 2030 | alto | 37400 | 6150 |
| 2035 | bajo | 37200 | 6100 |
| 2035 | medio | 40500 | 6650 |
| 2035 | alto | 43800 | 7200 |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| ŷ[t] | GWh o MW | valor estimado/proyectado |
| error[t] | GWh o MW | diferencia observada-estimada |

## 7. Función objetivo

$$
D_{y,s}=D_y^{medio}(1+\delta_s)
$$

**Explicación de la función objetivo.** Define escenarios a partir de una trayectoria media y variaciones relativas.

## 8. Restricciones del modelo

### Escenario bajo

$$
\delta_{bajo}<0
$$

**Explicación.** Representa crecimiento conservador.

### Escenario medio

$$
\delta_{medio}=0
$$

**Explicación.** Representa trayectoria tendencial.

### Escenario alto

$$
\delta_{alto}>0
$$

**Explicación.** Representa crecimiento acelerado.

## 9. Guía para construir el archivo `.dat`

Este flujo no requiere archivo `.dat` de AMPL. La salida esperada es un archivo CSV que luego alimenta modelos de optimización.

## 10. Resultados esperados

Archivos `demanda_tnep.csv` y `demanda_gep.csv` con año, escenario, energía y pico.

## 11. Actividad asociada

[Actividad 04](../actividades/README.md)

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
