#include<bits/stdc++.h>
#include <iostream>
using namespace std;
// unordered_map<char,int> symbols = {
//         {"[",-1}, 
//         {"(",-2}, 
//         {"{",-3}, 
//         {"]", 1}, 
//         {")", 2}, 
//         {"}", 3}
//     };


bool isBalance(string s) {
    stack<char> st;
    std::unordered_map<std::string, int> symbol(
    {
    {"[",-1}, 
        {"(",-2}, 
        {"{",-3}, 
        {"]", 1}, 
        {")", 2}, 
        {"}", 3} });

    for(char c:s) {
        if (symbol[c] < 0) {
            st.push(c);
        } else {
            if (st.empty()) return false;
            char top = st.top();
            st.pop();
            if(symbol[top] + symbol[c]) return false;
        }
    }
    if (st.empty()) return true;
    return false;
}

int main() {
    string brak = "{[(())]}()";
    bool res = isBalance(brak);
    cout << res;
}