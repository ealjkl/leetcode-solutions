#include <bits/stdc++.h>

using namespace std;

class Compare {
public: 
    bool operator()(pair<int, int> &a, pair<int, int> &b) {
        return a.second < b.second;
    }
};


class Solution {
public:
    int minSetSize(vector<int>& arr) {
        int n = arr.size();
        unordered_map<int, int> counter;
        for (auto el: arr) {
            counter[el]++;
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, Compare> pq;

        for (auto &[key, val]: counter) {
            pq.push({key, val});
        }

        int total = 0;
        int ans = 0;
        while (total < n/2) {
            auto el = pq.top();
            total += el.second;
            ans++;
            pq.pop();
        }

        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> arr = {3,3,3,3,5,5,5,2,2,7};
    cout << sol.minSetSize(arr) << endl;
}