# 01 — Fundamentos de optimización

[Menú principal](../../README.md) · [Actividades](actividades/README.md) · [Datos](datos/) · [Guía AMPL](../../docs/guia_ampl.md)

## Propósito del módulo

La optimización matemática permite transformar una decisión técnica en un problema resoluble. En sistemas eléctricos esta idea aparece en decisiones de despacho, transporte de energía, ubicación de equipos, selección de inversiones y operación de recursos limitados. Antes de escribir código, el estudiante debe aprender a reconocer qué se decide, qué se conoce, qué se optimiza y qué restricciones no pueden violarse.

Un modelo no inicia con el solver; inicia con el enunciado. A partir del enunciado se identifican variables de decisión, parámetros, función objetivo, restricciones y dominio de las variables. Esta separación evita confundir datos con decisiones y permite revisar si el resultado tiene sentido físico o económico.

## De la decisión al modelo

Un problema general puede escribirse como:

$$
\min_x f(x)
$$

sujeto a:

$$
g_i(x)\leq 0,\qquad h_j(x)=0,\qquad x\in\mathcal{X}.
$$

El vector $x$ contiene las decisiones. La función $f(x)$ representa el criterio de comparación entre alternativas: costo, beneficio, pérdidas, energía no servida o una combinación de estos términos. Las restricciones $g_i(x)$ y $h_j(x)$ representan límites de recursos, balances, condiciones técnicas o reglas de operación. El conjunto $\mathcal{X}$ define el dominio de las variables: continuas, enteras, binarias, no negativas o acotadas.

En programación lineal, la función objetivo y las restricciones son lineales. En estos problemas, si existe una solución óptima finita, al menos una solución óptima se encuentra en un vértice de la región factible. Esta propiedad permite interpretar gráficamente casos pequeños y entender por qué las restricciones activas determinan la solución.

$$
\min c^Tx \qquad \text{sujeto a}\qquad Ax\leq b,\; x\geq 0.
$$

La forma matricial es importante porque los lenguajes algebraicos, como AMPL, escriben modelos con índices, pero el solver recibe una estructura matricial. Por eso la consistencia de dimensiones entre conjuntos, parámetros y variables es tan importante como la ecuación matemática.

## Dualidad, sensibilidad y dominio de variables

El multiplicador dual de una restricción mide cómo cambia el valor óptimo cuando se modifica el lado derecho de esa restricción. En problemas eléctricos esta interpretación reaparece como valor marginal de capacidad, recurso, demanda o congestión. Una restricción activa limita la solución; una restricción con holgura no modifica el óptimo localmente.

Para problemas diferenciables con restricciones, el Lagrangiano se define como:

$$
\mathcal{L}(x,\lambda,\mu)=f(x)+\sum_i\lambda_i g_i(x)+\sum_j\mu_jh_j(x).
$$

Las condiciones KKT combinan factibilidad, estacionariedad, dualidad y complementariedad:

$$
\lambda_i g_i(x^*)=0.
$$

La programación entera mixta aparece cuando parte de las decisiones son discretas. Una variable binaria permite modelar decisiones de selección, construcción, encendido o activación:

$$
y\in\{0,1\},\qquad x\leq My.
$$

El parámetro $M$ debe escogerse con cuidado: un valor demasiado pequeño elimina soluciones factibles y uno demasiado grande puede deteriorar la solución numérica.

## Lectura técnica de las figuras

![Proceso de modelado](figuras/01_proceso_modelado_matematico.svg)

El proceso de modelado empieza en el problema real, pasa por la definición algebraica y termina en la interpretación del resultado. La figura debe usarse para verificar que ninguna etapa se omita: datos, variables, restricciones, solución y lectura técnica.

![Región factible](figuras/02_region_factible.svg)

La región factible muestra las combinaciones de decisión que cumplen todas las restricciones. En un problema lineal de dos variables, el óptimo se ubica en un vértice; en modelos eléctricos reales, esta idea se conserva aunque la dimensión sea mucho mayor.

![Tipos de programación](figuras/06_tipos_programacion.svg)

La clasificación LP, MILP, QP, NLP y MINLP no es solo formal. Define el tipo de solver, el nivel de dificultad y la forma de validar optimalidad. Un despacho lineal, un unit commitment y un OPF-AC no tienen la misma estructura matemática.

## Ejemplos del módulo

| Recurso | Concepto principal | Acceso |
|---|---|---|
| Fábrica de pintura | programación lineal, recursos y utilidad | [Abrir](ejemplos/01_fabrica_pintura.md) |
| Producción de acero | mezcla de productos y restricciones de capacidad | [Abrir](ejemplos/02_produccion_acero.md) |
| Transporte de energía | flujos entre fuentes y cargas | [Abrir](ejemplos/03_transporte_energia.md) |
| Localización de antenas | decisión binaria y cobertura mínima | [Abrir](ejemplos/04_localizacion_antenas.md) |
| Forma matricial | relación entre formulación algebraica y solver | [Abrir](ejemplos/05_forma_matricial.md) |

## Actividad del módulo

Desarrolle las actividades del módulo desde [actividades/README.md](actividades/README.md). En cada caso, entregue la formulación, el archivo de datos construido desde las tablas, el archivo de ejecución, resultados y una validación de factibilidad.

---

[Menú principal](../../README.md) · [Actividades](actividades/README.md) · [Datos](datos/)
