#include<bits/stdc++.h>
using namespace std;
static bool desc(vector<int>& a, vector<int>& b){
    return a[1] > b[1];
}
int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
    int res = 0;
    sort(boxTypes.begin(), boxTypes.end(), desc);
    for(int i=0;i<boxTypes.size();i++) {
        if (boxTypes[i][0] > truckSize) {
            res += truckSize * boxTypes[i][1];
            return res;
        }
        truckSize -= boxTypes[i][0];
        res += boxTypes[i][0] * boxTypes[i][1];
    }
    return res;
}
int main() {

}