#include<bits/stdc++.h>
#include "/home/ealjkl/competitive-programming/utils/cpp/print.cpp"

using namespace std;


//initially remainingOpen = n
vector<string> solve(int remainingOpen, int toClose) {
    vector<string> ans;
    if (remainingOpen == 0) {
        string tail = "";
        for (int i = 0; i < toClose; i++) {
            tail += ')';
        }
        return {tail};
    }
    if (remainingOpen > 0) {
        // chose '('
        for (auto option:solve(remainingOpen - 1, toClose + 1)) {
            ans.push_back('(' + option);
        }
    }
    if (toClose > 0) {
        //chose ')'
        for (auto option: solve(remainingOpen, toClose - 1)) {
            ans.push_back(')' + option);
        }
    }
    return ans;
}

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans = solve(n, 0);
        return ans;
    }
};

int main() {
    Solution sol {};
    for (auto opt: sol.generateParenthesis(3)) {
        cout << "\"" << opt << "\"" << endl;
    }
}