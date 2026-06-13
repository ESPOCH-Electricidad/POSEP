# Modelo GEP con bloques de carga

> [Menú principal](../../README.md) · [Volver a GEP](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)

## 1. Contexto del problema

Relaciona inversión con operación aproximada por bloques.

## 2. Enunciado guía

Decidir inversión y generación por bloque.

## 3. Figura conceptual del modelo

![Figura conceptual](../assets/figuras/02_curva_duracion_carga.svg)

## 4. Datos que debe reconocer el estudiante

| Elemento | Descripción |
|---|---|
| Conjuntos | $Y$: años, $B$: bloques, $K$: tecnologías. |
| Parámetros | demanda, duración, CAPEX, FOM, costo variable, AF, FC. |
| Variables | $Build_{k,y}$, $Cap_{k,y}$, $Gen_{k,y,b}$, $ENS_{y,b}$. |

## 5. Formulación matemática

### Función objetivo

$$
\min Z=C^{inv}+C^{fix}+C^{op}+C^{ENS}
$$

### Balance

$$
\sum_kGen_{k,y,b}+\sum_eGen_{e,y,b}+ENS_{y,b}=D_{y,b}
$$

Demanda por bloque.

### Capacidad

$$
Cap_{k,y}=Cap_{k,y-1}+Build_{k,y}
$$

Capacidad acumulada.

### Reserva

$$
\sum_kFC_kCap_{k,y}\geq(1+RM)D_y^{peak}
$$

Margen firme.

## 6. Interpretación técnica

La solución no debe interpretarse solo como un valor objetivo. El estudiante debe explicar qué decisiones se activan, qué restricciones quedan vinculantes y qué implicación física o económica tiene el resultado.

## 7. Qué resultado debe graficarse

Capacidad nueva, capacidad acumulada, generación por bloque y ENS.

## 8. Errores frecuentes

- Confundir MW y MWh.
- No usar duración de bloque.
- No separar nueva capacidad y acumulada.

## 9. Actividad relacionada

[Ir a la actividad](../actividades/actividad_05_gep_multianual.md)

---

> [Menú principal](../../README.md) · [Volver a GEP](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)
