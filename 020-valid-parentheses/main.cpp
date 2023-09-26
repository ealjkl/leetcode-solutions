#include <bits/stdc++.h>

using namespace std;

char closingBrace(char ch) {
    if (ch == '(') return ')';
    if (ch == '{') return '}';
    if (ch == '[') return ']';
    return 'a';
}

class Solution {
public:
    
    bool isValid(string s) { 
        stack<char> st;
        for (int i = 0; i < s.length(); i++) {
            char ch = s[i];
            if (ch == '(' || ch == '{' || ch == '[') {
                st.push(ch);
            } else {
                if (st.empty()) {
                    return false;
                }

                char popped = st.top();
                st.pop();
                if (closingBrace(popped) !=  ch) {
                    return false;
                }
            }
        }
        return st.empty();
    }
}; 

int main() {
    Solution sol{};
    cout << boolalpha;
    cout << sol.isValid("()[]{}") << endl;
    cout << sol.isValid("(])") << endl;
    cout << sol.isValid("[") << endl;
    cout << sol.isValid("]") << endl;
}