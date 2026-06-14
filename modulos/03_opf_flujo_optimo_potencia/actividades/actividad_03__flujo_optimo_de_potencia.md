# Actividad 03 — Flujo óptimo de potencia

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Datos](../datos/)

## Competencia

Formular un OPF con balance nodal, flujo por líneas, límites térmicos y despacho económico con restricciones de red.

## Trabajo solicitado

1. Construya un OPF-DC con los datos de barras, líneas y generadores.
2. Defina una barra de referencia angular.
3. Resuelva el caso base.
4. Identifique líneas congestionadas y compare el despacho contra un caso sin límites de transmisión.
5. Explique cómo la red modifica el costo operativo.

## Entregables

- Formulación matemática del OPF-DC.
- Archivos `.mod`, `.dat` y `.run`.
- Tabla de generación por unidad.
- Flujos por línea y ángulos por barra.
- Identificación de congestión.
- Figura o tabla resumen de red.

## Validación mínima

- El balance nodal debe cumplirse en todas las barras.
- Los flujos deben respetar límites.
- La barra de referencia debe estar fijada.
- El costo debe aumentar o mantenerse cuando se activan restricciones de red.
