
subroutine func(x, x_o)
implicit none
real*8,intent(in) :: x
real*8,intent(out) :: x_o

x_o = x**2 + x + 1
end subroutine func

function func2() result(x_o)
implicit none
real*8 :: x_o, xtemp
integer :: i

x_o = 0
do i = 1, 10000000
xtemp = i
x_o = x_o + (xtemp**2 + xtemp + 1)
end do
end function func2

function array_func(a) result(a_o)
    implicit none
    real*8, dimension(:) :: a
    real*8, dimension(SIZE(a)) :: a_o
    integer :: i

    do i = 1, SIZE(a)
        a_o(i) = 2*a(i)
    end do
    
end function array_func