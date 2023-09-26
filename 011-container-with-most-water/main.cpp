#include <bits/stdc++.h>
#include "/home/ealjkl/competitive-programming/utils/cpp/print.cpp"
using namespace std;

class Solution {
public:
    int maxArea(vector<int> &height) {
        int n = height.size();
        int max_l = 0;
        for (int i = 0; i < n; i++) {
            int cand = (n - i - 1)*height[i];
            max_l = max(cand, max_l);
        }

        return max_l;
    }
};

int main() {
    Solution sol {}; 

    vector<int> x = {1,8,6,2,5,4,8,3,7};
    println(sol.maxArea(x));
}