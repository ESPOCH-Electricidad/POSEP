# Operación de cascada hidroeléctrica

[Inicio](../../README.md) | [Bloque](../README.md) | [Modelos](README.md) | [Actividades](../actividades/README.md)

![Esquema del modelo](../assets/figuras/modelos/hidrotermico.svg)

## 1. Idea del modelo

Modela varios embalses conectados. La decisión de turbinamiento en una central puede afectar disponibilidad aguas abajo.

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
- `A`: relaciones aguas arriba/abajo.

### 3.2 Índices

- `g`: generador
- `t`: periodo horario
- `h`: unidad hidroeléctrica si aplica

### 3.3 Parámetros

- `Inflow_{r,t}`: aportes.
- `Vmin_r`, `Vmax_r`: límites de volumen.
- `ProdCoef_r`: coeficiente de producción.

### 3.4 Variables de decisión

- `Vol_{r,t}`: volumen.
- `Turb_{r,t}`: turbinamiento.
- `Spill_{r,t}`: vertimiento.
- `Ph_{r,t}`: generación.

### 3.5 Función objetivo

Minimizar costo térmico o maximizar valor hidro, según el caso de estudio.

### 3.6 Restricciones

### R1. Balance hídrico

Volumen actual depende del volumen anterior, aportes, turbinamiento y vertimiento.

```text
Vol[r,t] = Vol[r,t-1] + Inflow[r,t] + upstream[r,t] - Turb[r,t] - Spill[r,t]
```
### R2. Producción hidro

La generación depende del caudal turbinado.

```text
Ph[r,t] = ProdCoef[r] * Turb[r,t]
```
### R3. Límites de volumen

El embalse respeta límites operativos.

```text
Vmin[r] <= Vol[r,t] <= Vmax[r]
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
