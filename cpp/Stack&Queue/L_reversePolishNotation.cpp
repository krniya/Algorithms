#include<bits/stdc++.h>
using namespace std;

int evalRPN(vector<string>& tokens) {
        stack<int> stack;
        for(string token:tokens) {
            if(token == "+") {
                int first = stack.top();
                stack.pop();
                int second = stack.top();
                stack.pop();
                stack.push(first + second);
            }
            else if(token == "-") {
                int first = stack.top();
                stack.pop();
                int second = stack.top();
                stack.pop();
                stack.push(second - first);
            }
            else if(token == "*") {
                int first = stack.top();
                stack.pop();
                int second = stack.top();
                stack.pop();
                stack.push(first * second);
            }
            else if(token == "/") {
                int first = stack.top();
                stack.pop();
                int second = stack.top();
                stack.pop();
                stack.push(second / first);
            }
            else {
                stack.push(stoi(token));
            }
        }
        return stack.top();
    }

int main() {

}