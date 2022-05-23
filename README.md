# Integracion de Monte Carlo

Se utilizó el compilador de fortran de gnu, junto con el compilador default de la instalación de windows que tengo, auqneu preferiblemente hacerlo en linux, pues tiene menos complicaciones.

Se tienen que compilar los archivos de fortran antes de correr lo de python, desde el folder de python correr

`py -m numpy.f2py  -c --fcompiler=gnu95 --compiler=mingw32 ../fortran/faverage.f95 -m faverage`
`py -m numpy.f2py  -c --fcompiler=gnu95 --compiler=mingw32 ../fortran/xorshift256.f95 -m xorshift256`

esa linea de arriba sirvio para mi en Win10

en Ubuntu, 

`python3 -m numpy.f2py -c ../fortran/xorshift256.f95 -m xorshift256`
`python3 -m numpy.f2py -c ../fortran/faverage.f95 -m faverage`

En `main.py` se encuentra un ejemplo de como se utiliza, devuelve un histograma de los diferentes valores para la integral obtenidos

los archivos `*_graphs.py` producen imagenes de los tiempos que tarda en correr el generador de numeros aleatorios en el sistema.

Referencias

https://en.wikipedia.org/wiki/Law_of_large_numbers
https://en.wikipedia.org/wiki/Monte_Carlo_integration
https://www.youtube.com/watch?v=WAf0rqwAvgg
http://arxiv-export-lb.library.cornell.edu/pdf/1704.00358


