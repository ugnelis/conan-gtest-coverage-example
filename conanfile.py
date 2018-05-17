import os
from conans import ConanFile, tools, CMake


class ConanGTestCoverageExampleConan(ConanFile):
    name = "conan-gtest-coverage-example"
    version = "0.0.1"
    url = "https://github.com/ugnelis/conan-gtest-coverage-example"
    author = "Ugnius Malukas"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    description = "Conan GTest coverage example."
    exports_sources = "*"

    def build_requirements(self):
        self.build_requires("gtest/1.8.0@%s/%s" % ("bincrafters", "stable"))

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()
        cmake.test()

    def package_info(self):
        self.env_info.CONAN_GTEST_COVERAGE_EXAMPLE_DIR = os.path.join(self.package_folder, 'setup')
