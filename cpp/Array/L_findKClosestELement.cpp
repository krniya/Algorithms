#include<bits/stdc++.h>
using namespace std;

vector<int> findClosestElements(vector<int>& a, int k, int x) {
    int num=INT_MAX;
    int mark=0;
    for(int i=0;i<a.size();i++){
        if(num>abs(x-a[i])){
            num=abs(x-a[i]);
            mark=i;
        }
    }
    vector<int>ans;
    ans.push_back(a[mark]);
    int i=mark+1;
    int j=mark-1;
    while(ans.size()<k){
        if(i>=a.size())
            ans.push_back(a[j--]);
        else if(j<0)
            ans.push_back(a[i++]);
        else if(abs(x-a[j])<=abs(x-a[i]))
            ans.push_back(a[j--]);
        else
            ans.push_back(a[i++]);
    }
    sort(ans.begin(),ans.end());
    return ans;
}