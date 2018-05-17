#ifndef CONAN_GTEST_COVERAGE_EXAMPLE_HELLOBOI_H
#define CONAN_GTEST_COVERAGE_EXAMPLE_HELLOBOI_H

#include <iostream>

namespace HelloWorld {
    /**
     * Hello Boi class.
     */
    class HelloBoi {
    public:
        /**
         * Constructor.
         */
        HelloBoi();

        /**
         * Get greeting for our boi.
         * @param name Name of the boi.
         * @return greeting.
         */
        std::string getGreeting(const std::string &name);
    };
}

#endif //CONAN_GTEST_COVERAGE_EXAMPLE_HELLOBOI_H
