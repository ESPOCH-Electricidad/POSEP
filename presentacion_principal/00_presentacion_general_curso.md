# Presentación general del curso

## 1. Propósito de la asignatura

La asignatura estudia cómo formular, implementar y analizar modelos de operación y planificación de sistemas eléctricos de potencia. El énfasis está en convertir decisiones técnicas en modelos matemáticos resolubles y en interpretar sus resultados desde el punto de vista eléctrico, operativo y económico.

## 2. Mapa temporal del sistema eléctrico

| Horizonte | Problema típico | Herramienta principal |
|---|---|---|
| Segundos–minutos | control, estabilidad, regulación primaria | simulación dinámica, control |
| Horas–días | despacho económico, unit commitment, OPF | LP, QP, MILP, NLP |
| Semanas–meses | mantenimiento, hidrología, reservas, operación hidrotermal | programación matemática y escenarios |
| Años | expansión de generación y transmisión | MILP, planificación multietapa |
| Décadas | transición energética, política pública, resiliencia | escenarios, robustez, sensibilidad |

## 3. Ruta de aprendizaje

1. Optimización matemática aplicada.
2. AMPL como lenguaje algebraico.
3. Operación de corto plazo.
4. Flujo óptimo de potencia.
5. Proyección de demanda.
6. Expansión de transmisión.
7. Expansión de generación.

## 4. Flujo de herramientas

Excel organiza datos de entrada. Python valida, transforma y visualiza. AMPL formula y resuelve los modelos. Los resultados vuelven a Python o Excel para análisis, tablas y gráficos.

```text
Excel/CSV → Python → AMPL (.mod/.dat/.run) → Solver → Resultados CSV → Python/Excel
```

## 5. Entregables del curso

- Formulación matemática de cada problema.
- Archivo `.mod` documentado.
- Archivo `.dat` o base de datos de entrada.
- Archivo `.run` reproducible.
- Tabla de resultados.
- Figura técnica de interpretación.
- Discusión de factibilidad, sensibilidad y limitaciones.
