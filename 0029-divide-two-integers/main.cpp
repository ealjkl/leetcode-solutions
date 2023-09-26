#include <bits/stdc++.h>

using namespace std;

int lastBit(int n) {
    int ans = 0;
    while(n) {
        n = (n >> 1);
        ans++;
    }
    return ans;
}

class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend < 0) {
            return -divide(-dividend, divisor);
        }
        if (divisor < 0) {
            return -divide(dividend, -divisor);
        }
        if (divisor > dividend) {
            return 0;
        }
        if (divisor == dividend) {
            return 1;
        }
        int noDividendBits = lastBit(dividend);
        int noDivisorBits = lastBit(divisor);
        int q = 0;
        int current = (dividend >> noDividendBits - noDivisorBits);
        while (current) {

        }
        return 1;
    }
};

int main() {
    Solution sol;
    sol.divide(10, 3);
    cout << lastBit(3) << " " << bitset<16>(3) << endl;
    cout << lastBit(7) << " " << bitset<16>(7) << endl;
    cout << lastBit(11) << " " << bitset<16>(11) << endl;
}