# python binding.

# location of generated cmake modules
list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})

find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

pybind11_add_module(nfsim MODULE module.cpp ${CMAKE_CURRENT_SOURCE_DIR}/../NFsim.cpp)
target_compile_options(nfsim PUBLIC -DBUILD_PYTHON_MODULE)

target_link_libraries(nfsim PRIVATE pybind11::pybind11)
