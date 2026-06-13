# Operación de cascada hidroeléctrica

> [Menú principal](../../README.md) · [Volver a Operación](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)

## 1. Contexto del problema

Varios embalses conectados obligan a rastrear volumen y caudales.

## 2. Enunciado guía

Modelar volumen, turbinamiento y vertimiento en una cascada.

## 3. Figura conceptual del modelo

![Figura conceptual](../assets/figuras/05_balance_hidrotermico.svg)

## 4. Datos que debe reconocer el estudiante

| Elemento | Descripción |
|---|---|
| Conjuntos e índices | $R$: embalses; $T$: periodos |
| Parámetros | demanda, costos, límites técnicos, disponibilidad |
| Variables | $V_{r,t}$, $Q_{r,t}$, $S_{r,t}$ |

## 5. Formulación matemática

### Función objetivo

$$
\min Z=C^{op}
$$

### Balance hídrico

$$
V_{r,t}=V_{r,t-1}+A_{r,t}+Q^{up}_{r,t}-Q_{r,t}-S_{r,t}
$$

Conservación de agua.

### Generación

$$
H_{r,t}=\rho_rQ_{r,t}
$$

Producción proporcional al caudal.

## 6. Interpretación técnica

La solución no debe interpretarse solo como un valor objetivo. El estudiante debe explicar qué decisiones se activan, qué restricciones quedan vinculantes y qué implicación física o económica tiene el resultado.

## 7. Qué resultado debe graficarse

Volumen por embalse y generación hidro.

## 8. Errores frecuentes

- No revisar límites.
- No interpretar ENS.
- No graficar resultados horarios.

## 9. Actividad relacionada

[Ir a la actividad](../actividades/actividad_02_operacion_corto_plazo.md)

---

> [Menú principal](../../README.md) · [Volver a Operación](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)
