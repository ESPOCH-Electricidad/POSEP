set K;
set B;
set Y ordered;

param demand {B,Y} >= 0;
param hours {B} >= 0;
param existing_cap {K} >= 0 default 0;
param max_new_cap {K,Y} >= 0 default Infinity;
param inv_ann {K,Y} >= 0;
param fom {K} >= 0 default 0;
param vom {K} >= 0;
param af {K,B,Y} >= 0 <= 1;
param firm_credit {K} >= 0 <= 1;
param peak_demand {Y} >= 0;
param reserve_margin {Y} >= 0 default 0.15;
param VOLL >= 0 default 5000;

var Build {K,Y} >= 0;
var Cap {K,Y} >= 0;
var Gen {K,B,Y} >= 0;
var LS {B,Y} >= 0;

minimize TotalCost:
    sum {k in K, y in Y} (inv_ann[k,y] + fom[k]) * Build[k,y]
  + sum {k in K, b in B, y in Y} vom[k] * Gen[k,b,y] * hours[b]
  + sum {b in B, y in Y} VOLL * LS[b,y] * hours[b];

subject to CapacityFirst {k in K, y in Y: ord(y)=1}:
    Cap[k,y] = existing_cap[k] + Build[k,y];

subject to CapacityNext {k in K, y in Y: ord(y)>1}:
    Cap[k,y] = Cap[k,prev(y)] + Build[k,y];

subject to MaxBuild {k in K, y in Y}:
    Build[k,y] <= max_new_cap[k,y];

subject to Balance {b in B, y in Y}:
    sum {k in K} Gen[k,b,y] + LS[b,y] = demand[b,y];

subject to GenerationLimit {k in K, b in B, y in Y}:
    Gen[k,b,y] <= af[k,b,y] * Cap[k,y];

subject to ReserveRequirement {y in Y}:
    sum {k in K} firm_credit[k] * Cap[k,y] >= (1 + reserve_margin[y]) * peak_demand[y];
