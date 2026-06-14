# 5. Programación entera mixta

## Definición

Un problema MILP combina variables continuas con variables enteras o binarias:

\[
\min c^Tx+d^Ty
\]

\[
Ax+By \leq b
\]

\[
x \geq 0
\]

\[
y \in \{0,1\}^n
\]

## Lectura técnica

Las variables binarias representan decisiones lógicas: construir/no construir, encender/apagar, seleccionar/no seleccionar, activar/desactivar. En sistemas eléctricos aparecen en compromiso de unidades, expansión de líneas, selección de tecnologías y ubicación de recursos.

## Restricción de activación

Una relación frecuente es:

\[
x \leq My
\]

Si \(y=0\), entonces \(x=0\). Si \(y=1\), \(x\) puede tomar valores hasta \(M\).

## Riesgo del parámetro Big-M

El valor de \(M\) debe ser suficientemente grande para no cortar soluciones factibles, pero no excesivamente grande porque degrada la relajación lineal y puede generar inestabilidad numérica.

## Ejemplo: construir una línea

\[
-f^{max}y \leq f \leq f^{max}y
\]

Si la línea no se construye \((y=0)\), el flujo debe ser cero. Si se construye \((y=1)\), el flujo puede moverse dentro de sus límites térmicos.

## Complejidad

Los MILP son más difíciles que los LP porque el solver debe explorar combinaciones discretas. Métodos como branch-and-bound y branch-and-cut combinan relajaciones lineales, cotas y poda de ramas.
