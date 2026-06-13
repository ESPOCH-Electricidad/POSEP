# Modelo de transporte de energía

[Inicio](../../README.md) | [Bloque](../README.md) | [Modelos](README.md) | [Actividades](../actividades/README.md)

![Esquema del modelo](../assets/figuras/modelos/modelo_transporte_energia.svg)

## 1. Idea del modelo

El modelo de transporte asigna flujos desde fuentes hacia centros de demanda al menor costo. Es uno de los modelos más útiles para introducir balance, oferta, demanda y costos por arco antes de pasar a redes eléctricas con leyes físicas.

## 2. Lectura didáctica previa

| Elemento | Interpretación |
|---|---|
| Fuentes | Centrales o nodos con capacidad de suministro. |
| Destinos | Ciudades o nodos con demanda. |
| Variable | Flujo enviado de cada fuente a cada destino. |
| Analogía | Base conceptual para modelos de transporte en TNEP. |

## 3. Formulación matemática

### 3.1 Conjuntos

- `I`: fuentes de oferta.
- `J`: centros de demanda.

### 3.2 Índices

- `i ∈ I`: fuente.
- `j ∈ J`: destino.

### 3.3 Parámetros

- `S_i`: oferta máxima.
- `D_j`: demanda.
- `c_{i,j}`: costo unitario de transporte.
- `α`: factor de reserva o disponibilidad.

### 3.4 Variables de decisión

- `f_{i,j} ≥ 0`: flujo enviado de fuente `i` a destino `j`.

### 3.5 Función objetivo

Minimizar el costo total de transporte:  

```text
min Z = sum_{i in I} sum_{j in J} c_{i,j} f_{i,j}
```

### 3.6 Restricciones

### R1. Oferta

El flujo total desde cada fuente no puede superar su oferta disponible.

```text
sum_{j in J} f_{i,j} <= α S_i
```
### R2. Demanda

Cada destino debe recibir su demanda.

```text
sum_{i in I} f_{i,j} >= D_j
```
### R3. No negatividad

No existen flujos negativos.

```text
f_{i,j} >= 0
```

## 4. Construcción del archivo `.dat`

El `.dat` debe declarar `I`, `J`, oferta, demanda y matriz de costos. Se recomienda revisar si la oferta total es suficiente.

## 5. Interpretación del archivo `.out`

El `.out` debe permitir identificar rutas usadas, rutas no usadas, costo total y destinos críticos.

## 6. Errores frecuentes

- Olvidar declarar combinaciones origen-destino.
- No verificar factibilidad oferta-demanda.
- Interpretar el modelo como red eléctrica física; aquí no hay ángulos ni reactancias.

## 7. Actividades relacionadas

- [Actividad 01](../actividades/actividad_01_fundamentos_optimizacion.md)
