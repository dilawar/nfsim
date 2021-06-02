file(GLOB_RECURSE SRCS "*.cpp")
add_library(NFcore OBJECT ${SRCS})
set_target_properties(NFcore PROPERTIES POSITION_INDEPENDENT_CODE ON)
