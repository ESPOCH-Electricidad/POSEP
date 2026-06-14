# 06 — Expansión de generación

[Menú principal](../../README.md) · [Modelos](modelos/README.md) · [Actividades](actividades/README.md) · [Datos](datos/) · [Guía AMPL](../../docs/guia_ampl.md)

## Propósito del módulo

La expansión de generación decide qué tecnologías construir, cuánta capacidad instalar y en qué momento hacerlo. La decisión debe atender energía, demanda máxima y reserva, pero también debe reconocer que no toda la capacidad instalada aporta la misma firmeza. Una central térmica despachable, una planta solar y un parque eólico pueden tener el mismo MW instalado, pero no el mismo aporte en horas críticas.

## Demanda futura y bloques de carga

El GEP no necesita representar necesariamente las 8760 horas si el objetivo es una práctica introductoria. Una curva de duración de carga permite agrupar horas con demanda similar en bloques representativos. Cada bloque $b$ tiene demanda $D_b$ y duración $h_b$.

![Curva de duración de carga](figuras/02_curva_duracion_carga.svg)

La energía atendida en un bloque depende de su duración. Por eso la restricción de generación no debe escribirse solo en MW si la variable representa energía:

$$
Gen_{k,b}\leq AF_k Cap_k h_b
$$

Donde $AF_k$ representa disponibilidad o factor de aporte energético de la tecnología.

## Costos de inversión y costos operativos

El costo de una tecnología no se mide únicamente por su CAPEX. El modelo debe combinar inversión anualizada, costo fijo, costo variable y penalización por energía no servida:

$$
\min Z=\sum_k CRF\,Capex_k\,Build_k + \sum_k FOM_k Cap_k + \sum_{k,b} VOM_k Gen_{k,b} + \sum_b VOLL\,ENS_b
$$

El CRF convierte la inversión en un costo anual equivalente. El costo fijo depende de la capacidad disponible, mientras que el costo variable depende de la energía generada. La energía no servida se penaliza para evitar que el modelo atienda demanda incumplida como si fuera una alternativa normal.

## Capacidad existente, nueva inversión y capacidad acumulada

La capacidad total resulta de sumar capacidad existente e inversión nueva:

$$
Cap_k=ExistingCap_k+Build_k
$$

En un modelo multianual, la capacidad depende de decisiones acumuladas:

$$
Cap_{k,y}=ExistingCap_{k,y}+\sum_{\tau\leq y} Build_{k,\tau}
$$

Esta ecuación es esencial porque una planta construida en un año sigue disponible en años posteriores, salvo que se modele retiro por vida útil.

## Reserva firme y suficiencia

La suficiencia de capacidad no se evalúa con capacidad instalada total, sino con capacidad firme. El crédito firme $FC_k$ mide qué fracción de la capacidad puede considerarse disponible para cubrir demanda pico:

$$
\sum_k FC_k Cap_{k,y}\geq (1+RM)D_y^{peak}
$$

![Reserva firme](figuras/04_reserva_firme.svg)

Esta restricción explica por qué una tecnología barata por MWh puede no reemplazar completamente a una tecnología despachable si su aporte firme es bajo.

## Screening curve

Antes de resolver un GEP, las curvas de selección permiten comparar tecnologías según horas de uso. Una tecnología con alto CAPEX y bajo costo variable puede ser conveniente para muchas horas; una con bajo CAPEX y alto costo variable puede ser conveniente para pocas horas.

![Screening curve](figuras/03_screening_curve.svg)

Esta figura no reemplaza al modelo de expansión, pero ayuda a interpretar el resultado: base, media y punta suelen requerir tecnologías distintas.

## Modelos del módulo

| Modelo | Pregunta que responde | Acceso |
|---|---|---|
| GEP estático | Cuánta capacidad instalar en un año objetivo | [Abrir](modelos/01_modelo_gep_estatico_capacidad.md) |
| GEP con bloques | Cómo se usa la capacidad en demanda base, media y punta | [Abrir](modelos/02_modelo_gep_bloques_carga.md) |
| GEP multianual | Cuándo instalar capacidad durante el horizonte | [Abrir](modelos/03_modelo_gep_multianual.md) |

## Actividad

La actividad del módulo exige formular un GEP con tecnologías candidatas, bloques de carga y reserva firme. El estudiante debe construir su `.dat` desde las tablas disponibles, implementar el `.mod` y analizar sensibilidad de demanda, margen de reserva y costo de inversión.

[Ir a la actividad](actividades/actividad_06__expansion_de_generacion.md)

---

[Menú principal](../../README.md) · [Modelos](modelos/README.md) · [Actividades](actividades/README.md) · [Datos](datos/)
