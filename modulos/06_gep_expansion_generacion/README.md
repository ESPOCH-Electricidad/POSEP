# Modelos — Expansión de generación

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)

Este bloque contiene tres modelos GEP organizados por complejidad. No todos son multietapa: el criterio para clasificar un modelo como multietapa es que la inversión esté indexada temporalmente, que exista persistencia o acumulación de capacidad entre periodos y que el modelo pueda representar el momento de construcción.

| Modelo | Tipo | Clasificación temporal | Acceso |
|---|---|---|---|
| GEP base por periodos | MIP simplificado | Multietapa simplificado | [Abrir](01_modelo_gep_estatico_capacidad.md) |
| GEP estático con bloques de carga | LP/MILP estático | Estático | [Abrir](02_modelo_gep_bloques_carga.md) |
| GEP multianual con selección tecnológica | MILP multianual | Multietapa completo | [Abrir](03_modelo_gep_multianual.md) |

## Lectura recomendada

1. Revisar primero el modelo base por periodos para entender la acumulación de capacidad.
2. Revisar después el modelo estático con bloques para conectar inversión y operación anual representativa.
3. Revisar finalmente el modelo multianual, donde aparecen selección tecnológica, construcción anual, lead time, operación por bloques, emisiones, renovables, presupuesto y ENS.

## Archivos AMPL asociados

| Modelo | Archivos esperados |
|---|---|
| GEP base por periodos | `GEP_base_Garver.mod`, `GEP_base_Garver.dat`, `GEP_base_Garver.run`, `GEP_base_Garver.out` |
| GEP estático con bloques | `gep_static_garver.mod`, `gep_static_garver.dat`, `gep_static_garver.run`, `gep_static_garver.out` |
| GEP multianual | `gep_multiyear_garver.mod`, `gep_multiyear_garver.dat`, `gep_multiyear_garver.run`, `gep_multiyear_garver.out` |

---

[Menú principal](../../../README.md) · [Volver al módulo](../README.md) · [Actividades](../actividades/README.md) · [Datos](../datos/)
