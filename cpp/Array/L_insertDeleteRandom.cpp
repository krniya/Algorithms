#include<bits/stdc++.h>
using namespace std;

class RandomizedSet {
private:
    vector<int> a;
    unordered_map<int,int> m;
    
public:
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if(m.find(val)!=m.end()) 
            return false;
        else {
            a.push_back(val);
            m[val]=a.size()-1;
            return true;
        }
    }
    
    bool remove(int val) {
        if(m.find(val)==m.end())
            return false;
        else {
            int last=a.back();  
            a[m[val]]=a.back();
            a.pop_back();	
            m[last]=m[val];	  
            m.erase(val);	
            return true;
        }
    }
    
    int getRandom() {
        return a[rand()%a.size()];
    }
};