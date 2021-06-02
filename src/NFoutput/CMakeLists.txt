file(GLOB_RECURSE SRCS *.cpp)
add_library(NFoutput OBJECT ${SRCS})
set_target_properties(NFoutput PROPERTIES POSITION_INDEPENDENT_CODE ON)
