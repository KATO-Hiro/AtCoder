#include <bits/stdc++.h>
#include <atcoder/segtree>

using namespace std;
using namespace atcoder;

using ll = long long;
const ll INF = 1e18;

// (1st value, 1st count, 2nd value, 2nd count)
struct Node {
    ll first_value;
    ll first_count;
    ll second_value;
    ll second_count;
};

Node op(Node x, Node y) {
    map<ll, ll> value_count;

    // value, countのペアに変換
    value_count[x.first_value] += x.first_count;
    value_count[x.second_value] += x.second_count;
    value_count[y.first_value] += y.first_count;
    value_count[y.second_value] += y.second_count;

    // x, yにおける1st, 2ndのvalueとcountを取得
    vector<pair<ll, ll>> sorted_values(value_count.begin(), value_count.end());
    sort(sorted_values.rbegin(), sorted_values.rend());

    Node result;
    result.first_value = sorted_values[0].first;
    result.first_count = sorted_values[0].second;
    
    if (sorted_values.size() > 1) {
        result.second_value = sorted_values[1].first;
        result.second_count = sorted_values[1].second;
    } else {
        result.second_value = -INF;
        result.second_count = 0;
    }

    return result;
}

Node e() {
    return {-INF, 0, -INF + 1, 0};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;
    vector<int> a(n);
    
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<Node> initial(n);
    
    for (int i = 0; i < n; ++i) {
        initial[i] = {a[i], 1, -INF, 0};
    }

    segtree<Node, op, e> seg(initial);

    for (int i = 0; i < q; ++i) {
        int qi;
        cin >> qi;
        
        if (qi == 1) {
            int p, x;
            cin >> p >> x;
            --p;
            seg.set(p, {x, 1, -INF, 0});
        } else {
            int l, r;
            cin >> l >> r;
            --l;
            Node res = seg.prod(l, r);
            cout << res.second_count << '\n';
        }
    }

    return 0;
}
