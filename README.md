# conan-gtest-coverage-example
Conan.io package GTest with coverage implementation.

## Projects
This `conan-gtest-coverage-example` consists of two Conan.io sub-projects:
* [hello-world](helloworld) - is a library which has GTests.
* [app](app) - is binary which uses `hello-world` library.

## Usage
First of all, `hello-world` needs to be compiled:
```bash
$ cd helloworld
$ conan create . ugnelis/stable
```

Then `app` binary can be built:
```bash
$ cd app
$ conan create . ugnelis/stable
```
