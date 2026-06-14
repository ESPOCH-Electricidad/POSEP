# Planificación y Operación de Sistemas Eléctricos de Potencia

![Banner del curso](docs/img/banner_operacion_planificacion_sep.svg)

[Guía docente](docs/guia_docente.md) · [Ruta de aprendizaje](docs/ruta_aprendizaje.md) · [Evaluación](docs/evaluacion.md) · [Guía AMPL](docs/guia_ampl.md)

## Presentación

Este repositorio acompaña el estudio de problemas de operación y planificación de sistemas eléctricos de potencia mediante formulación matemática, datos de trabajo y actividades de modelación. El recorrido no está pensado como un conjunto de archivos sueltos: cada módulo presenta el problema técnico, desarrolla los fundamentos necesarios, organiza los datos del caso y propone una actividad para que el estudiante construya sus propios archivos de trabajo.

La asignatura avanza desde la formulación de problemas de optimización hasta modelos de despacho, flujo óptimo de potencia, proyección de demanda, expansión de transmisión y expansión de generación. Python se usa para análisis de datos y visualización; AMPL se usa para expresar modelos algebraicos de optimización con claridad y reproducibilidad.

## Operación y planificación

La operación decide cómo utilizar recursos disponibles: generación, reservas, unidades encendidas, transferencias por la red, tensiones, congestión y uso del agua en centrales hidroeléctricas. La planificación decide qué infraestructura se requiere en el futuro: refuerzos de red, nueva generación, reserva, suficiencia y escenarios de demanda.

![Operación y planificación](docs/img/operacion_vs_planificacion.svg)

La diferencia entre ambas escalas no es solo temporal. En operación predominan restricciones de corto plazo y costos variables; en planificación aparecen inversiones, vida útil, incertidumbre, crecimiento de demanda y suficiencia de capacidad.

## Horizonte temporal

El curso conecta decisiones que van desde horas hasta años. En el corto plazo, la demanda se trata como un dato horario o un pronóstico inmediato. En el largo plazo, la demanda se convierte en una trayectoria que debe justificarse mediante escenarios y supuestos técnicos.

![Horizonte temporal](docs/img/horizonte_temporal_sep.svg)

## Ruta del curso

![Mapa general del curso](docs/img/mapa_general_curso.svg)

| Módulo | Tema | Entrada principal |
|---:|---|---|
| 01 | Fundamentos de optimización | [Abrir módulo](modulos/01_fundamentos_optimizacion/README.md) |
| 02 | Operación de corto plazo | [Abrir módulo](modulos/02_operacion_corto_plazo/README.md) |
| 03 | Flujo óptimo de potencia | [Abrir módulo](modulos/03_opf_flujo_optimo_potencia/README.md) |
| 04 | Proyección de demanda eléctrica | [Abrir módulo](modulos/04_proyeccion_demanda/README.md) |
| 05 | Expansión de transmisión | [Abrir módulo](modulos/05_tnep_expansion_transmision/README.md) |
| 06 | Expansión de generación | [Abrir módulo](modulos/06_gep_expansion_generacion/README.md) |

## Flujo de trabajo computacional

El flujo recomendado es: leer el enunciado, identificar conjuntos e índices, ordenar los datos, escribir la formulación, construir el archivo de datos y resolver el modelo. Los resultados se validan comparando balance, límites, costos, capacidad, energía no servida y sensibilidad de los principales parámetros.

![Flujo Python AMPL](docs/img/flujo_python_ampl.svg)

## Cómo trabajar cada módulo

1. Leer el problema técnico y los fundamentos del módulo.
2. Revisar las ecuaciones y comprobar el significado de cada variable.
3. Abrir los datos del caso y verificar unidades.
4. Construir el archivo `.dat` a partir de las tablas disponibles.
5. Implementar el modelo en `.mod` siguiendo la formulación matemática.
6. Crear un archivo `.run` para cargar datos, seleccionar solver, resolver y reportar resultados.
7. Presentar un informe breve con formulación, resultados, validación y análisis técnico.

## Licencia y citación

Consulte [LICENSE.md](LICENSE.md), [CITATION.cff](CITATION.cff) y [CONTRIBUTING.md](CONTRIBUTING.md).
