# Modelo binario de localización y cobertura

> [Menú principal](../../README.md) · [Volver a Fundamentos](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)

## 1. Contexto del problema

El modelo introduce decisiones discretas: instalar o no instalar. Esta lógica prepara al estudiante para UC, TNEP y GEP.

## 2. Enunciado guía

Seleccionar sitios de instalación para cubrir todos los elementos requeridos al menor costo.

## 3. Figura conceptual del modelo

![Figura conceptual](../assets/figuras/modelos/modelo_localizacion_binaria.svg)

## 4. Datos que debe reconocer el estudiante

| Elemento | Descripción |
|---|---|
| Conjuntos | $A$: sitios, $M$: elementos. |
| Índices | $a\in A$, $m\in M$. |
| Parámetros | $C_a$, $q_{m,a}$. |
| Variables | $y_a$, $z_{m,a}$ binarias. |

## 5. Formulación matemática

### Función objetivo

$$
\min Z=\sum_{a\in A}C_ay_a
$$

### Cobertura

$$
\sum_{a\in A}z_{m,a}\geq 1\quad \forall m
$$

Cada elemento queda cubierto.

### Activación

$$
z_{m,a}\leq y_a\quad \forall m,a
$$

Solo se cubre desde sitios instalados.

### Elegibilidad

$$
z_{m,a}\leq q_{m,a}\quad \forall m,a
$$

Solo se permite cobertura técnicamente válida.

## 6. Interpretación técnica

La solución no debe interpretarse solo como un valor objetivo. El estudiante debe explicar qué decisiones se activan, qué restricciones quedan vinculantes y qué implicación física o económica tiene el resultado.

## 7. Qué resultado debe graficarse

Mapa de sitios instalados, elementos cubiertos y costo total.

## 8. Errores frecuentes

- Confundir cobertura posible con decisión.
- No imponer dominio binario.
- No justificar redundancia.

## 9. Actividad relacionada

[Ir a la actividad](../actividades/actividad_01C_localizacion_binaria.md)

---

> [Menú principal](../../README.md) · [Volver a Fundamentos](../README.md) · [Modelos del bloque](README.md) · [Actividades](../actividades/README.md) · [Casos](../../06_casos_de_estudio/README.md)
