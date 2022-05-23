function faverage(a, b, arr) result(a_o)
    implicit none
    real*8 :: a, b
    real*8, dimension(:)::arr
    real*8 :: a_o
    integer :: i

    a_o = 0
    do i = 1, size(arr)
        a_o = a_o + ((b-a)/size(arr))*arr(i)
    end do
    
end function faverage