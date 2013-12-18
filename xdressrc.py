from xdress.utils import apiname
from xdress.typesystem import TypeSystem
import os

ts = TypeSystem.empty()
package = 'eigentest'     # top-level python package name
extra_types = 'eigentest_extra_types'

stlcontainers = [
    ('vector', 'str'),
    ('set', 'uint'),
    ('map', 'int', 'float'),
    ]

_fromsrcdir = lambda x: os.path.join('core', x)
_incore = {'srcfiles': _fromsrcdir('eigentest.h'),
           'incfiles': 'eigentest.h',
           'language': 'c++', }

c2py = (
        ('{proxy_name}_shape = (x,y)\n'
         '{proxy_name} = np.PyArray_SimpleNewFromData(2, {var}_shape, {t.cython_nptypes[0]}, &{var}[0])\n'
         '{proxy_name} = np.PyArray_Copy({proxy_name})\n'),
        ('{proxy_name}_shape = (x,y)\n'
        '{proxy_name} = np.PyArray_SimpleNewFromData(2, {proxy_name}_shape, {t.cython_nptypes[0]}, &{var}[0])\n'),
        ('if {cache_name} is None:\n'
         '    {proxy_name}_shape = (x,y)\n'
         '    {proxy_name} = np.PyArray_SimpleNewFromData(2, {proxy_name}_shape, {t.cython_nptypes[0]}, &{var}[0])\n'
         '    {cache_name} = {proxy_name}\n'
        )
       )

py2c=(
      ('# {var} is a {t.type}\n'
       'cdef int i{var}\n'
       'cdef int {var}_size\n'
       'cdef {t.cython_npctypes[0]} * {var}_data\n'
       '{var}_size = len({var})\n'
       'if isinstance({var}, np.ndarray) and (<np.ndarray> {var}).descr.type_num == {t.cython_nptype}:\n'
       '    {var}_data = <{t.cython_npctypes[0]} *> np.PyArray_DATA(<np.ndarray> {var})\n'
       '    {proxy_name} = {t.cython_ctype}(<size_t> {var}_size)\n'
       '    for i{var} in range({var}_size):\n'
       '        {proxy_name}[i{var}] = {var}_data[i{var}]\n'
       'else:\n'
       '    {proxy_name} = {t.cython_ctype}(<size_t> {var}_size)\n'
       '    for i{var} in range({var}_size):\n'
       '        {proxy_name}[i{var}] = <{t.cython_npctypes[0]}> {var}[i{var}]\n'
       ),
      ('{proxy_name}')
     )

# register_class(name=None, template_args=None, cython_c_type=None, cython_cimport=None, cython_cy_type=None, cython_py_type=None, cython_template_class_name=None, cython_template_function_name=None, cython_cyimport=None, cython_pyimport=None, cython_c2py=None, cython_py2c=None, cpp_type=None, human_name=None, from_pytype=None)[source]¶
ts.register_class('Matrix', template_args=('t', 'x', 'y'),
                  cython_c_type='class',  cython_cimport=('Eigen/Dense'),
                  cython_cy_type='class', cython_py_type='numpy.array',
                  cython_template_class_name=None, cython_template_function_name=None,
                  cython_cyimport='matrix', cython_pyimport='numpy', cython_c2py=c2py,
                  cython_py2c=py2c, cpp_type='Eigen::Matrix')

classes = [
     apiname('EigenTest', **_incore)
    ]

#del ts
