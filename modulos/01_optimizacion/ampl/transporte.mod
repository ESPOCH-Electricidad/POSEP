set I;
set J;

param oferta {I} >= 0;
param demanda {J} >= 0;
param costo {I,J} >= 0;

var flujo {I,J} >= 0;

minimize CostoTotal:
    sum {i in I, j in J} costo[i,j] * flujo[i,j];

subject to Oferta {i in I}:
    sum {j in J} flujo[i,j] <= oferta[i];

subject to Demanda {j in J}:
    sum {i in I} flujo[i,j] = demanda[j];
