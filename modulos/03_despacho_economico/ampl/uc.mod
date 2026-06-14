set G;
set T ordered;

param demand {T} >= 0;
param reserve {T} >= 0 default 0;
param Pmin {G} >= 0;
param Pmax {G} >= 0;
param cvar {G} >= 0;
param cstart {G} >= 0;
param RU {G} >= 0 default Infinity;
param RD {G} >= 0 default Infinity;
param u0 {G} binary default 0;
param P0 {G} >= 0 default 0;

var u {G,T} binary;
var v {G,T} binary;
var Pg {G,T} >= 0;

minimize TotalCost:
    sum {g in G, t in T} cvar[g] * Pg[g,t]
  + sum {g in G, t in T} cstart[g] * v[g,t];

subject to Balance {t in T}:
    sum {g in G} Pg[g,t] = demand[t];

subject to ReserveReq {t in T}:
    sum {g in G} (Pmax[g]*u[g,t] - Pg[g,t]) >= reserve[t];

subject to MinOutput {g in G, t in T}:
    Pg[g,t] >= Pmin[g] * u[g,t];

subject to MaxOutput {g in G, t in T}:
    Pg[g,t] <= Pmax[g] * u[g,t];

subject to StartupFirst {g in G, t in T: ord(t)=1}:
    v[g,t] >= u[g,t] - u0[g];

subject to StartupNext {g in G, t in T: ord(t)>1}:
    v[g,t] >= u[g,t] - u[g,prev(t)];

subject to RampUpFirst {g in G, t in T: ord(t)=1}:
    Pg[g,t] - P0[g] <= RU[g];

subject to RampUpNext {g in G, t in T: ord(t)>1}:
    Pg[g,t] - Pg[g,prev(t)] <= RU[g];

subject to RampDownFirst {g in G, t in T: ord(t)=1}:
    P0[g] - Pg[g,t] <= RD[g];

subject to RampDownNext {g in G, t in T: ord(t)>1}:
    Pg[g,prev(t)] - Pg[g,t] <= RD[g];
