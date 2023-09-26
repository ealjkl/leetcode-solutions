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

auto pow(int x, int n) -> int {
    int ans = 1;
    while (n) {
        if (n & 1) {
            ans *= x;
        }
        x *= x;
        n = n >> 1;
    }
    return ans;
}

auto my_sqrt(int x) -> int {
    if (x == 0) return 0;
    int L = 1, R = x;
    int M, M2;
    while (L <= R) {
        M = L + (R - L)/2;
        if (M > INT_MAX/M) {
            R = M - 1;
            continue;
        }
        M2 = M*M;
        if (M2 == x) {
            return M;
        }
        if (M2> x) {
            R = M - 1;
        } else if (M2 < x) {
            L = M + 1;
        }
    }
    return M2 >= x || M > INT_MAX/M ? M - 1 : M;
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    auto y =  my_sqrt(2147483647);
    cout << "y: " << y << endl;
}