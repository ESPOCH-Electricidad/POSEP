set N;
set G;
set L within {N,N};
set T;

param bus {G} symbolic in N;
param demand {N,T} >= 0;
param Pmax {G} >= 0;
param cvar {G} >= 0;
param B {L};
param Fmax {L} >= 0;
param ref symbolic in N;

var Pg {G,T} >= 0;
var theta {N,T};
var f {L,T};

minimize TotalCost:
    sum {g in G, t in T} cvar[g] * Pg[g,t];

subject to FlowDef {(i,j) in L, t in T}:
    f[i,j,t] = B[i,j] * (theta[i,t] - theta[j,t]);

subject to Balance {n in N, t in T}:
    sum {g in G: bus[g]=n} Pg[g,t] - demand[n,t]
    = sum {(i,j) in L: i=n} f[i,j,t] - sum {(i,j) in L: j=n} f[i,j,t];

subject to GenLimit {g in G, t in T}:
    Pg[g,t] <= Pmax[g];

subject to LineMax {(i,j) in L, t in T}:
    f[i,j,t] <= Fmax[i,j];

subject to LineMin {(i,j) in L, t in T}:
    f[i,j,t] >= -Fmax[i,j];

subject to Reference {t in T}:
    theta[ref,t] = 0;
