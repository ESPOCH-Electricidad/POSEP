# Guía 05 — Exportación de resultados

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Guías](README.md)

## Opciones

| Método | Uso |
|---|---|
| `display` | revisión rápida en consola |
| `printf` | escribir resultados controlados |
| `write table` | exportar mediante manejadores de tablas |
| Python/amplpy | convertir variables a DataFrame y escribir Excel |

```ampl
printf {g in G} "%s,%f
", g, P[g] > "resultados_generacion.csv";
```

Antes de exportar, verifique factibilidad, valor objetivo y unidades.
