module msws
    implicit none
    
contains
subroutine rand32(n, a_o)
    implicit none
    integer*8, intent(in) :: n
    integer*4, dimension(n), intent(out) :: a_o
    integer*8 :: x, w, s
    integer*4 :: o
    integer :: i

    DATA s/z'b5ad4eceda1ce2a9'/

    x = 0_8
    w = 0_8

    a_o = 0
    print *, a_o

    do i = 1, size(a_o)
        x = x * x
        w = w + s
        x = x + w
        o = ior(lshift(x, 32), rshift(x, 32))
        a_o(i) = o
        print *, i
    end do

    print *, a_o
    
end subroutine rand32
end module msws