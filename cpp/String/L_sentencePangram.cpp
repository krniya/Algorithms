#include<bits/stdc++.h>
using namespace std;

bool checkIfPangram(string sentence) {
    unordered_set<char> checked;
    for(char ch: sentence) {
        checked.insert(ch);
    }
    return checked.size() == 26;
}