#include <bits/stdc++.h>
using namespace std;

map<string, int> strFreq(vector<string> strList) {
    map<string,int> hm;
    for (auto it: strList) {
        hm[it]++;
    }
    return hm;
}

int main() {
    vector<string> strList = {"abc","dfs","dsa","fsd","sdf","abc","dsa","abc"};
    map<string, int> freq = strFreq(strList);
    for (auto it: freq) {
        cout<<it.first<<" "<<it.second<<endl;
    }
}
