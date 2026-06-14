# Actividad 01A — Programación lineal de producción

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Datos](../datos/) · [Guía AMPL](../../../docs/guia_ampl.md)

## Competencia

Formular e implementar un problema de programación lineal identificando variables de decisión, función objetivo, restricciones activas, recursos limitantes y sensibilidad de parámetros.

## Enunciado

Una planta puede producir pintura azul y pintura negra. Cada producto tiene precio de venta, tasa de producción y límite de mercado. La planta dispone de un número limitado de horas semanales. Se debe decidir cuántos litros producir de cada pintura para maximizar ingresos, sin exceder capacidad de producción ni demanda de mercado.

## Datos del caso

Use los archivos `pintura_productos.csv` y `pintura_parametros.csv`.

| Producto | Precio [USD/L] | Producción [L/h] | Mercado máximo [L] |
|---|---:|---:|---:|
| azul | 10 | 40 | 1000 |
| negra | 15 | 30 | 860 |

| Parámetro | Valor | Unidad |
|---|---:|---|
| Hours | 40 | h/semana |

## Formulación requerida

Defina el conjunto de productos $p \in P$. La variable $x_p$ representa litros producidos por producto.

Función objetivo:

$$
\max Z=\sum_{p\in P} price_p x_p
$$

Restricción de tiempo:

$$
\sum_{p\in P}\frac{x_p}{rate_p}\leq Hours
$$

Restricción de mercado:

$$
0\leq x_p\leq market_p \qquad \forall p\in P
$$

## Tareas

1. Construya el archivo `caso.dat` desde las tablas del enunciado.
2. Escriba `modelo.mod` usando conjuntos y parámetros, no valores fijos dentro de las restricciones.
3. Cree `ejecutar.run` para resolver y mostrar producción, ingreso total y uso de horas.
4. Identifique si el límite de horas es activo.
5. Repita el caso aumentando `Hours` a 45 y explique el cambio.
6. Repita el caso reduciendo el mercado máximo de pintura negra a 700 L.

## Validación

Compruebe que la producción no excede el mercado máximo y que las horas usadas no superan las disponibles. Si la solución usa exactamente 40 horas, interprete el valor económico de una hora adicional.

## Entregables

- Formulación matemática.
- `modelo.mod`, `caso.dat`, `ejecutar.run`.
- Tabla de producción y uso de recursos.
- Dos escenarios de sensibilidad.
- Conclusión técnica de máximo 10 líneas.

## Evaluación

| Criterio | Peso |
|---|---:|
| Formulación general con conjuntos y parámetros | 30 % |
| Archivo `.dat` correctamente construido | 20 % |
| Solución y validación de restricciones | 25 % |
| Sensibilidad e interpretación | 25 % |
