# Planificación y Operación de Sistemas Eléctricos de Potencia

![Portada académica](assets/img/portada_academica_v15.png)

Este repositorio reúne material docente, modelos algebraicos, datos de prueba y scripts de apoyo para estudiar problemas de optimización aplicados a la operación y planificación de sistemas eléctricos de potencia. La secuencia inicia con la formulación matemática de problemas de optimización, continúa con la implementación en AMPL y avanza hacia aplicaciones eléctricas: despacho económico, flujo óptimo de potencia, proyección de demanda, expansión de transmisión y expansión de generación.

El repositorio está pensado para que el estudiante pueda recorrer el curso directamente desde los archivos `README.md`: primero lee la teoría, luego revisa la formulación matemática, identifica los datos requeridos y finalmente ejecuta los modelos o scripts correspondientes.

## Mapa general del curso

![Mapa general del curso](assets/img/mapa_general_curso.png)

La lógica del curso es progresiva. Primero se estudia cómo convertir una decisión técnica en un modelo matemático. Luego se implementa ese modelo en AMPL. Después se incorporan restricciones propias de los sistemas eléctricos: balance de potencia, límites de generación, restricciones de red, reserva, indisponibilidad, hidrología, demanda futura y decisiones de inversión.

## Horizonte temporal de los problemas eléctricos

![Horizonte temporal de SEP](assets/img/horizonte_temporal_sep.png)

El horizonte temporal permite ubicar cada problema en su escala natural. La operación de corto plazo trabaja con horas o días: despacho económico, unit commitment y flujo óptimo de potencia. La planificación trabaja con meses, años o décadas: proyección de demanda, expansión de transmisión y expansión de generación. Esta separación evita mezclar decisiones operativas con decisiones de inversión, aunque ambas se conectan mediante restricciones técnicas y señales económicas.

## Operación y planificación

![Operación vs planificación](assets/img/operacion_vs_planificacion.png)

En operación, la infraestructura se considera dada y se decide cómo utilizarla. En planificación, se decide qué infraestructura construir, cuándo construirla y bajo qué escenarios de demanda, disponibilidad de recursos, costos y confiabilidad. La operación responde a la pregunta “¿cómo uso el sistema existente?”, mientras que la planificación responde “¿qué sistema necesito para atender condiciones futuras?”.

## Flujo de trabajo computacional

![Flujo Python AMPL](assets/img/flujo_python_ampl.png)

El flujo de trabajo recomendado es: preparar datos en hojas de cálculo o archivos CSV, validar y transformar datos con Python, resolver los modelos de optimización en AMPL y analizar resultados nuevamente con Python. Esta separación reproduce una práctica habitual en estudios eléctricos: los datos se documentan, el modelo algebraico se mantiene independiente y los resultados se procesan de forma reproducible.

## Navegación del repositorio

| Módulo | Tema | Enlace |
|---|---|---|
| 01 | Fundamentos de optimización | [Abrir](modulos/01_optimizacion/README.md) |
| 02 | AMPL para modelos eléctricos | [Abrir](modulos/02_ampl/README.md) |
| 03 | Despacho económico y operación de corto plazo | [Abrir](modulos/03_despacho_economico/README.md) |
| 04 | Flujo óptimo de potencia | [Abrir](modulos/04_opf/README.md) |
| 05 | Proyección de demanda | [Abrir](modulos/05_demanda/README.md) |
| 06 | Expansión de transmisión | [Abrir](modulos/06_tnep/README.md) |
| 07 | Expansión de generación | [Abrir](modulos/07_gep/README.md) |


## Criterio didáctico del repositorio

La lógica de trabajo es **datos → formulación → implementación**. Cada módulo contiene datos de entrada en CSV o XLSX y la formulación matemática directamente en su `README.md`. Con esa información, el estudiante debe poder construir su propio archivo `.dat` y su propio archivo `.mod`.

Cuando se incluyen archivos AMPL de referencia, estos sirven para comprobación, discusión docente o depuración. La intención principal no es entregar modelos cerrados, sino mostrar la estructura del problema con datos suficientes para que cada estudiante reproduzca la modelación.

## Organización de cada módulo

Cada módulo mantiene una estructura compacta:

```text
README.md   teoría, formulación, navegación y actividad del tema
ampl/       modelos, datos AMPL y archivos de ejecución, cuando aplica
datos/      archivos CSV o XLSX usados como entrada
python/     scripts auxiliares de lectura, conversión, validación o gráficos, cuando aplica
figuras/    figuras técnicas usadas en el README del módulo
```

La teoría se encuentra directamente en el `README.md` de cada módulo. No se usan carpetas separadas de teoría, guías, actividades o plantillas, para que el recorrido sea directo y navegable.

## Ruta sugerida de trabajo

1. Abrir el `README.md` principal para ubicar el curso y el horizonte temporal.
2. Avanzar por los módulos en orden.
3. En cada módulo, leer primero la teoría y la formulación.
4. Revisar los datos de entrada antes de ejecutar cualquier modelo.
5. Ejecutar los archivos `.run` desde la carpeta `ampl/` del módulo correspondiente.
6. Usar los scripts de Python para preparar datos, exportar archivos `.dat` o graficar resultados.

## Requisitos mínimos

- AMPL con un solver LP/MILP compatible, por ejemplo HiGHS, CBC, CPLEX o Gurobi.
- Python 3.10 o superior para los scripts auxiliares.
- Paquetes usuales de Python: `pandas`, `numpy` y `matplotlib`.
- Editor de texto o entorno de desarrollo para revisar archivos `.mod`, `.dat`, `.run`, `.py` y `.md`.
