from msilib.schema import Complus
import numpy as np
import matplotlib.pyplot as plt

from src.python.msws32.msws32 import msws32
import src.python.xorshift256 as xs
import src.python.faverage as fv

from numpy import sin, cos, tan, arctan, arccos, arcsin, arccosh, arcsinh, arctanh, tanh, sinh, cosh, log, exp
from numpy import pi, euler_gamma

a = float(input('Ingresa el limite inferior de integración\n'))
b = float(input('Ingresa el limite superior de integración\n'))
n = 10000

func = input('''
Ingresa la funcion a evaluar
+ suma\n
- resta\n
/ division\n
* multiplicacion\n
** potencia\n

Solo se pueden usar parentesis\n
Tambien se encuentran las funciones sin, cos,\n
tan, arctan, arccos, arcsin, arccosh,\n
arcsinh, arctanh, tanh, sinh, cosh, log, exp\n
pueden ser utilizadas como <fn>(x)\n

**SOLO UTILIZAR LA VARIABLE X**\n
funcion:\n
''')

exec(
    compile(f'def f(x): return {func}', 'function', 'exec')
    )

areas = []
n_areas = 100000

v_f = np.vectorize(f)
for _ in range(n_areas):
    areas.append(fv.faverage(a, b, v_f(xs.rnd(a,b,np.zeros(n)))))

plt.title('Distribution of Areas Calculated')
plt.hist(areas, bins = 30, ec = 'black')
plt.xlabel('Areas')
plt.ylabel('Freq')

print(f'La imagen se ha producido\nSe utilizaron {n_areas} areas y {n} evaluaciones para cada area')

plt.savefig('mixedResult.png')
