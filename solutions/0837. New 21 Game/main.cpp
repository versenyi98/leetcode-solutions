#include <iostream>

#include "../solution.hpp"

int main() {
    Solution solution;

    std::cout << solution.new21Game(10, 1, 10) << std::endl;
    std::cout << solution.new21Game(6, 1, 10) << std::endl;
    std::cout << solution.new21Game(21, 17, 10) << std::endl;

    return 0;
}