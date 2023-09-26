#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        int y = abs(x);
        int sign = signbit(x);
        int ans = 0;
        while (y > 0) {
            //TODO: this made sense, but not reaaaaally sure it is the correct condition, though it passed the tests
            if ((INT_MAX - (y % 10))/10.0 <= ans) {
                return 0;
            }
            ans = 10*ans + (y % 10);
            y /= 10;
        }
        if (ans < 0) {
            return 0;
        }
        return ((sign == 0) ? ans: -ans);
    }
};

int main() {
    int x = 123;
    Solution sol {};
    cout << sol.reverse(1463847412) << endl;
    // cout << sol.reverse(-123) << endl;
    // cout << sol.reverse(120) << endl;
    
    // int z = 964632435;
    // z += z*10;
    // cout << "z: " << z << endl;
}