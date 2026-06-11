# Despacho hidrotérmico

> Nota: esta página describe la formulación matemática con fines didácticos. La implementación computacional puede variar según el solver, el lenguaje de modelado y las simplificaciones adoptadas en clase.


## Idea del modelo

Coordina generación térmica e hidroeléctrica considerando costos térmicos, disponibilidad de agua, evolución de embalses y restricciones de demanda.

## Conjuntos e índices


- $h \in \mathcal{H}$: centrales hidroeléctricas.
- $g \in \mathcal{G}$: centrales térmicas.
- $t \in \mathcal{T}$: periodos.


## Parámetros


- $D_t$: demanda.
- $C_g(P_{g,t})$: costo térmico.
- $A_{h,t}$: aportes hidráulicos.
- $V_h^{\min}, V_h^{\max}$: límites de volumen.
- $Q_h^{\min}, Q_h^{\max}$: límites de turbinamiento.
- $\eta_h$: productividad hídrica.


## Variables de decisión


- $P_{g,t}$: generación térmica.
- $P_{h,t}$: generación hidroeléctrica.
- $Q_{h,t}$: caudal turbinado.
- $S_{h,t}$: vertimiento.
- $V_{h,t}$: volumen almacenado.


## Función objetivo


$$
\min \sum_{t}\sum_g C_g(P_{g,t})
$$


## Restricciones principales


Balance eléctrico:

$$
\sum_g P_{g,t}+\sum_h P_{h,t}=D_t
$$

Relación producción-agua:

$$
P_{h,t}=\eta_h Q_{h,t}
$$

Balance hídrico:

$$
V_{h,t}=V_{h,t-1}+A_{h,t}-Q_{h,t}-S_{h,t}
$$

Límites de volumen y turbinamiento:

$$
V_h^{\min}\leq V_{h,t}\leq V_h^{\max}, \qquad Q_h^{\min}\leq Q_{h,t}\leq Q_h^{\max}
$$


## Interpretación de resultados


El resultado muestra cuándo conviene usar agua y cuándo reservarla. La interpretación debe considerar costo térmico, escasez hídrica y valor futuro del agua.


## Actividad sugerida

Comparar el despacho cuando los aportes hídricos se reducen en 20 %.
