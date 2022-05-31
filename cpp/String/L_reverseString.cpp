#include <bits/stdc++.h>
using namespace std;


int main() {
    string str, revStr;
    cin >> str;
    for (int i = str.size() - 1; i >=0; i--) {
        revStr.push_back(str[i]);
    }
    cout << revStr;
}