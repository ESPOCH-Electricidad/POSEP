set K;
set B;

param demand {B} >= 0;
param hours {B} >= 0;
param existing_cap {K} >= 0 default 0;
param max_new_cap {K} >= 0 default Infinity;
param inv_ann {K} >= 0;
param fom {K} >= 0 default 0;
param vom {K} >= 0;
param af {K,B} >= 0 <= 1;
param firm_credit {K} >= 0 <= 1;
param peak_demand >= 0;
param reserve_margin >= 0 default 0.15;
param VOLL >= 0 default 5000;

var NewCap {K} >= 0;
var Cap {K} >= 0;
var Gen {K,B} >= 0;
var LS {B} >= 0;

minimize TotalCost:
    sum {k in K} (inv_ann[k] + fom[k]) * NewCap[k]
  + sum {k in K, b in B} vom[k] * Gen[k,b] * hours[b]
  + sum {b in B} VOLL * LS[b] * hours[b];

subject to CapacityDef {k in K}:
    Cap[k] = existing_cap[k] + NewCap[k];

subject to MaxNew {k in K}:
    NewCap[k] <= max_new_cap[k];

subject to Balance {b in B}:
    sum {k in K} Gen[k,b] + LS[b] = demand[b];

subject to GenerationLimit {k in K, b in B}:
    Gen[k,b] <= af[k,b] * Cap[k];

subject to ReserveRequirement:
    sum {k in K} firm_credit[k] * Cap[k] >= (1 + reserve_margin) * peak_demand;
