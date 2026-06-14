# 06 — Expansión de transmisión

[Menú principal](../../README.md) · [Actividades](actividades/README.md) · [Datos](datos/)

## Pregunta guía

¿Qué ocurre si existe generación suficiente, pero la red no puede transportar la energía hacia los centros de demanda?

## Contexto técnico

La expansión de transmisión decide qué líneas, refuerzos o corredores construir para reducir congestión, energía no servida y costos operativos futuros. La demanda proyectada del módulo 05 alimenta estos modelos.

## Desarrollo conceptual

```text
red existente → demanda futura → generación disponible → congestión → corredores candidatos → inversión → modelo de transporte → modelo DC → formulación disyuntiva → expansión multietapa
```

## Figura central

![Red base y corredores candidatos](figuras/01_red_base_candidatos_garver.svg)

## Modelos incluidos

| Modelo | Enlace |
| --- | --- |
| Modelo 01 — Transporte para expansión de transmisión | [Abrir](modelos/01_modelo_transporte_expansion_transmision.md) |
| Modelo 02 — Constructivo de refuerzo de red | [Abrir](modelos/02_modelo_constructivo_refuerzo_red.md) |
| Modelo 03 — DC de expansión de transmisión | [Abrir](modelos/03_modelo_dc_expansion_transmision.md) |
| Modelo 04 — Híbrido de expansión de transmisión | [Abrir](modelos/04_modelo_hibrido_expansion_transmision.md) |
| Modelo 05 — Lineal disyuntivo de expansión de transmisión | [Abrir](modelos/05_modelo_lineal_disyuntivo_expansion_transmision.md) |
| Modelo 06 — Multietapa de expansión de transmisión | [Abrir](modelos/06_modelo_multietapa_expansion_transmision.md) |

## Validación de resultados

No debe existir flujo en candidatos no construidos; los límites Fmax deben cumplirse; la inversión debe corresponder a corredores seleccionados; si hay ENS debe justificarse; en multietapa la capacidad construida debe acumularse.
