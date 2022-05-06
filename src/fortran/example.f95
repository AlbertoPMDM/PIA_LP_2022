function rnd(a, b, arr) result(arr_o)
    implicit none
    real*8, intent(in) :: a, b
    real*8, dimension(:) :: arr
    real*8, dimension(size(arr)) :: arr_o
    
    CALL random_number(arr)

    arr_o = (b-a) * arr + a

end function rnd

function array_func(a) result(a_o)
    implicit none
    real*8, dimension(:) :: a
    real*8, dimension(SIZE(a)) :: a_o
    integer :: i

    do i = 1, SIZE(a)
        a_o(i) = 2*a(i)
    end do
    
end function array_func