#ifndef HELLO_WORLD_HELLOBOI_H
#define HELLO_WORLD_HELLOBOI_H

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

#endif //HELLO_WORLD_HELLOBOI_H
