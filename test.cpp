class solution { public: int minimumAverageDifference(vector int>& nums) {
if (nums.Size ==1 return nums[ed int n=nums.size(); long long sum=e; for(auto u:nums)
Sum+=u;
vector int> v(n); long long k=0;
for(int i=0;i<n;i++) {
k+=nums[i]; long long rt=sum-k; long long lt=k/(i+1); long long rta; if((n-1-i)==0)
rtare; else rta=rt/(n-1-1);
v[i]=abs(lt-rta);
int mi-INT MAX,id=INT MAX; for(int i=0;i<n;i++){ i (v[i]cmi){
mi=v[i]; id=i;
return id;