program cummy
    implicit none
    integer*8 :: x, w, s, n, i
    integer*4 :: o
    double precision :: r

    DATA s/z'b5ad4eceda1ce2a9'/

    x = 0
    w = 0

    n = 3000

    do i = 1, n
        x = x * x
        w = w + s
        x = x + w
        o = ishftc(x, 32)
        r = (o + 2147483648._8)/4294967295._8
        print '(*(f21.18))', r
    end do

end program cummy