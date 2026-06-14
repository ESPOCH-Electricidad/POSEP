# Actividad 01C — Localización de antenas

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Datos](../datos/)

## Competencia

Formular un problema entero mixto con variables binarias de selección y restricciones de cobertura.

## Trabajo solicitado

Use el caso de localización de antenas. Defina candidatos, zonas de demanda, matriz de cobertura y costo de instalación. El objetivo es seleccionar antenas de mínimo costo garantizando cobertura mínima de todas las zonas.

## Entregables

1. Formulación MILP completa.
2. Archivo `.dat` con candidatos, zonas, costos y matriz de cobertura.
3. Antenas seleccionadas y costo total.
4. Zonas cubiertas por cada antena seleccionada.
5. Sensibilidad: incremente el requisito de cobertura de una zona o bloquee un candidato.

## Validación mínima

- Todas las zonas deben cumplir cobertura.
- Las variables de selección deben ser binarias.
- La solución debe justificar por qué no se seleccionan alternativas más costosas si no son necesarias.
