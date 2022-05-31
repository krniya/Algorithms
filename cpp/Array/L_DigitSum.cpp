#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int dSum = 0;
    while (n > 0) {
        int digit = n % 10;
        dSum += digit;
        n = n/10;
    }
    cout<<dSum;
}