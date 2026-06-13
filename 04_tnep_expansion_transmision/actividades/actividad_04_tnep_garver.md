# Actividad 04 — TNEP: expansión de transmisión en sistema Garver simplificado

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)


## 0. Revisión previa obligatoria

Antes de desarrollar esta actividad, el estudiante debe revisar los documentos de la carpeta `../modelos/` del bloque correspondiente. La actividad no consiste en copiar el modelo revisado en clase: primero debe replicar su lógica y luego construir una variante, escenario o extensión propia.

## 1. Contexto

La planificación de expansión de transmisión determina qué nuevos circuitos deben construirse para transportar energía
desde las zonas de generación hacia los centros de carga. Esta actividad usa un sistema tipo Garver simplificado para comparar
formulaciones TNEP revisadas previamente en la carpeta `modelos/`.

## 2. Objetivo general

Construir desde cero modelos AMPL de expansión de transmisión, comparar formulaciones de transporte, DC, híbrida y lineal
disyuntiva, e interpretar las decisiones de inversión bajo sensibilidad de demanda y costos.

## 3. Datos del caso

### Tabla 1. Barras, generación máxima y demanda

| Barra | Generación máxima disponible [MW] | Demanda [MW] |
|------:|----------------------------------:|-------------:|
| 1 | 150 | 80  |
| 2 | 0   | 240 |
| 3 | 360 | 40  |
| 4 | 0   | 160 |
| 5 | 0   | 240 |
| 6 | 600 | 0   |

### Tabla 2. Corredores de transmisión

| Corredor | Desde | Hasta | Circuitos existentes | Máx. nuevos | Reactancia x [p.u.] | Capacidad por circuito [MW] | Costo por circuito [kUSD] |
|---------|------:|------:|---------------------:|------------:|--------------------:|----------------------------:|--------------------------:|
| C12 | 1 | 2 | 1 | 3 | 0.40 | 100 | 40 |
| C14 | 1 | 4 | 1 | 3 | 0.60 | 80  | 60 |
| C15 | 1 | 5 | 0 | 3 | 0.20 | 100 | 20 |
| C23 | 2 | 3 | 1 | 3 | 0.20 | 100 | 20 |
| C24 | 2 | 4 | 1 | 3 | 0.40 | 100 | 40 |
| C26 | 2 | 6 | 0 | 3 | 0.30 | 100 | 30 |
| C35 | 3 | 5 | 1 | 3 | 0.20 | 100 | 20 |
| C36 | 3 | 6 | 0 | 3 | 0.30 | 100 | 30 |
| C45 | 4 | 5 | 1 | 3 | 0.40 | 100 | 40 |
| C46 | 4 | 6 | 0 | 3 | 0.30 | 100 | 30 |
| C56 | 5 | 6 | 0 | 3 | 0.20 | 100 | 20 |

### Tabla 3. Parámetros generales

| Parámetro | Valor |
|----------|------:|
| Penalización por energía no servida | 5000 USD/MWh |
| Barra de referencia | 1 |
| Límite angular máximo sugerido | 0.6 rad |
| Demanda total base | 760 MW |

## 4. Trabajo solicitado

El estudiante debe replicar y comparar cuatro formulaciones:

### Parte A. Modelo de transporte

- No considera ángulos.
- Usa balance nodal y límites de flujo.
- Permite representar transporte energético agregado.

### Parte B. Modelo DC

- Usa ángulos de barras.
- Relaciona flujo con diferencia angular y reactancia.
- Considera circuitos existentes y nuevos.

### Parte C. Modelo híbrido

- Representa parte de la red mediante flujo DC y parte mediante transporte, según criterio justificado.
- Debe explicar qué simplificación se adopta y por qué.

### Parte D. Modelo lineal disyuntivo

- Usa variables binarias o enteras para construcción.
- Debe activar restricciones de flujo según circuitos construidos.
- Debe evitar soluciones físicamente inconsistentes.

## 5. Archivos requeridos

```text
actividad_04_tnep_transporte.dat
actividad_04_tnep_dc.dat
actividad_04_tnep_hibrido.dat
actividad_04_tnep_disyuntivo.dat

actividad_04_tnep_transporte.mod
actividad_04_tnep_dc.mod
actividad_04_tnep_hibrido.mod
actividad_04_tnep_disyuntivo.mod

actividad_04.run
actividad_04.out
resultados_actividad_04.xlsx
informe_actividad_04.pdf
```

Si el estudiante decide usar un solo archivo `.dat` con parámetros para todas las formulaciones, debe justificarlo y mantener consistencia.

## 6. Escenarios obligatorios

| Escenario | Modificación |
|----------|--------------|
| Base | Datos originales |
| S1 — Demanda alta | Aumentar demanda de barras 2, 4 y 5 en 20 % |
| S2 — Restricción presupuestaria | Limitar inversión máxima a 140 kUSD |
| S3 — Corredor costoso | Duplicar costo de C15 y C56 |
| S4 — Seguridad reforzada | Exigir que ENS sea cero |
| S5 — Menor capacidad | Reducir capacidad por circuito en 20 % |

## 7. Excel de resultados

### Hoja 1. Datos

Barras, generación, demanda y corredores.

### Hoja 2. Inversión por formulación

| Modelo | Escenario | Corredor | Nuevos circuitos | Costo inversión |
|-------|-----------|----------|-----------------:|----------------:|

### Hoja 3. Resultados operativos

| Modelo | Escenario | ENS total | Costo inversión | Costo ENS | Costo total |
|-------|-----------|----------:|----------------:|----------:|------------:|

### Hoja 4. Gráficos

1. número de circuitos nuevos por corredor;
2. costo total por formulación;
3. ENS por escenario;
4. comparación transporte vs DC vs híbrido vs disyuntivo.

## 8. Preguntas directrices

1. ¿Qué corredores son seleccionados en cada formulación?
2. ¿La solución del modelo de transporte coincide con la del modelo DC? Explique.
3. ¿Qué formulación resulta más restrictiva y por qué?
4. ¿Qué corredores aparecen como estratégicos cuando aumenta la demanda?
5. ¿Qué efecto tiene limitar el presupuesto?
6. ¿Por qué una solución con bajo costo puede no ser eléctricamente aceptable?
7. ¿Qué formulación recomendaría para una planificación real y bajo qué condiciones?

## 9. Criterios de evaluación

Consultar `rubrica_actividad_04.csv`.
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)
