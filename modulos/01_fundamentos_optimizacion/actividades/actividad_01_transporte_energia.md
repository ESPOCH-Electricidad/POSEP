# Actividad 01B — Transporte de energía

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Datos](../datos/) · [Guía AMPL](../../../docs/guia_ampl.md)

## Competencia

Construir un modelo de transporte de mínimo costo utilizando balances de oferta y demanda, parámetros bidimensionales y variables indexadas por pares origen-destino.

## Enunciado

Tres fuentes de energía pueden abastecer tres centros de carga. Cada fuente tiene una oferta máxima y cada carga tiene una demanda que debe ser atendida. El costo de transporte depende del par fuente-carga. Se debe determinar la asignación de energía de mínimo costo.

## Datos del caso

Use `transporte_fuentes.csv`, `transporte_cargas.csv` y `transporte_costos.csv`.

| Fuente | Oferta [MWh] |
|---|---:|
| F1 | 120 |
| F2 | 100 |
| F3 | 90 |

| Carga | Demanda [MWh] |
|---|---:|
| C1 | 80 |
| C2 | 110 |
| C3 | 90 |

| Fuente | C1 | C2 | C3 |
|---|---:|---:|---:|
| F1 | 5 | 7 | 9 |
| F2 | 6 | 4 | 8 |
| F3 | 9 | 6 | 3 |

## Formulación requerida

Conjuntos: $f\in F$ fuentes, $c\in C$ cargas. Variable $x_{f,c}$: energía enviada desde $f$ hacia $c$.

$$
\min Z=\sum_{f\in F}\sum_{c\in C} cost_{f,c}x_{f,c}
$$

Oferta:

$$
\sum_{c\in C}x_{f,c}\leq supply_f \qquad \forall f\in F
$$

Demanda:

$$
\sum_{f\in F}x_{f,c}=demand_c \qquad \forall c\in C
$$

No negatividad:

$$
x_{f,c}\geq0
$$

## Tareas

1. Escriba los datos como conjuntos `F`, `C`, parámetros `supply`, `demand` y `cost`.
2. Implemente el modelo en AMPL usando una variable bidimensional.
3. Genere una tabla de envíos $x_{f,c}$.
4. Calcule el costo total y el uso de cada fuente.
5. Aumente la demanda de C2 en 20 MWh y analice qué fuente absorbe el incremento.
6. Reduzca la oferta de F2 a 80 MWh y explique cómo cambia la asignación.

## Validación

La suma enviada a cada carga debe coincidir exactamente con su demanda. La suma enviada desde cada fuente no puede superar su oferta. Revise si queda capacidad sin usar y si eso tiene sentido con la oferta total disponible.

## Entregables

- Formulación y archivos AMPL.
- Tabla fuente-carga de envíos.
- Costos totales de caso base y dos variaciones.
- Interpretación de la ruta de menor costo y de las restricciones activas.
