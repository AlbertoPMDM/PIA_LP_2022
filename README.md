# UwU

Se tienen que compilar los archivos de fortran antes de correr lo de python

`py -m numpy.f2py  -c --fcompiler=gnu95 --compiler=mingw32 ../fortran/example.f95 -m example`

esa linea de arriba sirvio para mi en Win10

en Ubuntu, 

`python3 -m numpy.f2py -c ../fortran/example.f95 -m example`

