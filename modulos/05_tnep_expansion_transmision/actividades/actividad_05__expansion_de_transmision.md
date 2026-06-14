# Actividad 05 — Expansión de transmisión

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Datos](../datos/)

## Competencia

Formular y resolver un problema de expansión de transmisión, interpretando inversión, congestión, energía no servida y efecto de la demanda futura.

## Trabajo solicitado

1. Construya un modelo de transporte o DC-TNEP con los datos del módulo.
2. Identifique corredores existentes y candidatos.
3. Resuelva el caso base.
4. Repita el análisis con demanda incrementada.
5. Compare circuitos construidos, costo total y energía no servida.

## Entregables

- Formulación matemática.
- Archivos `.mod`, `.dat` y `.run`.
- Tabla de líneas construidas.
- Flujos por corredor.
- Costo de inversión y ENS.
- Figura de red o tabla de corredores.
- Discusión del escenario de demanda alta.

## Validación mínima

- El balance debe cumplirse en cada barra o zona.
- Los flujos deben respetar capacidad existente y nueva.
- No deben construirse más circuitos que el máximo permitido.
- La expansión debe reducir congestión o ENS respecto al caso restringido.
