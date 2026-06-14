# Ejemplo 04 — Localización de antenas

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

El caso introduce programación entera mixta mediante selección de sitios candidatos para cubrir medidores. Es un ejemplo directo de variables binarias.

## 2. Enunciado

Una empresa de servicios públicos desea instalar antenas para lectura remota de 10 medidores. Una antena cubre un medidor si está dentro de un radio de 520 m. Existen 8 sitios candidatos con costos y barrio asociado. Se debe seleccionar el conjunto de antenas de mínimo costo que cubra todos los medidores y que instale al menos una antena por barrio.



## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| I | medidores |
| J | antenas candidatas |
| B | barrios |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| cost[j] | USD | costo de instalación de la antena j |
| a[i,j] | 0/1 | 1 si la antena j cubre el medidor i |
| barrio[j] | - | barrio al que pertenece la antena j |
| Jb[b] | - | subconjunto de antenas ubicadas en el barrio b |

## 5. Datos completos para construir el archivo de datos

### Antenas candidatas

| antena | cost_usd | barrio |
| --- | --- | --- |
| A1 | 1500 | B1 |
| A2 | 800 | B1 |
| A3 | 1200 | B2 |
| A4 | 1700 | B2 |
| A5 | 900 | B3 |
| A6 | 1100 | B3 |
| A7 | 600 | B4 |
| A8 | 1000 | B4 |

### Matriz de cobertura

| medidor | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| M2 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| M3 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| M4 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |
| M5 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| M6 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 |
| M7 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| M8 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| M9 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| M10 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| y[j] | binaria | 1 si se instala la antena j; 0 en caso contrario |

## 7. Función objetivo

$$
\min Z=\sum_{j\in J} cost_j y_j
$$

**Explicación de la función objetivo.** Minimiza el costo total de instalación de las antenas seleccionadas.

## 8. Restricciones del modelo

### Cobertura de medidores

$$
\sum_{j\in J} a_{i,j} y_j\geq 1\quad \forall i\in I
$$

**Explicación.** Cada medidor debe estar cubierto por al menos una antena seleccionada.

### Cobertura por barrio

$$
\sum_{j\in J_b} y_j\geq 1\quad \forall b\in B
$$

**Explicación.** Garantiza presencia mínima de infraestructura en cada barrio.

### Dominio binario

$$
y_j\in\{0,1\}\quad \forall j\in J
$$

**Explicación.** Cada antena se instala o no se instala; no existen decisiones fraccionarias.

## 9. Plantilla `.dat` sugerida

```ampl
set I := M1 M2 M3 M4 M5 M6 M7 M8 M9 M10;
set J := A1 A2 A3 A4 A5 A6 A7 A8;
set B := B1 B2 B3 B4;

set Jb[B1] := A1 A2;
set Jb[B2] := A3 A4;
set Jb[B3] := A5 A6;
set Jb[B4] := A7 A8;

param cost :=
A1 1500
A2 800
A3 1200
A4 1700
A5 900
A6 1100
A7 600
A8 1000
;

param a:
       A1 A2 A3 A4 A5 A6 A7 A8 :=
M1     1  1  0  0  0  0  0  0
M2     1  0  1  0  0  0  0  0
M3     0  1  1  1  0  0  0  0
M4     0  0  1  1  1  0  0  0
M5     0  0  0  1  1  1  0  0
M6     0  0  0  0  1  1  1  0
M7     0  0  0  0  0  1  1  1
M8     0  0  0  0  0  0  1  1
M9     1  0  0  0  0  0  0  1
M10    0  1  0  0  0  0  0  1
;
```

## 10. Resultados esperados

El estudiante debe reportar antenas seleccionadas, costo total, medidores cubiertos y cumplimiento por barrio.

## 11. Actividad asociada

[Actividad 01C](../actividades/actividad_01_localizacion_antenas.md)

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
