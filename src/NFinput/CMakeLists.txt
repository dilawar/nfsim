file(GLOB_RECURSE SRCS *.cpp)
add_library(NFinput OBJECT ${SRCS})
set_target_properties(NFinput PROPERTIES POSITION_INDEPENDENT_CODE ON)
