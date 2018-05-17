#include <gtest/gtest.h>
#include "helloworld/helloboi.h"

using namespace HelloWorld;

TEST(HelloBoiTest, getGreeting_GetGreeting_True)
{
    HelloBoi helloBoi;
    ASSERT_EQ("Welcome, Ugnius!", helloBoi.getGreeting("Ugnius"));
}
