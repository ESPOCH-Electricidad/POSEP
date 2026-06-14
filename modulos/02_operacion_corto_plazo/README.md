# 02 — Operación de corto plazo

[Menú principal](../../README.md) · [Modelos](modelos/README.md) · [Actividades](actividades/README.md) · [Datos](datos/) · [Guía AMPL](../../docs/guia_ampl.md)

## Propósito del módulo

La operación de corto plazo decide cómo utilizar los recursos disponibles para atender la demanda hora a hora. En este horizonte, la capacidad instalada ya existe y la pregunta central es cuánto debe generar cada unidad, qué unidades deben estar encendidas y cómo se usa el agua almacenada sin comprometer periodos futuros.

La demanda se trata como dato operativo. Las decisiones se organizan alrededor de costos variables, límites de generación, reservas, rampas, mínimos técnicos, arranques y balances de energía.

![Demanda y reserva](figuras/01_curva_demanda_reserva.svg)

## Costo variable y costo marginal

En despacho económico, el costo relevante de corto plazo es el costo variable. Para una unidad térmica puede expresarse como:

$$
c_g^{var}=HR_g p_g^{fuel}+c_g^{VOM}+EF_g p^{CO_2}
$$

El término $HR_g p_g^{fuel}$ convierte combustible en costo por MWh eléctrico; $c_g^{VOM}$ representa operación y mantenimiento variable; y $EF_g p^{CO_2}$ internaliza el costo de emisiones si existe una señal de carbono.

Si los costos son lineales, el despacho se ordena por mérito: primero generan las unidades de menor costo variable hasta cubrir la demanda. La unidad que atiende el último MW define el costo marginal del sistema en un modelo uninodal sin congestión.

![Orden de mérito y costo marginal](figuras/02_orden_merito_costo_marginal.svg)

## Despacho económico lineal

La formulación básica es:

$$
\min \sum_{g \in G} c_g P_g
$$

sujeto a:

$$
\sum_{g \in G} P_g = D
$$

$$
P_g^{min} \leq P_g \leq P_g^{max} \qquad \forall g \in G
$$

El balance asegura que la generación cubra la demanda. Los límites de generación representan restricciones técnicas de cada unidad. La solución debe revisarse comprobando que la suma de generación coincide con la demanda y que ninguna unidad opera fuera de rango.

## Costos por tramos y costos cuadráticos

Muchas unidades no se representan correctamente con un costo variable único. Una aproximación lineal por tramos permite dividir la producción de una unidad en bloques con costos crecientes. Si se usa una función cuadrática:

$$
C_g(P_g)=a_g+b_gP_g+c_gP_g^2
$$

su costo marginal es:

$$
MC_g(P_g)=b_g+2c_gP_g
$$

Esta relación conecta la operación eléctrica con la teoría de optimización no lineal y ayuda a interpretar por qué el despacho incremental iguala costos marginales bajo ciertas condiciones.

## Compromiso de unidades

El despacho económico asume que las unidades están disponibles. El unit commitment añade la decisión de encender o apagar cada unidad:

$$
u_{g,t}\in\{0,1\}
$$

$$
P_g^{min}u_{g,t}\leq P_{g,t}\leq P_g^{max}u_{g,t}
$$

También deben considerarse costos de arranque, rampas y reserva:

$$
P_{g,t}-P_{g,t-1}\leq RU_g
$$

$$
\sum_g \left(P_g^{max}u_{g,t}-P_{g,t}\right) \geq R_t
$$

![Compromiso de unidades](figuras/03_unit_commitment_timeline.svg)

## Despacho hidrotérmico

En un sistema hidrotérmico, el agua tiene costo de oportunidad. Usarla ahora puede reducir generación térmica presente, pero también puede disminuir flexibilidad futura. El balance de embalse se expresa como:

$$
S_{t+1}=S_t+I_t-Q_t-Sp_t
$$

La generación hidroeléctrica puede aproximarse mediante:

$$
P_{h,t}=\rho_h Q_{h,t}
$$

Donde $S_t$ es almacenamiento, $I_t$ afluencia, $Q_t$ caudal turbinado, $Sp_t$ vertimiento y $\rho_h$ coeficiente de producción.

![Balance de embalse](figuras/04_balance_embalse.svg)

## Modelos del módulo

| Modelo | Decisión que representa | Acceso |
|---|---|---|
| Despacho económico uninodal | Generación por unidad en una hora | [Abrir](modelos/01_despacho_economico_uninodal.md) |
| Despacho por tramos | Producción por segmentos de costo | [Abrir](modelos/02_despacho_economico_por_tramos.md) |
| Despacho con pérdidas | Generación considerando pérdidas técnicas | [Abrir](modelos/03_despacho_con_perdidas.md) |
| Compromiso de unidades | Encendido, apagado, reserva y rampas | [Abrir](modelos/04_compromiso_unidades_termicas.md) |
| Hidrotérmico simple | Uso de agua y generación térmica | [Abrir](modelos/05_despacho_hidrotermico_simple.md) |
| Cascada hidroeléctrica | Relación aguas arriba y aguas abajo | [Abrir](modelos/06_operacion_cascada_hidroelectrica.md) |

## Actividad

La actividad del módulo integra despacho económico, unit commitment e hidrotérmico. El estudiante debe construir archivos `.mod`, `.dat` y `.run`, resolver escenarios y justificar la solución con criterios técnicos.

[Ir a la actividad](actividades/actividad_02__operacion_de_corto_plazo.md)

---

[Menú principal](../../README.md) · [Modelos](modelos/README.md) · [Actividades](actividades/README.md) · [Datos](datos/)
