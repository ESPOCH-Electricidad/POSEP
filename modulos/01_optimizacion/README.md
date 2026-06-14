[← Inicio](../../README.md) | [Siguiente módulo →](../02_ampl/README.md)

# Módulo 01 — Fundamentos de optimización

## Objetivo

Formular problemas de decisión mediante conjuntos, parámetros, variables, función objetivo y restricciones. El módulo trabaja con programación lineal, forma matricial y variables binarias antes de pasar a modelos eléctricos.

![Proceso de modelado](figuras/01_proceso_modelado_matematico.svg)

## Estructura general

Un problema de optimización se escribe como:

$$
\min_x f(x)
$$

sujeto a:

$$
g_i(x) \leq 0 \quad \forall i
$$

$$
h_j(x) = 0 \quad \forall j
$$

$$
x \in X
$$

La variable $x$ contiene las decisiones; $f(x)$ mide el desempeño; las restricciones representan límites físicos, económicos o lógicos; y $X$ define el dominio de las variables.

## Caso 1. Producción de pinturas

### Enunciado

Una planta fabrica pintura azul y pintura negra. Cada litro vendido genera un ingreso distinto y cada producto requiere una cantidad diferente de tiempo de fabricación. La planta dispone de un número limitado de horas por semana y existe una demanda máxima por producto. Se requiere determinar la producción semanal que maximiza el ingreso.

### Datos completos

**Productos**

| producto   |   precio_usd_l |   produccion_l_h |   demanda_max_l |
|:-----------|---------------:|-----------------:|----------------:|
| azul       |             10 |               40 |            1000 |
| negra      |             15 |               30 |             860 |

**Parámetros generales**

| parametro         |   valor | unidad   |
|:------------------|--------:|:---------|
| horas_disponibles |      40 | h/semana |

### Modelo matemático

Conjunto:

$$
p \in P
$$

Parámetros:

$$
r_p: \text{ ingreso unitario [USD/L]}, \qquad a_p: \text{ tasa de producción [L/h]}, \qquad \bar{x}_p: \text{ demanda máxima [L]}
$$

$$
H: \text{ horas disponibles [h]}
$$

Variable:

$$
x_p \geq 0 \qquad \forall p \in P
$$

Función objetivo:

$$
\max Z = \sum_{p \in P} r_p x_p
$$

Restricciones:

$$
\sum_{p \in P} \frac{x_p}{a_p} \leq H
$$

$$
x_p \leq \bar{x}_p \qquad \forall p \in P
$$

### Actividad

Construya `pintura.mod`, `pintura.dat` y `pintura.run` a partir de la formulación y las tablas.

## Caso 2. Producción de acero

### Enunciado

Una acería produce láminas y bobinas. Cada producto tiene una utilidad por tonelada, una tasa de producción y un límite de venta. La planta dispone de 40 horas semanales. Se requiere maximizar la utilidad semanal.

### Datos completos

**Productos**

| producto   |   utilidad_usd_t |   produccion_t_h |   demanda_max_t |
|:-----------|-----------------:|-----------------:|----------------:|
| laminas    |               25 |               20 |             500 |
| bobinas    |               30 |               15 |             450 |

**Parámetros generales**

| parametro         |   valor | unidad   |
|:------------------|--------:|:---------|
| horas_disponibles |      40 | h/semana |

### Modelo matemático

$$
\max Z = \sum_{p \in P} u_p x_p
$$

$$
\sum_{p \in P} \frac{x_p}{a_p} \leq H
$$

$$
0 \leq x_p \leq \bar{x}_p \qquad \forall p \in P
$$

### Actividad

Use el mismo archivo `.mod` del caso de pinturas y construya un nuevo `.dat` para acero. Explique qué parte del modelo permanece y qué parte cambia.

## Caso 3. Transporte de energía

### Enunciado

Tres fuentes pueden abastecer tres cargas. Cada fuente tiene una oferta máxima de energía y cada carga requiere una demanda fija. El costo de enviar energía depende del par fuente–carga. Se debe minimizar el costo total de suministro.

### Datos completos

**Fuentes**

| fuente   |   oferta_mwh |
|:---------|-------------:|
| F1       |          120 |
| F2       |          100 |
| F3       |           90 |

**Cargas**

| carga   |   demanda_mwh |
|:--------|--------------:|
| C1      |            80 |
| C2      |           110 |
| C3      |            90 |

**Costos**

| fuente   | carga   |   costo_usd_mwh |
|:---------|:--------|----------------:|
| F1       | C1      |               5 |
| F1       | C2      |               7 |
| F1       | C3      |               9 |
| F2       | C1      |               6 |
| F2       | C2      |               4 |
| F2       | C3      |               8 |
| F3       | C1      |               9 |
| F3       | C2      |               6 |
| F3       | C3      |               3 |

### Modelo matemático

Conjuntos:

$$
i \in I, \qquad j \in J
$$

Parámetros: $s_i$ oferta, $d_j$ demanda y $c_{ij}$ costo unitario.

Variable:

$$
x_{ij} \geq 0
$$

Función objetivo:

$$
\min Z=\sum_{i\in I}\sum_{j\in J}c_{ij}x_{ij}
$$

Restricciones:

$$
\sum_{j\in J}x_{ij}\leq s_i \qquad \forall i\in I
$$

$$
\sum_{i\in I}x_{ij}=d_j \qquad \forall j\in J
$$

### Actividad

Construya `transporte.mod`, `transporte.dat` y `transporte.run`. Verifique si la oferta total permite cubrir la demanda total.

## Caso 4. Forma matricial

### Enunciado

Considere un problema lineal en forma matricial. Se requiere minimizar un costo sujeto a tres restricciones de recursos.

### Datos completos

**Matriz A y vector b**

| restriccion   |   x1 |   x2 |   x3 |   b |
|:--------------|-----:|-----:|-----:|----:|
| R1            |    2 |    1 |    1 |  60 |
| R2            |    1 |    3 |    2 |  90 |
| R3            |    2 |    2 |    3 | 120 |

**Vector c**

| variable   |   costo |
|:-----------|--------:|
| x1         |       8 |
| x2         |       6 |
| x3         |       5 |

### Modelo matemático

$$
\min Z=c^Tx
$$

$$
Ax\leq b
$$

$$
x\geq 0
$$

### Actividad

Escriba la formulación indexada equivalente y construya el `.dat` desde las tablas.

## Caso 5. Localización de antenas

### Enunciado

Se desea instalar el menor costo de antenas para cubrir diez medidores inteligentes. Una antena cubre un medidor si la matriz de cobertura toma valor 1. Cada medidor debe quedar cubierto por al menos una antena.

### Datos completos

**Antenas candidatas**

| antena   |   costo_usd | sector   |
|:---------|------------:|:---------|
| A1       |        1500 | B1       |
| A2       |         800 | B1       |
| A3       |        1200 | B2       |
| A4       |        1700 | B2       |
| A5       |         900 | B3       |
| A6       |        1100 | B3       |
| A7       |         600 | B4       |
| A8       |        1000 | B4       |

**Matriz de cobertura**

| medidor   |   A1 |   A2 |   A3 |   A4 |   A5 |   A6 |   A7 |   A8 |
|:----------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
| M1        |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |
| M2        |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |
| M3        |    0 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |
| M4        |    0 |    0 |    1 |    1 |    1 |    0 |    0 |    0 |
| M5        |    0 |    0 |    0 |    1 |    1 |    1 |    0 |    0 |
| M6        |    0 |    0 |    0 |    0 |    1 |    1 |    1 |    0 |
| M7        |    0 |    0 |    0 |    0 |    0 |    1 |    1 |    1 |
| M8        |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |
| M9        |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |
| M10       |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    1 |

### Modelo matemático

Conjuntos:

$$
a\in A, \qquad m\in M
$$

Parámetros: $c_a$ costo de antena y $cov_{ma}$ cobertura binaria.

Variable:

$$
y_a\in\{0,1\}
$$

Función objetivo:

$$
\min Z=\sum_{a\in A}c_a y_a
$$

Restricción de cobertura:

$$
\sum_{a\in A}cov_{ma}y_a\geq 1 \qquad \forall m\in M
$$

### Actividad

Construya el MILP y verifique que cada medidor tenga cobertura.

## Entregables

1. Archivos `.mod`, `.dat` y `.run` construidos por el estudiante.
2. Tabla con variables óptimas y valor objetivo.
3. Interpretación de restricciones activas, holguras y factibilidad.
