set S;  # fuentes
set D;  # destinos

param supply {S} >= 0;
param demand {D} >= 0;
param cost {S,D} >= 0;

var x {S,D} >= 0;

minimize TotalCost:
    sum {i in S, j in D} cost[i,j] * x[i,j];

subject to SupplyLimit {i in S}:
    sum {j in D} x[i,j] <= supply[i];

subject to DemandBalance {j in D}:
    sum {i in S} x[i,j] = demand[j];
