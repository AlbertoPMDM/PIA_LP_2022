function rnd(a, b, arr) result(arr_o)
    implicit none
    real*8, intent(in) :: a, b
    real*8, dimension(:) :: arr
    real*8, dimension(size(arr)) :: arr_o
    
    CALL random_number(arr)

    arr_o = (b-a) * arr + a 

end function rnd