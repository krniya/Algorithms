#include <bits/stdc++.h>
using namespace std;

class ParkingSystem
{
public:
    vector<int> slot;
    ParkingSystem(int big, int medium, int small)
    {
        slot = {big, medium, small};
    }

    bool addCar(int carType)
    {
        if (slot[carType - 1])
        {
            slot[carType - 1]--;
            return true;
        }
        return false;
    }
};

/**
 * @brief
 *
 */

int main()
{
    ParkingSystem *obj = new ParkingSystem(1, 1, 0);
    for (auto a : obj->slot)
    {
        cout << a;
    }
    cout << "\n";
    bool param_1 = obj->addCar(1);
    cout << param_1 << "\n";
    for (auto a : obj->slot)
    {
        cout << a;
    }
    cout << "\n";
    bool param_2 = obj->addCar(2);
    cout << param_2 << "\n";
    for (auto a : obj->slot)
    {
        cout << a;
    }
    cout << "\n";
    bool param_3 = obj->addCar(3);
    cout << param_3 << "\n";
    for (auto a : obj->slot)
    {
        cout << a;
    }
    cout << "\n";
    bool param_4 = obj->addCar(1);
    cout << param_4 << "\n";
    for (auto a : obj->slot)
    {
        cout << a;
    }
}