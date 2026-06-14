# 02 — Operación de corto plazo

[Menú principal](../../README.md) · [Actividades](actividades/README.md) · [Datos](datos/)

## Introducción conceptual

La operación de corto plazo decide cómo cubrir la demanda usando generación disponible, reserva, compromisos de unidades y recursos hidráulicos. En esta etapa la demanda se trata como parámetro conocido del problema.

## Fundamentos del tema

El módulo avanza desde despacho económico hasta compromiso de unidades y despacho hidrotérmico. La teoría debe permitir interpretar costo marginal, orden de mérito, pérdidas, rampas, mínimos técnicos, arranques y balance de embalse.

## Figuras técnicas principales

![Curva de demanda y reserva](figuras/01_curva_demanda_reserva.svg)

Demanda horaria, capacidad disponible y reserva

![Orden de mérito y costo marginal](figuras/02_orden_merito_costo_marginal.svg)

Despacho por costo variable creciente

![Compromiso de unidades](figuras/03_unit_commitment_timeline.svg)

Decisiones binarias en el tiempo

![Balance de embalse](figuras/04_balance_embalse.svg)

El agua como recurso intertemporal

## Ecuaciones base

### Despacho económico

$$
\min \sum_{g,t}c_gP_{g,t}
$$

Minimiza costo operativo.

### Balance

$$
\sum_gP_{g,t}+ENS_t=D_t
$$

Demanda atendida en cada periodo.

### Unit commitment

$$
\underline{P}_gu_{g,t}\leq P_{g,t}\leq \overline{P}_gu_{g,t}
$$

Vincula generación y estado.

### Embalse

$$
V_{h,t}=V_{h,t-1}+A_{h,t}-Q_{h,t}-S_{h,t}
$$

Balance hídrico intertemporal.

## Ejemplos o modelos del módulo

| Recurso | Qué aporta | Acceso |
|---|---|---|
| Despacho económico uninodal | costo marginal y orden de mérito | [Abrir](modelos/01_despacho_economico_uninodal.md) |
| Despacho económico por tramos | costos lineales por segmentos | [Abrir](modelos/02_despacho_economico_por_tramos.md) |
| Despacho con pérdidas | puente entre ED y OPF | [Abrir](modelos/03_despacho_con_perdidas.md) |
| Compromiso de unidades | MILP operativo | [Abrir](modelos/04_compromiso_unidades_termicas.md) |
| Despacho hidrotérmico simple | agua y térmica | [Abrir](modelos/05_despacho_hidrotermico_simple.md) |
| Operación de cascada hidroeléctrica | embalses conectados | [Abrir](modelos/06_operacion_cascada_hidroelectrica.md) |


## Capa de datos de la v14

Las páginas de ejemplos/modelos del módulo incluyen datos suficientes para construir archivos de datos de trabajo. En los modelos AMPL se incluye una plantilla `.dat` sugerida en el propio README del modelo; en el módulo de demanda se especifican plantillas CSV para Python y archivos de salida hacia TNEP/GEP.

## Implementación en AMPL

Los modelos de despacho económico, despacho por tramos, compromiso de unidades y operación hidrotérmica deben implementarse a partir de las ecuaciones de cada página de modelo. Consulte la [Guía AMPL](../../docs/guia_ampl.md) para ciclos `for`, sensibilidad con `repeat while`, construcción de `.dat` desde tablas y exportación de resultados.

## Actividad del módulo

Revise [actividades/README.md](actividades/README.md) y desarrolle la actividad principal: **Actividad 02 — Operación de corto plazo**.

---

[Menú principal](../../README.md) · [Actividades](actividades/README.md) · [Datos](datos/)
