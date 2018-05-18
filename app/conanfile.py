from conans import ConanFile, tools, CMake


class AppConan(ConanFile):
    name = "app"
    version = "0.0.1"
    description = "Binary example."
    url = "https://github.com/ugnelis/conan-gtest-coverage-example"
    author = "Ugnius Malukas"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"

    def requirements(self):
        self.requires("hello-world/0.0.1@%s/%s" % ("ugnelis", "stable"))

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def imports(self):
        self.copy("*.so", "bin", "lib")
        self.copy("*.dll", "bin", "bin")
        self.copy("*.dylib", "bin", "lib")
