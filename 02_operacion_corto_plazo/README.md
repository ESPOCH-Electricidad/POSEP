# 02 — Operación de corto plazo

> [Menú principal](../README.md) · [Índice del sitio](../docs/index.md) · [Ruta de aprendizaje](../docs/learning_path.md) · [Modelos](../docs/modelos.md) · [Casos](../docs/casos_de_estudio.md) · [Evaluación](../docs/evaluacion.md)



![Mapa visual del bloque](../docs/assets/img/bloques/02_operacion.svg)

## 1. Propósito del bloque

La operación de corto plazo estudia cómo abastecer la demanda en horizontes de horas o días. Las decisiones son principalmente operativas: cuánto genera cada unidad, qué unidades se encienden, cómo se cumple la reserva y cómo se utiliza la energía hidroeléctrica disponible.

![Operación de corto plazo](assets/figuras/teoria/operacion_corto_plazo.svg)

## 2. Problemas típicos

| Problema | Decisión principal | Tipo de modelo |
|---|---|---|
| Despacho económico | generación por unidad | LP o QP |
| Despacho por tramos | generación por segmento | LP |
| Compromiso de unidades | encendido, arranque y generación | MILP |
| Despacho hidrotérmico | uso de agua y generación térmica | LP/MILP |
| Cascadas hidroeléctricas | volumen, turbinamiento y vertimiento | LP/NLP según detalle |

## 3. Ecuación base de balance

Para cada periodo $t$, la generación total debe cubrir la demanda y la energía no servida:

$$
\sum_{g \in G} P_{g,t} + ENS_t = D_t
$$

La diferencia entre modelos está en las restricciones adicionales: límites de generación, rampas, mínimos técnicos, estados binarios, reserva y balance hídrico.

## 4. Ruta de aprendizaje

| Modelo | Acceso |
|---|---|
| Despacho económico uninodal | [Abrir](modelos/01_despacho_economico_uninodal.md) |
| Despacho económico por tramos | [Abrir](modelos/02_despacho_economico_por_tramos.md) |
| Despacho hidrotérmico simple | [Abrir](modelos/03_despacho_hidrotermico_simple.md) |
| Cascada hidroeléctrica | [Abrir](modelos/04_operacion_cascada_hidroelectrica.md) |
| Cascada con rampas | [Abrir](modelos/05_cascada_hidroelectrica_con_rampas.md) |
| Compromiso de unidades | [Abrir](modelos/06_compromiso_unidades_termicas.md) |

## 5. Carpetas del bloque

| Carpeta | Uso |
|---|---|
| [modelos](modelos/README.md) | Formulaciones matemáticas |
| [notebooks](notebooks/) | Exploración de datos y gráficos |
| [actividades](actividades/README.md) | Evaluación aplicada |
| [ED_despacho_economico](ED_despacho_economico/README.md) | Material de ED |
| [UC_unit_commitment](UC_unit_commitment/README.md) | Material de UC |
| [despacho_hidrotermico](despacho_hidrotermico/README.md) | Material hidrotermico |
---

> [Menú principal](../README.md) · [Índice del sitio](../docs/index.md) · [Ruta de aprendizaje](../docs/learning_path.md) · [Modelos](../docs/modelos.md) · [Casos](../docs/casos_de_estudio.md) · [Evaluación](../docs/evaluacion.md)
