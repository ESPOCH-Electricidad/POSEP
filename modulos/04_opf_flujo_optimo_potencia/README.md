# 04 — Flujo óptimo de potencia

[Menú principal](../../README.md) · [Actividades](actividades/README.md) · [Datos](datos/)

## Pregunta guía

¿Por qué no basta con saber cuánto genera cada unidad si no se considera dónde están conectadas generación, demanda y líneas?

## Contexto técnico

El despacho económico uninodal ignora la red. El OPF incorpora barras, líneas, límites de transmisión, ángulos, tensiones y congestión. Esto permite estudiar redispatch, flujos, pérdidas y factibilidad eléctrica.

## Desarrollo conceptual

```text
despacho económico sin red → ubicación de generación y demanda → balance nodal → flujo DC → límites térmicos → congestión → redispatch → OPF-AC
```

## Figura central

![Red de 3 barras con flujos](figuras/02_red_3_barras_con_flujos.svg)

## Modelos incluidos

| Modelo | Enlace |
| --- | --- |
| Modelo 01 — Flujo óptimo de potencia DC | [Abrir](modelos/01_flujo_optimo_potencia_dc.md) |
| Modelo 02 — Flujo óptimo de potencia AC | [Abrir](modelos/02_flujo_optimo_potencia_ac.md) |

## Validación de resultados

La barra slack debe tener ángulo cero; los balances nodales deben cerrar; los flujos deben respetar Fmax; si hay congestión debe identificarse la línea activa; en OPF-AC las tensiones deben permanecer dentro de Vmin/Vmax.
