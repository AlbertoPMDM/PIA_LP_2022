# UwU

Se tienen que compilar los archivos de fortran antes de correr lo de python

``py -m numpy.f2py  -c --fcompiler=gnu95 --compiler=mingw32 ../fortran/example.f95 -m example

py py -m numpy.f2py  -c --fcompiler=gnu95 --compiler=mingw32 src/fortran/fmsws32.f95 -m fmsws32 -h fmsws32.pyf

py -m numpy.f2py src/fortran/fmsws32.f95 -m fmsws32 -h fmsws32.pyf

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

program cum
    use msws
    implicit none
    integer*8 :: n
    double precision, allocatable, dimension(:) :: a
    
    n = 10

    a = msws32(0_8, 1_8, n)

    print *, a
    
end program cum

