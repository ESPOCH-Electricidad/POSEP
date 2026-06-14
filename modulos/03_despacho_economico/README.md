[← Inicio](../../README.md) | [← Módulo anterior](../02_ampl/README.md) | [Siguiente módulo →](../04_opf/README.md)

# Módulo 03 — Despacho económico y operación de corto plazo

## Propósito

El módulo aborda decisiones de operación para una demanda conocida: cuánto generar, con qué unidades, bajo qué límites y con qué costo. La formulación inicia con despacho lineal y avanza hacia pérdidas, compromiso de unidades y operación hidrotérmica.

## Competencia

Formular problemas de operación de corto plazo, interpretar el costo marginal y comprobar que la solución respeta balance, límites técnicos, reserva y disponibilidad de recursos.

![Orden de mérito](figuras/02_orden_merito_con_demanda.png)

## Costo variable de una unidad térmica

Si se dispone de tasa de calor y precio del combustible, el costo variable puede expresarse como:

$$
c_g^{fuel}=HR_g p_g^{fuel}
$$

$$
c_g^{var}=c_g^{fuel}+c_g^{VOM}+EF_g p^{CO_2}
$$

En los casos siguientes el costo variable ya se entrega en USD/MWh para concentrar la práctica en la formulación.

## Caso 1. Despacho económico lineal

### Enunciado

Un sistema debe abastecer una demanda de una hora usando tres unidades térmicas. Cada generador tiene potencia mínima, potencia máxima y costo variable. Se debe minimizar el costo total horario.

### Datos del caso

**Generadores**

| gen   |   Pmin [MW] |   Pmax [MW] |   costo [USD/MWh] |
|:------|------------:|------------:|------------------:|
| G1    |          20 |         100 |                15 |
| G2    |          30 |          80 |                22 |
| G3    |           0 |          60 |                35 |

**Demanda**

| parametro   |   valor | unidad   |
|:------------|--------:|:---------|
| demanda     |     150 | MW       |

### Formulación matemática

**Conjuntos e índices:** $g\in G$.

**Parámetros:** $P_g^{min}$, $P_g^{max}$, $c_g$ y $D$.

**Variable:** $P_g\geq 0$, potencia generada [MW].

**Función objetivo**

$$
\min Z=\sum_{g\in G}c_gP_g
$$

**Restricciones**

$$
\sum_{g\in G}P_g=D
$$

$$
P_g^{min}\leq P_g\leq P_g^{max}\qquad \forall g\in G
$$

### Actividad

Construya los tres archivos de AMPL para este caso. Reporte despacho, costo total y unidad marginal. Verifique que el balance cierre exactamente y que ningún generador opere fuera de límites. Como variación individual use $D'=150+5d$, donde $d$ es el último dígito de su código de estudiante.

## Caso 2. Despacho por tramos

### Enunciado

Algunas unidades se representan mediante bloques de generación con costos crecientes. Se debe decidir cuánto usar de cada tramo para atender la demanda al menor costo.

### Datos del caso

**Bloques de generación**

| gen   | tramo   |   Pmax tramo [MW] |   costo tramo [USD/MWh] |
|:------|:--------|------------------:|------------------------:|
| G1    | K1      |                60 |                      14 |
| G1    | K2      |                50 |                      21 |
| G2    | K1      |                70 |                      18 |
| G2    | K2      |                60 |                      28 |

**Demanda**

| parametro   |   valor | unidad   |
|:------------|--------:|:---------|
| demanda     |     170 | MW       |

### Formulación matemática

**Conjuntos e índices:** $g\in G$, $k\in K_g$.

**Parámetros:** $\overline{P}_{gk}$ capacidad del tramo y $c_{gk}$ costo del tramo.

**Variable:** $p_{gk}\geq 0$.

**Función objetivo**

$$
\min Z=\sum_{g\in G}\sum_{k\in K_g}c_{gk}p_{gk}
$$

**Restricciones**

$$
\sum_{g\in G}\sum_{k\in K_g}p_{gk}=D
$$

$$
0\leq p_{gk}\leq \overline{P}_{gk}\qquad \forall g\in G,\; k\in K_g
$$

### Actividad

Implemente el modelo por tramos. Indique qué bloques quedan completamente usados, parcialmente usados o sin despacho. Explique cómo esta representación aproxima una curva de costo no lineal.

## Caso 3. Despacho con pérdidas

### Enunciado

El balance de potencia debe considerar pérdidas de transmisión representadas mediante coeficientes $B$. Al incluir pérdidas, la generación total debe superar la demanda.

### Datos del caso

**Generadores**

| gen   |   Pmin [MW] |   Pmax [MW] |   costo [USD/MWh] |
|:------|------------:|------------:|------------------:|
| G1    |          20 |         120 |                16 |
| G2    |          20 |         100 |                20 |
| G3    |          10 |          80 |                30 |

**Demanda**

| parametro   |   valor | unidad   |
|:------------|--------:|:---------|
| demanda     |     180 | MW       |

**Matriz de coeficientes $B$**

| g   | h   |   B_1_mw |
|:----|:----|---------:|
| G1  | G1  |  8e-05   |
| G1  | G2  |  2e-05   |
| G1  | G3  |  1e-05   |
| G2  | G1  |  2e-05   |
| G2  | G2  |  0.0001  |
| G2  | G3  |  3e-05   |
| G3  | G1  |  1e-05   |
| G3  | G2  |  3e-05   |
| G3  | G3  |  0.00012 |

### Formulación matemática

**Conjuntos e índices:** $g,h\in G$.

**Parámetros:** $B_{gh}$, $P_g^{min}$, $P_g^{max}$, $c_g$, $D$.

**Variable:** $P_g\geq 0$.

**Pérdidas**

$$
P^{loss}=\sum_{g\in G}\sum_{h\in G}P_gB_{gh}P_h
$$

**Función objetivo**

$$
\min Z=\sum_{g\in G}c_gP_g
$$

**Restricciones**

$$
\sum_{g\in G}P_g=D+P^{loss}
$$

$$
P_g^{min}\leq P_g\leq P_g^{max}\qquad \forall g\in G
$$

### Actividad

Resuelva primero el despacho sin pérdidas y luego el despacho con pérdidas. Compare generación total, costo total y participación de cada unidad. Presente el valor de $P^{loss}$ y compruebe el cierre del balance.

## Caso 4. Unit commitment

### Enunciado

Durante seis horas se debe decidir qué unidades permanecen encendidas, cuánto generan y cuándo arrancan. La solución debe atender demanda, reserva, límites de operación y rampas.

### Datos del caso

**Unidades**

| gen   |   Pmin [MW] |   Pmax [MW] |   costo [USD/MWh] |   arranque [USD] |   rampa subida [MW/h] |   rampa bajada [MW/h] |   estado_inicial |
|:------|------------:|------------:|------------------:|-----------------:|----------------------:|----------------------:|-----------------:|
| G1    |          30 |         120 |                18 |              500 |                    50 |                    50 |                1 |
| G2    |          20 |          90 |                24 |              350 |                    40 |                    40 |                0 |
| G3    |          10 |          60 |                38 |              120 |                    30 |                    30 |                0 |

**Demanda y reserva**

|   hora |   demanda [MW] |   reserva [MW] |
|-------:|---------------:|---------------:|
|      1 |            110 |             15 |
|      2 |            130 |             15 |
|      3 |            160 |             20 |
|      4 |            180 |             20 |
|      5 |            150 |             15 |
|      6 |            120 |             15 |

### Formulación matemática

**Conjuntos e índices:** $g\in G$, $t\in T$.

**Parámetros:** $P_g^{min}$, $P_g^{max}$, $c_g$, $SU_g$, $RU_g$, $RD_g$, $u_g^0$, $D_t$, $R_t$.

**Variables**

$$
P_{gt}\geq 0,\qquad u_{gt}\in\{0,1\},\qquad v_{gt}\in\{0,1\}
$$

**Función objetivo**

$$
\min Z=\sum_{t\in T}\sum_{g\in G}c_gP_{gt}+\sum_{t\in T}\sum_{g\in G}SU_gv_{gt}
$$

**Restricciones**

Balance:

$$
\sum_{g\in G}P_{gt}=D_t\qquad \forall t\in T
$$

Límites dependientes del estado:

$$
P_g^{min}u_{gt}\leq P_{gt}\leq P_g^{max}u_{gt}\qquad \forall g,t
$$

Reserva:

$$
\sum_{g\in G}P_g^{max}u_{gt}\geq D_t+R_t\qquad \forall t
$$

Arranque:

$$
v_{gt}\geq u_{gt}-u_{g,t-1}\qquad \forall g,t
$$

Rampas:

$$
P_{gt}-P_{g,t-1}\leq RU_g,\qquad P_{g,t-1}-P_{gt}\leq RD_g
$$

Para $t=1$, use el estado inicial $u_g^0$ y una generación inicial coherente definida por el docente o por el estudiante.

### Actividad

Construya el MILP de unit commitment. Entregue una tabla por hora con estado, arranque, generación, reserva disponible y costo. Analice si alguna unidad permanece encendida por reserva o por mínimo técnico.

## Caso 5. Despacho hidrotérmico

### Enunciado

Un sistema con una central hidroeléctrica y dos unidades térmicas debe abastecer demanda en cuatro periodos. La decisión de turbinar agua afecta el volumen futuro del embalse, por lo que el agua tiene costo de oportunidad.

### Datos del caso

**Central hidroeléctrica**

| hidro   |   v0_hm3 |   vmin_hm3 |   vmax_hm3 |   qmax_hm3 |   produccion_mwh_hm3 |
|:--------|---------:|-----------:|-----------:|-----------:|---------------------:|
| H1      |       80 |         20 |        120 |         35 |                    2 |

**Unidades térmicas**

| gen   |   Pmax [MW] |   costo [USD/MWh] |
|:------|------------:|------------------:|
| T1    |         100 |                35 |
| T2    |          80 |                55 |

**Demanda y afluencia**

|   periodo |   demanda [MW] |   afluencia [hm3] |
|----------:|---------------:|------------------:|
|         1 |            130 |                20 |
|         2 |            170 |                15 |
|         3 |            150 |                10 |
|         4 |            120 |                25 |

**Penalización por energía no servida**

| parametro   |   valor | unidad   |
|:------------|--------:|:---------|
| VOLL        |    1000 | USD/MWh  |

### Formulación matemática

**Conjuntos e índices:** $t\in T$, $g\in G^T$.

**Parámetros:** $D_t$, $I_t$, $V^0$, $V^{min}$, $V^{max}$, $Q^{max}$, $\rho$, $c_g$, $VOLL$.

**Variables:** $V_t$, $Q_t$, $Sp_t$, $P_t^H$, $P_{gt}^T$ y $ENS_t$.

**Función objetivo**

$$
\min Z=\sum_{t\in T}\sum_{g\in G^T}c_gP_{gt}^T+\sum_{t\in T}VOLL\cdot ENS_t
$$

**Restricciones**

Balance eléctrico:

$$
P_t^H+\sum_{g\in G^T}P_{gt}^T+ENS_t=D_t\qquad \forall t
$$

Producción hidroeléctrica:

$$
P_t^H=\rho Q_t\qquad \forall t
$$

Balance del embalse:

$$
V_t=V_{t-1}+I_t-Q_t-Sp_t\qquad \forall t
$$

Límites:

$$
V^{min}\leq V_t\leq V^{max},\qquad 0\leq Q_t\leq Q^{max},\qquad 0\leq P_{gt}^T\leq P_g^{max}
$$

### Actividad

Resuelva el despacho hidrotérmico y reporte volumen, caudal turbinado, vertimiento, generación térmica y energía no servida. Explique cuándo conviene guardar agua y cuándo conviene turbinar.

## Extensión. Dos embalses en cascada

### Datos adicionales

**Embalses**

| embalse   |   v0_hm3 |   vmin_hm3 |   vmax_hm3 |   qmax_hm3 |   produccion_mwh_hm3 |
|:----------|---------:|-----------:|-----------:|-----------:|---------------------:|
| R1        |       70 |         20 |        110 |         30 |                  2.2 |
| R2        |       60 |         15 |        100 |         35 |                  1.8 |

**Afluencias**

| embalse   |   t1 |   t2 |   t3 |   t4 |
|:----------|-----:|-----:|-----:|-----:|
| R1        |   15 |   10 |   12 |   18 |
| R2        |    8 |    7 |    9 |   10 |

**Relación aguas arriba**

| embalse   | aguas_arriba   |
|:----------|:---------------|
| R1        |                |
| R2        | R1             |

Para el embalse aguas abajo, agregue como entrada el caudal turbinado y el vertimiento del embalse aguas arriba. Presente la ecuación modificada y discuta cómo cambia la decisión de operación.

## Evaluación

| Criterio | Ponderación |
|---|---:|
| Balances eléctricos e hidráulicos correctamente formulados | 25 % |
| Representación de límites técnicos, reserva y estados | 25 % |
| Construcción de datos y ejecución de casos | 20 % |
| Interpretación de costo marginal, pérdidas y agua | 20 % |
| Presentación de resultados | 10 % |


## Archivos de datos

| Archivo | Uso |
|---|---|
| `cascada_afluencias.csv` | Tabla editable del caso |
| `cascada_embalses.csv` | Tabla editable del caso |
| `cascada_upstream.csv` | Tabla editable del caso |
| `ed_demanda.csv` | Tabla editable del caso |
| `ed_generadores.csv` | Tabla editable del caso |
| `ed_perdidas_B.csv` | Tabla editable del caso |
| `ed_perdidas_demanda.csv` | Tabla editable del caso |
| `ed_perdidas_generadores.csv` | Tabla editable del caso |
| `ed_tramos.csv` | Tabla editable del caso |
| `ed_tramos_demanda.csv` | Tabla editable del caso |
| `hidrotermico_demanda_afluencia.csv` | Tabla editable del caso |
| `hidrotermico_hidro.csv` | Tabla editable del caso |
| `hidrotermico_termicas.csv` | Tabla editable del caso |
| `hidrotermico_voll.csv` | Tabla editable del caso |
| `uc_demanda_reserva.csv` | Tabla editable del caso |
| `uc_unidades.csv` | Tabla editable del caso |
