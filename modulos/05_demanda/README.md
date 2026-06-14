[← Inicio](../../README.md) | [← Módulo anterior](../04_opf/README.md) | [Siguiente módulo →](../06_tnep/README.md)

# Módulo 05 — Proyección de demanda

## Objetivo

Construir insumos de demanda para operación, TNEP y GEP. El módulo distingue energía anual, potencia pico, factor de carga, variables explicativas y escenarios.

![Energía vs pico](figuras/01_energia_vs_pico.svg)

## Caso 1. Base histórica

### Datos completos

|   anio |   energia_gwh |   pico_mw |   poblacion_millones |   pib_indice |
|-------:|--------------:|----------:|---------------------:|-------------:|
|   2018 |         25000 |      4200 |                 16.9 |          100 |
|   2019 |         25800 |      4350 |                 17.1 |          101 |
|   2020 |         25200 |      4280 |                 17.3 |           96 |
|   2021 |         26800 |      4480 |                 17.5 |          100 |
|   2022 |         27900 |      4650 |                 17.7 |          104 |
|   2023 |         29100 |      4820 |                 17.9 |          107 |
|   2024 |         30300 |      4990 |                 18.1 |          110 |

### Cálculos

Demanda media anual:

$$
\bar{D}_y=\frac{E_y}{8760}
$$

Factor de carga:

$$
LF_y=\frac{\bar{D}_y}{D_y^{max}}
$$

Crecimiento compuesto:

$$
CAGR=\left(\frac{X_T}{X_0}\right)^{1/T}-1
$$

### Actividad

Calcule demanda media, factor de carga y crecimiento anual. Explique el efecto de la caída de demanda en 2020.

## Caso 2. Regresión con variables explicativas

Modelo:

$$
Y_t=\beta_0+\beta_1Pop_t+\beta_2PIB_t+\epsilon_t
$$

Use $Y_t$ como energía anual o potencia pico. Compare el ajuste contra CAGR.

## Caso 3. Escenarios

### Datos completos

|   anio | escenario   |   energia_gwh |   pico_mw |
|-------:|:------------|--------------:|----------:|
|   2025 | bajo        |         30900 |      5070 |
|   2025 | medio       |         31200 |      5120 |
|   2025 | alto        |         31600 |      5200 |
|   2030 | bajo        |         34000 |      5600 |
|   2030 | medio       |         35600 |      5850 |
|   2030 | alto        |         37400 |      6150 |
|   2035 | bajo        |         37200 |      6100 |
|   2035 | medio       |         40500 |      6650 |
|   2035 | alto        |         43800 |      7200 |

### Parámetros para modelos

$$
D_{y,s}^{peak},\qquad E_{y,s}
$$

### Actividad

Construya un archivo `.dat` con conjuntos $Y$ y $S$ para usar en expansión.

## Salida para TNEP

|   anio | escenario   |   pico_mw |
|-------:|:------------|----------:|
|   2025 | bajo        |      5070 |
|   2025 | medio       |      5120 |
|   2025 | alto        |      5200 |
|   2030 | bajo        |      5600 |
|   2030 | medio       |      5850 |
|   2030 | alto        |      6150 |
|   2035 | bajo        |      6100 |
|   2035 | medio       |      6650 |
|   2035 | alto        |      7200 |

## Salida para GEP

|   anio | escenario   |   energia_gwh |   pico_mw |
|-------:|:------------|--------------:|----------:|
|   2025 | bajo        |         30900 |      5070 |
|   2025 | medio       |         31200 |      5120 |
|   2025 | alto        |         31600 |      5200 |
|   2030 | bajo        |         34000 |      5600 |
|   2030 | medio       |         35600 |      5850 |
|   2030 | alto        |         37400 |      6150 |
|   2035 | bajo        |         37200 |      6100 |
|   2035 | medio       |         40500 |      6650 |
|   2035 | alto        |         43800 |      7200 |

## Entregables

1. Tabla histórica procesada.
2. Proyección por CAGR.
3. Proyección por regresión.
4. `.dat` de demanda para TNEP.
5. `.dat` de demanda para GEP.
