# 2. Modelos de proyección, escenarios y validación

## Modelo de regresión

\[
D_t = \beta_0 + \beta_1 PIB_t + \beta_2 Pob_t + \beta_3 Temp_t + \epsilon_t
\]

## Series de tiempo

Una serie de demanda puede tener tendencia, estacionalidad y ruido. Antes de usar modelos ARIMA/SARIMAX se debe revisar estacionariedad, rezagos y error de pronóstico.

## Métricas

\[
MAE = \frac{1}{n}\sum_t |D_t-\hat{D}_t|
\]

\[
RMSE = \sqrt{\frac{1}{n}\sum_t(D_t-\hat{D}_t)^2}
\]

\[
MAPE = \frac{100}{n}\sum_t \left|\frac{D_t-\hat{D}_t}{D_t}\right|
\]

## Escenarios

Un escenario bajo/base/alto no es solo una curva desplazada. Debe tener una justificación: crecimiento económico, electrificación, eficiencia, clima o política pública.
