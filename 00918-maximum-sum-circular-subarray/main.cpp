#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define fi first
#define se second
#define endl '\n'
#define debug(x) cout << #x << ": " << x << endl
#define REP(i, a, b) for (int i = a; i < b; i++)

class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int total_sum = 0;
        int max_sum = INT_MIN;
        int curr_max = INT_MIN;
        int curr_min = INT_MAX;
        int min_sum = INT_MAX;
        for (auto num: nums) {
            //max
            curr_max = max(curr_max, num);
            max_sum = max(max_sum, curr_max);
            //min
            curr_min = min(curr_min, num);
            min_sum = min(min_sum, curr_min);
            total_sum += num;
        }
        return max_sum  > 0 ? max(max_sum, total_sum - min_sum): max_sum;
    }
};

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vi nums = {-3, -2, -3};
    Solution s{};
    auto ans = s.maxSubarraySumCircular(nums);
    cout << "ans " << ans << endl;
}