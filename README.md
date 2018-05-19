# conan-gtest-coverage-example [![Build Status](https://travis-ci.org/ugnelis/conan-gtest-coverage-example.svg?branch=master)](https://travis-ci.org/ugnelis/conan-gtest-coverage-example) [![Coverage Status](https://coveralls.io/repos/github/ugnelis/conan-gtest-coverage-example/badge.svg?branch=master)](https://coveralls.io/github/ugnelis/conan-gtest-coverage-example?branch=master)
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
