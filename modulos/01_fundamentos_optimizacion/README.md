# 01 — Fundamentos de optimización

[Menú principal](../../README.md) · [Ejemplos](ejemplos/README.md) · [Actividades](actividades/README.md) · [Datos](datos/) · [Guía AMPL](../../docs/guia_ampl.md)

## Propósito del módulo

La optimización matemática permite transformar una decisión técnica en un problema resoluble. En sistemas eléctricos esta habilidad es central: antes de despachar generadores, calcular flujos o decidir inversiones, se debe reconocer qué variables se controlan, qué restricciones no pueden violarse y qué criterio define una solución preferible.

El módulo no inicia con redes eléctricas porque primero es necesario dominar la estructura común de los modelos: variables, función objetivo, restricciones, dominio de decisión, factibilidad, optimalidad y sensibilidad.

![Proceso de modelado matemático](figuras/01_proceso_modelado_matematico.svg)

## De una decisión a una formulación

Un problema de optimización se escribe, en forma general, como:

$$
\min_x f(x)
$$

sujeto a:

$$
g_i(x) \leq 0, \qquad h_j(x)=0, \qquad x \in X
$$

La variable $x$ representa la decisión; $f(x)$ mide el desempeño; las restricciones $g_i$ y $h_j$ definen las condiciones técnicas, económicas o físicas; y $X$ establece si las variables son continuas, enteras, binarias o no negativas.

En una formulación bien construida, cada ecuación debe responder a una pregunta: qué se decide, cuánto cuesta o beneficia, qué recurso limita, qué balance debe cumplirse y qué condiciones hacen aceptable la solución.

## Programación lineal

La programación lineal aparece cuando la función objetivo y las restricciones son lineales:

$$
\max \; c^T x
$$

$$
Ax \leq b, \qquad x \geq 0
$$

La región factible es el conjunto de soluciones que cumplen todas las restricciones. Si el problema tiene solución óptima finita, esta ocurre en un vértice de la región factible. Por eso los ejemplos de producción, mezcla y transporte son importantes: permiten ver cómo una restricción de capacidad, demanda o mercado puede volverse activa y determinar la solución.

![Región factible](figuras/02_region_factible.svg)

## Dualidad y sensibilidad

Una restricción activa tiene valor económico porque limita la mejora de la función objetivo. En programación lineal, ese valor se interpreta mediante variables duales o precios sombra. Si una hora adicional de trabajo permite producir más, su valor marginal se mide por cuánto mejora el objetivo al relajar esa restricción.

Esta idea reaparece en sistemas eléctricos: una línea congestionada, una reserva limitada o una capacidad máxima de generación pueden tener precio sombra. Por eso la sensibilidad no es un complemento estadístico, sino una herramienta para interpretar qué restricciones gobiernan el resultado.

![Dualidad y sensibilidad](figuras/08_dualidad_sensibilidad.svg)

## Programación entera mixta

Algunas decisiones no son continuas. Construir una línea, encender una unidad o instalar una antena son decisiones sí/no. Se representan mediante variables binarias:

$$
y_i \in \{0,1\}
$$

Una relación típica entre una decisión binaria y una variable continua es:

$$
x_i \leq M y_i
$$

Si $y_i=0$, la variable continua queda desactivada. Si $y_i=1$, puede tomar un valor hasta $M$. El valor de $M$ debe elegirse con cuidado: si es demasiado pequeño, elimina soluciones válidas; si es excesivo, debilita el modelo.

## No linealidad y convexidad

Los problemas cuadráticos y no lineales aparecen cuando el costo depende de la potencia al cuadrado, cuando se modelan pérdidas o cuando se representa flujo AC. En problemas convexos, un óptimo local también es global; en problemas no convexos, la solución puede depender del punto inicial y de la estrategia de solución.

![Convexidad y no convexidad](figuras/05_convexidad_no_convexidad.svg)

Las condiciones KKT permiten interpretar optimalidad con restricciones. No se usan solo como resultado matemático: explican equilibrio entre gradiente de la función objetivo, restricciones activas y multiplicadores.

![Condiciones KKT](figuras/07_kkt.svg)

## Ejemplos del módulo

| Ejemplo | Decisión principal | Acceso |
|---|---|---|
| Fábrica de pintura | Producción óptima bajo tiempo y mercado | [Abrir](ejemplos/01_fabrica_pintura.md) |
| Producción de acero | Uso de capacidad semanal | [Abrir](ejemplos/02_produccion_acero.md) |
| Transporte de energía | Asignación de oferta a demanda | [Abrir](ejemplos/03_transporte_energia.md) |
| Localización de antenas | Selección binaria de ubicaciones | [Abrir](ejemplos/04_localizacion_antenas.md) |
| Forma matricial | Relación entre modelo algebraico y matriz | [Abrir](ejemplos/05_forma_matricial.md) |

## Actividades

Las actividades del módulo exigen construir la formulación y luego implementarla. No basta con obtener un número: se debe explicar qué restricción es activa, qué recurso limita la solución y cómo cambiaría el resultado si se modifica un dato.

[Ir a actividades](actividades/README.md)

---

[Menú principal](../../README.md) · [Ejemplos](ejemplos/README.md) · [Actividades](actividades/README.md) · [Datos](datos/)
