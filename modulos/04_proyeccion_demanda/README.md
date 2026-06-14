# 04 — Proyección de demanda eléctrica

[Menú principal](../../README.md) · [Modelos](modelos/README.md) · [Actividades](actividades/README.md) · [Datos](datos/)

## Propósito del módulo

La demanda es el insumo que conecta la operación con la planificación. Un modelo de expansión no decide correctamente si la demanda futura está mal construida. Por eso no basta con extrapolar una serie: se debe distinguir energía anual, demanda pico, perfil horario, estacionalidad, crecimiento económico, escenarios e incertidumbre.

## Energía y demanda pico

La energía anual mide consumo acumulado; la demanda pico dimensiona capacidad, red y reserva. Dos sistemas pueden tener la misma energía anual y demandas pico diferentes si sus perfiles horarios son distintos. El factor de carga resume esta relación:

$$
LF=\frac{E}{D^{max}\,8760}
$$

![Energía y pico](figuras/01_energia_vs_pico.svg)

Un factor de carga bajo indica que la infraestructura se dimensiona para pocas horas críticas. En planificación, eso puede justificar tecnologías de punta, almacenamiento, gestión de demanda o refuerzos de red.

## Tendencia, estacionalidad y variables explicativas

La demanda eléctrica responde a crecimiento poblacional, actividad económica, clima, eficiencia, electrificación y cambios tarifarios. Una proyección útil debe separar tendencia de variaciones transitorias. Una forma simple es:

$$
D_y = \alpha + \beta_1 Pop_y + \beta_2 GDP_y + \varepsilon_y
$$

También puede usarse crecimiento compuesto:

$$
D_y = D_0(1+g)^{y-y_0}
$$

![Tendencia y estacionalidad](figuras/02_tendencia_estacionalidad.svg)

## Métricas de validación

La calidad de una proyección se evalúa comparando valores estimados y observados. Las métricas más usadas son:

$$
MAE=\frac{1}{n}\sum_t |D_t-\hat{D}_t|
$$

$$
RMSE=\sqrt{\frac{1}{n}\sum_t(D_t-\hat{D}_t)^2}
$$

$$
MAPE=\frac{100}{n}\sum_t \left|\frac{D_t-\hat{D}_t}{D_t}\right|
$$

![Métricas de validación](figuras/03_metricas_validacion.svg)

## Escenarios para planificación

El resultado de demanda debe entregarse como escenario bajo, medio y alto, porque TNEP y GEP necesitan evaluar sensibilidad de inversión. La demanda media puede ser coherente con tendencia histórica; la alta puede representar electrificación acelerada o crecimiento económico mayor; la baja puede representar eficiencia energética o menor actividad.

![Escenarios de demanda](figuras/04_escenarios_demanda.svg)

## Modelos del módulo

| Recurso | Uso | Acceso |
|---|---|---|
| Exploración de demanda | Energía, pico, factor de carga | [Abrir](modelos/01_exploracion_demanda.md) |
| Regresión | Proyección con variables explicativas | [Abrir](modelos/02_regresion_demanda.md) |
| Series de tiempo | Tendencia histórica y predicción | [Abrir](modelos/03_series_tiempo.md) |
| Escenarios y exportación | Preparación para TNEP y GEP | [Abrir](modelos/04_escenarios_exportacion.md) |

## Actividad

La actividad exige construir una proyección con datos históricos, justificar escenarios y generar archivos de salida para los módulos de expansión.

[Ir a la actividad](actividades/actividad_04__proyeccion_de_demanda.md)

---

[Menú principal](../../README.md) · [Modelos](modelos/README.md) · [Actividades](actividades/README.md) · [Datos](datos/)
