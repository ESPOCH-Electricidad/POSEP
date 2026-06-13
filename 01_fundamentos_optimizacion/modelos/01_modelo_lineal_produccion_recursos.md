# Modelo lineal de producción con recursos limitados

[Inicio](../../README.md) | [Bloque](../README.md) | [Modelos](README.md) | [Actividades](../actividades/README.md)

![Esquema del modelo](../assets/figuras/modelos/modelo_produccion_lineal.svg)

## 1. Idea del modelo

Este modelo representa una situación elemental de asignación de recursos: se dispone de una capacidad limitada y se debe decidir cuánto producir de cada alternativa. Aunque el ejemplo puede ser de producción industrial, su estructura es la misma que aparece en despacho económico, selección de tecnologías y asignación de energía.

## 2. Lectura didáctica previa

| Elemento | Interpretación |
|---|---|
| Tipo de problema | Programación lineal si las variables son continuas; MILP si se exige producción entera. |
| Decisión | Cantidad a producir o suministrar. |
| Restricción central | Uso de capacidad o recurso disponible. |
| Resultado esperado | Producción óptima y recurso limitante. |

## 3. Formulación matemática

### 3.1 Conjuntos

- `P`: conjunto de productos o alternativas.

### 3.2 Índices

- `p ∈ P`: producto o alternativa de producción.

### 3.3 Parámetros

- `c_p`: beneficio o costo unitario.
- `a_p`: consumo de recurso por unidad.
- `R`: recurso disponible.
- `u_p`: producción máxima permitida.

### 3.4 Variables de decisión

- `x_p ≥ 0`: cantidad producida del producto `p`.

### 3.5 Función objetivo

Maximizar beneficio o minimizar costo total. En forma de maximización:  

```text
max Z = sum_{p in P} c_p x_p
```

### 3.6 Restricciones

### R1. Disponibilidad de recurso

El uso total del recurso no puede superar la capacidad disponible.

```text
sum_{p in P} a_p x_p <= R
```
### R2. Límite de producción

Cada alternativa puede tener una producción máxima.

```text
0 <= x_p <= u_p
```
### R3. Dominio

Las variables son continuas salvo que el problema exija unidades enteras.

```text
x_p >= 0
```

## 4. Construcción del archivo `.dat`

El archivo `.dat` debe declarar el conjunto `P` y los parámetros `c`, `a`, `u` y `R`. Se recomienda usar nombres de parámetros con unidades explícitas.

## 5. Interpretación del archivo `.out`

El archivo `.out` debe permitir identificar valor objetivo, producción por alternativa y restricción activa. Si una restricción está activa, su holgura debe ser cero o muy cercana a cero.

## 6. Errores frecuentes

- Confundir maximización con minimización.
- No verificar unidades del recurso.
- Escribir restricciones explícitas que no escalan.
- No analizar holguras.

## 7. Actividades relacionadas

- [Actividad 01](../actividades/actividad_01_fundamentos_optimizacion.md)
