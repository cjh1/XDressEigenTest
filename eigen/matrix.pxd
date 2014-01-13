cdef extern from *:
    ctypedef void* int_parameter
    int_parameter one "1"
    int_parameter two "2"
    int_parameter three "3"

cdef extern from "<Eigen/Dense>" namespace "Eigen":
    cdef cppclass Matrix[T, R, C]:
        Matrix() nogil except +

