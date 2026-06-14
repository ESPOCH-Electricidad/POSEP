set GTH;
set H;
set T ordered;

param demand {T} >= 0;
param cvar {GTH} >= 0;
param Pmax_th {GTH} >= 0;
param inflow {H,T} >= 0;
param Smin {H} >= 0;
param Smax {H} >= 0;
param S0 {H} >= 0;
param Rmax {H} >= 0;
param rho {H} >= 0;
param VOLL >= 0 default 5000;

var Pg {GTH,T} >= 0;
var Ph {H,T} >= 0;
var R {H,T} >= 0;
var Spill {H,T} >= 0;
var S {H,T} >= 0;
var LS {T} >= 0;

minimize TotalCost:
    sum {g in GTH, t in T} cvar[g] * Pg[g,t]
  + sum {t in T} VOLL * LS[t];

subject to Balance {t in T}:
    sum {g in GTH} Pg[g,t] + sum {h in H} Ph[h,t] + LS[t] = demand[t];

subject to ThermalLimit {g in GTH, t in T}:
    Pg[g,t] <= Pmax_th[g];

subject to HydroConversion {h in H, t in T}:
    Ph[h,t] = rho[h] * R[h,t];

subject to ReleaseLimit {h in H, t in T}:
    R[h,t] <= Rmax[h];

subject to StorageFirst {h in H, t in T: ord(t)=1}:
    S[h,t] = S0[h] + inflow[h,t] - R[h,t] - Spill[h,t];

subject to StorageNext {h in H, t in T: ord(t)>1}:
    S[h,t] = S[h,prev(t)] + inflow[h,t] - R[h,t] - Spill[h,t];

subject to StorageMin {h in H, t in T}:
    S[h,t] >= Smin[h];

subject to StorageMax {h in H, t in T}:
    S[h,t] <= Smax[h];
