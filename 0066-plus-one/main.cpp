#include <bits/stdc++.h>
#include "/home/ealjkl/competitive-programming/utils/cpp/print.cpp"

using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        vector<int> ans(n);
        int tot = 1 + digits[n - 1];
        int d = tot % 10;
        int carry = tot/10;
        ans[n - 1] = d;
        for (int i = n - 2; i >= 0; i--) {
            int tot = digits[i] + carry;
            int d = tot % 10;
            carry = tot/10;
            ans[i] = d;
        }
        if (carry) {
            ans.insert(ans.begin(), 1);
        }
        return ans;
    }
};

int main() {
    // vector<int> digits = {1,2,3};
    vector<int> digits = {9,9,9};
    Solution sol;
    println(sol.plusOne(digits));
}