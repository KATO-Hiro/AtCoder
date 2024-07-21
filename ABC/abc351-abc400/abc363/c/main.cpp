#include <iostream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    string s;
    cin >> s;

    vector<char> s_vec(s.begin(), s.end());
    set<string> patterns;
    set<string> met;

    sort(s_vec.begin(), s_vec.end());

    do {
        string pattern(s_vec.begin(), s_vec.end());
        patterns.insert(pattern);
    } while (next_permutation(s_vec.begin(), s_vec.end()));

    for (const auto& pattern : patterns) {
        bool ok = false;

        for (int i = 0; i < n; ++i) {
            int j = i + k;

            if (j > n) break;

            string t = pattern.substr(i, k);
            string t_rev = t;
            reverse(t_rev.begin(), t_rev.end());

            if (t == t_rev) {
                ok = true;
                break;
            }
        }

        if (ok) {
            met.insert(pattern);
        }
    }

    cout << patterns.size() - met.size() << endl;

    return 0;
}