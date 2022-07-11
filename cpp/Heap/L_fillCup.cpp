#include<bits/stdc++.h>
using namespace std;

int fillCups(vector<int>& amount) {
    if(amount[1]+amount[2]+amount[3]==1)return 1;
    if(amount[1]+amount[2]+amount[3]==0)return 0;
    priority_queue<int>pq;
    for(int i=0;i<3;i++)
    {
        pq.push(amount[i]);
    }
    int count=0;
    while(pq.top()!=0)
    {
            int n=pq.top();  pq.pop();  int m=pq.top();
            if(m==0){   
                count+=n;
                break;}
            else{
                pq.pop();
                pq.push(n-1);
                pq.push(m-1);
                }
        count++;
    }
    return count;
}

int main() {

}