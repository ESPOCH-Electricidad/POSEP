# 03 — Flujo óptimo de potencia

[Menú principal](../../README.md) · [Modelos](modelos/README.md) · [Actividades](actividades/README.md) · [Datos](datos/) · [Guía AMPL](../../docs/guia_ampl.md)

## Propósito del módulo

El despacho económico decide generación sin representar explícitamente la red. El flujo óptimo de potencia incorpora barras, líneas, límites de transferencia y variables eléctricas. La pregunta deja de ser solo qué unidad es más barata; ahora importa dónde está conectada y qué capacidad tiene la red para transportar su energía.

![Red de barras y líneas](figuras/01_red_barras_lineas.svg)

## Balance nodal

En una red, el balance se cumple en cada barra. Para el modelo DC, la inyección neta en una barra es igual a la suma de flujos que salen por las líneas conectadas:

$$
\sum_{g \in G_i} P_g - D_i = \sum_{j:(i,j)\in L} F_{ij}
$$

Esta ecuación es más fuerte que un balance uninodal: obliga a que generación y demanda sean compatibles con la topología.

![Balance nodal](figuras/02_balance_nodal.svg)

## Aproximación DC

El OPF DC aproxima el flujo activo mediante diferencias angulares:

$$
F_{ij}=\frac{\theta_i-\theta_j}{x_{ij}}
$$

Se asume magnitud de tensión cercana a 1 p.u., ángulos pequeños y resistencia despreciable. Esta aproximación no sustituye al OPF AC, pero permite estudiar congestión, límites térmicos y precios sombra con un modelo lineal.

![Flujo DC por ángulos](figuras/03_flujo_dc_angulos.svg)

Una barra debe fijarse como referencia angular:

$$
\theta_{ref}=0
$$

Sin esta condición, el sistema de ángulos queda indeterminado porque solo importan diferencias de ángulo.

## Límites térmicos y congestión

Cada línea tiene una capacidad máxima:

$$
-F_{ij}^{max}\leq F_{ij}\leq F_{ij}^{max}
$$

Cuando un límite se vuelve activo, la unidad más barata del sistema puede no abastecer toda la demanda. Aparece congestión y el costo marginal puede diferir entre barras.

## OPF AC como extensión

El OPF AC representa tensiones, potencia activa y reactiva, pérdidas y límites de voltaje. Su formulación es no lineal y no convexa, por lo que se introduce después del modelo DC.

![Comparación DC y AC](figuras/04_comparacion_dc_ac.svg)

## Modelos del módulo

| Modelo | Decisión que representa | Acceso |
|---|---|---|
| OPF DC | Despacho con red linealizada y límites de línea | [Abrir](modelos/01_flujo_optimo_potencia_dc.md) |
| OPF AC introductorio | Balance AC y restricciones de tensión | [Abrir](modelos/02_flujo_optimo_potencia_ac.md) |

## Actividad

La actividad solicita formular y resolver un OPF DC de tres barras, analizar congestión y comparar el despacho con el caso uninodal.

[Ir a la actividad](actividades/actividad_03__flujo_optimo_de_potencia.md)

---

[Menú principal](../../README.md) · [Modelos](modelos/README.md) · [Actividades](actividades/README.md) · [Datos](datos/)
