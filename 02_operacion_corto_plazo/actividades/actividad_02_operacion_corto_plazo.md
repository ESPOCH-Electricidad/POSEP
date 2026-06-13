# Actividad 02 — Operación de corto plazo: ED, UC y coordinación hidrotérmica

## 1. Contexto

La operación de corto plazo de un sistema eléctrico exige decidir qué unidades generan, cuánto producen y cómo se cubre
la demanda horaria al menor costo posible, respetando límites técnicos. Esta actividad integra tres niveles de modelación:

1. despacho económico horario;
2. compromiso de unidades con variables binarias;
3. coordinación hidrotérmica simplificada.

El objetivo inicial es replicar los modelos revisados previamente en la carpeta `modelos/` del bloque de operación,
pero construyendo completamente los archivos AMPL desde datos tabulados.

## 2. Objetivo general

Formular e implementar en AMPL un modelo de operación de corto plazo que permita comparar despacho económico,
compromiso de unidades y participación hidroeléctrica bajo distintos escenarios de demanda y disponibilidad.

## 3. Datos del caso

### Tabla 1. Unidades térmicas

| Unidad | Tecnología | Costo variable [USD/MWh] | Pmin [MW] | Pmax [MW] | Rampa subida [MW/h] | Rampa bajada [MW/h] | Costo arranque [USD] | Estado inicial |
|-------|------------|---------------------------|----------:|----------:|--------------------:|--------------------:|---------------------:|---------------|
| T1    | Gas ciclo combinado | 32 | 50 | 180 | 60 | 60 | 1200 | 1 |
| T2    | Vapor térmico       | 45 | 40 | 150 | 50 | 50 | 1800 | 0 |
| T3    | Motor diésel        | 70 | 10 | 80  | 80 | 80 | 400  | 0 |

### Tabla 2. Unidad hidroeléctrica equivalente

| Unidad | Costo variable [USD/MWh] | Pmin [MW] | Pmax [MW] | Energía disponible diaria [MWh] | Factor de disponibilidad |
|-------|---------------------------|----------:|----------:|--------------------------------:|-------------------------:|
| H1    | 5                         | 0         | 120       | 520                             | 1.00 |

### Tabla 3. Demanda horaria

| Hora | Demanda [MW] |
|-----:|-------------:|
| 1 | 180 |
| 2 | 210 |
| 3 | 260 |
| 4 | 300 |
| 5 | 280 |
| 6 | 240 |
| 7 | 220 |
| 8 | 190 |

### Tabla 4. Parámetros operativos generales

| Parámetro | Valor | Unidad |
|----------|------:|--------|
| Reserva mínima | 10 | % de la demanda horaria |
| Penalización por energía no servida | 2500 | USD/MWh |
| Horizonte | 8 | horas |
| Tiempo mínimo encendido | 2 | horas |
| Tiempo mínimo apagado | 1 | horas |

## 4. Trabajo solicitado

### Parte A. Despacho económico horario

Construya un modelo de despacho económico continuo sin variables binarias. Todas las unidades pueden operar entre cero y
su capacidad máxima. Debe incluir balance por hora y energía hidroeléctrica disponible diaria.

### Parte B. Compromiso de unidades

Extienda el modelo para incorporar variables binarias de encendido/apagado para unidades térmicas. Incluya:

- relación entre generación y estado de unidad;
- costos de arranque;
- rampas;
- estado inicial;
- reserva operativa;
- energía no servida penalizada.

### Parte C. Coordinación hidrotérmica simplificada

Incluya la unidad hidroeléctrica como recurso limitado por energía diaria. Analice cómo cambia el despacho térmico cuando
la disponibilidad hidroeléctrica se reduce.

## 5. Archivos que debe entregar el estudiante

```text
actividad_02.dat
actividad_02.mod
actividad_02.run
actividad_02.out
resultados_actividad_02.xlsx
informe_actividad_02.pdf
```

El archivo `.dat` debe ser construido por el estudiante a partir de las tablas. No se entrega un `.dat` resuelto.

## 6. Requerimientos mínimos del archivo `.mod`

El modelo debe incluir:

### Conjuntos

- unidades térmicas;
- unidades hidroeléctricas;
- horas.

### Parámetros

- costos variables;
- costos de arranque;
- límites mínimos y máximos;
- rampas;
- demanda;
- reserva;
- disponibilidad hidroeléctrica;
- penalización ENS.

### Variables

- generación térmica por unidad y hora;
- generación hidroeléctrica por hora;
- estado binario de unidad térmica;
- arranque;
- energía no servida;
- reserva disponible.

### Restricciones

1. balance de potencia por hora;
2. límites de generación;
3. relación generación-estado;
4. rampas;
5. cálculo de arranque;
6. límite de energía hidroeléctrica diaria;
7. reserva mínima;
8. no negatividad y binariedad.

## 7. Escenarios obligatorios

| Escenario | Modificación |
|----------|--------------|
| Base | Datos originales |
| S1 — Demanda alta | Aumentar toda la demanda en 12 % |
| S2 — Combustible caro | Aumentar costo variable de T1, T2 y T3 en 25 % |
| S3 — Hidrología baja | Reducir energía disponible de H1 en 50 % |
| S4 — Sin unidad diésel | Forzar T3 fuera de servicio |
| S5 — Mayor reserva | Aumentar reserva mínima a 18 % |

## 8. Excel de resultados

El Excel debe incluir:

### Hoja 1. Demanda y disponibilidad

Tabla de demanda, reserva requerida y disponibilidad máxima por hora.

### Hoja 2. Despacho por hora

| Escenario | Hora | Pg_T1 | Pg_T2 | Pg_T3 | Pg_H1 | ENS | Costo horario |
|----------|-----:|------:|------:|------:|------:|----:|--------------:|

### Hoja 3. Compromiso de unidades

| Escenario | Hora | u_T1 | u_T2 | u_T3 | startup_T1 | startup_T2 | startup_T3 |
|----------|-----:|-----:|-----:|-----:|-----------:|-----------:|-----------:|

### Hoja 4. Gráficos

Debe contener:

1. curva de demanda vs generación total;
2. generación por tecnología;
3. costo horario por escenario;
4. estado de unidades térmicas;
5. energía hidroeléctrica utilizada.

## 9. Preguntas directrices

1. ¿Qué unidad térmica define el costo del sistema en las horas pico?
2. ¿Qué cambia entre el despacho económico continuo y el compromiso de unidades?
3. ¿En qué horas la restricción de reserva modifica el despacho?
4. ¿Cómo se utiliza el recurso hidroeléctrico cuando es escaso?
5. ¿La energía no servida aparece en algún escenario? ¿Qué significa?
6. ¿Qué escenario produce mayor costo operativo y por qué?
7. ¿Qué limitaciones tendría este modelo para aplicarse a un sistema real?

## 10. Criterios de evaluación

Consultar `rubrica_actividad_02.csv`.
