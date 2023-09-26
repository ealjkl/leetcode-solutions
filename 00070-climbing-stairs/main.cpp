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

template <unsigned int N>
struct Fibonacci {
    static constexpr unsigned int value = Fibonacci<N-1>::value + Fibonacci<N-2>::value;
};

template <>
struct Fibonacci<0u> {
    static constexpr unsigned int value = 0;
};

template <>
struct Fibonacci<1u> {
    static constexpr unsigned int value = 1;
};

template <unsigned int N>
constexpr unsigned int fib() {
    return Fibonacci<N>::value;
}

template<unsigned int N>
constexpr std::array<unsigned int, N> dp = []() constexpr {
    std::array<unsigned int, N> a;
    for (unsigned int i = 0; i < N; i++) {
        a[i] = fib<i>();
    }
    return a;
}();

class Solution {
public:
    int climbStairs(int n) {
        return dp<46>[n];
    }
};

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    Solution sol;
    auto ans = sol.climbStairs(11);

}