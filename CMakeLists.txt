cmake_minimum_required(VERSION 2.8)

project(EigenTest)

set( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_LIST_DIR}/cmake )

include( UseCython )

find_package(Eigen3 REQUIRED)

# With CMake, a clean separation can be made between the source tree and the
# build tree.  When all source is compiled, as with pure C/C++, the source is
# no-longer needed in the build tree.  However, with pure *.py source, the
# source is processed directly.  To handle this, we reproduce the availability
# of the source files in the build tree.
add_custom_target( ReplicatePythonSourceTree ALL ${CMAKE_COMMAND} -P
  ${CMAKE_CURRENT_SOURCE_DIR}/cmake/ReplicatePythonSourceTree.cmake
  ${CMAKE_CURRENT_BINARY_DIR}
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} )

set( cxx_pyx_files
  eigentest.pyx
  stlcontainers.pyx
  eigentest_extra_types.pyx
)

get_directory_property(_include_directories DIRECTORY
  . INCLUDE_DIRECTORIES )


list(APPEND _include_directories ${EIGEN3_INCLUDE_DIR} ${CMAKE_INSTALL_PREFIX}/include)

add_custom_target(xdress ALL
  COMMAND xdress --builddir ${CMAKE_CURRENT_BINARY_DIR} --packagedir ${CMAKE_CURRENT_BINARY_DIR}/eigentest   -I  ${_include_directories} WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  COMMENT "Running xdress ...")

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

#  set_source_files_properties( ${cxx_pyx_files}
#    PROPERTIES CYTHON_IS_CXX TRUE )

#  cython_add_module( stlcontainers stlcontainers.pyx )
#

