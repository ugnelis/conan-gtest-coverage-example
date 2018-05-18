#include <iostream>
#include "helloworld/helloboi.h"

int main(int argc, char *argv[])
{
    HelloWorld::HelloBoi helloBoi;
    std::cout << helloBoi.getGreeting("Ugnius") << std::endl;
    return 0;
}
