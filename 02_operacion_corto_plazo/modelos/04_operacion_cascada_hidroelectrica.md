# Operación de cascada hidroeléctrica

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)



![Esquema del modelo](../assets/figuras/modelos/hidrotermico.svg)

## 1. Intuición del modelo

Representa embalses conectados. El agua turbinada o vertida en una central puede influir en centrales aguas abajo.

## 2. Elementos de la formulación

| Elemento | Descripción |
|---|---|
| Conjuntos | $R$: embalses; $T$: periodos. |
| Parámetros | $A_{r,t}$: aportes; $\underline{V}_r$, $\overline{V}_r$; $\rho_r$. |
| Variables | $V_{r,t}$, $Q_{r,t}$, $S_{r,t}$, $H_{r,t}$. |

## 3. Formulación matemática

### Balance hídrico

Conservación de volumen en cada embalse.

$$
V_{r,t}=V_{r,t-1}+A_{r,t}+Q^{up}_{r,t}-Q_{r,t}-S_{r,t}
$$

### Producción hidro

Generación proporcional al caudal turbinado.

$$
H_{r,t}=\rho_r Q_{r,t}
$$

### Límites de volumen

El embalse opera dentro de límites.

$$
\underline{V}_r\leq V_{r,t}\leq \overline{V}_r
$$

## 4. Interpretación técnica

El análisis debe interpretar el valor temporal del agua y el efecto de restricciones de volumen.

## 5. Actividad relacionada

- [Ir a la actividad](../actividades/actividad_02_operacion_corto_plazo.md)
---

> [Menú principal](../../README.md) · [Índice del sitio](../../docs/index.md) · [Ruta de aprendizaje](../../docs/learning_path.md) · [Modelos](../../docs/modelos.md) · [Casos](../../docs/casos_de_estudio.md) · [Evaluación](../../docs/evaluacion.md)
