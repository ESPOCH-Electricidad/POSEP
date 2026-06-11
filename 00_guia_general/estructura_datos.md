# Estructura sugerida de datos

## Archivos mínimos por caso

```text
caso_x/
├── README.md
├── metadata.yaml
├── datos_csv/
│   ├── buses.csv
│   ├── branches.csv
│   ├── generators.csv
│   └── demands.csv
├── datos_dat/
│   └── caso_x.dat
└── notebooks/
    └── explorar_caso_x.ipynb
```

## Campos recomendados

### buses.csv

| Campo | Descripción |
|---|---|
| bus | Identificador de barra |
| type | Tipo: slack, PV, PQ, load, generation |
| Pd | Demanda activa |
| Qd | Demanda reactiva, si aplica |
| Vmax | Límite superior de tensión |
| Vmin | Límite inferior de tensión |

### branches.csv

| Campo | Descripción |
|---|---|
| from_bus | Barra origen |
| to_bus | Barra destino |
| r | Resistencia |
| x | Reactancia |
| b | Susceptancia shunt |
| rateA | Límite térmico |
| existing | 1 si existe, 0 si es candidato |
| max_new | Número máximo de circuitos candidatos |

### generators.csv

| Campo | Descripción |
|---|---|
| gen | Identificador |
| bus | Barra |
| Pmin | Potencia mínima |
| Pmax | Potencia máxima |
| cost | Costo variable |
| startup | Costo de arranque, si aplica |
| technology | Tecnología |
| firm | Crédito de capacidad firme |
| emissions | Factor de emisiones |
