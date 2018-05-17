cmake_minimum_required(VERSION 2.8)

project(conan-gtest-coverage-example)

# Initialize Conan.io.
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Setup testing.
include(CTest)
find_package(GTest REQUIRED)

# Add headers.
include_directories("${PROJECT_SOURCE_DIR}/include")

# Add libraries.
add_library(helloworld
        ${PROJECT_SOURCE_DIR}/src/helloboi.cpp
        )

# Install files.
install(
        FILES README.md
        DESTINATION .
)

# Add tests directory.
add_subdirectory(test)
