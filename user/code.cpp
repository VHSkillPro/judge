#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;

void Solve() {
    int n; cin >> n;
    vector<ll> a(n);
    for (auto &i: a) cin >> i;
    
    ld sum = 0;
    for (auto &x: a) {
        sum += log(x);
    }
    
    auto check = [&](ll base){
        return n * log(base) > sum;
    };
    
    ll l = 0, r = *max_element(a.begin(), a.end()) + 1;
    while (l + 1 < r) {
        ll m = (l + r) >> 1;
        if (check(m)) r = m;
        else l = m;
    }
    
    cout << r;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    
    int nTest = 1;
    // cin >> nTest;
    while (nTest--) {
        Solve();
        if (nTest > 0) {
            cout << "\n";
        }
    }
    return 0;
}