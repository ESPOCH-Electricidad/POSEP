# 5. Importación desde Excel y CSV

## Dos rutas recomendadas

### Ruta A: Excel directo con `table`

AMPL puede leer tablas externas mediante declaraciones `table`. Esta opción es útil cuando la instalación tiene habilitado el driver correspondiente.

```ampl
load amplxl.dll;

table Generators IN "amplxl" "input_sep.xlsx" "Generators":
    G <- [GEN], Pmax, cvar;

read table Generators;
```

### Ruta B: Excel/CSV → Python → `.dat`

Esta ruta es más robusta en laboratorios y repositorios porque no depende de drivers locales. Python lee Excel o CSV, valida datos y genera un archivo `.dat` para AMPL.

```text
input.xlsx → python/generar_dat.py → caso.dat → AMPL
```

## Criterio práctico

- Para docencia básica: usar `.dat` y CSV.
- Para flujos profesionales: usar Python como capa de validación.
- Para prototipos rápidos: usar `table` si el entorno lo permite.
