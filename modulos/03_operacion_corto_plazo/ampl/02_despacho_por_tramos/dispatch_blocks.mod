set G;
set T;
set K;

param demand {T} >= 0;
param block_cap {G,K} >= 0;
param block_cost {G,K} >= 0;

var p {G,K,T} >= 0;

minimize TotalCost:
    sum {g in G, k in K, t in T} block_cost[g,k] * p[g,k,t];

subject to Balance {t in T}:
    sum {g in G, k in K} p[g,k,t] = demand[t];

subject to BlockLimit {g in G, k in K, t in T}:
    p[g,k,t] <= block_cap[g,k];
