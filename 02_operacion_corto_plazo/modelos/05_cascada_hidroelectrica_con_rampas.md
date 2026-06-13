# Cascada hidroeléctrica con restricciones de rampa

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)



![Esquema del modelo](../assets/figuras/modelos/hidrotermico.svg)

## 1. Intuición del modelo

Agrega límites de variación temporal para representar cambios máximos de turbinamiento o generación entre periodos.

## 2. Elementos de la formulación

| Elemento | Descripción |
|---|---|
| Conjuntos | $R$: embalses; $T$: periodos. |
| Parámetros | $RU_r$, $RD_r$, límites hidráulicos. |
| Variables | $Q_{r,t}$, $V_{r,t}$, $H_{r,t}$. |

## 3. Formulación matemática

### Rampa subida

El caudal no puede aumentar bruscamente.

$$
Q_{r,t}-Q_{r,t-1}\leq RU_r
$$

### Rampa bajada

El caudal no puede disminuir bruscamente.

$$
Q_{r,t-1}-Q_{r,t}\leq RD_r
$$

### Balance hídrico

Se mantiene conservación de agua.

$$
V_{r,t}=V_{r,t-1}+A_{r,t}-Q_{r,t}-S_{r,t}
$$

## 4. Interpretación técnica

La solución suaviza la operación y puede aumentar costo térmico si restringe el uso hidro en horas críticas.

## 5. Actividad relacionada

- [Ir a la actividad](../actividades/actividad_02_operacion_corto_plazo.md)
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)
