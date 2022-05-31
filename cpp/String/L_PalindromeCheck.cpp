#include <bits/stdc++.h>
using namespace std;

bool palCheck1(string str) {
    string revStr;
    for (int i = str.size() - 1; i >=0; i--) {
        revStr.push_back(str[i]);
    }
    if (str == revStr) {
        return true;
    } else {
        return false;
    }
}

bool palCheck2(string str) {
    int i = 0;
    int j = str.size() - 1;
    while (i<j) {
        if (str[i] != str[j]) {
            return false;
        }
        i+=1;
        j-=1;
    }
    return true;
}

int main() {
    string str;
    cin >> str;
    if(palCheck1(str)) {
        cout<<"Yes";
    }
    else {
        cout<<"No";
    }
}


