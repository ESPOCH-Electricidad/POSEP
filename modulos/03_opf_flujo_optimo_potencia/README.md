# 03 — Flujo óptimo de potencia

[Menú principal](../../README.md) · [Actividades](actividades/README.md) · [Datos](datos/)

## Introducción conceptual

El OPF incorpora la red al despacho económico. La solución depende de la ubicación de generación y demanda, límites de líneas, ángulos, tensiones, reactivos y pérdidas.

## Fundamentos del tema

El módulo explica balance nodal, flujo DC, ecuaciones AC, congestión y precios nodales. OPF-DC se utiliza para entender flujos y congestión; OPF-AC para analizar factibilidad eléctrica.

## Figuras técnicas principales

![Red de barras y líneas](figuras/01_red_barras_lineas.svg)

Elementos principales de un sistema de potencia

![Balance nodal](figuras/02_balance_nodal.svg)

Cada barra conserva potencia

![Flujo DC](figuras/03_flujo_dc_angulos.svg)

Flujo activo proporcional a diferencia angular

![OPF-DC vs OPF-AC](figuras/04_comparacion_dc_ac.svg)

Diferencias de alcance y complejidad

## Ecuaciones base

### Balance nodal DC

$$
\sum_{g\in G_n}P_g-P_n^D+ENS_n=\sum_\ell A_{n,\ell}F_\ell
$$

Balance por barra.

### Flujo DC

$$
F_\ell=\frac{\theta_i-\theta_j}{x_\ell}
$$

Flujo linealizado.

### Potencia activa AC

$$
P_i=V_i\sum_jV_j(G_{ij}\cos\theta_{ij}+B_{ij}\sin\theta_{ij})
$$

Balance activo no lineal.

### Potencia reactiva AC

$$
Q_i=V_i\sum_jV_j(G_{ij}\sin\theta_{ij}-B_{ij}\cos\theta_{ij})
$$

Balance reactivo no lineal.

## Ejemplos o modelos del módulo

| Recurso | Qué aporta | Acceso |
|---|---|---|
| OPF-DC | balance nodal, ángulos y congestión | [Abrir](modelos/01_flujo_optimo_potencia_dc.md) |
| OPF-AC | tensión, reactivos y pérdidas | [Abrir](modelos/02_flujo_optimo_potencia_ac.md) |


## Capa de datos de la v14

Las páginas de ejemplos/modelos del módulo incluyen datos suficientes para construir archivos de datos de trabajo. En los modelos AMPL se incluye una plantilla `.dat` sugerida en el propio README del modelo; en el módulo de demanda se especifican plantillas CSV para Python y archivos de salida hacia TNEP/GEP.

## Implementación en AMPL

El OPF DC debe implementarse cuidando índices de barras, líneas y generadores. La [Guía AMPL](../../docs/guia_ampl.md) muestra cómo declarar conjuntos de pares, balances nodales y reportes por línea.

## Actividad del módulo

Revise [actividades/README.md](actividades/README.md) y desarrolle la actividad principal: **Actividad 03 — Flujo óptimo de potencia**.

---

[Menú principal](../../README.md) · [Actividades](actividades/README.md) · [Datos](datos/)
