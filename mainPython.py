import matplotlib.pyplot as plt

from src.python.msws32.msws32 import msws32

from numpy import sin, cos, tan, arctan, arccos, arcsin, arccosh, arcsinh, arctanh, tanh, sinh, cosh, log, exp
from numpy import pi, euler_gamma

rnd = msws32()

a = float(input('Ingresa el limite inferior de integración\n'))
b = float(input('Ingresa el limite superior de integración\n'))
n = 1000

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
n_areas = 1000

for _ in range(n_areas):
    xrand = [i for i in rnd.rand32(a, b, n, rnd.state)]

    integral = 0
    for i in xrand:
        integral += f(i)
    answer = (b-a)/n*integral

    areas.append(answer)

plt.title('Distribution of Areas Calculated')
plt.hist(areas, bins = 30, ec = 'black')
plt.xlabel('Areas')
plt.ylabel('Freq')

print(f'La imagen se ha producido\nSe utilizaron {n_areas} areas y {n} evaluaciones para cada area')

plt.show()

# plt.savefig('pythonResult.png')
