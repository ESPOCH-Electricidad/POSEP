# Planificación y Operación de Sistemas Eléctricos de Potencia

![Banner del repositorio](docs/img/banner_operacion_planificacion_sep.svg)

[Guía docente](docs/guia_docente.md) · [Ruta de aprendizaje](docs/ruta_aprendizaje.md) · [Evaluación](docs/evaluacion.md) · [Guía AMPL](docs/guia_ampl.md)

## Presentación

Este repositorio reúne material docente para estudiar problemas de operación y planificación de sistemas eléctricos de potencia mediante formulación matemática, datos de trabajo y modelación computacional. La intención es que cada tema pueda trabajarse como una unidad de clase: primero se revisan los fundamentos, luego se estudian los modelos, se preparan los datos y finalmente se desarrolla una actividad evaluable.

El curso parte de optimización matemática y avanza hacia aplicaciones eléctricas: despacho económico, compromiso de unidades, despacho hidrotérmico, flujo óptimo de potencia, proyección de demanda, expansión de transmisión y expansión de generación. Los datos incluidos en cada módulo están pensados para que el estudiante construya sus propios archivos de entrada y verifique sus resultados con criterios técnicos.

## Operación y planificación de sistemas eléctricos

En operación se decide cómo utilizar los recursos existentes para atender la demanda en el corto plazo. Las decisiones típicas son la generación de cada unidad, el encendido o apagado de centrales, la asignación de reserva, el uso del agua en embalses, el flujo por líneas y la gestión de congestión.

En planificación se decide cómo preparar el sistema para condiciones futuras. La demanda deja de ser un dato fijo y se convierte en una variable de estudio; a partir de ella se evalúan refuerzos de red, nuevas tecnologías de generación, suficiencia de capacidad, confiabilidad y costo de inversión.

![Operación y planificación](docs/img/operacion_vs_planificacion.svg)

## Horizonte temporal de las decisiones

Las herramientas del curso se organizan según el horizonte de decisión. En horas o días se estudian problemas de operación. En meses y años se preparan datos de demanda, disponibilidad y escenarios. En horizontes multianuales se formulan problemas de expansión de transmisión y generación.

![Horizonte temporal](docs/img/horizonte_temporal_sep.svg)

## Ruta del curso

![Mapa general del curso](docs/img/mapa_general_curso.svg)

| Módulo | Tema | Enlace |
|---:|---|---|
| 01 | Fundamentos de optimización | [Abrir](modulos/01_fundamentos_optimizacion/README.md) |
| 02 | Operación de corto plazo | [Abrir](modulos/02_operacion_corto_plazo/README.md) |
| 03 | Flujo óptimo de potencia | [Abrir](modulos/03_opf_flujo_optimo_potencia/README.md) |
| 04 | Proyección de demanda eléctrica | [Abrir](modulos/04_proyeccion_demanda/README.md) |
| 05 | Expansión de transmisión | [Abrir](modulos/05_tnep_expansion_transmision/README.md) |
| 06 | Expansión de generación | [Abrir](modulos/06_gep_expansion_generacion/README.md) |

## Python y AMPL

Python se utiliza para revisar datos, preparar tablas, estimar demanda, construir escenarios y generar figuras. AMPL se utiliza para escribir modelos algebraicos de optimización y resolverlos con un solver adecuado. En las actividades, el estudiante debe traducir la formulación matemática a archivos `.mod`, preparar sus datos en `.dat` o desde tablas CSV, y ejecutar el caso con un archivo `.run`.

![Flujo Python AMPL](docs/img/flujo_python_ampl.svg)

## Cómo trabajar cada módulo

1. Leer el README del módulo para entender el problema técnico.
2. Revisar los ejemplos o modelos asociados.
3. Identificar conjuntos, índices, parámetros, variables, función objetivo y restricciones.
4. Usar los datos suministrados para preparar el archivo de entrada.
5. Implementar el modelo en AMPL o el flujo de análisis en Python, según corresponda.
6. Validar que los resultados respeten unidades, balances, límites técnicos y sentido económico.
7. Presentar resultados con tablas, figuras y una interpretación técnica.

## Licencia y citación

Consulte [LICENSE.md](LICENSE.md), [CITATION.cff](CITATION.cff) y [CONTRIBUTING.md](CONTRIBUTING.md).
