# Actividad 05 — GEP: planificación de expansión de generación multianual

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/ruta_aprendizaje.md) · [Modelos](../../docs/mapa_modelos.md) · [Casos](../../docs/mapa_casos.md) · [Evaluación](../../docs/evaluacion.md)


## 0. Revisión previa obligatoria

Antes de desarrollar esta actividad, el estudiante debe revisar los documentos de la carpeta `../modelos/` del bloque correspondiente. La actividad no consiste en copiar el modelo revisado en clase: primero debe replicar su lógica y luego construir una variante, escenario o extensión propia.

## 1. Contexto

La planificación de expansión de generación decide qué tecnologías deben incorporarse al sistema, en qué periodo y con qué
capacidad, para cubrir crecimiento de demanda, criterios de reserva, costos de inversión y operación, y confiabilidad.
Esta actividad representa el núcleo de la asignatura porque conecta modelación matemática, datos de entrada, operación por
bloques y análisis de decisiones de largo plazo.

## 2. Objetivo general

Formular, implementar y analizar un modelo GEP multianual en AMPL, construyendo desde cero archivos `.dat`, `.mod`, `.run`
y `.out`, y evaluando escenarios de demanda, hidrología, costos y emisiones.

## 3. Datos del caso de estudio

Se considera un sistema simplificado con tres años de planificación y tres bloques de demanda por año.

### Tabla 1. Años de planificación

| Año | Factor de crecimiento de demanda |
|----:|---------------------------------:|
| 2026 | 1.00 |
| 2030 | 1.18 |
| 2035 | 1.38 |

### Tabla 2. Bloques de demanda

| Bloque | Duración [h/año] | Factor de demanda |
|-------|------------------:|------------------:|
| Pico  | 900  | 1.00 |
| Medio | 3500 | 0.72 |
| Bajo  | 4360 | 0.48 |

Demanda pico base 2026: **520 MW**.

### Tabla 3. Generación existente

| Planta | Tecnología | Capacidad [MW] | Costo variable [USD/MWh] | Factor disponibilidad | Emisiones [tCO2/MWh] |
|-------|------------|---------------:|---------------------------:|----------------------:|----------------------:|
| E_Hidro | Hidro | 220 | 6  | 0.70 | 0.00 |
| E_Gas   | Gas   | 180 | 35 | 0.90 | 0.45 |
| E_Diesel| Diésel| 80  | 90 | 0.85 | 0.78 |

### Tabla 4. Tecnologías candidatas

| Tecnología | Tamaño módulo [MW] | CAPEX [kUSD/MW] | FOM [kUSD/MW-año] | Costo variable [USD/MWh] | Factor disponibilidad | Crédito firme | Emisiones [tCO2/MWh] | Máx. módulos |
|------------|-------------------:|----------------:|------------------:|--------------------------:|----------------------:|--------------:|----------------------:|-------------:|
| CCGT       | 100 | 900  | 18 | 38 | 0.90 | 0.90 | 0.42 | 5 |
| Solar      | 50  | 650  | 10 | 0  | 0.28 | 0.20 | 0.00 | 8 |
| Eólica     | 50  | 1100 | 22 | 0  | 0.38 | 0.25 | 0.00 | 6 |
| BESS       | 25  | 500  | 8  | 2  | 0.85 | 0.60 | 0.00 | 6 |

### Tabla 5. Parámetros económicos y técnicos

| Parámetro | Valor | Unidad |
|----------|------:|--------|
| Tasa de descuento | 8 | % |
| Margen de reserva | 15 | % sobre demanda pico |
| Penalización ENS | 6000 | USD/MWh |
| Límite emisiones base | 1600 | ktCO2 acumuladas |
| Vida útil representativa | 25 | años |
| Presupuesto máximo por año | 250000 | kUSD |

## 4. Trabajo solicitado

### Parte A. Modelo GEP base

Construya un modelo que minimice:

```text
costo de inversión + costo fijo + costo operativo + penalización por ENS
```

Debe incluir:

- construcción de módulos por tecnología y año;
- capacidad acumulada;
- operación por año, bloque y tecnología;
- balance de energía por bloque;
- límites de generación por disponibilidad;
- reserva firme;
- energía no servida;
- presupuesto anual.

### Parte B. Modelo GEP con restricción ambiental

Agregue cálculo de emisiones y límite acumulado.

### Parte C. Análisis multiescenario

Resolver escenarios de demanda, hidrología, costos y emisiones.

## 5. Archivos requeridos

```text
actividad_05_gep.dat
actividad_05_gep.mod
actividad_05_gep.run
actividad_05_gep.out
resultados_actividad_05.xlsx
informe_actividad_05.pdf
```

## 6. Escenarios obligatorios

| Escenario | Modificación |
|----------|--------------|
| Base | Datos originales |
| S1 — Alta demanda | Aumentar demanda pico base a 580 MW |
| S2 — Hidrología baja | Reducir disponibilidad de E_Hidro de 0.70 a 0.45 |
| S3 — Solar competitiva | Reducir CAPEX solar en 30 % |
| S4 — Gas caro | Aumentar costo variable CCGT y E_Gas en 35 % |
| S5 — Carbono restringido | Reducir límite de emisiones acumuladas a 1000 ktCO2 |
| S6 — Presupuesto restringido | Reducir presupuesto máximo anual a 160000 kUSD |

## 7. Excel de resultados

### Hoja 1. Datos

Años, bloques, generación existente y tecnologías candidatas.

### Hoja 2. Capacidad

| Escenario | Año | Tecnología | Nueva capacidad [MW] | Capacidad acumulada [MW] |
|----------|----:|------------|---------------------:|--------------------------:|

### Hoja 3. Operación

| Escenario | Año | Bloque | Tecnología | Generación [MWh] | ENS [MWh] |
|----------|----:|--------|------------|-----------------:|----------:|

### Hoja 4. Costos y emisiones

| Escenario | Costo inversión | Costo fijo | Costo operativo | Costo ENS | Costo total | Emisiones |
|----------|----------------:|------------:|----------------:|----------:|------------:|----------:|

### Hoja 5. Gráficos

Debe incluir:

1. nueva capacidad por tecnología y año;
2. capacidad acumulada por año;
3. generación por tecnología;
4. costo total por escenario;
5. ENS por escenario;
6. emisiones acumuladas.

## 8. Preguntas directrices

1. ¿Qué tecnología se construye primero y por qué?
2. ¿La solución está dominada por inversión, operación o reserva?
3. ¿Qué ocurre con la expansión cuando se reduce disponibilidad hidroeléctrica?
4. ¿Cómo cambia la solución cuando el CAPEX solar disminuye?
5. ¿Qué escenario produce mayor ENS?
6. ¿La restricción ambiental cambia la mezcla tecnológica?
7. ¿Qué tecnología aporta capacidad firme y cuál aporta energía barata?
8. ¿Qué limitaciones tiene este GEP simplificado frente a un sistema real?

## 9. Evaluación

Consultar `rubrica_actividad_05.csv`.
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/ruta_aprendizaje.md) · [Modelos](../../docs/mapa_modelos.md) · [Casos](../../docs/mapa_casos.md) · [Evaluación](../../docs/evaluacion.md)
