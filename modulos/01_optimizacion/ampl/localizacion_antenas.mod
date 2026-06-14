# Modelo de localizacion/cobertura de antenas
# Uso docente: reconstruir este modelo desde la formulacion MILP del README.

set C;                 # zonas de carga o clientes
set A;                 # ubicaciones candidatas

param costo {A} >= 0;  # costo de instalar una antena en la ubicacion a
param cubrir {C,A} binary;  # 1 si la antena a cubre la zona c

var y {A} binary;      # 1 si se instala antena en a

minimize CostoTotal:
    sum {a in A} costo[a] * y[a];

subject to Cobertura {c in C}:
    sum {a in A} cubrir[c,a] * y[a] >= 1;
