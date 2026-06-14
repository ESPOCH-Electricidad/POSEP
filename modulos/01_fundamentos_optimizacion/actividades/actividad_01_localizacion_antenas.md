# Actividad 01C — Localización binaria de antenas

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Datos](../datos/) · [Guía AMPL](../../../docs/guia_ampl.md)

## Competencia

Formular un problema entero mixto de selección de instalaciones mediante variables binarias y restricciones de cobertura.

## Enunciado

Se dispone de ocho ubicaciones candidatas para instalar antenas de comunicación. Cada antena tiene un costo y cubre un subconjunto de medidores. Se debe seleccionar el conjunto de antenas de menor costo que permita cubrir todos los medidores al menos una vez.

## Datos del caso

Use `antenas_candidatas.csv` y `antenas_cobertura.csv`.

La variable binaria $y_a$ indica si se instala la antena $a$.

## Formulación requerida

$$
\min Z=\sum_{a\in A} cost_a y_a
$$

Cobertura mínima:

$$
\sum_{a\in A} cover_{m,a}y_a \geq 1 \qquad \forall m\in M
$$

Dominio binario:

$$
y_a\in\{0,1\}\qquad \forall a\in A
$$

## Tareas

1. Construya en `.dat` el conjunto de antenas, medidores, costos y matriz de cobertura.
2. Implemente el modelo con variable binaria.
3. Reporte antenas seleccionadas, costo total y número de medidores cubiertos por cada antena seleccionada.
4. Identifique si algún medidor queda cubierto por más de una antena.
5. Agregue una restricción de máximo cuatro antenas instaladas y compare.
6. Agregue una restricción de redundancia para que los medidores M4, M5 y M6 tengan al menos dos coberturas.

## Validación

Para cada medidor, calcule la suma de cobertura obtenida. No basta con reportar antenas seleccionadas: se debe demostrar que todos los medidores cumplen la restricción.

## Entregables

- Archivos `.mod`, `.dat`, `.run`.
- Tabla de antenas seleccionadas.
- Tabla medidor-cobertura resultante.
- Comparación entre caso base, máximo cuatro antenas y redundancia M4-M6.
- Comentario sobre costo adicional por confiabilidad.
