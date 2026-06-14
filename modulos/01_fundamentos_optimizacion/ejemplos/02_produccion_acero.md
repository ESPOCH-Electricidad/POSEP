# Ejemplo 02 — Producción de acero

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

## 1. Contexto del problema

Una empresa decide producción semanal de láminas y bobinas usando tiempo limitado de planta. El ejemplo refuerza formulación lineal, unidades y límites de producción.

## 2. Enunciado

Una empresa de acero produce láminas y bobinas. Cada producto tiene utilidad por tonelada, tasa de producción y venta máxima semanal. Con 40 horas disponibles, se debe decidir la producción semanal que maximiza el beneficio.



## 3. Conjuntos requeridos

| Conjunto | Descripción |
| --- | --- |
| P | productos de acero |

## 4. Parámetros requeridos

| Parámetro | Unidad | Descripción |
| --- | --- | --- |
| profit[p] | USD/t | utilidad unitaria por tonelada |
| rate[p] | t/h | tasa de producción |
| maxProd[p] | t | producción máxima semanal |
| Hours | h | horas disponibles |

## 5. Datos completos para construir el archivo de datos

### Productos

| producto | profit_usd_t | rate_t_h | max_prod_t |
| --- | --- | --- | --- |
| laminas | 25 | 20 | 500 |
| bobinas | 30 | 15 | 450 |

### Parámetro escalar

| parametro | valor | unidad |
| --- | --- | --- |
| Hours | 40 | h/semana |

## 6. Variables de decisión

| Variable | Unidad/dominio | Descripción |
| --- | --- | --- |
| x[p] | t, continua no negativa | toneladas producidas del producto p |

## 7. Función objetivo

$$
\max Z=\sum_{p\in P} profit_p x_p
$$

**Explicación de la función objetivo.** Maximiza el beneficio semanal considerando que cada producto aporta una utilidad por tonelada.

## 8. Restricciones del modelo

### Tiempo de planta

$$
\sum_{p\in P}\frac{x_p}{rate_p}\leq Hours
$$

**Explicación.** Cada tonelada consume tiempo de producción según la tasa del producto.

### Máximo semanal

$$
x_p\leq maxProd_p\quad \forall p\in P
$$

**Explicación.** Limita la producción a la capacidad comercial o técnica semanal.

### No negatividad

$$
x_p\geq 0\quad \forall p\in P
$$

**Explicación.** La producción no puede ser negativa.

## 9. Plantilla `.dat` sugerida

```ampl
set P := laminas bobinas;

param profit :=
laminas 25
bobinas 30
;

param rate :=
laminas 20
bobinas 15
;

param maxProd :=
laminas 500
bobinas 450
;

param Hours := 40;
```

## 10. Resultados esperados

El estudiante debe reportar producción por producto, beneficio total, horas utilizadas y restricciones vinculantes.

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
