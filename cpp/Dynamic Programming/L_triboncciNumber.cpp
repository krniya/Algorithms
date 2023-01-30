#include<bits/stdc++.h>
using namespace std;

int tribonacci(int n) {
        if(!n) return 0;
        int first = 0, second = 1, third = 1, temp;
        for(int i=0; i<n-2; i++) {
            temp = first + second + third;
            first = second;
            second = third;
            third = temp;
        }
        return third;
    }