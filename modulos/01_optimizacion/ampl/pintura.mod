set P;
set R;

param beneficio {P} >= 0;
param recurso_disp {R} >= 0;
param consumo {R,P} >= 0;

var x {P} >= 0;

maximize BeneficioTotal:
    sum {p in P} beneficio[p] * x[p];

subject to Recurso {r in R}:
    sum {p in P} consumo[r,p] * x[p] <= recurso_disp[r];
