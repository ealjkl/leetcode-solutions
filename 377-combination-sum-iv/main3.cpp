#include <bits/stdc++.h>
#include "/home/ealjkl/competitive-programming/utils/cpp/print.cpp"

using namespace std;

vector<int> cache(1001);

int cachedFunc(vector<int> &nums, int target, vector<int> &cache) {
    int ans = 0;
    if (target < 0) {
        return 0;
    }
    if (target == 0) {
        return 1;
    }
    auto cached = cache[target];
    if (cached > -1) {
        return cache[target];
    }

    for (auto num: nums) {
        int combinations = cachedFunc(nums, target - num, cache);
        ans += combinations;
    }
    cache[target] = ans;
    return ans;
}

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        fill(cache.begin(), cache.end(), -1);
        return cachedFunc(nums, target, cache);
    }
};

int main() {
    Solution sol {};
    // vector<int> x = {1, 2, 3};
    vector<int> y = {3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25};
    // cout << sol.combinationSum4(x, 4) << endl;
    cout << sol.combinationSum4(y, 10) << endl;
}