# distutils: language = c++

from cpython cimport array
import array

cdef class Enigma:
    cdef int num_rotors
    cdef array.array rotors
    cdef int reflector
    cdef array.array plugboard
    cdef array.array rings
    cdef array.array offsets
