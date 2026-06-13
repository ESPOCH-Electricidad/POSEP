# Cascada hidroeléctrica con restricciones de rampa

[Inicio](../../README.md) | [Bloque](../README.md) | [Modelos](README.md) | [Actividades](../actividades/README.md)

![Esquema del modelo](../assets/figuras/modelos/hidrotermico.svg)

## 1. Idea del modelo

Extiende la operación de cascadas incorporando límites de variación temporal en generación o caudal turbinado.

## 2. Lectura didáctica previa

| Elemento | Interpretación |
|---|---|
| Horizonte | Corto plazo: horas o días. |
| Decisión | Generación, estado o uso de recursos por periodo. |
| Salida clave | Costo operativo, despacho, ENS y restricciones activas. |

## 3. Formulación matemática

### 3.1 Conjuntos

- `R`: embalses.
- `T`: periodos.

### 3.2 Índices

- `g`: generador
- `t`: periodo horario
- `h`: unidad hidroeléctrica si aplica

### 3.3 Parámetros

- `RampUp_r`, `RampDown_r`: rampas.
- `TurbMin_r`, `TurbMax_r`: límites de turbinamiento.

### 3.4 Variables de decisión

- `Turb_{r,t}`
- `Vol_{r,t}`
- `Ph_{r,t}`

### 3.5 Función objetivo

Optimizar operación respetando dinámica hidráulica y rampas.

### 3.6 Restricciones

### R1. Rampa subida

El turbinamiento no puede aumentar más que la rampa permitida.

```text
Turb[r,t] - Turb[r,t-1] <= RampUp[r]
```
### R2. Rampa bajada

El turbinamiento no puede disminuir más que la rampa permitida.

```text
Turb[r,t-1] - Turb[r,t] <= RampDown[r]
```
### R3. Balance hídrico

Se mantiene la conservación de volumen.

```text
Vol[r,t] = Vol[r,t-1] + Inflow[r,t] - Turb[r,t] - Spill[r,t]
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
