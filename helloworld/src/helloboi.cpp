#include "helloworld/helloboi.h"

using namespace HelloWorld;

HelloBoi::HelloBoi() {
}

std::string HelloBoi::getGreeting(const std::string &name) {
    return "Welcome, " + name + "!";
}
