file(GLOB_RECURSE SRCS *.cpp)
add_library(NFscheduler OBJECT ${SRCS})
set_target_properties(NFscheduler PROPERTIES POSITION_INDEPENDENT_CODE ON)
