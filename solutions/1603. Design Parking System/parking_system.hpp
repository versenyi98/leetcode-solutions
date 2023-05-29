#pragma once

class ParkingSystem {
public:
    ParkingSystem(int big, int medium, int small);
    bool addCar(int carType);

private:
    int slots[3];
};
