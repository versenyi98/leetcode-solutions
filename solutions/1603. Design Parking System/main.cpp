#include <iostream>

#include "parking_system.hpp"

int main() {
    ParkingSystem parking_system(1, 1, 0);

    std::cout << parking_system.addCar(1) << std::endl;
    std::cout << parking_system.addCar(2) << std::endl;
    std::cout << parking_system.addCar(3) << std::endl;
    std::cout << parking_system.addCar(1) << std::endl;  

    return 0;
}