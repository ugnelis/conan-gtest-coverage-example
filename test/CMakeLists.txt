add_executable(unit_tests
        helloboi_test.cpp
        )

target_link_libraries(unit_tests
        helloworld
        GTest::Main
        GTest::GTest
        )

add_test(
        NAME unit_tests
        COMMAND $<TARGET_FILE:unit_tests>
)
