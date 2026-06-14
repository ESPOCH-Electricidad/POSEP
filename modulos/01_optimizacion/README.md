[← Inicio](../../README.md) | [Siguiente módulo →](../02_ampl/README.md)

# Módulo 01 — Fundamentos de optimización

## Propósito

El módulo introduce la formulación de problemas de optimización antes de usar AMPL. La atención está en reconocer decisiones, datos, restricciones y función objetivo. Los ejemplos son deliberadamente pequeños para que el estudiante pueda verificar cada ecuación y cada unidad.

## Competencia

Formular problemas lineales y mixto-enteros a partir de un enunciado técnico, identificando conjuntos, índices, parámetros, variables de decisión, función objetivo y restricciones.

![Proceso de modelado](figuras/01_proceso_modelado_matematico.svg)

## Caso 1. Producción de pinturas

### Enunciado

Una planta puede producir pintura azul y pintura negra. Cada litro vendido genera un ingreso, cada producto tiene una tasa de producción distinta y existe un máximo comercial de venta semanal. Se debe decidir cuántos litros producir de cada pintura para maximizar el ingreso semanal sin exceder las horas disponibles de producción.

### Datos del caso

**Productos**

| producto   |   precio [USD/L] |   tasa [L/h] |   demanda máxima [L] |
|:-----------|-----------------:|-------------:|---------------------:|
| azul       |               10 |           40 |                 1000 |
| negra      |               15 |           30 |                  860 |

**Parámetro general**

| parametro         |   valor | unidad   |
|:------------------|--------:|:---------|
| horas_disponibles |      40 | h/semana |

### Formulación matemática

**Conjuntos e índices**

$P$: conjunto de pinturas, con índice $p\in P$.

**Parámetros**

$r_p$: ingreso unitario de la pintura $p$ [USD/L].

$a_p$: tasa de producción de la pintura $p$ [L/h].

$D_p^<built-in function max>$: demanda máxima de la pintura $p$ [L].

$H$: horas disponibles de producción [h/semana].

**Variable de decisión**

$x_p\geq 0$: litros producidos de la pintura $p$.

**Función objetivo**

$$
\max Z=\sum_{p\in P} r_p x_p
$$

**Restricciones**

Disponibilidad de horas:

$$
\sum_{p\in P} \frac{x_p}{a_p}\leq H
$$

Demanda máxima:

$$
0\leq x_p\leq D_p^{max} \qquad \forall p\in P
$$

### Actividad

Construya `pintura.mod`, `pintura.dat` y `pintura.run`. Reporte producción óptima, ingreso total, horas utilizadas y holgura de cada restricción. Después incremente $H$ en el último dígito de su código de estudiante y explique si cambia la restricción que limita la solución.

## Caso 2. Producción de acero

### Enunciado

Una acería produce láminas y bobinas. La estructura matemática es igual al caso anterior, pero cambian los datos, las unidades y la interpretación económica. El objetivo es mostrar que un mismo modelo algebraico puede resolver problemas distintos si los datos están correctamente separados.

### Datos del caso

**Productos**

| producto   |   utilidad [USD/t] |   tasa [t/h] |   demanda máxima [t] |
|:-----------|-------------------:|-------------:|---------------------:|
| laminas    |                 25 |           20 |                  500 |
| bobinas    |                 30 |           15 |                  450 |

**Parámetro general**

| parametro         |   valor | unidad   |
|:------------------|--------:|:---------|
| horas_disponibles |      40 | h/semana |

### Formulación matemática

**Conjuntos e índices**

$P$: conjunto de productos de acero, con índice $p\in P$.

**Parámetros**

$u_p$: utilidad unitaria del producto $p$ [USD/t].

$a_p$: tasa de producción [t/h].

$D_p^<built-in function max>$: demanda máxima [t].

$H$: horas disponibles [h/semana].

**Variable de decisión**

$x_p\geq 0$: producción del producto $p$ [t].

**Función objetivo**

$$
\max Z=\sum_{p\in P} u_p x_p
$$

**Restricciones**

$$
\sum_{p\in P} \frac{x_p}{a_p}\leq H
$$

$$
0\leq x_p\leq D_p^{max}\qquad \forall p\in P
$$

### Actividad

Use el mismo archivo `.mod` del caso de pinturas y construya únicamente un nuevo `.dat`. Compare ambas soluciones y explique qué parte pertenece al modelo y qué parte pertenece al caso de estudio.

## Caso 3. Transporte de energía

### Enunciado

Tres fuentes pueden entregar energía a tres cargas. Cada ruta tiene un costo de transporte. Se debe determinar cuánta energía enviar desde cada fuente hacia cada carga minimizando el costo total y cumpliendo oferta y demanda.

### Datos del caso

**Fuentes**

| fuente   |   oferta [MWh] |
|:---------|---------------:|
| F1       |            120 |
| F2       |            100 |
| F3       |             90 |

**Cargas**

| carga   |   demanda [MWh] |
|:--------|----------------:|
| C1      |              80 |
| C2      |             110 |
| C3      |              90 |

**Costos de transporte**

| fuente   | carga   |   costo [USD/MWh] |
|:---------|:--------|------------------:|
| F1       | C1      |                 5 |
| F1       | C2      |                 7 |
| F1       | C3      |                 9 |
| F2       | C1      |                 6 |
| F2       | C2      |                 4 |
| F2       | C3      |                 8 |
| F3       | C1      |                 9 |
| F3       | C2      |                 6 |
| F3       | C3      |                 3 |

### Formulación matemática

**Conjuntos e índices**

$F$: conjunto de fuentes, con índice $f\in F$.

$C$: conjunto de cargas, con índice $c\in C$.

**Parámetros**

$S_f$: oferta disponible en la fuente $f$ [MWh].

$D_c$: demanda de la carga $c$ [MWh].

$k_{fc}$: costo de transporte desde $f$ hacia $c$ [USD/MWh].

**Variable de decisión**

$x_{fc}\geq 0$: energía enviada desde la fuente $f$ hacia la carga $c$ [MWh].

**Función objetivo**

$$
\min Z=\sum_{f\in F}\sum_{c\in C} k_{fc}x_{fc}
$$

**Restricciones**

Oferta máxima por fuente:

$$
\sum_{c\in C}x_{fc}\leq S_f\qquad \forall f\in F
$$

Demanda de cada carga:

$$
\sum_{f\in F}x_{fc}=D_c\qquad \forall c\in C
$$

### Actividad

Construya el modelo de transporte en AMPL. Antes de resolver, verifique que la oferta total sea mayor o igual que la demanda total. Entregue la matriz de flujos óptimos y compruebe que cada fila y cada columna cumple su balance.

## Caso 4. Forma matricial de un LP

### Enunciado

Se desea formular un problema lineal de forma compacta usando una matriz de coeficientes. Este caso prepara al estudiante para entender que AMPL expande restricciones indexadas hasta formar la matriz que recibe el solver.

### Datos del caso

**Matriz $A$ y vector $b$**

| restriccion   |   x1 |   x2 |   x3 |   b |
|:--------------|-----:|-----:|-----:|----:|
| R1            |    2 |    1 |    1 |  60 |
| R2            |    1 |    3 |    2 |  90 |
| R3            |    2 |    2 |    3 | 120 |

**Vector de coeficientes del objetivo**

| variable   |   coeficiente objetivo |
|:-----------|-----------------------:|
| x1         |                      8 |
| x2         |                      6 |
| x3         |                      5 |

### Formulación matemática

**Conjuntos e índices**

$I$: conjunto de restricciones, con índice $i\in I$.

$J$: conjunto de variables, con índice $j\in J$.

**Parámetros**

$a_{ij}$: coeficiente de la variable $j$ en la restricción $i$.

$b_i$: lado derecho de la restricción $i$.

$c_j$: coeficiente de la variable $j$ en la función objetivo.

**Variable de decisión**

$x_j\geq 0$: nivel de la variable $j$.

**Función objetivo**

$$
\max Z=\sum_{j\in J} c_jx_j
$$

**Restricciones**

$$
\sum_{j\in J} a_{ij}x_j\leq b_i\qquad \forall i\in I
$$

### Actividad

Construya un `.mod` genérico que no mencione explícitamente `x1`, `x2` ni `x3`. Toda la información debe entrar por el `.dat`. Luego agregue una cuarta variable propuesta por usted y documente los cambios necesarios en la tabla de datos.

## Caso 5. Localización de antenas

### Enunciado

Se requiere cubrir diez medidores inteligentes mediante antenas candidatas. Una antena cubre un medidor si el valor de la matriz de cobertura es igual a 1. Cada medidor debe quedar cubierto al menos por una antena y el costo total de instalación debe ser mínimo.

### Datos del caso

**Antenas candidatas**

| antena   |   costo [USD] | sector   |
|:---------|--------------:|:---------|
| A1       |          1500 | B1       |
| A2       |           800 | B1       |
| A3       |          1200 | B2       |
| A4       |          1700 | B2       |
| A5       |           900 | B3       |
| A6       |          1100 | B3       |
| A7       |           600 | B4       |
| A8       |          1000 | B4       |

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

### Formulación matemática

**Conjuntos e índices**

$A$: conjunto de antenas candidatas, con índice $a\in A$.

$M$: conjunto de medidores, con índice $m\in M$.

**Parámetros**

$c_a$: costo de instalar la antena $a$ [USD].

$cov_{ma}$: parámetro binario que vale 1 si la antena $a$ cubre el medidor $m$.

**Variable de decisión**

$y_a\in\{0,1\}$: vale 1 si se instala la antena $a$.

**Función objetivo**

$$
\min Z=\sum_{a\in A} c_a y_a
$$

**Restricciones**

Cobertura mínima de cada medidor:

$$
\sum_{a\in A} cov_{ma}y_a\geq 1\qquad \forall m\in M
$$

### Actividad

Formule el MILP y resuélvalo. Reporte antenas seleccionadas, costo total y cobertura final de cada medidor. Justifique si existen antenas baratas que no se instalan y antenas costosas que sí resultan necesarias.

## Entregables del módulo

- Archivos `.mod`, `.dat` y `.run` construidos por el estudiante para cada caso asignado.
- Tabla de resultados y verificación de restricciones.
- Informe breve con interpretación técnica de cada solución.

## Evaluación

| Criterio | Ponderación |
|---|---:|
| Identificación correcta de conjuntos, parámetros y variables | 20 % |
| Formulación algebraica completa | 25 % |
| Construcción ordenada del `.dat` desde las tablas | 20 % |
| Ejecución, validación y lectura del resultado | 20 % |
| Interpretación técnica | 15 % |


## Archivos de datos

| Archivo | Uso |
|---|---|
| `acero_parametros.csv` | Tabla editable del caso |
| `acero_productos.csv` | Tabla editable del caso |
| `antenas_candidatas.csv` | Tabla editable del caso |
| `antenas_cobertura.csv` | Tabla editable del caso |
| `matriz_A_b.csv` | Tabla editable del caso |
| `pintura_parametros.csv` | Tabla editable del caso |
| `pintura_productos.csv` | Tabla editable del caso |
| `transporte_cargas.csv` | Tabla editable del caso |
| `transporte_costos.csv` | Tabla editable del caso |
| `transporte_fuentes.csv` | Tabla editable del caso |
| `vector_c.csv` | Tabla editable del caso |
