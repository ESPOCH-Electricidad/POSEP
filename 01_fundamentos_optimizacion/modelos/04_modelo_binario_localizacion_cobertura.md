# Modelo binario de localización y cobertura

[Inicio](../../README.md) | [Bloque](../README.md) | [Modelos](README.md) | [Actividades](../actividades/README.md)

![Esquema del modelo](../assets/figuras/modelos/modelo_localizacion_binaria.svg)

## 1. Idea del modelo

Este modelo introduce decisiones discretas: instalar o no instalar un recurso. La lógica es análoga a construir una línea, instalar una central o seleccionar una tecnología candidata.

## 2. Lectura didáctica previa

| Elemento | Interpretación |
|---|---|
| Tipo | Programación lineal entera mixta. |
| Decisión | Instalar activos candidatos. |
| Cobertura | Cada demanda debe ser atendida por al menos un activo. |
| Analogía eléctrica | Inversión en transmisión o generación. |

## 3. Formulación matemática

### 3.1 Conjuntos

- `A`: sitios candidatos.
- `M`: elementos a cubrir.

### 3.2 Índices

- `a ∈ A`: sitio candidato.
- `m ∈ M`: elemento de demanda.

### 3.3 Parámetros

- `C_a`: costo de instalar en `a`.
- `d_{m,a}`: distancia o elegibilidad.
- `Dmax`: distancia máxima.
- `cover_{m,a}`: parámetro binario de cobertura.

### 3.4 Variables de decisión

- `y_a ∈ {0,1}`: 1 si se instala en sitio `a`.
- `z_{m,a} ∈ {0,1}`: 1 si `m` es cubierto por `a`.

### 3.5 Función objetivo

Minimizar costo de instalación:  

```text
min Z = sum_{a in A} C_a y_a
```

### 3.6 Restricciones

### R1. Cobertura mínima

Cada elemento debe ser cubierto por al menos un sitio instalado.

```text
sum_{a in A} z_{m,a} >= 1
```
### R2. Activación

No se puede asignar cobertura a un sitio no instalado.

```text
z_{m,a} <= y_a
```
### R3. Elegibilidad

Solo se permite cobertura si el sitio es técnicamente válido.

```text
z_{m,a} <= cover_{m,a}
```

## 4. Construcción del archivo `.dat`

El `.dat` debe contener costos y matriz de cobertura. La matriz puede derivarse de distancias y distancia máxima.

## 5. Interpretación del archivo `.out`

El `.out` debe reportar sitios instalados, elementos cubiertos y costo total.

## 6. Errores frecuentes

- Confundir parámetro binario de cobertura con variable de decisión.
- No limitar asignaciones a sitios instalados.
- No justificar distancia máxima o criterio técnico.

## 7. Actividades relacionadas

- [Actividad 01](../actividades/actividad_01_fundamentos_optimizacion.md)
