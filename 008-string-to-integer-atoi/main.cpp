#include<bits/stdc++.h>
#include "/home/ealjkl/competitive-programming/utils/cpp/print.cpp"

using namespace std;

bool isNumber(char c) {
    vector<char> numsChars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
    if (count(numsChars.begin(), numsChars.end(), c) > 0) {
        return true;
    } else {
        return false;
    }
}

class Solution {
public:
    int myAtoi(string s) {
        int i;
        int sign = 1;
        for (i = 0; i < s.length(); i++) {
            auto ch = s[i];
            if (ch == ' ') {
                continue;
            } else {
                break;
            }
        }
        if (s[i] == '-') {
            sign = -1;
            i++;
        } else if (s[i] == '+') {
            i++;
        }
        string num_str = "";

        for (; i < s.length(); i++) {
            auto ch = s[i];
            if (!(ch == '0')) {
                break;
            }
        }
        
        for (; i< s.length(); i++) {
            auto ch = s[i];
            if (!isNumber(ch)) {
                break;
            }
            num_str += ch;
        }
        if (num_str.length() == 0) {
            return 0;
        }

        int num = sign*(num_str[num_str.length() - 1] - '0');
        int p = 10;
        for (int j = num_str.length() - 2; j >= 0; j--) {
            char ch = num_str[j];
            int ch_num = ch - '0';
            if (sign == 1) {
                if (ch_num > (INT_MAX - num)/p) {
                    return INT_MAX;
                }
                num += ch_num*p;
                if (j != 0) {
                    if (p > INT_MAX/10) {
                        return INT_MAX;
                    }
                    p *= 10;
                }
            } else {
                // println("num, p, ch_num, INT_MIN             : ", num, p, ch_num, INT_MIN);
                // println("truncated: ch_num, (num - INT_MIN)/p: ", ch_num, (num - INT_MIN)/p);
                // println("real: cn_num, (num - INT_MIN)/p     : ", ch_num, static_cast<double>(num - INT_MIN)/static_cast<double>(p));
                // println();
                if (ch_num > (num - (INT_MIN + 1))/p) {
                    return INT_MIN;
                }
                num -= ch_num*p; 
                if (j != 0) {
                    if (-p < INT_MIN/10) {
                        return INT_MIN;
                    }
                    p *= 10;
                }
            }
            
        }

        return num;
    }
};

int main() {
    Solution sol {};
    // cout << sol.myAtoi("42") << endl;
    // cout << sol.myAtoi("+0042") << endl;
    // cout << sol.myAtoi("-91283472332") << endl;
    // cout << sol.myAtoi("4193 with words") << endl;
    // cout << sol.myAtoi("-2147483649") << endl;
    cout << sol.myAtoi("words and 987") << endl;
    // cout << "-----------------------" << endl;
    // cout << sol.myAtoi("21474836460") << endl;
    // cout << sol.myAtoi("-42") << endl;
    cout << "-----------------------" << endl;
    // println("INT_MIN", INT_MIN);
}