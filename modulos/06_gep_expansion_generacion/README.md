# 06 — Expansión de generación

[Menú principal](../../README.md) · [Actividades](actividades/README.md) · [Datos](datos/) · [Guía AMPL](../../docs/guia_ampl.md)

## Propósito del módulo

La expansión de generación decide qué tecnologías incorporar, cuánta capacidad instalar y en qué momento hacerlo para atender la demanda futura. A diferencia del despacho económico, aquí la capacidad no es un dato fijo: es una decisión de inversión. Por esa razón el modelo combina costos de construcción, costos fijos, costos variables, disponibilidad, reserva, bloques de carga y penalización por energía no servida.

El resultado de un GEP no debe interpretarse solo como una lista de MW instalados. La capacidad instalada tiene distinto valor según la tecnología, su disponibilidad, su contribución firme y el momento en que produce energía. Una planta solar, una unidad térmica y una hidroeléctrica pueden tener la misma capacidad nominal, pero no aportan el mismo servicio al sistema durante el pico o en condiciones críticas.

## De la demanda futura al requerimiento de capacidad

El módulo de demanda entrega insumos para expansión: demanda pico, energía anual y bloques representativos. La demanda pico condiciona reserva y suficiencia; la energía y los bloques condicionan operación, costos variables y utilización esperada de cada tecnología. En modelos con bloques de carga, cada bloque $b$ tiene una demanda $D_{y,b}$ y una duración $h_b$.

El balance de energía por bloque puede escribirse como:

$$
\sum_k Gen_{k,y,b}+ENS_{y,b}=D_{y,b}\,h_b.
$$

La generación de cada tecnología está limitada por capacidad, disponibilidad y duración del bloque:

$$
Gen_{k,y,b}\leq AF_k\,Cap_{k,y}\,h_b.
$$

Esta restricción evita que una tecnología produzca más energía de la que permite su capacidad efectiva en el bloque considerado.

## Inversión, capacidad acumulada y reserva firme

En un modelo multianual, la capacidad total de una tecnología se acumula con las inversiones realizadas en años previos:

$$
Cap_{k,y}=Cap_{k,y-1}+Build_{k,y}.
$$

Si existe capacidad inicial, la ecuación debe iniciar desde el parque existente. Si existe retiro de unidades, debe agregarse un término de retiro o vida útil.

La suficiencia de capacidad se representa con una restricción de reserva firme:

$$
\sum_k FC_k Cap_{k,y}\geq(1+RM)D_y^{peak}.
$$

El parámetro $FC_k$ es el crédito firme de la tecnología. Esta diferencia es fundamental: no toda la capacidad instalada puede contarse como capacidad disponible en el pico. La restricción obliga a que el sistema cuente con capacidad confiable suficiente para cubrir demanda máxima más margen de reserva.

## Función objetivo de expansión

Una función objetivo típica minimiza inversión anualizada, costos fijos, costos variables y penalización por energía no servida:

$$
\min Z=\sum_{k,y}CRF_k I_k Build_{k,y}+\sum_{k,y}FOM_k Cap_{k,y}+\sum_{k,y,b}VOM_k Gen_{k,y,b}+\sum_{y,b}VOLL\,ENS_{y,b}.
$$

El término de inversión anualizada permite comparar tecnologías con distintos costos de capital. El costo fijo depende de la capacidad disponible. El costo variable depende de la energía generada. El VOLL permite medir el costo de no suministrar energía, pero debe ser suficientemente alto para que el racionamiento no se use como sustituto barato de inversión cuando el objetivo es planificar suficiencia.

## Screening curve y bloques de carga

La screening curve es una herramienta previa al modelo de optimización. Compara tecnologías según costo fijo anual y costo variable para identificar en qué rangos de utilización una tecnología podría ser competitiva. No reemplaza al GEP, porque no representa red, reserva, disponibilidad, límites de construcción ni escenarios, pero ayuda a interpretar por qué tecnologías de alto CAPEX pueden ser atractivas con muchas horas de uso y tecnologías de bajo CAPEX pueden ser útiles para pocas horas de punta.

La curva de duración de carga permite convertir un perfil horario en bloques. Esta simplificación reduce el tamaño del modelo, pero debe conservar información suficiente sobre demanda base, media y pico. Si los bloques son mal definidos, el modelo puede subestimar necesidades de flexibilidad o capacidad firme.

## Lectura técnica de las figuras

![Demanda futura](figuras/01_demanda_futura_energia_pico.svg)

La figura relaciona energía y demanda pico. En GEP ambos datos son necesarios: la energía influye en operación y el pico influye en reserva y capacidad firme.

![Curva de duración de carga](figuras/02_curva_duracion_carga.svg)

La curva de duración ordena la demanda de mayor a menor y permite construir bloques representativos. Los bloques deben conservar la información operativa relevante sin volver innecesariamente grande el modelo.

![Screening curve](figuras/03_screening_curve.svg)

La screening curve permite comparar tecnologías por horas equivalentes de operación. Es una lectura económica previa que ayuda a interpretar los resultados del modelo de expansión.

![Reserva firme](figuras/04_reserva_firme.svg)

La reserva firme distingue capacidad nominal y capacidad confiable. Esta distinción es central para tecnologías variables y para sistemas donde el pico ocurre en horas de baja disponibilidad renovable.

## Modelos del módulo

| Recurso | Concepto principal | Acceso |
|---|---|---|
| GEP estático de capacidad | inversión para un año objetivo | [Abrir](modelos/01_modelo_gep_estatico_capacidad.md) |
| GEP con bloques de carga | inversión y operación representativa | [Abrir](modelos/02_modelo_gep_bloques_carga.md) |
| GEP multianual | acumulación de capacidad en el horizonte | [Abrir](modelos/03_modelo_gep_multianual.md) |

## Actividad del módulo

La actividad se desarrolla desde [actividades/README.md](actividades/README.md). El estudiante debe formular un GEP, construir los datos desde las tablas de tecnologías, años y bloques, resolver un caso base, reportar capacidad nueva y comparar el resultado con una variación de demanda, reserva o costo de inversión.

---

[Menú principal](../../README.md) · [Actividades](actividades/README.md) · [Datos](datos/)
