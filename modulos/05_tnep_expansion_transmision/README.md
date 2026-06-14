# 05 — Expansión de transmisión

[Menú principal](../../README.md) · [Modelos](modelos/README.md) · [Actividades](actividades/README.md) · [Datos](datos/) · [Guía AMPL](../../docs/guia_ampl.md)

## Propósito del módulo

La expansión de transmisión decide qué refuerzos de red construir para transportar energía desde los puntos de generación hacia los centros de demanda. No es suficiente comparar costos de líneas: una línea candidata solo tiene valor si reduce congestión, evita energía no servida o permite utilizar generación más económica.

![Red existente y candidatos](figuras/01_red_existente_candidatos.svg)

## Modelo de transporte

El modelo de transporte representa oferta, demanda y capacidades de corredores sin usar ángulos eléctricos. Es útil como primera aproximación:

$$
\sum_{j} f_{ij} - \sum_{j} f_{ji} + g_i + ens_i = d_i
$$

$$
0 \leq f_{ij} \leq \bar{F}_{ij}^{exist}+\bar{F}_{ij}^{cand} y_{ij}
$$

La variable binaria $y_{ij}$ indica si se construye un corredor candidato. Aunque este modelo no reproduce leyes de Kirchhoff, permite entender la lógica de inversión bajo balance y límites de transferencia.

![Transporte y DC](figuras/02_transporte_vs_dc.svg)

## Modelo DC-TNEP

El modelo DC añade ángulos y reactancias:

$$
f_{ij}=\frac{\theta_i-\theta_j}{x_{ij}}
$$

Para una línea candidata, esta relación solo debe activarse si la línea se construye. Se usa una formulación disyuntiva linealizada con $M$:

$$
-M(1-y_{ij}) \leq f_{ij}-\frac{\theta_i-\theta_j}{x_{ij}} \leq M(1-y_{ij})
$$

Si $y_{ij}=1$, el flujo queda ligado a los ángulos. Si $y_{ij}=0$, la restricción se relaja y el flujo debe quedar en cero por el límite de capacidad.

![Restricción big-M](figuras/03_big_m_disyuntivo.svg)

## Expansión multietapa

En horizontes de varios años, la decisión no solo es qué construir, sino cuándo. La construcción acumulada se representa como:

$$
y_{ij,y}^{acc}=\sum_{\tau \leq y} y_{ij,\tau}
$$

La decisión temprana tiene mayor efecto operativo, pero también adelanta inversión. La decisión tardía reduce costo presente, pero puede aumentar congestión o energía no servida.

![Expansión multietapa](figuras/04_expansion_multietapa.svg)

## Modelos del módulo

| Modelo | Pregunta que responde | Acceso |
|---|---|---|
| Transporte | Qué corredores alivian déficit sin ley DC | [Abrir](modelos/01_modelo_transporte_expansion_transmision.md) |
| Refuerzo constructivo | Qué obra construir con límites discretos | [Abrir](modelos/02_modelo_constructivo_refuerzo_red.md) |
| DC-TNEP | Qué líneas construir con flujo DC | [Abrir](modelos/03_modelo_dc_expansion_transmision.md) |
| Híbrido | Comparación entre transporte y DC | [Abrir](modelos/04_modelo_hibrido_expansion_transmision.md) |
| Disyuntivo | Uso de variable binaria y big-M | [Abrir](modelos/05_modelo_lineal_disyuntivo_expansion_transmision.md) |
| Multietapa | Construcción acumulada por año | [Abrir](modelos/06_modelo_multietapa_expansion_transmision.md) |

## Actividad

La actividad pide formular un TNEP con corredores candidatos, construir el archivo de datos y comparar una solución de transporte con una solución DC.

[Ir a la actividad](actividades/actividad_05__expansion_de_transmision.md)

---

[Menú principal](../../README.md) · [Modelos](modelos/README.md) · [Actividades](actividades/README.md) · [Datos](datos/)
