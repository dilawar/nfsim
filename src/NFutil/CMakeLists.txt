file(GLOB_RECURSE SRCS *.cpp)
add_library(NFutil OBJECT ${SRCS})
set_target_properties(NFutil PROPERTIES POSITION_INDEPENDENT_CODE ON)
