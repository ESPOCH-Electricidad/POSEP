# Actividad 06 — Expansión de generación

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Datos](../datos/)

## Competencia

Formular y resolver un problema de expansión de generación, diferenciando capacidad instalada, capacidad firme, operación por bloques y costo total anualizado.

## Trabajo solicitado

1. Construya un modelo GEP estático o multianual a partir de las tablas de tecnologías, años y bloques.
2. Incluya inversión, capacidad acumulada, generación por bloque, reserva firme y ENS.
3. Resuelva el caso base.
4. Compare con una variación: demanda alta, mayor margen de reserva, menor disponibilidad renovable o cambio de CAPEX.
5. Explique por qué el modelo selecciona una tecnología y no otra.

## Entregables

- Formulación matemática completa.
- Archivos `.mod`, `.dat` y `.run`.
- Tabla de capacidad nueva y capacidad total.
- Generación por tecnología y bloque.
- Reserva firme disponible.
- Costo total desagregado.
- Figura de capacidad o generación.
- Discusión de sensibilidad.

## Validación mínima

- La demanda por bloque debe estar cubierta o penalizada como ENS.
- La generación no debe superar capacidad disponible por bloque.
- La restricción de reserva firme debe cumplirse.
- La inversión debe respetar límites máximos de construcción.
- El resultado debe explicarse con costo fijo, costo variable, disponibilidad y crédito firme.
