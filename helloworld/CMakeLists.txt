cmake_minimum_required(VERSION 2.8)

project(hello-world CXX)

# Initialize Conan.io.
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Setup testing.
enable_testing()

# Setup coverage.
option(COVERAGE "Generate coverage data" OFF)
if (COVERAGE)
    if(CMAKE_COMPILER_IS_GNUCXX)
        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fprofile-arcs -ftest-coverage")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-arcs -ftest-coverage")
    endif()
endif()

# Add headers.
include_directories("${PROJECT_SOURCE_DIR}/include")

# Add libraries.
add_library(${PROJECT_NAME}
        ${PROJECT_SOURCE_DIR}/src/helloboi.cpp
        )

# Link libraries.
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

# Install files.
install(FILES README.md
        DESTINATION .
        )

install(TARGETS ${PROJECT_NAME}
        DESTINATION lib
        )

# Add tests directory.
add_subdirectory(test)
