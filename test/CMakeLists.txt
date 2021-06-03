enable_testing()

file(GLOB_RECURSE XML_MODELS *.xml)

set(LIST_TESTS "")
foreach(_xml ${XML_MODELS})
    message(STATUS " [test]Adding test for ${_xml}")
    get_filename_component(_test_name ${_xml} NAME_WE)
    add_test(NAME test_${_test_name}
        COMMAND ${Python3_EXECUTABLE} -m nfsim -xml ${_xml}
        )
    list(APPEND LIST_TESTS test_${_test_name})
endforeach()

set_tests_properties(${LIST_TESTS} PROPERTIES ENVIRONMENT PYTHONPATH=${CMAKE_BINARY_DIR}/py)
