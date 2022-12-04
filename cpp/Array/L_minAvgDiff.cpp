#include<bits/stdc++.h>
using namespace std;

int minimumAverageDifference(vector <int>& nums){
    int n=nums.size();
    long long sum = 0;
        for (auto i:nums)
            sum+=i;
    vector<int> a(n);
    long long k =0;
    for(int i=0;i<n;i++) {
        k+=nums[i];
        long long r=sum-k;
        long long l=k/(i+1);
        long long rt;
        if((n-1-i)==0)
            rt=0;
        else
            rt=r/(n-1-i);
        a[i]=abs(l-rt);
    }
    int m=INT_MAX,id=INT_MAX;
    for(int i=0;i<n;i++) {
        if(a[i]<m){
            m=a[i];
            id=i;
        }
    }
    return id;
    }