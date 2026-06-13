# Caso IEEE 14 barras

[Inicio](../../README.md) | [Casos de estudio](../README.md)

## Estado

**Completo.**

## Propósito

Sistema de prueba para flujo de potencia y OPF. Se usa como primer caso de red con datos AC.

## Datos disponibles

| Archivo | Descripción |
|---|---|
| `datos/ieee14_opf_ac.dat` | Datos adaptados para OPF-AC. |

## Usos recomendados

| Modelo | Uso |
|---|---|
| OPF-AC | Análisis de tensión, potencia activa/reactiva y límites. |
| OPF-DC | Puede derivarse una aproximación DC a partir de los datos. |

## Recomendaciones de uso

1. Revisar el archivo de datos antes de construir el `.dat` propio.
2. Verificar unidades y escalas económicas.
3. Documentar toda adaptación realizada.
4. Comparar los resultados con el comportamiento esperado del sistema.
