# python binding.

# location of generated cmake modules
list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})

find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

pybind11_add_module(nfsim MODULE module.cpp)
target_link_libraries(nfsim PRIVATE pybind11::pybind11)
