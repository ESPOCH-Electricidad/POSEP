set P;
param price{P};
param rate{P};
param market{P};
param Hours;

var x{p in P} >= 0, <= market[p];

maximize Revenue:
    sum {p in P} price[p] * x[p];

subject to TimeLimit:
    sum {p in P} x[p] / rate[p] <= Hours;
