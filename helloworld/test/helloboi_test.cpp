#include <gtest/gtest.h>
#include "helloworld/helloboi.h"

TEST(HelloBoiTest, getGreeting_GetGreeting_True)
{
    HelloWorld::HelloBoi helloBoi;
    ASSERT_EQ("Welcome, Ugnius!", helloBoi.getGreeting("Ugnius"));
}
