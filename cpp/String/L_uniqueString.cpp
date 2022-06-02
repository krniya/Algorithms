#include <bits/stdc++.h>
using namespace std;

set<string> uniqueStr(vector<string> strList) {
    set<string> strSet;
    for (auto it: strList) {
        strSet.insert(it);
    }
    return strSet;
}

int main() {
    vector<string> strList = {"abc","dfs","dsa","fsd","sdf","abc","dsa","abc"};
    set<string> strSet = uniqueStr(strList);
    for (auto it: strSet) {
        cout<<it<<endl;
    }
}