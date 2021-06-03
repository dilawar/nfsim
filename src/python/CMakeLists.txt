# python binding.

# location of generated cmake modules
list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})

find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

set(PY_OUTPUT_DIR ${CMAKE_BINARY_DIR}/py)

pybind11_add_module(_nfsim MODULE module.cpp ${CMAKE_CURRENT_SOURCE_DIR}/../NFsim.cpp)

# Copy generated python module
file(MAKE_DIRECTORY ${PY_OUTPUT_DIR}/nfsim)
add_custom_target(copy_py_tree ALL
    DEPENDS _nfsim
    COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_CURRENT_SOURCE_DIR}/nfsim
    ${PY_OUTPUT_DIR}/nfsim/
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:_nfsim> ${PY_OUTPUT_DIR}/nfsim/
    COMMENT "Copying Python module and source tree to ${PY_OUTPUT_DIR}"
    VERBATIM)

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/setup.py.in
    ${PY_OUTPUT_DIR}/setup.py)

target_compile_options(_nfsim PUBLIC
    -DBUILD_PYTHON_MODULE
    -DNFSIM_VERSION="${NFSIM_VERSION}")

target_link_libraries(_nfsim PRIVATE NFsim pybind11::pybind11)

enable_testing()
add_test(NAME pytest COMMAND ${Python3_EXECUTABLE} -m pytest
    ${CMAKE_SOURCE_DIR}/test/python)

set_tests_properties(pytest PROPERTIES
    ENVIRONMENT PYTHONPATH=${CMAKE_CURRENT_SOURCE_DIR})
