list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_LIST_DIR}/cmake)
include( UseCython )

if( NOT NUMPY_INCLUDE_DIR )
  find_package( PythonInterp )
  execute_process(
    COMMAND ${PYTHON_EXECUTABLE} -c "import numpy; print(numpy.get_include())"
    OUTPUT_VARIABLE _numpy_include
    OUTPUT_STRIP_TRAILING_WHITESPACE
    )
  find_path( NUMPY_INCLUDE_DIR numpy/arrayobject.h
    HINTS ${_numpy_include} )
endif()

include_directories( ${NUMPY_INCLUDE_DIR}  )

set_source_files_properties( ${cxx_pyx_files}
    PROPERTIES CYTHON_IS_CXX TRUE )


cython_add_module( stlcontainers ${CMAKE_BINARY_DIR}/eigentest/stlcontainers.pyx )
cython_add_module( eigentest_extra_types ${CMAKE_BINARY_DIR}/eigentest/eigentest_extra_types.pyx )
cython_add_module( eigentest ${CMAKE_BINARY_DIR}/eigentest/eigentest.pyx )
