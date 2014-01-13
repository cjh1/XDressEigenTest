cdef extern from "<Eigen/Dense>" namespace "Eigen":
    cdef cppclass Matrix[T, R, C]:
        Matrix() nogil except +

