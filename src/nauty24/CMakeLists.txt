file(GLOB_RECURSE SRCS *.c)
add_library(nauty24 OBJECT ${SRCS})
set_target_properties(nauty24 PROPERTIES POSITION_INDEPENDENT_CODE ON)
