#include<bits/stdc++.h>
using namespace std;

int alternateDigitSum(int n) {
    string s = to_string(n); //creatig string of n
    int sum=0, fl=1;
    for(int i=0; i<s.size(); i++) //Add and substract values alternately
    {
        if(fl)  sum += s[i]-'0'; 
        else sum -= s[i]-'0';
        fl = 1 -fl;
    }
    return sum;
}