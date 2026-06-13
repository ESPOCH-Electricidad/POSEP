# Cascada hidroeléctrica con restricciones de rampa

> [Menú principal](../../README.md) · [Volver a Operación](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)

## 1. Contexto del problema

Los caudales o generación no pueden cambiar abruptamente entre periodos.

## 2. Enunciado guía

Incorporar rampas a la operación de cascada.

## 3. Figura conceptual del modelo

![Figura conceptual](../assets/figuras/05_balance_hidrotermico.svg)

## 4. Datos que debe reconocer el estudiante

| Elemento | Descripción |
|---|---|
| Conjuntos e índices | $R$: embalses; $T$: periodos |
| Parámetros | demanda, costos, límites técnicos, disponibilidad |
| Variables | $Q_{r,t}$, $V_{r,t}$ |

## 5. Formulación matemática

### Función objetivo

$$
\min Z=C^{op}
$$

### Rampa subida

$$
Q_{r,t}-Q_{r,t-1}\leq RU_r
$$

Cambio máximo hacia arriba.

### Rampa bajada

$$
Q_{r,t-1}-Q_{r,t}\leq RD_r
$$

Cambio máximo hacia abajo.

## 6. Interpretación técnica

La solución no debe interpretarse solo como un valor objetivo. El estudiante debe explicar qué decisiones se activan, qué restricciones quedan vinculantes y qué implicación física o económica tiene el resultado.

## 7. Qué resultado debe graficarse

Series temporales de caudal y rampas activas.

## 8. Errores frecuentes

- No revisar límites.
- No interpretar ENS.
- No graficar resultados horarios.

## 9. Actividad relacionada

[Ir a la actividad](../actividades/actividad_02_operacion_corto_plazo.md)

---

> [Menú principal](../../README.md) · [Volver a Operación](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)
