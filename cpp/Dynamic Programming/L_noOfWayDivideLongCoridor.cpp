#include <bits/stdc++.h>
using namespace std;

int numberOfWays(string corridor)
{
    const int mod = 1000000007; // Define the modulo value for the final result
    long res = 1;               // Initialize the result variable to 1 (will be updated during iteration)
    int prevSeat = 0;           // Initialize the variable to track the index of the previous seat
    int numSeats = 0;           // Initialize the variable to count the number of seats encountered

    for (int i = 0; i < corridor.length(); i++)
    {
        char c = corridor[i];
        if (c == 'S')
        {
            numSeats += 1; // Increment the seat count when 'S' is encountered
            // Check if there are more than 2 consecutive seats and an odd number of seats
            if (numSeats > 2 && numSeats % 2 == 1)
            {
                // Update the answer using the distance between the current seat and the previous seat
                res = res * (i - prevSeat) % mod;
            }
            prevSeat = i; // Update the previous seat index to the current index
        }
    }

    // Return the answer only if there are more than 1 seat and an even number of seats
    return numSeats > 1 && numSeats % 2 == 0 ? res : 0;
}