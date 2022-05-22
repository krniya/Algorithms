const int lim = 1e5 + 5;
long long pSum[lim], sSum[lim];
int arr[lim], pMin[lim], sMin[lim];
const int mod = 1e9 + 7;


long long helper(int left, int right){
    if(left == right) return ((long long)arr[left]*arr[left])%mod;
    int mid = (left + right)/2;
    for (int i = mid; i >= left; i--)
    {
        sMin[i] = arr[i];
        sSum[i] = arr[i];
        if (i + 1 <= mid)
        {
            sMin[i] = min(sMin[i + 1], arr[i]);
            sSum[i] = (sSum[i + 1] + arr[i])%mod;
        }
    }
    for (int i = mid + 1; i <= right; i++)
    {
        pMin[i] = arr[i];
        pSum[i] = arr[i];
        if (i - 1 > mid)
        {
            pMin[i] = min(pMin[i - 1], arr[i]);
            pSum[i] = (pSum[i - 1] + arr[i])%mod;
        }
    }
    long long ans = 0, sLeft = 0, sRight = 0;
    for (int i = mid, j2 = mid; i >= left; i--)
    {
        sLeft = sSum[i];
        while (j2 + 1 <= right && pMin[j2 + 1] > sMin[i]){
            j2++;
            sRight = (sRight + pSum[j2])%mod;
        }
        long long s = sRight;
        s = (s + ((j2-mid)*sLeft)%mod)%mod;
        s = (s*sMin[i])%mod;
        ans = (ans + s)%mod;
    }
    sLeft = 0, sRight = 0;
    for(int i=mid+1,j2=mid+1;i<=right;i++){
        sRight = pSum[i];
        while(j2-1>=left && sMin[j2-1] >= pMin[i]){
            j2--;
            sLeft = (sLeft + sSum[j2]);
        }
        long long s = sLeft;
        s = (s + ((mid+1-j2)*sRight)%mod)%mod;
        s = (s*pMin[i])%mod;
        ans = (ans + s)%mod;
    }
    ans = (ans + helper(left,mid))%mod;
    ans = (ans + helper(mid+1,right))%mod;
    return ans;
}

class Solution {
public:
    int totalStrength(vector<int>& s) {
        int n = (int)s.size();
        for(int i=0;i<n;i++) arr[i] = s[i];
        long long ans = helper(0,n-1);
        return (int)ans;
    }
};