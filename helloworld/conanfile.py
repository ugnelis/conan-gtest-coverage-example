import os
from conans import ConanFile, tools, CMake


class HelloWorldConan(ConanFile):
    name = "hello-world"
    version = "0.0.1"
    description = "Library example."
    url = "https://github.com/ugnelis/conan-gtest-coverage-example"
    author = "Ugnius Malukas"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"
    options = {"shared": [True, False], "coverage": [True, False]}
    default_options = "shared=False", "coverage=False"

    def build_requirements(self):
        self.build_requires("gtest/1.8.0@%s/%s" % ("bincrafters", "stable"))

    def build(self):
        cmake = CMake(self)
        # Coverage.
        if self.options.coverage:
            cmake.definitions["COVERAGE"] = "ON"
        cmake.configure()
        cmake.install()
        cmake.test()

    def package(self):
        self.copy("*.h")
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="bin", keep_path=False)
        self.copy("*.dylib", dst="bin", src="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello-world"]
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
        if self.options.shared:
            self.env_info.LD_LIBRARY_PATH.append(os.path.join(self.package_folder, "lib"))
            self.env_info.DYLD_LIBRARY_PATH.append(os.path.join(self.package_folder, "lib"))
