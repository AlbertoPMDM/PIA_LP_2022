# UwU

Se tienen que compilar los archivos de fortran antes de correr lo de python

`py -m numpy.f2py  -c --fcompiler=gnu95 --compiler=mingw32 ../fortran/example.f95 -m example`

esa linea de arriba sirvio para mi en Win10

en Ubuntu, 

`python3 -m numpy.f2py -c ../fortran/example.f95 -m example`

# TODO
### MOntecarlo integration
+ Pseudorandom number generator
        + bit shifting
        + maybe middle square weyl sequence
        http://arxiv-export-lb.library.cornell.edu/pdf/1704.00358
+ Check statistical randomness
+ Mock up in python only
+ timing of the time-critical sections
+ implementation of time-critical sections in fortran
+ implementation of fortran in pyton

