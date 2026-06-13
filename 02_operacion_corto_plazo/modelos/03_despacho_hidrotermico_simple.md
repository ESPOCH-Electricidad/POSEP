# Despacho hidrotérmico simple

> [Menú principal](../../README.md) · [Volver a Operación](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)

## 1. Contexto del problema

El agua disponible debe coordinarse con generación térmica costosa.

## 2. Enunciado guía

Asignar generación hidro y térmica minimizando costo.

## 3. Figura conceptual del modelo

![Figura conceptual](../assets/figuras/05_balance_hidrotermico.svg)

## 4. Datos que debe reconocer el estudiante

| Elemento | Descripción |
|---|---|
| Conjuntos e índices | $G$: térmicas; $H$: hidro; $T$: periodos |
| Parámetros | demanda, costos, límites técnicos, disponibilidad |
| Variables | $P_{g,t}$, $H_{h,t}$ |

## 5. Formulación matemática

### Función objetivo

$$
\min Z=\sum_{t,g}c_gP_{g,t}+\sum_tVOLL\,ENS_t
$$

### Balance

$$
\sum_gP_{g,t}+\sum_hH_{h,t}+ENS_t=D_t
$$

Demanda cubierta con hidro, térmica y ENS.

### Energía hidro

$$
\sum_tH_{h,t}\leq E_h
$$

El recurso hidro es limitado.

## 6. Interpretación técnica

La solución no debe interpretarse solo como un valor objetivo. El estudiante debe explicar qué decisiones se activan, qué restricciones quedan vinculantes y qué implicación física o económica tiene el resultado.

## 7. Qué resultado debe graficarse

Área apilada hidro/térmica y uso de agua.

## 8. Errores frecuentes

- No revisar límites.
- No interpretar ENS.
- No graficar resultados horarios.

## 9. Actividad relacionada

[Ir a la actividad](../actividades/actividad_02_operacion_corto_plazo.md)

---

> [Menú principal](../../README.md) · [Volver a Operación](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)
