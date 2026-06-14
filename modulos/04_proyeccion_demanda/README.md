# 04 — Proyección de demanda eléctrica

[Menú principal](../../README.md) · [Actividades](actividades/README.md) · [Datos](datos/)

## Introducción conceptual

La proyección de demanda se introduce después de operación y OPF porque hasta ese punto la demanda se usa como parámetro. En planificación, la demanda futura se convierte en insumo estratégico para TNEP y GEP.

## Fundamentos del tema

El módulo se desarrolla principalmente en Python: limpieza de datos, visualización, regresión, series temporales, métricas de error, construcción de escenarios y exportación hacia modelos de optimización.

## Figuras técnicas principales

![Energía vs demanda pico](figuras/01_energia_vs_pico.svg)

Dos variables distintas para planificación

![Tendencia y estacionalidad](figuras/02_tendencia_estacionalidad.svg)

Componentes de una serie de demanda

![Validación de modelos](figuras/03_metricas_validacion.svg)

Medidas de error para comparar proyecciones

![Escenarios de demanda](figuras/04_escenarios_demanda.svg)

Incertidumbre para planificación

## Ecuaciones base

### MAE

$$
MAE=\frac{1}{n}\sum_{t=1}^{n}|D_t-\hat{D}_t|
$$

Error absoluto medio.

### RMSE

$$
RMSE=\sqrt{\frac{1}{n}\sum_{t=1}^{n}(D_t-\hat{D}_t)^2}
$$

Penaliza errores grandes.

### MAPE

$$
MAPE=\frac{100}{n}\sum_{t=1}^{n}\left|\frac{D_t-\hat{D}_t}{D_t}\right|
$$

Error porcentual medio.

### Escenario

$$
D_y^{alto}=D_y^{medio}(1+\Delta_y)
$$

Construcción simple de escenario alto.

## Ejemplos o modelos del módulo

| Recurso | Qué aporta | Acceso |
|---|---|---|
| Exploración de demanda | limpieza y visualización en Python | [Abrir](modelos/01_exploracion_demanda.md) |
| Regresión de demanda | demanda vs variables explicativas | [Abrir](modelos/02_regresion_demanda.md) |
| Series temporales | ARIMA/SARIMAX | [Abrir](modelos/03_series_tiempo.md) |
| Escenarios y exportación | demanda para AMPL | [Abrir](modelos/04_escenarios_exportacion.md) |


## Capa de datos de la v14

Las páginas de ejemplos/modelos del módulo incluyen datos suficientes para construir archivos de datos de trabajo. En los modelos AMPL se incluye una plantilla `.dat` sugerida en el propio README del modelo; en el módulo de demanda se especifican plantillas CSV para Python y archivos de salida hacia TNEP/GEP.

## Actividad del módulo

Revise [actividades/README.md](actividades/README.md) y desarrolle la actividad principal: **Actividad 04 — Proyección de demanda**.

---

[Menú principal](../../README.md) · [Actividades](actividades/README.md) · [Datos](datos/)
