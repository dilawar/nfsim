file(GLOB_RECURSE SRCS *.cpp)
add_library(NFfunction OBJECT ${SRCS})
set_target_properties(NFfunction PROPERTIES POSITION_INDEPENDENT_CODE ON)
