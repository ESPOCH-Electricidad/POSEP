# 1. Costos operativos de generación

## Idea central

En operación de corto plazo, el orden de despacho no se construye con CAPEX ni LCOE, sino principalmente con costos variables y restricciones técnicas. El costo variable indica cuánto aumenta el costo del sistema cuando una unidad produce un MWh adicional.

## Costo de combustible

Si una unidad térmica tiene tasa de calor \(HR_g\) en MMBtu/MWh y el combustible cuesta \(p^{fuel}_g\) en USD/MMBtu:

\[
c^{fuel}_g = HR_g p^{fuel}_g
\]

## Costo variable total

\[
c^{var}_g = c^{fuel}_g + c^{VOM}_g + EF_g p^{CO_2}
\]

donde:

- \(c^{VOM}_g\): O&M variable en USD/MWh.
- \(EF_g\): factor de emisión en tCO2/MWh.
- \(p^{CO_2}\): precio del carbono en USD/tCO2.

## Relación heat rate–eficiencia

Como \(1\;MWh = 3.412\;MMBtu\), la eficiencia aproximada es:

\[
\eta_g = \frac{3.412}{HR_g}
\]

Una unidad con mayor heat rate necesita más combustible por MWh y, en general, tiene mayor costo variable.

## Ejemplo

Si \(HR=7.2\;MMBtu/MWh\), \(p^{fuel}=6.5\;USD/MMBtu\), \(c^{VOM}=3\;USD/MWh\), \(EF=0.36\;tCO2/MWh\) y \(p^{CO2}=30\;USD/tCO2\):

\[
c^{fuel}=7.2(6.5)=46.8\;USD/MWh
\]

\[
c^{CO2}=0.36(30)=10.8\;USD/MWh
\]

\[
c^{var}=46.8+3+10.8=60.6\;USD/MWh
\]

## Lectura técnica

Un cambio en precio de combustible o carbono puede alterar el orden de mérito y desplazar unidades que antes eran económicas.
