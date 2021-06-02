# python binding.

# location of generated cmake modules
list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})

find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

pybind11_add_module(nfsim MODULE module.cpp ${CMAKE_CURRENT_SOURCE_DIR}/../NFsim.cpp)
target_compile_options(nfsim PUBLIC
    -DBUILD_PYTHON_MODULE
    -DNFSIM_VERSION="${NFSIM_VERSION}")

target_link_libraries(nfsim PRIVATE NFsim pybind11::pybind11)

enable_testing()
add_test(NAME pytest COMMAND ${Python3_EXECUTABLE} -m pytest
    ${CMAKE_SOURCE_DIR}/test/python)

set_tests_properties(pytest PROPERTIES ENVIRONMENT PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR})
