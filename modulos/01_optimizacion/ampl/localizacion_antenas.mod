set A;        # ubicaciones candidatas
set Z;        # zonas de demanda

param costo {A} >= 0;
param cobertura {A,Z} binary;
param presupuesto >= 0;

var y {A} binary;
var atendida {Z} binary;

maximize ZonasCubiertas:
    sum {z in Z} atendida[z];

subject to Presupuesto:
    sum {a in A} costo[a] * y[a] <= presupuesto;

subject to ActivarCobertura {z in Z}:
    atendida[z] <= sum {a in A} cobertura[a,z] * y[a];
