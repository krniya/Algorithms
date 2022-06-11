#include<bits/stdc++.h>
using namespace std;

bool strongPasswordCheckerII(string p) {
        if(p.size() < 8) return false;
        bool low = false , upper = false ,digit = false ,special = false;
        for(auto c : p){
            if(c>='a' and c<='z') low = true;
            else if(c>='A' and c <='Z') upper = true;
            else if(isdigit(c)) digit = true;
            else special = true;
        }
        //Check the 6th condition
        for(int i=0;i+1<p.size();i++) if(p[i] == p[i+1]) return false;
        if(low and upper and digit and special) return true;
        return false;
    }

int main() {
    cout<<strongPasswordCheckerII("NiYa@1233");
}