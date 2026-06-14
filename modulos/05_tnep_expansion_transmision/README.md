# 05 — Expansión de transmisión

[Menú principal](../../README.md) · [Actividades](actividades/README.md) · [Datos](datos/)

## Introducción conceptual

La expansión de transmisión decide qué líneas o refuerzos construir para transportar energía desde generación hacia demanda futura, minimizando inversión, operación y energía no servida.

## Fundamentos del tema

El módulo compara formulaciones de expansión: transporte, constructivo, DC, híbrido, lineal disyuntivo y multietapa. La demanda proyectada del módulo 04 alimenta estos modelos.

## Figuras técnicas principales

![Red existente y candidatos](figuras/01_red_existente_candidatos.svg)

Elementos de un problema TNEP

![Transporte vs DC](figuras/02_transporte_vs_dc.svg)

Diferencia entre modelos de red

![Big-M disyuntivo](figuras/03_big_m_disyuntivo.svg)

Activación de líneas candidatas

![Expansión multietapa](figuras/04_expansion_multietapa.svg)

Cuándo construir también importa

## Ecuaciones base

### Costo de inversión

$$
C^{inv}=\sum_{\ell}c_\ell n_\ell
$$

Costo de circuitos nuevos.

### Capacidad

$$
-\overline{F}_\ell(n_\ell^0+n_\ell)\leq F_\ell\leq \overline{F}_\ell(n_\ell^0+n_\ell)
$$

Límite con circuitos existentes y nuevos.

### Activación

$$
-My_\ell\leq F_\ell\leq My_\ell
$$

Flujo solo si la línea se construye.

### Multietapa

$$
N_{\ell,t}=N_{\ell,t-1}+n_{\ell,t}
$$

Acumulación temporal.

## Ejemplos o modelos del módulo

| Recurso | Qué aporta | Acceso |
|---|---|---|
| Modelo de transporte | formulación inicial | [Abrir](modelos/01_modelo_transporte_expansion_transmision.md) |
| Modelo constructivo | refuerzo iterativo | [Abrir](modelos/02_modelo_constructivo_refuerzo_red.md) |
| Modelo DC | flujos con ángulos | [Abrir](modelos/03_modelo_dc_expansion_transmision.md) |
| Modelo híbrido | fidelidad parcial | [Abrir](modelos/04_modelo_hibrido_expansion_transmision.md) |
| Modelo lineal disyuntivo | candidatos binarios | [Abrir](modelos/05_modelo_lineal_disyuntivo_expansion_transmision.md) |
| Modelo multietapa | planificación temporal | [Abrir](modelos/06_modelo_multietapa_expansion_transmision.md) |


## Capa de datos de la v14

Las páginas de ejemplos/modelos del módulo incluyen datos suficientes para construir archivos de datos de trabajo. En los modelos AMPL se incluye una plantilla `.dat` sugerida en el propio README del modelo; en el módulo de demanda se especifican plantillas CSV para Python y archivos de salida hacia TNEP/GEP.

## Actividad del módulo

Revise [actividades/README.md](actividades/README.md) y desarrolle la actividad principal: **Actividad 05 — Expansión de transmisión**.

---

[Menú principal](../../README.md) · [Actividades](actividades/README.md) · [Datos](datos/)
