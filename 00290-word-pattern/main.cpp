#include <bits/stdc++.h>
#include <string_view>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define fi first
#define se second
#define endl '\n'
#define debug(x) cout << #x << ": " << x << endl
#define REP(i, a, b) for (int i = a; i < b; i++)


void split(string str, char separator, vector<string> &strings) {
    int startIndex = 0, endIndex = 0;
    for (int i = 0; i <= str.size(); i++) {
        // If we reached the end of the word or the end of the input.
        if (str[i] == separator || i == str.size()) {
            endIndex = i;
            string temp;
            temp.append(str, startIndex, endIndex - startIndex);
            strings.push_back(temp);
            startIndex = endIndex + 1;
        }
    }
}

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> m1 = {};
        unordered_map<string, char> m2 = {};
        vector<string> words;
        split(s, ' ',  words);
        if (pattern.length() != words.size()) {
            return false;
        }
        for (int i = 0; i < words.size(); i++) {
            auto word = words[i];
            auto letter = pattern[i];
            if (m1.count(letter) && m1[letter] != word) {
                return false;
            }
            m1[letter] = word;
            if (m2.count(word) && m2[word] != letter) {
                return false;
            }
            m2[word] = letter;
        }
        return true;
    }
};


signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    Solution sol;
    auto ans = sol.wordPattern("a", "a");
    cout << ans << endl;
}