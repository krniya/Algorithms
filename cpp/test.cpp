class Solution {
public:
    // splitong the words
    int divider(string &str){
        int noOfWord = 1;
        for(char ch: str){
            noOfWord += ch == ' ';
        }
        return noOfWord;
    }
    
    string largestWordCount(vector<string>& messages, vector<string>& senders) {
        map<string,int> hm;
        int n;
        n = messages.size();
        for(int i=0;i<n;i++){
            hm[senders[i]] += divider(messages[i]);
        }
        string res;
        int count = 0;
        for(auto [key, val]: hm){
            if(val >= count){
                count = val;
                res = max(res, key);
            }
        }
        return res;
    }
};