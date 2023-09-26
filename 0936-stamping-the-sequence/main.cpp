#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> movesToStamp(string stamp, string target) {
        vector <int> ans;
        for (int i = 0; i < target.length() - stamp.length() + 1; i++) {
            string so = target.substr(i, stamp.length());
        }
        return ans;
    }
};

int main() {
    Solution sol;
    sol.movesToStamp("abca", "aabcaca");
}