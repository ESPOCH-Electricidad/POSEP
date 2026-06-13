# Compromiso de unidades térmicas

> [Menú principal](../../README.md) · [Volver a Operación](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)

## 1. Contexto del problema

El operador decide encender unidades y generar respetando arranques, mínimos y rampas.

## 2. Enunciado guía

Formular un MILP de encendido y despacho.

## 3. Figura conceptual del modelo

![Figura conceptual](../assets/figuras/04_unit_commitment_timeline.svg)

## 4. Datos que debe reconocer el estudiante

| Elemento | Descripción |
|---|---|
| Conjuntos e índices | $G$: unidades; $T$: horas |
| Parámetros | demanda, costos, límites técnicos, disponibilidad |
| Variables | $P_{g,t}$, $u_{g,t}$, $v_{g,t}$ |

## 5. Formulación matemática

### Función objetivo

$$
\min Z=\sum_{g,t}c_gP_{g,t}+\sum_{g,t}SU_gv_{g,t}
$$

### Estado

$$
\underline{P}_gu_{g,t}\leq P_{g,t}\leq \overline{P}_gu_{g,t}
$$

Generación ligada al encendido.

### Arranque

$$
v_{g,t}\geq u_{g,t}-u_{g,t-1}
$$

Detecta encendido.

## 6. Interpretación técnica

La solución no debe interpretarse solo como un valor objetivo. El estudiante debe explicar qué decisiones se activan, qué restricciones quedan vinculantes y qué implicación física o económica tiene el resultado.

## 7. Qué resultado debe graficarse

Cronograma de encendido y generación por unidad.

## 8. Errores frecuentes

- No revisar límites.
- No interpretar ENS.
- No graficar resultados horarios.

## 9. Actividad relacionada

[Ir a la actividad](../actividades/actividad_02_operacion_corto_plazo.md)

---

> [Menú principal](../../README.md) · [Volver a Operación](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)
