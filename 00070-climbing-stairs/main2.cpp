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

template<int stage>
struct Fib
{
  //Make this value a constant value equal to the (stage-1) + (stage -2)
  //which the compile will generate for us and save in the types of:
  // Fib<stage-1> and Fib<stage-2>. This all works because stage is known at compile 
  // time, as all template parameters must be.
  static const uint64_t value = Fib<stage-1>::value + Fib<stage-2>::value;

  static inline uint64_t getValue(int i)
  {
    if (i == stage) // Does the current class hold the given place?
    {
      return value;  // Return it!
    } else {
      return Fib<stage-1>::getValue(i); // Get it from the previous class!
    }
  }
};

template<> // Template specialization for the 0's case.
struct Fib<0>
{
  static const uint64_t value = 1;

  static inline uint64_t getValue(int i)
  {
    assert(i == 0);
    return 1;
  }
};

template<> // Template specialization for the 1's case
struct Fib<1>
{
  static const uint64_t value = 1;

  static inline uint64_t getValue(int i)
  {
    if (i == 1)
    {
      return value;
    } else {
      return Fib<0>::getValue(i);
    }
  }
};

class Solution {
public:
    int climbStairs(int n) {
        return Fib<46>::getValue(n);
    }
};

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    Solution sol;
    auto ans = sol.climbStairs(11);
    cout << ans << endl;
}