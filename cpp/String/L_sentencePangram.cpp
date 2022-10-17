#include<bits/stdc++.h>
using namespace std;

bool checkIfPangram(string sentence) {
    unordered_set<char> checked;
    for(char ch: sentence) {
        checked.insert(ch);
    }
    return checked.size() == 26;
}

bool checkIfPangram(string sentence) {
    
    vector<int> freq(26);                      //create a frequency vector 
    
    for(auto ch:sentence) freq[ch-'a']++;      //update count of each character
    
    for(auto it:freq){                         //traverse freq vector
        if(it==0) return false;                //if any aplhabet's occurence is 0
    }                                          //return false;
    return true;
}