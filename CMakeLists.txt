cmake_minimum_required(VERSION 3.14 FATAL_ERROR)
project(NFsim LANGUAGES CXX C)

#find_package(XMLRPC REQUIRED abyss-server c++2)

#if (NOT XMLRPC_FOUND)
#  message (FATAL_ERROR "XMLRPC-C not found")
#endif (NOT XMLRPC_FOUND)

set(NFSIM_VERSION 1.13)

set(CMAKE_CXX_STANDARD 14)
add_definitions(-DNFSIM_VERSION=${NFSIM_VERSION})

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()


option(ENABLE_PYTHON "Enable python module" ON)

find_package(Python3 COMPONENTS Interpreter REQUIRED)
find_program(CONAN conan HINTS $ENV{HOME}/.local/bin)
if(NOT CONAN)
    message(STATUS "Installing conan using python3-pip")
    execute_process(COMMAND ${Python3_EXECUTABLE} -m pip install conan)
endif()
include(${CMAKE_SOURCE_DIR}/cmake/conan.cmake)

# location of generated cmake modules
list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})

#
# Install using conan
#
conan_cmake_configure(REQUIRES
        pybind11/2.6.1
        muparser/2.3.2
    GENERATORS cmake_find_package
    OPTIONS ${CONAN_OPTIONS})

conan_cmake_autodetect(settings)
conan_cmake_install(PATH_OR_REFERENCE .
    BUILD missing
    REMOTE conan-center
    SETTINGS ${settings})

find_package(muparser REQUIRED)
include_directories(${muparser_INCLUDE_DIRS})

include(CheckCCompilerFlag)
include(CheckCXXCompilerFlag)

add_definitions(-Wall)

add_subdirectory(src/nauty24)
add_subdirectory(src/NFutil)
add_subdirectory(src/NFscheduler)
add_subdirectory(src/NFreactions)
add_subdirectory(src/NFoutput)
add_subdirectory(src/NFinput)
add_subdirectory(src/NFfunction)
add_subdirectory(src/NFcore)
add_subdirectory(src/NFtest)

add_library(NFsim STATIC
    $<TARGET_OBJECTS:nauty24>
    $<TARGET_OBJECTS:NFutil>
    $<TARGET_OBJECTS:NFscheduler>
    $<TARGET_OBJECTS:NFreactions>
    $<TARGET_OBJECTS:NFoutput>
    $<TARGET_OBJECTS:NFinput>
    $<TARGET_OBJECTS:NFfunction>
    $<TARGET_OBJECTS:NFcore>
    $<TARGET_OBJECTS:NFtest>)


target_link_libraries(NFsim PUBLIC muparser::muparser)

add_executable(NFsim-exe ${CMAKE_SOURCE_DIR}/src/NFsim.cpp)
target_link_libraries(NFsim-exe PRIVATE NFsim)
set_target_properties(NFsim-exe PROPERTIES OUTPUT_NAME NFsim)

#
# Python extension
#
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/src/python)

enable_testing()
