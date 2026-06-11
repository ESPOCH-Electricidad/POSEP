# Planificación y Operación de Sistemas Eléctricos de Potencia

Repositorio docente para organizar **casos de estudio, datos de prueba, guías, actividades, notebooks y recursos de IA** aplicados a la operación y planificación de sistemas eléctricos de potencia.

> **Criterio de publicación:** este repositorio público prioriza datos, documentación y actividades. Los modelos AMPL completos (`.mod`) y archivos de ejecución (`.run`) pueden mantenerse en la plataforma institucional o en repositorios privados del docente.

## Propósito

- Facilitar el aprendizaje progresivo de modelos de optimización aplicados a sistemas eléctricos.
- Disponer de casos de prueba reutilizables: Garver, IEEE 14, IEEE 24 RTS y sistemas didácticos.
- Integrar actividades de análisis, evaluación formativa y uso crítico de IA.
- Documentar cada modelo matemático en términos de **conjuntos, índices, parámetros, variables, función objetivo y restricciones**.

## Bloques del repositorio

| Bloque | Carpeta | Contenido principal | Finalidad didáctica |
|---|---|---|---|
| Fundamentos | `01_fundamentos_optimizacion` | LP, MILP, NLP, formulación matemática | Entender la estructura de un problema de optimización antes de modelar SEP |
| Operación | `02_operacion_corto_plazo` | ED, ED con pérdidas, UC, despacho hidrotérmico | Modelar decisiones operativas de corto plazo |
| OPF | `03_opf_flujo_optimo_potencia` | OPF-DC, OPF-AC | Relacionar optimización con restricciones de red |
| TNEP | `04_tnep_expansion_transmision` | Transporte, DC, híbrido, lineal disyuntivo | Decidir expansión de transmisión y comparar formulaciones |
| GEP | `05_gep_expansion_generacion` | Base, estático con bloques, multianual | Decidir expansión de generación por tecnología y periodo |
| Casos | `06_casos_de_estudio` | Garver, IEEE 14, IEEE 24 RTS, sistemas didácticos | Reutilizar datos comunes en varios modelos |
| Presentaciones | `07_presentaciones` | Beamer/Overleaf, HTML, material multimedia | Convertir materiales técnicos en recursos docentes |
| Evaluación | `08_actividades_y_evaluacion` | Actividades, rúbricas, cuestionarios | Evaluar ejecución, interpretación y pensamiento crítico |
| IA | `09_ia_aplicada_docencia` | Prompts, respuestas revisadas, errores IA | Documentar cómo se usó IA y cómo fue validada |

## Cómo usar este repositorio

1. Revisa `00_guia_general/guia_estudiante.md`.
2. Selecciona el bloque del curso.
3. Lee la formulación matemática del modelo.
4. Explora los datos del caso de estudio.
5. Ejecuta el notebook de apoyo si está disponible.
6. Ejecuta el modelo AMPL entregado por el docente en la plataforma institucional.
7. Compara, interpreta y documenta resultados.
8. Responde la actividad o evaluación correspondiente.

## Nota sobre reproducibilidad

Los notebooks incluidos están diseñados para lectura, validación, visualización de datos y ejemplos mínimos. La ejecución completa de AMPL puede realizarse en local o en Google Colab con `amplpy`, según indique el docente.

## Licencia sugerida

- Material didáctico: Creative Commons Attribution 4.0 International (CC BY 4.0), salvo que se indique otra cosa.
- Notebooks y scripts auxiliares: MIT License.
- Casos externos: respetar la licencia y cita de la fuente original.
