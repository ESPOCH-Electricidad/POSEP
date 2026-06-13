# Flujo óptimo de potencia AC

[Inicio](../../README.md) | [Bloque](../README.md) | [Modelos](README.md) | [Actividades](../actividades/README.md)

![Esquema del modelo](../assets/figuras/modelos/opf_red_dc_ac.svg)

## 1. Idea del modelo

El OPF-AC representa el comportamiento eléctrico completo mediante ecuaciones no lineales de potencia activa y reactiva. Permite analizar tensión, potencia reactiva, pérdidas y límites operativos más cercanos a la operación real.

## 2. Lectura didáctica previa

| Elemento | Interpretación |
|---|---|
| Decisión | Generación activa/reactiva, tensiones y ángulos. |
| Restricción física | Ecuaciones no lineales de flujo AC. |
| Ventaja | Representación eléctrica más completa. |
| Limitación | Problema no lineal y más difícil de resolver. |

## 3. Formulación matemática

### 3.1 Conjuntos

- `N`: barras.
- `L`: líneas.
- `G`: generadores.

### 3.2 Índices

- `i,j ∈ N`: barras conectadas.
- `g ∈ G`: generador.

### 3.3 Parámetros

- `Pd_i`, `Qd_i`.
- `G_ij`, `B_ij`: admitancia.
- `Vmin_i`, `Vmax_i`.
- `Pmin_g`, `Pmax_g`, `Qmin_g`, `Qmax_g`.

### 3.4 Variables de decisión

- `Pg_g`, `Qg_g`.
- `V_i`: magnitud de tensión.
- `theta_i`: ángulo.
- `Pij`, `Qij`: flujos.

### 3.5 Función objetivo

Minimizar costo de generación sujeto a ecuaciones AC y límites operativos.

### 3.6 Restricciones

### R1. Balance activo

Generación activa menos demanda activa igual a inyección AC.

```text
Pg_i - Pd_i = P_i(V,theta)
```
### R2. Balance reactivo

Generación reactiva menos demanda reactiva igual a inyección reactiva.

```text
Qg_i - Qd_i = Q_i(V,theta)
```
### R3. Límites de tensión

Cada barra mantiene tensión dentro de rango.

```text
Vmin_i <= V_i <= Vmax_i
```
### R4. Límites de generación

Generadores respetan límites P y Q.

```text
Pmin_g <= Pg_g <= Pmax_g; Qmin_g <= Qg_g <= Qmax_g
```

## 4. Construcción del archivo `.dat`

El `.dat` debe incluir datos eléctricos completos: r, x, b, límites de tensión y límites de reactivos.

## 5. Interpretación del archivo `.out`

El `.out` debe reportar tensiones, ángulos, P/Q de generadores, flujos, pérdidas y posibles límites activos.

## 6. Errores frecuentes

- Usar datos DC incompletos para AC.
- No inicializar variables de tensión/ángulo.
- Ignorar límites de reactivos.
- Comparar DC y AC sin considerar pérdidas.

## 7. Actividades relacionadas

- [Actividad 03](../actividades/actividad_03_opf_dc_ac.md)
