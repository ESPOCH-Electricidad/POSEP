# Despacho económico con costos por tramos

[Inicio](../../README.md) | [Bloque](../README.md) | [Modelos](README.md) | [Actividades](../actividades/README.md)

![Esquema del modelo](../assets/figuras/modelos/despacho_economico.svg)

## 1. Idea del modelo

Este modelo aproxima curvas de costo no lineales mediante segmentos lineales. Permite representar que los primeros MW de una unidad pueden ser más baratos que los últimos.

## 2. Lectura didáctica previa

| Elemento | Interpretación |
|---|---|
| Horizonte | Corto plazo: horas o días. |
| Decisión | Generación, estado o uso de recursos por periodo. |
| Salida clave | Costo operativo, despacho, ENS y restricciones activas. |

## 3. Formulación matemática

### 3.1 Conjuntos

- `G`: generadores.
- `K`: tramos de costo.
- `T`: periodos.

### 3.2 Índices

- `g`: generador
- `t`: periodo horario
- `h`: unidad hidroeléctrica si aplica

### 3.3 Parámetros

- `c_{g,k}`: costo del tramo.
- `PmaxSeg_{g,k}`: capacidad del tramo.
- `D_t`: demanda.

### 3.4 Variables de decisión

- `PgSeg_{g,k,t}`: generación del tramo.
- `Pg_{g,t}`: generación total.

### 3.5 Función objetivo

Minimizar el costo total por segmentos.

### 3.6 Restricciones

### R1. Balance

La suma de segmentos cubre la demanda.

```text
sum_g sum_k PgSeg[g,k,t] = D[t]
```
### R2. Límite por tramo

Cada segmento no supera su capacidad.

```text
0 <= PgSeg[g,k,t] <= PmaxSeg[g,k]
```
### R3. Generación total

La generación de unidad es suma de tramos.

```text
Pg[g,t] = sum_k PgSeg[g,k,t]
```

## 4. Construcción del archivo `.dat`

El `.dat` debe separar demanda horaria, datos técnicos de unidades, costos y parámetros temporales. Use unidades explícitas: MW, MWh, USD/MWh.

## 5. Interpretación del archivo `.out`

El `.out` debe reportar generación por hora, costo total, energía no servida, estados binarios y uso de recursos hídricos cuando aplique.

## 6. Errores frecuentes

- No vincular generación y estado binario en UC.
- No revisar rampas entre horas.
- Mezclar MW y MWh.
- No interpretar la energía hidro como recurso limitado.

## 7. Actividades relacionadas

- [Actividad 02](../actividades/actividad_02_operacion_corto_plazo.md)
