#include <bits/stdc++.h>

using namespace std;

// class Solution {
// public:
//     int searchInsert(vector<int>& nums, int target) {
//         int n = nums.size();
//         int L = 0, R = n - 1; 
//         int M;
//         while(L <= R) {
//             M = L + (R - L)/2;
//             cout << "M: " << M << endl;
//             if (nums[M] == target) {
//                 return M;
//             } else if (nums[M] < target) {
//                 L = M + 1;
//             } else {
//                 R = M - 1;
//             }
//         }
//         M = L + (R - L)/2;
//         return M;
//     }
// };

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        auto p = lower_bound(nums.begin(), nums.end(), target);
        auto idx = p - nums.begin();
        return idx;
    }
};


int main() {
    Solution sol;

    vector<int> nums = {1, 3, 5, 6};
    cout <<  sol.searchInsert(nums, 0) << endl;
    cout <<  sol.searchInsert(nums, 5) << endl;
    cout <<  sol.searchInsert(nums, 2) << endl;
    cout <<  sol.searchInsert(nums, 7) << endl;
}