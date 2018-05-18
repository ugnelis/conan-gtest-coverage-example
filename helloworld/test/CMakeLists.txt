add_executable(hellow-world-test
        helloboi_test.cpp
        )

target_link_libraries(hellow-world-test
        ${PROJECT_NAME}
        ${CONAN_LIBS}
        )

ADD_TEST(NAME hellow-world-test
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
        COMMAND hellow-world-test
        )