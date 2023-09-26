#include <bits/stdc++.h>
#include "/home/ealjkl/competitive-programming/utils/cpp/print.cpp"

using namespace std;

map<int, int> cache;

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        int ans = 0;
        if (target < 0) {
            return 0;
        }
        if (target == 0) {
            return 1;
        }

        for (auto num: nums) {
            int combinations = combinationSum4(nums, target - num);
            ans += combinations;
        }
        return ans;
    }
};

int main() {
    Solution sol {};
    // vector<int> x = {1, 2, 3};
    vector<int> y = {3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25};
    // cout << sol.combinationSum4(x, 4) << endl;
    cout << sol.combinationSum4(y, 10) << endl;
}