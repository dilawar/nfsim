file(GLOB_RECURSE SRCS *.cpp)
add_library(NFtest OBJECT ${SRCS})
set_target_properties(NFtest PROPERTIES POSITION_INDEPENDENT_CODE ON)
