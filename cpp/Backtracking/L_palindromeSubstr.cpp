#include<bits/stdc++.h>
using namespace std;


vector<vector<string>> partition(string s) {
    vector<string> curr;
    vector<vector<string>> result;
    dfs(s, 0, curr, result);
    return result;
}
void dfs(string s, int start, vector<string>& curr, vector<vector<string>>& result) {
    if (start == s.size()) {
        result.push_back(curr);
        return;
    }
    for (int i = start; i < s.size(); i++) {
        if (isPalindrome(s, start, i)) {
            string str = s.substr(start, i - start + 1);
            curr.push_back(str);
            dfs(s, i + 1, curr, result);
            curr.pop_back();
        }
    }
}
bool isPalindrome(string s, int left, int right) {
    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int main() {

}