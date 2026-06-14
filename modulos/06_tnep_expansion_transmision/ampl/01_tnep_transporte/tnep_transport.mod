set N;
set G;
set L within {N,N};

param bus {G} symbolic in N;
param demand {N} >= 0;
param Pmax {G} >= 0;
param cvar {G} >= 0 default 0;
param Fmax {L} >= 0;
param existing {L} >= 0 integer default 0;
param invcost {L} >= 0;
param VOLL >= 0 default 5000;

var Pg {G} >= 0;
var f {L};
var y {L} binary;
var LS {N} >= 0;

minimize TotalCost:
    sum {(i,j) in L} invcost[i,j] * y[i,j]
  + sum {g in G} cvar[g] * Pg[g]
  + sum {n in N} VOLL * LS[n];

subject to Balance {n in N}:
    sum {g in G: bus[g]=n} Pg[g] + LS[n] - demand[n]
    = sum {(i,j) in L: i=n} f[i,j] - sum {(i,j) in L: j=n} f[i,j];

subject to GenLimit {g in G}:
    Pg[g] <= Pmax[g];

subject to FlowMax {(i,j) in L}:
    f[i,j] <= Fmax[i,j] * (existing[i,j] + y[i,j]);

subject to FlowMin {(i,j) in L}:
    f[i,j] >= -Fmax[i,j] * (existing[i,j] + y[i,j]);

subject to ExistingFixed {(i,j) in L: existing[i,j] > 0}:
    y[i,j] = 0;
