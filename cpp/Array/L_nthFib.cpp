#include<bits/stdc++.h>
using namespace std;

int fib(int n) {
    vector<int> fib = {1,1};
    int nextFib;
    if (n==0) return 0;
    if (n<=2) return fib[1];
    for (int i=3;i<=n;i++) {
        nextFib = fib[0] + fib[1];
        fib[0] = fib[1];
        fib[1] = nextFib;
    }
    return fib[1];
}

int main() {

}