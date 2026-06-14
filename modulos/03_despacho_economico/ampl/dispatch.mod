set G;
set T;

param demand {T} >= 0;
param Pmin {G} >= 0 default 0;
param Pmax {G} >= 0;
param cvar {G} >= 0;
param VOLL >= 0 default 5000;

var Pg {G,T} >= 0;
var LS {T} >= 0;

minimize TotalCost:
    sum {g in G, t in T} cvar[g] * Pg[g,t]
  + sum {t in T} VOLL * LS[t];

subject to Balance {t in T}:
    sum {g in G} Pg[g,t] + LS[t] = demand[t];

subject to MinGen {g in G, t in T}:
    Pg[g,t] >= Pmin[g];

subject to MaxGen {g in G, t in T}:
    Pg[g,t] <= Pmax[g];
