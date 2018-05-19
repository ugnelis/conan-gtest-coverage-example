cmake_minimum_required(VERSION 2.8)

project(app CXX)

# Initialize Conan.io.
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Add executable.
add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

# Link libraries.
target_link_libraries(
        ${PROJECT_NAME}
        hello-world
)

# Install files.
install(FILES README.md
        DESTINATION .
        )
