#include "parking_system.hpp"

#include <bits/stdc++.h>

ParkingSystem::ParkingSystem(int b, int m, int s) : slots{b, m, s} {}

bool ParkingSystem::addCar(int type) {
    type--;
    return (slots[type] = std::max(-1, --slots[type])) >= 0;
}