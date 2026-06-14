# Ejemplo 01 — Fábrica de pintura

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

Una planta produce dos tipos de pintura con un tiempo semanal limitado. El caso introduce programación lineal, región factible, restricciones activas y análisis de sensibilidad.

## 2. Enunciado

Paint Deals produce pintura azul y negra. La pintura azul se vende a 10 USD/L y la negra a 15 USD/L. La planta puede producir un color a la vez: azul a 40 L/h y negra a 30 L/h. El mercado limita la venta semanal a 1000 L de azul y 860 L de negra. La planta opera 40 h por semana. Se debe decidir cuántos litros producir de cada pintura para maximizar ingresos.



## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| P | productos de pintura |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| price[p] | USD/L | ingreso unitario por litro vendido |
| rate[p] | L/h | tasa de producción |
| market[p] | L | máximo de venta semanal |
| Hours | h | horas disponibles por semana |

## 5. Datos completos para construir el archivo de datos

### Productos

| producto | price_usd_l | rate_l_h | market_l |
| --- | --- | --- | --- |
| azul | 10 | 40 | 1000 |
| negra | 15 | 30 | 860 |

### Parámetro escalar

| parametro | valor | unidad |
| --- | --- | --- |
| Hours | 40 | h/semana |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| x[p] | L, continua no negativa | litros producidos del producto p |

## 7. Función objetivo

$$
\max Z=\sum_{p\in P} price_p x_p
$$

**Explicación de la función objetivo.** Maximiza el ingreso semanal total. Cada litro producido y vendido aporta un ingreso unitario distinto según el color.

## 8. Restricciones del modelo

### Tiempo disponible

$$
\sum_{p\in P}\frac{x_p}{rate_p}\leq Hours
$$

**Explicación.** Convierte litros producidos en horas de producción. La suma de horas usadas no puede superar las 40 horas semanales.

### Límite de mercado

$$
x_p\leq market_p\quad \forall p\in P
$$

**Explicación.** La producción no debe superar la cantidad máxima que puede venderse de cada color.

### No negatividad

$$
x_p\geq 0\quad \forall p\in P
$$

**Explicación.** No se permiten cantidades negativas de producción.

## 9. Plantilla `.dat` sugerida

```ampl
set P := azul negra;

param price :=
azul  10
negra 15
;

param rate :=
azul  40
negra 30
;

param market :=
azul  1000
negra 860
;

param Hours := 40;
```

## 10. Resultados esperados

El estudiante debe reportar producción por color, ingreso total, horas utilizadas y restricciones activas.

## 11. Actividad asociada

[Actividad 01A](../actividades/actividad_01_programacion_lineal.md)


## 12. Validación mínima

- Verifique que todas las unidades sean consistentes.
- Compruebe que todos los conjuntos usados en la formulación tengan datos.
- Revise que el balance principal cierre.
- Identifique restricciones activas.
- Compare el resultado contra una estimación manual simple.

## 13. Preguntas de análisis

1. ¿Qué restricción limita principalmente la solución?
2. ¿Qué parámetro tendría mayor impacto si cambia?
3. ¿El resultado es técnicamente razonable?
4. ¿Qué dato adicional se necesitaría para aplicar el modelo a un sistema real?

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
