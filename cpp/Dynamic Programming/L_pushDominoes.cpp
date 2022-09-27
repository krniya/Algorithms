#include<bits/stdc++.h>
using namespace std;

string pushDominoes(string str) {
        int n=str.size();
        vector<int>arr(n);
        string ans=str;
        
        int right_force=0;
        for(int i=0;i<n;i++){
            if(str[i]=='L')
                right_force=0;
            if(str[i]=='R')
                right_force=1;
            if(str[i]=='.' && right_force>0)
                right_force++;
            arr[i]=right_force;
        }
       
        int left_force=0;
        for(int i=n-1;i>=0;i--){
            if(str[i]=='R') left_force=0;
            if(str[i]=='L') left_force=1;
            if(str[i]=='.')
            {
                if(left_force>0)
                    left_force++;
                
                if(arr[i]==0 && left_force>0)
                    ans[i]='L';
                else if(arr[i]>0 && left_force==0)
                    ans[i]='R';
                
                //force from both direction
                else if(arr[i]<left_force)
                    ans[i]='R';
                else if(arr[i]>left_force) 
                    ans[i]='L';
                
                // equilibrium condition arr[i] == left_force 
                else
                    ans[i]='.';  // no change
            }
        }
        return ans;
    }