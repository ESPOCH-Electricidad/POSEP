# Ejemplo 05 — Forma matricial de un programa lineal

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

Este ejemplo muestra cómo los modelos lineales pueden escribirse con matrices y vectores. Es útil para entender cómo los solvers procesan modelos algebraicos.

## 2. Enunciado

Se desea resolver un programa lineal de minimización con tres variables y tres restricciones. El estudiante debe reconocer la matriz de coeficientes, el vector de costos, el vector del lado derecho y el dominio de las variables.



## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| I | restricciones |
| J | variables |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| A[i,j] | - | coeficiente de la variable j en la restricción i |
| b[i] | - | lado derecho de la restricción i |
| c[j] | - | coeficiente de costo de la variable j |

## 5. Datos completos para construir el archivo de datos

### Matriz A

| restriccion | x1 | x2 | x3 | b |
| --- | --- | --- | --- | --- |
| R1 | 2 | 1 | 1 | 60 |
| R2 | 1 | 3 | 2 | 90 |
| R3 | 2 | 2 | 3 | 120 |

### Vector c

| variable | c |
| --- | --- |
| x1 | 8 |
| x2 | 6 |
| x3 | 5 |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| x[j] | continua no negativa | variable de decisión j |

## 7. Función objetivo

$$
\min Z=\sum_{j\in J}c_jx_j
$$

**Explicación de la función objetivo.** Minimiza el costo lineal total asociado al vector de variables.

## 8. Restricciones del modelo

### Restricciones matriciales

$$
\sum_{j\in J}A_{i,j}x_j\geq b_i\quad \forall i\in I
$$

**Explicación.** Cada fila de la matriz representa una restricción lineal.

### No negatividad

$$
x_j\geq 0\quad \forall j\in J
$$

**Explicación.** Todas las variables son continuas no negativas.

## 9. Guía para construir el archivo `.dat`

A partir de las tablas anteriores, prepare el archivo de datos respetando los nombres de conjuntos, parámetros y unidades del modelo. La siguiente estructura muestra cómo debe organizarse la información.

```ampl
set I := R1 R2 R3;
set J := x1 x2 x3;

param c :=
x1 8
x2 6
x3 5
;

param b :=
R1 60
R2 90
R3 120
;

param A:
      x1 x2 x3 :=
R1    2  1  1
R2    1  3  2
R3    2  2  3
;
```

## 10. Resultados esperados

El estudiante debe identificar matriz A, vector b, vector c, solución óptima y restricciones activas.

## 11. Actividad asociada

[Actividad 01A](../actividades/actividad_01_programacion_lineal.md)

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
