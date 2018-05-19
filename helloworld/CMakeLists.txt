cmake_minimum_required(VERSION 2.8)

project(hello-world CXX)

# Initialize Conan.io.
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Setup testing.
enable_testing()

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
