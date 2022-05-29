class Solution {
public:
    int rearrangeCharacters(string s, string target) {
        int a = 26;
        vector<int> first(a), last(a);
        for(char c: s) {
            first[c-'a']++;
        }
        for(char c: target) {
            last[c-'a']++;
        }
        int res = (int)1e9;
        for(int i=0;i<a;i++){
            if(last[i] == 0) continue;
            res = min(res, first[i]/last[i]);
        } 
        return res;
    }
};