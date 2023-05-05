#include<bits/stdc++.h>
using namespace std;

int maxVowels(string s, int k) {
        int count=0,ctemp=0;  //count the vowels
        for(int i=0;i<s.length();i++){
            if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u')
                ctemp++;
            if(i-k>=0)
                if(s[i-k]=='a' || s[i-k]=='e' || s[i-k]=='i' || s[i-k]=='o' || s[i-k]=='u')
                        ctemp--;            
            if(ctemp>count)
                count=ctemp;
        }
        return count;
    }